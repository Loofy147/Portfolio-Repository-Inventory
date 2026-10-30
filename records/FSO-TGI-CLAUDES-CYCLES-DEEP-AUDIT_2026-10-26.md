# FSO/TGI and Claude's Cycles — Deep Audit

**Date:** 2026-10-26  
**Portfolio source of record:** \`Loofy147/Portfolio-Repository-Inventory\`  
**Portfolio parent:** \`main@1b4c21ea8c63945984fd138bab8323012bbe2813\`  
**Review depth:** D3 selective source, tests/CI, artifact-tree comparison, and related-repository analysis. No local execution of the source repositories was performed during this review; CI logs cited below were inspected.

## Executive disposition

Keep the graph-theoretic Claude's Cycles problem as the bounded mathematical core. Treat FSO/TGI as several distinct efforts until their relationships are proved: (1) Hamiltonian-decomposition algorithms, (2) a restricted fiber/column-uniform construction, (3) the much broader TGI claims, and (4) the proposed FSC agent-economy product.

The strongest finding is not that all the mathematics is wrong. The function-counting identity \(N_b(m)=m^{m-1}\varphi(m)\) has a valid direct counting proof under its stated definition. The failure is that the repository promotes restricted ansatz-level arguments and smoke tests into universal topological laws, while the implementations contain inconsistent verification conventions and simulated product behavior.

**Current disposition**
- **Retain:** graph model, cycle constructors, full-coordinate verifier, exact small-instance fixtures, and independently checkable experiments.
- **Re-scope:** parity obstruction as a claim about a clearly defined restricted column-uniform/step-size ansatz, unless a separate proof establishes a broader theorem.
- **Unverified:** the Closure Lemma as a universal decomposition-count theorem, “stateless O(1) routing” as actual network discovery, TGI as a general reasoning system, and economic/cryptographic claims of FSC.
- **Do not treat as production-ready:** the FSC escrow contract, reputation/staking features, routing, session-key, or HRR-based payment claims.

## Scope and provenance

### Repositories and observed refs

| Repository | Observed default-branch ref | Main inspected surfaces |
|---|---|---|
| [Global-theorem-](https://github.com/Loofy147/Global-theorem-) | \`main@b5616f3045d85080ed80dbba492094732e63cb95\` | \`core.py\`, \`fiber.py\`, \`solutions.py\`, \`theorems.py\`, \`docs/LAWS.md\`, \`research/cycles_even_m.py\`, CI workflow and run log |
| [Global-structure-](https://github.com/Loofy147/Global-structure-) | \`main@5f56b300cbf7287507e75991d7bb0217fe670403\` | \`core.py\`, \`solutions.py\`, \`theorems.py\`, \`cycles_even_m.py\`, \`pyproject.toml\`, CI workflow and run log |
| [-Fiber-Stratified-Optimization---FSO-](https://github.com/Loofy147/-Fiber-Stratified-Optimization---FSO-) | \`main@315039c9340b80ade89cfd93d583da4483687eea\` | \`FOUNDATIONS.md\`, \`THEORY.md\`, \`FSC_WHITEPAPER.md\`, \`fsc_core/*\`, \`contracts/TopologicalEscrow.sol\`, benchmark, status report |

External mathematical baseline: [Donald Knuth, “Claude's Cycles” (Stanford CS)](https://cs.stanford.edu/~knuth/papers/claude-cycles.pdf). Knuth's problem is to decompose the directed arcs of the graph on \(\mathbb{Z}_m^3\) into three directed Hamiltonian cycles. It is a combinatorics problem with an explicit graph and checkable success condition; a successful decomposition is not, by itself, evidence for a general-purpose intelligence architecture.

## Finding 1 — The graph problem and the restricted construction are conflated

The fiber map \(s=(i+j+k)\bmod m\) is a useful structural reduction: every permitted coordinate-increment arc moves from \(F_s\) to \(F_{s+1}\). The inspected \`fiber.py\` implementation restricts local assignments to depend on \((s,j)\), not the full vertex coordinates. That is a particular construction family, not the full set of possible vertex-to-permutation assignments.

The parity derivation in \`docs/LAWS.md\` depends on assumptions of the restricted form: each step component is coprime to even \(m\), hence odd, and the selected components sum to an even \(m\). Under those assumptions, the number of odd summands must be even. This argument does not establish that every Hamiltonian decomposition on the original graph has that form.

The broad statements “if \(m\) is even, \(k\) must also be even” and “the universe strictly requires a lift to \(k=4\)” exceed what the restricted argument proves. They should be stated only with explicit ansatz assumptions unless a separate general proof is supplied.

### Internal contradiction recorded on CI

In \`Global-structure-/theorems.py\`, the verification script reports both:
- “Even \(m\) + Odd \(k\) (3) is mathematically obstructed”, based on the \`extract_weights(...).h2_blocks\` predicate; and
- “\(m=4\) 3D sigma verified via full-coordinate search”, by checking the full-coordinate \`SOLUTION_M4\`.

The current-HEAD run [37953773568](https://github.com/Loofy147/Global-structure-/actions/runs/37953773568) logs both messages. Its test job succeeded; the publish-to-PyPI job failed and Docker deployment was skipped. The mathematical contradiction is therefore present in the repository's own verification narrative. The scope distinction is confirmed by an independent check of the stored \(m=4,k=3\) fixture. I parsed the 64 permutation indices from [solutions.py](https://github.com/Loofy147/Global-structure-/blob/5f56b300cbf7287507e75991d7bb0217fe670403/solutions.py) (blob SHA \(b7f92523bb773cbacda5f5df64b4cf65cc34d328\)), generated the six permutations of \(S_3\) in lexicographic order, and independently built each per-colour successor map using the documented edge-index \(\to\) colour convention. For each of the three colours, all 64 vertices had in-degree one; traversal from \(000\) visited 64 distinct vertices and returned to \(000\). **All three cycles passed.** This independently confirms a full-coordinate \(m=4,k=3\) decomposition and falsifies the blanket claim that even modulus universally requires even dimension. It does not falsify the narrower parity result for the restricted column-uniform construction.

Important qualification: the workflow's success status is not proof of every reported theorem. The verifier records booleans and prints “proved” messages; its exit status does not enforce that every returned result is true. A regression suite must assert the expected outcomes explicitly and independently.

## Finding 2 — The counting identity is sound; the broader cardinality theorem is not established by its checker

The identity
\[
N_b(m)=m^{m-1}\varphi(m)
\]
is correct for the stated set of functions \(b:\mathbb{Z}_m\to\mathbb{Z}_m\) whose sum is coprime to \(m\): fixing the first \(m-1\) values leaves the last value uniquely determined for each target sum modulo \(m\), giving \(m^{m-1}\) functions per residue and \(\varphi(m)\) coprime residues.

However, \`verify_moduli_space_laws()\` in \`Global-theorem-/theorems.py\` counts these \(b\)-functions for \(m=3\), then calculates the claimed decomposition count from the proposed formula \(\varphi(m)N_b(m)^{k-1}\). It does not independently enumerate full graph decompositions, establish a free group action, or prove that the solution set is a torsor. Checking that a formula evaluates to 648 is not an independent verification that exactly 648 decompositions exist.

**Required distinction:** valid function-counting lemma; unproved connection between that count and the space of Hamiltonian decompositions; unproved general Closure Lemma. These must be separate theorem statements with separate evidence and falsifiers.

## Finding 3 — \`Global-theorem-/core.py\` has a cycle-verifier convention mismatch and permissive stubs

At the observed ref, the search score machinery builds the inverse map from cycle colour to the selected arc using \`pa[permutation][colour] = arc_index\`. The solution documentation describes per-vertex permutations as \`arc → cycle\`. But \`verify_sigma()\` in \`Global-theorem-/core.py\` uses \`arc = p[c]\` instead of the inverse lookup \`p.index(c)\`. For the documented \`arc → cycle\` representation, the verifier follows the wrong arc for a given cycle colour.

Related scripts reuse the same direct-index convention, so a test calling that same logic is not an independent oracle. Establish one canonical representation and make the verifier and all constructors comply with it.

The end of the same file also defines compatibility stubs:
- \`verify_functional_graph(...): return True\`
- \`vertices(...): return []\`
- \`trace_cycle(...): return []\`
- \`arc_sequence(...): return []\`

These functions must not be used as valid verification or data-generation primitives. Replace false-success stubs with explicit \`NotImplementedError\` or complete implementations; add tests that fail if these stubs are invoked on a verification path.

By contrast, Global-structure-/core.py constructs a colour-to-arc inverse map, but its own connectivity loop does not explicitly assert in-degree one or that the traversal returns to its starting vertex after \(m^k\) steps. Therefore the helper alone is not a sufficiently strong oracle. The independent fixture check above supplies the stronger evidence for the stored \(m=4,k=3\) solution; use such a checker for every regression fixture.

## Finding 4 — CI green is not equivalent to core-math verification

- [Global-theorem- CI run 33179439601](https://github.com/Loofy147/Global-theorem-/actions/runs/33179439601) succeeded on the observed main SHA. The configured \`fso_ci.yml\` runs \`research/tests/test_tgi_agent.py\`, \`test_action_mapper.py\`, \`test_knowledge_mapper.py\`, and \`test_jules_integration.py\`. It does not run \`core.py\`'s verifier, \`theorems.py\`, the core spike test, or the standalone even-\(m\) decomposition script.
- [Global-structure- CI run 37953773568](https://github.com/Loofy147/Global-structure-/actions/runs/37953773568) ran the script-level “theorem verification”, synthesis verification, and universal ingestor checks. The test job passed, but the run then failed at PyPI publication; Docker deployment was skipped. The theorem script itself reports contradictory scopes and does not force an all-results-true exit condition.
- The FSO repository's observed tree has 35 file blobs and no test files or GitHub Actions workflow. Its \`README.md\` is only a title line. The substantial claims mainly live in prose and demos rather than a reproducible test contract.

Do not use workflow-green badges as proof of mathematical claims unless the workflow demonstrably executes an independent test for the exact claim.

## Finding 5 — FSO/FSC application code is a conceptual mock, not the advertised production protocol

Several source-level behaviors are materially narrower than the whitepaper/status claims:

- \`fsc_core/routing.py\`: \`hash_capabilities()\` uses Python's built-in \`hash(tuple(capabilities_vector))\`, not a canonical stable capability identifier. For string-valued capabilities, Python hash randomization makes cross-process identity unsuitable as a stable registry key. \`route_request()\` returns a descriptive string; it does not query a registry, choose a live provider, or return a traversable path. The benchmark times this calculation against a worst-case list scan, not equivalent service-discovery workloads.
- \`fsc_core/tgi.py\`: the “inference” engine calculates a fourth coordinate from a sum and returns a success flag. No graph traversal, evidence-backed deduction, semantic validation, or theorem proof occurs in that method.
- \`fsc_core/negotiation.py\`: proposals contain random noise. The “session key” is a built-in Python hash of an FFT-derived tuple, not an authenticated, cryptographically secure key-establishment protocol.
- \`fsc_core/resonance.py\`: cosine similarity can measure vector alignment, but a threshold of 0.85 is not a mathematical proof of task correctness or human intent. The code has no external ground-truth validator or adversarial calibration.
- \`fsc_core/optimization.py\`: simulated annealing updates a randomly chosen scalar score using random \(-1,0,+1\) steps; it does not represent a Hamiltonian decomposition or calculate a graph-derived objective.
- \`fsc_core/staking.py\`: balances are an in-memory Python dictionary and \`release_escrow()\` returns a string; it does not transfer funds.
- \`contracts/TopologicalEscrow.sol\`: the code explicitly simulates the oracle by calculating \`keccak256(promptVectorHash, workVectorHash) % 101\`, then treats that number as a resonance score. It does not calculate HRR cosine similarity or verify submitted work. Since a worker chooses \`workVectorHash\`, they can search offline for a hash that clears the threshold; the score is not an independent quality oracle. A failure status can also trigger a stake penalty. Do not deploy this contract with real funds.

These are implementation facts, not judgments about whether an eventual production design could solve the underlying problems. They are sufficient to reject the current implementation as evidence for the whitepaper's production/security claims.

## Finding 6 — Cross-repository copies are evidenced; Git ancestry and direction are not

Blob-SHA comparison across the observed \`Global-theorem-\` and \`Global-structure-\` trees found byte-identical non-empty files at different paths, including:
- \`research/cycles_even_m.py\` ↔ \`cycles_even_m (2).py\`
- \`research/discovery_engine.py\` ↔ \`discovery_engine (3).py\`
- \`research/global_structure.py\` ↔ \`global_structure (1).py\`
- \`research/global_structure_paper.pdf\` ↔ \`global_structure_paper.pdf\`
- \`research/k4_m4_search.py\` ↔ \`k4_m4_search.py\`
- \`research/moduli_theorem.py\` ↔ \`moduli_theorem.py\`
- \`research/odd_m_solver.py\` ↔ \`odd_m_solver.py\`
- \`research/paper2_methodology.pdf\` ↔ \`paper2_methodology.pdf\`
- \`research/reformulation_engine.py\` ↔ \`reformulation_engine.py\`
- \`research/weighted_moduli_pipeline_v2.py\` ↔ \`weighted_moduli_pipeline_v2.py\`

This proves those file contents are identical at the observed refs. It does not, by itself, establish which repository copied from which, the author/date of the copy, or common Git ancestry.

The trees also contain checked-in interpreter artifacts: 53 \`.pyc\` files in the inspected Global-theorem tree and 55 in Global-structure. Global-structure contains byte-identical root and \`src/tgi_manifold/core.py\` copies. These increase drift and audit risk and should be cleaned up under a separate hygiene change. Do not infer the mathematical result from the compiled artifacts.

## Next controlled work

1. **Freeze the graph contract.** Define a vertex as a \(k\)-tuple in \(\mathbb{Z}_m^k\), each vertex's permutation as an explicit direction (prefer documented edge-index \(\rightarrow\) colour), and each colour successor as a derived map. Document arc-disjointness and Hamiltonicity invariants.
2. **Create an independent verifier.** Check every vertex has exactly one valid permutation; for each colour build successors from inverse lookup; check in-degree one for every vertex; traverse from a fixed start and require exactly \(m^k\) distinct vertices and return to start. Reject missing/extra vertices, invalid permutations, and malformed values.
3. **Add regression fixtures:** verified solutions for \(m=3\), \(m=4\), and \(m=5\) where available; include a negative fixture with a known multi-cycle colouring. Assert results rather than merely printing them. Keep constructor and verifier implementations independent.
4. **Narrow the theorem statements.** State the parity result for the exact column-uniform/step-size assumptions and identify which lemma proves each premise. Separate theorem, exhaustive finite check, heuristic discovery, and conjecture. Independently enumerate the \(m=3,k=3\) decomposition space before claiming the count 648 or torsor structure.
5. **Downgrade FSC product claims until end-to-end evidence exists.** Replace process-random hash routing with canonical capability identities plus a real registry; make route output concrete; specify cryptographic session establishment; use an independent quality oracle; remove stochastic toy scores from optimization evidence; test escrow/timeout/dispute and adversarial worker-hash grinding; obtain independent smart-contract review before any real-money use.
6. **Consolidate provenance and hygiene.** Choose which repository is the canonical mathematical source, replace duplicate code/document copies with links or generated artifacts where appropriate, add \`.gitignore\` rules and remove tracked bytecode, and keep research receipts distinct from production guarantees.

## Audit boundaries and falsifiers

This pass reviewed selected source, documentation, repository trees, and Actions logs. It did not execute either Python codebase locally, prove every theorem false, reproduce an exhaustive solution count, or perform a full smart-contract audit. It did independently execute a separate small verifier over the source-stored \(m=4,k=3\) fixture as described above. The remaining findings are falsifiable: a corrected independent verifier and tests can settle tuple semantics and further fixtures; a formal derivation can establish or refute the broader closure/count claims; and reproducible integration tests plus adversarial contract testing can distinguish a production implementation from a demo.

The original D3 review made no source changes. Implementation follow-up is recorded below; the proposed source changes are on a non-default branch and have not been merged. This document records portfolio observations and recommended next work only.


## Implementation follow-up — 2026-10-30

### Selected implementation target

The bounded mathematical implementation target is now **Global-structure-** because its observed tree contains the explicit full-coordinate \(m=4,k=3\) witness and an implementation capable of checking full-coordinate assignments. This is a selection for the mathematical implementation frontier, not a claim that the wider TGI product architecture is canonical or production-ready.

- Repository: [Loofy147/Global-structure-](https://github.com/Loofy147/Global-structure-)
- Base: \`main@5f56b300cbf7287507e75991d7bb0217fe670403\`
- Working branch: \`fix/independent-hamiltonian-verifier\`
- Current branch head: \`5530004e9876fcaae9f946ee973ee6ab7d2c99d8\`
- Pull request: [#28 — Add independent Hamiltonian verifier and scope parity rule](https://github.com/Loofy147/Global-structure-/pull/28)
- PR state: OPEN, unmerged; base has not moved.

### Implemented on the PR branch

1. Added \`hamiltonian_verifier.py\`, an independent verifier that checks exact vertex coverage, valid edge-to-colour permutations, in-degree one for every colour, and one \(m^k\)-length cycle returning to the origin.
2. Adapted the legacy \`verify_sigma\` interface for full-coordinate mappings, restricted fiber mappings, and indexed fixtures.
3. Changed \`solve(4,3)\` to return the stored full-coordinate witness instead of rejecting it under the restricted parity predicate. Unknown cases remain heuristic; search failure is not proof of non-existence.
4. Added the explicit \`column_uniform_blocked\` property while retaining the legacy \`h2_blocks\` field.
5. Narrowed README and theorem-script language so parity refers to the column-uniform ansatz rather than all possible decompositions.
6. Added \`docs/HAMILTONIAN_VERIFICATION.md\` and wired a standard-library unittest suite into the PR workflow.

### Local regression evidence

A local harness exercising the branch's verifier implementation and adapter/fixture behavior passed **11/11 tests**:

- Positive fixtures: \(m=3,k=3\); \(m=4,k=3\); \(m=5,k=3\).
- Compatibility inputs: stratified mapping, indexed fixture, full-coordinate mapping, and the \`solve(4,3)\` path.
- Negative fixtures: multiple short cycles despite in-degree one; mutated assignment; missing vertex; extra vertex; and a non-permutation.
- Python compilation check passed for the verifier, adapter harness, and test module.

This is local regression evidence. It is not a successful GitHub Actions run on the complete repository checkout.

### GitHub Actions limitation

The PR workflow has attempted three successive PR heads. The latest run is [41017822102](https://github.com/Loofy147/Global-structure-/actions/runs/41017822102) on commit \`5530004e9876fcaae9f946ee973ee6ab7d2c99d8\`. GitHub job metadata reports \`runner_id=0\` and zero executed steps. The earlier attempts exhibit the same pre-runner failure. Therefore:

- the workflow is **not CI-verified**;
- this failure is not evidence that the new tests failed;
- the cause of runner allocation failure is not established by the available job metadata;
- the PR remains open and must not be treated as merge-ready solely on local tests.

### Repository boundaries

No default branch has been changed in the three reviewed FSO/TGI repositories. The proposed implementation is isolated to the PR branch in \`Global-structure-\`. \`Global-theorem-\` and the standalone FSO/FSC prototype remain unchanged in this follow-up. Their eventual disposition and cross-repository cleanup are separate tasks; do not silently copy the implementation into every duplicate repository.
