# Repository Cards — Batch 017

Inspection date: 2026-08-30
Purpose: descriptive census only. No strategic decision is assigned here.

## 1. Larouine
- Observed surface: `.github`, `configs`, `docs`, `prototypes`, `hisham/`, `STATE_OF_THE_HELIX.md`, two shell setup/fix scripts, empty `main.py` and empty `requirements.txt`, plus a small `project_analysis.pdf`.
- Current interpretation: Helix-related experimental/research workspace with structural scaffolding, documentation and prototypes; the source depth is not yet established.
- Important evidence: a Helix state document and explicit repair/setup scripts indicate project evolution artifacts beyond README-level description.
- Unknowns: child-directory contents, PDF content, history and relation to other Helix repositories.
- Review state: `D2-structure-plus-artifacts`.

## 2. Youcef-app
- Observed surface: Next.js-style application with `app`, `components`, `hooks`, `lib`, `public`, `styles`, `package.json`, `pnpm-lock.yaml`, Tailwind and Next configuration.
- Current interpretation: actual web application surface, not a placeholder.
- Unknowns: business purpose, server/API behavior and test/deployment status require source inspection.
- Review state: `D2-structurally-identified`.

## 3. Fln
- Observed surface: effectively a v0/Vercel-synced frontend repository; root also includes the same broad Next/Tailwind-style application scaffolding and a 140KB pnpm lockfile.
- README explicitly states it is automatically synced with a v0.dev deployment called `Frontend design`.
- Current interpretation: generated/deployed frontend surface rather than a canonical standalone product repository.
- Unknowns: exact local modifications and relationship to other v0-generated application repositories.
- Review state: `provenance-and-lineage-review`.

## 4. End-to-end-ecosystem-
- Observed surface: README describes a NEXUS AI Orchestrator with `NexusOrchestrator`, `AgentManager`, abstract `Agent`, `MathAgent`, `RLAgent` and `ExecutionAgent`; also mentions related TuberOrchestratorAI and EulerNet code in the same repository.
- Important implementation note: README itself acknowledges that `ExecutionAgent` uses unsandboxed `exec()` and is insecure for production.
- Current interpretation: multi-agent orchestration prototype combining routing, math, RL and code execution, with related project material co-located.
- Unknowns: actual tree beyond the documented source names, test execution results, and provenance of included related projects.
- Review state: `D2-candidate`.

## 5. Zebra
- Observed surface: README describes a Dockerized multi-service prototype implementing an `Observe → Analyze → Suggest` pipeline, with telemetry, Jaeger, causal inference and Shadow LLM components.
- Current interpretation: self-governing/self-improving AI systems prototype with explicit observability and analysis architecture.
- Important evidence constraint: the README's claims of mathematical guarantees are not treated as established by the description alone.
- Unknowns: implementation depth, tests, causal-engine details and mathematical guarantee evidence require source/docs inspection.
- Review state: `D2-candidate`.

## 6. Larouine / Helix lineage signal
- `STATE_OF_THE_HELIX.md`, `prototypes/`, configuration and repair tooling make Helix a lineage candidate.
- No repository relationship is asserted until cross-repository tree/history comparison is performed.

## 7. Census hygiene note
Some repositories identified in this batch were already present in earlier descriptive lists under different search ordering. They are only reclassified here when new structural evidence changes what is known; no strategic decision is introduced.

## 8. Global note for this batch
No KEEP/MERGE/EXTRACT/FREEZE/ARCHIVE decision is made. Candidate relationships and provenance signals remain non-decisional until coverage and cross-repository comparison are complete.
