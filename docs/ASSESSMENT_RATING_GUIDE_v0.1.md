# Assessment Rating Guide v0.1

This guide defines the interpretation of the 0–5 assessment dimensions used by `schema/assessment.schema.json`.

Scores are measurements of the current evidence packet, not truth values and not irreversible portfolio decisions.

## Technical substance

- 0: no usable implementation evidence
- 1: minimal or unresolved implementation surface
- 2: concrete prototype or partial implementation
- 3: substantive implementation with bounded scope
- 4: substantial architecture plus executable implementation
- 5: substantial system with multiple integrated implementation surfaces

## Validation / evidence

- 0: no validation evidence
- 1: documentation-only or unexecuted claims
- 2: partial executable evidence or inspected tests
- 3: deterministic/local executable evidence
- 4: strong automated validation with meaningful bounded coverage
- 5: current-head automated validation plus reproducible execution/build artifacts

A score of 5 does not mean production readiness.

## Strategic value

- 0–1: little demonstrated relevance to the current working corpus
- 2: relevant but peripheral
- 3: useful supporting value
- 4: direct reusable/supporting value for a core path
- 5: current target or critical support surface for the current portfolio operating path

This dimension is intentionally owner/context dependent and must include an evidence basis.

## Reuse potential

- 0–1: no reusable implementation evidence
- 2: local or narrow reuse
- 3: reusable subsystem or documented primitive
- 4: clear cross-project primitive/architecture reuse potential
- 5: intentionally modular primitive or control-plane surface with direct cross-project applicability

## Completion cost

For this portfolio, a higher value means **more remaining engineering/revalidation effort** to close the currently known scope.

- 0–1: little remaining work for the assessed scope
- 2: low remaining effort
- 3: moderate remaining effort
- 4: high remaining effort or several important open gates
- 5: substantial production/research validation frontier remains

Completion cost is not a recommendation to stop work. It is a planning signal.

## Confidence

Each dimension carries its own confidence:

- high: directly supported by current repository/ref/CI or strong executable evidence
- medium: evidence-supported but includes interpretation or bounded extrapolation
- low: limited evidence
- unknown: insufficient evidence to justify the score

A score with medium confidence must not be presented as an established fact.
