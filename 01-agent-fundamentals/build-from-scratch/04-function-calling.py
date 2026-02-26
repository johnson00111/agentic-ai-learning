"""
04 - Function Calling (Tools)
使用 OpenAI Function Calling API 讓 Agent 能呼叫外部工具
"""
import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# 定義可用工具（functions 定義）
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "取得指定城市的當前天氣",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市名稱，如 Taipei, Tokyo, New York"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "溫度單位"
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "執行數學計算",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "數學運算式，如 '2 + 2' 或 '100 * 5'"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "搜索網路資訊",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索關鍵詞"
                    }
                },
                "required": ["query"]
            }
        }
    }
]


# 工具實作（實際應用中這些會呼叫真實 API）
def get_current_weather(location: str, unit: str = "celsius"):
    """模擬天氣 API"""
    mock_weather = {
        "Taipei": {"temperature": 25, "condition": "Sunny"},
        "Tokyo": {"temperature": 18, "condition": "Cloudy"},
        "New York": {"temperature": 15, "condition": "Rainy"}
    }
    weather = mock_weather.get(location, {"temperature": 20, "condition": "Unknown"})
    
    if unit == "fahrenheit":
        weather["temperature"] = weather["temperature"] * 9/5 + 32
    
    return weather


def calculate(expression: str):
    """安全計算"""
    try:
        # 移除危險字元，只允許數字和運算符
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            return {"error": "Invalid characters in expression"}
        
        result = eval(expression, {"__builtins__": {}}, {})
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}


def search_web(query: str):
    """模擬網路搜索"""
    return {"results": f"Mock search results for: {query}"}


# 工具映射
tool_functions = {
    "get_current_weather": get_current_weather,
    "calculate": calculate,
    "search_web": search_web
}


class FunctionCallingAgent:
    """
    使用 OpenAI Function Calling API 的 Agent
    這是現代 agent framework（如 LangChain）的核心機制
    """
    
    def __init__(self):
        self.messages = [{
            "role": "system",
            "content": "你是個 helpful assistant。當用戶需要外部資訊（天氣、計算、搜索）時，你應該使用提供的工具。"
        }]
    
    def run(self, user_input: str):
        """執行 agent 循環"""
        self.messages.append({"role": "user", "content": user_input})
        
        while True:
            # 1. 呼叫 API 並提供 tools 定義
            response = client.chat.completions.create(
                model="gpt-4",
                messages=self.messages,
                tools=TOOLS,
                tool_choice="auto"  # 讓模型決定是否使用工具
            )
            
            message = response.choices[0].message
            
            # 2. 檢查是否有 tool calls
            if message.tool_calls:
                # 加到 messages
                self.messages.append(message)
                
                # 3. 執行每個 tool call
                for tool_call in message.tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    
                    print(f"🔧 呼叫工具: {function_name}({function_args})")
                    
                    # 4. 執行函數
                    if function_name in tool_functions:
                        result = tool_functions[function_name](**function_args)
                        
                        # 5. 加回對話（tool 回覆）
                        self.messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "name": function_name,
                            "content": json.dumps(result)
                        })
                        print(f"📤 結果: {result}\n")
                    else:
                        print(f"⚠️ 未知工具: {function_name}")
                        
            else:
                # 沒有 tool calls，直接回覆
                assistant_response = message.content
                self.messages.append({"role": "assistant", "content": assistant_response})
                return assistant_response


def demo():
    """Demo function calling agent"""
    agent = FunctionCallingAgent()
    
    test_queries = [
        "台北今天天氣怎麼樣？",
        "請計算 (100 + 50) * 2",
        "搜索一下 OpenAI 的最新模型",
        "哈嘍，你是誰？"  # 不需要工具的問題
    ]
    
    for query in test_queries:
        print(f"\n{'='*60}")
        print(f"👤 用戶: {query}")
        print(f"{'='*60}")
        
        response = agent.run(query)
        print(f"🤖 Agent: {response}\n")
        
        # 重置對話
        agent.messages = [agent.messages[0]]


if __name__ == "__main__":
    demo()

"""
💡核心觀念：
1. tools 定義告訴 model「有什麼工具可用」和「參數格式」
2. model 自己決定何時使用哪個工具
3. tool_choice="auto" 讓模型決定，也可以強制要求使用特定工具
4. 這就是 ChatGPT plugins、LangChain Tools 的底層機制
5. 比 ReAct Pattern 更結構化，因為參數解析是自動的

🔑 關鍵差異：
- ReAct: 模型輸出文字，你手動解析 Action
- Function Calling: 模型輸出結構化 tool call，API 直接給你參數
"""
