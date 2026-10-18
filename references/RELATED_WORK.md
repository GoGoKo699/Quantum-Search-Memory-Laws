# Related work and scientific context

## The question addressed here

Grover search achieves a quadratic reduction in oracle queries for unstructured search, and its square-root query scaling is optimal in the ideal black-box model [Grover96; BBBV97]. Under noise, the relevant question is which parts of that advantage survive a specified access process.

This work studies an unknown phase oracle $`O_w=I-2|w\rangle\langle w|`$, with the identity oracle representing the unmarked instance. A stationary, fair, hidden two-state Markov chain determines whether the oracle acts in each clock slot. Its switching probability is $`\delta`$. The algorithm can apply known controls and choose when to query, but cannot observe, reset, or control the hidden activation bit. The activation process continues through measurements, restarts, and idle intervals.

Writing $`r=\min\{\delta,1-\delta\}`$, the optimal actual-query and elapsed-slot costs at fixed bounded error are achieved simultaneously:

```math
q_*=\Theta\!\left(\sqrt N+rN\right),\qquad
T_*=\Theta\!\left(\sqrt N+rN+\delta^{-1}\right),
\qquad 0<\delta\leq1.
```

The distinction between these resources matters when the oracle can remain inactive for a long interval. In the call-driven convention, in which every advancing slot is itself a charged oracle call, the cost becomes $`Q=\Theta(\sqrt N+rN+\delta^{-1})`$.

For every switching rate, an input prepared independently of the hidden activation process sees the same single-slot averaged channel:

```math
\mathcal E_w(\rho)=\frac12\rho+\frac12O_w\rho O_w.
```

The result concerns computational information in a temporal access process that is absent from this single-use channel description. The comparisons below identify where established noisy-search results share the problem and where their access assumptions differ.

## Independent faulty oracles and search lower bounds

Regev and Schiff establish the central impossibility result for independent oracle omissions [RS08]. A faulty call applies the correct query with probability $`1-p`$ and otherwise applies the identity. Their lower bound is proportional to $`pN/(1-p)`$; every fixed positive omission probability destroys the quadratic search advantage. Their proof bounds arbitrary algorithms, rather than only the standard Grover circuit.

The independent point $`\delta=1/2`$ of the present Markov family recovers this linear-query obstruction. Extending the result to other switching rates requires accounting for correlations between the algorithm and a hidden activation state. The lower bound here tracks two conditional coherent components and penalizes the component antisymmetric under exchange of the hidden states. Substitution of an independent-call channel would discard that memory.

Shenvi, Brown, and Whaley study random oracle phase errors in discrete- and continuous-time search [SBW03]. Their analysis gives the sensitivity scale $`\epsilon_{\mathrm{rms}}=O(N^{-1/4})`$ for preserving Grover scaling, with an error-dependent regime proportional to $`\epsilon_{\mathrm{rms}}^2N`$. This is an important precedent for noise-dependent search crossovers. An interpolation between square-root search and an error-weighted linear term is not, by itself, a distinctive contribution of the present result.

Lolck, Mančinska, and Paraashar show that independent faulty access does not eliminate every quantum advantage: their general robustification preserves super-cubic query advantages [LMP24]. Their Section 4 also uses random omission to adjust a faulty oracle's effective failure probability. The [independent-pair comparison](../science/paired-comparison.md) here combines this dilution ingredient with the fair two-slot process to prove optimal cost $`\Theta(\sqrt N+\eta N)`$ for mismatch probability $`0\leq\eta\leq1/2`$. The stationary Markov result needs a separate lower bound because successive pairs share the hidden environment.

## Temporally correlated noise in Grover dynamics

Mandal, Ghoshal, Srivastava, and Sen analyze Grover search under a fixed local unitary error with classical memory [MGSS23]. Their two possible steps are

```math
G_w=R_sO_w,\qquad G'_w=\chi_mG_w,
```

where $`\chi_m`$ is a tensor product of a chosen single-qubit unitary on selected sites and identity elsewhere. Their transition rule is

```math
p(i\mid j)=(1-\mu)p_i+\mu\,\mathbf 1_{i=j}.
```

