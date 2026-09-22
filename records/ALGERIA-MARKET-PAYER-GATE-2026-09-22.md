
# Algeria Market Research — Payer Gate — 2026-09-22

Purpose:
Make payer identity a mandatory gate for opportunity research across all sectors and transaction layers. A problem, trigger, accepted artifact, or regulatory requirement is not sufficient without a plausible direct payer and payment mechanism.

## Mandatory payer model

For every candidate transaction, record separately:

1. Economic sufferer — who loses money/time/risk when the problem persists?
2. Beneficiary — who receives the benefit?
3. Budget owner — whose budget can fund the purchase?
4. Buyer/PO authority — who can authorize the vendor and issue the order?
5. User/operator — who consumes the service/artifact?
6. Acceptance authority — who decides whether the deliverable is accepted?
7. Legal/regulatory authority — who has statutory authority, if any?
8. Actual payer — which legal entity transfers money to us?
9. Payment mechanism — invoice/PO/advance/retainer/milestone/other.
10. Payment timing — before, on delivery, or after an external event.

## Payer Gate

A candidate cannot advance to "entry candidate" unless:
- a specific legal entity can be named as the payer;
- a plausible budget owner and buying authority can be named;
- the payer has an economic reason to buy now;
- payment does not depend on an unproven third-party reimbursement;
- our artifact/service is contractually bounded;
- regulatory/acceptance roles are not falsely attributed to us.

When beneficiary != payer, record the transfer mechanism explicitly. If no mechanism exists, commercial hypothesis is UNKNOWN.

## Payer matrix — current frontier

### Import → Production / Technical Preflight
Economic sufferer: importer when a shipment risks delay/rejection.
Beneficiary: importer, production unit, procurement/import function.
Likely payer: importing company as legal entity.
Likely budget owner: import/procurement/technical function; exact role UNKNOWN.
Buyer authority: company procurement/management; UNKNOWN for first transaction.
Acceptance authority: border conformity authority accepts/refuses the imported product, not our report.
Legal authority: Ministry of Commerce / competent frontier services in the relevant scope.
Payment mechanism hypothesis: fixed-fee preflight invoice paid by importer before shipment.
Pre-kill: import broker, customs, routine paperwork are existing functions/services.
Status: OPEN; payer willingness and role are unverified.
Source anchor: Ministry of Commerce states the importer or duly authorized representative files the conformity dossier and the authority issues admission/refusal outcomes.

### Contract → Execution → Acceptance → Payment
Economic sufferer: contractor when work cannot be accepted/billed/paid.
Beneficiary: contractor/project team.
Likely payer: contractor for B2B/private work or a subcontracting contractor. For public work, the public contracting authority pays the prime contractor; it does not automatically pay a new intermediary.
Budget owner: contractor/project/commercial/technical management; UNKNOWN.
Acceptance authority: contracting authority/client.
Legal authority: contract/public-procurement framework.
Payment mechanism hypothesis: subcontract/PO from contractor.
Pre-kill: generic tender writing, accounting, routine quantity surveying.
Critical payer problem: beneficiary and ultimate payer differ in public procurement; a new entrant lacks an obvious direct purchasing path unless the contractor itself buys the service.
Status: OPEN but lower entry priority until a real payer is identified.

### Incident → Insurance Claim
Economic sufferer: insured company with an asset loss.
Beneficiary: insured/company management.
Likely payer: insured company, broker/intermediary, or another contracted service buyer; UNKNOWN.
Acceptance authority: insurer/appointed expert.
Legal authority: insurer/expert/regulatory framework.
Pre-kill: generic insurance expertise is already supplied by qualified experts.
Potential artifact: technical evidence pack only.
Status: OPEN, high uncertainty and legal-boundary sensitivity.
Payer must not be assumed to be the insurer.

### Export Order → Compliance → Border → Payment
Economic sufferer: exporter if shipment/acceptance is delayed or rejected.
Beneficiary: exporter/manufacturer.
Likely payer: exporter legal entity; exact budget owner UNKNOWN.
Acceptance authority: CACQE and other destination/border authorities depending on product.
Legal authority: competent conformity/origin authorities.
Payment mechanism hypothesis: pre-shipment fixed-fee technical-readiness invoice.
Pre-kill: freight forwarding, generic origin paperwork, official certification.
Status: OPEN.
Source anchor: Ministry of Commerce says relevant export conformity requests include product/lot/quantity/destination requirements and manufacturer technical sheet; CACQE issues the conformity certificate in the relevant procedure.

### Asset → Operation → Hidden Loss
Economic sufferer: plant owner/operator.
Beneficiary: production/operations/finance.
Likely payer: plant/company.
Budget owner: plant manager, operations, maintenance, energy, or finance; UNKNOWN.
Acceptance authority: company management.
Payment mechanism hypothesis: fixed diagnostic fee; success-fee model not validated.
Pre-kill: generic dashboards and maintenance consulting.
Status: OPEN / high uncertainty.
Critical payer risk: decision-maker may prefer internal engineering staff or may not release data.

