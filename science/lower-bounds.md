# Universal lower bounds for search with Markov omissions

For search among $`N`$ items with at most one mark, stationary Markov omissions impose the necessary resource bounds

```math
q=\Omega\!\left(\sqrt N+rN\right),
\qquad
T=\Omega\!\left(\sqrt N+rN+\frac1\delta\right),
\qquad
r=\min\{\delta,1-\delta\}.
```

Here $`q`$ counts actual oracle calls and $`T`$ counts oracle slots, including idle slots during which the noise evolves. The constants are uniform in $`N\geq3`$ and known $`0<\delta\leq1`$, with success probability at least $`0.9`$ on every promised input. If the noise advances only when an oracle call is consumed, take $`q=T`$.

The proofs below cover arbitrary quantum states, ancillas, intermediate measurements, classical randomness, and adaptive classical choices of when to query, idle, or stop. They require finite worst-case resource budgets. The matching algorithms use ordinary phase queries; see [Upper bounds](upper-bounds.md). The extension to weighted families of inputs is proved in [Weighted extension](weighted-extension.md).

## 1. Oracle, noise, and resources

The query register has basis $`\{|i\rangle:i\in[N]\}`$. For a marked item $`w\in[N]`$, the phase oracle is

```math
O_w=I-2|w\rangle\langle w|.
```

Write $`O_{\varnothing}=I`$ for the no-mark input. The label $`\varnothing`$ denotes an input instance, not an additional query index or a known unmarked reference state.

In oracle slot $`t`$, a call applies $`O_w^{b_t}`$. The hidden bit obeys

```math
b_1\sim\mathrm{Bernoulli}(1/2),\qquad
b_{t+1}=b_t\oplus z_t,\qquad
z_t\stackrel{\mathrm{iid}}{\sim}\mathrm{Bernoulli}(\delta).
```

The chain is external to the algorithm. It advances once per slot, independently of the input and the algorithm's operations. Its marginal is fair at every fixed slot. The algorithm receives no fault flags, has no access to the noise environment, and cannot reset the chain. Its other operations are ideal.

An algorithm has a deterministic horizon $`T`$: it stops by slot $`T`$ on every input and every history. Let $`K`$ be its random number of actual calls, and let $`q`$ be a worst-case bound, so $`K\leq q\leq T`$. A slot containing a call counts toward both resources; an idle counts only toward $`T`$. The algorithm must output $`w`$ when $`w\in[N]`$ is marked, and `none` on the no-mark input, with probability at least $`0.9`$.

The call-driven convention is obtained by counting only consumed oracle calls as slots. In that convention waiting does not advance the chain, a dummy call is charged, and the two worst-case budgets coincide.

## 2. Access models used in the proof

The algorithms in the upper bound need only the uncontrolled phase oracle above. For the lower bound, we may strengthen access by allowing a coherent enable flag $`E`$:

```math
C_w=I-2P_w,\qquad
P_w=|w\rangle\langle w|_I
\otimes|1\rangle\langle1|_E\otimes I_{\mathrm{work}}.
```

The hidden bit acts on the entire enabled query: the operation is $`C_w^{b_t}`$. In particular, an enabled query can be omitted, and a disabled query is the identity for either hidden bit. The projectors satisfy

```math
\sum_{w=1}^N P_w
=I_I\otimes|1\rangle\langle1|_E\otimes I_{\mathrm{work}}
=:J.
```

A lower bound in this stronger model also bounds uncontrolled phase access. We use the enable register to represent classical adaptive schedules after purification. We do not interpret a coherent flag amplitude as a fractional physical call in the original model.

The standard bit-response oracle

```math
B_w|i,a\rangle=|i,a\oplus[i=w]\rangle
```

is a reflection as well:

```math
B_w=I-2\bigl(|w\rangle\langle w|_I
\otimes|-\rangle\langle-|_R\bigr),
\qquad |-\rangle=(|0\rangle-|1\rangle)/\sqrt2.
```