For $`p_0=p_1=1/2`$, its switching probability is exactly $`\delta=(1-\mu)/2`$. The stochastic memory family thus coincides with the persistent half of the present parameter range. Their lifted recurrence for the conditional states is directly relevant: introducing a classical memory register or diagonalizing a transfer operator is established methodology.

The quantum action differs. An omitted oracle leaves the diffusion step $`R_s`$ in place. Representing this in the notation above would require

```math
G'_w=R_s=\chi_wG_w,\qquad \chi_w=R_sO_wR_s.
```

This error depends on the unknown marked address and is generally nonlocal; it is not the fixed product error of [MGSS23]. Their analysis concerns specified noisy Grover dynamics and memory-dependent success curves. The present result determines optimal resource scaling over all admissible algorithms.

There is also a restart convention to distinguish. Section IV.1 of [MGSS23] compares repeated search runs through $`1-(1-P)^k`$, justified by independent trial successes. Under a continuously evolving hidden environment, a register reset does not itself produce independent trials. The present upper bound instead establishes success conditional on every prior history and includes elapsed mixing intervals explicitly.

Temporal-noise effects also appear in spatial search. Cattaneo, Rossi, Paris, and Maniscalco study continuous-time quantum walks with independent random telegraph noise on graph links [CRPM18]. Their Hamiltonian has a noisy transport term and a fixed marked-vertex term. This is a direct precedent for switching-rate-dependent search performance, with noise on graph dynamics rather than application of the unknown oracle.

## Dephasing and general noisy-query frameworks

Rosmanis proves the lower bound $`\Omega(\max\{Np,\sqrt N\})`$ for search with independent depolarizing or dephasing query noise, including a version in which the occurrence of the error is flagged [Ros23]. The full depolarizing query complexity is characterized up to logarithmic factors. These results establish that knowing whether irreversible damage occurred need not restore Grover search.

The 2024 addendum makes another access distinction explicit [Ros24]. Independent depolarization of one known query qubit both before and after the ideal oracle gives an $`\Omega(Np)`$ obstruction. If that single-qubit noise occurs only on one side of the oracle, adapted search retains quadratic speedups. Locality alone therefore does not classify a noisy-oracle model: placement of the noise within each query also matters.

Agarwal, Rao, and Song develop a lower-bound framework based on fractional block sensitivity [ARS26]. Their Section 6 permits arbitrary exogenous temporal correlations in dephasing flags, including Markov and long-range dependence. This theorem allows temporal correlation. Its conditional quantum actions, with the flag revealed after the query, are

```math
Z_t=0:\quad \mathcal O_x(\rho),
\qquad
Z_t=1:\quad \Delta_I\!\left(\mathcal O_x(\rho)\right),
```

where $`\Delta_I`$ completely dephases the query-index register. Theorem 6.3 gives a variational lower-bound resource using predictable conditional dephasing probabilities. Their negligent-oracle theorem is a separate result for repeated access to a fixed faulty channel.

The quantum operation associated with a hidden state is the decisive distinction from the present omission process. For an involutory oracle and two successive omission calls without intervening controls,

```math
O_w^{b_{t+1}}O_w^{b_t}=O_w^{b_{t+1}\oplus b_t}.
```

The averaged two-query action is therefore

```math
\rho\longmapsto(1-\delta)\rho+\delta O_w\rho O_w.
```

At zero switching it is exactly the identity: a later correlated application removes the first query's phase uncertainty. For an input independent of the same fair Markov flag process, indexed dephasing instead gives

```math
\rho\longmapsto
\frac{1-\delta}{2}\rho+
\frac{1+\delta}{2}\Delta_I(\rho).
```

Here an involutory ideal query commutes with indexed dephasing, and neither call dephases with probability $`(1-\delta)/2`$. A later ideal query does not undo dephasing. Identifying classical flag distributions consequently does not identify the quantum access processes. The correlated-dephasing framework is adjacent, but its hypotheses differ from the correlated-omission hypotheses.

## Oracle protection under local noise

