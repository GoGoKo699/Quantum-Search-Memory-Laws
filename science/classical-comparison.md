# Classical comparison in the coherent bit-oracle model

A comparison between classical and quantum query counts requires a common membership interface. An uncontrolled phase query on a classical basis state changes only a global phase. We therefore use the coherent bit oracle
```math
U_w|j,z\rangle
=|j,z\oplus\mathbf1[j=w]\rangle,
\qquad
U_{\varnothing}=I,
```
with physical call $`U_w^{b_t}`$ and the same stationary Markov activation process:
```math
b_1\sim\mathrm{Bernoulli}(1/2),
\qquad
b_{t+1}=b_t\oplus z_t,
\qquad
z_t\stackrel{\mathrm{iid}}{\sim}\mathrm{Bernoulli}(\delta).
```
Assume $`N\ge3`$, supplied $`0<\delta\le1`$, and at most one marked item. Put $`r=\min\{\delta,1-\delta\}`$.

A classical algorithm supplies basis-state indices and response bits, and reads classical responses. A quantum algorithm may query the same unitary coherently. There are no fault labels or resets of the hidden process.

## 1. Resource theorem

In the clock-driven model, a slot may contain one query or an idle, and the hidden bit advances in either case. Let $`q_C`$ be the worst-case number of actual classical oracle calls and $`T_C`$ the worst-case elapsed slots.

**Theorem.** There is a classical randomized algorithm with success at least $`0.9`$ on every promised input and simultaneous resource bounds
```math
q_C=O(N),
\qquad
T_C=O(N+\delta^{-1}).
```
It always answers correctly on the no-mark input and never reports an unmarked index. Every bounded-horizon classical algorithm with success at least $`0.9`$ satisfies
```math
q_C=\Omega(N),
\qquad
T_C=\Omega(N+\delta^{-1}).
```
Thus the two bounds are simultaneously optimal. In the call-driven model, replacing idle intervals by charged dummy calls gives the tight single-resource law
```math
Q_C=\Theta(N+\delta^{-1}).
```

The quantum constructions transfer to this interface by keeping the response qubit in $`|-\rangle`$, since
```math
U_w(|\psi\rangle\otimes|-\rangle)
=(O_w|\psi\rangle)\otimes|-\rangle.
```
The universal lower proof also applies to arbitrary coherent bit-query strategies. Indeed,
```math
U_w=I-2P_w,
\qquad
P_w=|w\rangle\langle w|\otimes|-\rangle\langle-|,
\qquad
\sum_{w=1}^{N}P_w
=I\otimes|-\rangle\langle-|\preceq I.
```
This is the projector-sum condition used by the [lower-bound potential](lower-bounds.md). Therefore the optimal quantum bounds in this same interface are
```math
q_Q=\Theta(\sqrt N+rN),
\qquad
T_Q=\Theta(\sqrt N+rN+\delta^{-1}).
```
The [quantum construction](upper-bounds.md) attains both bounds with one fixed schedule.

## 2. Sampling an index with a fixed number of random bits

For arbitrary $`N`$, let $`n=\lceil\log_2N\rceil`$. Draw an $`n`$-bit uniform integer $`V\in\{0,\ldots,2^n-1\}`$ and set
```math
J=1+(V\bmod N).
```
This uses exactly $`n`$ unbiased random bits. Since $`N\le2^n<2N`$, every index has probability
```math
\pi_j=\Pr(J=j)\ge2^{-n}\ge\frac1{2N}.
```
The modular reduction needs only a comparison and, if necessary, one subtraction. It therefore costs $`O(n)`$ classical bit operations. For $`N=2^n`$, the distribution is exactly uniform.

All candidate draws below are independent copies of this bounded sampler. Exact uniformity on a non-power-of-two set and an unbounded rejection loop are unnecessary.

## 3. Persistent activation: $`0<\delta\le1/2`$

Define
```math
g=\left\lceil\frac{\ln2}{2\delta}\right\rceil,
\qquad
y=\min\{N,\delta^{-1}\},
\qquad
L=\max\{1,\lfloor y/8\rfloor\},
\qquad
M_C=\left\lceil32\ln(10)\frac{N}{L}\right\rceil.
```

Each trial idles for $`g`$ slots and then makes $`L`$ consecutive classical queries. For each useful call, draw a fresh candidate $`J`$, initialize the response bit to zero, apply $`U_w^{b_t}`$, and read the response. Retain the first response 1 and its candidate index. Continue the fixed schedule for all $`M_C`$ trials, then output the retained index or $`\mathtt{none}`$.