The proof therefore also covers arbitrary coherent response inputs. With a separate enable flag its projector is the displayed projector tensored with $`|1\rangle\langle1|_E`$, and the sum over marks is at most $`J`$. Conjugating the response qubit by Hadamard gates identifies bit-response access with controlled phase access, for each individual noise trajectory. A bit query with response fixed to $`|-\rangle`$ implements an uncontrolled phase query. The reverse conversion is not assumed.

Consequently the same lower bounds apply in the common bit-response model used for a classical comparison, while the upper bound already holds in the phase-only model.

## 3. Statement with constants

Define, for $`0<\delta<1`$,

```math
A_\delta
=\frac{1-2\delta+2\delta^2}{\delta(1-\delta)}.
```

### Theorem 1

Every algorithm satisfying the preceding contract obeys

```math
q\geq\frac25\sqrt N
```

and

```math
\mathbb E_{\varnothing} K
\geq\frac{4N}{25A_\delta}
\geq\frac4{25}\,rN
\qquad(0<\delta<1).
```

The expectation is on the no-mark input. At $`\delta=1`$, the last lower bound is interpreted as the trivial inequality $`\mathbb E_{\varnothing}K\geq0`$.

For $`0<\delta<1`$, the horizon also satisfies

```math
T-1\geq
\frac{\log(9/2)}{-\log(1-\delta)}.
```

In particular, for $`0<\delta\leq1/2`$,

```math
T-1\geq\frac{\log(9/2)}{2\delta}.
```

These inequalities imply the resource bounds stated at the beginning, since $`\mathbb E_{\varnothing}K\leq q\leq T`$. Their proofs are given in Sections 4–8.

The Markov-dependent proof uses a positive-semidefinite pure-component decomposition, following the method lineage of Regev and Schiff for independent faulty queries [RS]. The additional state variable below retains the distinction between the two hidden memory states.

## 4. A fixed-horizon normal form

Purify the algorithm's initial state, private randomness, and CPTP operations. For a measurement, keep its outcome and an untouched copy of the outcome in ancillary registers; later operations are controlled on the retained outcome. The untouched copy preserves the original classical branching statistics. Registers purifying discarded systems can be kept without being used again.

Classical choices to query or idle are represented by the enable register. Thus a fixed sequence of input-independent isometries, extended to unitaries on a sufficiently large workspace, reproduces the original adaptive process. The input dependence is entirely in the oracle. A stopped branch retains its answer, disables subsequent queries, and is padded to horizon $`T`$. In the clock-driven model these are idle slots. In the call-driven analysis, the noise trajectory can be extended after a branch has stopped because that extension cannot change its retained output.

Let $`|\psi_t\rangle`$ be the normalized purified algorithm state on the no-mark input after $`t`$ slots and the associated common control. It is independent of the hidden bit, because $`O_{\varnothing}=I`$. Define

```math
p_t=\langle\psi_t|J|\psi_t\rangle,
\qquad 0\leq t<T,
```

at the point immediately before the next query operation. For the purified classical schedule, $`p_t`$ is its no-mark probability of making an actual call in that slot. Hence

```math
\sum_{t=0}^{T-1}p_t=\mathbb E_{\varnothing}K.
```

This identity does not condition on a measurement history. The proof retains the entire history in the state. In particular, it does not incorrectly replace the posterior distribution of the hidden bit after an observation by a fresh fair bit.

For a marked input, let $`\rho_t^{w,0}`$ and $`\rho_t^{w,1}`$ be the normalized algorithm states conditioned only on the current hidden bit. The unconditioned hidden marginal remains fair because the external chain evolves independently of all algorithm controls. Thus

```math
\rho_t^w=\frac12\rho_t^{w,0}+\frac12\rho_t^{w,1}.
```

Correlations between the hidden bit and the algorithm's retained records are fully contained in these conditional states.

## 5. Positive components and the memory recurrence

### Lemma 2: conditional positive components

There exist subnormalized vectors $`\phi_t^{w,0},\phi_t^{w,1}`$ satisfying

