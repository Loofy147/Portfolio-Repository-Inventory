# Startup Resource Acquisition — Credit, API and Ecosystem Program Scan

**Checked:** 2026-11-09  
**Purpose:** Reduce actual cash burn and unlock useful infrastructure, model access, expertise, distribution and financing.  
**Scope:** Portfolio-wide; programmes are evaluated as enablers for any eligible product/company, not as proof that a product should be built.  
**Applicant-specific eligibility:** UNKNOWN until legal entity, ownership, company age, public domain/email, funding, partner affiliation, previous credits and cloud/account status are confirmed.

## Executive decision

The four original programmes are real, but their headline maxima are not equally accessible. The current research found several additional programmes with better fit to existing workloads:

- **Vercel for Startups — up to $30K**: strongest direct infrastructure fit for a product already deployed on Vercel, but it is partner-backed and has strict funding-recency requirements.
- **OpenAI API data-sharing incentive**: potentially usable without migrating infrastructure, if the user's own API organization is eligible and explicitly opts in at selected-project level after data classification.
- **Microsoft for Startups**: low initial benefit ($200), with staged progression to $150K; a possible $200K ceiling for eligible investor-network-backed startups. The largest tiers require sustained Azure use, so do not spend artificially to unlock them.
- **Google for Startups Cloud**: $2K pre-funded Start tier; Scale tier up to $200K generally or $350K for AI-first startups, subject to funding, age, MVP, website/domain and other criteria.
- **AWS Activate**: current detailed AWS June 2026 guide states $1K Founders and up to $100K Portfolio; older $200K headlines should not be used without a current offer document.
- **Cloudflare / DigitalOcean / NVIDIA**: strong additional programmes for edge hosting, ordinary cloud workloads and AI ecosystem benefits, but with company, partner, prior-credit and service exclusions.
- **Algeria Startup label → A-Venture / ASF**: the domestic company-formation and investment route; ASF offers equity/quasi-equity, not grants. Startup label is a prerequisite to ASF.

**No application has been submitted, no credits have been claimed, no cloud provider has been changed, and no API data-sharing setting has been enabled.**

## 1. Resource programme register

### 1.1 API and AI access

| Programme | Verified benefit | Eligibility and constraints | Decision |
|---|---|---|---|
| OpenAI API data-sharing incentive | Per day: usage tiers 1–2 up to 250K tokens in model group 1 and 2.5M in group 2; tiers 3–5 up to 1M and 10M. Quotas are shared across included models. Shared evaluations currently processed at no cost up to 7 runs/week. | Eligibility is visible only in the user's own Platform Data Controls page. An organization owner must opt in; can be enabled for selected projects. ZDR organizations cannot opt in; Enterprise orgs are excluded from input/output sharing. Positive API balance required. Only listed models qualify; tools, fine-tuning, evals and fine-tuned models are excluded from the complimentary-token allocation. Input/output sharing means enabled-project data is shared with OpenAI for usage-pattern, quality and model-improvement purposes. Never share sensitive, confidential or proprietary data without appropriate rights/permissions. | **First eligibility check; consent decision separate.** Prefer only a project with synthetic, redacted or otherwise explicitly shareable data. No global-org enablement by default. |
| OpenAI for Startups API credits | Free API credits, rate-limit upgrades, direct technical help and events may be available to VC-backed portfolio startups. No universal public dollar amount. | Requires a unique referral code from a participating VC, product/API-use description, company/business contacts, basic funding details and OpenAI Organization ID. Not open as a generic direct application. | **Conditional partner path.** Check only if a legitimate participating-VC relationship exists. |
| Google AI Studio / Gemini API free access | Free prototyping access to Gemini models through AI Studio, plus a free usage tier for selected APIs/models subject to quotas and terms. | Rate-limited and model-specific; free-tier data treatment and production restrictions must be checked before using real user/customer data. Free experimentation is not the same as startup credits or a production SLA. | **No-regret prototype option** for non-sensitive experiments; use paid/project credits only after product-specific workload needs are known. |
| AWS Bedrock through Activate credits | AWS credits can cover eligible AWS use including Amazon Bedrock, which exposes several third-party foundation models through one AWS interface. | Model availability, pricing, regional access, data terms and credit-service eligibility vary. Bedrock use consumes the AWS credit pool and is not a separate unrestricted model grant. | **Useful if an AWS-hosted workload is already justified.** Benchmark latency, quality and effective cost before routing production traffic. |
| NVIDIA Inception partner benefits | Member portal may expose cloud credits from partners, preferred software/hardware pricing, training and technical resources. Partner-credit amounts are not guaranteed or universal. | Membership itself is free, but partner offers/credits are not a guaranteed fixed award. Company must be incorporated, under 10 years old, have a public website, at least one employed developer and a clear NVIDIA technology use case. Consulting/outsourcing, crypto, cloud providers, resellers and public companies are excluded. | **Good AI ecosystem application** if there is an incorporated AI product company; do not count partner credits until a specific offer is approved. |

