# Repository Cards — Batch 011

Date: 2026-08-30
Scope: structural/content scan; no strategic decisions.

| Repository | Observed surface | Concise description | Knowledge status |
|---|---|---|---|
| Loofy147/Ai | `.github`, `backend`, `client`, `vscode-extension`, minimal README | Multi-surface AI application/repo with backend, client, and VS Code extension components. The README is insufficient to identify exact product purpose. | STRUCTURALLY IDENTIFIED; purpose still partial |
| Loofy147/agentic-apis | README + `categories`, `data`, `scripts` | Agentic API/catalog style repository with categorized data and supporting scripts. Exact implementation depth requires directory inspection. | PARTIAL |
| Loofy147/autonomous-manifold-v2-analysis | `agents`, multiple `autonomous_manifold_v*.py`, `cgce.py`, config, 81KB log, v4 state + improvement report | Research/implementation workspace around autonomous manifold versions, agents, monitoring and state evolution; contains substantial implementation and runtime artifacts. | D2 TARGET |
| Loofy147/Swarm-AGI | numbered research stages `1_foundations`…`5_experimental`, `Legion`, `main.py`, outputs, requirements | Research program organized as staged foundations → moonshot → deep vision → legion → experimental work, with executable code and outputs. | D2 TARGET |
| Loofy147/Guardian-Ai | Dockerfile/Compose, frontend, `guardian_ai`, `main.py`, performance profiler, pytest config, release config | Full-stack AI/guardian application with Python core plus frontend/containerization/testing/release surfaces. | D2 TARGET |
| Loofy147/All-in-Ai | tests, `ai-agents`, `api-gateway`, architecture, audit report, CI/testing strategy, feature branches | Multi-component AI platform scaffold; current default ref is `phase-0-initial-setup`, indicating an explicit staged implementation path. | D2 TARGET |
| Loofy147/orbit-agent | multiple large Python implementations, agents metadata, benchmarks, episode logs, extracted code/kernels/meta, merged variants | Agent experimentation repository with multiple implementations/merged variants plus execution logs and extracted artifacts. Strong candidate for internal lineage analysis. | D2 TARGET + lineage |
| Loofy147/new-AGI | ARC inspector, FSUN baseline, competition submission, data, episteme, legacy, NeuroGolf production script | Broad AGI/ARC research workspace containing competition tooling, baselines, data, legacy material and a production-named model script. | D2 TARGET |
| Loofy147/ai-chatbot | Next-style app structure, `app`, components/hooks, Drizzle config, articles/artifacts, CI-related files | Substantial AI chatbot application with web UI, persistence/schema tooling and artifact area. | D2 TARGET |
| Loofy147/outonomos-system | extensive API/system/deployment/feature/implementation documentation + Docker | Highly documented autonomous/outonomous system with API, deployment, implementation guides and enhancement roadmap surfaces; implementation depth needs source-tree inspection. | D2 TARGET |
| Loofy147/Workflows-academy | client/server/shared, package.json, 259KB pnpm lock, platform structure, analysis, ideas, patches | Full-stack workflow/education platform with substantial lockfile, client/server/shared architecture and patch/ideas documentation. | D2 TARGET |
| Loofy147/dyad-algerian-builder- | devcontainer, cursor config, CI, Husky, lint/format configs, env example, contribution docs | Large Algerian-focused builder/development environment with strong repository engineering/tooling surface. | D2 TARGET |
| Loofy147/Taskflow | `src/App.tsx`, components/layouts/pages/router/services/store/types, extensive root artifacts | Full web application surface for task/workflow management; contains implementation, documentation and many generated design artifacts. | D2 TARGET |
| Loofy147/Genieune | methodology/data strategy, technical report, model `.pt` files, analysis JSON, app.py, model implementation, Kaggle deploy script | ML/model repository with actual PyTorch artifacts, methodology, analysis results and deployment tooling. Artifact validity/provenance must be checked separately. | D2 TARGET + artifact audit |
| Loofy147/Spike-Function-Framework | `.env`, env template, CI directory, deployment/implementation checklists, patent claims, demo/app code | Function/agent framework with deployment and implementation documentation. Presence of a committed `.env` is a security/provenance signal; contents were intentionally not inspected or reproduced. | D2 TARGET + SECURITY REVIEW |
| Loofy147/Rust-agents | Cargo manifest/lock, architecture/checklists/reports/risk register/roadmaps | Rust-based agent system with explicit architecture, compliance, engineering and risk-management documentation. | D2 TARGET |
| Loofy147/Maintenance-life | API/architecture/checklist/developer guide, Dockerfile, benchmarks, security/contribution docs | Large maintenance-oriented engineering system with API and architecture documentation, Docker and benchmarking surfaces. | D2 TARGET |
| Loofy147/vO_trading_donors | Next-style app/components/hooks/lib, component config, multiple dashboard screenshots, feature documentation | Trading/product dashboard implementation with UI components and substantial design artifacts. Exact strategy/engine requires source inspection. | D2 TARGET |
| Loofy147/HCA/HCA-Reasoner | app.py, model_hca.py, requirements, data/docs/experiments/hca package, HF upload script | HCA contains a real reasoner subproject with model/application code, data/experiments and model publication tooling, beyond the repository-level checkpoint artifacts. | D2 TARGET |

## Important observations

- `Ai`, `agentic-apis`, `new-AGI`, and several agent repositories cannot be classified reliably from README alone.
- `orbit-agent` contains multiple implementation generations and extracted artifacts; this is potentially valuable for chronology/lineage reconstruction.
- `new-AGI` explicitly retains `legacy`, so historical implementations are part of the repository surface and should not be discarded from the inventory.
- `Genieune` has both a 4.2MB model artifact and a second 30-byte `.pt` artifact; these must not be treated as equivalent model deliverables.
- `Spike-Function-Framework` has a committed `.env` file. Treat this as a security finding to investigate, without exposing secret values.
- `HCA-Reasoner` confirms that the HCA repository is a container for a substantive subproject, not merely a model checkpoint store.

No repository in this batch receives KEEP/MERGE/EXTRACT/FREEZE/ARCHIVE status.