Shen and Choi introduce oracle distillation, which constructs a high-fidelity Boolean oracle from noisy access [SC26]. Their noise families include bounded-Pauli-weight adversarial errors and independent per-qubit depolarization after an ideal query. Their weak-query construction uses this locality structure. Section VIII explicitly compares their setting with faulty omissions and identifies the nonlocal, function-dependent error associated with omitting the unknown oracle.

For the phase-reflection family, an omitted query is the desired query followed by the error $`O_w`$ itself. For $`N=2^n`$, let $`w_j`$ be the bits encoding the marked index $`w-1`$. Then

```math
O_w=
I-2^{1-n}\prod_{j=1}^n
\left(I+(-1)^{w_j}Z_j\right).
```

The expansion contains Pauli strings up to weight $`n`$, with coefficients depending on the marked address. Literal omission noise therefore does not belong to the bounded-fraction low-weight adversarial family. The distillation results and the present temporal-memory result concern different structures available for protecting oracle access.

The base distillation protocol should not be characterized as simply assuming free fractional queries: its weak queries are constructed from the stipulated noisy access. Fractional and continuous-query formulations are separate extensions of that work.

## Randomly selected constraint oracles

Dong, Li, and Ma study random selection among Grover operators associated with different constraint sets [DLM26]. The target is their intersection, and the motivation is to avoid constructing a potentially expensive global constraint oracle. Their two-operator theorem has a sparse-union condition relating the database size to the constraint sets and their intersection.

This is a relevant example of randomized Grover evolution with a provable search advantage. It does not specialize to omitted-oracle search by replacing one constraint with the entire domain: that substitution violates the theorem's sparse-union regime. The random choice is also an algorithmic choice among available constraint oracles, rather than an inaccessible stationary activation process.

## Contribution and scope

The contribution is an optimal resource law for a minimal stationary fault process. Its ingredients play different roles:

- The actual-query lower bound controls hidden environmental memory for arbitrary algorithms, including adaptive decisions to idle.
- The upper bound attains the lower-bound order without observing or resetting the environment.
- The elapsed-time lower bound accounts separately for long inactive intervals.
- The full switching range distinguishes persistence from anticorrelation, although both can support square-root query scaling near their respective endpoints.

For positive persistence, useful coherent intervals compete with the waiting time for oracle availability. Near perfect alternation, consecutive queries expose independent transition bits and produce reliable logical queries. Independent fair omissions recover the Regev–Schiff obstruction. These mechanisms explain why a single-use channel and a marginal error probability do not determine optimal search costs.

The setting remains a stationary, exogenous, two-state omission process with a known transition parameter and ideal known controls. It gives neither a general ordering of noise by a scalar measure of memory nor a fault-tolerance theorem for arbitrary hardware. Earlier work already establishes memory-dependent search performance, correlated dephasing bounds, and strong oracle protection under locality assumptions. The claim here is the sharp query/time characterization under its explicit access contract.

## Primary references

The keys below match the accompanying [structured bibliography](references.bib). Links point to publisher records or author-deposited texts.

The proof also uses standard ingredients outside noisy-search theory: the exact Grover success formula [BBHT98], decompositions of known controlled gates [Barenco95], and the pure-reference fidelity–trace-distance inequality [FG97]. Their uses are identified in the [upper](../science/upper-bounds.md) and [lower](../science/lower-bounds.md) proofs.

