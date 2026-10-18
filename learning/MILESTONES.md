# Thirty milestones for search with hidden oracle memory

This map organizes the project's mathematical story into **12 background and preliminary milestones** followed by **18 narrative and innovation milestones**. The first phase moves from individual states and oracle actions to the complete search task and its clocks. The second moves from local certification and composition identities to optimal algorithms, universal lower bounds, resource comparisons, and the weighted extension. M12 and M30 provide the respective phase syntheses.

The allocation reflects the structure of the result. Twelve milestones establish the shared language of quantum queries, hidden classical memory, distinguishability, and resource accounting. Eighteen then connect the distinct constructive mechanisms, the memory-sensitive converse, and their consequences. Each milestone names an ingredient that supports the scientific argument.

The selected educational anchor is Childs's [*Lecture Notes on Quantum Algorithms*][childs]. The [Childs bridge](CHILDS_BRIDGE.md) records the selected edition and passage locations, clarifies notation and access conventions, and supplies foundations absent from those passages. The linked files in [science](../science/model.md) remain the authoritative homes of the definitions and proofs. Childs pointers identify relevant conceptual entries; they do not attribute the project's noisy-oracle statements to the notes.

## Navigable index

**Phase I — Background and preliminaries**

| Milestone | Milestone | Milestone |
|---|---|---|
| [M01 States and relative phase](#m01-states-and-relative-phase) | [M02 Three oracle interfaces](#m02-three-oracle-interfaces) | [M03 Hidden randomness and mixed states](#m03-hidden-randomness-and-mixed-states) |
| [M04 Distinguishability and positive order](#m04-distinguishability-and-positive-order) | [M05 Grover reflection geometry](#m05-grover-reflection-geometry) | [M06 Short coherent runs and their costs](#m06-short-coherent-runs-and-their-costs) |
| [M07 The two-state memory process](#m07-the-two-state-memory-process) | [M08 Adaptive histories at a finite horizon](#m08-adaptive-histories-at-a-finite-horizon) | [M09 Actual calls and elapsed slots](#m09-actual-calls-and-elapsed-slots) |
| [M10 Progress against an identity reference](#m10-progress-against-an-identity-reference) | [M11 Weighted projector packing](#m11-weighted-projector-packing) | [M12 Synthesis of the complete contract](#m12-synthesis-of-the-complete-contract) |

**Phase II — Narrative and innovation**

| Milestone | Milestone | Milestone |
|---|---|---|
| [M13 An exact phase-only certificate](#m13-an-exact-phase-only-certificate) | [M14 Active windows after every history](#m14-active-windows-after-every-history) | [M15 Persistent search with fixed budgets](#m15-persistent-search-with-fixed-budgets) |
| [M16 Alternation exposes independent innovations](#m16-alternation-exposes-independent-innovations) | [M17 A simultaneous constructive bound](#m17-a-simultaneous-constructive-bound) | [M18 The availability obstruction](#m18-the-availability-obstruction) |
| [M19 Positive components conditioned on memory](#m19-positive-components-conditioned-on-memory) | [M20 Symmetric and antisymmetric components](#m20-symmetric-and-antisymmetric-components) | [M21 A balanced progress potential](#m21-a-balanced-progress-potential) |
| [M22 Terminal separation and call occupation](#m22-terminal-separation-and-call-occupation) | [M23 The optimal quantum resource law](#m23-the-optimal-quantum-resource-law) | [M24 The classical optimum on a common interface](#m24-the-classical-optimum-on-a-common-interface) |
| [M25 When query and time advantages differ](#m25-when-query-and-time-advantages-differ) | [M26 The independent-pair mechanism](#m26-the-independent-pair-mechanism) | [M27 Equality of complete access processes](#m27-equality-of-complete-access-processes) |
| [M28 The weighted Markov bound](#m28-the-weighted-markov-bound) | [M29 Fractional block sensitivity at the identity](#m29-fractional-block-sensitivity-at-the-identity) | [M30 Synthesis of mechanisms, resources, and scope](#m30-synthesis-of-mechanisms-resources-and-scope) |

## Phase I: Background and preliminaries

### M01 States and relative phase

**Central question.** How can a phase mark change an observed outcome while leaving every address label unchanged?

**Understanding target.** A search register carries amplitudes over valid addresses; known unitary operations convert their relative phases into measurement probabilities. A phase multiplying an entire isolated state has no observable effect, whereas a phase between two address components can be detected by interference.

**Dependencies and story role.** This is the local starting point. It supplies the meaning of the oracle reflection, the two-address certificate, and the basis-state dummy calls.

**Conceptual connection.** The information supplied by a phase oracle resides in relations between amplitudes. This makes the choice of accessible registers and reference states part of the computational model.

**Sources.** [Model §1](../science/model.md#1-search-task-and-access); [upper bounds §2](../science/upper-bounds.md#2-a-phase-only-certificate-with-exact-soundness); [Childs §§1.1–1.2, p1][childs].

### M02 Three oracle interfaces

**Central question.** Which operations are supplied by an ordinary phase oracle, a coherent bit oracle, and a coherently enabled oracle?

**Understanding target.** The ordinary reflection is $`O_w=I-2|w\rangle\langle w|`$. Preparing the bit oracle's response in $`|-\rangle`$ gives phase kickback. An additional coherent enable sector belongs to the stronger model used for the lower bound; the phase-only upper bound receives no such sector.

**Dependencies and story role.** [M01](#m01-states-and-relative-phase) supplies relative phase. This milestone fixes the interfaces before any algorithm or comparison is counted.

**Conceptual connection.** Childs §21.2 includes an answer/control bit in its phase-query notation. Restriction to its active sector gives the ordinary phase action, while the full interface retains extra coherent control.

**Sources.** [Model §1](../science/model.md#1-search-task-and-access); [lower bounds §2](../science/lower-bounds.md#2-access-models-used-in-the-proof); [Childs §21.2, p98][childs]; [bridge §1](CHILDS_BRIDGE.md#1-from-ideal-queries-to-the-project-contract).

### M03 Hidden randomness and mixed states

**Central question.** What state description preserves correlations between an algorithm and an unobserved activation bit?

**Understanding target.** Density operators describe the algorithm after the hidden randomness is averaged out. Conditional operators $`\rho_t^{w,0}`$ and $`\rho_t^{w,1}`$ retain the information needed to propagate that average. The oracle and ideal controls define completely positive, trace-preserving evolution; a register reset leaves the external hidden process intact.

**Dependencies and story role.** [M01](#m01-states-and-relative-phase) and [M02](#m02-three-oracle-interfaces) identify the quantum system and its actions. This milestone supplies the state language for the memory-aware proof.

**Conceptual connection.** Classical uncertainty about which unitary acted and quantum coherence within the algorithm coexist in one joint state. Averaging the hidden bit too early can erase their correlation.

**Sources.** [Model §2](../science/model.md#2-stationary-hidden-process); [lower bounds §§4–5](../science/lower-bounds.md#4-a-fixed-horizon-normal-form); [bridge §2](CHILDS_BRIDGE.md#2-a-hidden-classical-bit-requires-density-operators).

### M04 Distinguishability and positive order

**Central question.** How can a positive component of a mixed state constrain the probability of a correct final answer?

**Understanding target.** Trace distance bounds differences in measurement probabilities. Positive semidefinite order gives a precise meaning to retaining a subnormalized component: $`\rho\succeq|\phi\rangle\langle\phi|`$. Against a normalized pure reference, the inequality $`D(\rho,|\psi\rangle\langle\psi|)\le\sqrt{1-\langle\psi|\rho|\psi\rangle}`$ connects output separation to component overlap.

**Dependencies and story role.** [M01](#m01-states-and-relative-phase) and [M03](#m03-hidden-randomness-and-mixed-states) supply states and mixtures. These relations will provide both the preserved positive component and the terminal lower-bound condition.

**Conceptual connection.** Observable decision error becomes a geometric separation requirement. The component need not equal the entire state to impose that requirement.

**Sources.** [Lower bounds Lemmas 2 and 4](../science/lower-bounds.md#lemma-2-conditional-positive-components); [Childs §23.1, p109][childs] for the pure-state adversary entry; [bridge §5](CHILDS_BRIDGE.md#5-from-final-outputs-to-a-positive-component-potential) for the mixed-state ingredients.

### M05 Grover reflection geometry

**Central question.** Why does alternating a known reflection and a marked reflection accumulate useful amplitude?

**Understanding target.** The uniform state and the marked direction determine an invariant two-dimensional plane. In that plane, $`G=R_sO_w`$, with $`R_s=2|s\rangle\langle s|-I`$, is a rotation whose angle is set by the initial marked overlap.

**Dependencies and story role.** [M01](#m01-states-and-relative-phase) and [M02](#m02-three-oracle-interfaces) give the phase and access conventions. This local geometry is the coherent engine used inside every search trial.

**Conceptual connection.** A product of reflections turns a small overlap into accumulated rotation. Childs §19.1 uses the opposite sign for the marked reflection; that sign is an overall phase in a fixed ordinary-query sequence, without giving a controlled-oracle conversion.

**Sources.** [Upper bounds §3](../science/upper-bounds.md#3-a-uniform-bound-for-short-grover-runs); [Childs §19.1, p87][childs]; [bridge §1](CHILDS_BRIDGE.md#1-from-ideal-queries-to-the-project-contract).

### M06 Short coherent runs and their costs

**Central question.** How much marked probability can a deliberately short coherent interval create?

**Understanding target.** With $`\theta=\arcsin(N^{-1/2})`$, the exact success probability after $`m`$ ideal steps is $`\sin^2((2m+1)\theta)`$. A suitably bounded integer choice of $`m`$ gives a uniform lower bound of order $`m^2/N`$, including small database sizes. The number of unknown-oracle calls is distinct from the known gates used to prepare and reflect the state.

**Dependencies and story role.** [M05](#m05-grover-reflection-geometry) supplies the rotation; [M02](#m02-three-oracle-interfaces) fixes what a call means. This milestone makes coherence-window length a resource variable.

**Conceptual connection.** Quadratic amplitude accumulation can be useful before a full Grover run is completed.

**Sources.** [Upper bounds §§3,7](../science/upper-bounds.md#3-a-uniform-bound-for-short-grover-runs) for the exact formula, uniform bound, and implementation accounting; [Childs §19.3, pp88–89][childs] as the conceptual amplitude-amplification entry, with its quantum-walk formulation.

### M07 The two-state memory process

**Central question.** What changes with the switching probability when every fixed slot still has a fair activation bit?

**Understanding target.** The supplied parameter $`0<\delta\le1`$ defines $`b_{t+1}=b_t\oplus z_t`$ with independent $`z_t\sim\mathrm{Bernoulli}(\delta)`$ and fair $`b_1`$. The transition modes have eigenvalues $`1`$ and $`\kappa=1-2\delta`$. Thus persistence and alternation occupy opposite ends of the same family, while $`r=\min\{\delta,1-\delta\}`$ measures proximity to either deterministic endpoint.

**Dependencies and story role.** [M03](#m03-hidden-randomness-and-mixed-states) supplies conditional states. The two transition modes organize both the constructive regimes and the lower-bound potential.

**Conceptual connection.** Stationarity fixes an unconditional marginal; it does not fix the posterior after an algorithm's observed history.

**Sources.** [Model §2](../science/model.md#2-stationary-hidden-process); [upper bounds §4.1](../science/upper-bounds.md#41-mixing-is-conditional-on-the-entire-preceding-history); [bridge §3](CHILDS_BRIDGE.md#3-fair-marginals-do-not-reset-a-posterior).

### M08 Adaptive histories at a finite horizon

**Central question.** How can one argument cover private randomness, intermediate measurements, and decisions to query, idle, or stop?

**Understanding target.** A fixed horizon permits retained classical outcome records, purified private randomness, and branch-dependent ideal controls. Stopped branches can remain idle. In the stronger lower-bound model, a coherent enable flag represents these classical scheduling decisions while preserving their probabilities; the external chain advances at every elapsed slot.

**Dependencies and story role.** [M02](#m02-three-oracle-interfaces) supplies the stronger interface, and [M03](#m03-hidden-randomness-and-mixed-states) supplies the state description. This milestone fixes the scope of “arbitrary algorithms.”

**Conceptual connection.** Deferring measurements changes the representation of a computation while retained records preserve the operational meaning of its classical schedule.

**Sources.** [Lower bounds §4](../science/lower-bounds.md#4-a-fixed-horizon-normal-form); [Childs §21.2, p98][childs] for the ideal query-sequence starting point; [bridge §6](CHILDS_BRIDGE.md#6-why-the-proof-charges-queries-and-time-separately).

### M09 Actual calls and elapsed slots

**Central question.** Which resource is consumed when the algorithm waits for an inaccessible oracle to become available?

**Understanding target.** In the clock-driven model the random number of actual calls satisfies $`K\le q\le T`$, with fixed worst-case budgets $`q`$ and $`T`$. Idle slots advance the hidden chain without adding calls. In the call-driven model every advancing slot consumes a charged query, including dummy calls. Known-gate cost, quantum workspace, classical counters, and output length are separate implementation quantities.

**Dependencies and story role.** [M06](#m06-short-coherent-runs-and-their-costs), [M07](#m07-the-two-state-memory-process), and [M08](#m08-adaptive-histories-at-a-finite-horizon) identify useful operations, memory evolution, and schedules. This milestone establishes the two-resource statement used throughout.

**Conceptual connection.** An interaction clock measures access opportunities; it is not a specification of physical gate durations.

**Sources.** [Model §§3,6](../science/model.md#3-two-clock-contracts); [upper bounds §7](../science/upper-bounds.md#7-preparation-known-gates-workspace-and-output); [Childs §1.6, p3][childs]; [bridge §6](CHILDS_BRIDGE.md#6-why-the-proof-charges-queries-and-time-separately).

### M10 Progress against an identity reference

**Central question.** How can local limits on oracle-dependent change force a global search lower bound?

**Understanding target.** The no-mark oracle leaves a common reference evolution. Marked inputs must eventually become distinguishable from it, while input-independent controls preserve the relevant geometric relations. Hybrid or adversary arguments connect terminal separation to the amount of query amplitude that can be distributed over possible marked addresses.

**Dependencies and story role.** [M02](#m02-three-oracle-interfaces), [M04](#m04-distinguishability-and-positive-order), [M08](#m08-adaptive-histories-at-a-finite-horizon), and [M09](#m09-actual-calls-and-elapsed-slots) specify access, separation, and costs. This milestone supplies the architecture of the coherent search floor.

**Conceptual connection.** A local progress bound becomes a search lower bound only after it is summed over alternatives sharing the same reference.

**Sources.** [Lower bounds §7](../science/lower-bounds.md#7-the-coherent-search-lower-bound-counts-actual-calls); [Childs §§23.1–23.3, pp109–113][childs]; [Childs §21.6, pp100–101][childs] for the polynomial-method search comparison.

### M11 Weighted projector packing

**Central question.** How can alternatives share query coordinates without being counted as independent uses of the same amplitude?

**Understanding target.** Nonnegative weights $`\omega_a`$ and projectors $`P_a`$ obeying $`\sum_a\omega_aP_a\preceq I`$ impose a local capacity constraint. It follows that $`\sum_a\omega_a\|P_a\psi\|^2\le\|\psi\|^2`$. Neither pairwise orthogonality nor commutation of the projectors is required.

**Dependencies and story role.** [M02](#m02-three-oracle-interfaces), [M04](#m04-distinguishability-and-positive-order), and [M10](#m10-progress-against-an-identity-reference) supply reflections, positive order, and summed progress. This milestone prepares the extension beyond singleton marked addresses.

**Conceptual connection.** A weighted packing translates overlap among alternative inputs into a bound on total information-bearing query occupation.

**Sources.** [Weighted extension §1](../science/weighted-extension.md#1-an-operator-packing-theorem); [Childs §23.2, pp110–112][childs] for the query-projector progress structure; [bridge §7](CHILDS_BRIDGE.md#7-weighted-alternatives-and-the-identity-reference).

### M12 Synthesis of the complete contract

**Central question.** What precisely is the computational task once states, memory, access, and clocks are specified together?

**Understanding target.** For $`N\ge3`$, the input has at most one marked address, and the required output is that address or `none` with probability at least $`9/10`$ on every input. The supplied switching parameter, fair stationary chain, ideal known controls, inaccessible environment, and finite resource budgets define one complete process. Ordinary phase access supports the construction, coherent bit access supports the common comparison, and stronger coherent enable access supports the converse.

**Dependencies and story role.** M01–M11 combine here: [M02](#m02-three-oracle-interfaces) fixes access, [M07](#m07-the-two-state-memory-process) fixes memory, [M08](#m08-adaptive-histories-at-a-finite-horizon) fixes algorithmic scope, and [M09](#m09-actual-calls-and-elapsed-slots) fixes accounting. This closes the background phase.

**Conceptual connection.** Complexity belongs to the full access contract, including which hidden events advance during waiting and which output must be certified.

**Sources.** [Model §§1–3,6–7](../science/model.md); [bridge §§1–3,6](CHILDS_BRIDGE.md).

## Phase II: Narrative and innovation

### M13 An exact phase-only certificate

**Central question.** How can a candidate be certified without a known unmarked address or a free ideal verifier?

**Understanding target.** For candidate $`j`$, two distinct references $`a_1,a_2\ne j`$ support two tests of $`(|j\rangle+|a_i\rangle)/\sqrt2`$ in the plus/minus basis. Both query slots are consumed. A true candidate passes whenever both calls act; a false candidate has at least one entirely unmarked test and can never pass both. The same soundness holds on the no-mark input for every noise trajectory.

**Dependencies and story role.** [M01](#m01-states-and-relative-phase), [M02](#m02-three-oracle-interfaces), and [M12](#m12-synthesis-of-the-complete-contract) give interference and the exact access contract. This is the first local component of the construction.

**Conceptual connection.** Exact soundness follows from the at-most-one-mark promise and two distinct reference addresses, without requiring independent activation bits.

**Sources.** [Upper bounds §2](../science/upper-bounds.md#2-a-phase-only-certificate-with-exact-soundness); [bridge §4](CHILDS_BRIDGE.md#4-a-complete-phase-only-certificate).

### M14 Active windows after every history

**Central question.** What makes a new trial useful when preceding observations may have strongly biased the hidden-bit posterior?

**Understanding target.** For $`0<\delta\le1/2`$, a mixing gap of $`g=\lceil\ln2/(2\delta)\rceil`$ slots gives a lower bound on activation conditional on every complete preceding history. With a suitable $`m=\Theta(\min\{\sqrt N,\delta^{-1}\})`$, the event that all $`m+2`$ useful slots act has conditional probability at least $`1/16`$.

**Dependencies and story role.** [M06](#m06-short-coherent-runs-and-their-costs), [M07](#m07-the-two-state-memory-process), [M08](#m08-adaptive-histories-at-a-finite-horizon), and [M13](#m13-an-exact-phase-only-certificate) identify the coherent interval, conditional dynamics, and certificate. This produces a uniform success opportunity.

**Conceptual connection.** Mixing can restore a quantitative lower bound after arbitrary histories while the environment continues evolving without a reset.

**Sources.** [Upper bounds §§4.1–4.2](../science/upper-bounds.md#41-mixing-is-conditional-on-the-entire-preceding-history); [bridge §3](CHILDS_BRIDGE.md#3-fair-marginals-do-not-reset-a-posterior).

### M15 Persistent search with fixed budgets

**Central question.** How do uniformly useful coherent windows become a bounded-cost search algorithm?

**Understanding target.** Each trial succeeds with conditional probability at least $`m^2/(16N)`$. A fixed $`M=\Theta(N/m^2)`$ trials reduce failure below $`1/10`$ by repeated conditioning. The same schedule uses $`q=M(m+2)`$ actual calls and $`T=M(g+m+2)`$ elapsed slots, giving $`q=O(\sqrt N+\delta N)`$ and $`T=O(\sqrt N+\delta N+\delta^{-1})`$.

**Dependencies and story role.** [M09](#m09-actual-calls-and-elapsed-slots) supplies accounting, and [M14](#m14-active-windows-after-every-history) supplies the history-uniform event. This assembles the persistent half of the upper bound.

**Conceptual connection.** Multiplication of conditional failure bounds requires a uniform guarantee after each history; it does not require independent trials.

**Sources.** [Upper bounds §4.3](../science/upper-bounds.md#43-fixed-budget-amplification-and-both-resource-bounds).

### M16 Alternation exposes independent innovations

**Central question.** How can strong anticorrelation turn individually unreliable calls into reliable logical access?

**Understanding target.** Two consecutive calls on the same register with no intervening operation obey $`O_w^{b_{t+1}}O_w^{b_t}=O_w^{z_t}`$. On disjoint pairs, the relevant innovations are independent. For $`1/2\le\delta\le1`$, this produces a logical oracle with omission probability $`1-\delta`$ at the cost of two actual calls; at $`\delta=1`$, every logical call is perfect.

**Dependencies and story role.** [M02](#m02-three-oracle-interfaces), [M07](#m07-the-two-state-memory-process), and [M13](#m13-an-exact-phase-only-certificate) supply involutory access, innovations, and verification. This is the second local constructive mechanism.

**Conceptual connection.** Composition cancels the unknown entering activation bit and exposes the independently generated transition bit.

**Sources.** [Upper bounds §5](../science/upper-bounds.md); [model §2](../science/model.md#2-stationary-hidden-process).

### M17 A simultaneous constructive bound

**Central question.** What does one complete algorithm cost across the full switching range, including its known operations and output?

**Understanding target.** The two constructions attain $`q=O(\sqrt N+rN)`$ and $`T=O(\sqrt N+rN+\delta^{-1})`$ simultaneously, with fixed budgets and zero false positives. Uniform preparation works for arbitrary $`N`$ without QRAM. In the stated ideal-gate model, known gates cost $`O((\sqrt N+rN)\log^2N)`$, improved to $`O((\sqrt N+rN)\log N)`$ for powers of two. Quantum workspace is $`O(\log N)`$; classical storage includes $`O(\log N+\log(T+1))`$ for records and counters. The answer is one address or `none`.

**Dependencies and story role.** [M06](#m06-short-coherent-runs-and-their-costs), [M09](#m09-actual-calls-and-elapsed-slots), [M15](#m15-persistent-search-with-fixed-budgets), and [M16](#m16-alternation-exposes-independent-innovations) combine local mechanisms into the full constructive statement.

**Conceptual connection.** Supplying a state-preparation circuit and charging certification makes the query claim an explicit algorithm; the oracle clock remains separate from physical gate time.

**Sources.** [Upper bounds §§1,4–7](../science/upper-bounds.md); [model §6](../science/model.md#6-preparation-verification-and-time-units); [Childs §§1.2–1.6, pp1–3][childs].

### M18 The availability obstruction

**Central question.** Why can elapsed time be large even if few actual calls are sufficient once the oracle acts?

**Understanding target.** The probability that all $`T`$ slots are inactive is $`\tfrac12(1-\delta)^{T-1}`$. On that event, a marked input produces the no-mark evolution regardless of the schedule. Success $`9/10`$ on both inputs forces this event to have small probability, yielding $`T=\Omega(\delta^{-1})`$ in the persistent regime. At $`\delta=0`$, the same obstruction prevents the required success.

**Dependencies and story role.** [M07](#m07-the-two-state-memory-process), [M08](#m08-adaptive-histories-at-a-finite-horizon), [M09](#m09-actual-calls-and-elapsed-slots), and [M17](#m17-a-simultaneous-constructive-bound) identify the hidden trajectory, schedule, and upper-bound waiting term. This isolates the elapsed-time converse.

**Conceptual connection.** An event carrying no input information imposes a deadline obstruction even when ideal controls are unrestricted.

**Sources.** [Lower bounds §8](../science/lower-bounds.md#8-availability-and-the-endpoints); [model §7](../science/model.md#7-endpoints-and-scope); [bridge §6](CHILDS_BRIDGE.md#6-why-the-proof-charges-queries-and-time-separately).

### M19 Positive components conditioned on memory

**Central question.** Which coherent information can be retained through correlated random omissions without replacing them by independent noise?

**Understanding target.** Each normalized conditional state admits a maintained component $`\rho_t^{w,b}\succeq|\phi_t^{w,b}\rangle\langle\phi_t^{w,b}|`$. The components update by weighted means under the Markov transition. The positive residual follows from the identity that a mixture of two pure outer products exceeds the outer product of their weighted mean by a positive rank-one operator.

**Dependencies and story role.** [M03](#m03-hidden-randomness-and-mixed-states), [M04](#m04-distinguishability-and-positive-order), and [M08](#m08-adaptive-histories-at-a-finite-horizon) supply conditional states, order, and the normal form. This begins the universal noisy-query converse after [M18](#m18-the-availability-obstruction) separates availability.

**Conceptual connection.** A tractable coherent component can be followed inside a larger mixed state while retaining the hidden-memory dependence.

**Sources.** [Lower bounds §5, Lemma 2](../science/lower-bounds.md#lemma-2-conditional-positive-components); [bridge §§2,5](CHILDS_BRIDGE.md#5-from-final-outputs-to-a-positive-component-potential).

### M20 Symmetric and antisymmetric components

**Central question.** Which coordinates reveal how the oracle action interacts with the two memory modes?

**Understanding target.** Define $`s=(\phi_0+\phi_1)/2`$ and $`d=(\phi_0-\phi_1)/2`$. The reduced state satisfies $`\rho\succeq|s\rangle\langle s|+|d\rangle\langle d|`$. For the query projector $`P_w`$, one oracle-and-mixing step obeys

```math
s'=(I-P_w)s+P_wd,\qquad
d'=\kappa\bigl((I-P_w)d+P_ws\bigr).
```

The sign of $`\kappa`$ is retained, including the alternating regime.

**Dependencies and story role.** [M07](#m07-the-two-state-memory-process) supplies the transition modes, and [M19](#m19-positive-components-conditioned-on-memory) supplies the coherent components. This produces the local recurrence on which progress is bounded.

**Conceptual connection.** Diagonalizing the classical transition separates an average component from a memory imbalance, while the marked reflection exchanges their projected parts.

**Sources.** [Lower bounds §5](../science/lower-bounds.md#5-positive-components-and-the-memory-recurrence); [bridge §5](CHILDS_BRIDGE.md#5-from-final-outputs-to-a-positive-component-potential).

### M21 A balanced progress potential

**Central question.** What quantity limits information gain while accounting for the coherence stored in the memory imbalance?

**Understanding target.** For $`0<\delta<1`$, the potential

```math
F^w=\|\psi-s^w\|^2+\frac{2}{1+\kappa^2}\|d^w\|^2
```

has one-slot growth at most $`A_\delta\|P_w\psi\|^2`$, where $`A_\delta=(1-2\delta+2\delta^2)/[\delta(1-\delta)]\le1/r`$. Completing squares gives this bound for either sign of $`\kappa`$. A wholly idle slot has nonpositive growth.

**Dependencies and story role.** [M04](#m04-distinguishability-and-positive-order), [M10](#m10-progress-against-an-identity-reference), and [M20](#m20-symmetric-and-antisymmetric-components) supply geometry, progress architecture, and the exact recurrence. This is the local inequality supporting the universal converse.

**Conceptual connection.** The coefficient balances distance from the reference against coherence that remains correlated with hidden memory.

**Sources.** [Lower bounds §6, Lemma 3](../science/lower-bounds.md#lemma-3-one-slot-growth); [bridge §5](CHILDS_BRIDGE.md#5-from-final-outputs-to-a-positive-component-potential).

### M22 Terminal separation and call occupation

**Central question.** How does the local potential inequality constrain every adaptive algorithm's actual calls?

**Understanding target.** Correctness gives trace distance at least $`4/5`$ from the pure no-mark reference, hence $`|\langle\psi,s^w\rangle|\le3/5`$ and $`F_T^w\ge4/25`$. Summing over marks uses $`\sum_wP_w\preceq J`$, where $`J`$ is the query-enable projector. The accumulated reference occupation is exactly $`\mathbb E_{\varnothing}K`$, yielding $`q\ge\mathbb E_{\varnothing}K\ge(4/25)rN`$.

**Dependencies and story role.** [M04](#m04-distinguishability-and-positive-order), [M08](#m08-adaptive-histories-at-a-finite-horizon), [M09](#m09-actual-calls-and-elapsed-slots), and [M21](#m21-a-balanced-progress-potential) connect output error, schedules, accounting, and local growth. This completes the memory-dependent query lower bound.

**Conceptual connection.** An adaptive algorithm's own reference-history query probabilities provide the accounting measure, so idle time cannot be charged as oracle-dependent progress.

**Sources.** [Lower bounds §§4,6](../science/lower-bounds.md#6-growth-and-terminal-separation); [bridge §§5–6](CHILDS_BRIDGE.md#6-why-the-proof-charges-queries-and-time-separately).

### M23 The optimal quantum resource law

**Central question.** How do coherent search, unpredictable switching, and availability combine into matching resource bounds?

**Understanding target.** An ideal oracle can simulate the noise trajectory privately using at most the original number of actual calls, preserving the ideal $`\Omega(\sqrt N)`$ search floor. Combining this with the memory and availability bounds matches the construction:

```math
q_*=\Theta(\sqrt N+rN),\qquad
T_*=\Theta(\sqrt N+rN+\delta^{-1}).
```

Both costs are attained by one algorithm. In the call-driven contract, mixing intervals are charged dummy calls and $`Q_*=\Theta(\sqrt N+rN+\delta^{-1})`$. The point $`\delta=1`$ is covered by perfect paired access.

**Dependencies and story role.** [M10](#m10-progress-against-an-identity-reference), [M17](#m17-a-simultaneous-constructive-bound), [M18](#m18-the-availability-obstruction), and [M22](#m22-terminal-separation-and-call-occupation) assemble the complete optimal quantum statement.

**Conceptual connection.** Separate obstructions can be combined because they constrain the same task and the same budgets; their sum and maximum differ only by constants.

**Sources.** [Model §4](../science/model.md#4-main-resource-theorem); [lower bounds §§3,7–9](../science/lower-bounds.md); [upper bounds §6](../science/upper-bounds.md#6-call-driven-accounting-and-the-excluded-endpoint); [Childs §21.6, pp100–101, and §23.3, p113][childs] for the ideal search floor.

### M24 The classical optimum on a common interface

**Central question.** What comparison isolates a quantum advantage while giving both algorithms the same informative oracle?

**Understanding target.** On the common bit-oracle interface, classical search attains $`q_{\mathrm C}=\Theta(N)`$ and $`T_{\mathrm C}=\Theta(N+\delta^{-1})`$ simultaneously. Bounded random-bit sampling, conditional active windows, and paired calls give fixed-budget upper bounds. An ideal-oracle no-mark transcript coupling supplies the linear actual-call lower bound, and availability supplies the time term. Sampling, counters, and the returned address are included in the implementation account.

**Dependencies and story role.** [M02](#m02-three-oracle-interfaces), [M09](#m09-actual-calls-and-elapsed-slots), [M14](#m14-active-windows-after-every-history), [M16](#m16-alternation-exposes-independent-innovations), and [M23](#m23-the-optimal-quantum-resource-law) establish common access and comparable resources. This supplies the classical baseline.

**Conceptual connection.** A computational comparison requires matched interfaces as well as matched noise and clocks.

**Sources.** [Classical comparison §§1–7](../science/classical-comparison.md); [model §1](../science/model.md#1-search-task-and-access); [Childs §19.1, p87][childs].

### M25 When query and time advantages differ

**Central question.** In which regimes does a reduction in oracle calls also shorten completion time?

**Understanding target.** Comparing the two optimal laws gives separate query and elapsed-time speedups. For $`\delta\ll N^{-1}`$, quantum search still uses order $`\sqrt N`$ actual calls, but both elapsed times are dominated by $`\delta^{-1}`$. Near perfect alternation, $`1-\delta\lesssim N^{-1/2}`$ supports square-root quantum costs in both resources. The scales $`N^{-1/2}`$ and $`N^{-1}`$ have different roles on the persistent side. Under call-driven accounting, the charged-query comparison equals the elapsed-slot comparison.

**Dependencies and story role.** [M23](#m23-the-optimal-quantum-resource-law) and [M24](#m24-the-classical-optimum-on-a-common-interface) supply matching quantum and classical laws. This turns the formulas into a regime-level interpretation.

**Conceptual connection.** Query reduction and access latency describe distinct computational benefits.

**Sources.** [Interpretation §§1–2](../science/interpretation.md); [classical comparison §§5–6](../science/classical-comparison.md#6-query-advantage-and-elapsed-time-advantage); [model §3](../science/model.md#3-two-clock-contracts).

### M26 The independent-pair mechanism

**Central question.** What can be established when correlations occur inside known, independently refreshed pairs?

**Understanding target.** For $`0\le\eta\le1/2`$, pair probabilities $`P_{00}=P_{11}=(1-\eta)/2`$ and $`P_{01}=P_{10}=\eta/2`$ make matched pairs of Grover steps produce either $`I`$ or $`G^2`$. Conditioned on all $`B`$ pairs matching, the accumulated action is $`G^{2K}`$ with $`K\sim\mathrm{Binomial}(B,1/2)`$. A suitable $`B=\Theta(\min\{\sqrt N,\eta^{-1}\})`$, taking $`B=\Theta(\sqrt N)`$ at $`\eta=0`$, yields candidate probability of order $`B^2/N`$. Charged certification and fixed trials give $`Q=O(\sqrt N+\eta N)`$.

**Dependencies and story role.** [M05](#m05-grover-reflection-geometry), [M06](#m06-short-coherent-runs-and-their-costs), [M13](#m13-an-exact-phase-only-certificate), and [M16](#m16-alternation-exposes-independent-innovations) supply reflection composition, short-run bounds, and certification. This introduces the supporting pair comparison.

**Conceptual connection.** Correlated faults can produce pauses and coherent double steps when the interposed known control is part of the composition.

**Sources.** [Independent-pair comparison §§1–3](../science/paired-comparison.md); [upper bounds §2](../science/upper-bounds.md#2-a-phase-only-certificate-with-exact-soundness).

### M27 Equality of complete access processes

**Central question.** When does simulation of a noisy oracle transfer a lower bound to algorithms with arbitrary intervening controls?

**Understanding target.** A shared private coin, combined with independent omissions, reproduces the complete two-slot pair distribution. Equality of this process preserves the algorithm's evolution through adaptive interposed operations, transferring the faulty-oracle lower bound and giving $`Q=\Theta(\sqrt N+\eta N)`$. Stationary Markov pairs share an environment, so the independent-pair reduction does not supply their universal converse or remove their availability cost.

**Dependencies and story role.** [M08](#m08-adaptive-histories-at-a-finite-horizon), [M10](#m10-progress-against-an-identity-reference), and [M26](#m26-the-independent-pair-mechanism) supply arbitrary controls, lower-bound transfer, and the paired law. This completes the comparison and fixes its boundary.

**Conceptual connection.** Equality of a marginal channel is weaker than equality of the sequence of conditional quantum actions accessible to an algorithm.

**Sources.** [Independent-pair comparison §§4–5](../science/paired-comparison.md#4-lower-bound-by-equality-of-the-full-two-slot-process); [related work: independent faulty oracles](../references/RELATED_WORK.md#independent-faulty-oracles-and-search-lower-bounds); [bridge §6](CHILDS_BRIDGE.md#6-why-the-proof-charges-queries-and-time-separately).

### M28 The weighted Markov bound

**Central question.** Which part of the memory-dependent lower bound survives beyond singleton marked addresses?

**Understanding target.** For alternatives $`R_a=I-2P_a`$ with outputs separated from an identity reference, a packing $`\sum_a\omega_aP_a\preceq I`$ and total weight $`W=\sum_a\omega_a`$ give $`\mathbb E_0K\ge(4/25)rW`$. The same positive-component and potential lemmas apply to each reflection. Only the final weighted occupation sum changes; overlapping or noncommuting alternative projectors are allowed.

**Dependencies and story role.** [M11](#m11-weighted-projector-packing), [M21](#m21-a-balanced-progress-potential), and [M22](#m22-terminal-separation-and-call-occupation) provide packing, local growth, and terminal separation. This identifies the general mathematical content of the search converse.

**Conceptual connection.** The number of search alternatives is a special case of a weighted amount of distinguishable reflection structure.

**Sources.** [Weighted extension §1](../science/weighted-extension.md#1-an-operator-packing-theorem), invoking [lower bounds Lemmas 2–4](../science/lower-bounds.md#lemma-2-conditional-positive-components); [bridge §7](CHILDS_BRIDGE.md#7-weighted-alternatives-and-the-identity-reference).

### M29 Fractional block sensitivity at the identity

**Central question.** How does the weighted reflection bound become a Boolean-function statement, and why is its reference input fixed?

**Understanding target.** For a nonconstant promised Boolean function whose domain contains $`0^n`$, sensitive blocks there define a fractional packing with coordinate capacities one. Their bit-oracle reflection projectors realize $`\mathrm{fbs}(f,0^n)`$. With $`Q_{0.1}(f)`$ denoting ideal bounded-error bit-query complexity, the resulting bounds are

```math
q=\Omega\!\left(Q_{0.1}(f)+r\,\mathrm{fbs}(f,0^n)\right),\qquad
T=\Omega\!\left(Q_{0.1}(f)+r\,\mathrm{fbs}(f,0^n)+\delta^{-1}\right).
```

These are necessary bounds, without a matching upper claim for arbitrary functions. A known input translation also acts on omitted slots, so it does not preserve this noise model or justify maximizing the sensitivity over reference inputs.

**Dependencies and story role.** [M02](#m02-three-oracle-interfaces), [M18](#m18-the-availability-obstruction), [M23](#m23-the-optimal-quantum-resource-law), and [M28](#m28-the-weighted-markov-bound) supply the bit interface, availability, ideal simulation, and weighted theorem. This completes the extension with its exact domain of applicability.

**Conceptual connection.** A symmetry of an ideal query problem need not be a symmetry of faulty access.

**Sources.** [Weighted extension §§2–5](../science/weighted-extension.md#2-fractional-block-sensitivity-at-the-identity-input); [bridge §7](CHILDS_BRIDGE.md#7-weighted-alternatives-and-the-identity-reference).

### M30 Synthesis of mechanisms, resources, and scope

**Central question.** Which information about the full access process explains the resource law and supports valid comparisons with other noise models?

**Understanding target.** The term $`\sqrt N`$ expresses the coherent search floor, $`rN`$ expresses the memory-dependent progress obstruction, and $`\delta^{-1}`$ expresses availability. Persistent windows and paired innovations attain the corresponding bounds. The common bit-oracle baseline distinguishes query advantage from elapsed-time advantage; independently refreshed pairs and the identity-reference extension identify precisely which arguments transfer.

**Dependencies and story role.** [M23](#m23-the-optimal-quantum-resource-law) supplies optimality, [M25](#m25-when-query-and-time-advantages-differ) supplies the regime comparison, [M27](#m27-equality-of-complete-access-processes) supplies the process boundary, and [M29](#m29-fractional-block-sensitivity-at-the-identity) supplies the extension boundary. Together with the [M12 contract synthesis](#m12-synthesis-of-the-complete-contract), these complete the global scientific story.

**Conceptual connection.** For a fresh input independent of the hidden bit, all switching rates share the same fair single-use averaged channel, while their temporal access costs differ. Related-work comparisons therefore specify the conditional quantum action, temporal law, revealed information, and resource contract. Hidden omissions, irreversible dephasing, fixed local gate errors, and prescribed noisy Grover dynamics support different statements.

**Sources.** [Model §§4–7](../science/model.md#4-main-resource-theorem); [interpretation §§3–4](../science/interpretation.md#3-what-the-lower-bound-adds); [related work and scientific context](../references/RELATED_WORK.md); [independent-pair comparison §5](../science/paired-comparison.md#5-relation-to-stationary-memory); [weighted extension §§4–5](../science/weighted-extension.md#4-why-the-reference-input-remains-fixed).

[Childs bridge](CHILDS_BRIDGE.md) · [Scientific entrypoint](../science/model.md) · [Repository overview](../README.md)

[childs]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf
