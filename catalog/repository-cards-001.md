# Repository Cards — Batch 001

Date: 2026-08-30
Scope: repositories directly inspected during the current census pass.

Each card is intentionally short. It records what is currently established, not a final project judgment.

## 1. `Loofy147/Scraper`
**Summary:** Small frontend-oriented repository on branch `feat/developer-resources-explorer`. Root currently exposes `index.html` (~18KB) and `CardSkeleton.js`; no README was exposed in the inspected branch. This looks like a developer-resources explorer UI surface, but the full purpose should remain `UNKNOWN` until the HTML/JS implementation is inspected.
**Class:** app/UI prototype signal.
**Evidence:** root tree inspected.
**Knowledge:** observed, partial.

## 2. `Loofy147/Gptscraper`
**Summary:** Repository is empty at `main`; GitHub reports no repository contents.
**Class:** empty.
**Evidence:** GitHub empty-repository response.
**Knowledge:** observed, high confidence.

## 3. `Loofy147/socials`
**Summary:** Frontend repository with `src`, Vite, TypeScript, Tailwind, ESLint, package manifests and `.bolt`; README contains only the word `socials`. The implementation surface is non-empty, but intended product/function is not yet established from the inspected documentation.
**Class:** frontend application / prototype signal.
**Evidence:** root tree + README.
**Knowledge:** observed, partial.

## 4. `Loofy147/Bravolino`
**Summary:** Interactive educational platform for Algerian children aged 5–12, covering curriculum-oriented lessons, games, progress tracking, parent dashboards and teacher/school tooling. Root contains backend/frontend directories, documentation, a large dataset, and supporting media/artifacts.
**Class:** substantial product candidate / edtech.
**Evidence:** README + root tree.
**Knowledge:** observed, strong surface evidence; implementation depth still requires code/test inspection.

## 5. `Loofy147/Smart-bot`
**Summary:** Repository contains only a very small README (`# Smart-bot`) at the inspected revision. No substantive implementation was established in this pass.
**Class:** minimal / unknown.
**Evidence:** README + root tree.
**Knowledge:** observed.

## 6. `Loofy147/ClimateNow`
**Summary:** Current inspected branch exposes only a top-level `climatenow/` directory. No README or implementation contents were established in this pass.
**Class:** unknown / likely early-stage project.
**Evidence:** root tree.
**Knowledge:** observed, low-information.

## 7. `Loofy147/A-louer`
**Summary:** Algerian Sales Agent architecture for e-commerce reselling. Documentation explicitly defines scraper, database, API server, frontend, payment gateway and automated reselling engine. The data model defines products, sales, users and transactions; repository also contains substantial Jupyter notebooks.
**Class:** product/application prototype with detailed design artifacts.
**Evidence:** `ARCHITECTURE.md`, `DATA_MODEL.md`, root tree.
**Knowledge:** observed, strong design evidence; implementation/validation depth not yet established.

## 8. `Loofy147/gemini-cli`
**Summary:** Full-featured Gemini CLI repository containing extensive CI/tooling/configuration and documentation. Its README describes the open-source terminal AI agent, built-in tools, MCP support, GitHub integration and multiple authentication modes. The repository is substantial and operationally structured; relationship to upstream/origin history still needs explicit Git ancestry inspection before treating it as an original project versus a fork/derived codebase.
**Class:** external/derived software repository candidate; provenance review required.
**Evidence:** README + root tree + repository metadata.
**Knowledge:** observed; provenance classification pending.

## 9. `Loofy147/termux-alo`
**Summary:** Private repository on `master`, small (~82KB) according to the census metadata. No content surface was inspected in this pass.
**Class:** unknown.
**Evidence:** census metadata only.
**Knowledge:** observed metadata; function unknown.

## 10. `Loofy147/hichem-project`
**Summary:** Repository currently contains a single Arabic-named ZIP artifact holding Meta Orchestrator AI specifications/vision/architecture material. This is more accurately an artifact/archive of design work than a conventional implementation repository at the inspected revision.
**Class:** specification/archive artifact; likely related to Meta Orchestrator lineage.
**Evidence:** root tree.
**Knowledge:** observed, high confidence for current surface; ZIP contents not yet inspected.

## 11. `Loofy147/CloudCostGuard`
**Summary:** Go-based FinOps tool combining a Terraform-plan analysis CLI with a backend pricing service, PostgreSQL, GitHub PR comments, Docker Compose, end-to-end tests and Kubernetes deployment manifests. README defines a concrete workflow from Terraform plan to monthly cost delta.
**Class:** substantial developer-tool/product candidate.
**Evidence:** README.
**Knowledge:** strong product/architecture signal; implementation and CI results require direct inspection.

## 12. `Loofy147/studio`
**Summary:** Firebase Studio starter project using Next.js; README points directly to `src/app/page.tsx` and describes it as a starter rather than a finished product.
**Class:** starter/scaffold.
**Evidence:** README.
**Knowledge:** observed.

## 13. `Loofy147/training-home`
**Summary:** Repository is centered on training data and processing rather than a conventional application: a ~1.5MB JSONL dataset, `learning-materials/`, a processing script and GitHub metadata. This may be a research/training asset feeding other AI projects, but cross-repository use is not yet proven.
**Class:** dataset/training infrastructure candidate.
**Evidence:** root tree.
**Knowledge:** observed, partial.

## Batch observations

- `Gptscraper` is genuinely empty at the inspected revision; it should remain visible in the inventory rather than being silently omitted.
- `Bravolino`, `A-louer`, `CloudCostGuard` and `training-home` demonstrate why repository size alone is insufficient: each has a different kind of substance (product, design-heavy application, developer infrastructure, training data).
- `hichem-project` is a strong candidate for extracting historical design provenance because the repository is essentially a packaged Meta Orchestrator specification artifact.
- `gemini-cli` must be treated carefully because repository identity/provenance is distinct from implementation value; original-vs-derived status is a separate question.
- `termux-alo` and `ClimateNow` remain unknown rather than being assigned an invented purpose.
