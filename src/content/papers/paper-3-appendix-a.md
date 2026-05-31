---
title: "Appendix A – Generalized EGH Formulas"
kind: "appendix"
paperNumber: 3
order: 2
subtitle: "Closed-form moment identities for the bulk-marginal diagonal in the grouped-Dirichlet regime."
---


*Technical appendix extending EGH 2507.06046's equations (4.6) and (4.18)
to arbitrary complex bulk states via explicit O(n) Weingarten computation.
Referenced in §8.1 of the main text. This material was developed during
the Phase 3 numerical program of the research that led to the main paper;
it is included here because it fills a minor but genuine gap in the
published EGH formulas and is verified against direct Monte Carlo
simulation at high precision.*

---

## A.1 Setup

This appendix works within the EGH 2507.06046 construction, briefly
recapped here. The bulk Hilbert space factorizes as
$\mathcal{H}_{\rm bulk} = \mathcal{H}_{M_a} \otimes \mathcal{H}_{M_b}
\otimes \mathcal{H}_\alpha \otimes \mathcal{H}_\beta$, where
$(M_a, M_b)$ are matter factors and $(\alpha, \beta)$ are two auxiliary
pointer systems – $\alpha$ the AdS-boundary observer and $\beta$ the
closed-universe observer. The EGH encoding map is
$$
V \;=\; \sqrt{d_b}\; V_{\rm HKLL} \otimes \langle 0 |_b\, O,
\qquad d_b \equiv d_\beta\, d_{M_b},
$$
where $V_{\rm HKLL}: \mathcal{H}_{M_a} \otimes \mathcal{H}_\alpha \to
\mathcal{H}_\alpha$ is the HKLL-style reconstruction map and $O \in O(d_b)$
is a Haar-random orthogonal matrix on $\mathbb{R}^{d_b}$. The observer-included
maps $V_\alpha$ and $V_\beta$ are obtained by applying HUZ cloning to $V$
for the two respective pointer systems.

EGH's equations (4.5), (4.6), and (4.18) compute the expected purity
$\mathbb{E}_O \langle \mathrm{Tr}(\rho_{M_a}^2) \rangle$ under various
choices of the bulk state. These moments are the central SWAP-test
observables for observer complementarity in the AS2R cosmological
configuration.

### Two bulk state configurations

EGH consider two kinds of bulk states:

1. **Two-factor state** for $V_\alpha$:
   $$|\psi_1\rangle \;=\; |\psi_1\rangle_{M_a M_b} \otimes |\psi_\alpha\rangle \otimes |\psi_\beta\rangle,$$
   where $|\psi_1\rangle_{M_a M_b} = \sum_{ij} c_{ij} |i\rangle|j\rangle$
   with matrix $c \in \mathbb{C}^{d_{M_a} \times d_{M_b}}$.

2. **One-factor state** for $V_\beta$ (control/no-baby):
   $$|\psi_2\rangle \;=\; |\psi_2\rangle_{M_a} \otimes |\psi_\alpha\rangle.$$

### The EGH formulas

EGH's published expressions are:

**(4.5)** *(exact, always):* $\mathbb{E}_O \langle \mathrm{Tr}(\rho_{M_a}^2) \rangle_{V_\alpha |\psi_2\rangle} = 1$.

**(4.6)** *(stated for general bulk):*
$$
\mathbb{E}_O \langle \mathrm{Tr}(\rho_{M_a}^2) \rangle_{V_\alpha |\psi_1\rangle}
\;=\; \frac{d_b}{d_b + 2}\Bigl[\, 1 + \mathrm{Tr}(\psi^2) + \mathrm{Tr}(\psi \psi^T)\,\Bigr],
\qquad \psi \;\equiv\; c\, c^\dagger.
\tag{A.6}
$$

**(4.18)** *(stated for general bulk):*
$$
\mathbb{E}_O \langle \mathrm{Tr}(\rho_{M_a}^2) \rangle_{V_\beta |\psi_1\rangle}
\;=\; \frac{d_b}{d_b + 2}\Bigl[\,\mathrm{Tr}(\omega^2) + \mathrm{Tr}(\psi^2) + \mathrm{Tr}(\omega \omega^T)\, \mathrm{Tr}(\psi \psi^{T_{M_b}})\,\Bigr],
\qquad \omega \;\equiv\; |\psi_\beta\rangle\langle\psi_\beta|.
\tag{A.18}
$$

### The issue

Equations (A.6) and (A.18) as published are valid only under implicit
assumptions about the reality of the bulk state components. Specifically,
numerical verification reveals that:

