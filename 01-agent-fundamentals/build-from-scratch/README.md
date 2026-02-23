# Build Agent from Scratch

學習如何不用 high-level library（如 LangChain），直接用 OpenAI API 從零建構 Agentic Agent。

## 核心概念

- **直接呼叫 API**: 使用 `openai.ChatCompletion.create()` 而非 wrapper library
- **手動管理對話**: 自己維護 message history
- **ReAct Pattern**: Reasoning → Acting → Observing
- **Function Calling**: 讓 LLM 能呼叫外部工具

##檔案結構

```
build-from-scratch/
├── README.md
├── 01-basic-chat-loop.py          # 最基礎的對話迴圈
├── 02-manual-memory.py            # 手動管理 message history
├── 03-react-pattern.py            # ReAct pattern 實作
└── 04-function-calling.py         # 加入 function calling 能力
```

##前置需求

```bash
pip install openai python-dotenv
```

##快速開始

從 `01-basic-chat-loop.py` 開始，逐步理解 agent 的核心機制。

##參考資源

- [OpenAI API Documentation](https://platform.openai.com/docs/introduction)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