- **[Grover96]** Lov K. Grover, “A fast quantum mechanical algorithm for database search,” *Proceedings of the 28th Annual ACM Symposium on Theory of Computing*, pp. 212–219 (1996). [Author-deposited version](https://arxiv.org/abs/quant-ph/9605043).
- **[BBBV97]** Charles H. Bennett, Ethan Bernstein, Gilles Brassard, and Umesh Vazirani, “Strengths and Weaknesses of Quantum Computing,” *SIAM Journal on Computing* **26**(5), 1510–1523 (1997). [Author-deposited version](https://arxiv.org/abs/quant-ph/9701001).
- **[BBHT98]** Michel Boyer, Gilles Brassard, Peter Høyer, and Alain Tapp, “Tight bounds on quantum searching,” *Fortschritte der Physik* **46**, 493–506 (1998). [Author-deposited version](https://arxiv.org/abs/quant-ph/9605034).
- **[Barenco95]** A. Barenco, C. H. Bennett, R. Cleve, D. P. DiVincenzo, N. Margolus, P. Shor, T. Sleator, J. Smolin, and H. Weinfurter, “Elementary gates for quantum computation,” *Physical Review A* **52**, 3457–3467 (1995). [Publisher](https://doi.org/10.1103/PhysRevA.52.3457) · [Author-deposited version](https://arxiv.org/abs/quant-ph/9503016).
- **[FG97]** Christopher A. Fuchs and Jeroen van de Graaf, “Cryptographic Distinguishability Measures for Quantum Mechanical States,” arXiv:quant-ph/9712042 (1997; v2, 3 April 1998). [Author-deposited version](https://arxiv.org/abs/quant-ph/9712042).
- **[SBW03]** Neil Shenvi, Kenneth R. Brown, and K. Birgitta Whaley, “Effects of a random noisy oracle on search algorithm complexity,” *Physical Review A* **68**, 052313 (2003). [Publisher](https://doi.org/10.1103/PhysRevA.68.052313) · [Full text](https://arxiv.org/html/quant-ph/0304138v2).
- **[RS08]** Oded Regev and Liron Schiff, “Impossibility of a Quantum Speed-Up with a Faulty Oracle,” in *Automata, Languages and Programming*, ICALP 2008, *Lecture Notes in Computer Science* **5125**, pp. 773–781 (Springer, 2008). [Publisher](https://doi.org/10.1007/978-3-540-70575-8_63) · [Full text](https://arxiv.org/html/1202.1027v1). The arXiv deposit dates from 2012; the conference publication is from 2008.
- **[CRPM18]** Marco Cattaneo, Matteo A. C. Rossi, Matteo G. A. Paris, and Sabrina Maniscalco, “Quantum spatial search on graphs subject to dynamical noise,” *Physical Review A* **98**, 052347 (2018). [Publisher](https://doi.org/10.1103/PhysRevA.98.052347) · [Author-deposited version](https://arxiv.org/abs/1809.01969).
- **[MGSS23]** Sheikh Parvez Mandal, Ahana Ghoshal, Chirag Srivastava, and Ujjwal Sen, “Invariance of success probability in Grover's quantum search under local noise with memory,” *Physical Review A* **107**, 022427 (2023). [Publisher](https://doi.org/10.1103/PhysRevA.107.022427) · [Full text, v4](https://arxiv.org/html/2112.02640v4).
- **[Ros23]** Ansis Rosmanis, “Quantum Search with Noisy Oracle,” arXiv:2309.14944v1 (26 September 2023). [Author-deposited version](https://arxiv.org/abs/2309.14944).
- **[Ros24]** Ansis Rosmanis, “Addendum to ‘Quantum Search with Noisy Oracle’,” arXiv:2405.11973v1 (20 May 2024). [Full text](https://arxiv.org/html/2405.11973v1).
- **[LMP24]** David Rasmussen Lolck, Laura Mančinska, and Manaswi Paraashar, “Quantum Advantage with Faulty Oracle,” arXiv:2411.04931v1 (7 November 2024). [Full text](https://arxiv.org/html/2411.04931v1).
- **[DLM26]** Dekuan Dong, Yingzhou Li, and Jiaxin Ma, “Random Grover Search,” arXiv:2606.11759v2 (2 July 2026; first submitted 10 June 2026). [Full text](https://arxiv.org/html/2606.11759v2).
- **[SC26]** Ruohan Shen and Soonwon Choi, “Oracle Distillation,” arXiv:2609.31596v1 (25 September 2026). [Full text](https://arxiv.org/html/2609.31596v1).
- **[ARS26]** Mehil Agarwal, Shravas Rao, and Fang Song, “Noisy Quantum Query Complexity via Fractional Block Sensitivity,” arXiv:2610.00506v2 (2 October 2026; first submitted 30 September 2026). [Full text](https://arxiv.org/html/2610.00506v2).
