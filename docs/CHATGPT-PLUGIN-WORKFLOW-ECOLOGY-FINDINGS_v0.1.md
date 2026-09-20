# ChatGPT Plugin / Workflow Ecology Findings v0.1

**Recorded:** 2026-09-20  
**Scope:** Findings from the ChatGPT plugin/app ecosystem investigation conducted in September 2026.  
**Repository role:** Durable portfolio discovery; not a product commitment.

## 1. Executive finding

The ChatGPT plugin directory is no longer best understood as a simple connector catalogue. OpenAI currently describes plugins as reusable workflow packages that can contain skills, connected apps, and app templates; the directory is the primary discovery surface for workflow capabilities across ChatGPT and Codex.

The important opportunity question therefore shifts from:

> Which connector/app should be built?

to:

> What valuable, reusable compositions, workflows, capabilities, and shared assets can emerge from groups of people who already use overlapping plugin/app stacks?

A second-order opportunity may exist above individual plugins: a layer for discovering, sharing, adapting, executing, verifying, and improving workflows built from existing connectors.

This is a research direction, not yet an established product opportunity.

## 2. User-reported ecosystem observation

The user inspected the ChatGPT Plugins directory and observed a large cross-domain ecosystem containing, among others:

- General work / knowledge: Airtable, Notion, Google Drive, Slack, Gmail, Outlook.
- Engineering / build: GitHub, Vercel, Supabase, Convex, Railway, Lovable, AppDeploy, Hugging Face, Exa, Firecrawl.
- Design / media: Canva, Figma, Runway, Higgsfield, OpenArt, Invideo, HeyGen, Product Design, Magnific, Mobbin.
- Commerce / business: Shopify, Stripe, HubSpot, Wix, Docusign, monday.com.
- Analytics: PostHog, Mixpanel, Amplitude, Tableau, Data Analytics, Windsor.ai, Metricool, vidIQ, Ubersuggest.
- Research: Deep Research, Consensus, SciSpace, Scite, Elicit, Undermind.
- Finance, travel, healthcare, security, education, communications, and specialist scientific tools.
- User-reported installed/connected set during the investigation included Airtable, Tripadvisor, Booking.com, AppDeploy, Parqet, Devpost Hackathons, Canva, Convex, Deep Research, Figma, GitHub, Hugging Face, Lovable, Notion, OpenAI Developers, Plugin Management, and later Shopify.

This inventory is **USER_REPORTED**, not an authoritative census of directory availability.

## 3. Current platform facts

OpenAI's current documentation states:

- As of July 9, 2026, the app directory was migrated to the Plugin directory.
- Plugins are the primary discovery surface for workflow capabilities across ChatGPT and Codex.
- A plugin can include skills, connected apps, and app templates.
- Some plugins contain multiple apps.
- App access still depends on account, workspace, plan, supported surface, region, and provider authorization.

Sources:
- https://help.openai.com/en/articles/11487775
- https://help.openai.com/en/articles/20001256

## 4. Important correction to the initial hypothesis

Initial hypothesis:

> The main missing layer might be universal agent/tool orchestration.

Disposition: **CONTRADICTED / ALREADY CROWDED**

Current evidence shows substantial existing work on orchestration and runtime infrastructure, including:

- OpenAI Agents SDK: agents, tools, MCP, guardrails, sessions, human-in-the-loop, tracing.
- Composio Tool Router and related tool/session infrastructure.
- Zapier's AI orchestration / app automation platform.
- Cloudflare Agents + MCP / durable execution capabilities.
- Broader workflow-runtime infrastructure such as Inngest and Temporal-like systems.

Therefore, a generic "universal plugin orchestrator" should not be treated as the current opportunity without additional evidence.

Sources:
- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/mcp/
- https://docs.composio.dev/kb/guide/mcp-tool-router-sessions
- https://developers.cloudflare.com/agents/tools/mcp/

## 5. More defensible technical gap hypothesis

The more interesting gap is between:

1. selecting/calling tools, and
2. proving that a multi-tool workflow actually achieved the required external state.

Relevant primitives include:

- preconditions;
- action execution;
- observation;
- postconditions;
- independent verification;
- idempotency;
- retry classification;
- evidence;
- durable state;
- approval / human checkpoints.

This resembles an **Outcome Integrity Layer** or **Verifiable Multi-Tool Execution** layer rather than a general orchestrator.

### Example

A workflow may perform:

Shopify lookup -> Stripe mutation -> Gmail notification.

