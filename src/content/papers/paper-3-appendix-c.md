---
title: "Appendix C — The Entropy-Replacement Proof (Haar)"
kind: "appendix"
paperNumber: 3
order: 4
subtitle: "C.1–C.5 off-diagonal F_off; C.6 diagonal-to-bulk F_diag by the centered-operator reduction; C.7 assembly."
---


This appendix proves Theorem 1 (§3.5) for the Haar bulk class: the von
Neumann entropy of the actual observer-reduced state may be replaced by the
Shannon entropy of its diagonal, with an error subleading to the two-observer
signal by a full power of $d$. All constants below are dimension-independent;
we write $D = d^2 d_M$ for the effective dimension, $\rho \in (0,1)$ for the
non-isometry ratio, and $X \in \{A,B\}$ for the two observers.

Throughout, $\rho_{R_X}$ is the observer-$X$ reduced state of the HUZ-included,
$V$-mapped state (§3.1). Two diagonals enter, and must be kept distinct:
$$
D_X := \mathrm{diag}(\rho_{R_X})\ \text{(actual, $V$-dependent)},
\qquad
P_X := \mathrm{diag}(\rho_X^{\rm bulk}),\ \ (P_A)_a = \sum_{bc}|\psi_{abc}|^2,\ \ (P_B)_b=\sum_{ac}|\psi_{abc}|^2,
$$
with $P_X$ depending only on $|\psi\rangle$. The full entropy-replacement error is
taken against the bulk-marginal diagonal $P_X$ (the object the scaling laws of
§§4–5 use), and splits into an off-diagonal and a diagonal-to-bulk part:
$$
F_{AB} := \bigl[S(\rho_{R_A}) - S(\rho_{R_B})\bigr] - \bigl[H(P_A) - H(P_B)\bigr]
\;=\; F_{\rm off} + F_{\rm diag},
$$
$$
F_{\rm off} := \bigl[S_A - S_B\bigr] - \bigl[H(D_A) - H(D_B)\bigr],
\qquad
F_{\rm diag} := \bigl[H(D_A) - H(D_B)\bigr] - \bigl[H(P_A) - H(P_B)\bigr].
$$
The off-diagonal perturbation is $E_X := \rho_{R_X} - D_X$. Sections C.1–C.5
bound $F_{\rm off}$ (the resolvent machinery); §C.6 adds the short diagonal-to-bulk
bound (Lemma C.6) and assembles the full statement. We prove:

> **Theorem C.1 (entropy replacement, Haar class).** In the joint Haar measure
> on bulk and $V$, with $d_A = d_B = d$ and $d_M$, $\rho$ fixed, the replacement
> against the bulk-marginal diagonal obeys
> $$
> \mathbb{E}\bigl[F_{AB}^2\bigr] = O\!\bigl(d^{-4} d_M^{-2}\bigr),
> \qquad\text{hence}\qquad
> \mathbb{E}\,\bigl|[S_A-S_B]-[H(P_A)-H(P_B)]\bigr| = O\!\bigl(d^{-2} d_M^{-1}\bigr) = o\!\bigl(d^{-3/2} d_M^{-1}\bigr),
> $$
> *with both $F_{\rm off}$ and $F_{\rm diag}$ of order $O(d^{-4}d_M^{-2})$ in $L^2$.*

Since the Haar two-observer signal has variance $\Theta(d^{-3}d_M^{-2})$
(Theorem 2), the replacement-error variance is suppressed by one power of
$d$, and Theorem 2 is unconditional.

The proof has four ingredients: an exact resolvent representation of $F_{AB}$
(§C.1); a linear bound reducing to a bulk-marginal moment (§C.2–C.3); a
nonlinear bound controlled by a fourth moment of $E_X$ (§C.4); the
fourth-moment estimate itself (§C.5); and a diagonal-to-bulk bound for
$F_{\rm diag}$ (Lemma C.6). The argument is assembled in §C.7.

---

## C.1 An exact antisymmetric resolvent representation

