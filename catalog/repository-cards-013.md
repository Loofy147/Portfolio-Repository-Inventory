# Repository Cards — Batch 013

Date: 2026-08-30
Scope: census continuation with structural inspection; no strategic decisions.

## Loofy147/Workflows-n8n-builder-
Observed root: `.env.example`, `AGENTS.md`, `ARCHITECTURE.md`, README, `backend/`, `frontend/`, `infrastructure/`, `templates/`. README describes an Algerian AI workflow platform with multi-agent orchestration, event-driven execution, cloud/local LLM gateway, zero-trust authorization and workflow SBOM generation. The root structure confirms backend/frontend/infrastructure separation and deployment-oriented material. These are declared/structural capabilities, not yet runtime proof.
Knowledge: STRUCTURALLY IDENTIFIED; implementation verification open.
Evidence: root tree + README.

## Loofy147/Ai-is-clever
Observed root: Dockerfile, `SKILL_REGISTRY_JSON.json`, `datasets.csv`, `harvest/`, Hugging Face/Kaggle upload scripts, `hiro_agent/`, a zipped `hiro-agent-source-code.zip`, `industrial_demo.py`, `rebuild_self.py`, `rebuild_self_v2.py`, `restore_agent.py`, and `thoughts.json`. Despite a 14-byte README, the repository contains an agent implementation/artifact ecosystem with multiple rebuild/restore scripts and external publication tooling. The presence of both source directory and source ZIP makes artifact/provenance comparison relevant.
Knowledge: STRUCTURALLY IDENTIFIED; lineage/artifact relationship open.
Evidence: root tree.

## Loofy147/PraGma
README identifies PRAGMA as an agentic coordination and labor-market protocol on Solana. Root contains Anchor configuration, Rust/Cargo lockfiles, protocol strategy HTML, validation scripts, distribution/token scripts, docs, simulations and tests. The README specifies on-chain registry/task/staking/fees programs, a TypeScript SDK, economic simulations and integration tests. Validation claims are repository-reported until the test suite and on-chain programs are inspected.
Knowledge: D2 TARGET; protocol/implementation audit open.
Evidence: root tree + README. fileciteturn139file0 fileciteturn146file0

## Loofy147/negative-space
Observed root: `.github`, `.jules`, `AGENTS.md`, `CHANGELOG.md`, Dockerfile, `SYSTEM_AUDIT.md`, `TECHNICAL_DOCS.md`, `backend/`, `frontend/`, `nsp/`, `changes.diff`, and docker-compose. README is only `# negative-space`. This is therefore a substantive system repository with explicit audit/technical documentation and backend/frontend/infrastructure surfaces. Purpose must be established from those artifacts rather than the README title.
Knowledge: STRUCTURALLY IDENTIFIED; semantic/source audit open.
Evidence: root tree + README. fileciteturn140file0 fileciteturn147file0

## Loofy147/Kaggriculture
Observed root: 25KB README plus extensive research material: `COMPARATIVE_BENCHMARK_v1.md`, `REPORT_MINIMAL_INTERVENTION_v2.md`, `RESEARCH_META_OBSERVER_v1.md`, multiple `RESEARCH_REPORT_v*.md` generations and AGENTS guidance. The repository is clearly a research/evaluation workspace with versioned research reports and benchmark material. Domain semantics and executable surfaces require deeper tree inspection.
Knowledge: D2 TARGET; research lineage important.
Evidence: root tree. fileciteturn141file0

## Loofy147/meta-secure-framework
Observed root: threat-model documents, configuration, `knowledge_hub.json`, Python packaging (`pyproject.toml`, `setup.py`, requirements), `sacef/`, `examples/`, `scripts/`, `tests/`, and GitHub configuration. This is an implementation-oriented security framework with explicit threat-model and test surfaces. The exact security mechanisms remain to be established from source.
Knowledge: D2 TARGET; security implementation audit open.
Evidence: root tree. fileciteturn142file0

## Loofy147/methodology-explorer
Observed root: client/server/shared architecture, Drizzle configuration and migrations, component configuration, package.json, 325KB pnpm lockfile, `patches/`, `todo.md`, and README. This is a full-stack methodology exploration application, not a documentation-only repository. The shared dependency/tree similarity with `leverscan-app` is notable at the structural level and should be compared later, but is not classified as lineage here.
Knowledge: STRUCTURALLY IDENTIFIED; relationship/provenance comparison open.
Evidence: root tree. fileciteturn143file0

## Loofy147/device-activity-tracker
README and root establish a Node/TypeScript + React security-research application for RTT-based activity inference from WhatsApp/Signal delivery behavior. Root includes Docker, frontend/client, `src/`, package manifest and `.env.example`. The README explicitly attributes the underlying research to Gegenhuber et al. and links to an external source repository for installation context. Thus both technical implementation and external-research provenance matter. Quantitative/security claims require source and experimental verification.
Knowledge: D2 TARGET + provenance/security research.
Evidence: root tree + README. fileciteturn144file0 fileciteturn148file0