### 1.2 Cloud and developer infrastructure

| Programme | Current offer | Critical conditions | Fit / decision |
|---|---|---|---|
| Microsoft for Startups | Up to $150K Azure credits over time; eligible Investor Network-backed startups may reach $200K. Standard path starts at $200; milestones can reach $5K, $25K, $50K, then $150K. | Privately held, for-profit company owning a software product/service; HQ in a country where Azure services are available; below Series C; excludes agencies/consultancies, education/government and crypto mining; prior free Azure credit ceiling applies. Milestones require real sustained Azure workloads. The $150K milestone requires 10+ workloads and about $3K/month Azure usage sustained over 60 days. Investor path needs a qualifying partner/referral. | **High conditional priority** if a legal company owns a product and Azure workloads have natural fit. Do not create workloads or spend solely to climb tiers. Confirm HQ-country eligibility at application. |
| AWS Activate | Current detailed guide dated 4 June 2026: $1K Founders; up to $100K Portfolio. Credits cover more than 200 AWS services and can support Bedrock. | Founders: new to Activate, self-funded or pre-Series B, functioning company website, founded in past 10 years. Portfolio: approved Activate Provider affiliation and Org ID, prior-credit ceiling, pre-Series B, site and company age. Application needs an active linked AWS account. Credits are prospective and generally expire in 1–2 years depending on package. | **Low-friction small entry / larger partner route.** Correct the old $200K headline to the current detailed $100K guide unless a newer written offer states otherwise. |
| Google for Startups Cloud — Start | Up to $2K Google Cloud credits valid for one year, plus training and possible Google Workspace benefits. | Digital-native startup with working MVP, clear model and plans to seek VC funding soon; founded within 24 months; no prior GCP credits beyond free trial. Requires business domain, matching business email and Google Cloud Billing ID. | **Conditional early-stage option.** Not automatic for any solo project; VC-funding intent is part of the stated Start-tier criteria. |
| Google for Startups Cloud — Scale / AI-first | Up to $200K general or $350K AI-first over two years. General: up to $100K year 1 plus 20% of year-2 spend up to another $100K. AI-first: up to $250K year 1 plus up to $100K year 2. Eligible Google models such as Gemini/Gemma are covered. | VC-funded; Pre-Seed/Seed within 5 years or Series A within 12 months; company founded within 5 years; prior GCP credits not above $5K. AI tier requires AI to be foundational to the company and is case-by-case. Third-party models/Marketplace services are not covered. | **Potentially high AI infrastructure value, but future-stage.** The $350K figure is not a general or unfunded award. |
| Vercel for Startups | Flexible Commitment up to $30K towards Vercel usage (seats, compute, data transfer, v0, AI Gateway and more), with Enterprise-tier access for up to one year. | Must be affiliated with an approved Vercel Startup Partner and prove it; Series A or earlier and apply within 12 months of most recent funding; public company site and matching domain email; no prior Vercel startup credit. Single Vercel Team only, non-transferable, payment method required; no retroactive billing; up to 50% of monthly credit can be used for AI Gateway. | **Best direct platform fit where a product is already on Vercel.** Partner affiliation/funding are hard gates. Existing Vercel deployment is not itself proof of eligibility. |
| Cloudflare for Startups | Public tiers: $10K for Tier 3 bootstrapped/self-funded under $1M raised; $100K for partner-backed under $5M; $350K for partner-backed $5M+; valid one year. Core security/network services included free. | Incorporated under 10 years, for-profit technology product, public website, public LinkedIn/X/GitHub, matching business email, first-time applicant. Public page's general eligibility says funded within 12 months, which conflicts with Tier 3 wording “no minimum funding”; written clarification is needed. Workers AI subcaps: $2.5K/$10K/$50K by tier; R2 cap $10K; AI Gateway currently excluded. No extension. | **Strong edge/serverless candidate** for apps, APIs, queues, storage and security if product fit exists. Tier 3 eligibility ambiguity is a blocker to treating the $10K as accessible. |
| DigitalOcean Startups | 12 months of DigitalOcean credits (amount varies), 15 months Standard support, expert guidance and partner perks; selected startups may apply separately for GPU credits. | AI-native startups prioritized; not service-based agencies/consultancies; $10M or less raised; company website and matching business email; new DigitalOcean team account/card; no prior DigitalOcean startup credits. Credits are awarded through partners, though applicants without an existing VC/accelerator partner can select “Other”. General monthly consumption ceiling $10K. Core credits exclude GPU Droplets, H100 GPU Kubernetes, bare-metal GPU, dedicated/serverless inference for third-party models, Paperspace and Cloudways. No extension. | **Useful for ordinary app/database/container workloads**, not a GPU or third-party LLM subsidy. Award amount and country eligibility remain unconfirmed. |
| Cloudflare baseline free services | Free core DNS/CDN/security features are offered outside the startup credit programme. | Service limits and acceptable-use conditions still apply. | **No-regret cost-control layer** if it fits existing architecture; no need to apply or migrate the whole stack. |

