# Reproduce the finite checks

The resource laws are analytical theorems proved in the [scientific account](../science/model.md). The checks here test finite ingredients: the exact activation-process identities, the trajectory-level phase certificate, and the conditional-state invariant used by the lower bound.

## Run

Use Python 3.10 or later and install the declared numerical dependency. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The default command checks the committed outputs and does not rewrite them. It exits with an error if an invariant fails, a reference output is missing, or a recomputed result differs beyond the stated floating-point tolerance.

The committed outputs were generated and rechecked with Python 3.12.14 and NumPy 2.3.5. The dependency range in `requirements.txt` permits compatible NumPy releases; the tolerances below allow ordinary floating-point variation across environments.

| Check | Finite evidence | Scientific connection |
|---|---|---|
| [Activation and certification](check_process.py) | Exact rational pair-dilution probabilities at five mismatch values; independent logical activations at five switching values; 928 Boolean phase-certificate cases for sizes 3 through 8 | [Paired comparison](../science/paired-comparison.md) and [phase certificate](../science/upper-bounds.md) |
| [Memory potential](check_potential.py) | 18 scenarios, each with four marked inputs, 12 slots and a 12-dimensional algorithm space; phase projectors and response projectors with idle slots | [Conditional-state decomposition and potential bound](../science/lower-bounds.md) |

The potential calculation uses a fixed random seed, `20261018`, and switching rates `0.001, 0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99, 0.999`. It evolves the normalized density operators conditional on the hidden bit and separately evolves their subnormalized pure components. Random common unitaries exercise noncommuting controls. The response-projector cases also test a projector sum strictly smaller than the identity and slots with no query.

At every step it checks conditional trace normalization, positive-semidefinite remainders, the individual potential-growth inequality and its sum over marked inputs. The invariant tolerances are `1e-10` for positivity and normalization and `1e-9` for the potential inequalities. Comparison with the committed numerical output uses relative tolerance `1e-8` and absolute tolerance `1e-10` to allow ordinary floating-point variation.

## Expected result

The runner reports `passed: true`, 928 certificate cases, 18 potential scenarios, four marked inputs per scenario and 12 steps per input. In the committed run, the most negative residual eigenvalue is approximately $`-5.95\times10^{-16}`$ and the maximum trace error is approximately $`1.89\times10^{-15}`$, consistent with floating-point roundoff. The full outputs are [process.json](expected/process.json) and [potential.json](expected/potential.json).

For a scientifically reviewed change to a calculation, reference outputs can be regenerated explicitly:

```bash
python3 verification/run_all.py --record
python3 verification/run_all.py
```

Recording outputs is not an independent correctness check. Review the changed calculation and its relation to the written proof before accepting a new reference.

## Evidence boundary

Enumeration establishes the displayed finite cases. It does not prove the asymptotic bounds, the conditional success guarantee for all histories, the resource theorem for all adaptive algorithms, or bibliographic priority. Those statements rely on the [written proofs](../science/model.md#5-proof-dependencies) and [attributed primary sources](../references/RELATED_WORK.md). The numerical matrix calculation is a check of algebra and normalization, not a simulation of the full search algorithm or a hardware performance estimate.