## Loofy147/School-
README identifies "Jomra" / "جمرة", an educational systems-engineering platform teaching a nine-layer top-down method from business vision through AI, UX, compliance, security and implementation. Root also contains `PIPELINE_DESIGN.md`, `PROJECT_SUMMARY.md`, `ROADMAP.md`, `book/`, `capstone/`, and `website/`, confirming that the repository combines curriculum, project artifacts and website material rather than a single application core.
Knowledge: STRUCTURALLY IDENTIFIED + educational/system artifact.
Evidence: root tree + README. fileciteturn145file0 fileciteturn149file0

## Loofy147/leverscan-app
Observed root: 42KB README, client/server/shared, Drizzle schema/migrations, package manifest/322KB pnpm lockfile, `references/`, `patches/`. README describes a React 19 + Tailwind 4 + Express + tRPC + Manus Auth + database template with Vitest coverage and a schema/router/db build loop. The repository is strongly template/framework-shaped. Its relationship to `methodology-explorer` is a comparison target because both expose shared directory names and identical blob SHAs for some framework configuration files, but no lineage decision is made.
Knowledge: STRUCTURALLY IDENTIFIED; provenance/template analysis open.
Evidence: root tree + README. fileciteturn150file0 fileciteturn157file0

## Loofy147/new-math
README describes Micro-AGI / Atlas Edition: five-layer probabilistic neuro-symbolic architecture, ETBS, symbolic reasoning, genetic self-evolution, model zoo, active sampling and a production-roadmap checklist. It also defines mathematical metrics and provides `unittest` and demo execution commands. The README contains many theoretical/formal claims; those must be separated from implemented equations and empirical evidence.
Knowledge: D2 TARGET; mathematics/claim verification open.
Evidence: README. fileciteturn152file0

## Loofy147/researchers
README identifies a Mathematical Frameworks Analysis Suite v5.3 with `src/math_unification/`, analysis/clustering/Q-score modules, synthesis and adversarial analysis, and a runnable `main.py`. The repository is therefore a computational research/synthesis engine rather than merely a document collection. Methodological validity and Q-score semantics require later code/data review.
Knowledge: D2 TARGET; research-method audit open.
Evidence: README. fileciteturn153file0

## Loofy147/SIE
README identifies a curriculum/verification system implementing ingest → sandboxed execute → vetting gate → registry, with SQLite lesson storage, tests and an MCP adapter. It reports four vetted lessons, including real git execution and artifact validation. This is directly relevant to the portfolio's evidence/verification lineage, but the stated lesson results remain repository evidence until the scripts/tests are re-executed independently.
Knowledge: D2 TARGET; evidence/verification lineage target.
Evidence: README. fileciteturn154file0

## Loofy147/Dz-blockchain
Root contains a short README, a `dz-blockchain/` directory and a 43KB `dz_blockchain_rust.rs.txt` artifact. This is not an empty repository despite the tiny README. The `.rs.txt` artifact suggests a Rust implementation or specification stored as text; nested directory and file contents are required before its exact nature can be described.
Knowledge: PARTIALLY IDENTIFIED; nested/source inspection open.
Evidence: root tree. fileciteturn155file0

## Loofy147/nextjs-ai-chatbot
README identifies this as the Chat SDK / Next.js AI chatbot template with App Router, AI SDK, multi-provider gateway, Neon Postgres, Vercel Blob and Auth.js. The repository is explicitly presented as a reusable open-source template, so provenance and local modifications matter before treating it as original portfolio work.
Knowledge: PROVENANCE REVIEW + STRUCTURALLY IDENTIFIED.
Evidence: README. fileciteturn156file0

## Batch observations

1. `Ai-is-clever` demonstrates that a tiny README can hide multiple implementation generations, packaged source and model-publication tooling.
2. `PraGma`, `meta-secure-framework`, `SIE`, `new-math`, `researchers`, and `device-activity-tracker` represent distinct evidence types: protocol implementation, security framework, empirical verification pipeline, theoretical AI system, mathematical analysis engine, and security research application.
3. `methodology-explorer` and `leverscan-app` are now explicit structural comparison targets because both use client/server/shared + Drizzle + patches and share some configuration blob SHAs. That is a clue, not a lineage conclusion.
4. `negative-space` and `Dz-blockchain` must not be downgraded because their READMEs are short; their root trees prove additional content.
5. `School-` is primarily a curriculum/system-engineering artifact with book/capstone/website components, not just a school application.

No strategic KEEP/MERGE/EXTRACT/FREEZE/ARCHIVE decision is assigned in this batch.
