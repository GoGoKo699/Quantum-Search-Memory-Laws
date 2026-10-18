# Search with a hidden oracle clock

An oracle can fail half the time and still support a quantum search advantage. The relevant resource depends on how its failures are arranged in time and on whether an algorithm must spend queries to let that time pass. This project determines the optimal search costs for a hidden, stationary two-state Markov process and separates actual oracle calls from elapsed oracle slots.

The account has three parts. The [lower bounds](lower-bounds.md) identify independent obstructions from search, memory loss and inactivity. The [constructions](upper-bounds.md) attain all three scales, with a [classical comparison](classical-comparison.md) using the same oracle interface. The [interpretation](interpretation.md) explains their joint consequences. A [weighted extension](weighted-extension.md) and a [paired-process comparison](paired-comparison.md) give supporting results.

## 1. Search task and access

Fix an integer $`N\ge3`$. The promise is either no marked item or exactly one marked item $`w\in[N]=\{1,\ldots,N\}`$. An algorithm must output the marked index, or the symbol `none` when there is no mark. Success is at least $`9/10`$ on every promised instance, averaged over the hidden environment and the algorithm's own randomness and measurements. Resource budgets are fixed worst-case bounds, including unsuccessful executions.

The ideal phase oracle is

```math
O_w=I-2\lvert w\rangle\langle w\rvert,
\qquad O_{\varnothing}=I.
```

Here $`\varnothing`$ denotes the no-mark **instance**. It does not add a known unmarked index to the query register. The constructive quantum results need only ordinary, uncontrolled phase calls.

For the comparison with classical computation, both algorithms receive the same standard bit oracle,

```math
U_w\lvert j,z\rangle
=\lvert j,z\oplus\mathbf 1_{\{j=w\}}\rangle,
\qquad U_{\varnothing}=I.
```

The response qubit $`\lvert-\rangle=(\lvert0\rangle-\lvert1\rangle)/\sqrt2`$ converts a bit call to a phase call. Conversely, the lower-bound proof treats the bit oracle directly as a reflection,

```math
U_w=I-2P_w,
\qquad
P_w=\lvert w\rangle\langle w\rvert
\otimes\lvert-\rangle\langle-\rvert.
```

The classical algorithm uses ordinary basis inputs and a measured bit response. A comparison between classical basis queries and an uncontrolled phase oracle would not give the same information interface; that comparison is not used here.

## 2. Stationary hidden process

At slot $`t`$, an activation bit $`b_t`$ determines whether the oracle acts. An actual call applies $`O_w^{b_t}`$, or $`U_w^{b_t}`$ for the bit interface. The hidden process is

```math
b_1\sim\operatorname{Bernoulli}(1/2),
\qquad
b_{t+1}=b_t\oplus z_t,
\qquad
z_t\overset{\mathrm{iid}}{\sim}\operatorname{Bernoulli}(\delta),
\qquad 0<\delta\le1.
```

The parameter $`\delta`$ is supplied to the algorithm. The cost of estimating an unknown noise rate is not included in this model. Define

```math
r=\min\{\delta,1-\delta\},
\qquad \kappa=1-2\delta.
```

The stationary distribution is fair, and the centered activation has correlation $`\kappa^\ell`$ across $`\ell`$ slots. Thus small $`\delta`$ gives long runs of the same state; $`\delta`$ close to one gives near-alternation. At $`\delta=1/2`$, activation bits are independent.

At any fixed slot, an input prepared independently of the hidden activation process sees the marginal channel

```math
\mathcal F_w(\rho)
=\tfrac12\rho+\tfrac12O_w\rho O_w.
```

This equation does not describe an independent channel application to a system already correlated with the hidden memory. In particular, an adaptive choice of when to query can change the posterior activation probability. The lower bound permits that adaptation rather than assuming independent faults or independent restarts.

The algorithm has no activation flags, environment access or reset of the hidden process. It may use ideal known gates, fresh algorithm-owned registers, measurements and classical randomization. Preparing a fresh search register does not reset $`b_t`$.

## 3. Two clock contracts

### Clock-driven oracle

The environment advances once per elapsed slot, whether the algorithm queries or idles. A slot supports at most one actual oracle call. Write $`K`$ for the random number of actual calls on an execution, $`q`$ for a fixed upper bound on $`K`$, and $`T`$ for the fixed elapsed-slot horizon. Every branch satisfies $`K\le q\le T`$ after harmless padding of the budgets. An algorithm that stops early can retain its output and idle to the common horizon.

Query times may depend on earlier classical outcomes. Idle slots consume $`T`$ but not $`q`$. The lower bound also allows a coherent enable flag, a stronger access model introduced only for the converse. This does not add a controlled query to the constructive assumptions.

### Call-driven oracle

The same Markov transition occurs once per consumed physical oracle call. Waiting without calling does not advance the hidden process. Every dummy call used to allow mixing is charged. Write $`Q`$ for the fixed total physical-call budget in this contract.

These are different resource models. A clock-driven construction cannot be assigned the call-driven query cost while treating its idle periods as free transitions.

## 4. Main resource theorem

