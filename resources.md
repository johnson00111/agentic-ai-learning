# Curated Resources for Agentic AI

A growing collection of resources for building AI agent systems.
Updated as I progress through each learning phase.

> Resources marked with ⭐ are ones I've personally completed and found most valuable.
> Resources without ⭐ are on my reading/watch list.

---

## Courses

| Course | Platform | Duration | Status |
|--------|----------|----------|--------|
| [AI Agentic Design Patterns with AutoGen](https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/) | DeepLearning.AI | ~2 hrs | 🔲 Planned |
| [AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) | DeepLearning.AI | ~3 hrs | 🔲 Planned |

---

## Papers

| Paper | Year | Status |
|-------|------|--------|
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | 2022 | 🔲 Planned |
| [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) | 2023 | 🔲 Planned |
| [ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) | 2023 | 🔲 Planned |
| [AgentVerse: Facilitating Multi-Agent Collaboration](https://arxiv.org/abs/2308.10848) | 2023 | 🔲 Planned |
| [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | 2023 | 🔲 Planned |

---

## Frameworks & Tools

### Agent Frameworks
| Tool | Link | Notes |
|------|------|-------|
| AutoGen | [GitHub](https://github.com/microsoft/autogen) | Primary framework for this project |
| Microsoft Agent Framework | [GitHub](https://github.com/microsoft/agent-framework) | AutoGen successor, will evaluate later |
| CrewAI | [GitHub](https://github.com/crewAIInc/crewAI) | Alternative to compare against |
| LangGraph | [Docs](https://langchain-ai.github.io/langgraph/) | For custom stateful workflows |

### LLM & Inference
| Tool | Link | Notes |
|------|------|-------|
| Ollama | [ollama.com](https://ollama.com) | Local LLM runtime |
| Qwen3 | [GitHub](https://github.com/QwenLM/Qwen3) | Primary model — recommended for agent tasks |

### Free GPU Access
| Platform | GPU | Free Limit | Link |
|----------|-----|------------|------|
| Google Colab | T4 (15GB VRAM) | ~3-12 hrs/session | [colab.google](https://colab.research.google.com) |
| Kaggle | T4 x2 | 30 hrs/week | [kaggle.com](https://www.kaggle.com) |
| ngrok | — | 1 free tunnel | [ngrok.com](https://ngrok.com) |

---

## Reference Projects

| Project | Why I'm Studying It |
|---------|-------------------|
| [MetaGPT](https://github.com/geekan/MetaGPT) | Multi-agent software team with SOPs |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Role-playing agents for software dev |
| [OpenClaw](https://github.com/steipete/openclaw) | Personal agent with tool integration |

---

## Taxonomy

How different concepts in agentic AI relate to each other:

```
Agentic AI
├── Personal Assistants ─── OpenClaw, Siri
├── Coding Agents ───────── Claude Code, Cursor, Devin
├── Multi-Agent Collab ──── MetaGPT, ChatDev, CrewAI
├── Social Simulation ───── Generative Agents, AgentSociety
│
├── Agent Design Patterns
│   ├── Instruction-based (simple prompt)
│   ├── Hard-coded workflow (predefined steps)
│   ├── ReAct (reasoning + acting loop)
│   └── Constraint-based (iterate until constraints met)
│
└── Key Components
    ├── LLM (brain)
    ├── Tools (extend capabilities)
    ├── Memory (persist context)
    ├── Skills (lazy-loaded modules)
    └── HITL (human oversight)
```