Write the von Neumann entropy through the integral representation
$S(\sigma) = -\mathrm{Tr}(\sigma\log\sigma)$ and the resolvent identity
$\log\sigma = \int_0^\infty\!\bigl[(1+t)^{-1} - (\sigma+t)^{-1}\bigr]dt$. Applied
to the antisymmetric combination $S(\rho_{R_A}) - S(\rho_{R_B})$ and to the
diagonal pair $H(D_A) - H(D_B)$, and subtracting, the constant and single-resolvent
terms cancel between the two observers, leaving an exact representation of the
difference $F_{\rm off}$. After the substitution $t = s/d$ (Jacobian $ds/d$),

> **Lemma C.1 (resolvent representation).**
> $$
> F_{\rm off} = \frac1d\int_0^\infty Y_s\,ds,
> \qquad
> Y_s = t\,R_t^{AB}\big|_{t=s/d},
> $$
> $$
> R_t^{AB} = \mathrm{Tr}\!\bigl[(D_A+t)^{-1} E_A (\rho_{R_A}+t)^{-1}\bigr] - (A\!\to\!B).
> $$

This is exact — all orders in the perturbation $E_X$ — and is the antisymmetric
analogue of the single-observer resolvent identity of Engelhardt–Gesteau–Harlow.
The integrand is concentrated near the eigenvalue scale $t \sim 1/d$
(equivalently $s \sim \rho^{-1}$); integrability at both ends follows from
$\|E_X\|_F \le 2$ and $\|(\,\cdot\,+t)^{-1}\|_{\rm op} \le 1/t$.

*Numerical check.* The representation reproduces the direct entropy difference
with correlation $1.0000$ and unit slope across $d \in \{4,5,6\}$, with the
integrand peaking at $s = td \approx 0.5$.

We split the integrand by one application of the resolvent identity
$(\rho_{R_X}+t)^{-1} = (D_X+t)^{-1} - (D_X+t)^{-1}E_X(\rho_{R_X}+t)^{-1}$,
giving $Y_s = Y_s^{\rm lin} + Y_s^{\rm nl}$ with
$$
Y_s^{\rm lin} = t\Bigl(\mathrm{Tr}[(D_A+t)^{-2}E_A] - (A\!\to\!B)\Bigr),
\qquad
Y_s^{\rm nl} = -t\Bigl(\mathrm{Tr}[G_A E_A G_A E_A \widetilde G_A] - (A\!\to\!B)\Bigr),
$$
where $G_X := (D_X+t)^{-1}$ and $\widetilde G_X := (\rho_{R_X}+t)^{-1}$. The two
pieces are bounded in §C.2–C.3 and §C.4 respectively.

---

## C.2 The linear bound

The linear integrand is a weighted version of the bulk-marginal object of §5.
Writing the diagonal entries $p_X^a = 1/d + \delta_a^X$ and centering, define
the weighted operator $H_X(t) = \sum_a (p_X^a+t)^{-2}\,\widetilde Q_X^{(a)}$,
where $\widetilde Q_X^{(a)}$ is the centered single-block operator of §C.3; then
$\mathrm{Tr}[(D_A+t)^{-2}E_A]-(A\!\to\!B) = \rho^{-1}\mathrm{Tr}[(P_V-\rho I)(H_A(t)-H_B(t))]$.

> **Lemma C.2 (linear bound).** $\displaystyle
> \mathbb{E}_\psi\,\mathrm{Tr}\!\bigl[(H_A(t)-H_B(t))^2\bigr] \le \frac{C\,d^2}{(1+s)^6 d_M}$,
> $C$ absolute, hence $\mathbb{E}[F_{\rm off}^2]_{\rm lin} = O(d^{-4}d_M^{-2})$.

