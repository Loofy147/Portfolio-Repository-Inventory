# Repository Inventory — Batch 036

Source: GitHub owner listing/search for Loofy147; inspection date: 2026-08-30.

## Newly/explicitly registered surfaces

| Repository | Observed identity / surface | Evidence level | Notes |
|---|---|---|---|
| `socials` | README-only observed; text is only `socials`. | minimal | Do not infer emptiness from README. |
| `Gptscraper` | GitHub contents endpoint reports repository empty on `main`. | current-empty | Current branch evidence only; history not assessed. |
| `DernAi` | README-only observed (`# DernAi`). | minimal | Identity unresolved. |
| `System-manifi` | README-only observed (`# System-manifi`). | minimal | Identity unresolved. |
| `X` | README-only observed (`# X`). | minimal | Identity unresolved. |
| `Guardian-Ai` | Decision-support platform for online optimization combining ML predictions with Learning-Augmented Algorithms; React frontend, FastAPI backend, PostgreSQL, Redis, Celery, Docker Compose. | substantial-description | Worst-case guarantee claim remains a claim until implementation/theory verification. |
| `new-math` | Micro-AGI probabilistic neuro-symbolic framework; five layers, ETBS, causal graph, SymPy, DEAP, NetworkX, Pydantic; README specifies symbolic/numeric simulation, verification, model zoo, correlation filtering and roadmap checks. | substantial-description | Mathematical formulations and AGI-readiness claims require independent verification. |
| `Intellectual-intelligence.-` | `Archon Prime V4` integration layer; app/docs/experiments/scripts/tests, prospecting/outreach/onboarding automation, Google Calendar integration, experiment tracking and CI. | substantial-description | Repository name does not match project identity; lineage/provenance should be preserved. |
| `nextjs-ai-chatbot` | `Chat SDK` / Next.js AI chatbot template with AI SDK, multiple model providers, Neon/Postgres, Vercel Blob, Auth.js. | substantial-description | README identifies it as a free open-source template; provenance/upstream status must be separated from local modifications. |
| `cognitive-dissonance` | Runnable POC with proposer/critic/evaluator/learner/meta-controller/safety-gate services, MLP core logic, MLflow registry, Prometheus and integration tests; Nemotron challenge tooling; README explicitly leaves true learner update, Kubernetes and broader adversarial tests open. | substantial-description | Strong candidate for lineage comparison with agent/reasoning and self-improvement systems. |
| `Rust-agents` | Rust multi-agent framework using hierarchical delegation: Orchestrator → SupervisorAgent → ExecutorAgent; ReAct execution; OpenAI and Mock LLMs; file, directory, shell and web tools; OpenTelemetry/Jaeger. | substantial-description | Arbitrary shell execution is part of the described tool surface; security boundary should be assessed later. |
| `Business-Operating-System` | AI-BOS architecture with gateway, executive agent, orchestration/event bus, agent kernel, specialist agents, tools, memory, intelligence/model routing, optimization, observation, governance/RBAC/HITL and replay. | substantial-description | Strong orchestration/governance lineage target. |
| `PraGma` | PRAGMA Agentic Coordination Layer on Solana; Anchor programs for registry/task/staking/fees, TypeScript SDK, simulations, tests, and 87-assertion validation suite. | substantial-description | Economic/security correctness remains to be independently validated. |
| `self-growing-machine` | Programmable Growing Neural Cellular Automaton: local MLP update rule, local perception, DNA signal, growth, self-maintenance, self-healing and multi-shape morphogenesis; training/verification scripts and Kaggle notebook. | substantial-description | Experimental outcomes require reproducible execution to promote claims. |
| `LightRAG` | Local repository README explicitly identifies LightRAG, links to HKUDS/LightRAG, describes RAG core/server, KG retrieval, multimodal integration, model/storage options and extensive project history. | provenance-critical | Treat as upstream/external project unless repository history proves local authorship/modification. |
| `Realizations-engine-` | README only: title `Realizations-engine-`. | minimal | Identity unresolved at current surface. |

## Important structural observations

1. `new-math` and `cognitive-dissonance` both contain explicit experimental/self-improvement semantics, but they are different architectural approaches and must not be merged conceptually from names alone.
2. `Business-Operating-System`, `Rust-agents`, and `Guardian-Ai` form potential reusable architecture clusters, but no merge/keep decision is made at census stage.
3. `Intellectual-intelligence.-` is an explicit identity mismatch: repository name vs `Archon Prime V4` README identity.
4. `nextjs-ai-chatbot` and `LightRAG` require provenance separation because their own README text identifies them as template/upstream software.
5. `Gptscraper` is recorded as current-empty rather than generally empty.

## Census status

This batch is additive only. No repository-level disposition (`KEEP`, `MERGE`, `EXTRACT`, `FREEZE`, `ARCHIVE`) is assigned here.