```math
\rho_t^{w,b}\succeq
|\phi_t^{w,b}\rangle\langle\phi_t^{w,b}|,
\qquad b\in\{0,1\},
```

with initial vectors $`\phi_0^{w,0}=\phi_0^{w,1}=\psi_0`$. Before the common control following a slot, they can be updated by

```math
\begin{aligned}
\widetilde\phi_{t+1}^{w,0}
&=(1-\delta)\phi_t^{w,0}
+\delta C_w\phi_t^{w,1},\\
\widetilde\phi_{t+1}^{w,1}
&=\delta\phi_t^{w,0}
+(1-\delta)C_w\phi_t^{w,1}.
\end{aligned}
```

**Proof.** The inactive hidden branch applies the identity and the active branch applies $`C_w`$. The subsequent symmetric transition mixes the two conditional states with weights $`1-\delta,\delta`$. For any vectors $`a,b`$ and $`p\in[0,1]`$,

```math
\begin{aligned}
p|a\rangle\langle a|+(1-p)|b\rangle\langle b|
={}&|pa+(1-p)b\rangle\langle pa+(1-p)b|\\
&+p(1-p)|a-b\rangle\langle a-b|.
\end{aligned}
```

The last summand is positive semidefinite. Mixing the already positive residuals preserves positivity, so the claimed new vectors are valid. Applying the common isometry preserves the invariant. Induction proves the lemma. $`\square`$

For endpoint bookkeeping we also apply the hidden transition after the final query. A stochastic map on an unobserved register does not change the algorithm's reduced state. This operation only changes its conditional decomposition; it does not add an oracle call or an elapsed slot to the algorithm being analyzed.

Define

```math
s_t^w=\frac{\phi_t^{w,0}+\phi_t^{w,1}}2,\qquad
d_t^w=\frac{\phi_t^{w,0}-\phi_t^{w,1}}2,\qquad
\kappa=1-2\delta.
```

Lemma 2 implies

```math
\rho_t^w\succeq
|s_t^w\rangle\langle s_t^w|
+|d_t^w\rangle\langle d_t^w|.
\qquad\text{(1)}
```

Substituting $`C_w=I-2P_w`$ into its update gives

```math
\widetilde s_{t+1}^w=(I-P_w)s_t^w+P_wd_t^w,
\qquad
\widetilde d_{t+1}^w
=\kappa\bigl((I-P_w)d_t^w+P_ws_t^w\bigr).
\qquad\text{(2)}
```

The common control is then applied to $`\psi_t,\widetilde s_{t+1}^w,\widetilde d_{t+1}^w`$. Equation (2) remains valid for negative $`\kappa`$, including the alternating regime $`\delta>1/2`$.

## 6. Growth and terminal separation

For $`0<\delta<1`$, put

```math
\beta=\frac2{1+\kappa^2},\qquad
c=\frac{1-\kappa^2}{1+\kappa^2}>0,
\qquad
F_t^w=\|\psi_t-s_t^w\|^2+\beta\|d_t^w\|^2.
```

Initially $`F_0^w=0`$. A common isometry preserves the potential, so we may analyze (2) before that isometry.

### Lemma 3: one-slot growth

For every marked input,

```math
F_{t+1}^w-F_t^w
\leq A_\delta\|P_w\psi_t\|^2.
\qquad\text{(3)}
```

**Proof.** Abbreviate $`x=P_w\psi_t`$, $`u=P_ws_t^w`$, and $`v=P_wd_t^w`$. The marked-subspace contribution to the increment is

```math
\|x-v\|^2-\|x-u\|^2
+\beta\bigl(\kappa^2\|u\|^2-\|v\|^2\bigr).
```

The identities $`\beta\kappa^2-1=1-\beta=-c`$ therefore give the exact full increment

```math
\begin{aligned}
F_{t+1}^w-F_t^w
={}&2\mathrm{Re}\langle x,u-v\rangle
-c(\|u\|^2+\|v\|^2)\\
&-\beta(1-\kappa^2)\|(I-P_w)d_t^w\|^2.
\end{aligned}
\qquad\text{(4)}
```

