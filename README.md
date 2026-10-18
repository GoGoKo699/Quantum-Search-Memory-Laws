# Quantum Search Memory Laws

**How do temporal correlations in hidden oracle failures change the optimal cost of quantum search?** A stationary oracle that is inactive half the time can support very different search costs depending on its switching rate. This project gives matching bounds for actual oracle calls and elapsed oracle slots.

The hidden activation bit switches each slot with supplied probability $`0<\delta\le1`$. There is at most one marked item among $`N\ge3`$ indices. Write $`r=\min\{\delta,1-\delta\}`$. In the clock-driven model, idling advances the hidden process and costs elapsed time but no oracle call.

| Resource | Optimal quantum cost | Optimal classical cost |
|---|---:|---:|
| Actual oracle calls | $`\Theta(\sqrt N+rN)`$ | $`\Theta(N)`$ |
| Elapsed oracle slots | $`\Theta(\sqrt N+rN+\delta^{-1})`$ | $`\Theta(N+\delta^{-1})`$ |

**One algorithm simultaneously attains both bounds** in each computational model, with fixed worst-case budgets and success at least $`9/10`$. The comparison uses the same bit-oracle interface. The quantum upper bound also holds with ordinary, uncontrolled phase access and uses an exact certificate with zero false positives.

When $`\delta\ll1/N`$, quantum search retains its quadratic reduction in actual calls, while both quantum and classical elapsed times become $`\Theta(1/\delta)`$. Waiting for activation can determine completion time even when fewer queries suffice.

If the environment advances only when a physical oracle call is consumed, every mixing call is charged. In that call-driven model the quantum optimum is $`\Theta(\sqrt N+rN+\delta^{-1})`$ and the classical optimum is $`\Theta(N+\delta^{-1})`$.

## Read the science

Start with the [model, exact statements and proof dependencies](science/model.md). The [lower-bound proof](science/lower-bounds.md) separates ideal-search, memory-loss and availability obstructions. The [quantum constructions](science/upper-bounds.md) and [classical comparison](science/classical-comparison.md) attain the resource laws. The [interpretation](science/interpretation.md) connects the mechanisms and limiting regimes.

| To inspect | Read |
|---|---|
| Clock conventions, access assumptions and main theorems | [Model](science/model.md) |
| Lower bounds for arbitrary adaptive algorithms | [Hidden-memory potential](science/lower-bounds.md) |
| Fixed schedules, conditional mixing and exact phase verification | [Upper bounds](science/upper-bounds.md) |
| Matched classical bit-oracle baseline | [Classical comparison](science/classical-comparison.md) |
| Weighted reflection families and identity-input fractional block sensitivity | [Weighted extension](science/weighted-extension.md) |
| Independent pair refresh and its mismatch law | [Paired-process comparison](science/paired-comparison.md) |
| Regime table and physical resource meaning | [Interpretation](science/interpretation.md) |
| Established ingredients and closest noise models | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Reproducible finite calculations | [Verification](verification/README.md) |

[The LLM reading guide](llms.txt) maps scientific questions to their authoritative files.

## Learn the project

The single educational anchor is Andrew M. Childs's *Lecture Notes on Quantum Algorithms* (17 April 2025). The [30-milestone map](learning/MILESTONES.md) develops 12 background/preliminary milestones and 18 narrative/innovation milestones, progressing from local ingredients to global understanding within each phase. Each milestone has a central question, an understanding target, dependencies and source pointers.

The [Childs-to-project bridge](learning/CHILDS_BRIDGE.md) gives the targeted source readings, translates ideal-query notation, and supplies the mixed-state, hidden-memory and distinguishability steps needed for this problem. The map and bridge lead to the authoritative scientific files above; they do not require reading the entire lecture course first.

## Reproduce the finite checks

From the repository root, run:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The suite checks exact activation identities and phase-certification cases, then tests the conditional-state and potential inequalities in finite numerical examples. The default command compares with committed outputs without rewriting them. Universal and asymptotic statements follow from the written proofs, rather than the finite checks.

## Scope

The hidden process is stationary, fair, external, unobserved and not resettable. Its switching probability is supplied. All verification calls and waiting slots are counted. No fault flags, known-unmarked reference, ideal verification oracle or QRAM is used by the constructions.

Known controls are ideal. Elapsed slots count a discrete oracle-interaction clock with control operations between slots; they are not a full device wall-clock or gate-depth estimate. Preparation, known-gate and counter costs are specified in the [resource account](science/upper-bounds.md#7-preparation-known-gates-workspace-and-output). The permanently inactive endpoint prevents the required success at $`\delta=0`$; perfect alternation at $`\delta=1`$ is included.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