- (A.6) holds when $c \in \mathbb{R}^{d_{M_a} \times d_{M_b}}$ (real
  matter-factor amplitudes).
- (A.18) holds when $c$ is real *and* $|\psi_\beta\rangle = |0\rangle_\beta$
  is a computational basis state.

For complex $c$, or for general $|\psi_\beta\rangle$ in (A.18), the
measured purity disagrees with (A.6) and (A.18) by terms of order unity.
This is not a bug in EGH's derivation – their physics setup implicitly
assumed these restrictions – but it does mean that applying their
formulas to a generic complex bulk state produces wrong answers.

In this appendix we derive corrected formulas (A.6$'$) and (A.18$'$) that
hold for arbitrary complex $c$ and arbitrary complex $|\psi_\beta\rangle$,
and reduce to the EGH formulas under the respective restrictions.

## A.2 O($n$) Weingarten and the source of real-vs-complex sensitivity

The averaging in (A.6) and (A.18) is over $O \sim \mathrm{Haar}(O(d_b))$,
the Haar measure on the real orthogonal group. The relevant fourth moments
are governed by the O($n$) Weingarten formula:
$$
\mathbb{E}_{O \sim O(d)}[O_{ij} O_{kl} O_{i'j'} O_{k'l'}]
\;=\; \sum_{\pi, \sigma \in M_4} \mathrm{Wg}_O(\pi, \sigma)\,
\delta_\pi(i,j,i',j')\, \delta_\sigma(k,l,k',l'),
$$
where $M_4$ is the set of pair matchings on $\{1,2,3,4\}$ and
$\mathrm{Wg}_O$ is the O($n$) Weingarten function. For our purposes, the
key feature of O($n$) Weingarten – in contrast to U($n$) Weingarten – is
that the sum runs over *pair matchings* of the full set of $2k$ indices
rather than pairs of permutations of $k$ indices.

Operationally, this means that O($n$) fourth moments contain crossed terms
of the form $O_{ij} O_{kl} O_{ij'} O_{kl'}$ (two pairs of "matched" row
indices with different column indices). When these crossed terms act on
complex bulk amplitudes $c_{ij}$, they produce combinations like
$c_{ij} c^*_{i j'} c_{kl} c^*_{kl'}$ that are *not* symmetric under
complex conjugation of $c$. In contrast, real $c$ satisfies $c^*_{ij} = c_{ij}$,
and these crossed terms collapse to the symmetric forms $\mathrm{Tr}(\psi^2)$
and $\mathrm{Tr}(\psi\psi^T)$ appearing in (A.6). For complex $c$, the
crossed terms produce a genuinely new structure.

## A.3 Generalized formula (4.6$'$)

Define, for arbitrary complex $c \in \mathbb{C}^{d_{M_a} \times d_{M_b}}$
(with $\|c\|_F = 1$) and arbitrary complex $|\psi_\beta\rangle \in \mathbb{C}^{d_\beta}$
(with $\||\psi_\beta\rangle\| = 1$), the composite matrix
$$
K: \mathbb{C}^{d_\beta \cdot d_{M_b}} \to \mathbb{C}^{d_{M_a}},
\qquad
K_{i, (n, j)} \;=\; c_{ij}\, b_n,
\qquad b_n \equiv \langle n | \psi_\beta \rangle.
$$
Let
$$
A \;\equiv\; \mathrm{Re}(K^T \bar K) \;\in\; \mathbb{R}^{(d_\beta d_{M_b}) \times (d_\beta d_{M_b})}.
$$
The matrix $A$ is real symmetric by construction.

