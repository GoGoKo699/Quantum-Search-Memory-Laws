# Weighted reflection families and fractional block sensitivity

The Markov lower-bound argument extends from individual marked items to weighted collections of distinguishable inputs. The relevant condition is an operator packing inequality. It yields a fractional block-sensitivity lower bound at the identity input, with the same separation between actual oracle calls and oracle slots.

Throughout,

```math
b_1\sim\mathrm{Bernoulli}(1/2),\qquad
b_{t+1}=b_t\oplus z_t,\qquad
z_t\stackrel{\mathrm{iid}}{\sim}\mathrm{Bernoulli}(\delta),
\qquad
r=\min\{\delta,1-\delta\},
```

where $`0<\delta\leq1`$ is known. The noise is external and unobserved. No fault flags or noise resets are available. It advances once per oracle slot, including idle slots. Ideal controls, ancillas, measurements, and private randomness are allowed. The schedule may adapt classically to recorded outcomes, with deterministic maximum slot horizon $`T`$. Let $`K`$ be the random number of actual oracle calls and $`q`$ a worst-case bound on $`K`$. Required success is $`0.9`$ on every promised input.

The weighted input construction for independently negligent queries appears in Agarwal, Rao, and Song [ARS, Section 3], building on the pure-component method of Regev and Schiff [RS]. The proof below supplies the two-state memory recurrence explicitly. It uses the weighted construction as a method, without identifying an arbitrary correlated omission process with independent negligence.

## 1. An operator packing theorem

Consider a finite family of oracle inputs. Let the reference input have oracle $`R_0=I`$. Every alternative input $`a`$ has a reflection oracle

```math
R_a=I-2P_a,
\qquad P_a=P_a^\dagger=P_a^2.
```

Assume that the output required on $`a`$ differs from that required on the reference. Choose nonnegative weights $`\omega_a`$ satisfying

```math
\sum_a\omega_aP_a\preceq I,
\qquad
W=\sum_a\omega_a.
\qquad\text{(1)}
```

The projectors need not be mutually orthogonal or commute.

### Theorem 1: weighted reference bound

For $`0<\delta<1`$, every algorithm with the stated correctness and resource guarantees satisfies

```math
\boxed{
\mathbb E_0K
\geq
\frac4{25}
\frac{\delta(1-\delta)}{1-2\delta+2\delta^2}\,W
\geq\frac4{25}\,rW.
}
\qquad\text{(2)}
```

The expectation is on the reference input. At $`\delta=1`$, the memory-dependent conclusion reduces to the trivial bound zero.

### Proof

