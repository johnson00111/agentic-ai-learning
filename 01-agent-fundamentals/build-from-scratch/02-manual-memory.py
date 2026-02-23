"""
02 - Manual Memory Management
手動管理 memory：實作不同策略的對話歷史管理
"""
import os
from openai import OpenAI
from collections import deque

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ConversationBuffer:
    """Buffer Memory：保留完整對話歷史（但限制總 token 數）"""
    
    def __init__(self, max_tokens=4000):
        self.messages = []
        self.max_tokens = max_tokens
        self.current_tokens = 0
    
    def add_message(self, role: str, content: str, token_count: int):
        """加入訊息，如果超過限制就移除最舊的"""
        self.messages.append({"role": role, "content": content})
        self.current_tokens += token_count
        
        # 簡單策略：如果超過限制，移除除第一則（system prompt）外最舊的
        while self.current_tokens > self.max_tokens and len(self.messages) > 2:
            removed = self.messages.pop(1)  # 保留 index 0 (system)
            # 估算 removed token（簡單算法：字數 / 4）
            removed_tokens = len(removed["content"]) // 4
            self.current_tokens -= removed_tokens
    
    def get_messages(self):
        return self.messages


class ConversationWindow:
    """Window Memory：只保留最近 N 輪對話"""
    
    def __init__(self, k=5):
        self.messages = []
        self.k = k  # 保留最近 k 輪對話
    
    def add_message(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        
        # 保留 system prompt + 最近 k 輪
        if len(self.messages) > (self.k * 2 + 1):
            # 移除最舊的 user-assistant pair
            self.messages = [self.messages[0]] + self.messages[-(self.k*2):]
    
    def get_messages(self):
        return self.messages


class SummaryMemory:
    """Summary Memory：定期總結舊對話"""
    
    def __init__(self, client, summary_threshold=10):
        self.client = client
        self.messages = []
        self.turn_count = 0
        self.summary_threshold = summary_threshold
        self.summary = ""
    
    def add_message(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        self.turn_count += 1
        
        # 每 N 輪總結一次
        if self.turn_count >= self.summary_threshold:
            self._summarize()
            self.turn_count = 0
    
    def _summarize(self):
        """把舊對話總結成一段摘要"""
        conversation_text = "\n".join([
            f"{m['role']}: {m['content']}" 
            for m in self.messages[:-2]  # 保留 user 剛輸入的
        ])
        
        summary_prompt = f"""請將以下對話總結成簡短摘要（100字內）：

{conversation_text}
"""
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": summary_prompt}]
        )
        
        self.summary = response.choices[0].message.content
        # 重置 messages，只保留 summary + 最近對話
        self.messages = [
            {"role": "system", "content": f"先前對話摘要：{self.summary}"},
            *self.messages[-2:]  # 保留最後的 user input
        ]
    
    def get_messages(self):
        return self.messages


def demo_agent_with_memory(memory_class):
    """使用指定 memory strategy 的 agent"""
    agent = memory_class(client)
    
    # 加入 system prompt
    agent.add_message("system", "你是一個 helpful assistant")
    
    print(f"🤖 Agent ({memory_class.__name__}): 哈嘍！輸入 'exit' 結束\n")
    
    while True:
        user_input = input("👤 你: ")
        if user_input.lower() == 'exit':
            break
        
        # 加入訊息
        agent.add_message("user", user_input)
        agent.add_message("assistant", "")  # 佔位
        
        # 取得回覆
        response = client.chat.completions.create(
            model="gpt-4",
            messages=agent.get_messages()
        )
        
        assistant_msg = response.choices[0].message.content
        print(f"🤖 Agent: {assistant_msg}\n")
        
        # 更新記憶
        agent.messages[-1]["content"] = assistant_msg


if __name__ == "__main__":
    print("選擇 memory strategy:")
    print("1. ConversationBuffer (token-based)")
    print("2. ConversationWindow (round-based)")  
    print("3. SummaryMemory (summarization-based)")
    
    choice = input("輸入數字 (1-3): ")
    
    strategies = {
        "1": ConversationBuffer,
        "2": ConversationWindow,
        "3": SummaryMemory
    }
    
    if choice in strategies:
        demo_agent_with_memory(strategies[choice])
    else:
        print("無效選擇")

"""
💡核心觀念：
1. LangChain 的 Memory classes 本質就是這些策略的封裝
2理解這些，你就能客制自己的 memory 策略
3. 關鍵問題：context window 有限時，如何決策丟棄什麼
"""