**Proposition A.3.1.** For arbitrary complex $c$ and $|\psi_\beta\rangle$ as above,
$$
\boxed{\;\;
\mathbb{E}_O \langle \mathrm{Tr}(\rho_{M_a}^2) \rangle_{V_\alpha |\psi_1\rangle}
\;=\; \frac{d_b}{d_b + 2}\Bigl[\,(\mathrm{Tr}\,A)^2 + 2\,\mathrm{Tr}(A^2)\,\Bigr].
\;\;}
\tag{A.6$'$}
$$

*Proof sketch.* Expand $\langle \mathrm{Tr}(\rho_{M_a}^2) \rangle$ in components
of $c$ and $|\psi_\beta\rangle$. Every term carries a product of four $O$
matrix elements. Applying the O($n$) Weingarten formula to the fourth moments
and taking the large-$d_b$ simplification $\mathrm{Wg}_O(\{\text{identity matching}\}) \to 1/(d_b(d_b+2))$ (up to combinatorial factors for the two inequivalent pair matchings), one obtains the quadratic form in $A$. The specific
coefficients $(\mathrm{Tr}\,A)^2$ and $2\,\mathrm{Tr}(A^2)$ arise from the
two inequivalent pair matchings of the four $O$ indices. $\square$

**Reduction to EGH (A.6).** For real $c$ and $|\psi_\beta\rangle = |0\rangle_\beta$
(so $b_n = \delta_{n,0}$), the matrix $K$ reduces to $K_{i, (0, j)} = c_{ij}$
and vanishes for $n \neq 0$. Then $K^T \bar K$ is $d_{M_b} \times d_{M_b}$
(after dropping the empty $n \neq 0$ block), and $A = K^T \bar K = \psi$.
Hence $\mathrm{Tr}\,A = \mathrm{Tr}\,\psi = 1$ (from $\|c\|_F = 1$) and
$\mathrm{Tr}(A^2) = \mathrm{Tr}(\psi^2)$. Additionally, for real $c$, one
has the Weingarten-level identity
$(\mathrm{Tr}\,A)^2 + 2\,\mathrm{Tr}(A^2) \to 1 + \mathrm{Tr}(\psi^2) + \mathrm{Tr}(\psi \psi^T)$,
recovering (A.6) exactly.

The generalization to complex $c$ changes the value of $\mathrm{Tr}(A^2)$
by an amount proportional to $\mathrm{Im}(c)^2$ terms, and the Weingarten
crossed-matching contributions now produce genuinely new structure that
the real-$c$ simplification hides.

## A.4 Generalized formula (4.18$'$)

For the $V_\beta$ map acting on the same bulk state, the corresponding
generalization is:

**Proposition A.4.1.** For arbitrary complex $c$ and $|\psi_\beta\rangle$,
$$
\boxed{\;\;
\mathbb{E}_O \langle \mathrm{Tr}(\rho_{M_a}^2) \rangle_{V_\beta |\psi_1\rangle}
\;=\; \frac{d_b}{d_b + 2}\Bigl[\,\mathrm{Tr}(\psi^2) + \mathrm{Tr}(p_\beta^2)\bigl(1 + \mathrm{Tr}(\rho\, \rho^{T_{M_b}})\bigr)\,\Bigr],
\;\;}
\tag{A.18$'$}
$$
where:
- $\psi = c\, c^\dagger \in \mathbb{C}^{d_{M_a} \times d_{M_a}}$,
- $p_\beta$ is the diagonal matrix $p_\beta = \mathrm{diag}(|b_n|^2)_{n=1}^{d_\beta}$
  (so $\mathrm{Tr}(p_\beta^2) = \sum_n |b_n|^4 = \mathrm{Tr}(\omega^2)$ with
  $\omega = |\psi_\beta\rangle\langle\psi_\beta|$),
- $\rho = c\, c^\dagger$ reshaped with $M_b$ partial transpose: explicitly,
  $\rho^{T_{M_b}}_{(ij)(kl)} = \rho_{(il)(kj)}$ where $\rho_{(ij)(kl)} = c_{ij}\, c^*_{kl}$.

*Proof sketch.* Similar to (A.6$'$), expand in components and apply O($n$)
Weingarten to the fourth moments of $O$ that arise in $V_\beta$'s action.
The key difference from (A.6$'$) is that $V_\beta$ clones $\beta$ instead
of $\alpha$, so the $\beta$-factor enters as a quadratic form $|b_n|^2$
in both the primary trace and the crossed-matching contribution, yielding
the $\mathrm{Tr}(p_\beta^2)$ coefficient. $\square$

**Reduction to EGH (A.18).** For $|\psi_\beta\rangle = |0\rangle_\beta$,
$b_n = \delta_{n,0}$, so $p_\beta = \mathrm{diag}(1, 0, \ldots, 0)$ and
$\mathrm{Tr}(p_\beta^2) = 1$. For real $c$, additionally,
$\mathrm{Tr}(\rho\, \rho^{T_{M_b}}) = \mathrm{Tr}(\psi\, \psi^{T_{M_b}})$
(since conjugation is trivial), and $\mathrm{Tr}(\omega^2) = 1$,
$\mathrm{Tr}(\omega \omega^T) = 1$. Substituting into (A.18$'$),
$$
\frac{d_b}{d_b + 2}\Bigl[\mathrm{Tr}(\psi^2) + 1 \cdot (1 + \mathrm{Tr}(\psi \psi^{T_{M_b}}))\Bigr]
\;=\; \frac{d_b}{d_b + 2}\Bigl[1 + \mathrm{Tr}(\psi^2) + \mathrm{Tr}(\psi \psi^{T_{M_b}})\Bigr],
$$
which matches (A.18) after noting that $\mathrm{Tr}(\omega^2) + \mathrm{Tr}(\omega \omega^T) = 2$ in this limit
(both traces equal 1 for a rank-1 projector). $\square$

## A.5 Numerical verification

Both generalized formulas were verified against direct Monte Carlo
simulation for complex bulk states. Six dimension configurations spanning
$(d_\alpha, d_{M_a}, d_\beta, d_{M_b}) \in \{(2,2,2,2),\, (2,3,2,3),\,
(3,3,3,3),\, (2,2,3,3)\}$ with both maximally-entangled and Haar-random
$c$, at $N = 400$ samples of Haar-$O$ per configuration.

**Table A.1:** Verification of (A.6$'$) for complex $c$, $|\psi_\beta\rangle$ Haar
on $\mathcal{H}_\beta$. Columns show predicted vs. measured expected purity,
SEM, and the $z$-score of the discrepancy.

| $(d_\alpha, d_{M_a}, d_\beta, d_{M_b})$ | state | prediction | measured | SEM | $z$ |
|---|---|---:|---:|---:|---:|
| (2, 2, 2, 2) | max-ent | $1.1640$ | $1.1484$ | $0.018$ | $-0.86$ |
| (2, 2, 2, 2) | Haar | $1.1515$ | $1.1587$ | $0.019$ | $+0.38$ |
| (2, 3, 2, 3) | max-ent | $1.2237$ | $1.2274$ | $0.022$ | $+0.17$ |
| (3, 3, 3, 3) | max-ent | $1.1015$ | $1.0968$ | $0.014$ | $-0.33$ |
| (3, 3, 3, 3) | Haar | $1.5076$ | $1.5104$ | $0.048$ | $+0.06$ |
| (2, 2, 3, 3) | max-ent | $1.4916$ | $1.4814$ | $0.046$ | $-0.22$ |

Pooled $\chi^2 = 1.08 / 6$ dof, well within expectation. No systematic
trend in $z$ values.

**Table A.2:** Verification of (A.18$'$), same configurations.

| $(d_\alpha, d_{M_a}, d_\beta, d_{M_b})$ | state | prediction | measured | SEM | $z$ |
|---|---|---:|---:|---:|---:|
| (2, 2, 2, 2) | max-ent | $0.8378$ | $0.8400$ | $0.004$ | $+0.52$ |
| (2, 2, 2, 2) | Haar | $1.2876$ | $1.2916$ | $0.029$ | $+0.14$ |
| (2, 3, 2, 3) | max-ent | $1.0776$ | $1.0593$ | $0.019$ | $-0.97$ |
| (3, 3, 3, 3) | max-ent | $0.6390$ | $0.6400$ | $0.003$ | $+0.31$ |
| (3, 3, 3, 3) | Haar | $1.0262$ | $1.0126$ | $0.024$ | $-0.56$ |
| (2, 2, 3, 3) | max-ent | $1.2334$ | $1.2336$ | $0.038$ | $+0.01$ |

Pooled $\chi^2 = 1.66 / 6$ dof, consistent with expectation.

In both cases, Monte Carlo verification of the original EGH formulas (A.6)
and (A.18) at the *same* parameter configurations (but with real $c$ and
$|\psi_\beta\rangle = |0\rangle_\beta$) likewise passes pooled $\chi^2$
tests, confirming that the generalizations specialize correctly.

Reproducibility is bit-identical across runs under the same seed.

## A.6 Status

The generalizations (A.6$'$) and (A.18$'$) are minor but genuine
extensions of EGH 2507.06046's published formulas, correcting for the
implicit real-$c$ assumption in the original derivations. They are not
required for the main body of this paper – our two scaling theorems
(Theorems 2 and 3) involve entirely different quantities – but they
are included here because:

1. They were derived in the course of verifying EGH's result numerically
   (Phase 3 of our computational program), and verifying them was a
   prerequisite to the subsequent two-observer work;
2. They fill a real gap in the published EGH framework, specifically for
   bulk states with nonzero imaginary matter-factor amplitudes;
3. They demonstrate that the O($n$) Weingarten machinery applied carefully
   to complex bulk states yields structurally new terms not visible in
   the real-$c$ limit.

The formulas as stated are verified analytically to reduce to the EGH
originals under the appropriate real-and/or-basis-state restrictions, and
numerically to sub-$\sigma$ precision in the complex-bulk regime.

---

*End of Appendix A. Source code for verification: `phase3_egh_direct.py`.
Data: `phase3_generalized_4_6.csv`, `phase3_generalized_4_18.csv`.*
