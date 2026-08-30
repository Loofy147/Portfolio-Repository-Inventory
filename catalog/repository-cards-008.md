# Repository Cards — Batch 008

**Inventory date:** 2026-08-30
**Scope:** descriptive repository/content census and reassessment. No strategic decisions.
**Rule:** README is descriptive evidence only; repository content is established from accessible tree/source/build/data surfaces.

## 1. `Loofy147/SpotUp-gg`
- Root contains an Android/Gradle application: `app/`, Gradle Kotlin build files, source tree, ProGuard configuration, and `metadata.json`.
- `metadata.json` identifies the application as SpotUp, a spontaneous local-activity coordination app, with a server-side Gemini capability.
- Repository size is non-trivial; this is an application implementation surface, not a README-only concept.
- Implementation depth and execution state remain unverified at this pass.
- Evidence: GitHub root tree and `metadata.json`.

## 2. `Loofy147/agentdit`
- Root contains architecture/roadmap material, agent registry and benchmark artifacts, a large market-data JSON, Playwright tests, package manifests, UI entrypoint and legacy surface.
- README describes a financial AI execution layer combining vectorized double-entry accounting, SAC reinforcement learning, evaluation/governance, and behavioral fingerprinting.
- The stated accounting invariant is `Assets - (Liabilities + Equity) = 0.0`; actual enforcement must be verified in source/tests.
- Performance claims such as sub-0.2ms inference remain claims pending independent benchmark verification.
- Evidence: root tree and README.

## 3. `Loofy147/Hbo`
- Root contains substantial Python source including `advanced_optimizers.py` (~50KB), HPO patch tooling, configs, Docker/Compose, examples, a production-system directory, requirements and a coverage artifact.
- This repository therefore has a real implementation/engineering surface even apart from README quality.
- Scientific/optimization purpose and actual execution coverage require source and test inspection.

## 4. `Loofy147/Learning-agent`
- Root contains Dockerfile, Alembic configuration/migrations, app/data directories, a ~1.5MB dataset file, image/learning-material surfaces, pytest configuration, and application files.
- It is a training/learning-system repository with persistent data and deployment-oriented structure, not a minimal agent placeholder.
- Exact model architecture and runtime state require deeper source inspection.

## 5. `Loofy147/Trading-app`
- Root contains a Vite/TypeScript application with `App.tsx`, components, services, types, `package.json`, `package-lock.json`, `tsconfig.json`, Vite configuration, metadata and an npm output log.
- This establishes a real frontend/application surface.
- The repository's relationship to other trading repositories remains unknown until implementation comparison.

## 6. `Loofy147/TGI-Market-Engine`
- README is only 19 bytes, but the root tree contains `README_IMPLEMENTATION.md`, BTC and gold historical Parquet datasets, `src/`, `tgi_engine/`, `scripts/`, `tests/`, and GitHub configuration.
- This is strong evidence that the repository contains a TGI/market implementation and data pipeline despite the extremely short README.
- It must therefore not be classified as empty or trivial from README size.
- Relationship to the wider TGI/FSO family remains a candidate relationship, not a final conclusion.

## 7. `Loofy147/Swarm-AGI`
- Root contains staged research directories `1_foundations`, `2_moonshot`, `3_deep_vision`, `4_the_legion`, and `5_experimental`, plus `main.py`, outputs, requirements, and a `Legion` artifact.
- The repository is organized as a multi-phase research/experimentation workspace.
- Its exact relation to other swarm/AGI repositories requires cross-repository source and history comparison.

## 8. `Loofy147/NeuraSynth`
- Root contains application/CSS material plus a substantial documentation corpus: complete architecture PDF/TXT, business model, implementation plan, executive summary, expansion proposals, launch/relations plan, legal contracts/templates and optimization/gap analysis.
- This is a combined product-design, architecture and implementation artifact repository.
- The size and documentation volume should not be interpreted as proof of completed implementation.

## 9. `Loofy147/Rationale-agent`
- Root confirms `.github`, benchmark documentation, discovery and MVP planning documents, Dockerfile, `enhanced_agent.py`, `mas/`, OpenAPI specification, `pyproject.toml`, pytest configuration, scripts, tests and docs.
- This is materially richer than the README alone suggested.
- The README's six-phase MAS concept is supported by structural artifacts, but phase completion still requires implementation-level verification.

## 10. `Loofy147/HOLONOMY-Protocol-`
- Root contains architecture and engineering roadmap documents, a large `SIGNATURE_MAP.json`, `agent_commerce/`, patch tooling, archive/assets/contracts/config/docs, and a `holonomy/` implementation directory.
- The repository is a protocol/system artifact with implementation, specification and governance surfaces.
- Further inspection is required to separate current implementation from archived/aspirational material.

## 11. `Loofy147/Spike-Function-Framework`
- Root contains deployment manual, executive pitch, future-domain plan, implementation checklist, patent claims, prototype deployment checklist, roadmap, an agent OS demo, app code, GitHub configuration, and an `.env` file committed to the repository.
- This is clearly more than a README prototype; it combines engineering, deployment, commercialization and IP-oriented material.
- The committed `.env` requires a separate security/provenance check to determine whether it contains actual secrets or placeholders; no conclusion is made here.
- Claims and patent language require evidence and legal review separately from technical inventory.

## 12. `Loofy147/density-intilegence-`
- Root contains `SOLUTION.md`, categorization/analysis scripts, `density_attn.py`, synthetic-data generation, Kaggle notebook, local validation, `main.py`, `metric.py`, `models.py`, and data/demo directories.
- The repository is a real ML/experimental surface despite a 22-byte README.
- It is particularly relevant to the portfolio's density/learning/attention line and should be compared with related ML repositories later.

## 13. `Loofy147/Free-Will-framework-` (reassessment note)
- Previous README-centric interpretation is insufficient. Root content includes extensive operational/research documents, status JSONs, audit reports and technical references.
- The `EXECUTIVE_SUMMARY.md` contains both implementation/test claims and explicit contradictions/limitations, including formal verification discrepancies and recommendations to fix issues before deployment.
- This repository should be represented by its artifact graph and implementation evidence, not by the strongest marketing-style claims.

## 14. `Loofy147/Global-theorem-` / `Global-structure-` (reassessment note)
- Both repositories expose substantial mathematical/implementation material around TGI/FSO rather than being documentation-only placeholders.
- `Global-theorem-` contains a Codex with numerous mathematical laws and claims; these are propositions requiring independent mathematical verification, not automatically established theorems.
- `Global-structure-` exposes implementation-oriented TGI/FSO material including core/research paths and deployment narratives.

## Reassessment result

The audit protocol is now explicitly:

`METADATA -> ROOT TREE -> BUILD/MANIFEST -> SOURCE -> TESTS/CI -> DATA/ARTIFACTS -> README/DOCS -> HISTORY`

A short README changes only the `README evidence` field. It does not reduce the expected inspection depth.

No repository decision is made in this batch.
