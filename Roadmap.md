# AI Office — Learning Path & PoC Timeline

## Project Vision

Build a **general-purpose AI Office framework** that can:
- Dynamically generate AI agents for any role/industry via a Meta-Agent
- Auto-detect missing positions and create new agents on the fly
- Fill knowledge gaps through web search and RAG
- Be demonstrated with multiple industry examples (e.g., software company, marketing agency)

## Tech Stack (100% Free)

| Layer | Tool | License |
|-------|------|---------|
| Agent Framework | AutoGen / Microsoft Agent Framework | MIT |
| LLM | Qwen3-8B (via Ollama) | Apache 2.0 |
| Local Runtime | Ollama | MIT |
| Free GPU | Google Colab / Kaggle + ngrok | Free tier |
| Web Search | DuckDuckGo (`duckduckgo-search`) | Free |
| RAG / Vector DB | LangChain + ChromaDB | MIT |
| Interface | Gradio / Open WebUI | Free |

## GitHub Deliverables

| Repo | Purpose | Audience |
|------|---------|----------|
| `ai-office` | Main project — production-quality code, architecture docs, demo | Recruiters, hiring managers, open-source community |
| `ai-agent-learning` | Learning notes, paper reviews, tech comparisons | Shows learning ability and technical depth |

---

## Phase 0 — Environment Setup (Day 1–2)

**Goal:** Get all tools running, confirm the free GPU pipeline works.

- [ ] Install Python 3.10+, Git, VS Code
- [ ] Install Ollama locally (even on weak hardware, just to understand the tool)
- [ ] Set up Google Colab notebook: Ollama + Qwen3-8B + ngrok
- [ ] Verify API endpoint works: `curl https://xxxx.ngrok-free.app/v1/chat/completions`
- [ ] Set up Kaggle notebook as backup (more stable, 30 hrs/week free GPU)
- [ ] Create both GitHub repos with initial README
- [ ] Register ngrok free account, get authtoken

**Learning Resources:**
- Ollama official docs: https://ollama.com
- GitHub reference: `amin-tehrani/ollama-colab` (Colab + ngrok template)
- Qwen3 on Ollama: https://ollama.com/library/qwen3

**Learning Repo Output:** `03-local-llm/colab-ollama-setup.md`

---

## Phase 1 — Single Agent Fundamentals (Day 3–7)

**Goal:** Understand how one agent works — LLM + Instruction + Tools + Memory.

### Study
- [ ] Watch: DeepLearning.AI — *AI Agents in LangGraph* (free, ~3 hrs)
- [ ] Watch: DeepLearning.AI — *AI Agentic Design Patterns with AutoGen* (free, ~2 hrs)
- [ ] Read: ReAct paper (Yao et al., 2022) — understand Reasoning + Acting loop
- [ ] Read: AutoGen official docs — focus on `ConversableAgent`, `AssistantAgent`

### Practice
- [ ] Build a simple single agent with AutoGen + Qwen3 (via Colab API)
- [ ] Add tool use: connect DuckDuckGo search as a tool
- [ ] Add memory: make the agent remember context across turns
- [ ] Test: give the agent a role (e.g., "You are a PM") and verify it stays in character

### Key Concepts to Master
- System prompt design for role assignment
- Function calling / tool use with open-source models
- ReAct loop: Thought → Action → Observation → Repeat
- How AutoGen connects to OpenAI-compatible APIs (Ollama endpoint)

**Learning Repo Output:** `01-agent-fundamentals/`

---

## Phase 2 — Multi-Agent Collaboration (Day 8–14)

**Goal:** Understand how multiple agents talk, coordinate, and divide work.

### Study
- [ ] Read: MetaGPT paper — *Meta Programming for A Multi-Agent Collaborative Framework*
- [ ] Read: ChatDev paper — *Communicative Agents for Software Development*
- [ ] Read: AgentVerse paper — *Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors* (focus on dynamic agent recruitment)
- [ ] Explore: AutoGen GroupChat and GroupChatManager source code

### Practice
- [ ] Build a 3-agent software team: PM → Architect → Engineer (hard-coded workflow)
- [ ] Evolve to GroupChat: let agents discuss freely
- [ ] Experiment with message routing: who speaks next? how to prevent chaos?
- [ ] Compare: try the same task with CrewAI — note differences from AutoGen

### Key Concepts to Master
- Agent communication patterns: sequential, broadcast, selective
- Role boundary design: what should each agent know and NOT know
- Orchestration: hard-coded steps vs. dynamic conversation
- Failure handling: what happens when agents disagree or loop

**Learning Repo Output:** `02-multi-agent/`

---

## Phase 3 — Meta-Agent Design (Day 15–21)

**Goal:** Build the core innovation — an agent that creates other agents.

