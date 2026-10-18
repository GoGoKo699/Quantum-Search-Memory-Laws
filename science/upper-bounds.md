# Constructive bounds for stationary Markov oracle omissions

Let $`N\ge3`$ and let $`w\in[N]`$ be the unique marked index, if one exists. The phase oracle is
```math
O_w=I-2|w\rangle\langle w|,
\qquad O_{\varnothing}=I.
```
The label $`\varnothing`$ denotes the no-mark instance; it is not an additional query state. The hidden activation process satisfies
```math
b_1\sim\operatorname{Bernoulli}(1/2),
\qquad
b_{t+1}=b_t\oplus z_t,
\qquad
z_t\stackrel{\mathrm{iid}}{\sim}\operatorname{Bernoulli}(\delta),
\qquad 0<\delta\le1.
```
An oracle call in slot $`t`$ applies $`O_w^{b_t}`$. Both $`N`$ and $`\delta`$ are supplied for choosing the integer block and mixing budgets; estimating the switching rate from oracle observations is not part of the construction. Write $`r=\min\{\delta,1-\delta\}`$. All logarithms below are natural.

The algorithm has no observation of the activation bits, no operation that resets the hidden process, and no controlled-oracle access. Known gates, measurements, preparation of fresh work registers, and classical processing are available. Preparing a fresh algorithm register does not reset or refresh the oracle's hidden state.

## 1. The two timing contracts

In the **clock-driven model**, the hidden bit advances once per elapsed discrete slot. A slot contains either one oracle call or an idle. Let $`q`$ count actual oracle calls and $`T`$ count elapsed slots, so $`q\le T`$. Idle time costs $`T`$ but does not cost $`q`$.

In the **call-driven model**, the hidden bit advances only when an oracle call is consumed. Ordinary waiting does not advance the process. A mixing interval must therefore use actual dummy oracle calls, and every such call is charged to the single resource $`Q`$.

Both contracts use an ideal oracle-interaction clock: known controls occur between slots. The gate counts in Section 7 account for those controls separately. The elapsed-slot bound does not identify an oracle slot with the depth of a full implementation on a particular device.

### Constructive theorem

There is a quantum algorithm that outputs the marked index with probability at least $`0.9`$ when a unique mark exists and outputs $`\mathtt{none}`$ with certainty when no mark exists. It never outputs an incorrect index on any activation trajectory. In the clock-driven model, one fixed schedule simultaneously attains
```math
q=O\!\left(\sqrt N+rN\right),
\qquad
T=O\!\left(\sqrt N+rN+\delta^{-1}\right).
```
In the call-driven model, replacing the idle intervals by charged dummy calls gives
```math
Q=O\!\left(\sqrt N+rN+\delta^{-1}\right).
```
All budgets are worst-case bounds. No expected stopping-time or independent-restart assumption is used. Together with the [universal lower bounds](lower-bounds.md), these bounds are optimal up to absolute constants.

The remainder gives explicit integer schedules and proves their guarantees.

## 2. A phase-only certificate with exact soundness

For a proposed index $`j`$, choose two distinct indices $`a_1,a_2`$, both different from $`j`$. This is possible because $`N\ge3`$. The references can be deterministic functions of $`j`$, such as the next two indices in cyclic order; neither is assumed unmarked.

For each $`a_i`$, prepare
```math
|+_{j,a_i}\rangle
=\frac{|j\rangle+|a_i\rangle}{\sqrt2},
```
make one phase-oracle call, and measure in the two-state basis
```math
|\pm_{j,a_i}\rangle
=\frac{|j\rangle\pm|a_i\rangle}{\sqrt2}.
```
Accept $`j`$ exactly when both tests return the minus outcome. Both calls are made even if the first test fails, preserving a deterministic schedule.

**Lemma 1.** This certificate has zero false positives for every activation trajectory. If $`j=w`$ and both calls are active, it accepts with certainty.

**Proof.** When $`j=w`$, both references are unmarked, and an active call changes the prepared plus state to the corresponding minus state up to an irrelevant global phase. When $`j\ne w`$, at most one reference can be marked. At least one of the two tests therefore uses two unmarked indices and returns plus under either activation bit. With no marked index, both tests return plus. This argument is trajectory by trajectory and does not use independence of the two faults. $`\square`$

The certificate consumes two ordinary phase queries. It uses neither a controlled query nor a separate verification oracle.

## 3. A uniform bound for short Grover runs

Let
```math
|s\rangle=\frac1{\sqrt N}\sum_{j=1}^N|j\rangle,
\qquad
R_s=2|s\rangle\langle s|-I,
\qquad
\theta=\arcsin(N^{-1/2}).
```
For an ideal oracle, $`m`$ Grover steps $`R_sO_w`$ give success probability
```math
p_m=\sin^2((2m+1)\theta).
```
This is the usual two-dimensional rotation formula for Grover search [1,2].

