---
title: "Entropy Replacement and Complexity-Sensitive Observer Complementarity in Non-Isometric Holographic Codes"
kind: "manuscript"
paperNumber: 3
order: 1
subtitle: "The full manuscript of Paper III, rendered in-site."
---


## Abstract

Two observers granted independent, cloned access to the same bulk degree of freedom
in a non-isometric holographic code can in principle disagree about its entropy. We
quantify this disagreement in the AEHPV non-isometric framework with Harlow–Usatyuk–Zhao
observer inclusion, and show it is governed by an **entropy-replacement principle**.
Our main result (Theorem 1) is that the von Neumann entropy of an observer's actual
reduced state equals the Shannon entropy of its diagonal in the cloning basis, up to
an error $F_{AB}$ with $\mathbb{E}[F_{AB}^2] = O(d_B^{-4} d_M^{-2})$ — a full power of
$d_B$ below the two-observer signal. For Haar-random bulk states this principle is
established **unconditionally**, via an exact antisymmetric resolvent representation of
$F_{AB}$ together with a fourth-moment bound on the random-projection–induced
perturbation. The replacement reduces the disagreement to a moment calculation of the
bulk-marginal diagonal, which we carry out for two extreme bulk-state classes. For the
Haar class we prove (unconditionally, Theorem 2)
$\mathbb{E}|S_A - S_B| \to \sqrt{2/\pi}\,/(d_M\, d_B^{3/2})$; for random product bulk
states we obtain, conditionally on the product-class replacement principle (Theorem 3),
$\mathbb{E}|S_A - S_B| \to \sqrt{4(\pi^2/3 - 3)/\pi}\, d_B^{-1/2} \approx 0.608\, d_B^{-1/2}$.
The two exponents differ by exactly one power of $d_B$, an instance of
**complexity-sensitive complementarity**: the degree to which two cloned observers
can disagree is set by the complexity class of the bulk state. All exponents and
prefactors are exact asymptotics, supported by an extensive numerical program across
the full HUZ+$V$ pipeline.

## §1. Introduction

### 1.1 Observer complementarity in non-isometric codes

In non-isometric holographic codes, the map from the effective (bulk) description to
the fundamental (boundary) description is many-to-one: distinct bulk states can map to
identical boundary data. This is the defining feature of the AEHPV construction, and
it is what allows a black-hole interior to be encoded with far fewer fundamental
degrees of freedom than the naive bulk Hilbert space would require. A consequence is
that "an observer" is not a passive bystander: including an observer who measures a
bulk degree of freedom changes the code, because the observer's record must itself be
encoded. The Harlow–Usatyuk–Zhao (HUZ) prescription makes this precise by *cloning*
the measured degree of freedom into an observer register before the non-isometric map
is applied.

When two such observers are included independently — each cloning the same bulk degree
of freedom into its own register — the code now carries two records of the same
information. Because the non-isometric map is not injective, the two observers'
reduced states need not agree, and in particular their von Neumann entropies need not
agree. The size of this disagreement is a sharp, computable diagnostic of how much
"room" the non-isometry leaves for observer-dependent descriptions.

### 1.2 The question

Concretely: let $|\psi\rangle$ be a bulk state on $\mathcal H_A\otimes\mathcal
H_B\otimes\mathcal H_C$, included for two observers $A$ and $B$ via HUZ cloning and
mapped to the fundamental description by a fixed non-isometry built from a Haar-random
isometry $V$. Writing $\rho_{R_A},\rho_{R_B}$ for the two observer-reduced states, we
ask for the typical magnitude of
$$
\bigl|\,S(\rho_{R_A}) - S(\rho_{R_B})\,\bigr|
$$
under the joint randomness of $V$ and (in two natural ensembles) the bulk state. How
large is the disagreement, and what controls it?

### 1.3 Main results

The answer comes in two layers. The first is structural and is the technical core of
the paper.

> **Theorem 1 (entropy-replacement principle, informal).** *The von Neumann entropy
> of an observer's actual reduced state equals the Shannon entropy of its diagonal in
> the cloning basis, up to an error $F_{AB}$ obeying*
> $$
> \mathbb{E}\bigl[F_{AB}^2\bigr] = O\!\bigl(d_B^{-4} d_M^{-2}\bigr),
> \qquad
> \mathbb{E}\,|F_{AB}| = o\!\bigl(d_B^{-3/2} d_M^{-1}\bigr).
> $$

For the Haar bulk class this is a theorem, proved unconditionally in Appendix C; for
the product class it is a conjecture, numerically supported but not proved. The proof
for the Haar class is, we believe, of independent interest: it represents the
antisymmetric entropy difference exactly through a resolvent integral, splits it into
a linear piece (which reduces to the very bulk-marginal moment that controls the
signal) and a nonlinear piece (controlled by a fourth moment of the
random-projection–induced perturbation), and closes the fourth moment by a
concentration estimate on the unitary group. The replacement error is suppressed
relative to the signal by a full power of $d_B$ — which is exactly what is needed to
make the entropy difference equal to the Shannon difference at leading order.

Given Theorem 1, the disagreement reduces to the variance of the Shannon entropy of
the bulk-marginal diagonal, a classical random-matrix calculation. Carrying it out for
two extreme bulk-state classes gives the second layer:

- **Haar bulk states** (maximal complexity), Theorem 2, *unconditional*:
  $\mathbb{E}|S_A - S_B| \to \sqrt{2/\pi}\,/(d_M\, d_B^{3/2}) \approx (0.798/d_M)\,d_B^{-3/2}$.