*Proof.* The weight $w_X^a = (p_X^a+t)^{-2}$ satisfies, by the mean value
theorem on the event $\{p_X^a \ge c_0/d\}$ (whose complement is exponentially
rare), $|w_X^a - u^{-2}| \le K(s)\,|\delta_a^X|$ with $u = (1+s)/d$ and
$K(s) = \tfrac{2}{c_0^3}d^3(1+s)^{-3}$. Thus $H_X(t)$ has the form of the §C.3
object $G_X = \sum_a \delta_a^X \widetilde Q_X^{(a)}$ with weights bounded by
$K(s)|\delta_a^X|$. The base lemma's proof (§C.3) uses only the pointwise bound
$\|H_A-H_B\|_F^2 \le 4\max_X\mathrm{Tr}(H_X^2)$ and the exact single-block trace
formula, both valid for any weight; pulling out $K(s)^2$ and using the
single-observer base bound $\mathbb{E}_\psi\mathrm{Tr}(G_X^2)\le C_1/(d^5 d_M)$
gives $\mathbb{E}_\psi\mathrm{Tr}[(H_A-H_B)^2]\le 4K(s)^2 C_1/(d^5 d_M)
= \tfrac{16 C_1}{c_0^6}\,d(1+s)^{-6}d_M^{-1}\le C d^2(1+s)^{-6}d_M^{-1}$.
Then, with $Y_s^{\rm lin} = t\rho^{-1}\mathrm{Tr}[(P_V-\rho I)(H_A-H_B)]$ and
$\mathbb{E}_V|\mathrm{Tr}[(P_V-\rho I)M]|^2 = \kappa(\|M\|_F^2 - D^{-1}|\mathrm{Tr}M|^2)$
(Lemma C.3 below), Minkowski in $L^2(\psi)$ and $\int_0^\infty s(1+s)^{-3}ds = \tfrac12$
give $\mathbb{E}[F_{\rm off}^2]_{\rm lin} = O(1/(d^4 d_M^2))$. $\square$

*Numerical check.* The constant $C = \mathbb{E}_\psi\mathrm{Tr}[(H_A-H_B)^2]\cdot
(1+s)^6 d_M/d^2$ measures $1.44, 1.33, 1.21, 1.09, 1.01$ at $d = 4,\dots,8$
($d_M = 2$), decreasing toward the leading value; the $d_M$-scaling is exactly
$1/d_M$.

---

## C.3 The base moment lemma

The single-block object is $G_X = \sum_a \delta_a^X \widetilde Q_X^{(a)}$, where
$\widetilde Q_X^{(a)} = Q_X^{(a)} - p_X^a Q$ centers the rank-one block operator
$Q_X^{(a)} = \sum_b |\phi_{ab}\rangle\langle\phi_{ab}|$ against the total
$Q = \sum_{ab}|\phi_{ab}\rangle\langle\phi_{ab}|$. With $p_{ab} = \||\phi_{ab}\rangle\|^2$
the block masses (a flat Dirichlet vector on $d^2$ categories of concentration
$d_M$), the relevant block weights are $W_X^{(a)} = \sum_b p_{ab}^2$ and
$W_{\rm block} = \sum_{ab}p_{ab}^2$.

> **Lemma (base moment bound).** $\displaystyle
> \mathbb{E}_\psi\,\mathrm{Tr}\!\bigl[(G_A-G_B)^2\bigr] \le \frac{C_0}{d^4 d_M}$,
> with $C_0$ a dimension-independent constant.