### 1.3 Startup, accelerator and national funding pathways

| Route | Benefit / requirements | Current status |
|---|---|---|
| Startup.dz — Projet innovant label | Intended for project holders who have not yet created a company. Current form requests founder identity/CV, project description (max 400 chars), official pitch-deck template, detailed innovation presentation, prototype photo, stage, business model, website and relevant incubation/IP/award information. It is recognition/access, not a cash award. | **Available pathway; no submission made.** Decree-based evidence still requires a defensible innovation case, significant growth potential and team technical/scientific qualification/experience. |
| Startup.dz — Startup label | Requires an incorporated Algerian company, innovation, high growth potential, annual turnover under the committee-set ceiling, at least 50% qualifying ownership and no more than 250 employees; company age no more than 8 years. Label issued for 4 years and may be renewed once. | **Eligibility depends on legal company facts.** It unlocks ecosystem facilities, but does not automatically fund the company. |
| Algerian Startup Fund (ASF) | Public fund investing through equity and quasi-equity. Public site advertises tickets up to DZD 150M depending on need/maturity, plus investor readiness, partner network and post-investment support. | **Requires Startup label. Not a grant.** A company/product, team, traction and governance must survive investment assessment. |
| A‑Venture / Algeria Venture | National public accelerator linked with ASF; mentoring, go-to-market, corporate/POC access, investor readiness and ecosystem access for labelled startups. | **Programme/network exists; current intake dates not verified.** Monitor for relevant cohorts or open calls. |
| Google for Startups Accelerator: Africa | Three-month hybrid, equity-free accelerator; mentorship, technical work with experts, AI product early access, potential product credits and Cloud TPU access for eligible startups. | **2026 cohort closed** (applications closed 18 March; April–June programme). Monitor next cohort; no next dates published in this scan. |
| NESDA Extension | Financing up to DZD 10M under specified financing structures. | **Loan/financing route, not a grant.** Applies to qualifying existing micro-enterprises with operating-history, age, qualification and prior financing/repayment conditions; low priority unless applicant facts match. |

## 2. Fit to existing workloads — do not infer eligibility