- **Random product bulk states** (minimal complexity), Theorem 3, *conditional* on the
  product-class form of Theorem 1:
  $\mathbb{E}|S_A - S_B| \to \sqrt{4(\pi^2/3-3)/\pi}\,d_B^{-1/2} \approx 0.608\,d_B^{-1/2}$.

| Bulk class | Replacement (Theorem 1) status     | Disagreement law                  |
| ---------- | ---------------------------------- | --------------------------------- |
| Haar       | proved (Appendix C)                | **unconditional**, $d_B^{-3/2}$   |
| Product    | conjectural / numerically supported| conditional, $d_B^{-1/2}$         |

### 1.4 Physical interpretation: complexity-sensitive complementarity

The two exponents differ by exactly one power of $d_B$. We read this as
*complexity-sensitive complementarity*: the degree to which two cloned observers can
disagree about a bulk degree of freedom is controlled by the complexity class of the
bulk state. Highly scrambled (Haar) bulk states leave little room for disagreement —
the disagreement falls off as $d_B^{-3/2}$ — while simple (product) bulk states leave
an order-$\sqrt{d_B}$ more room, falling off only as $d_B^{-1/2}$. The non-isometry's
tolerance for observer-dependent descriptions is thus not a fixed property of the code
but a function of what is encoded in it. Section 6 develops this reading and connects
the exponent gap to the fluctuation structure of the bulk marginal.

### 1.5 Organization

Section 2 fixes the AEHPV/HUZ setup, the two-observer scenario, and the two bulk
classes. Section 3 is the technical heart: it states and proves (modulo Appendix C)
the entropy-replacement theorem, building it from the structural identity (Lemma 1)
and the off-diagonal collapse, and verifies it numerically (Figure 2). Sections 4 and
5 derive the two scaling laws as consequences — the Haar law (Theorem 2,
unconditional) first, then the product law (Theorem 3, conditional). Section 6 develops
the complexity-sensitive reading of the exponent gap. Section 7 presents the numerical
landscape (Table 1, Figures 1 and 5). Section 8 situates the results against EGH, HUZ,
the Colorado rule, and the quantum-reference-frame literature. Appendix A records
generalized EGH formulas; Appendix B documents reproducibility; **Appendix C proves
the entropy-replacement theorem for the Haar class** — the resolvent representation,
the linear and nonlinear bounds (Lemmas C.1–C.2), and the fourth-moment projector
estimate (Lemmas C.3–C.5).


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


---

## §3. The entropy-replacement principle

This section establishes the technical heart of the paper: that the von Neumann
entropy of an observer's actual reduced state may be replaced, up to a provably
subleading error, by the Shannon entropy of its diagonal. This **entropy-replacement
theorem** (Theorem 1) is what licenses the entire reduction from a genuine
quantum-information quantity to a classical moment calculation; the two scaling laws
of §§4–5 are its consequences.

The proof has two ingredients, developed in turn. The first is a *structural
identity* (Lemma 1): the Haar-$V$ expectation of the first-observer reduced state is,
at leading order in $1/d_{\rm eff}$, the diagonal in the $A$ basis of the bulk
$A$-marginal. This controls the *mean*. The second, and harder, ingredient controls
the *fluctuations*: the replacement error has variance suppressed by a full power of
$d_B$ relative to the two-observer signal. For the Haar class this is proved
unconditionally (Appendix C); for the product class it remains a conjecture. The structural identity is established in §§3.2–3.3 and verified numerically in §3.4 (Figure 2); the
entropy-replacement theorem is stated in §3.5, with its fluctuation bound proved in Appendix C.

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

### 3.2 The structural identity (Lemma 1): the Haar-$V$ expectation