A response 1 can occur only when the queried item is marked and the call is active. Soundness is therefore exact on every noise trajectory.

### Conditional success of a trial

Let $`H`$ be the complete previous history. The Markov mixing calculation gives a first useful activation probability of at least $`1/4`$, regardless of the posterior hidden bit conditioned on $`H`$. The probability that all $`L`$ useful slots are active obeys
```math
\Pr(E\mid H)
\ge\frac14(1-\delta)^{L-1}
\ge\frac18.
```
For $`\delta\le1/8`$, the choice of $`L`$ gives $`\delta L\le1/8`$, so Bernoulli's inequality bounds the stay probability below by $`7/8`$. For $`\delta>1/8`$, one has $`L=1`$ and no stay transition is needed.

Conditional on $`E`$, the probability of sampling a fixed marked item is
```math
1-(1-\pi_w)^L
\ge1-e^{-L/(2N)}
\ge\frac{L}{4N}.
```
The last inequality uses $`L\le N`$ and $`1-e^{-u}\ge u/2`$ for $`0\le u\le1`$. Thus every trial satisfies the uniform conditional lower bound
```math
\Pr(\text{trial finds }w\mid H)
\ge\frac{L}{32N}.
```
Repeated conditioning yields
```math
\Pr(\text{all }M_C\text{ trials fail})
\le\left(1-\frac{L}{32N}\right)^{M_C}
\le0.1.
```
No independence between the activation paths of different trials is assumed.

### Simultaneous budgets

The exact budgets are
```math
q_C=M_C L,
\qquad
T_C=M_C(g+L).
```
Since $`2\le y\le N`$ and $`y/16\le L\le y`$,
```math
q_C\le(32\ln10+1)N=O(N),
```
and
```math
T_C
=O\!\left(N+\frac{N}{\delta L}\right)
=O\!\left(N+\delta^{-1}\right).
```
These are bounds for a single algorithm, with deterministic query and slot budgets.

## 4. Alternating activation: $`1/2\le\delta\le1`$

Choose a candidate $`J`$, initialize one response bit to zero, and make two consecutive physical calls on the same index and response, without resetting or reading the response between calls. Their composition is
```math
U_w^{b_{2k}}U_w^{b_{2k-1}}
=U_w^{z_{2k-1}}.
```
The final response is 1 exactly when $`J=w`$ and the fresh within-pair transition bit is 1. Each pair therefore finds the mark with probability
```math
\delta\pi_w\ge\frac1{4N}.
```
The transition bits and the newly drawn candidate indices are independent across pairs. After
```math
K_C=\lceil4N\ln10\rceil
```
pairs, the failure probability is at most
```math
(1-\delta\pi_w)^{K_C}
\le e^{-K_C/(4N)}
\le0.1.
```
All calls are consecutive, so the deterministic budgets are
```math
q_C=T_C=2K_C=O(N).
```
The response cannot falsely identify an unmarked item. At $`\delta=1`$, each pair contains exactly one active call and supplies a perfect classical membership response, regardless of the initial activation bit.

## 5. Lower bounds and call-driven accounting

### Actual calls require linear classical search

An ideal membership oracle can simulate a noisy algorithm by privately drawing the external Markov path, performing idle slots at no query cost, and invoking the ideal oracle only for active calls. The simulation uses at most the noisy algorithm's worst-case number $`q_C`$ of actual calls.

For completeness, the ideal classical lower bound follows by coupling the no-mark input to a uniformly random unique mark. Fix the algorithm's internal randomness and follow its no-mark transcript. At most $`q_C`$ distinct indices are queried. Until a marked index is among those queried, the marked and no-mark transcripts coincide. Their output distributions therefore have total variation distance at most $`q_C/N`$, after averaging over the uniformly random mark and the algorithm's randomness.

Correctness at least $`0.9`$ requires the event “output $`\mathtt{none}`$” to have probability at least $`0.9`$ on the no-mark input and at most $`0.1`$ on the random marked input. Hence
```math
q_C\ge0.8N.
```
The argument permits adaptive queries, classical randomness, and a bounded adaptive query/idle schedule.

### Availability imposes elapsed time