*Proof.* Pointwise $\|G_A-G_B\|_F^2 \le 2\|G_A\|_F^2 + 2\|G_B\|_F^2 \le
4\max_X\mathrm{Tr}(G_X^2)$ (the cross term cancellation is not needed). The
single-observer trace has the exact closed form
$$
\mathrm{Tr}(G_X^2) = \sum_a (\delta_a^X)^2 W_X^{(a)} - 2 S_W^X\,\|\delta_X\|^2 + W_{\rm block}\,\|\delta_X\|^4,
$$
with $S_W^X = \sum_a \delta_a^X W_X^{(a)}$. The dominant term is the first; by
Cauchy–Schwarz, $\mathbb{E}\sum_a(\delta_a^X)^2 W_X^{(a)} = d\,\mathbb{E}[(\delta_1^X)^2 W_X^{(1)}]
\le d\sqrt{\mathbb{E}[(\delta_1^X)^4]\,\mathbb{E}[(W_X^{(1)})^2]}$. The fourth
central moment of the marginal $\delta_1^X$ (a centered $\mathrm{Beta}(dd_M, d(d-1)d_M)$
variable) is, in closed form, $\mathbb{E}[(\delta_1^X)^4] = (3+\gamma_2)\mu_2^2$
with
$$
\gamma_2 = \frac{6[(d-2)^2(D+1)-(d-1)(D+2)]}{(d-1)(D+2)(D+3)} \le \frac{12}{d\,d_M},
\qquad \mu_2 = \mathrm{Var}(\delta_1^X),
$$
so $\mathbb{E}[(\delta_1^X)^4]\le 7\mu_2^2$ for $d\ge3$; and $\mathbb{E}[(W_X^{(1)})^2]$
is the exact Dirichlet moment $\bigl(d(d_M)_4 + d(d-1)[(d_M)_2]^2\bigr)/(D)_4$.
Substituting the scalings $\mu_2 = \Theta(d^{-3}d_M^{-1})$ and
$\mathbb{E}[(W_X^{(1)})^2] = \Theta(d^{-6}d_M^{-2})$ gives the dominant term
$\Theta(d^{-5}d_M^{-1})$ and the stated bound after multiplying by $4$. The
remaining terms are smaller by $1/d$. $\square$

*Numerical check.* $\mathbb{E}_\psi\mathrm{Tr}[(G_A-G_B)^2]\cdot d^4 d_M =
0.40, 0.38, 0.35, 0.30, 0.25$ at $d = 4,5,6,8,10$; the closed-form $\gamma_2$
matches Monte Carlo to three digits.

---

## C.4 The nonlinear bound

> **Lemma (nonlinear bound).** $\displaystyle
> \mathbb{E}[F_{\rm off}^2]_{\rm nonlin} = O\!\bigl(d^{-4}d_M^{-2}\bigr)$,
> subleading to the signal by $1/d$.

*Proof.* By Schatten–Hölder applied to $Y_s^{\rm nl}$,
$$
\bigl|\mathrm{Tr}[G_X E_X G_X E_X \widetilde G_X]\bigr| \le \|G_X\|_{\rm op}^2\,\|\widetilde G_X\|_{\rm op}\,\|E_X\|_F^2,
$$
with $\|\widetilde G_X\|_{\rm op}\le 1/t$ deterministically ($\rho_{R_X}\succeq 0$)
and $\|G_X\|_{\rm op}\le \min(Cd, 1/t)$ on the good event. Hence, with $t = s/d$,
$|Y_s^{\rm nl}| \le \tfrac{s}{d}\min(Cd, d/s)^2\tfrac{d}{s}(\|E_A\|_F^2 + \|E_B\|_F^2)$.
Minkowski in $L^2$ and the kernel integral $\int_0^\infty \tfrac{s}{d}\min(Cd,d/s)^2\tfrac{d}{s}\,ds = 2Cd^2$
give $\sqrt{\mathbb{E}[F_{\rm off}^2]_{\rm nonlin}} \le \tfrac1d\cdot 2Cd^2\cdot 2\sqrt{\mathbb{E}\|E_X\|_F^4}$.
The fourth moment $\mathbb{E}\|E_X\|_F^4 = O(d^{-6}d_M^{-2})$ is supplied by §C.5,
whence $\mathbb{E}[F_{\rm off}^2]_{\rm nonlin} = O(d^{-4}d_M^{-2})$. The bad event
contributes $\mathrm{poly}(d)\cdot e^{-cdd_M}$, negligible. $\square$

*Numerical check.* The actual nonlinear contribution is
$\mathbb{E}[F^2]_{\rm nonlin}/\text{signal} = 0.011, 0.005, 0.003$ at $d=4,5,6$,
well inside the certified bound.