Use the [fixed-horizon normal form](lower-bounds.md#4-a-fixed-horizon-normal-form) to purify the algorithm's private operations, retain its classical schedule records, and pad stopped branches by disabled slots. The reference oracle is the identity, so its enlarged algorithm state $`\psi_t`$ is pure and independent of the hidden bit.

For the lower bound, allow controlled reflection access with projectors

```math
\widehat P_a=P_a\otimes|1\rangle\langle1|_E,
\qquad
J=I\otimes|1\rangle\langle1|_E.
```

This strengthens the original access. The packing condition gives

```math
\sum_a\omega_a\widehat P_a\preceq J.
\qquad\text{(3)}
```

Let $`p_t=\langle\psi_t|J|\psi_t\rangle`$. Because the schedule records are retained, $`p_t`$ is the reference-input probability of making an actual call in slot $`t+1`$, and $`\sum_{t=0}^{T-1}p_t=\mathbb E_0K`$.

Apply [Lemmas 2–4 of the search lower-bound proof](lower-bounds.md#lemma-2-conditional-positive-components) separately to the identity reference and each reflection $`I-2\widehat P_a`$. Their individual-input arguments require only an orthogonal reflection projector and an identity reference; they do not require the index projectors of unstructured search. In particular, they provide nonnegative potentials $`F_t^a`$ with $`F_0^a=0`$ and the one-slot bound

```math
F_{t+1}^a-F_t^a
\leq A_\delta\|\widehat P_a\psi_t\|^2,
\qquad
A_\delta=\frac{1-2\delta+2\delta^2}{\delta(1-\delta)}.
```

Since $`\widehat P_a`$ is a projector, (3) now yields

```math
\begin{aligned}
\sum_a\omega_a(F_{t+1}^a-F_t^a)
&\leq A_\delta
\sum_a\omega_a\langle\psi_t|\widehat P_a|\psi_t\rangle\\
&\leq A_\delta\langle\psi_t|J|\psi_t\rangle
=A_\delta p_t.
\end{aligned}
\qquad\text{(4)}
```

The correct output on $`a`$ differs from that on the reference. Therefore the event of returning the reference's required value has probabilities at least $`0.9`$ and at most $`0.1`$, respectively. Its probability difference is at least $`4/5`$. Lemma 4 then gives $`F_T^a\geq4/25`$ for every $`a`$. Summing (4) over the finite horizon gives

```math
\frac4{25}W
\leq\sum_a\omega_aF_T^a
\leq A_\delta\sum_{t=0}^{T-1}p_t
=A_\delta\mathbb E_0K.
\qquad\text{(5)}
```

This proves the first inequality of (2). For $`r=\min\{\delta,1-\delta\}\leq1/2`$,

```math
A_\delta
=\frac{1-2r+2r^2}{r(1-r)}
\leq\frac1r,
```

which proves the second. $`\square`$

## 2. Fractional block sensitivity at the identity input

Let $`f:D\to\{0,1\}`$ be a partial Boolean function with $`D\subseteq\{0,1\}^n`$ and $`0^n\in D`$. Total functions are included. For $`B\subseteq[n]`$, write $`1_B`$ for its indicator string. The sensitive blocks at zero are

```math
\mathcal B_0
=\{B\subseteq[n]:1_B\in D,\ f(1_B)\ne f(0^n)\}.
```

Define

```math
\begin{aligned}
\mathrm{fbs}(f,0^n)
={}&\max_{\omega_B\geq0}\ \sum_{B\in\mathcal B_0}\omega_B\\
\text{subject to }&
\sum_{\substack{B\in\mathcal B_0\\i\in B}}\omega_B\leq1
\quad\text{for every }i\in[n].
\end{aligned}
\qquad\text{(6)}
```

All sensitive blocks are nonempty, so the coordinate constraints already imply $`\omega_B\leq1`$. The optimum is finite and attained. The same packing definition and its use for negligent queries are given in [ARS].

We state the principal corollary in the standard bit-response model:

```math
O_x|i,a\rangle=|i,a\oplus x_i\rangle.
```

A noisy call is $`O_x^{b_t}`$, with exactly the common Markov process specified above. The oracle at $`0^n`$ is the identity. For $`x=1_B`$,

```math
O_{1_B}=I-2P_B,\qquad
P_B=\sum_{i\in B}|i\rangle\langle i|
\otimes|-\rangle\langle-|_R\otimes I_{\mathrm{work}}.
\qquad\text{(7)}
```

For every feasible solution of (6),

```math
\begin{aligned}
\sum_{B\in\mathcal B_0}\omega_BP_B
&=\sum_{i=1}^n
\left(\sum_{\substack{B\in\mathcal B_0\\i\in B}}\omega_B\right)
|i\rangle\langle i|\otimes|-\rangle\langle-|_R
\otimes I_{\mathrm{work}}\\
&\preceq I.
\end{aligned}
\qquad\text{(8)}
```

Each input $`1_B`$ requires an output different from that at $`0^n`$. Theorem 1 therefore applies to an optimal packing.

### Corollary 2

For $`0<\delta<1`$, every bounded-horizon algorithm computing $`f`$ with success $`0.9`$ on every input in $`D`$ satisfies

```math
\boxed{
\mathbb E_{0^n}K
\geq\frac4{25A_\delta}\mathrm{fbs}(f,0^n)
\geq\frac4{25}\,r\,\mathrm{fbs}(f,0^n).
}
\qquad\text{(9)}
```

The response qubit may be in an arbitrary coherent state and may be entangled with the rest of the algorithm. The derivation uses the full projector in (7), not a restriction to a phase-kickback input.

For uncontrolled phase access $`O_x|i\rangle=(-1)^{x_i}|i\rangle`$, use $`P_B=\sum_{i\in B}|i\rangle\langle i|\otimes I`$ instead. The same necessary bound holds for every function computable in that model. Uncontrolled phase access can have global-phase indistinguishability obstructions; for example, $`0^n`$ and $`1^n`$ cannot be distinguished by their uncontrolled phase oracles. The standard bit-response formulation avoids that access limitation and supports a direct comparison with classical bit queries.

For the at-most-one-mark decision promise, the sensitive blocks are the $`n`$ singletons and $`\mathrm{fbs}(f,0^n)=n`$. Thus (9) specializes to the search memory bound.

## 3. Ordinary query complexity and availability

Let $`Q_{0.1}(f)`$ denote the ideal quantum query complexity of $`f`$ with error at most $`0.1`$, in the standard bit-response model. A noisy algorithm can be simulated exactly using ideal queries by privately sampling its Markov trajectory and applying an ideal query only at its active attempted calls. The simulation uses at most $`q`$ ideal queries. Therefore

```math
q\geq Q_{0.1}(f).
\qquad\text{(10)}
```

Combining this with (9) gives the necessary actual-call bound

```math
q=\Omega\!\left(
Q_{0.1}(f)+r\,\mathrm{fbs}(f,0^n)
\right).
\qquad\text{(11)}
```

Suppose $`f`$ is nonconstant. Since $`0^n\in D`$, some input $`y\in D`$ has a different output. On the event that every one of the first $`T`$ hidden bits is zero, the algorithm on $`y`$ has the same output distribution as on $`0^n`$. That event has probability $`\tfrac12(1-\delta)^{T-1}`$, so correctness on the two inputs requires

```math
\frac9{20}(1-\delta)^{T-1}\leq\frac1{10}.
```

For $`0<\delta\leq1/2`$, this implies $`T=\Omega(1/\delta)`$. For $`\delta\geq1/2`$, the term $`1/\delta`$ is bounded and is absorbed by the nonzero ideal query complexity. Since $`T\geq q`$,

```math
T=\Omega\!\left(
Q_{0.1}(f)
+r\,\mathrm{fbs}(f,0^n)
+\frac1\delta
\right).
\qquad\text{(12)}
```

When every consumed oracle call advances the noise and idle time does not, the call and slot budgets coincide, so (12) is also a call-count lower bound. When idle slots advance the noise, the availability term belongs to $`T`$, not to $`q`$.

No matching upper bound is asserted for arbitrary $`f`$. Equations (9)–(12) are necessary resource bounds.

## 4. Why the reference input remains fixed

The corollary concerns $`\mathrm{fbs}(f,0^n)`$. It does not replace it by

```math
\mathrm{fbs}(f)=\max_{x\in D}\mathrm{fbs}(f,x).
```

For ideal bit or phase queries, a known input translation satisfies

```math
O_{x\oplus a}=O_aO_x.
```

The same correction does not preserve an omitted query. Given the actual noisy call $`O_x^b`$, applying the known $`O_a`$ produces $`O_aO_x^b`$. The desired translated omission would be

```math
O_{x\oplus a}^{\,b}=O_a^bO_x^b.
```

When $`b=0`$, the former is $`O_a`$ and the latter is the identity. An unobserved fault therefore prevents this translation argument. The same obstruction is explicit for independent negligent queries in [ARS, Section 3.1].

The reference oracle being the identity is also used analytically: it supplies a pure reference state independent of the hidden bit. This property is not guaranteed at another input center in the omission model. A bound maximized over input locations would need a separate proof and is not a consequence of the operator packing theorem.

## 5. Scope

The resource guarantees are worst-case actual-call and oracle-slot budgets. The expected-call inequality is on the reference input within a deterministic finite slot horizon. It does not assert a theorem for unbounded stopping times or arbitrary expected-time budgets.

The proof assumes the fair stationary two-state chain. It covers $`\delta>1/2`$ because the potential depends on $`(1-2\delta)^2`$. At $`\delta=1`$, the memory term vanishes; ordinary ideal-query and nonconstant-input distinguishability bounds remain. A biased stationary chain, observable fault information, or environment reset would require a different statement.

## References

- **[RS]** Oded Regev and Liron Schiff, *Impossibility of a Quantum Speed-up with a Faulty Oracle*, ICALP 2008. [Primary preprint, arXiv:1202.1027](https://arxiv.org/abs/1202.1027).
- **[ARS]** Mehil Agarwal, Shravas Rao, and Fang Song, *Noisy Quantum Query Complexity via Fractional Block Sensitivity*, arXiv:2610.00506v2 (2026). [Primary full text](https://arxiv.org/html/2610.00506v2), especially Section 3 for the weighted identity-input negligent-oracle bound and the failure of translation covariance.
