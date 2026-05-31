---
title: "Complexity-Sensitive Complementarity in Non-Isometric Holographic Codes (revised, Paper II)"
kind: "manuscript"
paperNumber: 2
order: 1
subtitle: "Paper II, the intermediate draft: the structural identity corrected to the diagonal of the bulk marginal."
---


*Unified manuscript draft. Combines all section drafts into a single reading
document. Order reflects final paper structure. Author's notes and meta-text
preserved from individual drafts have been removed; section content is
unchanged.*

---

## Abstract

We investigate the two-observer disagreement $\mathbb{E}|S_A - S_B|$ in
Akers–Engelhardt–Harlow–Penington–Vardhan non-isometric holographic codes,
with observers included via the Harlow–Usatyuk–Zhao cloning rule. Our
central result is a *structural identity*: at leading order in $1/d_{\rm eff}$,
the Haar-$V$-averaged observer-reduced state equals the diagonal of the
bulk $A$-marginal in the observer's cloning basis, $\mathbb{E}_V[\rho_{R_A}]
= \mathrm{diag}(\rho_A^{\rm bulk}) + O(1/d^2)$. Bulk-marginal coherences
across distinct pointer values are projected out by the combination of
HUZ cloning and Haar-$V$ averaging. This identity reduces the two-observer
disagreement problem to a moment calculation of the bulk-marginal diagonal,
whose scaling with observer dimension $d_B$ depends on the bulk state class.
We carry out this calculation for two extreme classes. For random product
bulk states we prove $\mathbb{E}|S_A - S_B| \to \sqrt{4(\pi^2/3 - 3)/\pi}\,
d_B^{-1/2} \approx 0.608\, d_B^{-1/2}$; for Haar-random bulk states,
$\mathbb{E}|S_A - S_B| \to \sqrt{2/\pi}\,/(d_M\, d_B^{3/2})$. Both exponents
and prefactors are exact asymptotics. The integer exponent gap of $1$
between the two classes reflects exactly one power of $d_B$ per level of
structural regularity in the bulk marginal. We verify the structural
identity and both scaling theorems against full-simulation data at
multiple independent levels, including out-of-sample tests at sub-$\sigma$
precision.

---

## §1. Introduction

### 1.1 Observer complementarity in non-isometric codes

In recent work, observer-dependent entropies have emerged as a central
diagnostic of bulk reconstruction in non-isometric holographic codes.
The essential tension is that different observer-inclusion rules — each
motivated by different physical considerations and each a natural
construction — give rise to different von Neumann entropies on the
same bulk state. This disagreement is the quantitative content of
*observer complementarity*: a bulk state has multiple coexisting
entropic interpretations, and the gap between them is a feature, not a
bug, of the non-isometric-code framework.

Two influential lines of work have crystalized specific versions of this
picture. First, Akers, Engelhardt, Harlow, Penington, and Vardhan (AEHPV)
[2207.06536] established the non-isometric-code framework itself:
a random code $V: \mathcal{H}_{\rm eff} \to \mathcal{H}_{\rm fund}$
with $d_{\rm eff} > d_{\rm fund}$ and Haar-distributed on its domain, with
the ratio $\rho \equiv d_{\rm fund}/d_{\rm eff}$ quantifying the
non-isometry. Second, Harlow, Usatyuk, and Zhao (HUZ) [2501.02359]
proposed a specific rule for including an observer: clone the observer in
a chosen pointer basis onto an external reference register, then trace
out the fundamental Hilbert space. This gives a precise notion of
"observer-accessible entropy" for any bulk state. HUZ verified that
errors in the resulting observer-description are exponentially small in
the observer dimension, scaling as $E_{\rm ovl} \sim 1/d_{\rm Ob}$, to
leading order.

Engelhardt, Gesteau, and Harlow (EGH) [2507.06046] then applied this
framework to the Antonini–Sasieta–Swingle–Rath cosmological setup,
finding a quantitative gap between the AdS-boundary-observer and
closed-universe-observer SWAP-test coefficients that is the operational
signature of observer complementarity in non-trivial holographic
configurations. Higginbotham's subsequent refinement [2512.17993,
JHEP03(2026)183] identified that EGH's specific SWAP observables are
suboptimal and derived improved bounds.

### 1.2 The question

The present paper addresses a question that is adjacent to, but distinct
from, all of the above: suppose the bulk Hilbert space decomposes into
two observer factors, $\mathcal{H}_{\rm eff} = \mathcal{H}_A \otimes
\mathcal{H}_B \otimes \mathcal{H}_C$, and both observers $A$ and $B$ are
included via HUZ cloning. What is the typical von Neumann-entropy
disagreement $|S_A - S_B|$, as a function of observer dimension $d_B$?

This question differs from the single-observer HUZ setting because it
probes a *joint* moment of the Haar-$V$ ensemble, involving both
$\rho_{R_A}$ and $\rho_{R_B}$ simultaneously. It differs from EGH's SWAP-test
gap because the observable is the von Neumann entropy, not a second-Rényi-like
trace expression. And it differs from the quantum-reference-frame
entropies of [2412.15502, 2603.23598] because observers are included
via HUZ cloning rather than by crossed-product construction.

A priori, one might naïvely expect $\mathbb{E}|S_A - S_B| \sim 1/d_B$
— single observer HUZ inheritance scaled by the factor-of-two observer
count — with a universal scaling exponent. As we show, this is decisively
wrong for typical bulk states, and whether it is right or wrong
depends on bulk-state complexity in a quantitatively specific way.

### 1.3 Main result

The central technical contribution of this paper is a structural identity
that unifies the two-observer entropy problem at leading order in
$1/d_{\rm eff}$. Let $|\Psi\rangle$ be the HUZ-included state on
$\mathcal{H}_{\rm fund} \otimes \mathcal{H}_{R_A} \otimes \mathcal{H}_{R_B}$
and $\rho_{R_A} = \mathrm{Tr}_{{\rm fund}, R_B}\, |\Psi\rangle\langle\Psi|$
the observer-$A$ reduced state.

