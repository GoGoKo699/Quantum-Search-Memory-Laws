# From Childs’s ideal queries to search with a hidden oracle clock

The educational anchor is Andrew M. Childs, [*Lecture Notes on Quantum Algorithms*, 17 April 2025](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), available from the [author’s course page](https://www.cs.umd.edu/~amchilds/qa/). All page numbers below are **printed page numbers**.

| Selected reading | Relevant locations | Connection |
| --- | --- | --- |
| Chapter 1, pp. 1–3 | States, operations, measurement | Ideal circuit language |
| Chapter 19, pp. 87–90 | §19.1, p. 87; §19.3, pp. 88–89 | Search reflections; amplification through a quantum walk |
| Chapter 21, pp. 97–102 | §§21.1–21.2, pp. 97–98; §21.6, pp. 100–101 | Query interfaces; polynomial lower bounds |
| Chapter 23, pp. 109–114 | §§23.1–23.3, pp. 109–113 | Distinguishability and adversary progress |

The density-operator and probability arguments below supply additional steps needed by this project. The omission theorem is in the [scientific model and proofs](../science/model.md#4-main-resource-theorem). Childs is the reading anchor; the scientific files identify the research sources used in those proofs.

## 1. From ideal queries to the project contract

There are $`N\ge3`$ possible addresses and **at most one** marked address $`w`$. The no-mark input is $`\varnothing`$. The required output is the marked index or “no mark,” with probability at least $`0.9`$ on every input. The project’s ordinary phase oracle is

```math
O_w=I-2|w\rangle\langle w|,
\qquad O_{\varnothing}=I.
```

Here $`\varnothing`$ labels an input, not an extra address known to be unmarked.

Some similarly named source operations have different access requirements:

| Childs notation | Project translation |
| --- | --- |
| Bit oracle $`\widehat O_x`$, Eq. (21.2) | Supplied XOR-bit oracle $`U_w`$ when $`x_j=\mathbf1[j=w]`$ |
| Phase oracle $`O_x`$, Eq. (21.3) | Acts as $`(-1)^{a x_j}`$; its response sector $`a=0`$ is inactive |
| Restriction to $`a=1`$ | Project’s ordinary phase oracle $`O_w`$ |
| Marked reflection $`2\Pi_M-I`$, §19.1 | Negative of the project’s marked reflection |

The response bit $`a`$ in this table is not the hidden activation bit introduced below. The bit interface supplies a phase call by preparing its response in $`|-\rangle`$. An ordinary phase call alone does not supply the coherent inactive sector of Eq. (21.3).

Childs's query input length $`n`$ corresponds to this search space size $`N`$, while the address register uses $`\lceil\log_2N\rceil`$ qubits. His uniform state $`|S\rangle`$ becomes the project's $`|s\rangle`$.

Changing a reflection’s sign is a global phase along a fixed ordinary-call trajectory; it need not remain global under coherent control. Likewise, §19.1’s two-query implementation of its marked reflection does not set this project’s native phase-call cost. These distinctions matter whenever a construction or lower bound is transferred between interfaces.

All known controls are ideal. The upper bounds receive no controlled phase oracle, fault flag, reset of the noise, or QRAM. See the [access contract](../science/model.md#1-search-task-and-access).

## 2. A hidden classical bit requires density operators

A density operator $`\rho`$ is positive semidefinite with trace one. A measurement effect $`0\preceq M\preceq I`$ occurs with probability $`\mathrm{tr}(M\rho)`$. A random ensemble has state

```math
\rho=\sum_\ell p_\ell|u_\ell\rangle\langle u_\ell|.
```

This is generally different from the outer product of the mean amplitude vector. For example, a fair mixture of $`(|j\rangle+|a\rangle)/\sqrt2`$ and $`(|j\rangle-|a\rangle)/\sqrt2`$ is $`(|j\rangle\langle j|+|a\rangle\langle a|)/2`$. The mean vector’s outer product instead has trace $`1/2`$.

A channel written as

```math
\Phi(\rho)=\sum_\ell K_\ell\rho K_\ell^\dagger,
\qquad
\sum_\ell K_\ell^\dagger K_\ell=I
```

preserves trace by cyclicity. It is completely positive: after adding any untouched auxiliary system, each summand still maps a positive operator to a positive operator. Such maps are called CPTP. An isolated fair omission has operators $`I/\sqrt2`$ and $`O_w/\sqrt2`$. Repeatedly composing this channel would assume fresh omissions and would erase the correlations studied here.

At a fixed clock time, retain the hidden classical state formally as

```math
\Omega_t=
\frac12|0\rangle\langle0|\otimes\rho_t^{w,0}
+\frac12|1\rangle\langle1|\otimes\rho_t^{w,1},
\qquad
\rho_t^w=\frac{\rho_t^{w,0}+\rho_t^{w,1}}2.
```

The conditional states contain the algorithm’s measurement records. The hidden register is inaccessible; tracing it out gives the algorithm’s actual state. The fair weights describe the unconditional process at fixed time, not the posterior after an observed history.

## 3. Fair marginals do not reset a posterior

The supplied parameter $`0<\delta\le1`$ specifies

```math
b_1\sim\mathrm{Bernoulli}(1/2),
\qquad b_{t+1}=b_t\oplus z_t,
\qquad z_t\overset{\mathrm{iid}}\sim\mathrm{Bernoulli}(\delta).
```

A call in slot $`t`$ applies $`O_w^{b_t}`$. In the clock-driven model, idle slots also advance the chain. This is an external activation process; it is not the algorithmic quantum walk in Chapter 19.

Chapter 19 uses $`\delta`$ for a walk spectral gap and $`\epsilon`$ for a marked fraction. Neither symbol there denotes this project's hidden flip probability or its required error probability.

Write $`\kappa=1-2\delta`$. If the past observed history is $`H`$ and $`a_H=\Pr(b_t=1\mid H)`$, the Markov recursion gives

```math
\Pr(b_{t+g}=1\mid H)
=\frac12+\kappa^g\left(a_H-\frac12\right).
```

For $`\delta\le1/2`$, taking $`g=\lceil\ln2/(2\delta)\rceil`$ makes this probability at least $`1/4`$ for every history. Preparing a fresh search register alone does not do so.

The upper proof therefore establishes a success probability $`s`$ conditional on every preceding failed-trial history. Repeated conditioning gives failure at most $`(1-s)^M`$ after $`M`$ trials. Independent restarts are unnecessary. This is the role of [charged mixing intervals](../science/upper-bounds.md#41-mixing-is-conditional-on-the-entire-preceding-history).

## 4. A complete phase-only certificate

Take $`N=3`$, measured candidate $`j=1`$, and references $`2,3`$. To test a reference $`a`$, prepare

```math
|+_{1,a}\rangle=\frac{|1\rangle+|a\rangle}{\sqrt2},
\qquad
|-_{1,a}\rangle=\frac{|1\rangle-|a\rangle}{\sqrt2},
```

make one ordinary phase call, and measure in this two-state basis. An active call changes plus to minus, up to global phase, exactly when the two addresses have different membership. An omitted call leaves plus.

Execute both tests and accept candidate $`1`$ only on two minus outcomes. If $`w=1`$ and both calls are active, both tests succeed. If $`w=2`$, the test using reference $`3`$ always fails; if $`w=3`$, the other test always fails. With no mark, both fail. Thus acceptance is **exactly sound on every fault trajectory**, although omissions can cause false negatives.

For general $`N\ge3`$, use two distinct references different from the candidate. At most one can be the actual mark when the candidate is wrong. The certificate costs exactly two calls and two consecutive slots, with known preparation and measurement controls. It returns a classical acceptance bit, enabling a measured candidate index to become a certified output. It needs neither a known unmarked reference nor an ideal verifier. The [complete construction](../science/upper-bounds.md#2-a-phase-only-certificate-with-exact-soundness) uses the same phase interface as search.

## 5. From final outputs to a positive component potential

Chapter 23 suggests tracking progress that a successful final measurement must force. Its Fact 23.1 concerns pure states. Here the noisy marked-input state is mixed, so an additional bridge is needed.

Define $`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$. The positive and negative parts of $`\rho-\sigma`$ have equal trace; maximizing $`\mathrm{tr}(M(\rho-\sigma))`$ over effects selects its positive part. Consequently every event-probability difference is at most $`D`$.

For a pure reference $`|\psi\rangle`$ and a decomposition $`\rho=\sum_\ell p_\ell|u_\ell\rangle\langle u_\ell|`$,

```math
\begin{aligned}
D(\rho,|\psi\rangle\langle\psi|)
&\le \sum_\ell p_\ell
\sqrt{1-|\langle\psi|u_\ell\rangle|^2}\\
&\le \sqrt{1-\langle\psi|\rho|\psi\rangle}.
\end{aligned}
```

The pure-state expression follows by diagonalizing the difference in the span of two vectors; convexity and concavity of the square root give the displayed inequalities. In the squared-fidelity convention, the overlap $`\langle\psi|\rho|\psi\rangle`$ is the fidelity with the pure reference. This is the pure-reference fidelity bound attributed to Fuchs–van de Graaf in the [scientific references](../science/lower-bounds.md#references).

The next device keeps useful coherent vectors without claiming they describe the entire mixed state. For any vectors $`u,v`$ and $`0\le p\le1`$,

```math
\begin{aligned}
p|u\rangle\langle u|+(1-p)|v\rangle\langle v|
={}&|pu+(1-p)v\rangle\langle pu+(1-p)v|\\
&+p(1-p)|u-v\rangle\langle u-v|.
\end{aligned}
```

The final term is positive semidefinite. Iterating this identity produces subnormalized vectors beneath the hidden-bit conditional densities. With their half-sum $`s_w`$ and half-difference $`d_w`$,

```math
\rho_w\succeq|s_w\rangle\langle s_w|+|d_w\rangle\langle d_w|.
```

The positive-component method’s Regev–Schiff lineage and the precise memory recurrence are given in [Lemma 2](../science/lower-bounds.md#5-positive-components-and-the-memory-recurrence).

The no-mark reference $`\psi`$ can be kept pure. Success $`0.9`$ on both no-mark and marked inputs forces $`D\ge0.8`$, hence $`|\langle\psi|s_w\rangle|\le0.6`$ and $`\|\psi-s_w\|\ge0.4`$. The memory-sensitive progress quantity is

```math
F_w=\|\psi-s_w\|^2+
\frac{2}{1+\kappa^2}\|d_w\|^2.
```

A query swaps the marked portions of $`s_w,d_w`$; the hidden transition multiplies the difference component by $`\kappa`$. The coefficient balances these effects. The [growth and terminal-separation proof](../science/lower-bounds.md#6-growth-and-terminal-separation) supplies the algebra, including negative $`\kappa`$.

## 6. Why the proof charges queries and time separately

For adaptive algorithms, keep measurement outcomes and untouched copies, and control subsequent actions on the records. This preserves classical branching statistics while giving a pure enlarged no-mark state. It does not reveal the environment. The lower proof allows an additional enable sector to represent query schedules; that strengthening grants no controlled oracle to the upper construction.

If $`K`$ is the actual call count, $`q`$ caps calls, and $`T`$ caps elapsed slots, with $`K\le q\le T`$, then

```math
\sum_{t=1}^{T}\Pr_{\varnothing}(\text{call in slot }t)
=\mathbb E_{\varnothing}K\le q.
```

Idle slots send $`d_w`$ to $`\kappa d_w`$ and cannot increase the potential. Summing its growth over alternatives therefore charges actual query occupancy and yields $`q=\Omega(rN)`$, where $`r=\min(\delta,1-\delta)`$. Ordinary ideal-query search lower bounds also survive exact simulation of the omissions, giving $`\Omega(\sqrt N)`$. Separately, the all-inactive trajectory has probability $`(1-\delta)^{T-1}/2`$, imposing an availability cost in elapsed time.

For the upper bound, reflect about the known uniform state $`|s\rangle`$ and the marked subspace. Their product rotates the marked/unmarked plane by $`2\theta`$, with $`\theta=\arcsin(1/\sqrt N)`$. The project’s [Grover/BBHT calculation](../science/upper-bounds.md#3-a-uniform-bound-for-short-grover-runs) gives marked probability $`\sin^2((2m+1)\theta)`$ after $`m`$ iterations. This exact formula is not derived in the selected Childs §19.3. Short coherent runs, mixing, and certification attain the persistent-regime bound. In the alternating regime, two consecutive calls without intervening controls satisfy

```math
O_w^{b_{2k}}O_w^{b_{2k-1}}=O_w^{z_{2k-1}}.
```

Different pairs use independent flips. Each logical call costs two physical calls; at $`\delta=1`$ it is ideal. Together the bounds give simultaneous fixed budgets

```math
q_Q=\Theta(\sqrt N+rN),
\qquad
T_Q=\Theta(\sqrt N+rN+1/\delta).
```

The fair, permanently frozen endpoint $`\delta=0`$ cannot support the required success.

The [classical comparison](../science/classical-comparison.md#1-resource-theorem) supplies both algorithms with the same coherent bit interface, with classical algorithms using classical queries:

```math
q_C=\Theta(N),
\qquad T_C=\Theta(N+1/\delta).
```

Thus $`\delta\ll1/N`$ preserves a query advantage while availability dominates both elapsed times. In the call-driven model, waiting requires calls, so the corresponding $`T`$ expressions become the call bounds.

These are discrete oracle-clock budgets, not total circuit running times. The [implementation convention](../science/upper-bounds.md#7-preparation-known-gates-workspace-and-output) permits exact known one-qubit rotations, gives polynomial-in-$`\log N`$ gates per useful operation and $`O(\log N)`$ quantum workspace, and outputs $`O(\log N)`$ classical bits. Explicit counters need $`O(\log N+\log(T+1))`$ classical bits. The supplied $`\delta`$ chooses the budgets; no rate-estimation procedure is assumed.

## 7. Weighted alternatives and the identity reference

Chapter 23’s weighted-input progress viewpoint also motivates asking which hard alternatives can share a limited query budget. Here the specific packing condition is

```math
\omega_a\ge0,
\qquad
\sum_a\omega_aP_a\preceq I,
\qquad
W=\sum_a\omega_a.
```

For alternatives $`I-2P_a`$ whose required outputs differ from an identity reference input’s output, it yields $`\mathbb E_{\mathrm{ref}}K\ge(4/25)rW`$. This nonnegative operator packing is not Childs’s general adversary matrix.

For Boolean inputs, coordinate packing of sensitive blocks gives the [fractional block sensitivity bound at the identity input](../science/weighted-extension.md#2-fractional-block-sensitivity-at-the-identity-input), $`0^n`$. It does not establish a maximum over arbitrary reference inputs or matching upper bounds for general functions.

The restriction has an operational reason. A known XOR translation applied after a faulty bit query gives $`U_aU_x^b`$, whereas a translated faulty oracle should give $`U_{x\oplus a}^b=U_a^bU_x^b`$. On an omitted call, the first applies $`U_a`$ and the second applies identity. Without the missing activation flag, that mismatch cannot be silently removed. The [fixed-reference discussion](../science/weighted-extension.md#4-why-the-reference-input-remains-fixed) makes this boundary explicit.

[30-milestone map](MILESTONES.md) · [Scientific entrypoint](../science/model.md) · [Repository overview](../README.md)