For any $`x`$ with $`\sqrt3\le x\le\sqrt N`$, define
```math
m(x)=\max\{1,\lfloor x/8\rfloor\}.
```
Then
```math
\frac{x}{16}\le m(x)\le x.
```
For $`x<16`$, the lower bound follows from $`m(x)\ge1`$; for $`x\ge16`$, it follows from $`\lfloor x/8\rfloor\ge x/8-1\ge x/16`$.

**Lemma 2.** For this choice of $`m=m(x)`$ and every $`N\ge3`$,
```math
p_m\ge\frac{m^2}{N}.
```

**Proof.** If $`m=1`$, the exact triple-angle identity gives
```math
p_1=\frac{(3-4/N)^2}{N}\ge\frac1N.
```
This treats all small-$`N`$ cases, including those where $`3\theta>\pi/2`$.

If $`m\ge2`$, then $`m\le\sqrt N/8`$ and $`N\ge256`$. Using
```math
N^{-1/2}\le\theta\le\frac{\pi}{2\sqrt N}
```
gives
```math
(2m+1)\theta
\le\frac{\pi}{8}+\frac{\pi}{2\sqrt N}
\le\frac{5\pi}{32}<\frac{\pi}{2}.
```
On this interval, $`\sin u\ge2u/\pi`$, so
```math
p_m
\ge\frac{4(2m+1)^2}{\pi^2N}
\ge\frac{16m^2}{\pi^2N}
\ge\frac{m^2}{N}.
```
$`\square`$

## 4. Persistent activation: $`0<\delta\le1/2`$

Set
```math
x=\min\{\sqrt N,\delta^{-1}\},
\qquad
m=m(x),
\qquad
g=\left\lceil\frac{\ln2}{2\delta}\right\rceil,
\qquad
M=\left\lceil16\ln(10)\frac{N}{m^2}\right\rceil.
```

Each trial uses the following fixed schedule:

1. Idle for $`g`$ slots.
2. Prepare a fresh $`|s\rangle`$ and perform $`m`$ ordinary steps $`R_sO_w^{b_t}`$ in consecutive slots.
3. Measure a candidate $`j`$ and perform the two-query certificate in the next two consecutive slots.

Run all $`M`$ trials, retaining the first accepted index. Return that index if one was accepted, and otherwise return $`\mathtt{none}`$. Continuing the prescribed schedule after acceptance makes both resource budgets deterministic.

### 4.1 Mixing is conditional on the entire preceding history

Let $`H`$ be the full classical history before a trial, including all previous candidates, certificate outcomes, and internal random choices. The current hidden bit can have an arbitrary posterior distribution conditioned on $`H`$. For a two-state symmetric Markov chain,
```math
\Pr(b_{t+L}=1\mid b_t)
=\frac12\left[1+(2b_t-1)(1-2\delta)^L\right].
```
Consequently, for any such posterior,
```math
\Pr(b_{t+L}=1\mid H)
\ge\frac{1-(1-2\delta)^L}{2}.
```
There are at least $`g`$ transitions between the previous trial's last useful call and the next trial's first useful call. Because
```math
(1-2\delta)^g\le e^{-2\delta g}\le\frac12,
```
the first useful activation probability is at least $`1/4`$, uniformly over histories. The first trial begins from the fair prior and also satisfies this bound. At $`\delta=1/2`$, one transition mixes exactly.

This argument does not claim exact independence from the previous history. The fresh work register removes retained computational state from the next search run, while the hidden process continues throughout.

### 4.2 A uniformly successful event

Let $`E`$ be the event that all $`m+2`$ useful slots of a trial are active. Conditional on any preceding history,
```math
\Pr(E\mid H)
\ge\frac14(1-\delta)^{m+1}
\ge\frac1{16}.
```
To verify the last inequality throughout the parameter range:

- If $`\delta\le1/8`$, then $`m\le1/(8\delta)`$, including the cutoff case $`m=1`$. Thus $`\delta(m+1)\le1/4`$, and Bernoulli's inequality gives $`(1-\delta)^{m+1}\ge3/4`$.
- If $`\delta>1/8`$, then $`m=1`$, and $`(1-\delta)^{m+1}=(1-\delta)^2\ge1/4`$.

On $`E`$, the search is ideal and a true candidate passes the certificate. Lemma 2 therefore gives
```math
\Pr(\text{trial accepts }w\mid H)
\ge\frac{m^2}{16N}.
```
Other activation trajectories may produce additional true acceptances but cannot produce false ones.

### 4.3 Fixed-budget amplification and both resource bounds