---

## C.5 The fourth-moment estimate

The nonlinear bound rests on a fourth moment of the off-diagonal perturbation
$E_X$. This follows from a single projector estimate plus a grouped-Dirichlet
moment bound.

> **Lemma C.3 (fourth-moment projector estimate).** Let $P_V$ be a Haar-random
> rank-$r$ projector on $\mathbb{C}^D$, $r=\rho D$, $\Pi = P_V - \rho I$. For any
> trace-zero $A$ on $\mathbb{C}^D$ (Hermitian or not),
> $$
> \mathbb{E}_V\bigl|\mathrm{Tr}(\Pi A)\bigr|^4 \le \frac{C_4\,\|A\|_F^4}{D^2},
> $$
> with a dimension-independent absolute constant $C_4$.

*Proof.* Since $\mathrm{Tr}(A)=0$, $\mathrm{Tr}(\Pi A) = \mathrm{Tr}(P_V A)$, which
has mean zero. Split $A = A_1 + iA_2$ into Hermitian trace-zero parts, so that
$|\mathrm{Tr}(\Pi A)|^4 \le 8[(\mathrm{Tr}\Pi A_1)^4 + (\mathrm{Tr}\Pi A_2)^4]$; it
suffices to bound each real piece. Writing $P_V = U\Pi_r U^\dagger$ with $U$ Haar
on $U(D)$ and $g_k(U) = \mathrm{Tr}(U\Pi_r U^\dagger A_k)$, the map
$U\mapsto U\Pi_r U^\dagger$ is $2$-Lipschitz in the Frobenius metric, so $g_k$ is
mean-zero and $2\|A_k\|_F$-Lipschitz. By the concentration inequality for
Lipschitz functions on $U(D)$ (Meckes, *The Random Matrix Theory of the Classical
Compact Groups*, 2019), $g_k$ is sub-Gaussian with variance proxy
$\sigma_k^2 = c_0\,(2\|A_k\|_F)^2/D$, whence $\mathbb{E}|g_k|^4 \le 3\sigma_k^4 \le
48 c_0^2 \|A_k\|_F^4/D^2$. Summing gives the claim with $C_4 = 384 c_0^2$. $\square$

*Remark.* The same estimate also follows from the fourth Weingarten moment of a
Haar rank-$r$ projector; the concentration proof is used only for the $O(D^{-2})$
scaling, not the sharp constant. Numerically and by the leading Gaussian pairing,
$C_4 D^2/\|A\|_F^4 \to 3\kappa^2 D^2 \to 3/16$ (the variable $\mathrm{Tr}(\Pi A)$ is
asymptotically Gaussian with variance $\kappa\|A\|_F^2$,
$\kappa = \tfrac{r(D-r)}{D(D^2-1)}$); measured $0.18$, flat across $D = 16,32,64$,
with kurtosis $\to 3$.

