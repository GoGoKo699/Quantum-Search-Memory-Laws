# Independent pairs: a supporting comparison

A process refreshed independently after every two calls provides a compact example of why single-call noise does not determine query complexity. It has a different timing law from the [stationary Markov oracle](model.md), whose hidden state persists across all trial boundaries.

## 1. Process and theorem

Keep the zero-or-one-mark phase-search task with $`N\ge3`$ and success $`9/10`$. Calls arrive in known consecutive pairs. Different pairs are independent, and the activation bits within each pair obey

```math
\Pr(00)=\Pr(11)=\frac{1-\eta}{2},
\qquad
\Pr(01)=\Pr(10)=\frac\eta2,
\qquad 0\le\eta\le\frac12.
```

Every slot has the same fair marginal omission channel. The algorithm receives neither activation flags nor an environment reset operation; independent refresh after a pair is part of the process definition. Every consumed slot, including padding and verification, counts as a physical query.

**Theorem P.** The optimal fixed query budget for this paired process is

```math
Q_\eta(N)=\Theta(\sqrt N+\eta N).
```

The upper bound needs only uncontrolled phase access, and its certificate has zero false positives. The lower bound allows arbitrary algorithm-owned ancillas, intermediate operations and adaptation between the two slots of a pair. The theorem concerns the stated interval $`0\le\eta\le1/2`$.

## 2. Matched pairs make pauses or double Grover steps

Let $`\lvert s\rangle=N^{-1/2}\sum_j\lvert j\rangle`$, $`R_s=2\lvert s\rangle\langle s\rvert-I`$ and $`G_w=R_sO_w`$. Use one known reflection after each physical query. On a matched pair with activation bit $`b`$,

```math
(R_sO_w^b)^2
=\begin{cases}
I,&b=0,\\
G_w^2,&b=1.
\end{cases}
```

At $`\eta=0`$, a run of $`B`$ pairs therefore produces $`G_w^{2K}\lvert s\rangle`$ with $`K\sim\mathrm{Binomial}(B,1/2)`$. Write $`\theta=\arcsin(N^{-1/2})`$. Averaging the usual Grover success probability gives

```math
P_B
=\mathbb E\sin^2((4K+1)\theta)
=\frac12\left[1-(\cos4\theta)^B\cos((4B+2)\theta)\right].
```

To derive the second equality, write $`\sin^2x=(1-\cos2x)/2`$ and use

```math
\mathbb E e^{8iK\theta}
=\left(\frac{1+e^{8i\theta}}2\right)^B
=e^{4iB\theta}(\cos4\theta)^B.
```

The omitted pair pauses the ideal rotation. This is an elementary consequence of the two reflections; the [attribution account](../references/RELATED_WORK.md) relates it to the reflection-reversal explanation in earlier faulty-oracle work.

## 3. Fixed-budget upper bound with charged certification

For $`N\ge1024`$, choose

```math
B=\max\left\{1,\left\lfloor
\min\left\{\frac1{16\theta},\frac1{4\eta}\right\}
\right\rfloor\right\},
```

where $`1/\eta=+\infty`$ at $`\eta=0`$. The probability that all $`B`$ search pairs match is at least $`1/2`$. Indeed, if $`B=1`$ it is $`1-\eta\ge1/2`$; otherwise $`B\eta\le1/4`$ and the union bound gives at least $`3/4`$.

Conditional on all pairs matching, their common bits remain independent and fair. Since $`(4B+1)\theta<\pi/2`$, the inequality $`\sin x\ge2x/\pi`$ on this interval yields

```math
\begin{aligned}
\mathbb E\sin^2((4K+1)\theta)
&\ge\frac4{\pi^2}\theta^2\mathbb E(4K+1)^2\\
&=\frac4{\pi^2}\theta^2(4B^2+8B+1)
\ge\frac{16B^2}{\pi^2N}.
\end{aligned}
```

Thus a measured candidate is correct with probability at least $`8B^2/(\pi^2N)`$.

Use the [two-distinct-reference certificate](upper-bounds.md) in one **fresh pair**: the first test occupies its first slot and the second test its second slot. A correct candidate is accepted when both calls are active, with probability $`(1-\eta)/2\ge1/4`$, independently of the completed search pairs. A wrong candidate never passes, because at least one of its two reference tests is entirely unmarked. This certificate uses two counted calls; it assumes neither a known unmarked reference nor a perfect membership test.

A full trial succeeds with probability at least $`2B^2/(\pi^2N)`$. Take

```math
M=\left\lceil\frac{\pi^2}{2}\log(10)\frac N{B^2}\right\rceil.
```

After $`M`$ fixed trials, return the first certified candidate, or `none` if no certificate appears. The failure probability on a marked input is at most $`\exp[-2MB^2/(\pi^2N)]\le1/10`$. The null input always produces `none`. The total budget is

```math
Q\le(2B+2)M
=O(N/B)
=O(\sqrt N+\eta N).
```

For the finite range $`3\le N<1024`$, prepare a uniform random candidate and apply the same fresh-pair certificate. Each trial succeeds with probability at least $`1/(4N)`$, so a fixed $`O(N)`$ calls suffice. On this finite range $`N\le32\sqrt N`$, so the same theorem holds after increasing the absolute constant.

## 4. Lower bound by equality of the full two-slot process

Take an IID faulty phase oracle with omission probability $`\eta`$. At the start of each desired pair, privately sample a coin $`c`$. With probability

```math
\lambda=\frac1{2(1-\eta)},
```

use the IID oracle in both slots; with probability $`1-\lambda`$, skip both calls. This is a valid mixture because $`0\le\eta\le1/2`$. Its joint activation law is exactly

```math
\begin{aligned}
\Pr(11)&=\lambda(1-\eta)^2=(1-\eta)/2,\\
\Pr(10)&=\Pr(01)=\lambda\eta(1-\eta)=\eta/2,\\
\Pr(00)&=1-\lambda+\lambda\eta^2=(1-\eta)/2.
\end{aligned}
```

These probabilities reproduce the process seen by any intervening quantum operation, including measurements and subsequent adaptation. The private coin is not exposed to the simulated algorithm. The simulator uses at most one IID faulty call per target slot.

[Regev and Schiff, Theorem 1](https://cims.nyu.edu/~regev/papers/faultygrover.pdf), gives $`Q>\eta N/[10(1-\eta)]`$ for distinguishing no mark from one mark with success $`9/10`$. The decision problem is a consequence of the search task, so this gives $`\Omega(\eta N)`$. An ideal oracle can also simulate the paired process by sampling its bits and skipping calls; the ordinary search lower bound gives $`\Omega(\sqrt N)`$. Together these lower bounds prove Theorem P.

## 5. Relation to stationary memory

Independent pair refresh guarantees repeated opportunities to enter an active pair even when $`\eta=0`$. A stationary Markov chain with $`\delta=0`$ instead remains in its initial state forever, including the inactive state with probability one half. Identifying the two models would incorrectly remove the availability obstruction from the main theorem.

The paired result shows how temporal dependence changes the effect of two ordinary phase calls. The [Markov result](model.md#4-main-resource-theorem) determines what remains possible when the hidden memory evolves continuously and the algorithm must account for its clock.