A timeout after a Stripe mutation does not imply failure. The correct next state may be UNKNOWN until the external state is checked. A verification-aware runtime could classify the action as VERIFIED_AFTER_UNKNOWN and suppress an unsafe duplicate retry.

This direction connects to known agent-runtime concerns, but remains a hypothesis about product differentiation.

Relevant current OpenAI evidence:
- Tool guardrails can run before and after tool calls.
- Human approval can gate sensitive tool execution.
- MCP tools can be dynamically filtered and traced.
- OpenAI's SDK exposes persistent sessions and workflow traces.

Sources:
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
- https://openai.github.io/openai-agents-python/tracing/
- https://openai.github.io/openai-agents-python/mcp/

## 6. The more important user-side reframing

The investigation then shifted from infrastructure-first to **groups of people already using GPT plus overlapping connectors**.

The useful segmentation is not only by occupation. It can be by recurring personal / project system and, more importantly, by the software stack already used together.

Examples observed as plausible stack signatures:

- GitHub + Notion + Figma + Vercel -> product-building / technical teams.
- Gmail + Calendar + Drive + Canva -> personal/work coordination and content-heavy workflows.
- Shopify + Canva + Stripe + analytics -> small e-commerce operators.
- Deep Research + Consensus / SciSpace + Notion / Drive -> researchers / knowledge workers.
- Booking.com + Tripadvisor + Calendar -> travel planning.
- Gmail + Calendar + Notion + Canva + Stripe -> freelancers / consultants.

These are **HYPOTHESES / EXEMPLARS**, not measured co-occurrence statistics.

## 7. Core product hypothesis from the user-stack perspective

A person who already has a useful connector stack may not need another standalone app.

They may need a **ready-made composition around the stack they already have**.

Example:

### Product-launch workflow

Research
-> Notion
-> Figma / Canva
-> GitHub
-> Vercel
-> PostHog

### Freelancer workflow

Lead
-> Gmail
-> research
-> proposal
-> Calendar
-> delivery
-> Stripe
-> follow-up
-> durable client state

The asset is therefore not merely a connector.

It is:

> **A reusable workflow composition tied to a known stack, with explicit inputs, outputs, setup, checkpoints, and evidence.**

## 8. Workflow assets are richer than prompts

A reusable AI asset can be modeled as:

- workflow instructions / skill;
- required apps / connectors;
- input schema;
- output schema;
- templates;
- examples;
- state requirements;
- permissions;
- human checkpoints;
- verification rules;
- provenance;
- version;
- measured outcomes.

This creates a possible progression:

prompt -> skill -> workflow -> verified workflow asset.

The asset can then be:

discover -> clone -> connect -> run -> modify -> contribute -> publish derivative.

This is consistent with OpenAI's current separation between plugins, skills, and apps.

Status: **INFERENCE / DESIGN HYPOTHESIS**

## 9. Social / community layer hypothesis

A plugin directory primarily answers:

> What software capabilities exist?

A workflow community could additionally answer:

- Who uses this stack?
- What are they doing with it?
- Which workflows work in practice?
- Can I reuse a workflow?
- Can I fork it?
- Can multiple people contribute?
- Can a specialist expose a reusable capability?
- Can results and evidence improve the workflow over time?

Potential graph:

PERSON
-> STACK
-> WORKFLOW
-> ASSET
-> PROJECT
-> RESULT
-> FEEDBACK
-> improved asset

Status: **HYPOTHESIS**

## 10. Multi-person collaboration hypothesis

The opportunity may extend beyond a single user's workflow.

A project can contain multiple participants with different plugin stacks:

Founder
<-> Designer
<-> Developer
<-> Marketer
<-> Customer

Each role can contribute to the same durable project state while using different tools.

Possible abstraction:

> shared project state across people, AI interactions, and external apps.

This is different from generic team chat or ordinary project management.

Status: **HYPOTHESIS**

## 11. Capability-market hypothesis

A deeper model is:

1. A user requests an outcome.
2. The system discovers a reusable capability / workflow.
3. The user grants access to required connectors.
4. The workflow executes.
5. The result is verified.
6. The workflow can be reused, forked, improved, or delegated.

This suggests a possible progression:

plugin marketplace
-> workflow marketplace
-> capability marketplace.

The last stage could expose trusted human-authored workflows or specialist capabilities without exposing the creator's entire account or data.

Status: **HYPOTHESIS**

## 12. Reputation / evidence opportunity

Once workflows can perform real actions, ordinary ratings are weak.