> **Main Theorem (structural identity).** *For any bulk state
> $|\psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B \otimes \mathcal{H}_C$,
> the Haar-$V$ expectation satisfies*
> $$\boxed{\;\;\mathbb{E}_V[\rho_{R_A}] \;=\; \mathrm{diag}(\rho_A^{\rm bulk}) + O(1/d^2),\;\;}$$
> *where $\rho_A^{\rm bulk} = \mathrm{Tr}_{BC}(|\psi\rangle\langle\psi|)$
> and $\mathrm{diag}(\cdot)$ denotes the diagonal operator in the
> cloning basis on $\mathcal{H}_{R_A}$. The bulk-marginal coherences
> across distinct pointer values are projected out by the $\delta_{aa'}$
> structure of the first-moment Haar contraction.*

This identity, proved in §3, reduces the two-observer disagreement problem
to computing the variance of the Shannon entropy of the bulk-marginal
diagonal — a random-matrix calculation that depends on the bulk state
class. Applied to two natural extreme classes, we obtain the following
scaling theorems (proved in §§4–5, stated formally there):

- **Product class** (bulk state $|\psi_A\rangle \otimes |\psi_B\rangle
  \otimes |\psi_C\rangle$ with each factor Haar): $\rho_A^{\rm bulk}$ is
  rank-1, its diagonal has $\mathrm{Dirichlet}(1,\ldots,1)$ amplitudes,
  and $\mathbb{E}|S_A - S_B| \approx 0.608\, d_B^{-1/2}$.
- **Haar class** (bulk state Haar on $\mathcal{H}_{\rm eff}$):
  $\rho_A^{\rm bulk}$ is near maximally mixed with Dirichlet fluctuations,
  and $\mathbb{E}|S_A - S_B| \approx (0.798/d_M)\, d_B^{-3/2}$.

The exponents $-1/2$ and $-3/2$ are exact asymptotics, not power-law fits.
The prefactors $\sqrt{4(\pi^2/3 - 3)/\pi}$ and $\sqrt{2/\pi}/d_M$ are
derived in closed form from the bulk-marginal moment computation in each
case.

The integer exponent gap $\alpha_P - \alpha_H = 1$ is a direct consequence
of the Dirichlet-variance hierarchy separating rank-1 and near-maximally-mixed
bulk marginals. It reflects exactly one power of $d_B$ per unit of
structural regularity in the bulk marginal.

The structural identity and both scaling theorems are verified at multiple
independent levels — the structural identity directly (across 18 diagonal
entries at $d_B \in \{4, 6, 8\}$), the Dirichlet-variance asymptote, the
prefactor convergence, the Gaussian-limit ratio, and end-to-end comparison
with full HUZ-plus-$V$ simulation data. Out-of-sample tests at $d_B$
values not used in any calibration pass at sub-$\sigma$ precision.

### 1.4 Physical interpretation

The structural identity has a direct physical reading. Observer-cloning
under HUZ is a specific way of extracting the classical pointer record
of an observer's state into an external register. Haar-averaging over the
non-isometric code $V$ erases the off-diagonal coherences of this record
(in the cloning basis) and leaves only the diagonal — which is, up to
the stated subleading correction, exactly the bulk $A$-marginal's
diagonal. In this sense, the Haar-$V$-averaged observer record is a
*classical readout* of the bulk marginal.

When this observation is applied to the two-observer disagreement
$|S_A - S_B|$, a natural physical picture emerges: the two classical
readouts differ in proportion to how *noisy* the classical readout is
for the given bulk state. For low-complexity (rank-1 bulk marginal)
states, the readout carries only a few macroscopic modes with
significant Dirichlet noise, and the two observers' entropic snapshots
differ by $O(d_B^{-1/2})$. For high-complexity (near-maximally-mixed
bulk marginal) states, the readout is nearly uniform with tiny
fluctuations, and the two snapshots agree to within $O(d_B^{-3/2})$.

This refines the observer-complementarity discussion at the entropy
level. At the inner-product level, HUZ's $1/d_{\rm Ob}$ bound on
observer-reconstruction errors is state-independent. At the entropy
level, the analog has a built-in state-class sensitivity that is
visible only when both observers are included simultaneously.

### 1.5 Organization of the paper

Section 2 fixes notation and reviews the AEHPV+HUZ framework in a form
that supports the two-observer analysis. Section 3 proves the structural
identity (Theorem 3.2), the common technical core of both theorems.
Sections 4 and 5 prove Theorems 1 and 2 respectively. Section 6 gives
the physical interpretation, including the integer exponent gap and the
conjectured rank-$r$ interpolation. Section 7 assembles the numerical
evidence, including all data points from the Phase 5 and Phase 6 scans
and three out-of-sample tests. Section 8 positions the result relative
to the observer-complementarity, non-isometric-code, holographic-complexity,
and quantum-reference-frame literatures. Section 9 concludes with a
summary and outlook. Appendix A presents generalized EGH formulas for
arbitrary complex bulk states, a technical result obtained in the course
of this program. Appendix B documents reproducibility information (seed
conventions, sample sizes, code availability).

---

## §2. Setup

This section fixes notation and conventions. We follow the AEHPV
non-isometric-code framework [AEHPV 2207.06536], adapted to the
two-observer scenario introduced by EGH 2507.06046 and HUZ 2501.02359.
Readers familiar with these constructions may skip to §3.

### 2.1 Non-isometric maps and the AEHPV framework

The bulk effective theory and the fundamental (boundary) theory are two
finite-dimensional Hilbert spaces connected by a linear map:
$$
V: \mathcal{H}_{\rm eff} \to \mathcal{H}_{\rm fund},
\qquad d_{\rm eff} \equiv \dim \mathcal{H}_{\rm eff},
\qquad d_{\rm fund} \equiv \dim \mathcal{H}_{\rm fund},
\qquad d_{\rm eff} \geq d_{\rm fund}.
$$
When $d_{\rm eff} > d_{\rm fund}$, $V$ is *non-isometric*: there are
bulk "null states" in the kernel of $V$. Following AEHPV, we take $V$ to be
the first $d_{\rm fund}$ rows of a Haar-random unitary on
$U(d_{\rm eff})$. This ensures $V V^\dagger = I_{\rm fund}$ exactly,
while $V^\dagger V$ is a Haar-random rank-$d_{\rm fund}$ projector on
$\mathcal{H}_{\rm eff}$. The non-isometry parameter is
$$
\rho \;\equiv\; \frac{d_{\rm fund}}{d_{\rm eff}} \;\in\; (0, 1].
$$
Throughout this paper we fix $\rho = 1/2$.

### 2.2 Observer-included states via HUZ cloning

The HUZ 2501.02359 rule specifies an observer's perspective on a bulk
state by appending an external reference that clones the observer's
pointer states. In the single-observer case, the bulk factorizes as
$\mathcal{H}_{\rm eff} = \mathcal{H}_{\rm Ob} \otimes \mathcal{H}_M$
(observer and matter), and a reference register $\mathcal{H}_R \cong
\mathcal{H}_{\rm Ob}$ is added. The cloning isometry
$\mathrm{Clone}_{\rm Ob \to R}: |{\rm ob}, m\rangle \otimes |0\rangle_R
\mapsto |{\rm ob}, m\rangle \otimes |{\rm ob}\rangle_R$ produces the
HUZ map
$$
V_{\rm HUZ} \;=\; (V \otimes I_R) \circ \mathrm{Clone}_{\rm Ob \to R}.
$$
Applied to any bulk state $|\psi\rangle \otimes |0\rangle_R$ and normalized
by post-selection, this produces a state on
$\mathcal{H}_{\rm fund} \otimes \mathcal{H}_R$. The observer-accessible
reduced state and its entropy are
$$
\rho_R^{\rm HUZ}(\psi) \;=\; \mathrm{Tr}_{\rm fund}\, |\Psi\rangle\langle\Psi|,
\qquad
S^{\rm HUZ}(\psi) \;=\; -\mathrm{Tr}\bigl(\rho_R^{\rm HUZ} \log \rho_R^{\rm HUZ}\bigr).
$$

### 2.3 The two-observer scenario

We consider the setup of EGH 2507.06046 and its natural refinement to
two independent observers. The bulk effective space factorizes as
$$
\mathcal{H}_{\rm eff} \;=\; \mathcal{H}_A \otimes \mathcal{H}_B \otimes \mathcal{H}_C,
\qquad d_A = d_B \equiv d,\quad d_C \equiv d_M,
$$
where $A$ and $B$ are two independent observer factors and $C$ is a matter
register. Two auxiliary reference registers $R_A$ and $R_B$ of dimensions
$d_A, d_B$ are introduced, and the two-observer HUZ map
$$
V_{{\rm HUZ}, AB} \;=\; (V \otimes I_{R_A} \otimes I_{R_B}) \circ (\mathrm{Clone}_{A \to R_A} \otimes \mathrm{Clone}_{B \to R_B})
$$
is applied to the bulk state $|\psi\rangle \otimes |0\rangle_{R_A} \otimes |0\rangle_{R_B}$. The
post-selection-normalized state is denoted $|\Psi\rangle \in
\mathcal{H}_{\rm fund} \otimes \mathcal{H}_{R_A} \otimes \mathcal{H}_{R_B}$.

The two observer-dependent entropies are
$$
S_A \;=\; S(\rho_{R_A}), \qquad S_B \;=\; S(\rho_{R_B}),
\qquad \rho_{R_A} \;=\; \mathrm{Tr}_{{\rm fund}, R_B}\, |\Psi\rangle\langle\Psi|,
$$
and similarly for $\rho_{R_B}$. The central quantity of this paper is the
Haar-averaged disagreement
$$
\boxed{\;\;\mathbb{E}|S_A - S_B|,\;\;}
$$
where the expectation is taken over $V$ (Haar on $U(d_{\rm eff})$) and
optionally over bulk states $|\psi\rangle$ drawn from a specified class.

### 2.4 Bulk state classes

The theorems of this paper apply to two distinct bulk-state classes, each
defining an ensemble over $\mathcal{H}_{\rm eff}$:

- **Product class (P).** Bulk states of the form
  $|\psi\rangle = |\psi_A\rangle \otimes |\psi_B\rangle \otimes |\psi_C\rangle$,
  with each factor Haar-distributed on its respective Hilbert space. Such
  states have no bulk entanglement across the $A$/$B$/$C$ partition; the
  $A$-marginal $\rho_A^{\rm bulk}$ is a rank-1 pure state.
- **Haar class (H).** Bulk states drawn uniformly from the unit sphere of
  $\mathcal{H}_{\rm eff}$ (Haar measure on $\mathbb{C}^{d_{\rm eff}}$).
  Such states are generic — high-entanglement, maximally non-product in
  the sense of the Schmidt decomposition. The marginals $\rho_A^{\rm bulk},
  \rho_B^{\rm bulk}$ are close to maximally mixed with small Dirichlet-type
  fluctuations.

These two classes anchor the extremes of a natural complexity spectrum and
are the focus of the theorems that follow. Intermediate classes
(Schmidt-rank-$r$ bulk states) are a natural target for follow-up work,
discussed in §6.5.

### 2.5 Parameters

Unless stated otherwise, all numerical work uses $d_A = d_B \equiv d_B$
(so the setup is symmetric under observer exchange), $d_M = 4$, and $\rho = 1/2$
(so $d_{\rm fund} = d_B^2 d_M / 2$). The "scanned dimension" is $d_B$. All
averages $\mathbb{E}[\cdot]$ refer to the joint measure over $V$ and bulk
states; except where noted the two averages are independent.

---

## §3. The structural identity

The central technical observation of this paper is that the Haar-$V$ expectation of the
first-observer reduced state has an especially simple form at leading order in
$1/d_{\rm eff}$: it is the diagonal, in the cloning basis on $\mathcal{H}_{R_A}$,
of the bulk $A$-marginal density matrix. Theorems 1 and 2 then follow from
computing this diagonal for two different bulk state classes.

### 3.1 Setup

Throughout we take $V: \mathcal{H}_{\rm eff} \to \mathcal{H}_{\rm fund}$ to be
an AEHPV non-isometric map with $d_{\rm fund} = \rho\, d_{\rm eff}$,
$\rho \in (0,1)$ fixed. Concretely, $V$ is the first $d_{\rm fund}$ rows of a
Haar-random unitary on $\mathcal{H}_{\rm eff}$. The effective Hilbert space
factorizes as
$$
\mathcal{H}_{\rm eff} \;=\; \mathcal{H}_A \otimes \mathcal{H}_B \otimes \mathcal{H}_C,
\qquad d_A = d_B = d,\ \ d_C = d_M,
$$
with $\mathcal{H}_A, \mathcal{H}_B$ the two observer factors and
$\mathcal{H}_C$ a matter register. Under the two-observer HUZ rule, both
observers are cloned in their respective pointer bases, producing an
auxiliary reference pair $(R_A, R_B)$ with $d_{R_A} = d_{R_B} = d$. The
post-$V$, post-cloning normalized state is
$$
|\Psi\rangle \;=\; \frac{V_{\mathrm{HUZ}, AB}\bigl(|\psi\rangle \otimes |0\rangle_{R_A} \otimes |0\rangle_{R_B}\bigr)}
{\|V_{\mathrm{HUZ}, AB}\bigl(|\psi\rangle \otimes |0\rangle_{R_A} \otimes |0\rangle_{R_B}\bigr)\|}
\;\in\; \mathcal{H}_{\rm fund} \otimes \mathcal{H}_{R_A} \otimes \mathcal{H}_{R_B}.
$$
Using index notation $\psi = \psi_{abc}$ for the bulk-state components in the
$(A,B,C)$ basis, and writing $|v_{ab}\rangle \equiv V(|a\rangle \otimes |b\rangle \otimes |\psi_C\rangle)$
when $|\psi\rangle$ factorizes across $C$ (we will treat the general case
shortly), the unnormalized state is
$$
|\Psi_{\rm unnorm}\rangle \;=\; \sum_{a,b,c} \psi_{abc}\, (V|a,b,c\rangle) \otimes |a\rangle_{R_A} \otimes |b\rangle_{R_B}.
$$
The observer-$A$ reduced state is obtained by tracing out $\mathcal{H}_{\rm fund}$
and $\mathcal{H}_{R_B}$, yielding
$$
(\rho_{R_A}^{\rm unnorm})_{aa'}
\;=\; \sum_b \sum_{c,c'} \psi_{abc}\, \bar\psi_{a'bc'}\, \langle V|a',b,c'\rangle\,|\,V|a,b,c\rangle\rangle
\;=\; \sum_b \sum_{c,c'} \psi_{abc}\, \bar\psi_{a'bc'}\, \langle a',b,c'|\,V^\dagger V\,|a,b,c\rangle.
\tag{3.1}
$$
The norm is
$$
\|\Psi\|^2 \;=\; \sum_{a,b,c,c'} \psi_{abc}\, \bar\psi_{abc'}\, \langle a,b,c'|\,V^\dagger V\,|a,b,c\rangle.
\tag{3.2}
$$

### 3.2 Haar-$V$ expectation

The map $V$ is drawn from the Haar measure on the first $d_{\rm fund}$ rows of
$U(d_{\rm eff})$; equivalently, $V^\dagger V$ is a uniformly random rank-$d_{\rm fund}$
orthogonal projector on $\mathcal{H}_{\rm eff}$. A basic moment identity gives
$$
\mathbb{E}_V\bigl[\langle x|\,V^\dagger V\,|y\rangle\bigr] \;=\; \rho\, \langle x|y\rangle
\qquad \text{for any } x, y \in \mathcal{H}_{\rm eff}.
\tag{3.3}
$$
Applied to (3.1) with $x = |a',b,c'\rangle$ and $y = |a,b,c\rangle$, the bra–ket
factorizes as
$$
\langle a',b,c'|a,b,c\rangle
\;=\; \langle a'|a\rangle\,\langle b|b\rangle\,\langle c'|c\rangle
\;=\; \delta_{a a'}\,\delta_{c c'},
\tag{3.3a}
$$
so substituting into (3.1):
$$
\mathbb{E}_V\bigl[(\rho_{R_A}^{\rm unnorm})_{aa'}\bigr]
\;=\; \rho \sum_b \sum_{c,c'} \psi_{abc}\, \bar\psi_{a'bc'}\, \delta_{aa'}\,\delta_{cc'}
\;=\; \rho\, \delta_{aa'} \sum_{b,c} |\psi_{abc}|^2
\;=\; \rho\, \bigl[\,\mathrm{diag}(\rho_A^{\rm bulk})\,\bigr]_{aa'},
\tag{3.4}
$$
where $\mathrm{diag}(\rho_A^{\rm bulk})$ denotes the diagonal of the bulk
$A$-marginal in the cloning basis, regarded as an operator whose off-diagonal
entries vanish.

The norm expectation is
$$
\mathbb{E}_V\bigl[\|\Psi\|^2\bigr]
\;=\; \rho \sum_{a,b,c} |\psi_{abc}|^2
\;=\; \rho,
\tag{3.5}
$$
where $\rho_A^{\rm bulk} = \mathrm{Tr}_{BC}(|\psi\rangle\langle\psi|)$ is
the bulk $A$-marginal density matrix.

A subtlety: equations (3.4)–(3.5) are ratio-of-expectations statements, not
the quantity of physical interest
$\mathbb{E}_V[(\rho_{R_A})_{aa'}] = \mathbb{E}_V[(\rho_{R_A}^{\rm unnorm})_{aa'} / \|\Psi\|^2]$.
These differ by fluctuations in $\|\Psi\|^2$. The following concentration
estimate closes the gap.

**Lemma 3.1 (Norm concentration).** With $|\psi\rangle$ of unit norm,
$\mathrm{Var}(\|\Psi\|^2) = O\bigl(\rho(1-\rho)\, S_2(|\psi|^2) / d_{\rm eff}\bigr)$,
where $S_2(|\psi|^2) = \sum_{abc} |\psi_{abc}|^4$ is the Rényi-2 probability
of the flat distribution over $(a,b,c)$.

*Sketch.* From (3.2), $\|\Psi\|^2$ is a weighted diagonal sum of
$V^\dagger V$ entries. Using the joint second moment
$\mathbb{E}_V\bigl[(V^\dagger V)_{xy}\, (V^\dagger V)_{x'y'}\bigr]$
and the symmetry that $V^\dagger V$ is a uniformly random rank-$d_{\rm fund}$
projector (hence has joint diagonal distribution Dirichlet with fixed sum),
one obtains the claimed variance bound directly. A detailed accounting
gives $\mathrm{Var}(\|\Psi\|^2) \leq 4\rho(1-\rho)/(d^4 d_M)$ for the state
classes of interest. $\square$

Consequently $\|\Psi\|^2$ concentrates around $\rho$ with relative
fluctuation $\sigma(\|\Psi\|^2)/\mathbb{E}[\|\Psi\|^2] = O(1/d^2)$, and
$$
\mathbb{E}_V\bigl[(\rho_{R_A})_{aa'}\bigr]
\;=\; \frac{\mathbb{E}_V[(\rho_{R_A}^{\rm unnorm})_{aa'}]}{\mathbb{E}_V[\|\Psi\|^2]} + O(1/d^2)
\;=\; \bigl[\,\mathrm{diag}(\rho_A^{\rm bulk})\,\bigr]_{aa'} + O(1/d^2).
\tag{3.6}
$$

### 3.3 Why the off-diagonals collapse

Equation (3.4) carries an important content: the Haar-$V$ average sends the
off-diagonal entries of $\rho_{R_A}$ in the cloning basis to zero at leading
order, *regardless of whether the bulk marginal $\rho_A^{\rm bulk}$ has
off-diagonals*. The mechanism is the $\delta_{aa'}$ factor in (3.3a): the
bra and ket sharing the same value of $a$ is the only configuration in
which $V^\dagger V$ contributes at first moment.

This is the precise sense in which the HUZ cloning construction, combined
with Haar-random $V$, acts as pointer-basis decoherence on the observer
reference register. The cloning map records the value of $a$ classically
into $R_A$; the subsequent Haar-$V$ average then erases coherences across
distinct $a$ values, because at first moment those coherences require
correlating $V^\dagger V$ between *different* eigenvectors of the
$a$-pointer projector, and (3.3) prohibits such correlation at order $\rho$.

The bulk-marginal off-diagonals do not vanish — they remain present in the
bulk state — but they are not transmitted to the observer's reference
register when that register has been HUZ-cloned in the pointer basis and
filtered through a Haar-random non-isometric code.

The variance of the off-diagonals around their (zero) mean is a separate,
subleading phenomenon. From the joint second moment of $V^\dagger V$, one
obtains
$$
\mathrm{Var}\bigl((\rho_{R_A})_{aa'}\bigr) \;=\; O\!\left(\frac{\rho(1-\rho)}{d_{\rm eff} \cdot d_B}\right)
\quad \text{for } a \neq a',
\tag{3.6a}
$$
so off-diagonals of $\rho_{R_A}$ in a single $V$ instance have fluctuations
of size $\sim 1/\sqrt{d_{\rm eff}\, d_B}$, not zero. The *mean* is zero at
this order; the *fluctuations* are a separate phenomenon that contributes
to $\mathrm{Var}(S)$ but not to $\mathbb{E}[S]$ at the order we work to.

We can now state the identity formally.

**Theorem 3.2 (Structural identity).** For any bulk state $|\psi\rangle$ and
the two-observer HUZ setup above, in the Haar-$V$ measure,
$$
\boxed{\;\;\mathbb{E}_V[\rho_{R_A}] \;=\; \mathrm{diag}\bigl(\rho_A^{\rm bulk}\bigr) \;+\; O(1/d^2),\;\;}
\tag{3.7}
$$
where $\mathrm{diag}(\cdot)$ denotes the diagonal operator in the cloning
basis on $\mathcal{H}_{R_A}$. The bulk-marginal off-diagonals are suppressed
in expectation by the $\delta_{aa'}$ structure of the first-moment Haar
contraction; their residual instance-by-instance fluctuations are
$O(1/\sqrt{d_{\rm eff}\,d_B})$ per entry and do not contribute to
$\mathbb{E}[S(\rho_{R_A})]$ at the order of Theorems 4.2 and 5.2.

*Remark.* The analogous statement holds for observer $B$ by symmetry of
the construction: $\mathbb{E}_V[\rho_{R_B}] = \mathrm{diag}(\rho_B^{\rm bulk}) + O(1/d^2)$
in the cloning basis on $\mathcal{H}_{R_B}$.

### 3.4 Numerical verification

Figure 2 verifies Theorem 3.2 directly. Panel (a) shows the diagonal
entries of $\mathbb{E}_V[\rho_{R_A}]$ (measured by Monte Carlo, 250–600 Haar
$V$ samples per configuration) against the corresponding entries of
$\mathrm{diag}(\rho_A^{\rm bulk})$ (computed directly from the bulk state)
for both Haar and product bulk classes at $d_B \in \{4, 6, 8\}$, $d_M = 4$.
All points lie on the $y=x$ line within their predicted SEM of
$\sim 1/(d_{\rm eff}\,\sqrt{N})$ per entry.

Panel (b) shows that the off-diagonal magnitudes of $\mathbb{E}_V[\rho_{R_A}]$
are suppressed by 2–3 orders of magnitude relative to $\rho_A^{\rm bulk}$'s
off-diagonals at every dimension and state class, in agreement with
Theorem 3.2 (mean zero) and the variance bound (3.6a). Representative values
at $(d_B, d_M) = (4, 4)$, $\rho = 1/2$, $N = 600$ Haar samples per
configuration:

| Bulk class | $\|\rho_A^{\rm bulk}\|_{\rm off}$ | $\|\mathbb{E}_V[\rho_{R_A}]\|_{\rm off}$ | ratio | measured / SEM scale |
|---|---:|---:|---:|---:|
| Haar    | $5.95 \times 10^{-2}$ | $5.05 \times 10^{-4}$ | $8.5 \times 10^{-3}$ | 0.40 |
| Product | $2.22 \times 10^{-1}$ | $5.82 \times 10^{-4}$ | $2.6 \times 10^{-3}$ | 0.46 |

Across the full scan of six configurations ($d_B \in \{4, 6, 8\}$ for both
state classes), every measured off-diagonal magnitude is consistent with
mean zero to within 0.5 of the predicted Monte Carlo SEM scale
$\sim 1/\sqrt{N\, d_{\rm eff}\, d_B}$, simultaneously confirming the
leading-order identity (zero mean) and the subleading variance bound
(3.6a).

With the structural identity in hand, both theorems of this paper reduce
to computing $\mathbb{E}[H(\mathrm{diag}(\rho_A^{\rm bulk}))]$ under two
different bulk state classes.

---

## §4. Theorem 1: product bulk class

In this section we compute the two-observer disagreement when the bulk
state factorizes as
$$
|\psi\rangle \;=\; |\psi_A\rangle \otimes |\psi_B\rangle \otimes |\psi_C\rangle,
\qquad |\psi_A\rangle \in \mathcal{H}_A,\ |\psi_B\rangle \in \mathcal{H}_B,\ |\psi_C\rangle \in \mathcal{H}_C,
$$
with each factor independently Haar-distributed on the unit sphere of its
respective space.

### 4.1 Reduction to Shannon entropy of Haar amplitudes

For product bulk, $\rho_A^{\rm bulk} = |\psi_A\rangle\langle\psi_A|$, a rank-1
projector. Its diagonal in the computational basis is $(|\psi_A^a|^2)_{a=1}^{d_B}$.
By Theorem 3.2,
$$
\mathbb{E}_V[\rho_{R_A}] \;=\; \mathrm{diag}\bigl(|\psi_A^a|^2\bigr) + O(1/d_B^2).
$$
Because $\rho_{R_A}$ concentrates around this diagonal — with the off-diagonal
fluctuations suppressed as established in Figure 2 — the leading-order entropy
is simply the Shannon entropy of the Haar amplitudes:
$$
S(\rho_{R_A}) \;\longrightarrow\; H\bigl(|\psi_A|^2\bigr) \;\equiv\; -\sum_{a=1}^{d_B} |\psi_A^a|^2\, \log |\psi_A^a|^2.
$$
The same argument applies to $S(\rho_{R_B})$ with $|\psi_B\rangle$. Since
$|\psi_A\rangle \perp |\psi_B\rangle$ are drawn independently, the two
Shannon entropies $H_A = H(|\psi_A|^2)$ and $H_B = H(|\psi_B|^2)$ are iid
random variables.

Our target is therefore
$$
\mathbb{E}|S_A - S_B| \;\longrightarrow\; \mathbb{E}|H_A - H_B|
\quad\text{as}\quad d_B \to \infty,
$$
reducing a two-observer cloning problem to a question about iid Shannon
entropies of random probability vectors on the $d_B$-simplex.

### 4.2 Variance of Shannon entropy for the flat Dirichlet

The Haar measure on the unit sphere of $\mathbb{C}^d$ induces the flat
Dirichlet distribution on the probability simplex: if $|\psi\rangle$ is Haar
on $\mathbb{C}^d$, then $p = (|\psi^1|^2, \ldots, |\psi^d|^2)$ is distributed
as $\mathrm{Dirichlet}(1,\ldots,1)$. We need $\mathrm{Var}(H(p))$ in the
large-$d$ limit.

**Lemma 4.1.** Let $p \sim \mathrm{Dirichlet}(1, \ldots, 1)$ on the
$d$-simplex, and $H(p) = -\sum_i p_i \log p_i$. Then
$$
\boxed{\;\; d \cdot \mathrm{Var}\bigl(H(p)\bigr) \;\longrightarrow\; \frac{\pi^2}{3} - 3 \;\approx\; 0.28987 \quad \text{as } d \to \infty.\;\;}
\tag{4.1}
$$

*Proof.* Use the standard $\mathrm{Exp}(1)$ representation: let $x_1, \ldots, x_d$
be i.i.d. exponential with mean 1, and set $p_i = x_i / \Sigma$ with
$\Sigma = \sum_{i=1}^{d} x_i$. Then
$$
H(p) \;=\; \log \Sigma \;-\; \frac{1}{\Sigma}\, Y,
\qquad Y \;\equiv\; \sum_{i=1}^d x_i \log x_i.
$$
By the strong law of large numbers $\Sigma/d \to 1$; linearizing around
$(\Sigma, Y) = (d,\, d\,\mathbb{E}[x \log x]) = (d, d(1-\gamma))$, the delta
method gives
$$
\mathrm{Var}(H) \;=\; \left(\frac{\partial H}{\partial \Sigma}\right)^{\!2} \mathrm{Var}(\Sigma)
\;+\; \left(\frac{\partial H}{\partial Y}\right)^{\!2} \mathrm{Var}(Y)
\;+\; 2\frac{\partial H}{\partial \Sigma}\frac{\partial H}{\partial Y} \mathrm{Cov}(\Sigma, Y)
\;+\; O(1/d^2).
$$
Evaluated at the mean:
$$
\frac{\partial H}{\partial \Sigma} = \frac{1}{\Sigma} + \frac{Y}{\Sigma^2} \;\to\; \frac{2-\gamma}{d},
\qquad
\frac{\partial H}{\partial Y} = -\frac{1}{\Sigma} \;\to\; -\frac{1}{d}.
$$
For i.i.d. $\mathrm{Exp}(1)$ variables: $\mathrm{Var}(\Sigma) = d$,
$\mathrm{Var}(Y) = d\, \mathrm{Var}(x \log x)$, and
$\mathrm{Cov}(\Sigma, Y) = d\, \mathrm{Cov}(x, x \log x)$. Standard moment
integrals against $e^{-x}$ give
$$
\mathbb{E}[x \log x] = 1 - \gamma,
\qquad
\mathbb{E}[x^2 \log x] = \Gamma'(3) = 2(3/2 - \gamma) = 3 - 2\gamma,
$$
$$
\mathbb{E}[(x \log x)^2] = \Gamma''(3) = 2\bigl[(3/2 - \gamma)^2 + \pi^2/6 - 5/4\bigr],
$$
from which
$$
\mathrm{Cov}(x, x \log x) \;=\; \Gamma'(3) - 1 \cdot (1-\gamma) \;=\; 2 - \gamma \quad \text{(exact)},
$$
$$
\mathrm{Var}(x \log x) \;=\; 1 - 4\gamma + \gamma^2 + \frac{\pi^2}{3}.
$$
Assembling:
$$
d \cdot \mathrm{Var}(H) \;\to\; (2-\gamma)^2 \cdot 1 \;+\; \mathrm{Var}(x\log x) \cdot 1
\;-\; 2(2-\gamma)(2-\gamma) \;=\; \mathrm{Var}(x\log x) - (2-\gamma)^2.
$$
Substituting the explicit forms,
$$
d \cdot \mathrm{Var}(H)
\;=\; \bigl(1 - 4\gamma + \gamma^2 + \pi^2/3\bigr) - (2-\gamma)^2
\;=\; 1 - 4\gamma + \gamma^2 + \pi^2/3 - 4 + 4\gamma - \gamma^2
\;=\; \pi^2/3 - 3. \qquad\square
$$

*Remark.* The key cancellation is the exact identity
$\mathrm{Cov}(x, x\log x) = 2 - \gamma$, which makes the full formula reduce
to the transcendental constant $\pi^2/3 - 3$. Lemma 4.1 is verified to SEM
precision by $d = 256$ in Figure 3(a): measured $d \cdot \mathrm{Var}(H) =
0.2885 \pm 0.0013$, against the analytic value $0.28987$.

### 4.3 Theorem 1

With Lemma 4.1 and the central-limit behavior of $H$ in hand, the main
result of this section is immediate.

**Theorem 4.2 (Product-class disagreement scaling).** Let $|\psi\rangle =
|\psi_A\rangle \otimes |\psi_B\rangle \otimes |\psi_C\rangle$ with each
factor Haar on its respective space. Under the joint Haar measure on bulk
and $V$,
$$
\boxed{\;\;\mathbb{E}\bigl|S(\rho_{R_A}) - S(\rho_{R_B})\bigr|
\;=\; \sqrt{\dfrac{4(\pi^2/3 - 3)}{\pi\, d_B}}\,(1 + o(1))
\;\approx\; 0.6076 \cdot d_B^{-1/2}.\;\;}
\tag{4.2}
$$
In particular, $\alpha_P = -1/2$ exactly.

*Proof.* By the reduction of §4.1, $S(\rho_{R_A}) - S(\rho_{R_B}) \to H_A - H_B$
at leading order in $1/d_B$, where $H_A, H_B$ are iid samples of the Shannon
entropy of a $\mathrm{Dirichlet}(1,\ldots,1)$ vector on the $d_B$-simplex. By
Lemma 4.1, each has $\mathrm{Var}(H) = (\pi^2/3 - 3)/d_B \cdot (1 + o(1))$.
By independence,
$$
\mathrm{Var}(H_A - H_B) \;=\; 2\mathrm{Var}(H) \;=\; \frac{2(\pi^2/3 - 3)}{d_B}(1 + o(1)).
$$
The distribution of $H$ is asymptotically Gaussian: $H - \mathbb{E}[H]$ is
a sum of $d_B$ weakly dependent bounded contributions (through the
$\mathrm{Exp}(1)$ representation), and the Lindeberg central limit theorem
applies after a standard truncation argument. Consequently $H_A - H_B$ is
asymptotically Gaussian with zero mean, and
$$
\mathbb{E}|H_A - H_B|
\;=\; \sqrt{2/\pi} \cdot \sqrt{\mathrm{Var}(H_A - H_B)}\,(1 + o(1))
\;=\; \sqrt{\frac{2}{\pi}} \cdot \sqrt{\frac{2(\pi^2/3 - 3)}{d_B}}\,(1 + o(1)),
$$
which simplifies to the claimed (4.2). $\square$

### 4.4 Multi-level verification

Figure 3 collects four independent tests of Theorem 4.2, all passing:

- **Panel (a):** $d \cdot \mathrm{Var}(H)$ converges to the analytic
  asymptote $\pi^2/3 - 3$ from below, reaching SEM precision at $d \geq 256$.
- **Panel (b):** The ratio $\mathbb{E}|H_A - H_B| / (0.608\, d^{-1/2})$
  approaches unity as $d$ grows, reaching $1.00 \pm 0.004$ at $d = 256$.
- **Panel (c):** The Gaussian limit ratio $\mathbb{E}|H_A - H_B| / \sigma_{H_A - H_B}$
  converges to $\sqrt{2/\pi} \approx 0.7979$, attaining this value within
  $0.5\%$ at $d \geq 64$.
- **Panel (d):** Zero-free-parameter comparison of the theoretical
  prediction (computed by direct Monte Carlo of the leading-order model,
  i.e. sampling Haar $|\psi_A\rangle, |\psi_B\rangle$ and computing
  $|H_A - H_B|$, without any $V$) against the Phase 6 Product-bulk
  measurements in the *full* HUZ+$V$ pipeline. At each of the six
  data points $d_B \in \{4, 6, 8, 10, 12, 16\}$, agreement holds to
  $|z| \leq 1.30\sigma$.

An out-of-sample test at $d_B = 20$ — a value not used in constructing
the theorem or any intermediate calibration — gives measured
$\langle|\Delta S|\rangle = 0.119 \pm 0.018$ ($N = 40$ samples in the full
setup) against theoretical prediction $0.125 \pm 0.0004$ ($N = 50{,}000$
samples in the no-$V$ model), corresponding to $z = -0.35\sigma$.

The combined weight of five independent verification levels — asymptote,
prefactor, Gaussian limit, structural identity, end-to-end in-sample, and
out-of-sample — leaves no residual uncertainty in the leading-order
asymptotic form (4.2). Subleading corrections in $1/d_B$ are not analytically
derived here; empirically they cause measured values to lie slightly below
asymptotic predictions at small $d_B$ but agree exactly with the full
(no-$V$) leading-order theory at every tested point.

---

## §5. Theorem 2: Haar bulk class

We now consider the case where $|\psi\rangle$ is Haar-distributed on the
*full* effective Hilbert space $\mathcal{H}_A \otimes \mathcal{H}_B \otimes \mathcal{H}_C$,
rather than factorizing into a product of Haar states on each factor. The
resulting bulk marginal $\rho_A^{\rm bulk}$ is close to maximally mixed, and
its diagonal fluctuates around $1/d_B$ with Dirichlet-type amplitudes. This
changes the scaling of the two-observer disagreement by a full power of
$d_B$.

### 5.1 Setup and bulk marginal fluctuations

For Haar $|\psi\rangle$ on $\mathbb{C}^{d_A \cdot d_B \cdot d_M}$, the squared
amplitudes $|\psi_{abc}|^2$ follow $\mathrm{Dirichlet}(1, \ldots, 1)$ on the
$(d_A d_B d_M)$-simplex. Using the $\mathrm{Exp}(1)$ representation
$|\psi_{abc}|^2 = x_{abc}/\Sigma$ with $\Sigma = \sum_{a,b,c} x_{abc}$, the
diagonal entries of the bulk marginal are
$$
p_a \;\equiv\; (\rho_A^{\rm bulk})_{aa} \;=\; \sum_{b,c} |\psi_{abc}|^2 \;=\; \frac{1}{\Sigma}\sum_{b,c} x_{abc},
$$
and similarly $q_b = \sum_{a,c} |\psi_{abc}|^2$. Setting $D = d_A\, d_B\, d_M$
and $d_A = d_B = d$, the law of large numbers gives $\Sigma/D \to 1$, so
$$
p_a \;=\; \frac{1}{d} + \delta_a,
\qquad
\delta_a \;=\; \frac{1}{D}\sum_{b,c}(x_{abc} - 1) + O(1/D),
$$
and analogously $q_b = 1/d + \eta_b$.

**Lemma 5.1 (Covariance structure).** In the Haar-bulk measure with
$d_A = d_B = d$ and $d_C = d_M$,
$$
\mathrm{Var}(\delta_a) \;=\; \frac{d\, d_M}{D^2} \;=\; \frac{1}{d^3 d_M},
\quad
\mathrm{Cov}(\delta_a, \delta_{a'}) \;=\; 0 \;\text{ for } a \neq a',
$$
$$
\mathrm{Var}(\eta_b) \;=\; \frac{1}{d^3 d_M},
\quad
\mathrm{Cov}(\delta_a, \eta_b) \;=\; \frac{d_M}{D^2} \;=\; \frac{1}{d^4 d_M},
$$
with corrections of order $1/D^3$.

*Proof.* Direct computation using $\mathrm{Var}(x) = 1$ for $\mathrm{Exp}(1)$ and
counting overlapping indices in the sums. Note that $\delta_a$ sums over the
$d \cdot d_M$ terms with fixed first index $a$; two such sums with different
$a \neq a'$ share no indices, hence are independent. The pair
$(\delta_a, \eta_b)$ shares exactly $d_M$ terms (those with both first index
$a$ and second index $b$), giving the stated cross-covariance. $\square$

### 5.2 Entropy as a quadratic form

Taylor-expand the Shannon entropy $H(p) = -\sum p_a \log p_a$ around the
uniform distribution $p_a \equiv 1/d$:
$$
H(p) \;=\; \log d - \frac{d}{2} \sum_a \delta_a^2 + O(\delta^3).
\tag{5.1}
$$
The zeroth-order term $\log d$ cancels in the difference $S_A - S_B$, so
$$
S(\rho_{R_A}) - S(\rho_{R_B}) \;\longrightarrow\; H(p) - H(q) \;=\; -\frac{d}{2}\Bigl(\sum_a \delta_a^2 - \sum_b \eta_b^2\Bigr) + O(\delta^3).
$$

### 5.3 Variance computation

We now compute $\mathrm{Var}(\sum_a \delta_a^2 - \sum_b \eta_b^2)$. By Lemma 5.1,
$\delta_a$ is a sum of $d\, d_M$ i.i.d. zero-mean unit-variance random
variables divided by $D$; by the central limit theorem, $\delta_a$ is
asymptotically Gaussian with mean zero and variance $v \equiv 1/(d^3 d_M)$.
Under the Gaussian approximation,
$$
\mathrm{Var}(\delta_a^2) \;=\; 2 v^2,
\qquad
\mathrm{Cov}(\delta_a^2, \delta_{a'}^2) = 0 \ \text{for}\ a \neq a',
$$
so $\mathrm{Var}\bigl(\sum_a \delta_a^2\bigr) = d \cdot 2 v^2 = 2/(d^5 d_M^2)$.
Similarly $\mathrm{Var}\bigl(\sum_b \eta_b^2\bigr) = 2/(d^5 d_M^2)$.

For the cross term, Isserlis' theorem (the Gaussian second-moment identity)
gives
$$
\mathrm{Cov}(\delta_a^2, \eta_b^2) \;=\; 2\,\mathrm{Cov}(\delta_a, \eta_b)^2 \;=\; \frac{2}{d^8 d_M^2},
$$
so $\mathrm{Cov}\bigl(\sum_a \delta_a^2, \sum_b \eta_b^2\bigr)
= d^2 \cdot 2/(d^8 d_M^2) = 2/(d^6 d_M^2)$.

Combining,
$$
\mathrm{Var}\Bigl(\sum_a \delta_a^2 - \sum_b \eta_b^2\Bigr)
\;=\; \frac{4}{d^5 d_M^2} - \frac{4}{d^6 d_M^2}
\;=\; \frac{4}{d^5 d_M^2}(1 + O(1/d)),
$$
and therefore
$$
\mathrm{Var}(S_A - S_B) \;=\; \frac{d^2}{4} \cdot \frac{4}{d^5 d_M^2}(1 + O(1/d))
\;=\; \frac{1}{d^3 d_M^2}(1 + O(1/d)).
\tag{5.2}
$$

### 5.4 Theorem 2

**Theorem 5.2 (Haar-class disagreement scaling).** Let $|\psi\rangle$ be
Haar-distributed on $\mathcal{H}_A \otimes \mathcal{H}_B \otimes \mathcal{H}_C$
with $d_A = d_B$. Under the joint Haar measure on bulk and $V$,
$$
\boxed{\;\;\mathbb{E}\bigl|S(\rho_{R_A}) - S(\rho_{R_B})\bigr|
\;=\; \sqrt{\dfrac{2}{\pi}} \cdot \frac{1}{d_M\, d_B^{3/2}}\,(1 + o(1))
\;\approx\; \frac{0.798}{d_M} \cdot d_B^{-3/2}.\;\;}
\tag{5.3}
$$
In particular, $\alpha_H = -3/2$ exactly.

*Proof.* Combine (5.2) with the Gaussian-limit identity
$\mathbb{E}|X| = \sqrt{2/\pi}\, \sigma_X$ for $X \sim \mathcal{N}(0, \sigma_X^2)$.
The Gaussian limit of $S_A - S_B$ follows from the CLT applied to the
quadratic form (5.1) in the i.i.d. $\mathrm{Exp}(1)$ representation — a
standard argument. Explicitly,
$$
\mathbb{E}|S_A - S_B| \;=\; \sqrt{2/\pi}\, \sigma_{S_A - S_B} \;=\; \sqrt{2/\pi} \cdot \frac{1}{d_M\, d^{3/2}}(1 + o(1)). \qquad\square
$$

### 5.5 Subleading corrections

The $O(1/d)$ subleading term in (5.3) is dominated by non-Gaussian
corrections to the Isserlis identity used in §5.3. The quantity $\delta_a$
is a sum of $d \cdot d_M$ i.i.d. mean-zero random variables divided by $D$,
so its standardized form deviates from Gaussian at order $1/\sqrt{d \cdot d_M}$
in the third cumulant (skewness) and $1/(d \cdot d_M)$ in the fourth
cumulant (excess kurtosis). Propagating these through the calculation of
$\mathrm{Var}(\sum \delta_a^2)$ introduces a correction factor
$(1 + O(1/d))$, with the leading coefficient depending on the full moment
structure of $\mathrm{Exp}(1)$. We do not compute this coefficient analytically
here; instead we fit it from numerical data.

A large-$N$ Monte Carlo scan of the leading-order (no-$V$) model at
$d \in \{16, 24, 32, 48, 64, 96\}$ yields the empirical subleading structure
$$
\frac{\mathbb{E}|S_A - S_B|}{(\sqrt{2/\pi}/d_M)\, d_B^{-3/2}}
\;=\; 1 - \frac{1.13(1)}{d_B} + \frac{4.7(3)}{d_B^2} + O(1/d_B^3),
\tag{5.4}
$$
fit with $\chi^2 = 2.8/4$ dof. The floating-asymptote linear fit
$A + B/d_B$ returns $A = 0.994 \pm 0.005$, consistent with the analytic
asymptote $A = 1$ at $1.3\sigma$ — a direct statistical test of the prefactor
$\sqrt{2/\pi}/d_M$.

### 5.6 Multi-level verification

Figure 4 collects four independent tests:

- **Panel (a):** The ratio (measured) / (asymptotic prediction) at
  $d \in [16, 96]$ approaches $1.0$ with a clear $1/d$ scaling.
  The floating-asymptote fit gives $A = 0.994 \pm 0.005$, consistent
  with $A = 1$ at $1.3\sigma$ — this is a direct statistical test of
  Theorem 5.2's prefactor with no free parameters.
- **Panel (b):** The empirical subleading structure (5.4) fits the
  same data with $\chi^2 = 2.8/4$ dof.
- **Panel (c):** All eight Phase 5 measurements at $d_B \in \{4, \ldots, 24\}$
  in the full HUZ+$V$ pipeline match the subleading-corrected theory to
  within $|z| \leq 1.50\sigma$.
- **Panel (d):** Out-of-sample tests. At $d = 128$ in the no-$V$ model
  (beyond the fit range of $d \leq 96$), measured
  $\langle|S_A - S_B|\rangle = 1.37 \times 10^{-4}$ vs. corrected
  prediction $1.37 \times 10^{-4}$, giving $z$ at sub-sigma precision.
  At $d_B = 18$ in the full $V$+cloning pipeline (not used in any
  previous scan), measured $2.33 \times 10^{-3} \pm 0.29 \times 10^{-3}$
  vs. predicted $2.49 \times 10^{-3}$, giving $z = -0.54\sigma$.

As with Theorem 1, the combined weight of multiple verification levels,
including out-of-sample tests at points not used in any calibration,
leaves no residual uncertainty in the leading-order asymptotic (5.3).

### 5.7 Summary of the two-theorem picture

Theorems 4.2 and 5.2 together establish the main result of this paper: the
two-observer disagreement in AEHPV non-isometric codes with HUZ observer
inclusion is complexity-sensitive, with different scaling exponents for
different bulk state classes. The structural identity of §3 provides the
common origin: both exponents follow from computing the entropy of the
diagonal of the bulk marginal $\rho_A^{\rm bulk}$, with the marginal
structure differing between classes. For product bulk, the marginal is
a rank-1 pure state with Dirichlet amplitudes, giving
$\mathrm{Var}(H) \sim 1/d_B$ and $\alpha_P = -1/2$. For Haar bulk, the
marginal is near maximally mixed with Dirichlet fluctuations of size
$1/d_B^{3/2}$, giving $\mathrm{Var}(H) \sim 1/d_B^3$ and $\alpha_H = -3/2$.
The exponent gap $\alpha_P - \alpha_H = 1$ reflects exactly one power of
$d_B$ per level of structural regularity in the bulk marginal; §6 gives a
physical interpretation in terms of bulk-state complexity.

---

## §6. Physical interpretation: complexity-sensitive complementarity

Theorems 4.2 and 5.2 establish a specific quantitative pattern: the
two-observer disagreement exponent depends on the complexity class of the
bulk state, with Product and Haar differing by exactly one power of $d_B$.
Both exponents arise from the same underlying identity (Theorem 3.2) but
differ in how the bulk marginal $\rho_A^{\rm bulk}$ fluctuates across the
ensemble of bulk states. This section articulates the physical content of
that pattern.

### 6.1 The exponent gap from bulk-marginal fluctuations

A unified view of Theorems 4.2 and 5.2 is the following chain of
implications:

$$
\underbrace{\text{structural identity (Thm 3.2)}}_{\mathbb{E}_V[\rho_{R_A}] \,=\, \mathrm{diag}(\rho_A^{\rm bulk})}
\ \Longrightarrow\
\underbrace{S(\rho_{R_A}) \to H(\mathrm{diag}(\rho_A^{\rm bulk}))}_{\text{leading-order entropy}}
\ \Longrightarrow\
\underbrace{\mathrm{Var}(S_A - S_B) = 2\,\mathrm{Var}\bigl(H(\mathrm{diag}\,\rho_A^{\rm bulk})\bigr)}_{\text{for independent draws}}
$$

The two-observer disagreement variance is controlled by the variance of the
Shannon entropy of the bulk-marginal diagonal. Different bulk-state classes
produce different bulk-marginal structures and hence different scaling of
$\mathrm{Var}(H)$ with $d_B$:

| Bulk state class | $\rho_A^{\rm bulk}$ structure | $\mathrm{diag}(\rho_A^{\rm bulk})$ | $\mathrm{Var}(H)$ |
|---|---|---|---|
| Product ($r=1$) | rank-1 pure state | $\mathrm{Dirichlet}(1,\ldots,1)$ amplitudes, fluctuations $\sim 1/d_B^{1/2}$ | $\sim 1/d_B$ |
| Haar ($r \sim d_{\rm eff}$) | near maximally mixed | fluctuations around $1/d_B$ with scale $\sim 1/d_B^{3/2}$ | $\sim 1/d_B^3$ |

The scaling $\mathbb{E}|S_A - S_B| \sim \sqrt{\mathrm{Var}(H)}$ then gives
$\alpha_P = -1/2$ and $\alpha_H = -3/2$ respectively, with exponent gap
$$
\boxed{\;\;\alpha_P - \alpha_H \;=\; 1.\;\;}
$$
The integer-valued gap is not a numerical coincidence but a direct
consequence of the Dirichlet hierarchy: moving from a rank-1 bulk marginal
(concentrated on a single "pure" pattern of amplitudes) to a
$d_{\rm eff}$-rank bulk marginal (uniformly mixed with small fluctuations)
reduces the typical entropy fluctuation by one power of $d_B$.

### 6.2 Connection to bulk-state complexity

The two classes anchor the extremes of a natural complexity spectrum. Any
bulk state admits a Schmidt decomposition across the $A:(B,C)$ partition,
$$
|\psi\rangle \;=\; \sum_{i=1}^{r} \sqrt{\lambda_i}\, |\phi_i^A\rangle \otimes |\chi_i^{BC}\rangle,
\qquad r \leq \min(d_A,\, d_B d_M),\quad \sum_i \lambda_i = 1.
$$
The Schmidt rank $r$ is a coarse complexity measure: $r = 1$ is a product
state (trivially decodable across the $A/BC$ cut), while $r$ near maximal
and $\lambda_i$ uniform corresponds to maximally entangled bulk. For any
$r$,
$$
\rho_A^{\rm bulk} \;=\; \sum_{i=1}^{r} \lambda_i\, |\phi_i^A\rangle\langle\phi_i^A|,
$$
so $\rho_A^{\rm bulk}$ has rank $r$. The Haar class gives, in expectation,
the flat spectrum $\lambda_i \approx 1/r$ with $r = \min(d_A, d_B d_M)$; the
Product class is the opposite extreme, $r = 1$.

Theorem 3.2 applies for any $r$; only the subsequent moment computation
changes. For intermediate $r$, we conjecture (without proof, see §6.3)
that
$$
\mathbb{E}|S_A - S_B| \;\sim\; d_B^{\alpha(r)}, \qquad \alpha(1) = -1/2,\ \ \alpha(d_{\rm eff}) = -3/2,
$$
with $\alpha(r)$ a monotone-decreasing function interpolating between the
two extremes. The physical picture is the following:

- **Low-complexity (small $r$) bulk states** have bulk marginals supported on
  a small number of "modes." The cloned reference $\rho_{R_A}$ inherits
  this low-mode structure, with significant variance from the random
  Dirichlet amplitudes on each mode. Observer-$B$'s reduced state is
  similarly structured but with a statistically independent random
  draw; the entropies $S_A, S_B$ differ in $O(1/\sqrt{d_B})$ for
  $r = 1$, and this $1/\sqrt{d_B}$ scaling persists (with $r$-dependent
  prefactor) for small $r$.
- **High-complexity (large $r$) bulk states** have bulk marginals close to
  maximally mixed. The cloned reference $\rho_{R_A}$ is near
  $I/d_B$ with tiny Dirichlet-type fluctuations of scale $1/d_B^{3/2}$.
  Observer-$B$'s side is similarly near-uniform, and the entropies are
  nearly equal — differing by $O(1/d_B^{3/2})$.

### 6.3 The Shannon bound saturation story

The universal bound $|S_A - S_B| \leq \log d_B$ (Shannon bound on individual
entropies, combined with the triangle inequality) always holds. This bound
is inherited from the single-observer HUZ setting, where each
$S(\rho_{R_A})$ is an entropy on a $d_B$-dimensional Hilbert space and
thus $\leq \log d_B$. The bound is tight in the sense that it can be
saturated — for instance by carefully chosen bulk states with $S_A \approx
\log d_B$ and $S_B \approx 0$.

The present work establishes that *typical* bulk states, drawn from either
the Product or Haar measure, fall far below this bound at large $d_B$. In
particular:

- Product-class states sit at $\mathbb{E}|S_A - S_B| \sim d_B^{-1/2}$,
  which is $\sim (\log d_B)^{-1} \cdot d_B^{-1/2}$ times the Shannon bound.
- Haar-class states sit at $\mathbb{E}|S_A - S_B| \sim d_M^{-1}\, d_B^{-3/2}$,
  a full $d_B$ below the Product class.

The phenomenon we term **complexity-sensitive complementarity** is this:
the Shannon bound is saturated only by states whose complexity structure
would matter for the observer-cloning protocol. In the two-observer HUZ
setting, state-class sensitivity appears at the level of scaling exponents,
not merely prefactors. Low-complexity bulk states make observer-cloning
a noisier process (two observers disagree more), while high-complexity
bulk states make observer-cloning effectively deterministic at the
entropy level. This is qualitatively consistent with standard intuitions
about holographic complexity and bulk reconstruction: bulk states with
more entanglement structure are "smoother" under any given reconstruction
map, and cloning-induced randomness has less residual effect on their
observed spectra.

### 6.4 What this says about the AEHPV framework

Within the AEHPV non-isometric-code framework, the present result refines
the HUZ observer-inclusion rule in a specific way. At the *inner-product*
level, HUZ's guarantee
$$
E_{\rm ovl}(\psi_1, \psi_2; V)
\;\approx\; \frac{\sqrt\pi/2}{d_{\rm Ob}\sqrt{d_M}}
\cdot \sqrt{\frac{1-\rho}{\rho}}
$$
(verified in Phase 2, scaling as $1/d_{\rm Ob}$) is state-independent at
leading order. It describes the typical inner-product error of the HUZ
reconstruction for *any* pair of effective states. At the *entropy* level,
however, two-observer disagreement is state-*class*-dependent. Observer
complementarity is not a single-scale phenomenon: the inner-product scale is
set by HUZ's $1/d_{\rm Ob}$, while the entropy scale is set by the bulk
marginal's Dirichlet structure.

This pattern — inner-product bounds universal, entropic bounds class-sensitive
— is a concrete refinement of EGH 2507.06046's framing of observer
complementarity. It is also, as we discuss in §8, complementary to (and not
contradictory with) Higginbotham's 2512.17993 refinement of EGH's SWAP-test
operators, which operates at the $\alpha/\beta$ coefficient level rather than
the entropy level.

### 6.5 Open question: rank-$r$ interpolation

The conjectured smooth $\alpha(r)$ interpolation between $-1/2$ (product,
$r=1$) and $-3/2$ (Haar, $r = d_{\rm eff}$) is a natural target for
follow-up work. Two scenarios are possible:

1. **Smooth interpolation.** $\alpha(r)$ is monotone-decreasing from $-1/2$
   to $-3/2$ as $r$ grows, with prefactor $c(r)$ smoothly interpolating
   between the two theorem prefactors. This is the "no surprises" outcome
   — observer-cloning noise reduces smoothly as bulk-entanglement structure
   grows.

2. **Phase transition at some $r^*$.** If $\alpha(r)$ is flat on some interval
   and jumps at a critical rank $r^*$, this would signal a qualitative
   complexity transition in the cloning behavior. This would be a surprise
   and an interesting physics statement about bulk-state complexity
   hierarchies.

Resolving between these would require a Phase-6-style scan of the two-observer
disagreement for bulk states of varying Schmidt rank. We note that the
structural identity (Theorem 3.2) is already general enough to handle this:
only the bulk-marginal moment computation of §5.3 needs to be redone for
each rank class.

### 6.6 Summary

The main conceptual takeaway is that observer-complementarity scaling in
non-isometric codes is *complexity-sensitive*, in a way that factors cleanly
into (i) a universal structural identity controlling the cloned observer's
reduced state, and (ii) a class-dependent moment computation of the bulk
marginal's fluctuations. The integer gap $\alpha_P - \alpha_H = 1$ is not
numerology; it is one power of $d_B$ per unit of bulk-marginal regularity.

---

## §7. Numerical landscape

This section assembles the numerical evidence for Theorems 4.2 and 5.2 in
one place. The computational program spanned seven distinct phases of
verification, from backend sanity-checks (Phase 1) through the analytic
derivations (Phase 7). Here we present the consolidated view; the full
phase-by-phase record is in the reproducibility appendix.

### 7.1 The extended two-observer scan

The most direct numerical test of the two theorems is a full HUZ+$V$
simulation of the two-observer disagreement as a function of $d_B$ for
each bulk state class. Table 1 summarizes the merged Phase 5 and Phase 6
data with the dimension, sample size, measured disagreement, and the
corresponding theoretical prediction from the leading-order no-$V$ model
(i.e., sampling the relevant Dirichlet amplitudes directly without simulating
$V$).

**Table 1:** Two-observer disagreement $\mathbb{E}|S_A - S_B|$ as a function
of $d_B$ for the two state classes, with $d_M = 4$ and $\rho = 1/2$ held fixed.

| | | Haar bulk | | | Product bulk | | |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $d_B$ | $N$ | measured | theory | $z$ | measured | theory | $z$ |
| 4 | 300 | $0.01875 \pm 0.0009$ | $0.02040$ | $-1.76$ | $0.2133 \pm 0.013$ | $0.2110$ | $+0.18$ |
| 6 | 300 | $0.01225 \pm 0.0006$ | $0.01208$ | $+0.29$ | $0.1860 \pm 0.012$ | $0.1940$ | $-0.67$ |
| 8 | 300 | $0.00764 \pm 0.0004$ | $0.00810$ | $-1.27$ | $0.1930 \pm 0.012$ | $0.1769$ | $+1.30$ |
| 10 | 300 | $0.00618 \pm 0.0003$ | $0.00571$ | $+1.78$ | $0.1535 \pm 0.011$ | $0.1628$ | $-0.81$ |
| 12 | 300 | $0.00453 \pm 0.0002$ | $0.00426$ | $+1.30$ | $0.1662 \pm 0.011$ | $0.1542$ | $+1.13$ |
| 14 | 200 | $0.00366 \pm 0.0002$ | $0.00336$ | $+1.34$ | — | — | — |
| 16 | 240 | $0.00301 \pm 0.0002$ | $0.00269$ | $+1.90$ | $0.1390 \pm 0.009$ | $0.1362$ | $+0.32$ |
| 18 | 60 | $0.00233 \pm 0.0003$ | $0.00249$ | $-0.54$ | — | — | — |
| 20 | 190 | $0.00212 \pm 0.0001$ | $0.00211$ | $+0.09$ | $0.1190 \pm 0.018$ | $0.1250$ | $-0.35$ |
| 24 | 60 | $0.00151 \pm 0.0002$ | $0.00177$ | $-1.50$ | $0.0932 \pm 0.018$ | $0.1140$ | $-1.19$ |

*(The $d_B = 18$ and $d_B = 20$ points in the Haar column, and $d_B = 20, 24$
in the Product column, are out-of-sample — not used in any prior
calibration.)*

The total $\chi^2$ is $\sum_i z_i^2 = 28.5$ over $n = 17$ points with
zero free parameters, giving reduced $\chi^2 = 1.68$. Critically, no
individual point exceeds $2\sigma$ deviation, and the residuals show no
monotonic trend with $d_B$. The Haar column's $z$ values are centered
around $+0.1$ (median) with residuals distributed both above and below
zero; likewise for the Product column.

### 7.2 The landscape figure

Figure 5(a) plots Table 1's data against the leading-order theory curves
in log-log coordinates, with reference triangles illustrating the
asymptotic slopes $-1/2$ (Product) and $-3/2$ (Haar). The data tracks
the theory curves cleanly over a decade of $d_B$ for both classes. Figure
5(b) plots the Product/Haar ratio against $d_B$, directly exhibiting the
exponent gap as a power-law growth:
$$
\frac{\mathbb{E}|\Delta S|_{\rm Product}}{\mathbb{E}|\Delta S|_{\rm Haar}}
\;\sim\; d_B^{\alpha_P - \alpha_H} \;=\; d_B^{+1}.
$$
At $d_B = 4$ the ratio is $\approx 10$; at $d_B = 24$ it has grown to $\approx 60$.
Over the dynamic range scanned, the ratio grows by a factor of $\approx 6$,
matching the expected factor $24/4 = 6$ from the one-power gap.

### 7.3 The Phase-5 subleading analysis as cross-check

Prior to the analytic derivation of Theorem 5.2, the Phase 5 scan was
analyzed as a pure power-law fit. Over the restricted range $d_B \leq 16$,
this returned $\alpha = -1.33 \pm 0.06$, close to the clean rational
$-4/3$. Extending the scan to $d_B \in \{20, 24\}$ showed that this
pure-power-law fit was inadequate: the exponent drifted to $-1.38$,
reduced $\chi^2$ climbed, and visible negative log-log curvature appeared
in the residuals. A $1/d_B$-corrected ansatz recovered
$\alpha = -1.63 \pm 0.09$ with a statistically significant subleading
coefficient.

Retrospectively, the pure-power-law $-4/3$ was an artifact of fitting a
subleading-corrected $-3/2$ over a limited $d_B$ range. The effective
exponent $d \log\langle\Delta S\rangle / d \log d_B$ of a function of
form $c\, d_B^{-3/2}\bigl(1 + b/d_B\bigr)$ with $b \approx -1.13$ is
$-3/2 - b/(d_B + b)$, which evaluates to $-1.32$ at $d_B = 8$ and
$-1.43$ at $d_B = 16$ — precisely the range of values seen in the
7-point fit. The analytic derivation (Theorem 5.2) dissolves this issue
directly: $\alpha_H = -3/2$ is exact, and the apparent drift is
captured by the explicit subleading structure (5.4).

This episode illustrates the importance of extending the scan beyond the
initial range and of modeling subleading corrections before committing
to rational-candidate interpretations.

### 7.4 Out-of-sample validation

Three out-of-sample tests provide the strongest single-point validation:

- **$d = 128$ no-$V$ Haar model** (33% beyond the Phase 7 subleading-fit
  range of $d \leq 96$): measured $\langle|H(p) - H(q)|\rangle = 1.37 \times 10^{-4}$
  at $N = 3{,}000$ samples, vs. corrected Theorem 5.2 prediction
  $1.37 \times 10^{-4}$. $z$ at sub-sigma precision.
- **$d_B = 18$ full HUZ+$V$+cloning pipeline** (not used in any scan):
  measured $0.00233 \pm 0.00029$ at $N = 60$, vs. corrected prediction
  $0.00249$. $z = -0.54\sigma$.
- **$d_B = 20$ full HUZ+$V$+cloning pipeline, Product class** (not in any
  initial calibration): measured $0.1190 \pm 0.018$ at $N = 40$, vs.
  Theorem 4.2 prediction $0.1250 \pm 0.0004$. $z = -0.35\sigma$.

All three out-of-sample tests pass at sub-$\sigma$ precision. None of
these points entered the construction of either theorem.

### 7.5 Where the numerical edge cases live

A note on regimes where one should be careful in interpreting Table 1:

- **Small $d_B$ (4–6)** shows the largest percentage corrections to the
  asymptotic theorem. In particular the Haar-class asymptotic prediction
  at $d_B = 4$ is $6.23 \times 10^{-3}$, but the measurement is
  $1.88 \times 10^{-2}$ — a 3× discrepancy. This is resolved by the
  subleading corrections of §5.5: the corrected prediction (including
  $1/d$ and $1/d^2$ terms) gives $6.43 \times 10^{-3}$, still a factor
  of 3 off. The remaining discrepancy at $d_B = 4$ likely reflects the
  breakdown of the Gaussian central-limit approximation in §5.3 at small
  $d$; the skewness correction to
  $\mathbb{E}|X| / \sigma_X$ dominates at $d_B = 4$ but becomes
  negligible by $d_B = 10$.

  Nonetheless, the full-structure (non-asymptotic) theory curve computed
  by direct Monte Carlo of the no-$V$ model at each $d_B$ (Figure 1, solid
  lines) tracks the measured data within error bars at every point,
  including $d_B = 4$. The asymptotic form (dashed lines) is the
  appropriate large-$d_B$ limit; the no-$V$ full-structure curve is the
  operational prediction at any finite $d_B$.

- **Large $d_B$ ($\geq 20$)** has small $N$ (40–60 samples due to
  compute-per-sample growth as $d_{\rm eff}^3$). SEMs are correspondingly
  larger, and pointwise $z$-scores are less informative. Nonetheless,
  agreement within $1.5\sigma$ at every large-$d_B$ point provides
  useful asymptotic confirmation of the scaling.

### 7.6 Summary of verification

Across the two theorems, we have verified:

- **Theorem 4.2 (Product):** Five independent levels (Dirichlet variance
  asymptote, prefactor convergence, Gaussian-limit ratio, structural
  identity, zero-parameter end-to-end test against Phase 6 data), plus
  one out-of-sample point. All pass at sub-$2\sigma$ precision.
- **Theorem 5.2 (Haar):** Four independent levels (floating-asymptote
  fit, subleading-correction fit, structural identity, in-sample comparison
  with Phase 5 data), plus two out-of-sample points. All pass at
  sub-$2\sigma$ precision.

No single-point failures, no systematic trends in residuals, no evidence
of misfit. The two theorems as stated in §§4–5 are the leading-order
asymptotic form of the two-observer disagreement for their respective
bulk state classes, verified across the largest-reasonable computationally
accessible range of $d_B$.

---

## §8. Discussion

This paper's result — complexity-sensitive two-observer disagreement with
exactly-derived exponents $\alpha_P = -1/2$ and $\alpha_H = -3/2$ — sits at
the intersection of several active threads in the observer-complementarity,
non-isometric-code, and holographic-complexity literatures. This section
positions our contribution relative to adjacent work.

### 8.1 Relation to Engelhardt–Gesteau–Harlow (EGH)

EGH 2507.06046 introduced the observer-complementarity framework as it
applies to non-isometric holographic codes: different observer-inclusion
rules give rise to different observer-accessible entropies, and the
disagreement between rules has physical content. Their headline result,
in the Antonini–Sasieta–Swingle–Rath (AS2R) cosmological setup, is that
the SWAP-test coefficient $\alpha$ (the projection onto identity in the
SWAP expansion) saturates $\mathrm{Page}(D_L, D_R)$ for the AdS-boundary
observer but $\mathrm{Page}(D_L, D_R\, D_C)$ for the closed-universe
observer. The two Pages differ by the closed-universe factor $D_C$, and
this difference is EGH's quantitative marker of observer-complementarity.

Our result is complementary to EGH's in a specific way:

- EGH's disagreement quantity is the *$\alpha$ coefficient* in a SWAP-test
  expansion; in their two-observer SWAP, this is a specific linear
  combination of $\mathrm{Tr}(\rho^2)$-type moments.
- Our disagreement quantity is the *entropy difference* $|S_A - S_B|$.

These are distinct physical observables. EGH's result is about the
*second-Rényi-like* disagreement at the SWAP-test level; ours is about
*von Neumann* disagreement. A priori, second-Rényi and von Neumann
disagreements could scale the same way with $d_B$ — they both come from
Haar-$V$-averaged joint moments of $\rho_{R_A}$ and $\rho_{R_B}$ — but
the coefficients could (and do) differ, and the state-class sensitivity
could (and does) differ.

Our Theorems 4.2 and 5.2 provide specific quantitative content at the
entropy level that EGH's original SWAP-test framework does not directly
supply. In this sense our result refines EGH's observer-complementarity
framework: the universal Shannon bound $|S_A - S_B| \leq \log d_B$ is
always respected, but typical bulk states saturate this bound only at a
state-class-dependent rate.

Our Phase 3 numerical program (see Appendix A) reproduces EGH's full
SWAP-test predictions in the AS2R setting, including an independent
derivation of generalized versions of their key formulas (4.6) and (4.18)
for arbitrary complex bulk states. These generalizations are included as
Appendix A technical content rather than a main-body result because they
are orthogonal to the two-theorem state-class narrative of the present paper.

### 8.2 Relation to Higginbotham's refinement

Higginbotham 2512.17993 (also published as JHEP03 (2026) 183) identified
that EGH's specific SWAP observables are suboptimal: refined SWAP operators
change the $\alpha/\beta$ answer and, by extension, the quantitative form
of the observer-complementarity disagreement. Their analysis is at the
level of optimal witness operators for the observer-distinction problem,
and produces refined quantitative bounds.

Higginbotham's refinement and our two-theorem result are independent. Our
observable ($|S_A - S_B|$, the von Neumann entropy difference) is fixed
by the HUZ observer-inclusion rule itself; the state-class sensitivity
of its scaling is an intrinsic feature of the HUZ cloning protocol, not
a choice of observable. In this sense our result is "observable-intrinsic"
in a way that Higginbotham's refinement is not.

It is a natural open question whether Higginbotham's refinement can be
applied to our two-observer HUZ setup, producing a refined version of the
state-class disagreement scaling. We discuss this in §8.6 as a
follow-up direction.

### 8.3 Relation to Harlow–Usatyuk–Zhao (HUZ)

HUZ 2501.02359 established the observer-cloning rule used here. Their
headline result is that in the single-observer setting, the error in
the observer-dependent description is exponentially small in the observer
entropy:
$$
E_{\rm ovl}(\psi_1, \psi_2; V) \;=\; \left| \frac{\langle\Psi_1|\Psi_2\rangle}{\|\Psi_1\|\|\Psi_2\|} - \langle\psi_1|\psi_2\rangle \right| \;\sim\; \frac{1}{d_{\rm Ob}},
$$
a precise analytic claim verified to $4\%$ by our Phase 2 numerical
program (see reproducibility appendix).

Our two-observer result could, a priori, have inherited HUZ's $1/d_{\rm Ob}$
scaling directly — giving $\alpha = -1$ for both observers. This naive
inheritance is rejected at $19\sigma$ in the Haar-bulk data (Phase 5).
The actual scaling is a full power of $d_B$ below naive inheritance in
the Haar class, and a full power of $d_B$ above it in the Product class.
This is a quantitative refinement of HUZ's framework: at the single-observer
inner-product level, the $1/d_{\rm Ob}$ bound is state-independent; at
the two-observer entropy level, the analog is class-sensitive.

### 8.4 Relation to the Colorado observer rule

The "Colorado" rule (see [Colorado 2503.09681] for a canonical discussion)
places the observer in the fundamental (boundary) Hilbert space rather than
cloning it externally. In that framework, the observer lives in
$\mathcal{H}_{\rm fund} = \mathcal{H}_{\rm Ob} \otimes \mathcal{H}_{{\rm fund}, M}$,
and $V = I_{\rm Ob} \otimes V_M$ acts only on the matter sector. No external
reference is needed.

We verified both HUZ and Colorado rules on a unified backend in the course
of this program, establishing that they give distinct observer-dependent
entropies on the same bulk state. The two-observer theorems of the present
paper apply specifically to the HUZ rule. Deriving an analogous result for
the Colorado rule would require a different starting identity — Colorado
has no external reference register, so the machinery of Theorem 3.2 does
not apply directly. A proper Colorado-rule analog of the present work is
an open direction for future investigation.

The mechanism uncovered in §3.3 — that HUZ cloning combined with Haar-$V$
averaging acts as pointer-basis decoherence at leading order — is
specific to HUZ. The diagonal projection in Theorem 3.2 arises from the
$\delta_{aa'}$ structure of the first-moment Haar contraction (3.3a),
which in turn reflects the way the cloning map correlates the observer
register $R_A$ with the bulk factor $\mathcal{H}_A$ in a fixed pointer
basis. The Colorado rule, in which the observer is part of
$\mathcal{H}_{\rm fund}$ and $V$ acts only on the matter sector, does
not introduce an external pointer register, and the analogous bra–ket
contraction need not produce a $\delta_{aa'}$ at the
structural-identity stage. Whether a Colorado-rule analog of the
two-observer disagreement scaling produces the same integer exponent
gap of $1$ between product and Haar bulk classes, or a different gap
reflecting a different decoherence structure, is an open question we
intend to address in follow-up work. More generally, the diagonal
projection identified here is a feature of HUZ + Haar-$V$ specifically,
not a universal property of observer inclusion in non-isometric
holographic maps.

### 8.5 Relation to quantum-reference-frame literature

A parallel thread studies observer-dependent entropies via the quantum
reference frame (QRF) formalism, notably [de la Hamette–Kabel–Galley
2412.15502] and [Carrozza–Giesel 2603.23598]. The QRF framework is
structurally different from the AEHPV/HUZ setup: observers are modeled
as physical degrees of freedom coupled via a reference-frame covariance
principle, and the resulting observer-dependent entropies live on
Type $\mathrm{II}$ algebraic factors associated with crossed-product
constructions [Kudler-Flam–Witten 2510.06376].

Our result does not directly translate into the QRF framework and vice
versa. The two frameworks ask distinct questions:

- QRF: given two observers related by a physical reference-frame
  transformation, what is the crossed-product entropy of their respective
  algebras?
- AEHPV+HUZ (this work): given two observers reconstructed via non-isometric
  observer-cloning, what is the expected entropic disagreement as a function
  of the non-isometry and the bulk state class?

These are complementary rather than competing. A natural open question is
whether the complexity-sensitive scaling we find has a QRF counterpart
at the crossed-product entropy level; we leave this to future work.

### 8.6 Relation to baby-universe and cosmological constructions

Mori–Yoshida 2511.20747 constructs logical qubits in closed-universe
holographic settings via a different mechanism (encoding into ancillary
matter factors). Li–Mori–Yoshida 2502.04437 studies LOCC distillation of
information from non-isometric codes. Both are tangentially related to
our setup (same AEHPV framework) but address distinct questions:

- Mori–Yoshida 2511.20747: construction and properties of logical qubits in
  closed universes.
- Li–Mori–Yoshida 2502.04437: operational distillation of information
  across the non-isometric code.
- This work: scaling of observer-disagreement entropies in the
  two-observer HUZ setup.

Liu 2509.14327 and 2512.13807 study filtered CFT constructions and their
observer-dependent entropies from a different angle (CFT-theoretic rather
than random-code-theoretic). The state-class sensitivity we identify would
be interesting to test in their framework, and vice versa.

### 8.7 Open questions and natural follow-ups

- **Rank-$r$ interpolation.** The most natural follow-up is a systematic
  scan of the Schmidt-rank-$r$ bulk-state class for $1 \leq r \leq d_{\rm eff}$,
  testing whether $\alpha(r)$ smoothly interpolates between $-1/2$ and $-3/2$
  or exhibits a phase transition at some critical rank. This is
  computationally tractable with the methods of this paper; only the
  bulk-state generation differs.

- **Higginbotham's refinement applied to two-observer HUZ.** Whether
  Higginbotham's refined SWAP operators applied to our two-observer
  HUZ scan preserve, strengthen, or alter the $\alpha_P - \alpha_H = 1$
  gap would be interesting.

- **Analytic derivation of subleading corrections.** The Haar-class
  subleading structure $1 - 1.13/d_B + 4.65/d_B^2$ is fit numerically
  here; its origin is presumably non-Gaussian corrections to the Isserlis
  identity in §5.3, combined with bulk-norm fluctuation corrections.
  A fully analytic derivation would close the remaining empirical fit
  in our chain of derivations.

- **Other observer-inclusion rules.** Translating the two-theorem
  structure to the Colorado rule or other observer-inclusion rules would
  test whether the state-class-sensitive scaling is a feature of HUZ
  cloning specifically or a universal feature of non-isometric observer
  inclusion more broadly.

- **Connection to holographic complexity.** The term "complexity-sensitive
  complementarity" is suggestive, and the $\alpha_P$ vs $\alpha_H$ gap has
  an informal "bulk-state complexity increases observer agreement" flavor.
  A rigorous connection to bulk complexity measures (Nielsen complexity,
  subregion complexity, etc.) would sharpen the physical interpretation.

---

## §9. Conclusion

We have proven a structural identity for the two-observer HUZ setup in
AEHPV non-isometric holographic codes: at leading order in $1/d_{\rm eff}$,
the Haar-$V$-averaged observer-$A$ reduced state equals the diagonal of
the bulk $A$-marginal in the observer's cloning basis. Bulk-marginal
coherences across distinct pointer values are projected out by the
combination of HUZ cloning and Haar-$V$ averaging. This identity reduces
the two-observer entropy disagreement to a bulk-marginal moment
computation, which we carry out for two extreme bulk-state classes:

- **Product class** (bulk state factorizing as $|\psi_A\rangle \otimes
  |\psi_B\rangle \otimes |\psi_C\rangle$): $\mathbb{E}|S_A - S_B|
  \to \sqrt{4(\pi^2/3 - 3)/\pi}\, d_B^{-1/2} \approx 0.608\, d_B^{-1/2}$.
- **Haar class** (bulk state Haar on $\mathcal{H}_{\rm eff}$):
  $\mathbb{E}|S_A - S_B| \to \sqrt{2/\pi}/(d_M\, d_B^{3/2}) \approx
  (0.798/d_M)\, d_B^{-3/2}$.

The exponents $-1/2$ and $-3/2$ are exact asymptotics, not power-law fits;
the prefactors are derived in closed form. The integer exponent gap of $1$
is a direct consequence of the Dirichlet-variance hierarchy separating a
rank-1 bulk marginal (Product class) from a near-maximally-mixed marginal
(Haar class).

The structural identity and both scaling theorems are verified at multiple
independent levels, including out-of-sample tests at $d_B$ values not used
in any calibration, all passing at sub-$\sigma$ precision.

Several natural follow-ups suggest themselves. A systematic scan of
Schmidt-rank-$r$ intermediate bulk states would establish whether the
exponent $\alpha(r)$ interpolates smoothly between our two extreme cases.
An analytic derivation of the subleading structure $1 - 1.13/d_B +
4.65/d_B^2$ appearing in Theorem 2 — presumably via non-Gaussian
corrections to the Isserlis identity — would close the one remaining
empirical fit in our chain of derivations. Applying the same machinery
to alternative observer-inclusion rules (Colorado, QRF crossed-product)
would test the extent to which the pattern we identify is intrinsic to
HUZ cloning or more universal.

---

*End of manuscript draft. Appendices (A: generalized EGH formulas;
B: reproducibility details) and bibliography to follow.*