Repeated conditioning, rather than trial independence, yields
```math
\Pr(\text{no acceptance in }M\text{ trials})
\le\left(1-\frac{m^2}{16N}\right)^M
\le e^{-Mm^2/(16N)}
\le0.1.
```
The exact clock-driven budgets are
```math
q=M(m+2),
\qquad
T=M(g+m+2).
```
Since $`N/m^2\ge1`$, the ceiling in $`M`$ only changes an absolute constant. Also $`m+2\le3m`$, and hence
```math
q=O(N/m)
=O\!\left(\sqrt N+\delta N\right).
```
For the elapsed time, $`m\le\delta^{-1}`$ and $`\delta\le1/2`$ imply
```math
g+m+2
\le\frac{\ln2+5}{2\delta}
<\frac3\delta.
```
Together with $`m\ge x/16`$, this gives
```math
T=O\!\left(\frac{N}{\delta x^2}\right)
=O\!\left(\max\{\delta N,\delta^{-1}\}\right).
```
In particular, the same fixed schedule attains both claimed bounds. The inequality $`\max\{\delta N,\delta^{-1}\}\ge\sqrt N`$ identifies this elapsed bound with the stated full expression up to constants.

## 5. Alternating activation: $`1/2\le\delta\le1`$

Apply two consecutive physical oracle calls to the same register, with no control or measurement between them. Since $`O_w^2=I`$,
```math
O_w^{b_{2k}}O_w^{b_{2k-1}}
=O_w^{b_{2k-1}\oplus b_{2k}}
=O_w^{z_{2k-1}}.
```
The bits $`z_{2k-1}`$ are independent Bernoulli variables with parameter $`\delta`$. Disjoint pairs therefore provide an exact IID logical oracle with omission probability
```math
p=1-\delta\le\frac12.
```
This identity holds for every initial activation bit and every individual noise trajectory. Previous observations can bias the initial bit of a pair, but that bit cancels from the pair's product. The transition bit within the pair is fresh. Arbitrary known or adaptive controls between complete pairs do not change the conclusion.

Define
```math
x_-=\min\{\sqrt N,p^{-1}\},
\qquad
m_-=m(x_-),
\qquad
M_-=\left\lceil8\ln(10)\frac{N}{m_-^2}\right\rceil,
```
where $`p^{-1}=\infty`$ when $`p=0`$. Each trial uses $`m_-`$ logical Grover queries followed by the two logical certificate queries. A logical certificate query is one complete physical pair. Every trial therefore consumes $`2(m_-+2)`$ physical calls.

The event that all logical queries in the trial are active has probability
```math
(1-p)^{m_-+2}\ge\frac18.
```
For $`p\le1/8`$, the bound follows from $`p(m_-+2)\le3/8`$ and Bernoulli's inequality; $`p=0`$ is immediate. For $`p>1/8`$, one has $`m_-=1`$ and $`(1-p)^3\ge1/8`$.

Each trial thus accepts the mark with probability at least $`m_-^2/(8N)`$, while the certificate remains exactly sound. The stated $`M_-`$ gives failure at most $`0.1`$. With no idle slots,
```math
q=T=2(m_-+2)M_-
=O(N/m_-)
=O\!\left(\sqrt N+(1-\delta)N\right).
```
At $`\delta=1`$, activations alternate deterministically and every physical pair implements a perfect logical oracle. The unknown initial activation bit is irrelevant.

## 6. Call-driven accounting and the excluded endpoint

For $`0<\delta\le1/2`$ in the call-driven model, replace each of the $`g`$ idle slots before a trial by an actual dummy call on a fixed computational-basis state, such as $`|1\rangle`$. Keep that register unentangled with retained information. The oracle acts on it only by a global phase. The dummy calls therefore advance the hidden process without providing a measurement outcome or changing the subsequent search state.

Each dummy call is charged. The exact budget is
```math
Q=M(g+m+2).
```
The mixing and conditional-success proof is otherwise unchanged. For $`\delta\ge1/2`$, the paired construction already uses consecutive calls and needs no modification. Combining the schedules gives
```math
Q=O\!\left(\sqrt N+rN+\delta^{-1}\right).
```

The restriction $`\delta>0`$ is necessary for the stated success convention. At $`\delta=0`$, the fair initial bit is inactive forever with probability $`1/2`$. On that event the algorithm has the same transcript as on the no-mark instance. An algorithm that outputs $`\mathtt{none}`$ with probability at least $`0.9`$ on the no-mark instance therefore fails on a marked instance with probability at least $`0.45`$.

The restriction $`N\ge3`$ is also substantive for uncontrolled phase access. For $`N=2`$, the two unique-mark oracles differ by a global phase. For each activation trajectory, replacing one mark by the other changes only the algorithm's overall phase, so their output distributions cannot be distinguished.

## 7. Preparation, known gates, workspace, and output

