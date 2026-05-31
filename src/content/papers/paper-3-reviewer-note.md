---
title: "The Reviewer's Note"
kind: "reviewer-note"
paperNumber: 3
order: 5
subtitle: "A summary of the six-round adversarial review by Scholar (ChatGPT), and the final state of the manuscript."
---


This package incorporates every fix from the review rounds. The last substantive
item — Appendix C.6 — is now proved theorem-grade by the centered-operator method,
with no numerical constant inside the proof.

## C.6 — diagonal-to-bulk bound, closed via reduction to the §C.3 base moment
The proof now reduces F_diag to the SAME base moment that controls F_off:

1. Representation: eta_a^X = (1/rho) Tr[(P - rho I) Q_X^(a)] + normalization remainder,
   from (rho_RX^unnorm)_aa = Tr[P Q_X^(a)], Haar mean rho p_X^a, divided by Z ~ rho.
2. Linear error: L_A - L_B = -(d/rho) Tr[(P - rho I)(G_A - G_B)] + remainder, with the
   centered G_X = sum_a delta_a^X Qtil_X^(a), Qtil = Q_X^(a) - p_X^a Q (§C.3). The
   Q -> Qtil swap costs only a norm-fluctuation remainder, since
   sum_a delta_a^X p_X^a = ||delta_X||^2 and Tr[(P-rho I)Q] = Z - rho.
3. Projector variance: E_V[(L_A - L_B)^2 | psi] <= C (d^2/D) Tr[(G_A - G_B)^2].
4. Base moment (§C.3, already proved): E_psi Tr[(G_A - G_B)^2] <= C_0/(d^4 dM).
5. With D = d^2 dM: E[(L_A - L_B)^2] <= C C_0 (d^2/D)(1/d^4 dM) = O(d^-4 dM^-2).
   Normalization + quadratic Taylor remainders are O(d^-4 dM^-2) or smaller via the
   §§C.4-C.5 Frobenius / fourth-moment machinery.

F_off and F_diag are bounded by the same quantity E_psi Tr[(G_A-G_B)^2] through the
same rank-projector estimate, so the proof introduces no separate constant. The
representation was checked numerically before writing (scratch_centered_C6.py:
correlation 0.9995, 0.9998 with the direct linear error at d=4,5), but the bound does
not rely on numerics. Lemma C.6a (the old conditional-covariance route) is removed;
all numerics-dependent off-diagonal-covariance language is deleted from Appendix C. scratch_Mdom.py remains only as a labeled diagnostic, supporting no
proof step.

## Summary of the full review history (all resolved)
- §3 structural identity: E_V[rho_RA] = diag(rho_A^bulk) + O(1/d^2) (delta_aa' at
  first moment); off-diagonals collapse at first moment.
- Theorem hierarchy: Theorem 1 (entropy replacement, target bulk-marginal P_X);
  Theorem 2 (Haar, unconditional); Theorem 3 (product, conditional). Lemma 1 =
  structural identity.
- §4 Haar covariance: grouped-Dirichlet (T_A, T_B) proof; Cov(p_a,p_a')<0,
  Cov(p_a,q_b)=0; Var(T_A-T_B) ~ 4/(d^5 dM^2); Var(H(p)-H(q)) ~ 1/(d^3 dM^2).
- Appendix C: F_AB = F_off + F_diag, both O(d^-4 dM^-2), one power of d below the
  signal; Theorem 2 unconditional.
- Figures regenerated from canonical CSVs (Figure 4: A = 1.00 +/- 0.01, subleading
  1 - 1.0/d_B). Table 1 / Figure 4(c) / Figure 5 all load table1_full_scan.csv.
- Appendix B manifest matches the shipped reproducibility/ set; B.6 separates shipped
  checks from historical-development checks.

## Package
Flat: paper_full_v3_FINAL.md, paper_appendix_A/B/C.md, figure1-5.png,
reproducibility/, MANIFEST.txt, this note. Upload directly; do not wrap in another zip.

## Status
Theorem 2 unconditional (Appendix C complete, including C.6). Theorem 3 conditional on
the product-class replacement (small-mass rank-1 regime), explicitly flagged as the
single open analytic step and the natural follow-up.
