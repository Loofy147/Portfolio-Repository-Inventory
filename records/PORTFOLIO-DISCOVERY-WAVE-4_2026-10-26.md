# Portfolio Discovery Wave 4 — 2026-10-26

**Portfolio source of record:** `Loofy147/Portfolio-Repository-Inventory`
**Observed source ref:** `main@125c52c554fb59a3845aa7816ac8ffdf6ff94657`
**Related Deter-agent review frontier:** `spec/deterministic-control-hardening@c3a34b2dff64fb8590c6bae1f8b74f2ac8225e8f`
**Review depth:** D1/D2 selective inspection: README, architecture and assumption documents, named experiment receipts, selected decisions, and CI metadata. No complete test suites were executed except where an existing GitHub Actions result is cited.

## Findings

### 1. MORPHS: real read-only external API call with bounded capability binding

- Repository: [Loofy147/MORPHS](https://github.com/Loofy147/MORPHS)
- Observed ref: `main@861090a38141e89c7a3bf4d6eeb6c816fcf9b5f2`
- Inspected: `README.md`, `experiments/043c/result.json`, `.github/workflows/verify.yml`, and Actions run/artifact metadata.
- Current-HEAD CI: [run 37648832580](https://github.com/Loofy147/MORPHS/actions/runs/37648832580) completed successfully on the observed HEAD. The workflow includes Experiments 028–043c and uploads `morphs-043c-runtime-receipt`; the artifact registry reports 869 bytes and digest `sha256:a8929fd3739ec67bfb549b771f14e7e21bdb41937efff7a7915b6d2e6bd8f284`.
- The checked-in 043c `result.json` records an earlier runtime receipt, run 253 at commit `9fb25681c6c821e823f66f038e2327f3a9166098`. The current workflow/artifact confirms another passing run, but this review did not independently download and compare the artifact bytes or rewrite the historical result file.
- Observed capability scope: a real public GitHub read operation with a read-only host-injected token, bound capability/invoker, exact commit resolution before two read surfaces, content/Git blob identity checks and a persisted receipt.
- Explicit limits: provider independence, cryptographic receipt authenticity, independent CI attestation, arbitrary API/provider generalization, mutation semantics, ambiguous mutation recovery and production-grade capability registration remain unestablished.

**Disposition:** high-value experiment/reference for runtime receipts and least-privilege external read adapters. Do not claim independent trust or production readiness from the receipt alone.

### 2. Software-res: evidence contract for AI-generated software changes

- Repository: [Loofy147/Software-res](https://github.com/Loofy147/Software-res)
- Observed ref: `main@138a6be19fe4e4bcd008df2e7ba33588b31ca863`
- Inspected: README, `docs/ARCHITECTURE.md`, `docs/ASSUMPTIONS_AND_OPEN_QUESTIONS.md`, and Actions metadata.
- Described mechanism: evidence manifests and JSON Schema; a fail-closed collector/validator; a non-compensatory reliability vector; deterministic `AUTO_MERGE`, `REVIEW`, or `REJECT` decisions; local signing/verification proofs; controlled fixtures and policy-mutation tests.
- Limitations documented by the project: production SLSA builder trust and key management, external-corpus execution, independent ground-truth labels, calibrated thresholds and general software-reliability claims are not included.
- The latest inspected successful workflow was on an older commit, `d9cc00976efe4cebe8821b20e7904ab5fcd0da9a`, not this observed main HEAD. Therefore the current HEAD is **not CI-verified by this review**.

**Disposition:** candidate CI evidence adapter. Compare its artifact/evidence contract to Deter-agent's existing promotion gate before adopting any code or adding a second authority.

### 3. Algeria AI Product Fabric: document-to-quote-to-decision workflow

- Repository: [Loofy147/algeria-ai-product-fabric](https://github.com/Loofy147/algeria-ai-product-fabric)
- Observed ref: `main@b3545b83b1592a54a839932adfe9c0f74a8fe2bb`
- Inspected: README, `domains/procurement/README.md`, and Actions metadata.
- Described workflow: `Document → Quote → Decision → Evidence`; reusable document identity/evidence anchoring and decision lifecycle reside in the shared core, while procurement vocabulary and quote-specific policy live in the domain composition.
- Stated quote boundary: positive total, non-negative delivery period, at least one evidence anchor and no deterministic policy violation; violations result in `needs_review`, not approval.
- Open issue: page-level provenance mapping and the optional document parser adapter need production-level review. The latest observed successful CI was on older commit `fc9047a59ee1c3775400393f21a040fe538bd4e8`, so this pass does not claim current-HEAD CI success.

**Disposition:** candidate application vertical for evidence-bearing procurement and local business workflows; do not duplicate its domain rules in a universal runtime or transfer a quote into an approved business commitment automatically.

### 4. Bounties: independent security-research evidence workflow

- Repository: [Loofy147/Bounties](https://github.com/Loofy147/Bounties)
- Observed ref: `main@da2baad1efe39d928f69e8a5400b7e7762447759`
- Inspected: README and current-objective summary.
- Described workflow: target selection, scope snapshots, hypotheses, reproduction, audit maps, evidence packages, submissions and recorded outcomes. The lifecycle distinguishes `RECONNAISSANCE`, `HYPOTHESIS`, `REPRODUCED`, `IN-SCOPE`, `SUBMITTED`, `ACCEPTED`, `PAID`, and `REJECTED`.
- The README records specific hypothesis reversals after source and live-state inspection. This is a useful pattern for preserving negative findings rather than promoting plausible claims into findings.
- Scope: security research must remain within each program's current authorization and disclosure rules. A hypothesis or reproduced issue is not the same as an accepted/paid finding.

**Disposition:** treat as an outcome/evidence workflow, not a general software dependency. Potentially useful to the overall contribution model because it shows how submitted work, evidence, scope and acceptance differ.

### 5. Compute Qualification Infrastructure: a documented KILL decision

- Repository: [Loofy147/Compute-Qualification-Infrastructure](https://github.com/Loofy147/Compute-Qualification-Infrastructure)
- Observed ref: `main@38964f3cd0e021b53b112001faaff3e10cb3bc8c`
- Inspected: README and `decisions/final/2026-08-31-KILL.md`.
- Decision: KILL the investigated standalone compute-qualification product—not because the technical problem is unreal, but because the proposed underserved product wedge, defensibility and buyer willingness-to-pay did not clear the evidence gate.
- Preserved value includes market/competitor research, an evidence ledger, falsification criteria, and distinctions between benchmarked, qualified and production-approved claims.
- Reopen condition: a materially new opportunity charter and fresh commercial evidence, rather than simply rebranding the same idea.

**Disposition:** preserve as negative strategic knowledge. Do not add product code or restart the business build without new buyer evidence.

### 6. FSO/TGI: mathematical and combinatorial research candidates

- [Global-theorem-](https://github.com/Loofy147/Global-theorem-): `main@b5616f3045d85080ed80dbba492094732e63cb95`
- [Global-structure-](https://github.com/Loofy147/Global-structure-): `main@5f56b300cbf7287507e75991d7bb0217fe670403`
- [Fiber-Stratified-Optimization (FSO)](https://github.com/Loofy147/-Fiber-Stratified-Optimization---FSO-): `main@315039c9340b80ade89cfd93d583da4483687eea`
- Inspected: Global-theorem and Global-structure READMEs; FSO README at the observed ref contains only a heading. The portfolio's pre-existing `TGI-FSO-HAG` cluster is explicitly a candidate cluster, with commit lineage and theorem/test correspondence still required.
- Research value to test: discrete construction algorithms, symmetry/quotient reduction, parity obstructions, theorem fixtures and benchmark comparisons.
- Limits: statements about universal intelligence, complexity improvement or broad cross-domain applicability are project claims until definitions, assumptions and reproducible results establish them. A test run or self-authored theorem check is not an independent proof.

**Disposition:** research family only. First extract one precise theorem/algorithm, its assumptions, tested domain and baseline; do not transfer claims or declare code lineage by similarity.

## Cross-repository experiment candidates

### A. Verify a bounded external capability receipt
Use MORPHS's recorded GitHub read adapter as a reference for a narrow read-only action. Define exact scope, resolved commit, provider request identity, bytes/blob digest, trusted workflow identity and receipt version. Keep provider-originated content untrusted; a matching digest proves identity of bytes, not factual truth.

### B. Compare AI-code evidence gates
Compare Software-res' evidence manifest and risk-vector contract with Deter-agent's current promotion/evaluation contract. Build a translation/conformance test first. Do not combine policy engines or permit an evidence collector to authorize its own output.

### C. Turn the procurement vertical into a falsifiable product experiment
Use the Document → Quote → Decision → Evidence flow as a prototype hypothesis only when a real purchaser and an actual document workflow are identified. Measure extraction correction effort, evidence traceability, decision latency, and actual willingness to pay. Technical feasibility alone is not a product GO.

### D. Preserve negative decisions in all opportunity work
Reuse the Compute Qualification Infrastructure discipline: identify the unmet-gap gate, buyer, willingness-to-pay evidence, incumbent alternatives and explicit kill criteria before writing more product code.

### E. Formal research validation
For FSO/TGI candidates, select one narrowly stated mathematical claim and produce:
- precise definitions and domain bounds;
- proof obligations independent of implementation;
- exhaustive verification for tractable instances;
- counterexample search and property tests;
- a reproducible baseline/complexity comparison;
- a written result separating proven, experimentally supported, hypothesized and contradicted claims.

## Scope / non-claims

This is a selective research record, not a fresh repository census, a code-lineage assertion, an architecture merger, or proof that every README statement is true. The observed refs above are provenance pins for this review. No integration or production dependency was added by this record.