This mapping uses known project/deployment context as an execution-fit assessment. It does not assert that any project company or account is eligible.

| Workload / project family | Most relevant offers | Why |
|---|---|---|
| Taskora and existing Vercel-deployed web products | Vercel for Startups; Cloudflare baseline/free features; optionally Cloudflare for Startups; Microsoft/AWS/Google only if workload requirements justify a backend/cloud move | Vercel credits can reduce the bill on the existing platform without migration. Partner/funding eligibility is the blocker. Cloudflare can be added selectively for DNS/CDN/WAF/R2/edge services, not as an automatic replacement for Vercel. |
| AI agents, model orchestration and API-intensive products | OpenAI data-sharing incentive; Google AI Studio/Google Scale; AWS Activate + Bedrock; Microsoft Azure AI/Foundry; NVIDIA Inception; DigitalOcean Startup programme | These unlock model testing, inference access, technical guidance and compute, but provider prices, service coverage, data policies and quotas differ. Benchmark each model/workflow before assigning production traffic. |
| New deployable software products | Microsoft Start, AWS Founders, Google Start, Cloudflare Tier 3, DigitalOcean Startups | Early-stage credits may help if the company and website prerequisites exist and the services match actual architecture. Avoid submitting the same legal entity as multiple fictional startups. |
| R&D, accelerated compute and AI systems | NVIDIA Inception; Google Cloud AI Scale/TPU benefits; selected partner GPU programmes | NVIDIA membership is a no-fee ecosystem route, while GPU credits are conditional partner offers. DigitalOcean core credits explicitly exclude key GPU and third-party inference services. |
| Commercialisation, pilots and funding readiness | Startup.dz Project Innovant/Startup label; A‑Venture; ASF; Google Accelerator Africa next cohort; partner-backed cloud programmes | These create pathways to mentorship, pilots, investors, credits and public recognition. They require a real company/product/team/traction case, not merely a repository or prototype. |

## 3. Priority order

### Priority 0 — no-regret, no migration

1. Check the user's **own** OpenAI API organization for the data-sharing incentive notice. Do not change the setting. If eligible, isolate a non-sensitive test project and measure actual usage/savings. Keep production/customer/confidential data excluded unless appropriate permissions and a deliberate consent decision exist.
2. Use Google AI Studio's free access for non-sensitive prototypes where it is adequate; do not confuse free-tier experimentation with startup credits or production service guarantees.
3. Use existing Cloudflare free DNS/CDN/security features only where technically appropriate; no provider migration required.
4. Collect actual monthly spend, usage and service mix for Vercel, OpenAI, AWS, Azure, Google and other accounts. Credits have no economic value if there is no eligible usage.

### Priority 1 — direct-fit applications once entity facts are known

1. **Vercel for Startups** for workloads already on Vercel, if an approved Startup Partner, funding recency and company domain evidence exist.
2. **Microsoft for Startups** if a privately held, for-profit software company owns the product and Azure workloads have a natural place.
3. **AWS Activate Founders** if new to Activate, self-funded/pre-Series B, company website and age criteria fit; seek Portfolio only with a real provider Org ID.
4. **Google Start tier** if an eligible digital-native startup has a working MVP, is under 24 months old and intends to seek venture funding.
5. **NVIDIA Inception** if an incorporated AI product company has a website, developer and meaningful NVIDIA technology use case.

### Priority 2 — partner/VC-dependent higher-value routes

- Google Scale / AI-first ($200K / $350K maximums).
- AWS Activate Portfolio (up to $100K in current detailed guide).
- Microsoft Investor Network additional benefits and possible up-to-$200K ceiling.
- Vercel Startup Partner route (up to $30K).
- Cloudflare Tier 2/1; DigitalOcean partner-allocated credits.
- OpenAI Startup API credits using a participating VC's referral code.

### Priority 3 — Algerian capital and accelerator path

- Decide whether to use the Project Innovant label before incorporation or build the legal entity first and seek the Startup label.
- If a registered startup is genuinely eligible, ASF/A‑Venture can become a capital, mentorship and pilot-access route.
- Do not treat ASF equity/quasi-equity as a grant or raise capital simply to finance a project without a validated customer and clear capital plan.