Completing the square separately in $`u`$ and $`v`$ bounds the first line by $`2\|x\|^2/c`$. The second line is nonpositive. Finally,

```math
\frac2c
=\frac{2(1+\kappa^2)}{1-\kappa^2}
=A_\delta.
```

This proves (3). $`\square`$

Summing over marked items and using $`\sum_wP_w\preceq J`$ yields

```math
\sum_{w=1}^N(F_{t+1}^w-F_t^w)
\leq A_\delta p_t.
```

Consequently

```math
\sum_{w=1}^NF_T^w
\leq A_\delta\mathbb E_{\varnothing}K.
\qquad\text{(5)}
```

An idle does not create progress: with its enable flag identically zero, (2) reduces to $`s'=s,d'=\kappa d`$, and its increment is

```math
-\beta(1-\kappa^2)\|d\|^2\leq0.
```

### Lemma 4: terminal separation

Success $`0.9`$ implies $`F_T^w\geq4/25`$ for every $`w\in[N]`$.

**Proof.** Use the trace-distance convention

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

The output event “no mark” has probability at least $`0.9`$ on input $`\varnothing`$ and at most $`0.1`$ on input $`w`$. Data processing therefore gives

```math
D\bigl(\rho_T^w,|\psi_T\rangle\langle\psi_T|\bigr)\geq\frac45.
```

The pure-reference case of the fidelity–trace-distance inequality [FG] says

```math
D\bigl(\rho,|\psi\rangle\langle\psi|\bigr)
\leq\sqrt{1-\langle\psi|\rho|\psi\rangle}.
```

It follows that $`\langle\psi_T|\rho_T^w|\psi_T\rangle\leq9/25`$. By (1),

```math
|\langle\psi_T|s_T^w\rangle|\leq\frac35.
```

Taking the component of $`\psi_T-s_T^w`$ along the unit vector $`\psi_T`$ now gives

```math
\|\psi_T-s_T^w\|
\geq|1-\langle\psi_T|s_T^w\rangle|
\geq\frac25.
```

The other term of $`F_T^w`$ is nonnegative, proving the claim. $`\square`$

Combining Lemma 4 with (5) proves

```math
\mathbb E_{\varnothing}K\geq\frac{4N}{25A_\delta}.
```

For $`r=\min\{\delta,1-\delta\}\leq1/2`$,

```math
A_\delta
=\frac{1-2r+2r^2}{r(1-r)}
\leq\frac1r,
```

because $`1-2r+2r^2\leq1-r`$. This completes the proof of the Markov-dependent bound in Theorem 1.

## 7. The coherent search lower bound counts actual calls

The noisy process can be simulated using an ideal oracle. Privately sample its entire length-$`T`$ Markov trajectory, without exposing that trajectory to the simulated algorithm. Reproduce each idle slot freely. At a simulated call, use the ideal oracle if its sampled hidden bit is one and apply the identity otherwise. All controls, measurements, and stopping decisions are reproduced. This simulation is exact for every input and uses at most $`q`$ ideal calls.

It remains to give the ideal search lower bound, including adaptive algorithms. Grant the simulator controlled ideal access and purify its private randomness and measurements. Compress the free operations between successive ideal calls, and pad after stopping with disabled controlled calls. This gives $`q`$ oracle layers with common input-independent controls. Let $`\Psi_j^{\varnothing},\Psi_j^w`$ be the corresponding pure states.

At oracle layer $`j`$, the triangle inequality gives

```math
\|\Psi_{j+1}^w-\Psi_{j+1}^{\varnothing}\|
\leq\|\Psi_j^w-\Psi_j^{\varnothing}\|
+2\|P_w\Psi_j^{\varnothing}\|.
```

Iterating, then using Cauchy–Schwarz and $`\sum_wP_w\preceq I`$, yields