Let $`n=\lceil\log_2N\rceil`$. Encode index $`j`$ by the $`n`$-bit string for $`j-1`$. The following counts use arbitrary known single-qubit rotations and CNOT as elementary gates, with clean ancillary qubits for reversible control [3]. They are exact-control counts in this gate convention, rather than exact-synthesis claims for a fixed finite gate alphabet.

### Uniform preparation for arbitrary $`N`$

When $`N=2^n`$, preparing $`|s\rangle`$ requires $`n`$ Hadamard gates. For general supplied $`N`$, an exact circuit uses $`O(n^2)`$ elementary gates and $`O(n)`$ reusable clean ancillary qubits.

One explicit construction prepares the bits from most to least significant. After the first $`k`$ bits have been prepared, every populated prefix smaller than
```math
u_k=\left\lfloor\frac{N-1}{2^{n-k}}\right\rfloor
```
has a fully allowed continuation. Only the boundary prefix $`u_k`$ can have a partially filled continuation, of size
```math
c_k=N-u_k2^{n-k}.
```
For a full prefix, the next bit has equal amplitudes. For the boundary prefix, use an angle $`\alpha_k`$ satisfying
```math
\cos\alpha_k
=\sqrt{\frac{\min\{c_k,2^{n-k-1}\}}{c_k}},
\qquad 0\le k<n.
```
Using the convention $`R_y(\beta)=e^{-i\beta Y/2}`$, apply a Hadamard to the next bit and, conditioned on the previous prefix being $`u_k`$, apply the correction $`R_y(2\alpha_k-\pi/2)`$. This gives the appropriate square roots of the counts in the two child intervals. Prefix equality can be computed and uncomputed with $`O(k)`$ elementary gates and clean ancillas. Summing over $`k`$ gives $`O(n^2)`$ gates. The resulting state is exactly uniform on the valid encodings $`0,\ldots,N-1`$.

If $`A_N`$ denotes this preparation unitary, the known reflection is
```math
R_s=A_N\left(2|0^n\rangle\langle0^n|-I\right)A_N^{\dagger}.
```
The central basis-state reflection has an $`O(n)`$ gate implementation with clean ancillas, so $`R_s`$ also costs $`O(n^2)`$ gates. All oracle calls remain inside the valid $`N`$-dimensional query subspace; unused bit strings do not supply extra known-unmarked oracle states.

### Certificate and output costs

For two known distinct indices $`j,a`$, their plus superposition can be prepared using $`O(n)`$ Clifford gates. Choose one set bit of the XOR of their encodings. A Hadamard on that bit, CNOTs to the other differing bits, and X gates for the encoding of $`j`$ prepare $`(|j\rangle+|a\rangle)/\sqrt2`$. Reversing the affine part and measuring the Hadamard basis implements the plus/minus test. The two-reference verifier therefore needs $`O(n)`$ known gates in addition to its two charged oracle calls.

Measured work registers may be reinitialized and reused. The quantum workspace is $`O(n)`$ qubits, including the clean controls described above. Only the first accepted index, an acceptance flag, and classical schedule counters need be retained. Explicit schedule counters require $`O(\log(T+1))`$ classical bits, so the total classical storage is $`O(n+\log(T+1))`$ bits. The counter contribution need not be polynomial in $`\log N`$ when $`\delta`$ is extremely small. The output contains one $`n`$-bit index or the symbol $`\mathtt{none}`$.

Across the clock-driven construction, the number of known quantum elementary gates is
```math
O\!\left((\sqrt N+rN)\log^2N\right).
```
For a power-of-two database, the same construction gives $`O((\sqrt N+rN)\log N)`$ known gates with clean ancillas. Charged dummy intervals in the call-driven construction can keep a fixed basis state throughout; their oracle calls do not require an additional Grover reflection.

These bounds exclude classical scheduling operations and device-specific execution times. No database state preparation, QRAM, or loading of the unknown marked location is assumed.

## References

1. Lov K. Grover, “A fast quantum mechanical algorithm for database search,” *Proceedings of STOC 1996*, pp. 212–219. Primary preprint: [arXiv:quant-ph/9605043](https://arxiv.org/abs/quant-ph/9605043).
2. Michel Boyer, Gilles Brassard, Peter Høyer, and Alain Tapp, “Tight bounds on quantum searching,” *Fortschritte der Physik* **46**, 493–506 (1998). Primary preprint: [arXiv:quant-ph/9605034](https://arxiv.org/abs/quant-ph/9605034), Section 2, Eq. (2).
3. Adriano Barenco et al., “Elementary gates for quantum computation,” *Physical Review A* **52**, 3457–3467 (1995). Primary preprint: [arXiv:quant-ph/9503016](https://arxiv.org/abs/quant-ph/9503016), especially Corollaries 7.4 and 7.12. [DOI](https://doi.org/10.1103/PhysRevA.52.3457).