## 4. Economic-value method

`Net benefit = eligible cost avoided + value of in-kind benefits - migration/integration cost - unused/expired credits - post-credit premium - operational and lock-in risk`

Required inputs before ranking an offer financially:
- current monthly service spend by provider and product;
- forecast usage over the full credit period;
- services that the provider credits actually cover;
- expected burn rate and credit expiry;
- expected overage above monthly caps;
- cost to migrate, integrate, test, secure, maintain and exit;
- prices after benefits end;
- data residency, privacy, IP and publicity obligations;
- payment card, local payment, tax and currency constraints.

Never inflate resource usage to unlock a higher credit tier. The Microsoft $150K milestone's approximately $3K/month usage requirement is valuable only if the product already has that legitimate spend. The correct objective is lower net cost for the same useful workload.

## 5. Eligibility dossier — evidence needed

A shared company-level dossier would reduce repeat application effort:

1. Legal entity name, country of incorporation, registration date and ownership structure.
2. Product ownership/IP rights and whether the business is privately held and for-profit.
3. Public website, domain-matched business email, and one current product/demo video.
4. Company age, revenue stage, funding stage/date and verifiable equity-investment evidence.
5. Accelerator, incubator, investor/VC affiliation and relevant partner referral/Org IDs.
6. Previous credits from each provider, balances and expiration dates.
7. Cloud accounts, billing account IDs and actual monthly/annual usage.
8. Model API usage by model/project, input/output volume and data classification.
9. Company founder/team contacts, roles and dedicated developer/CTO availability.
10. Product-specific infrastructure architecture and a 12-month spend forecast.

Do not put identity numbers, personal IDs, private financial records, credentials or billing secrets into public repositories. Store private application material in the relevant provider portal or a restricted secure workspace.

## 6. Current blockers and unresolved checks

- **Applicant company status/ownership:** UNKNOWN. This is the largest cross-program gate.
- **Public domains and domain-matched business emails:** UNKNOWN by legal company.
- **Funding history and accelerator/VC referrals:** UNKNOWN.
- **Prior credits and current provider spend:** UNKNOWN.
- **Algeria-specific programme availability:** Open documentation does not confirm every provider's country decision. OpenAI API service support explicitly lists Algeria, but startup-incentive eligibility is a separate question. Google has a localized startup page for Algeria, but final application and billing-country acceptance still need confirmation. Microsoft, AWS, Vercel, Cloudflare, DigitalOcean and NVIDIA should be country-checked at their application/onboarding stage.
- **Cloudflare Tier 3 eligibility wording:** public page says bootstrapped/no minimum funding, while general eligibility also states funding within the last 12 months. Request written clarification before relying on Tier 3.
- **AWS headline maximums:** the detailed current guide says up to $100K Portfolio, not $200K. Any different offer needs a current written AWS source.
- **Google Scale:** the high value requires qualifying equity funding; government grants/prize/crowdfunding/angel/friends-family funding do not qualify for Scale under current FAQ.
- **Vercel:** a startup partner relationship and funding date are mandatory.
- **NVIDIA:** no fixed cloud credit amount is guaranteed by membership.

## 7. Status register