### Design
- [ ] Define Meta-Agent's system prompt: analyze user's company description → output role list
- [ ] Design role template schema (JSON): name, system_prompt, tools, skills
- [ ] Design orchestration logic: how does Meta-Agent decide the workflow for generated agents
- [ ] Plan knowledge gap detection: when should an agent trigger web search or RAG

### Build
- [ ] Implement Meta-Agent: takes "I want to start a marketing agency" → generates agent configs
- [ ] Implement dynamic agent instantiation: convert JSON configs into live AutoGen agents
- [ ] Implement GroupChat with dynamically created agents
- [ ] Add DuckDuckGo search tool to all agents
- [ ] Add basic RAG with ChromaDB for domain knowledge storage

### Test Scenarios
- [ ] Scenario 1: "Build me a software development company" → PM, Architect, Senior Dev, Junior Dev, QA
- [ ] Scenario 2: "Build me a digital marketing agency" → Strategist, Content Writer, SEO Specialist, Designer
- [ ] Scenario 3: "Build me a research lab" → PI, Literature Reviewer, Data Analyst, Writer

**AI Office Repo Output:** First working prototype in `src/`

---

## Phase 4 — Constraint Loop & Quality (Day 22–28)

**Goal:** Add constraint-based iteration so output quality is production-worthy.

### Build
- [ ] Define evaluation constraints per industry (e.g., for software: "code must pass linter")
- [ ] Implement constraint evaluation agent: reviews output, provides pass/fail + feedback
- [ ] Implement retry loop: if constraints not met → send feedback back → agents iterate
- [ ] Add human-in-the-loop (HITL): user can review and redirect at key checkpoints

### Polish
- [ ] Add logging: track full agent conversation history
- [ ] Add configuration file: users can customize roles, constraints, tools via YAML/JSON
- [ ] Write unit tests for Meta-Agent and agent instantiation logic
- [ ] Create `docker-compose.yml` for one-click local setup (big portfolio bonus)

**AI Office Repo Output:** Stable, testable version with constraint loop

---

## Phase 5 — Documentation & Portfolio Polish (Day 29–35)

**Goal:** Make the GitHub repos recruiter-ready.

### AI Office Repo (`ai-office`)
- [ ] Record demo video or GIF showing the system in action
- [ ] Write README.md (English):
  - One-line description + demo GIF at top
  - Features list
  - Architecture diagram (use Mermaid or draw.io)
  - Quick Start guide
  - Tech Stack table
  - Examples section (link to 2+ industry demos)
  - Future Work
- [ ] Write `docs/architecture.md`: detailed design decisions and trade-offs
- [ ] Write `docs/setup-guide.md`: step-by-step including free GPU setup
- [ ] Add `README_zh.md` for Chinese readers
- [ ] Clean up code: consistent naming, docstrings, type hints
- [ ] Pin this repo on GitHub profile

### Learning Repo (`ai-agent-learning`)
- [ ] Write README.md: learning roadmap overview with links to each section
- [ ] Add paper reading notes with your own analysis (not just summaries)
- [ ] Add tech comparison notes (AutoGen vs CrewAI, Qwen3 model size comparison)
- [ ] Add `resources.md`: curated list of courses, papers, repos, tools
- [ ] Link to ai-office repo as "the project I built from this learning"

---

## Summary Timeline

| Week | Phase | Deliverable |
|------|-------|-------------|
| Week 1 (Day 1–7) | Setup + Single Agent | Environment running, first agent with tools |
| Week 2 (Day 8–14) | Multi-Agent | 3-agent team working, paper notes done |
| Week 3 (Day 15–21) | Meta-Agent (Core) | Dynamic agent creation working, 3 demo scenarios |
| Week 4 (Day 22–28) | Constraints + Quality | Iteration loop, HITL, tests, Docker |
| Week 5 (Day 29–35) | Polish + Ship | README, demo video, portfolio-ready |

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Colab GPU session expires mid-work | Use Kaggle as backup (30 hrs/week); save checkpoints to Google Drive |
| Qwen3-8B quality not enough for multi-agent | Use Qwen3-14B quantized, or mix: Meta-Agent on larger model, workers on 8B |
| AutoGen being deprecated for Microsoft Agent Framework | Learn AutoGen first (simpler), code is migration-compatible; switch later if needed |
| Agent conversations go chaotic in GroupChat | Start with hard-coded sequential workflow, gradually loosen to dynamic chat |
| ngrok free tier URL changes on restart | Set up ngrok static domain (free); or use Cloudflare Tunnel as alternative |

---

## Stretch Goals (After PoC)

- [ ] Add MCP (Model Context Protocol) support for richer tool integration
- [ ] Web UI dashboard showing agent organization chart and real-time conversation
- [ ] Support multiple LLM backends (Qwen3 for Chinese tasks, Llama for English tasks)
- [ ] Benchmark: compare output quality across different model sizes
- [ ] Write a blog post / Medium article about the project (extra visibility)