A workflow could instead accumulate operational evidence such as:

- runs;
- completion rate;
- intervention rate;
- failure rate;
- verification status;
- execution time;
- supported apps;
- version history;
- provenance.

This supports a possible distinction between:

"popular workflow"

and

"evidenced workflow."

This also connects to the portfolio's existing trust / evidence design work.

Status: **HYPOTHESIS / DESIGN DIRECTION**

## 13. Three potentially distinct markets

The investigation identified three markets that must not be conflated:

### A. Workflow products
"Here is a ready-to-use workflow for your stack."

### B. Workflow infrastructure
"Here is infrastructure for creating, sharing, executing, versioning, and verifying workflows."

### C. Capability network
"Here are people / agents / workflows capable of accomplishing specific outcomes."

Which market has the strongest combination of demand, competition, build cost, defensibility, and network effects remains **UNKNOWN**.

## 14. Possible common architecture

A future system could conceptually contain:

CHATGPT / USER
-> workflow layer
-> reusable workflow
-> plugins / apps
-> external services

Cross-cutting state:

- identity;
- permissions;
- durable state;
- provenance;
- versioning;
- trust;
- reputation;
- evidence;
- results.

This is an architecture hypothesis only.

## 15. Connection to existing Loofy147 work

The investigation has clear conceptual overlap with existing project primitives:

- trust engine;
- evidence ledger / source-of-truth concepts;
- durable state;
- idempotent run contracts;
- approval policies;
- UNKNOWN as a first-class state;
- recovery / retry semantics;
- project / task / decision / claim / evidence / experiment / run / artifact abstractions;
- user-controlled activation and privacy.

This is **SHARED-PRIMITIVE-CANDIDATE** evidence, not proof that any existing project should become the implementation.

The correct next step is to validate the overlap at repository/ref level before extracting or reusing primitives.

## 16. Current claim ledger

### ESTABLISHED
The current ChatGPT Plugin directory is a broad workflow/app discovery surface and plugins may package multiple apps, skills, and app templates.

### ESTABLISHED
Generic agent/tool orchestration is an active and increasingly mature category with significant existing implementations.

### ESTABLISHED
Modern agent runtimes already expose guardrails, approvals, sessions, MCP integration, dynamic tool filtering, and tracing.

### USER_REPORTED
The visible directory contains a much broader range of capabilities than a small connector list, including commerce, design, deployment, analytics, research, finance, travel, healthcare, and security.

### INFERENCE
Overlapping user stacks are likely to be more useful segmentation units than isolated plugin categories.

### HYPOTHESIS
The directory may create demand for ready-made stack-specific workflow compositions.

### HYPOTHESIS
A social / community layer for workflow sharing, forking, evidence, and collaboration may have value above ordinary plugin discovery.

### HYPOTHESIS
A capability marketplace could connect users to trusted reusable workflows or specialist human/AI capabilities.

### HYPOTHESIS
Outcome verification across connected tools may be a more defensible technical layer than generic tool orchestration.

### UNKNOWN
Which user groups actually exhibit the strongest repeated stack patterns.

### UNKNOWN
Which workflow combinations have sufficient demand to support a product.

### UNKNOWN
Whether users will share or pay for workflows versus simply copying prompts or using generic agent products.

### UNKNOWN
Whether workflow reputation based on execution evidence creates meaningful marketplace trust.

## 17. Next discriminating research

Do not build the product yet.

Build a **Workflow Ecology Map**:

USER GROUP
-> COMMON STACK
-> RECURRENT OUTCOME
-> REPEATED WORKFLOW
-> CURRENT WORKAROUND
-> EXISTING PRODUCT
-> MISSING COMPOSITION
-> SHARING POTENTIAL
-> COLLABORATION POTENTIAL
-> VERIFICATION REQUIREMENT
-> BUSINESS MODEL

Priority evidence sources:

1. Plugin/app directory composition and included apps.
2. Public workflow/skill repositories and marketplaces.
3. Public user discussions showing recurring stack combinations.
4. Existing orchestration / workflow / capability-market products.
5. Concrete workflow examples with observable outputs.
6. Repository archaeology for reusable Loofy147 primitives.

The first useful deliverable after this record should be a matrix of real workflows, not a new implementation.

## 18. Provenance boundary

The original conversation contained a mixture of:
- current web-verified platform facts;
- user-reported directory contents;
- architectural inference;
- product hypotheses.

These must remain separate. Repetition in conversation is not additional evidence. The hypotheses above must not be promoted without new discriminating evidence.
