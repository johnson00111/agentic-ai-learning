# Agentic AI Learning

A structured learning journey into AI agent systems — from single-agent fundamentals to multi-agent orchestration and dynamic agent generation.

This repo documents my hands-on exploration of the agentic AI landscape, including paper reviews, framework comparisons, and experiment notes. The goal is to build a solid foundation for designing and implementing production-ready multi-agent systems.

## 🎯 Learning Outcome

Everything learned here feeds into my main project: **[ai-agent-office](https://github.com/johnson00111/ai-agent-office)** — a general-purpose framework that dynamically generates AI teams for any industry.

## 📚 Contents

| Topic | Description | Status |
|-------|-------------|--------|
| [01-agent-fundamentals](./01-agent-fundamentals/) | ReAct pattern, tool use, memory, single-agent design | Ongoing |
| [02-multi-agent](./02-multi-agent/) | Multi-agent collaboration, AutoGen vs CrewAI, orchestration patterns | Not started |
| [03-local-llm](./03-local-llm/) | Running Qwen3 locally via Ollama, free GPU setup (Colab/Kaggle + ngrok) | Not started |
| [04-papers](./04-papers/) | Paper reading notes with analysis | 🔲 Not started |
| [resources.md](./resources.md) | Curated list of courses, papers, repos, and tools | 🔲 Not started |

## 📄 Paper Reading List

| Paper | Key Takeaway | Notes |
|-------|-------------|-------|
| ReAct (Yao et al., 2022) | Reasoning + Acting loop as core agent pattern | [→ notes](./04-papers/react.md) |
| MetaGPT (Hong et al., 2023) | SOP-driven multi-agent software development | [→ notes](./04-papers/metagpt.md) |
| ChatDev (Qian et al., 2023) | Virtual software company with role-playing agents | [→ notes](./04-papers/chatdev.md) |
| AgentVerse (Chen et al., 2023) | Dynamic agent recruitment for emergent collaboration | [→ notes](./04-papers/agentverse.md) |
| Generative Agents (Park et al., 2023) | Observation-planning-reflection architecture for believable agents | [→ notes](./04-papers/generative-agents.md) |

## 🛠 Framework Comparison

| Framework | Best For | Dynamic Agent Creation | License |
|-----------|----------|----------------------|---------|
| AutoGen | Multi-agent conversation | ✅ via code | MIT |
| CrewAI | Role-based task pipelines | ✅ via config | MIT |
| LangGraph | Custom stateful workflows | ✅ full control | MIT |
| Microsoft Agent Framework | Production enterprise apps | ✅ graph-based | MIT |

Detailed comparison: [→ 02-multi-agent/framework-comparison.md](./02-multi-agent/framework-comparison.md)

## 📍 Roadmap

See [ROADMAP.md](./ROADMAP.md) for the full 5-week learning path and PoC timeline.

## 📖 Key Resources

**Courses (Free)**
- [AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) — DeepLearning.AI
- [AI Agentic Design Patterns with AutoGen](https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/) — DeepLearning.AI

**Repos**
- [microsoft/autogen](https://github.com/microsoft/autogen) — Multi-agent framework
- [geekan/MetaGPT](https://github.com/geekan/MetaGPT) — Multi-agent software company
- [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) — Communicative agents for software dev
- [QwenLM/Qwen3](https://github.com/QwenLM/Qwen3) — Open-source LLM with strong agent capabilities

**Docs**
- [Ollama](https://ollama.com) — Local LLM runtime
- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [LangChain Documentation](https://python.langchain.com/)
