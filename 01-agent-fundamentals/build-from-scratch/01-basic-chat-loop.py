"""
01 - Basic Chat Loop
最基礎的對話迴圈：直接用 OpenAI API 建立簡單的 chat agent
"""
import os
from openai import OpenAI

# 初始化 client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def simple_chat_agent():
    """最基本的 chat agent：維護對話歷史並持續對話"""
    messages = []
    
    print("🤖 Agent: 哈嘍！我是你的 basic chat agent（輸入 'exit' 結束）\n")
    
    while True:
        # 取得用戶輸入
        user_input = input("👤 你: ")
        
        if user_input.lower() == 'exit':
            print("🤖 Agent: 拜拜！")
            break
        
        # 加到 message history
        messages.append({"role": "user", "content": user_input})
        
        # 直接呼叫 OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
        
        # 取得回覆
        assistant_message = response.choices[0].message.content
        print(f"🤖 Agent: {assistant_message}\n")
        
        # 把 assistant 回覆也加入 history（關鍵！）
        messages.append({"role": "assistant", "content": assistant_message})


if __name__ == "__main__":
    simple_chat_agent()

"""
💡核心觀念：
1. 自己管理 messages 陣列，這就是 agent 的「記憶」
2. 每次 API call 都要傳完整的對話歷史
3. 沒有 LangChain 的 Memory class，但原理一模一樣
"""
