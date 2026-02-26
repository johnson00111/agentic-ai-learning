"""
03 - ReAct Pattern Implementation
實作 ReAct (Reasoning + Acting) Pattern：讓 Agent 能思考並採取行動
"""
import os
import json
import re
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ReActAgent:
    """
    ReAct Agent: 結合 Reasoning（思考）和 Acting（行動）
    Pattern: Thought → Action → Observation → Thought → ...
    """
    
    def __init__(self):
        self.messages = []
        self.system_prompt = """你是一個 ReAct Agent。面對問題時，請依照以下格式思考：

Thought: [你的思考過程]
Action: [你要採取的行動]
Observation: [行動結果]
Thought: [根據觀察的新思考]
...

可用工具：
- search: 搜索資訊（參數: {"query": "搜索關鍵詞"}）
- calculate: 計算數學（參數: {"expression": "數學式"}）
- final_answer: 給出最終答案（參數: {"answer": "答案"}）

當你準備好回答時，使用 final_answer 工具。
"""
        self.messages.append({"role": "system", "content": self.system_prompt})
        
        # Mock 工具執行
        self.tools = {
            "search": self.mock_search,
            "calculate": self.mock_calculate,
            "final_answer": self.final_answer
        }
        self.last_observation = ""
    
    def mock_search(self, query: str) -> str:
        """模擬搜索工具"""
        mock_results = {
            "Tokyo population": "Tokyo 人口約 1400 萬",
            "Apple CEO": "Apple CEO 是 Tim Cook",
            "Python release date": "Python 1.0 於 1991 年發布"
        }
        return mock_results.get(query, f"搜索 '{query}' 的結果：模擬資料")
    
    def mock_calculate(self, expression: str) -> str:
        """模擬計算工具"""
        try:
            # 安全評估簡單數學
            result = eval(expression, {"__builtins__": {}}, {})
            return str(result)
        except:
            return f"無法計算：{expression}"
    
    def final_answer(self, answer: str) -> str:
        """最終答案"""
        return f"Final Answer: {answer}"
    
    def parse_action(self, text: str):
        """從 LLM 輸出解析 action 和參數"""
        action_match = re.search(r'Action:\s*(\w+)\s*\{([^}]*)\}', text)
        if action_match:
            action_name = action_match.group(1)
            params_str = action_match.group(2)
            try:
                params = json.loads("{" + params_str + "}")
                return action_name, params
            except:
                return action_name, {"raw": params_str}
        return None, None
    
    def run(self, query: str, max_steps: int = 5):
        """執行 ReAct 循環"""
        print(f"🤖 ReAct Agent: 處理查詢「{query}」")
        print("-" * 50)
        
        self.messages.append({"role": "user", "content": query})
        
        for step in range(max_steps):
            # 1. 取得 LLM 回覆
            response = client.chat.completions.create(
                model="gpt-4",
                messages=self.messages
            )
            
            content = response.choices[0].message.content
            print(f"\n📝 Step {step + 1}:\n{content}\n")
            
            # 2. 解析 Action
            action, params = self.parse_action(content)
            
            if action and action in self.tools:
                # 3. 執行工具
                if action == "final_answer":
                    result = self.tools[action](**params)
                    print(f"✅ {result}")
                    return result
                else:
                    result = self.tools[action](**params)
                    observation = f"Observation: {result}"
                    print(f"🔍 {observation}")
                    
                    # 4. 加回對話
                    self.messages.append({"role": "assistant", "content": content})
                    self.messages.append({"role": "user", "content": observation})
            else:
                # 沒有行動，只是思考
                self.messages.append({"role": "assistant", "content": content})
        
        print("⚠️ 達到最大步驟限制")
        return "未能在限制步驟內完成"


def demo():
    """Demo ReAct Agent"""
    agent = ReActAgent()
    
    # 測試問題
    queries = [
        "What is the population of Tokyo divided by 2?",
        "Who is the CEO of Apple and what year is it now?"
    ]
    
    for query in queries:
        print("\n" + "=" * 60)
        agent.run(query)
        agent.messages = [agent.messages[0]]  # 重置但保留 system prompt


if __name__ == "__main__":
    demo()

"""
💡核心觀念：
1. ReAct = Reasoning（思考）+ Acting（行動）+ Observation（觀察）
2. LLM 決定何時使用工具、使用什麼工具
3. Observation 結果會加回對話，影響下次思考
4. 這就是 LangChain AgentExecutor 的核心原理
"""
