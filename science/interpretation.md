# Memory, queries and completion time

The [main theorem](model.md#4-main-resource-theorem) separates three costs:

```math
\underbrace{\sqrt N}_{\text{ideal search}}
\quad+\quad
\underbrace{rN}_{\text{unpredictable switching}}
\quad+\quad
\underbrace{\delta^{-1}}_{\text{availability}},
\qquad r=\min\{\delta,1-\delta\}.
```

The first two constrain actual quantum oracle calls. The third constrains the elapsed oracle clock, and it also constrains calls when calls are the only way to advance the environment.

## 1. Why both ends of the switching interval help

For small $`\delta`$, the hidden bit stays constant over a long interval. After a charged period of mixing, there is a constant conditional probability of an active interval long enough for a short Grover run and its certificate. Restarts work because each new trial has a success bound conditional on the entire earlier history. The argument does not assume the hidden environment has been reset.

For $`\delta`$ close to one, the useful structure is alternation. Since $`O_w^2=I`$, two consecutive calls with no intervening operation satisfy

```math
O_w^{b_{2k}}O_w^{b_{2k-1}}
=O_w^{b_{2k}\oplus b_{2k-1}}
=O_w^{z_{2k-1}}.
```

The odd innovations are independent. Pairing therefore produces an IID logical oracle with omission probability $`1-\delta`$. This mechanism explains the symmetric memory-loss factor $`r`$ in the query law. The availability penalty is asymmetric because an active run is useful while a permanently inactive run reveals nothing.

At $`\delta=1/2`$, the activation bits are independent and the query law becomes linear. This agrees with the IID faulty-oracle obstruction of [Regev and Schiff](../references/RELATED_WORK.md). At $`\delta=1`$, pairing gives an exact oracle despite the fair marginal inactivity of every fixed slot.

## 2. A query advantage can survive without a time advantage

Consider a persistent process with $`\delta\ll1/N`$. Its useful active runs are easily long enough for ideal quantum search. The optimal quantum algorithm uses $`\Theta(\sqrt N)`$ actual calls; a classical algorithm requires $`\Theta(N)`$.

However, both algorithms require $`\Theta(1/\delta)`$ elapsed slots. Otherwise an entirely inactive trajectory remains too likely for success $`9/10`$. The quantum algorithm needs fewer interactions with the oracle, while activation controls the completion time of both algorithms.

For $`\delta=N^{-\alpha}`$, with $`\alpha>0`$ fixed and $`N`$ sufficiently large, the complete comparison is:

| Persistence exponent | Quantum actual calls | Quantum elapsed slots | Classical elapsed slots |
|---|---:|---:|---:|
| $`0<\alpha<1/2`$ | $`\Theta(N^{1-\alpha})`$ | $`\Theta(N^{1-\alpha})`$ | $`\Theta(N)`$ |
| $`\alpha=1/2`$ | $`\Theta(\sqrt N)`$ | $`\Theta(\sqrt N)`$ | $`\Theta(N)`$ |
| $`1/2<\alpha<1`$ | $`\Theta(\sqrt N)`$ | $`\Theta(N^\alpha)`$ | $`\Theta(N)`$ |
| $`\alpha\ge1`$ | $`\Theta(\sqrt N)`$ | $`\Theta(N^\alpha)`$ | $`\Theta(N^\alpha)`$ |

Classical actual calls are $`\Theta(N)`$ in every row. Each row uses the clock-driven contract and one algorithm per computational model that simultaneously attains its call and slot bounds. In the call-driven contract, the quantum charged-call cost equals the quantum elapsed expression in this table.

For near-alternation, write $`1-\delta=N^{-\alpha}`$. Availability costs only a constant, so both quantum resources are $`\Theta(\sqrt N+N^{1-\alpha})`$ and both classical resources are $`\Theta(N)`$.

## 3. What the lower bound adds

Analyzing one noisy Grover circuit can show that a particular strategy improves or fails. The [memory potential](lower-bounds.md) controls every adaptive algorithm in the stated model. It keeps two subnormalized vectors associated with the hidden states and tracks their mean and difference. A query can build distinguishability from the null oracle; the Markov transition multiplies the difference component by $`\kappa`$, contracting its norm for $`0<\delta<1`$.

The potential weights these two effects so that the total increase at a slot is bounded by the null-instance probability of making a relevant query. Idle slots do not increase it. Thus the memory-loss obstruction is charged to actual calls even when the algorithm chooses its query times adaptively. A separate argument charges inactivity to elapsed time. These two arguments are why the resource distinction remains valid beyond the displayed constructions.

The [weighted extension](weighted-extension.md) identifies the common operator feature: a packing of the projectors on which different alternatives act nontrivially. Search uses orthogonal marked-index projectors. The fractional-block-sensitivity corollary uses a fractional packing of sensitive sets at an identity reference input.

## 4. What a single-call channel omits

All switching rates in the model have the same fair single-slot marginal channel. Their optimal search costs nonetheless range from Grover scaling to linear calls, with a separate availability scale. The temporal process determines how an earlier interaction constrains later faults.

The [independent-pair example](paired-comparison.md) makes the same distinction with a different clock. Perfectly repeated omission bits convert two Grover steps into either a double step or a pause. The stationary Markov process has no independent pair refresh; its availability cost is therefore part of the main theorem rather than inherited from that example.

Noise-assisted or memory-assisted search behavior has prior literature. The [source comparison](../references/RELATED_WORK.md) identifies the exact operation, timing and accessible information in the closest models. Here the conclusion is the optimal resource law for hidden oracle omissions under the stated clock contracts. It does not transfer automatically to local gate noise, dephasing after a correct query, or a device on which control operations change the effective sampling times.