### Pharma regulatory data / serialization
Economic sufferer: importer/marketing authorization holder/manufacturer if serialization data are incomplete or inconsistent.
Beneficiary: pharmaceutical establishment/importer/regulatory-quality team.
Likely payer: Algerian pharmaceutical establishment/importer; UNKNOWN.
Budget owner: regulatory affairs/quality/IT/operations; UNKNOWN.
Acceptance authority: MIPH/other competent authority; our artifact is support, not official approval.
Pre-kill: serialization hardware/software already offered by local providers; MIPH provides regulatory guidance and preparation support.
Potential transaction: foreign-manufacturer ↔ Algerian importer ↔ registered product ↔ serialization data consistency/readiness.
Status: OPEN but not entry candidate until payer + unresolved private gap are proven.
Source anchor: MIPH current serialization guidance.

### Quality Nonconformity → Supplier → CAPA
Economic sufferer: buyer/manufacturer with defective incoming material or supplier failure.
Beneficiary: buyer quality/production.
Likely payer: buyer/manufacturer with the supplier relationship; sometimes supplier if contractually responsible, but do not assume.
Acceptance authority: buyer QA / customer depending on chain.
Pre-kill: internal QA/CAPA functions are common.
Potential niche: cross-company containment/evidence when supplier is external.
Status: OPEN / low priority until payment owner is proven.

### Hazardous Waste → Licensed Chain → Proof
Economic sufferer: waste generator facing compliance/traceability risk.
Beneficiary: waste generator/compliance department.
Likely payer: waste generator or industrial customer; licensed operator normally gets paid directly for regulated physical services.
Acceptance authority: environmental authority / generator receiving the service evidence.
Pre-kill: collector/transport/treatment operators already exist and are regulated.
Potential niche: private chain-integrity reconciliation across multiple parties.
Status: OPEN / expansion only until payer gap is proven.

### Cold-chain Excursion → Dispute/Acceptance
Economic sufferer: shipper, carrier, warehouse, receiver, or insurer depending on contractual allocation.
Beneficiary: party seeking to prove product integrity or assign responsibility.
Likely payer: contractually responsible party; UNKNOWN.
Acceptance authority: customer/receiver/insurer/regulator depending on event.
Pre-kill: transport, storage, and data-loggers already exist.
Potential niche: evidence reconciliation after an excursion/dispute.
Status: OPEN / payer ambiguity is currently a major blocker.

### Construction Variation → Contract Change / Claim
Economic sufferer: contractor or client depending on the variation.
Beneficiary: party whose position is strengthened by correct scope/measurement/evidence.
Likely payer: contractor for claim-preparation support; client for independent verification; UNKNOWN.
Acceptance authority: project owner/contracting authority.
Pre-kill: generic quantity surveying and tender preparation.
Potential niche: early detection of material scope drift before dispute.
Status: OPEN / legal-boundary and payer ambiguity.

## Cross-domain payment rule

The preferred first customer has:
- direct economic consequence;
- direct budget;
- direct authority;
- bounded problem;
- short time-to-artifact;
- payment independent of government reimbursement, insurance settlement, or downstream customer collection;
- no requirement that we hold regulated authority.

Preferred structure:
Company → PO → our bounded artifact/service → acceptance → payment

Avoid:
Company → us → wait for authority/insurer/customer → payment

## Research consequence

A Payer column is mandatory in:
- opportunity maps,
- research records,
- customer discovery,
- paid experiments,
- pricing hypotheses,
- kill tests.

Do not rank opportunities without payer evidence.

## Next payer experiments

For every surviving chain, the first buying-side questions are:
- Who currently signs the PO?
- From which budget?
- Who is accountable for the outcome?
- What event triggers purchase?
- What do you currently pay, to whom, and how?
- What happens if nobody buys the service?
- Can you authorize a 1-day / 1-week fixed-price job directly?

Evidence priority:
1. actual invoice/PO or signed paid engagement;
2. actual procurement request/budget line;
3. direct statement from buying authority tied to a real case;
4. observed internal workflow/job role;
5. public vendor offer;
6. general market report.

Only levels 1–3 should materially upgrade payer confidence.

## Negative rule

Never infer payer from beneficiary. Never infer willingness-to-pay from legal obligation. Never infer budget authority from job title alone. Record UNKNOWN when provenance is insufficient.

## 2026-09-23 method audit additions

Payer identity remains a hard gate, but payer alone does not establish entry feasibility.

Every candidate must now distinguish:
- Market opportunity: real economic problem + plausible spending.
- Entry feasibility: reachable buyer + direct authority + low enough capital/liability/sales friction + executable first delivery.

Add to every payer record:
- sales cycle;
- reachable channel;
- working-capital requirement;
- delivery cost/effort;
- liability exposure;
- time-to-cash;
- whether first transaction can be invoiced directly.

Do not upgrade payer confidence from novelty, regulation, beneficiary status, job title, or public vendor existence.

Paid evidence remains the strongest validation:
actual invoice/PO/paid engagement > stated intent.


## 2026-09-23 public-procurement correction

Do not treat public/para-public procurement as categorically inaccessible to new low-capital entrants.

Sonelgaz Decision N°225/PDG/2025 contains an explicit mechanism for needs that can be satisfied by small/very-small enterprises and labeled startups: such services should generally be reserved for them, and newly created micro-enterprises without a first-year balance sheet are not to be required to provide similar professional references; diploma-based references may be considered.

Payer implication:
The contracting Sonelgaz-group entity can be the direct payer, but procurement qualification, acceptance, guarantees and payment timing remain case-specific.

Research implication:
Test specific micro/small-eligible consultations/lots rather than broad public tenders.