The entries of $E_X$ are exactly first-order in $\Pi$: $(E_X)_{aa'} =
\rho^{-1}\mathrm{Tr}(\Pi M_{a'a})/(1+\eta)$, where $M_{a'a}$ are trace-zero
operators (the off-diagonal blocks $N_{a'a}$ and the centered diagonal
$\widetilde Q_X^{(a)}$) and $\eta = \rho^{-1}\mathrm{Tr}(\Pi Q)$ is a normalization
fluctuation.

> **Proposition C.4 (fourth moment of the perturbation).** $\displaystyle
> \mathbb{E}\|E_X\|_F^4 \le \frac{C}{d^6 d_M^2}$, $C$ absolute.

*Proof.* On the good event $\mathcal{G} = \{|1+\eta|\ge\tfrac12\}$ (whose
complement has probability $\le e^{-cdd_M}$ and contributes
$\le\|E_X\|_{\rm op}^4\Pr(\mathcal{G}^c)\le 16 e^{-cdd_M}$, since $E_X$ is a
difference of density matrices so $\|E_X\|_{\rm op}\le 2$),
$\|E_X\|_F^4 \le 16\rho^{-4}\bigl(\sum_{a,a'}|\mathrm{Tr}(\Pi M_{a'a})|^2\bigr)^2$.
Expanding and taking $\mathbb{E}_V$, Cauchy–Schwarz and Lemma C.3 give
$\mathbb{E}_V[|\mathrm{Tr}\Pi M_{a'a}|^2|\mathrm{Tr}\Pi M_{c'c}|^2]\le
C_4 D^{-2}\|M_{a'a}\|_F^2\|M_{c'c}\|_F^2$, so
$\mathbb{E}_V\|E_X\|_F^4 \le 16\rho^{-4}C_4 D^{-2}\bigl(\sum_{a,a'}\|M_{a'a}\|_F^2\bigr)^2$.
The bracket bound (Lemma C.5) gives $\mathbb{E}_\psi(\cdot)^2 = O(d^{-2})$, and
with $D^2 = d^4 d_M^2$ the claim follows. $\square$

> **Lemma C.5 (bracket bound).** $\displaystyle
> \mathbb{E}_\psi\Bigl[\bigl(\textstyle\sum_{a,a'}\|M_{a'a}\|_F^2\bigr)^2\Bigr] \le \frac{C_B}{d^2}$,
> $C_B$ absolute.

*Proof.* The bracket equals $B = \sum_b[(p_B^b)^2 - W_B^{(b)}] + \sum_a\mathrm{Tr}((\widetilde Q_X^{(a)})^2)$.
The off-diagonal part has $\mathbb{E}_\psi = \Theta(1/d)$ (exact Dirichlet second
moment) and the diagonal part is $O(1/d^2)$, so $\mathbb{E}_\psi[B] = \Theta(1/d)$.
$B$ is a degree-2 polynomial in the Dirichlet masses; the grouped-Dirichlet
fourth moments (as in §C.3) give $\mathrm{Var}_\psi(B) = O(1/d^4)$, so
$\mathbb{E}_\psi[B^2] = (\mathbb{E}_\psi B)^2 + \mathrm{Var}_\psi(B) = O(1/d^2)$. $\square$

*Numerical check.* $\mathbb{E}[B]\,d = 0.98\to1.03$ and $\mathbb{E}[B^2]\,d^2 =
0.96\to1.06$ over $d=4$–$8$ (both flat, confirming $B$ concentrates), and
$\mathbb{E}\|E_X\|_F^4\cdot d^6 d_M^2 = 18.0, 11.9, 9.65$ at $d=4,5,6$
(bounded, decreasing).

---

## C.6 The diagonal-to-bulk bound

It remains to bound $F_{\rm diag} = [H(D_A)-H(D_B)] - [H(P_A)-H(P_B)]$, the error
from replacing the *actual* reduced diagonal $D_X=\mathrm{diag}(\rho_{R_X})$ by the
*bulk-marginal* diagonal $P_X$. Write $\eta_a^X := (\rho_{R_X})_{aa} - p_X^a$;
since $D_X$ and $P_X$ are both trace-one, $\sum_a \eta_a^X = 0$. The argument
reduces $F_{\rm diag}$ to the same base moment that controls $F_{\rm off}$, through
the centered block operators of §C.3.

**Representation.** With $Q_X^{(a)} = \sum_b |\phi_{ab}\rangle\langle\phi_{ab}|$ the
block operator and $P = V^\dagger V$, the unnormalized diagonal is
$(\rho_{R_X}^{\rm unnorm})_{aa} = \mathrm{Tr}[P\,Q_X^{(a)}]$, with Haar mean
$\mathbb{E}_V = \rho\,\mathrm{Tr}\,Q_X^{(a)} = \rho\,p_X^a$. Dividing by
$Z = \|\Psi\|^2$ (with $\mathbb{E}_V Z = \rho$) and using $\rho\,p_X^a =
\mathrm{Tr}[\rho I\,Q_X^{(a)}]$,
$$
\eta_a^X \;=\; \frac{1}{\rho}\,\mathrm{Tr}\!\bigl[(P-\rho I)\,Q_X^{(a)}\bigr] \;+\; r_a^X,
\qquad
r_a^X = -\,\frac{Z-\rho}{\rho}\,(\rho_{R_X})_{aa},
$$
the normalization remainder $r_a^X$ being $O(d^{-2})\cdot(\rho_{R_X})_{aa}$ by
Lemma 2. The leading-order entropy term of §C.6 (the Taylor expansion of $H$ about
$P_X$, using $\partial H/\partial p_a = -\log p_a - 1$ and $\sum_a \eta_a^X = 0$,
which removes the constant and the $-1$) is the linear functional
$$
L_X \;=\; -\,d\sum_a \delta_a^X\,\eta_a^X,
\qquad
F_{\rm diag} \;=\; (L_A - L_B) \;+\; (R_A - R_B),
$$
with $R_X = O\!\bigl(\sum_a (\eta_a^X)^2/p_X^a\bigr)$ the quadratic Taylor remainder.

**Reduction to the base moment.** Substituting the representation,
$$
L_A - L_B
\;=\; -\frac{d}{\rho}\,\mathrm{Tr}\!\Bigl[(P-\rho I)\,\textstyle\sum_a\bigl(\delta_a^A Q_A^{(a)} - \delta_a^B Q_B^{(a)}\bigr)\Bigr] \;+\; (\text{norm remainder}).
$$
Replacing each $Q_X^{(a)}$ by its centered form $\widetilde Q_X^{(a)} = Q_X^{(a)} - p_X^a Q$
changes the bracket by $\bigl(\sum_a \delta_a^X p_X^a\bigr)Q = \|\delta_X\|^2\,Q$
(since $\sum_a \delta_a^X p_X^a = \sum_a (p_X^a)^2 - 1/d = \|\delta_X\|^2$), and
$\mathrm{Tr}[(P-\rho I)Q] = Z-\rho$ is the norm fluctuation; this difference is
absorbed into the remainder. Hence, with $G_X = \sum_a \delta_a^X \widetilde Q_X^{(a)}$
the operator of §C.3,
$$
L_A - L_B \;=\; -\frac{d}{\rho}\,\mathrm{Tr}\!\bigl[(P-\rho I)(G_A - G_B)\bigr] \;+\; (\text{remainder}).
$$

For a uniformly random rank-$\rho D$ projector and any fixed Hermitian $M$, the
projector variance gives $\mathrm{Var}_V(\mathrm{Tr}[P M]) \le \rho(1-\rho)\,
\mathrm{Tr}(M^2)/(D-1)$. Applied with $M = G_A - G_B$ (fixed by $\psi$),
$$
\mathbb{E}_V\!\bigl[(L_A - L_B)^2 \,\big|\, \psi\bigr]
\;\le\; \frac{d^2}{\rho^2}\,\mathrm{Var}_V\!\bigl(\mathrm{Tr}[P(G_A-G_B)]\bigr)
\;\le\; C\,\frac{d^2}{D}\,\mathrm{Tr}\!\bigl[(G_A - G_B)^2\bigr],
\qquad C = \tfrac{1-\rho}{\rho}.
$$
Taking $\mathbb{E}_\psi$ and invoking the **base moment bound of §C.3**,
$\mathbb{E}_\psi\,\mathrm{Tr}[(G_A-G_B)^2] \le C_0/(d^4 d_M)$, and $D = d^2 d_M$,
$$
\mathbb{E}\bigl[(L_A - L_B)^2\bigr]
\;\le\; C\,\frac{d^2}{D}\cdot\frac{C_0}{d^4 d_M}
\;=\; C\,C_0\,\frac{d^2}{d^2 d_M}\cdot\frac{1}{d^4 d_M}
\;=\; O\!\bigl(d^{-4} d_M^{-2}\bigr).
$$

**Remainders.** The normalization remainder ($\propto Z-\rho$, of relative size
$O(d^{-2})$ by Lemma 2) and the quadratic Taylor remainder $R_A - R_B$ (a sum of
$(\eta_a^X)^2/p_X^a$ terms, controlled by the same Frobenius/fourth-moment estimates
of §§C.4–C.5 applied to the diagonal entries) each contribute
$\mathbb{E}[(R_A - R_B)^2] = O(d^{-4} d_M^{-2})$ or smaller. Collecting:

**Lemma C.6 (diagonal-to-bulk replacement).** *In the joint measure,*
$$
\mathbb{E}\bigl[F_{\rm diag}^2\bigr] \;=\; O\!\bigl(d^{-4} d_M^{-2}\bigr),
$$
*the same order as $F_{\rm off}$, hence one power of $d$ below the signal variance
$\Theta(d^{-3}d_M^{-2})$.* $\square$

The reduction is exact: $F_{\rm diag}$ and $F_{\rm off}$ are bounded by the *same*
quantity $\mathbb{E}_\psi\,\mathrm{Tr}[(G_A-G_B)^2]$ through the *same* rank-projector
variance estimate, so no separate constant is introduced. (The independent
Monte-Carlo value $\mathbb{E}[F_{\rm diag}^2]\cdot d^4 d_M^2 = 0.49, 0.36, 0.34$ at
$d=4,5,6$ is consistent, but the bound above does not rely on it.)

## C.7 Assembly

The off-diagonal error $F_{\rm off}$ is controlled by combining the linear bound
(Lemma C.2: $\mathbb{E}[F_{\rm off}^2]_{\rm lin} = O(d^{-4}d_M^{-2})$) with the
nonlinear bound (§C.4, via Proposition C.4: $\mathbb{E}[F_{\rm off}^2]_{\rm nonlin}
= O(d^{-4}d_M^{-2})$) and Minkowski's inequality, giving $\mathbb{E}[F_{\rm off}^2]
= O(d^{-4}d_M^{-2})$. Adding the diagonal-to-bulk bound (Lemma C.6:
$\mathbb{E}[F_{\rm diag}^2] = O(d^{-4}d_M^{-2})$) through $F_{AB} = F_{\rm off} +
F_{\rm diag}$ and Minkowski once more,
$$
\mathbb{E}\bigl[F_{AB}^2\bigr] = O\!\bigl(d^{-4}d_M^{-2}\bigr) = o\!\bigl(d^{-3}d_M^{-2}\bigr),
$$
which is one power of $d$ below the signal variance $\Theta(d^{-3}d_M^{-2})$.
By Cauchy–Schwarz, $\mathbb{E}|F_{AB}| \le \sqrt{\mathbb{E}[F_{AB}^2]} =
O(d^{-2}d_M^{-1}) = o(d^{-3/2}d_M^{-1})$. This proves Theorem C.1, hence
Theorem 1 for the Haar class, and makes Theorem 2 unconditional. $\blacksquare$

*End-to-end numerical check.* Directly, $\mathbb{E}[F_{AB}^2]/\text{signal} =
0.146, 0.094, 0.067$ and $\mathbb{E}|F_{AB}|/(d^{-3/2}d_M^{-1}) = 0.280, 0.233,
0.196$ at $d=4,5,6$ — both decreasing, consistent with the proved $O(1/d)$ and
$O(1/\sqrt d)$ suppression.

*Remark (product class).* The representation of §C.1 and the nonlinear bound of
§C.4 hold verbatim for any bulk class. The Haar-specific inputs are the
bulk-marginal moments of §C.3 and §C.5, which use the near-maximally-mixed
Dirichlet structure of the Haar marginal. For the product class the marginal is
rank-one, and the small-mass régime of its diagonal is not controlled by the
present argument; establishing the analogue of Lemma C.5 there would make
Theorem 3 unconditional as well. This is the sense in which Theorem 1
remains conjectural for the product class.