```math
\begin{aligned}
\sum_{w=1}^N\|\Psi_q^w-\Psi_q^{\varnothing}\|^2
&\leq4q\sum_{j=0}^{q-1}\sum_{w=1}^N\|P_w\Psi_j^{\varnothing}\|^2\\
&\leq4q^2.
\end{aligned}
```

Success $`0.9`$ implies output trace-distance separation at least $`4/5`$ for every marked item. The pure-state vector distance is at least that separation. Therefore

```math
\frac{16}{25}N\leq4q^2,
\qquad
q\geq\frac25\sqrt N.
```

This is the usual search hybrid argument [BBBV], applied after an exact simulation so that its resource is actual oracle calls rather than elapsed slots. No free ideal verifier is used.

## 8. Availability and the endpoints

For a fixed horizon $`T\geq1`$, the event

```math
\mathcal E_T=\{b_1=b_2=\cdots=b_T=0\}
```

has probability

```math
\Pr(\mathcal E_T)=\frac12(1-\delta)^{T-1}.
```

Conditional on this event, every attempted query is the identity, irrespective of the adaptive schedule. The marked-input process has exactly the no-mark output distribution. The latter is independent of the external noise trajectory. Thus the marked-input error is at least

```math
\frac9{20}(1-\delta)^{T-1}.
```

To make this at most $`1/10`$, it is necessary that

```math
(1-\delta)^{T-1}\leq\frac29.
```

For $`0<\delta<1`$, taking logarithms proves the exact horizon bound in Theorem 1. For $`0<\delta\leq1/2`$, use $`-\log(1-\delta)\leq2\delta`$ to obtain the $`1/\delta`$ bound. For $`\delta\geq1/2`$, the quantity $`1/\delta`$ is bounded by two and is absorbed by the nonzero query lower bound.

At $`\delta=1`$, the potential coefficient $`A_\delta`$ is singular and its reciprocal tends to zero. The memory-dependent term $`rN`$ vanishes, while the coherent lower bound remains. Indeed, two consecutive calls satisfy

```math
O_w^{b_{t+1}}O_w^{b_t}
=O_w^{b_t\oplus b_{t+1}}=O_w,
```

so a perfect logical query can be implemented with two physical calls.

Although $`\delta=0`$ is excluded from the theorem, its endpoint behavior explains the availability singularity. With probability one half the oracle is inactive forever. If the no-mark success probability is $`a`$, the marked success probability is at most $`1-a/2`$. Hence the worst-case success of the decision subproblem is at most

```math
\max_{0\leq a\leq1}\min\{a,1-a/2\}=\frac23.
```

In particular, success $`0.9`$ is impossible at this endpoint.

## 9. Scope of the result

The finite-horizon assumption is used to purify and pad the algorithm, to define a common external noise trajectory, and to apply the all-off event. The inequality for $`\mathbb E_{\varnothing}K`$ holds within that bounded horizon; it is not an unrestricted expected-stopping-time theorem.

The fair stationary distribution and the symmetric two-state transition matrix are part of the statement. The argument does not claim the same constants or law for a biased chain, a resettable noise source, observable fault flags, or an algorithm-controlled environment. The phase-only and bit-response comparisons preserve the same hidden trajectory.

## References

- **[RS]** Oded Regev and Liron Schiff, *Impossibility of a Quantum Speed-up with a Faulty Oracle*, ICALP 2008. [Primary preprint, arXiv:1202.1027](https://arxiv.org/abs/1202.1027). Its pure-component and progress-measure argument treats independently omitted queries.
- **[BBBV]** Charles H. Bennett, Ethan Bernstein, Gilles Brassard, and Umesh Vazirani, *Strengths and Weaknesses of Quantum Computing*, SIAM Journal on Computing **26**(5), 1510–1523 (1997). [Primary preprint, arXiv:quant-ph/9701001](https://arxiv.org/abs/quant-ph/9701001).
- **[FG]** Christopher A. Fuchs and Jeroen van de Graaf, *Cryptographic Distinguishability Measures for Quantum Mechanical States*. [Primary preprint, arXiv:quant-ph/9712042](https://arxiv.org/abs/quant-ph/9712042).