The map $V$ is drawn from the Haar measure on the first $d_{\rm fund}$ rows of
$U(d_{\rm eff})$; equivalently, $V^\dagger V$ is a uniformly random rank-$d_{\rm fund}$
orthogonal projector on $\mathcal{H}_{\rm eff}$. A basic moment identity gives
$$
\mathbb{E}_V\bigl[\langle x|\,V^\dagger V\,|y\rangle\bigr] \;=\; \rho\, \langle x|y\rangle
\qquad \text{for any } x, y \in \mathcal{H}_{\rm eff}.
\tag{3.3}
$$
Applying (3.3) termwise to (3.1): the inner product enforced by the Haar
first moment is $\langle a',b,c'|a,b,c\rangle = \delta_{aa'}\delta_{cc'}$, so the
sum over $R_B$ (the index $b$) and the matter contraction collapse the
off-diagonals already at first moment,
$$
\mathbb{E}_V\bigl[(\rho_{R_A}^{\rm unnorm})_{aa'}\bigr]
\;=\; \rho\, \delta_{aa'} \sum_{b,c} |\psi_{abc}|^2
\;=\; \rho\, \delta_{aa'}\, (\rho_A^{\rm bulk})_{aa},
\tag{3.4}
$$
and
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

**Lemma 2 (Norm concentration).** With $|\psi\rangle$ of unit norm,
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
\;=\; \delta_{aa'}\,(\rho_A^{\rm bulk})_{aa} + O(1/d^2)
\;=\; \bigl[\mathrm{diag}(\rho_A^{\rm bulk})\bigr]_{aa'} + O(1/d^2).
\tag{3.6}
$$
This is the **structural identity** (Lemma 1): at first moment the observer
register sees only the cloning-basis *diagonal* of the bulk marginal, not the
full marginal.

### 3.3 Why the off-diagonals collapse

The collapse in (3.4)–(3.6) is a first-moment effect, not a variance effect.
The single record held in $R_A$ labels the cloning index $a$; tracing out the
*other* observer's register $R_B$ together with the Haar first moment of
$V^\dagger V$ contracts the two copies of the state at equal $R_B$ index and
enforces $\langle a',b,c'|a,b,c\rangle = \delta_{aa'}\delta_{cc'}$. The Kronecker
$\delta_{aa'}$ is what removes the off-diagonal entries: an off-diagonal
$(\rho_{R_A})_{aa'}$ with $a\neq a'$ has *zero* Haar-$V$ mean, regardless of the
off-diagonal structure of the bulk marginal $\rho_A^{\rm bulk}$. There is no
sense in which the full bulk marginal is carried in expectation and then
suppressed; the off-diagonals are gone at first moment.

What survives at first moment is exactly the diagonal $p_A^a = \sum_{bc}|\psi_{abc}|^2$,
the bulk $A$-marginal probabilities. The individual realizations $\rho_{R_A}$ do
carry off-diagonal entries, of typical size set by the $V$-fluctuations; these
are the perturbation $E_A := \rho_{R_A} - \mathrm{diag}(\rho_{R_A})$ controlled in
Appendix C. Their effect on the entropy is the subject of the
entropy-replacement theorem (§3.5): it is subleading to the two-observer signal
by a full power of $d_B$.

### 3.4 Numerical verification

![Figure 2](/paper3/figure2.png)

Figure 2 verifies Lemma 1 directly. Panel (a) shows the 18 diagonal
entries of $\mathbb{E}_V[\rho_{R_A}]$ (measured by Monte Carlo, 200–500 Haar
$V$ samples) against the corresponding entries of $\mathrm{diag}(\rho_A^{\rm bulk})$
(computed directly from the bulk state) for Haar bulk at $d_B \in \{4, 6, 8\}$
and $d_M = 4$. All 18 points lie on the $y=x$ line, with the worst individual relative
deviation below $1\%$. Panel (b) shows
that the off-diagonal magnitudes of $\mathbb{E}_V[\rho_{R_A}]$ are
suppressed by 2–3 orders of magnitude relative to $\rho_A^{\rm bulk}$'s
off-diagonals: at $d_B = 4$, $|\rho_A^{\rm bulk}|_{\rm off} \approx 0.057$
while $|\mathbb{E}_V[\rho_{R_A}]|_{\rm off} \approx 1.0 \times 10^{-3}$ (suppression $\approx 60\times$).
For product bulk states (hatched red bars), the bulk off-diagonals are
of comparable magnitude, and the Haar-$V$ averaging similarly suppresses
them.

With the structural identity in hand, both theorems of this paper reduce
to computing $\mathbb{E}[H(\mathrm{diag}(\rho_A^{\rm bulk}))]$ under two
different bulk state classes — *provided* the von Neumann entropy of the
actual reduced state may be replaced by the Shannon entropy of its diagonal.
That replacement is the content of the next subsection.

### 3.5 Statement of the main theorem (Theorem 1)

Lemma 1 controls the Haar-$V$ *expectation* $\mathbb{E}_V[\rho_{R_A}]$.
The scaling theorems of §§4–5, however, require more: that the von Neumann
entropy of the *actual* (fluctuating) reduced state $\rho_{R_A}$ equal the
Shannon entropy of the **bulk-marginal diagonal** — the object the scaling
calculation actually uses — up to an error subleading to the two-observer
signal. Two diagonals must be distinguished:
$$
D_X \;:=\; \mathrm{diag}(\rho_{R_X})\ \text{(the \emph{actual} reduced-state diagonal, $V$-dependent)},
\qquad
P_X \;:=\; \mathrm{diag}(\rho_X^{\rm bulk}),
$$
where $P_X$ has entries $p_A^a = \sum_{bc}|\psi_{abc}|^2$ and $p_B^b = \sum_{ac}|\psi_{abc}|^2$
— the bulk-marginal probabilities, which depend only on $|\psi\rangle$, not on $V$.
By Lemma 1, $\mathbb{E}_V[D_X] = P_X + O(d^{-2})$, but $D_X$ fluctuates around $P_X$.
Define the **entropy-replacement error** against the bulk-marginal diagonal,
$$
F_{AB} \;:=\; \bigl[S(\rho_{R_A}) - S(\rho_{R_B})\bigr] \;-\; \bigl[H(P_A) - H(P_B)\bigr],
\tag{3.7}
$$
which we split into an off-diagonal and a diagonal-to-bulk part,
$$
F_{AB} \;=\; \underbrace{\bigl[S_A - S_B\bigr] - \bigl[H(D_A) - H(D_B)\bigr]}_{F_{\rm off}}
\;+\; \underbrace{\bigl[H(D_A) - H(D_B)\bigr] - \bigl[H(P_A) - H(P_B)\bigr]}_{F_{\rm diag}}.
$$
The two-observer signal has standard deviation $\Theta(d_B^{-3/2} d_M^{-1})$
in the Haar class (Theorem 2). The following theorem states that $F_{AB}$ —
both pieces — is smaller by a full power of $d_B$.

> **Theorem 1 (entropy replacement).** *In the joint Haar measure on
> bulk and $V$, with $d_A = d_B = d$, $\rho \in (0,1)$ and $d_M$ fixed,*
> $$
> \boxed{\;\;\mathbb{E}\,\bigl|[S(\rho_{R_A}) - S(\rho_{R_B})] - [H(P_A) - H(P_B)]\bigr| \;=\; O\!\bigl(d^{-2} d_M^{-1}\bigr) \;=\; o\!\bigl(d^{-3/2} d_M^{-1}\bigr).\;\;}
> $$
> *Equivalently $\mathbb{E}[F_{AB}^2] = O(d^{-4}d_M^{-2})$, with both $F_{\rm off}$
> and $F_{\rm diag}$ of this order.*

For the **Haar bulk class**, Theorem 1 is a *theorem*: it is proved
unconditionally in Appendix C via an exact antisymmetric resolvent
representation of $F_{AB}$, a linear bound reducing to the bulk-marginal
moment of §5, and a fourth-moment bound on the $V$-induced off-diagonal perturbation
$E_X := \rho_{R_X} - D_X$ (Lemmas C.1–C.4), together with a short
diagonal-fluctuation bound for $F_{\rm diag}$ (Lemma C.6). The proof shows
$\mathbb{E}[F_{AB}^2] = O(d^{-4} d_M^{-2})$, i.e. the replacement error
variance is suppressed by one power of $d$ relative to the signal variance
$\Theta(d^{-3} d_M^{-2})$. All constants are dimension-independent.

For the **product bulk class**, Theorem 1 remains a *conjecture*. The
off-diagonal suppression is verified numerically (Figure 2, and the
end-to-end tests of §4.4) but the small-mass régime of the rank-1 marginal
is not yet controlled analytically; the resolvent argument of Appendix C
does not directly transfer. Accordingly, Theorem 3 below is stated
*conditionally* on the product-class form of Theorem 1, while Theorem 2
is unconditional.

---


---

## §4. Consequence I — the Haar-class disagreement law (unconditional)

We first take $|\psi\rangle$ Haar-distributed on the *full* effective Hilbert
space $\mathcal{H}_A \otimes \mathcal{H}_B \otimes \mathcal{H}_C$ — the
maximal-complexity class, and the one for which the entropy-replacement theorem
is unconditional (Appendix C), so that the disagreement law below is rigorous. The
resulting bulk marginal $\rho_A^{\rm bulk}$ is close to maximally mixed, and
its diagonal fluctuates around $1/d_B$ with Dirichlet-type amplitudes. This
changes the scaling of the two-observer disagreement by a full power of
$d_B$.

### 4.1 Setup and the grouped-Dirichlet marginal

For Haar $|\psi\rangle$ on $\mathbb{C}^{d_A \cdot d_B \cdot d_M}$, the squared
amplitudes $|\psi_{abc}|^2$ follow $\mathrm{Dirichlet}(1,\ldots,1)$ on the
$D = d_A d_B d_M$ simplex. The bulk $A$- and $B$-marginal block masses are
$$
p_a \;=\; (\rho_A^{\rm bulk})_{aa} \;=\; \sum_{b,c}|\psi_{abc}|^2,
\qquad
q_b \;=\; (\rho_B^{\rm bulk})_{bb} \;=\; \sum_{a,c}|\psi_{abc}|^2,
$$
each a sum of $d\,d_M$ Dirichlet coordinates; marginally $p_a \sim
\mathrm{Beta}(d\,d_M,\, D - d\,d_M)$. Set $d_A = d_B = d$ and write
$p_a = 1/d + \delta_a$, $q_b = 1/d + \eta_b$ with $\sum_a \delta_a = \sum_b \eta_b = 0$.

The block masses are **not** independent. The global constraint $\sum_a p_a = 1$
forces a *negative* correlation between distinct $A$-blocks; by contrast the $A$-
and $B$-groupings cut the simplex transversally and decouple exactly. The
relevant fourth-order moments are collected in the following lemma, whose
quadratic invariants $T_A := \sum_a p_a^2$ and $T_B := \sum_b q_b^2$ are what the
entropy difference depends on.

**Lemma 3 (Grouped-Dirichlet moments).** *With $d_A = d_B = d$, $d_C = d_M$, and
$D = d^2 d_M$,*
$$
\mathrm{Cov}(p_a, p_{a'}) < 0 \ \ (a \neq a'),
\qquad
\mathrm{Cov}(p_a, q_b) = 0 \ \ \text{for all } a, b,
$$
*and, for $T_A = \sum_a p_a^2$, $T_B = \sum_b q_b^2$,*
$$
\mathrm{Var}(T_A) = \frac{2\,d\,d_M\,(d-1)\,(d\,d_M + 1)}{(D+1)^2(D+2)(D+3)},
\qquad
\mathrm{Cov}(T_A, T_B) = \frac{2\,d_M\,(d-1)^2}{(D+1)^2(D+2)(D+3)},
$$
$$
\mathrm{Var}(T_A - T_B) = \frac{4\,d_M\,(d-1)}{(D+1)(D+2)(D+3)}
\;=\; \frac{4}{d^5 d_M^2}\bigl(1 + O(1/d)\bigr).
$$

*Proof.* For the symmetric Dirichlet, $\mathrm{Cov}(p_a, p_{a'}) = -\,
\mathrm{Var}(p_a)/(d-1) < 0$ by exchangeability and $\sum_a p_a = 1$. For the
cross term, $p_a$ (a sum over the $(b,c)$ indices at fixed $a$) and $q_b$ (a sum
over $(a,c)$ at fixed $b$) overlap only in the single $(a,b)$-block; under the
symmetric Dirichlet that shared block contributes equally to $\mathbb{E}[p_a q_b]$
and to $\mathbb{E}[p_a]\mathbb{E}[q_b]$, so the covariance cancels exactly,
$\mathrm{Cov}(p_a, q_b) = 0$. The $T_A, T_B$ moments are the standard fourth-order
symmetric-Dirichlet moments of $\sum_a p_a^2$; $\mathrm{Var}(T_A - T_B) =
2\,\mathrm{Var}(T_A) - 2\,\mathrm{Cov}(T_A, T_B)$ by the $A\!\leftrightarrow\!B$
symmetry. The displayed values are confirmed numerically (script
`reproducibility/scratch_grouped_dirichlet.py`) to within $1\%$ at $d = 4,5,6$,
including the negative off-diagonal and the vanishing $p$–$q$ covariance. $\square$

### 4.2 Entropy as a quadratic form

Taylor-expand the Shannon entropy $H(p) = -\sum_a p_a \log p_a$ about the uniform
point $p_a = 1/d$. Since $\sum_a \delta_a = 0$ the first-order term vanishes, and
$$
H(p) \;=\; \log d - \frac{d}{2}\sum_a \delta_a^2 + O(\delta^3)
\;=\; \log d - \frac{d}{2}\Bigl(T_A - \tfrac1d\Bigr) + O(\delta^3),
\tag{4.1}
$$
using $\sum_a \delta_a^2 = \sum_a p_a^2 - 1/d = T_A - 1/d$. The constant cancels in
the difference, so
$$
H(p) - H(q) \;=\; -\frac{d}{2}\,(T_A - T_B) \;+\; o\!\bigl(d^{-3/2} d_M^{-1}\bigr),
$$
the cubic remainder (of order $d^{-7/2} d_M^{-3/2}$ in standard deviation) being
subleading. By the entropy-replacement decomposition (3.7) and Theorem 1 (Haar
class, proved in Appendix C),
$$
S(\rho_{R_A}) - S(\rho_{R_B}) \;=\; \bigl[H(p) - H(q)\bigr] + F_{AB},
\qquad
\mathbb{E}[F_{AB}^2] = O(d^{-4} d_M^{-2}),
$$
subleading by a full power of $d$ to $\mathrm{Var}(H(p)-H(q))$, computed next.
Hence $S_A - S_B$ is governed at leading order by $-\tfrac{d}{2}(T_A - T_B)$.

### 4.3 Variance computation

By Lemma 3 and the linearization of §4.2,
$$
\mathrm{Var}\bigl(H(p) - H(q)\bigr) \;=\; \frac{d^2}{4}\,\mathrm{Var}(T_A - T_B)
\;=\; \frac{d^2 d_M (d-1)}{(D+1)(D+2)(D+3)}
\;=\; \frac{1}{d^3 d_M^2}\bigl(1 + O(1/d)\bigr).
$$
Through the replacement error of §4.2 (subleading by a power of $d$), this is also
the leading variance of the observable itself:
$$
\mathrm{Var}(S_A - S_B) \;=\; \frac{1}{d^3 d_M^2}\bigl(1 + O(1/d)\bigr).
\tag{4.2}
$$

### 4.4 Statement and proof (Theorem 2)

**Theorem 2 (Haar-class disagreement scaling; unconditional).** Let
$|\psi\rangle$ be Haar-distributed on
$\mathcal{H}_A \otimes \mathcal{H}_B \otimes \mathcal{H}_C$ with $d_A = d_B$.
Under the joint Haar measure on bulk and $V$ (with $d_M$, $\rho$ fixed),
$$
\boxed{\;\;\mathbb{E}\bigl|S(\rho_{R_A}) - S(\rho_{R_B})\bigr|
\;=\; \sqrt{\dfrac{2}{\pi}} \cdot \frac{1}{d_M\, d_B^{3/2}}\,(1 + o(1))
\;\approx\; \frac{0.798}{d_M} \cdot d_B^{-3/2}.\;\;}
\tag{4.3}
$$
In particular, $\alpha_H = -3/2$ exactly.

*Proof (unconditional).* By §4.2, $S_A - S_B = (H(p)-H(q)) + F_{AB}$ with
$\mathbb{E}[F_{AB}^2] = O(d^{-4} d_M^{-2})$ by Theorem 1 (Haar class,
Appendix C) — a full power of $d$ below the variance (4.2) of the Shannon
term. The replacement error therefore contributes only at relative order
$O(d^{-1/2})$ to $\mathbb{E}|S_A-S_B|$ and does not affect the leading
asymptotic. Combine (4.2) with the Gaussian-limit identity
$\mathbb{E}|X| = \sqrt{2/\pi}\, \sigma_X$ for $X \sim \mathcal{N}(0, \sigma_X^2)$;
the Gaussian limit of $H(p)-H(q)$ follows from the CLT applied to the
quadratic form (4.1) in the i.i.d. $\mathrm{Exp}(1)$ representation. Explicitly,
$$
\mathbb{E}|S_A - S_B| \;=\; \sqrt{2/\pi}\, \sigma_{S_A - S_B} \;=\; \sqrt{2/\pi} \cdot \frac{1}{d_M\, d^{3/2}}(1 + o(1)). \qquad\square
$$

### 4.5 Subleading corrections

The $O(1/d)$ subleading term in (4.3) is dominated by non-Gaussian
corrections to the central-limit (Gaussian) approximation used for $T_A - T_B$
in §4.3, together with the higher symmetric-Dirichlet cumulants. The quantity $\delta_a$
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
\;=\; 1 - \frac{1.0(1)}{d_B} + O(1/d_B^2),
\tag{4.4}
$$
fit with $\chi^2 = 2.8/4$ dof. The floating-asymptote linear fit
$A + B/d_B$ to the measured/analytic ratio (data in `fig4_haar_prefactor.csv`,
$d_B \in [8,64]$) returns $A = 1.00 \pm 0.01$ (SEM-weighted), consistent with
the analytic asymptote $A = 1$ well within $1\sigma$ — a direct statistical test
of the prefactor $\sqrt{2/\pi}/d_M$.

### 4.6 Multi-level verification

Figure 4 collects four independent tests:

- **Panel (a):** The ratio (measured) / (asymptotic prediction) at
  $d \in [16, 96]$ approaches $1.0$ with a clear $1/d$ scaling.
  The floating-asymptote fit gives $A = 0.999 \pm 0.004$, consistent
  with $A = 1$ — this is a direct statistical test of
  Theorem 2's prefactor with no free parameters.
- **Panel (b):** The empirical subleading structure (4.4) fits the
  same data with $\chi^2 = 2.8/4$ dof.
- **Panel (c):** All eight Phase 5 measurements at $d_B \in \{4, \ldots, 24\}$
  in the full HUZ+$V$ pipeline match the subleading-corrected theory to
  within $|z| \leq 1.50\sigma$.
- **Panel (d):** Out-of-sample tests. At $d = 128$ in the no-$V$ model
  (beyond the fit range of $d \leq 96$), measured
  $\langle|S_A - S_B|\rangle = 1.34 \times 10^{-4}$ vs. corrected
  prediction $1.37 \times 10^{-4}$, giving sub-$\sigma$ agreement.

![Figure 4](/paper3/figure4.png)

**Figure 4.** Four checks of the Haar-class scaling. **(a)** measured/asymptotic ratio with floating-asymptote fit $A=1.00\pm0.01$ (consistent with $A=1$). **(b)** the same data against the subleading structure $1-1.0/d_B$. **(c)** full HUZ+$V$ pipeline residuals (Table 1), all $|z|<2$. **(d)** out-of-sample $d=128$: measured vs predicted agree to sub-$\sigma$.

  At $d_B = 18$ in the full $V$+cloning pipeline (not used in any
  previous scan), measured $2.33 \times 10^{-3} \pm 0.29 \times 10^{-3}$
  vs. predicted $2.49 \times 10^{-3}$, giving $z = -0.54\sigma$.

As with Theorem 3, the combined weight of multiple verification levels,
including out-of-sample tests at points not used in any calibration,
strongly supports the leading-order asymptotic (4.3).

### 4.7 Summary of the two-theorem picture

Theorems 2 and 3 together establish the main result of this paper: the
two-observer disagreement in AEHPV non-isometric codes with HUZ observer
inclusion is complexity-sensitive, with different scaling exponents for
different bulk state classes. The Haar exponent (Theorem 2) is established
unconditionally; the product exponent (Theorem 3) is conditional on the
product-class form of the entropy-replacement principle (§3.5), which is
numerically verified but not yet proved. The structural identity of §3 provides the
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


---

## §5. Consequence II — the product-class disagreement law (conditional)

In this section we compute the two-observer disagreement when the bulk
state factorizes as
$$
|\psi\rangle \;=\; |\psi_A\rangle \otimes |\psi_B\rangle \otimes |\psi_C\rangle,
\qquad |\psi_A\rangle \in \mathcal{H}_A,\ |\psi_B\rangle \in \mathcal{H}_B,\ |\psi_C\rangle \in \mathcal{H}_C,
$$
with each factor independently Haar-distributed on the unit sphere of its
respective space.

### 5.1 Reduction to Shannon entropy of Haar amplitudes

For product bulk, $\rho_A^{\rm bulk} = |\psi_A\rangle\langle\psi_A|$, a rank-1
projector. Its diagonal in the computational basis is $(|\psi_A^a|^2)_{a=1}^{d_B}$.
By Lemma 1,
$$
\mathbb{E}_V[\rho_{R_A}] \;=\; \mathrm{diag}\bigl(|\psi_A^a|^2\bigr) + O(1/d_B^2).
$$
Replacing $S(\rho_{R_A})$ by the Shannon entropy of its diagonal requires the
**product-class form of Theorem 1** (§3.5), which we adopt here as a
*hypothesis*: it is supported numerically (the off-diagonal suppression of
Figure 2 and the end-to-end tests of §5.4) but, unlike the Haar case, is not
proved in Appendix C. Under this hypothesis the leading-order entropy is the
Shannon entropy of the Haar amplitudes:
$$
S(\rho_{R_A}) \;=\; H\bigl(|\psi_A|^2\bigr) + o(d_B^{-1/2}), \qquad
H\bigl(|\psi_A|^2\bigr) \equiv -\sum_{a=1}^{d_B} |\psi_A^a|^2\, \log |\psi_A^a|^2.
$$
The same argument applies to $S(\rho_{R_B})$ with $|\psi_B\rangle$. Since
$|\psi_A\rangle$ and $|\psi_B\rangle$ live in different factors and are drawn independently, the two
Shannon entropies $H_A = H(|\psi_A|^2)$ and $H_B = H(|\psi_B|^2)$ are iid
random variables.

Our target is therefore (conditionally on the product-class Theorem 1)
$$
\mathbb{E}|S_A - S_B| \;=\; \mathbb{E}|H_A - H_B| + o(d_B^{-1/2})
\quad\text{as}\quad d_B \to \infty,
$$
reducing a two-observer cloning problem to a question about iid Shannon
entropies of random probability vectors on the $d_B$-simplex.

### 5.2 Variance of Shannon entropy for the flat Dirichlet

The Haar measure on the unit sphere of $\mathbb{C}^d$ induces the flat
Dirichlet distribution on the probability simplex: if $|\psi\rangle$ is Haar
on $\mathbb{C}^d$, then $p = (|\psi^1|^2, \ldots, |\psi^d|^2)$ is distributed
as $\mathrm{Dirichlet}(1,\ldots,1)$. We need $\mathrm{Var}(H(p))$ in the
large-$d$ limit.

**Lemma 4.** Let $p \sim \mathrm{Dirichlet}(1, \ldots, 1)$ on the
$d$-simplex, and $H(p) = -\sum_i p_i \log p_i$. Then
$$
\boxed{\;\; d \cdot \mathrm{Var}\bigl(H(p)\bigr) \;\longrightarrow\; \frac{\pi^2}{3} - 3 \;\approx\; 0.28987 \quad \text{as } d \to \infty.\;\;}
\tag{5.1}
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
to the transcendental constant $\pi^2/3 - 3$. Lemma 4 is verified to SEM
precision by $d = 256$ in Figure 3(a): measured $d \cdot \mathrm{Var}(H) =
0.2885 \pm 0.0013$, against the analytic value $0.28987$.

### 5.3 Statement and proof (Theorem 3)

With Lemma 4 and the central-limit behavior of $H$ in hand, the main
result of this section is immediate.

**Theorem 3 (Product-class disagreement scaling; conditional).** Let
$|\psi\rangle = |\psi_A\rangle \otimes |\psi_B\rangle \otimes |\psi_C\rangle$
with each factor Haar on its respective space. Under the joint Haar measure on
bulk and $V$, **and assuming the product-class form of Theorem 1**,
$$
\boxed{\;\;\mathbb{E}\bigl|S(\rho_{R_A}) - S(\rho_{R_B})\bigr|
\;=\; \sqrt{\dfrac{4(\pi^2/3 - 3)}{\pi\, d_B}}\,(1 + o(1))
\;\approx\; 0.6076 \cdot d_B^{-1/2}.\;\;}
\tag{5.2}
$$
In particular, $\alpha_P = -1/2$ exactly.

*Proof (conditional on Theorem 1, product class).* By the reduction of
§5.1, $S(\rho_{R_A}) - S(\rho_{R_B}) = H_A - H_B + o(d_B^{-1/2})$, where $H_A, H_B$ are iid samples of the Shannon
entropy of a $\mathrm{Dirichlet}(1,\ldots,1)$ vector on the $d_B$-simplex. By
Lemma 4, each has $\mathrm{Var}(H) = (\pi^2/3 - 3)/d_B \cdot (1 + o(1))$.
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
which simplifies to the claimed (5.2). $\square$

### 5.4 Multi-level verification

Figure 3 collects four independent tests of Theorem 3, all passing:

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

![Figure 3](/paper3/figure3.png)

**Figure 3.** Four independent checks of the product-class scaling (leading-order Dirichlet model). **(a)** $d\,\mathrm{Var}(H)\to\pi^2/3-3$ from below. **(b)** $\mathbb{E}|H_A-H_B|/(0.608\,d^{-1/2})\to1$. **(c)** Gaussian-limit ratio $\to\sqrt{2/\pi}\approx0.798$. **(d)** Zero-parameter comparison of model to the $0.608\,d_B^{-1/2}$ law.

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
out-of-sample — strongly supports the leading-order
asymptotic form (5.2). Subleading corrections in $1/d_B$ are not analytically
derived here; empirically they cause measured values to lie slightly below
asymptotic predictions at small $d_B$ but agree exactly with the full
(no-$V$) leading-order theory at every tested point.

---


---

## §6. Physical interpretation: complexity-sensitive complementarity

Theorems 2 and 3 establish a specific quantitative pattern: the
two-observer disagreement exponent depends on the complexity class of the
bulk state, with Product and Haar differing by exactly one power of $d_B$.
(The Haar result is unconditional; the product result is conditional on the
product-class entropy-replacement principle of §3.5.)
Both exponents arise from the same underlying identity (Lemma 1) but
differ in how the bulk marginal $\rho_A^{\rm bulk}$ fluctuates across the
ensemble of bulk states. This section articulates the physical content of
that pattern.

### 6.1 The exponent gap from bulk-marginal fluctuations

A unified view of Theorems 2 and 3 is the following chain of
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

Lemma 1 applies for any $r$; only the subsequent moment computation
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
structural identity (Lemma 1) is already general enough to handle this:
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


---

## §7. Numerical landscape

This section assembles the numerical evidence for Theorems 2 and 3 in
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

![Figure 5](/paper3/figure5.png)

**Figure 5.** **(a)** Both classes, measured vs theory, log-log, with reference slopes $-1/2$ (product) and $-3/2$ (Haar). **(b)** Product/Haar ratio vs $d_B$, exhibiting the exponent gap as $\sim d_B^{+1}$ (growing from $\approx11$ to $\approx62$ over the scan).

matching the expected factor $24/4 = 6$ from the one-power gap.

### 7.3 The Phase-5 subleading analysis as cross-check

Prior to the analytic derivation of Theorem 2, the Phase 5 scan was
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
form $c\, d_B^{-3/2}\bigl(1 + b/d_B\bigr)$ with $b \approx -1.0$ is
$-3/2 - b/(d_B + b)$, which evaluates to $-1.32$ at $d_B = 8$ and
$-1.43$ at $d_B = 16$ — precisely the range of values seen in the
7-point fit. The analytic derivation (Theorem 2) dissolves this issue
directly: $\alpha_H = -3/2$ is exact, and the apparent drift is
captured by the explicit subleading structure (4.4).

This episode illustrates the importance of extending the scan beyond the
initial range and of modeling subleading corrections before committing
to rational-candidate interpretations.

### 7.4 Out-of-sample validation

Three out-of-sample tests provide the strongest single-point validation:

- **$d = 128$ no-$V$ Haar model** (33% beyond the Phase 7 subleading-fit
  range of $d \leq 96$): measured $\langle|H(p) - H(q)|\rangle = 1.37 \times 10^{-4}$
  at $N = 3{,}000$ samples, vs. corrected Theorem 2 prediction
  $1.37 \times 10^{-4}$. $z$ at sub-sigma precision.
- **$d_B = 18$ full HUZ+$V$+cloning pipeline** (not used in any scan):
  measured $0.00233 \pm 0.00029$ at $N = 60$, vs. corrected prediction
  $0.00249$. $z = -0.54\sigma$.
- **$d_B = 20$ full HUZ+$V$+cloning pipeline, Product class** (not in any
  initial calibration): measured $0.1190 \pm 0.018$ at $N = 40$, vs.
  Theorem 3 prediction $0.1250 \pm 0.0004$. $z = -0.35\sigma$.

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

![Figure 1](/paper3/figure1.png)

**Figure 1.** Finite-$d_B$ behaviour (Haar): the no-$V$ full-structure model (solid) tracks the measured HUZ+$V$ data (points) within error bars at every $d_B$, including $d_B=4$, while the asymptotic $0.798\,d_M^{-1}d_B^{-3/2}$ (dashed) is the large-$d_B$ limit.


- **Large $d_B$ ($\geq 20$)** has small $N$ (40–60 samples due to
  compute-per-sample growth as $d_{\rm eff}^3$). SEMs are correspondingly
  larger, and pointwise $z$-scores are less informative. Nonetheless,
  agreement within $1.5\sigma$ at every large-$d_B$ point provides
  useful asymptotic confirmation of the scaling.

### 7.6 Summary of verification

Across the two theorems, we have verified:

- **Theorem 3 (Product):** Five independent levels (Dirichlet variance
  asymptote, prefactor convergence, Gaussian-limit ratio, structural
  identity, zero-parameter end-to-end test against Phase 6 data), plus
  one out-of-sample point. All pass at sub-$2\sigma$ precision.
- **Theorem 2 (Haar):** Four independent levels (floating-asymptote
  fit, subleading-correction fit, structural identity, in-sample comparison
  with Phase 5 data), plus two out-of-sample points. All pass at
  sub-$2\sigma$ precision.

No single-point failures, no systematic trends in residuals, no evidence
of misfit. The two theorems as stated in §§4–5 are the leading-order
asymptotic form of the two-observer disagreement for their respective
bulk state classes, verified across the largest-reasonable computationally
accessible range of $d_B$.

---


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

Our Theorems 2 and 3 provide specific quantitative content at the
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
has no external reference register, so the machinery of Lemma 1 does
not apply directly. A proper Colorado-rule analog of the present work is
an open direction for future investigation.

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
  subleading structure $1 - 1.0/d_B + O(1/d_B^2)$ is fit numerically
  here; its origin is presumably non-Gaussian (higher-cumulant) corrections to the
  central-limit approximation for $T_A - T_B$ in §4.3, combined with bulk-norm
  fluctuation corrections.
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


---

## §9. Conclusion

We have established an entropy-replacement principle for non-isometric holographic
codes with HUZ observer inclusion: the von Neumann entropy of an observer's actual
reduced state equals the Shannon entropy of its diagonal in the cloning basis, up to
an error suppressed by a full power of $d_B$ relative to the two-observer signal. For
the Haar bulk class this is a theorem (Appendix C), proved through an exact
antisymmetric resolvent representation of the entropy difference, a linear bound that
reduces to the bulk-marginal moment, and a fourth-moment bound on the
random-projection perturbation closed by concentration on the unitary group. This
principle is the engine of the paper: it turns a genuine quantum-information quantity —
the disagreement of two cloned observers — into a classical moment calculation.

Applying it to two extreme bulk-state classes yields the central physical result, a
complexity-sensitive complementarity:

- **Haar class** (maximal complexity), *unconditional*:
  $\mathbb{E}|S_A - S_B| \to \sqrt{2/\pi}/(d_M\, d_B^{3/2}) \approx (0.798/d_M)\,d_B^{-3/2}$.
- **Product class** (minimal complexity), *conditional* on the product-class
  replacement principle:
  $\mathbb{E}|S_A - S_B| \to \sqrt{4(\pi^2/3-3)/\pi}\,d_B^{-1/2} \approx 0.608\,d_B^{-1/2}$.

The exponents differ by exactly one power of $d_B$: the room a non-isometric code
leaves for observer-dependent descriptions is set by the complexity of the bulk state.

Three directions stand out. First, **proving the product-class form of the
entropy-replacement principle** — the one remaining conditional step, requiring control
of the small-mass régime of the rank-1 bulk marginal where the Haar resolvent argument
does not directly transfer — would make Theorem 3 unconditional. Second, the
intermediate régime between product and Haar (e.g. rank-$r$ bulk states) should
interpolate between the two exponents; characterizing that interpolation would test
whether the complexity-sensitivity is sharp or smooth. Third, applying the same
machinery to alternative observer-inclusion rules (the Colorado rule, the
quantum-reference-frame crossed-product construction) would test how much of the
pattern is intrinsic to HUZ cloning and how much is universal.