| ID | Status | Next action |
|---|---|---|
| GL-OPENAI-SHARING-2026-001 | Verified offer / eligible organization unknown | User checks their own org's visible eligibility notice; no setting change. |
| GL-OPENAI-STARTUP-API-2026-001 | Partner-only | Check only if real participating VC referral exists. |
| GL-MSFT-STARTUPS-2026-001 | Verified / entity eligibility unknown | Confirm product-owning company, country/HQ, prior credits and Azure workload fit. |
| GL-GOOGLE-CLOUD-START-2026-001 | Verified / entity eligibility unknown | Confirm company age, MVP, funding intent, billing ID and prior credits. |
| GL-GOOGLE-CLOUD-SCALE-2026-001 | Verified / funding/AI-first status unknown | Confirm qualifying equity and whether AI is core to the company. |
| GL-AWS-ACTIVATE-2026-001 | Verified / applicant and provider status unknown | Determine Founders vs Portfolio and previous Activate awards. |
| GL-VERCEL-STARTUPS-2026-001 | Verified / partner and funding gate unknown | Check approved partner relationship, round date and relevant Vercel Team. |
| GL-CLOUDFLARE-STARTUPS-2026-001 | Verified / terms ambiguity and applicant fit unknown | Obtain written Tier 3 funding-criteria clarification. |
| GL-DIGITALOCEAN-STARTUPS-2026-001 | Verified / award and country unknown | Confirm AI-native/product status, eligible services and partner route. |
| GL-NVIDIA-INCEPTION-2026-001 | Verified / company eligibility unknown | Assess incorporated AI product fit, website, developer and NVIDIA use case. |
| GL-GOOGLE-ACCEL-AFRICA-2026-001 | 2026 cohort closed / monitor next intake | Watch future cohort dates. |
| GL-ALGERIA-LABEL-ASF-2026-001 | Verified national route / entity and product eligibility unknown | Decide Project Innovant vs Startup label pathway; assess ASF only after customer/product evidence. |
| GL-ALGERIA-NESDA-EXT-2026-001 | Conditional / low priority | Check only if existing microenterprise operating-history criteria fit. |

## 8. Non-actions

No provider application was submitted. No account was created or migrated. No payment method was added. No terms were accepted. No data-sharing setting was changed. No grant, credit, investment or eligibility was represented as approved.

## 9. Official sources checked 2026-11-09

### OpenAI
- [API data-sharing and complimentary token incentive](https://help.openai.com/en/articles/10306912-sharing-feedback-evaluation-and-fine-tuning-data-and-api-inputs-and-outputs-with-openai).
- [OpenAI for Startups — VC-referral API credits](https://openai.com/startups).
- [OpenAI API supported countries — Algeria listed](https://developers.openai.com/api/docs/supported-countries).

### Microsoft
- [Microsoft for Startups overview and eligibility](https://learn.microsoft.com/en-us/startups/microsoft-for-startups/overview).
- [Standard programme milestones](https://learn.microsoft.com/en-us/startups/standard-benefits/unlock-more-benefits).
- [Investor Network additional benefits](https://learn.microsoft.com/en-us/startups/microsoft-for-startups/unlock-more-benefits).

### AWS
- [AWS Activate official application guide, 4 June 2026](https://aws.amazon.com/aws-startups/learn/applying-for-aws-activate-credits-a-step-by-step-guide/).
- [AWS Activate credits](https://aws.amazon.com/startups/credits).

### Google
- [Google for Startups Cloud benefits and tiers](https://cloud.google.com/startup/benefits).
- [Pre-funded Start tier](https://cloud.google.com/startup/pre-funded).
- [Programme FAQ, including AI tier and third-party-model exclusion](https://cloud.google.com/startup/faq).
- [Google for Startups Algeria Cloud page](https://startup.google.dz/cloud/).
- [Google for Startups Accelerator: Africa 2026 cohort](https://startup.google.dz/programs/accelerator/africa/).

### Vercel / Cloudflare / DigitalOcean / NVIDIA
- [Vercel for Startups credits and terms](https://vercel.com/startups/credits).
- [Cloudflare for Startups](https://www.cloudflare.com/startups/).
- [DigitalOcean Startups](https://www.digitalocean.com/startups).
- [DigitalOcean Startups Terms (11 May 2026)](https://www.digitalocean.com/legal/startups-program-terms-of-service).
- [NVIDIA Inception programme](https://www.nvidia.com/en-us/startups/).

### Algeria
- [Startup.dz — Project Innovant and Startup labels](https://startup.dz/pour-les-startups/).
- [Startup.dz — Project Innovant form](https://startup.dz/label-projet/).
- [Startup.dz — Startup label and criteria](https://startup.dz/).
- [Algerian Startup Fund](https://asf.dz/).
- [NESDA Extension](https://www.nesda.dz/Home/NesdaExtension).
