# Portfolio Cluster Map v0.1

Date: 2026-08-30
Status: candidate map; not a final portfolio architecture.

## Method

Clusters are created only from inspected evidence. Similar names alone produce a weak candidate. Stronger signals include explicit cross-links, shared architectural vocabulary, version progression, matching directory/module structure, and later code/history comparison.

A cluster does **not** mean the repositories should be merged. It means they should be reviewed together because they may represent the same idea, an evolution, a composition layer, or a reusable component lineage.

## Current candidate families

### C1 — TGI / FSO / HAG / sovereign computing

Primary candidates:
- Global-theorem-
- Global-structure-
- HAG
- Symmetric-HAG
- -Highly-Symmetric-HAG
- -Fiber-Stratified-Optimization---FSO-
- Sovereign-OS
- STRATOS

Evidence strength: **medium-high**.

The strongest evidence is the direct bridge in `Symmetric-HAG`, which points to both `Global-theorem-` and `HAG`. `Global-theorem-` and `Global-structure-` independently describe TGI/FSO, Hamiltonian/topological reasoning, and the same `Z_m^k` framework. `HAG` explicitly connects TGI, Closure Lemma and recursive self-improvement to a governed desktop agent. `Sovereign-OS` and `STRATOS` share torus/sovereign/kernel vocabulary, but their lineage remains weaker until code and history are compared.

Important: the mathematical and performance claims in this family remain repository claims until independently verified.

### C2 — Evidence-governed execution and orchestration

Primary candidates:
- canonical-capability-core
- Software-res
- algeria-ai-product-fabric
- ai-meta-orchestrator
- The-adaptive-methodology
- agentic-apis

Evidence strength: **medium**.

This family contains several different abstraction levels: verified/research primitives, software-evidence validation, product composition, orchestration, governance workflow, and an API/tool registry. The central question is whether they share load-bearing semantics or merely vocabulary.

### C3 — Algeria multi-agent platform variants

Primary candidates:
- algeria-multi-agent-platform
- algeria-multiagent-platform
- algeria-ai-product-fabric

Evidence strength: **high as a review cluster; lineage still unproven**.

The first two repositories have near-identical names and overlapping missions. `algeria-ai-product-fabric` is broader and explicitly separates core, adapters, domains and evaluation, so it may be an architectural umbrella rather than a direct duplicate.

### C4 — Autonomous trading / revenue systems

Primary candidates:
- Meta-meta
- -AI-Driven-Crypto-Portfolio-Manager-
- Drogon
- v0-portfolio-manager-framework

Evidence strength: **medium**.

`Meta-meta` has an event-driven trading architecture with signal aggregation, risk validation, portfolio management and backtesting. The crypto portfolio manager has multi-agent orchestration, execution and risk layers. `Drogon` contains an AutoRevenue application on a feature branch. The v0 repository appears to be a UI/deployment surface. These need chronology and module comparison.

### C5 — AI/social/e-commerce marketplaces

Primary candidates:
- Ai-e-commerce-marketplace
- AI-Ecommerce-Social-Marketplace2
- Shop-one

Evidence strength: **medium**.

`Ai-e-commerce-marketplace` is a concrete backend/frontend/docker project. `AI-Ecommerce-Social-Marketplace2` is minimal at the inspected revision. `Shop-one` contains a very large README artifact and workflows, so it may contain important specifications or generated implementation history that cannot be classified from the root alone.

### C6 — Delivery/logistics

Primary candidates:
- smart-delivery-platform-2
- smart-delivery-plat
- delivery-app

Evidence strength: **medium-low**.

The explicit delivery ecosystem is established for `smart-delivery-platform-2`; the other candidates need content/history inspection before lineage is assigned.

### C7 — Security / red-team automation

Primary candidates:
- Global-redteam
- Red-team-defence2-
- Syst-me-d-fensif-
- meta-secure-framework

Evidence strength: **medium**.

`Global-redteam` has a substantial concrete architecture spanning API security, fuzzing, property testing, race detection, SAST, orchestration, persistence and a vulnerable test application. The other names are cluster candidates until their implementation surfaces are inspected.

### C8 — RL / swarm / experimental agents

Primary candidates:
- HiveMind-RL
- MARL-Pro
- Unified-ai
- training-home

Evidence strength: **medium-low**.

`HiveMind-RL` explicitly combines deep RL, GAT-based communication and swarm behavior. `Unified-ai` is an umbrella architecture including RL/HRL and specialized agents. The remaining repositories need implementation comparison.

## Required next stage

For each candidate cluster, inspect:

1. repository tree;
2. primary implementation modules;
3. dependency manifests;
4. tests and benchmarks;
5. CI/workflows;
6. documentation/specifications;
7. branches/tags/commit chronology;
8. direct imports or copied modules where discoverable.

Only after these checks should an edge be promoted from `candidate` to a stronger relationship such as `same_idea`, `successor`, `component_source`, `dependency`, or `research_source`.

## Current rule

No repository is to be deleted or merged as a consequence of this map. The map is an analysis aid and a routing mechanism for deeper review.
