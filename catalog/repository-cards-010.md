# Repository Cards — Batch 010

Date: 2026-08-30
Scope: structural/source-surface review; no strategic decisions.

## Loofy147/Fusion-Engine
Observed surface: README is only 15 bytes, but the repository contains a substantial specification corpus: `FUSION_ENGINE_SPEC.md`, `FusionEngine.md`, `FusionEngine v4.md`, `FusionEngine_v4_1_Architecture_Spec.md`, `TECHNICAL_SPEC_v4.md`, `TECHNICAL_REVIEW_v4_4.md`, multiple Python engine implementations, and `edge_case_tests.py`. There are explicit v4.1/v4.2 variants and duplicated filenames with identical blob SHA for some review/spec artifacts. This strongly suggests an iterative engineering/specification lineage inside one repository, but does not establish whether the variants are canonical, generated, or experiments. Evidence: GitHub root tree inspection.
Status of knowledge: STRUCTURALLY IDENTIFIED; implementation and historical lineage not yet fully audited.

## Loofy147/Taskflow
Observed surface: repository contains substantial application structure and analysis artifacts. Root includes `COMPREHENSIVE_ANALYSIS.md`, many generated image artifacts, and the `src/` tree. `src/` contains App.tsx plus components, layouts, lib, pages, router, services, store and types. This is an implemented frontend/application surface rather than a README-only project. Evidence: root and `src/` tree inspection.
Status of knowledge: STRUCTURALLY IDENTIFIED; product semantics and backend/dependency surfaces require further inspection.

## Loofy147/Discovery-engine-
Observed surface: README is 19 bytes, but the repository contains multiple substantive Python modules: `advanced_modules.py`, duplicated `(1)` variant, AIMO gateway/inference/submission scripts, `aimo_kernel/`, `apex_v2.py` (~121 KB), `bundled_system.py` (~159 KB), and additional modules beyond the returned tree window. The naming shows several AIMO submission/gateway variants and a large bundled system. This is a strong indicator of iterative experimentation and/or successive packaging, but no conclusion about canonical version is made yet.
Status of knowledge: STRUCTURALLY IDENTIFIED; high need for source/history comparison.

## Loofy147/NeuraGrid
Observed surface: root contains a very short README, a `PITCH_DECK.md` (~8 KB), and a `neurogrid-demo/` directory. Therefore the repository is not empty, but its executable scope cannot be inferred from the root alone.
Status of knowledge: PARTIALLY IDENTIFIED; nested implementation surface remains to be inspected.

## Loofy147/Maintenance-life
Observed surface: extensive engineering/documentation surface including `API.md`, `ARCHITECTURE.md`, `CHECKLIST.md`, `DEVELOPER_GUIDE.md`, `SECURITY.md`, `ROADMAP.md`, Dockerfile, GitHub workflows, and benchmarks, in addition to README. This is a maintained engineering-style repository surface with explicit API/architecture/development governance documentation. The current evidence does not by itself establish runtime completeness.
Status of knowledge: STRUCTURALLY IDENTIFIED; implementation/runtime audit remains open.

## Loofy147/Genieune
Observed surface: repository contains methodology/data strategy/Hugging Face documentation, technical report, application code (`app.py`, `genuine_model.py`), a 4.2 MB PyTorch model artifact, a second `v2_2` model file with only 30 bytes, `analysis_results.json`, and deployment tooling (`deploy_kaggle.sh`). The coexistence of v2.1/v2.2 artifacts and analysis results is important provenance evidence. The 30-byte v2.2 artifact must not be interpreted as a valid trained model without inspecting its contents/history.
Status of knowledge: STRUCTURALLY IDENTIFIED; model provenance and execution validation remain open.

## Loofy147/HCA
Observed surface: root contains an `HCA-Reasoner` subtree, checkpoints, Kaggle material, and a PyTorch artifact `hca_tiny_reasoner_v1_final.pt`. The nested HCA-Reasoner tree contains its own README, `app.py`, `model_hca.py`, data/docs/experiments/hca directories, requirements, and upload tooling. This is a repository containing both experiment/model artifacts and an implementation subtree; it should not be treated as a single homogeneous application.
Status of knowledge: STRUCTURALLY IDENTIFIED; nested module relationships remain open.

## Loofy147/Payment-managment
Observed surface: root contains a 19-byte README and a `payment_gateway/` directory. The directory existence proves more than a README-only project, but its implementation surface has not yet been inspected deeply enough to describe the gateway itself.
Status of knowledge: PARTIALLY IDENTIFIED; nested inspection required.

## Loofy147/Rust-agents
Observed surface: root includes `.github`, `ARCHITECTURE.md`, `CHECKLIST.md`, `COMPLIANCE_CHECKLIST.md`, `DETAILED_REPORT.md`, `ENGINEERING_CHECKLIST.md`, `EXECUTIVE_SUMMARY.md`, `QUARTERLY_ROADMAP.md`, `RISK_REGISTER.md`, `ROADMAP.md`, `Cargo.toml`, and a large `Cargo.lock`. The project therefore has a Rust implementation/dependency surface plus explicit engineering, compliance, and risk documentation. README is not the sole source of project meaning.
Status of knowledge: STRUCTURALLY IDENTIFIED; source tree and actual agent implementation require deeper inspection.

## Loofy147/vO_trading_donors
Observed surface: root contains platform documentation plus a real Next.js-style application surface: `app/`, `components/`, `hooks/`, `lib/`, Next configuration, TypeScript declarations, and multiple dashboard screenshots. This is an implemented UI/platform surface with design evidence, not merely a concept document. Exact trading functionality and backend semantics remain to be inspected.
Status of knowledge: STRUCTURALLY IDENTIFIED; implementation/claim verification open.

## Loofy147/Founders-
Observed surface: README is 11 bytes and root contains `autodeploy-engine/`. This repository may function as a container/umbrella around the nested deployment engine rather than a standalone implementation at root. Nested tree and provenance remain uninspected.
Status of knowledge: PARTIALLY IDENTIFIED; do not classify as empty.

## Review rule reinforced by this batch
A short README, small repository metadata size, or minimal root description is not evidence of minimal repository substance. The inventory must inspect nested trees and artifacts before any absence claim is recorded.