Over $`T_C\ge1`$ elapsed slots, the all-inactive event has probability
```math
\Pr(b_1=\cdots=b_{T_C}=0)
=\frac12(1-\delta)^{T_C-1}.
```
On this event, a marked input produces the same transcript as the no-mark input. The no-mark transcript does not reveal the hidden process, so its internal output distribution is independent of this all-off event. If no-mark correctness is at least $`0.9`$, marked-input failure is at least
```math
\frac{0.9}{2}(1-\delta)^{T_C-1}.
```
Thus, for $`0<\delta<1`$,
```math
T_C-1
\ge\frac{\ln(9/2)}{-\ln(1-\delta)}.
```
For $`\delta\le1/2`$, this implies
```math
T_C-1\ge\frac{\ln(9/2)}{2\delta}.
```
For $`\delta\ge1/2`$, the term $`\delta^{-1}`$ is bounded and is absorbed by the linear search bound. Combining these facts with $`T_C\ge q_C`$ gives $`T_C=\Omega(N+\delta^{-1})`$.

At $`\delta=0`$, the fair initial inactive state persists forever with probability $`1/2`$, so the required success is impossible for the same reason. This endpoint is excluded from the theorem.

### Call-driven resource

In the call-driven model, replace each idle slot in the persistent-regime construction by a dummy classical bit-oracle call at a fixed index, ignoring and discarding its response. These calls advance the chain without being used to select the next trial. Their responses need not be known in advance.

Every dummy call is charged, giving
```math
Q_C=M_C(g+L)=O(N+\delta^{-1})
```
in the persistent regime. The alternating-regime construction needs no change. The ideal-query and all-off arguments now both charge consumed oracle calls, proving $`Q_C=\Theta(N+\delta^{-1})`$.

## 6. Query advantage and elapsed-time advantage

The common bit interface gives the following optimal resource comparison. Both clock-driven bounds in each column are attained simultaneously.

| Resource | Quantum | Classical |
| --- | --- | --- |
| Clock-driven actual calls | $`\Theta(\sqrt N+rN)`$ | $`\Theta(N)`$ |
| Clock-driven elapsed slots | $`\Theta(\sqrt N+rN+\delta^{-1})`$ | $`\Theta(N+\delta^{-1})`$ |
| Call-driven charged calls | $`\Theta(\sqrt N+rN+\delta^{-1})`$ | $`\Theta(N+\delta^{-1})`$ |

The corresponding speedup factors are
```math
S_q
=\Theta\!\left(\frac{N}{\sqrt N+rN}\right),
\qquad
S_T
=\Theta\!\left(
\frac{N+\delta^{-1}}
{\sqrt N+rN+\delta^{-1}}
\right).
```

For $`\delta\ll1/N`$, quantum search uses $`\Theta(\sqrt N)`$ actual calls while classical search uses $`\Theta(N)`$, but both elapsed times are $`\Theta(1/\delta)`$. For $`\delta=\Theta(N^{-1/2})`$, the elapsed times are $`\Theta(\sqrt N)`$ quantumly and $`\Theta(N)`$ classically. Near the other endpoint, $`1-\delta=O(N^{-1/2})`$ gives a quadratic advantage in both resources through exact pair composition. For any fixed $`\delta`$ strictly between zero and one, both complexities are linear in $`N`$.

## 7. Classical control and output costs

Each useful candidate draw consumes exactly $`n`$ random bits and $`O(n)`$ classical bit operations. A single response bit, a candidate register, the first accepted index, and schedule counters suffice. Explicit counters for the horizon and block schedule require $`O(\log(T_C+1))`$ bits, giving total classical storage $`O(n+\log(T_C+1))`$. This need not be polynomial in $`\log N`$ for arbitrarily small supplied $`\delta`$.

Across the clock-driven construction, candidate generation and membership-response processing use $`O(N\log N)`$ random bits and classical bit operations, excluding the scheduling of idle slots. No corresponding bound on all clock-tick bookkeeping is asserted when the horizon is much larger than $`N`$. The output is one $`n`$-bit index or $`\mathtt{none}`$.

The response bit can be reinitialized between trials or candidate pairs. This operation does not reset the external activation process. As with the quantum construction, elapsed slots count the specified oracle-interaction clock, separately from the implementation time of classical controls.

## Mathematical references

The constructions and coupling arguments above are proved explicitly. For the original unstructured-search algorithm and classical membership comparison, see Lov K. Grover, “A fast quantum mechanical algorithm for database search,” *Proceedings of STOC 1996*, pp. 212–219; primary preprint: [arXiv:quant-ph/9605043](https://arxiv.org/abs/quant-ph/9605043). The full quantum optimality statement uses the accompanying [upper-bound construction](upper-bounds.md) and [universal lower-bound proof](lower-bounds.md).