**Theorem Q: quantum search.** Uniformly in $`N\ge3`$ and supplied $`0<\delta\le1`$, every successful clock-driven quantum algorithm obeys

```math
q=\Omega(\sqrt N+rN),
\qquad
T=\Omega(\sqrt N+rN+\delta^{-1}).
```

There is a single algorithm attaining both corresponding upper bounds:

```math
q=O(\sqrt N+rN),
\qquad
T=O(\sqrt N+rN+\delta^{-1}).
```

The hidden constants are absolute and independent of $`N`$ and $`\delta`$. The statement holds for uncontrolled phase access and for coherent bit access. Its upper bound has zero false positives and succeeds on a unique mark with probability at least $`9/10`$.

For the call-driven contract, the optimal fixed budget is

```math
Q=\Theta(\sqrt N+rN+\delta^{-1}).
```

**Theorem C: classical search under the same bit oracle.** The clock-driven optima are simultaneously attainable:

```math
q_{\mathrm C}=\Theta(N),
\qquad
T_{\mathrm C}=\Theta(N+\delta^{-1}).
```

The optimal call-driven classical budget is $`\Theta(N+\delta^{-1})`$. These are randomized bounded-error bounds; the upper construction again has zero false positives.

The joint statements mean that one algorithm achieves both resource scales. They do not combine the query optimum of one algorithm with the elapsed-time optimum of another.

## 5. Proof dependencies

| Ingredient | What it establishes | Authoritative account |
|---|---|---|
| Simulation by an ideal oracle | Quantum $`\Omega(\sqrt N)`$ and classical $`\Omega(N)`$ call requirements | [Lower bounds](lower-bounds.md), [classical comparison](classical-comparison.md) |
| Conditional-state decomposition and memory potential | $`\mathbb E_{\varnothing}K\ge(4/25)rN`$, including adaptive idles | [Lower bounds](lower-bounds.md) |
| Entirely inactive environment path | $`\Omega(\delta^{-1})`$ elapsed slots, or charged calls in the call-driven contract | [Lower bounds](lower-bounds.md) |
| Mixing, short Grover runs and exact certification | Simultaneous upper bounds for $`0<\delta\le1/2`$ | [Upper bounds](upper-bounds.md) |
| Two consecutive queries expose one innovation | IID logical oracle and upper bounds for $`1/2\le\delta\le1`$ | [Upper bounds](upper-bounds.md) |
| Bounded classical sampling after mixing | Matched classical baseline with the same process | [Classical comparison](classical-comparison.md) |

The memory potential also applies to weighted reflection alternatives. If $`\sum_a\omega_aP_a\preceq I`$, it gives $`\mathbb E_{\varnothing}K\ge(4/25)r\sum_a\omega_a`$. A Boolean-oracle specialization yields $`\Omega(r\,\operatorname{fbs}(f,0^n))`$ when the all-zero string lies in the promise. The identity reference is part of that claim; see the [weighted extension](weighted-extension.md).

## 6. Preparation, verification and time units

The upper algorithms prepare a uniform superposition over known indices and reflect about it. For $`N=2^n`$, preparation is $`n`$ Hadamard gates. Arbitrary $`N`$ admits an explicit construction from known rotations with polynomial cost in $`\log N`$, given in the [upper-bound account](upper-bounds.md). The marked item is never loaded as classical data, and no QRAM is assumed.

Certification uses two known superpositions, each containing the candidate and a distinct reference index. Neither reference needs to be known unmarked. A false candidate cannot pass both tests under the zero-or-one-mark promise, on any hidden trajectory. The success proof counts both verification calls and the time they occupy.

Each preparation, reflection and candidate test uses polynomially many known gates in $`\log N`$ in the ideal-control query model. Explicit loop and waiting counters can require $`O(\log N+\log T)`$ classical bits. The output is one classical index, using $`O(\log N)`$ bits, or `none`.

The elapsed quantity $`T`$ is a **discrete oracle-interaction clock**, with ideal control operations between slots. It is not a full hardware gate-depth or wall-clock bound. If physical control operations themselves take appreciable time while the environment evolves, their duration must enter that different timing contract. Likewise, the cost of implementing the unknown black-box oracle is outside the query model.

## 7. Endpoints and scope

The exclusion of $`\delta=0`$ is necessary for the $`9/10`$ success requirement: with probability one half the oracle is inactive forever. At $`\delta=1`$, the initial bit is hidden but every consecutive pair contains exactly one active call, so two ordinary calls make one perfect logical query.

The condition $`N\ge3`$ supports the two-distinct-reference phase certificate. With an uncontrolled phase oracle and $`N=2`$, the two possible marked oracles differ only by a global phase, so mark identification is impossible. The bit interface has no such ambiguity, but the common theorem uses one domain for both interfaces.

The main law concerns stationary fair initialization, a supplied switching rate, a zero-or-one-mark promise, ideal other operations and the two explicit clock contracts. [Related work](../references/RELATED_WORK.md) distinguishes the hidden omission process from noise applied after a correct oracle and attributes the standard search and faulty-oracle ingredients.
