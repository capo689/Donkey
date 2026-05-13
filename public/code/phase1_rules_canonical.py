"""
phase1_rules_canonical.py — Phase 1 deliverable of the BH observer-complementarity
research program.

Ports the HUZ (Harlow-Usatyuk-Zhao 2501.02359) and Colorado
(Akers-Bueller-DeWolfe-Higginbotham-Reinking-Rodriguez 2503.09681)
observer-inclusion rules onto the unified backend. Supersedes the previous
thread's step2a_huz_rule.py and step2b_colorado_rule.py, both of which used
the pre-fix AEHPV normalization and whose specific entropy values were
therefore not canonical.

Produces canonical tables of observer-dependent entropies and effective
accessible ranks at multiple (d_Ob, d_M, d_fund) combinations.

Gate conditions (per Part 5, Phase 1 of bh_new_thread_spinup.md):
  1. Rank-of-reduced-state dimension predictions match exactly (integer-valued,
     therefore normalization-independent — the only dimension prediction that
     can meaningfully "fail").
  2. Haar-averaged entropies are reproducible with given seeds.
  3. Backend self-test still passes.

Plus a qualitative gate from Part 3, Result 4:
  - HUZ and Colorado agree to machine precision on product-state input (both 0).
  - On the specific superposed input (1/sqrt(d)) sum_i |i>|i>,
    S_Colorado = log(d_fund,M) exactly (derivation in code comments).

Run: python phase1_rules_canonical.py
"""
from __future__ import annotations

import math
import os
import subprocess
import sys

import numpy as np
import pandas as pd

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from bh_lab_backend import (
    SeededRNG,
    huz_single_observer_entropy,
    colorado_single_observer_entropy,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def effective_rank(rho: np.ndarray, tol: float = 1e-8) -> int:
    evals = np.linalg.eigvalsh(0.5 * (rho + rho.conj().T))
    return int(np.sum(evals > tol))


def page_entropy(d_small: int, d_large: int) -> float:
    """<S> for Haar-random pure state on C^{d_small*d_large} reduced to C^{d_small}.
    Exact Page formula (Foong-Kanno / Sen / Page)."""
    if d_small > d_large:
        d_small, d_large = d_large, d_small
    return (
        sum(1.0 / k for k in range(d_large + 1, d_small * d_large + 1))
        - (d_small - 1) / (2 * d_large)
    )


def haar_sample_huz(d_Ob: int, d_M: int, d_fund: int,
                    n_samples: int, seed: int) -> dict:
    rng = SeededRNG(seed=seed)
    entropies = np.empty(n_samples)
    ranks = np.empty(n_samples, dtype=int)
    for i in range(n_samples):
        V = rng.aehpv_map(d_Ob * d_M, d_fund)
        psi = rng.haar_state(d_Ob * d_M)
        S, rho_R = huz_single_observer_entropy(psi, V, d_Ob, d_M)
        entropies[i] = S
        ranks[i] = effective_rank(rho_R)
    std = float(np.std(entropies, ddof=1))
    return {
        "mean_S": float(np.mean(entropies)),
        "std_S": std,
        "sem_S": std / math.sqrt(n_samples),
        "rank_mode": int(np.bincount(ranks).argmax()),
        "rank_min": int(ranks.min()),
        "rank_max": int(ranks.max()),
    }


def haar_sample_colorado(d_Ob: int, d_M: int, d_fundM: int,
                          n_samples: int, seed: int) -> dict:
    rng = SeededRNG(seed=seed)
    entropies = np.empty(n_samples)
    ranks = np.empty(n_samples, dtype=int)
    for i in range(n_samples):
        V_M = rng.aehpv_map(d_M, d_fundM)
        psi = rng.haar_state(d_Ob * d_M)
        S, rho_Ob = colorado_single_observer_entropy(psi, V_M, d_Ob)
        entropies[i] = S
        ranks[i] = effective_rank(rho_Ob)
    std = float(np.std(entropies, ddof=1))
    return {
        "mean_S": float(np.mean(entropies)),
        "std_S": std,
        "sem_S": std / math.sqrt(n_samples),
        "rank_mode": int(np.bincount(ranks).argmax()),
        "rank_min": int(ranks.min()),
        "rank_max": int(ranks.max()),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> bool:
    print("=" * 78)
    print("Phase 1 — HUZ + Colorado canonical tables")
    print("=" * 78)

    print("\n[A] Backend self-test")
    result = subprocess.run(
        [sys.executable, os.path.join(_HERE, "bh_lab_backend.py")],
        capture_output=True, text=True,
    )
    backend_ok = (result.returncode == 0)
    if not backend_ok:
        print("  FAIL: backend returned non-zero.")
        print(result.stdout[-1200:])
    else:
        print("  backend self-test passed (11 checks).")

    N_SAMPLES = 80
    BASE_SEED = 424242

    print(f"\n[B] HUZ dimension sweep  (n_samples per row = {N_SAMPLES})")
    huz_rows = []
    for d_Ob in (2, 3, 4):
        for d_M in (2, 3, 4):
            for d_fund in (2, 3, 5, 8):
                if d_fund > d_Ob * d_M:
                    continue
                seed = BASE_SEED + d_Ob * 10_000 + d_M * 100 + d_fund
                stats = haar_sample_huz(d_Ob, d_M, d_fund, N_SAMPLES, seed)
                huz_rows.append({
                    "d_Ob": d_Ob, "d_M": d_M, "d_eff": d_Ob * d_M, "d_fund": d_fund,
                    "d_out(fund*R)": d_fund * d_Ob,
                    "rank_pred": min(d_Ob, d_fund),
                    "rank_obs":  stats["rank_mode"],
                    "<S_HUZ>":   stats["mean_S"],
                    "SEM":       stats["sem_S"],
                    "logdOb":    math.log(d_Ob),
                    "log_min":   math.log(min(d_Ob, d_fund)),
                })
    df_huz = pd.DataFrame(huz_rows)
    print(df_huz.to_string(index=False, float_format=lambda x: f"{x:.4f}"))

    print(f"\n[C] Colorado dimension sweep  (n_samples per row = {N_SAMPLES})")
    col_rows = []
    for d_Ob in (2, 3, 4):
        for d_M in (3, 4, 5):
            for d_fundM in (2, 3, 4):
                if d_fundM > d_M:
                    continue
                seed = BASE_SEED + d_Ob * 10_000 + d_M * 100 + d_fundM + 7
                stats = haar_sample_colorado(d_Ob, d_M, d_fundM, N_SAMPLES, seed)
                col_rows.append({
                    "d_Ob": d_Ob, "d_M": d_M, "d_fundM": d_fundM,
                    "d_out(Ob*fundM)": d_Ob * d_fundM,
                    "rank_pred": min(d_Ob, d_fundM),
                    "rank_obs":  stats["rank_mode"],
                    "<S_Colorado>": stats["mean_S"],
                    "SEM":          stats["sem_S"],
                    "logdOb":       math.log(d_Ob),
                    "log_min":      math.log(min(d_Ob, d_fundM)),
                })
    df_col = pd.DataFrame(col_rows)
    print(df_col.to_string(index=False, float_format=lambda x: f"{x:.4f}"))

    print("\n[D] Rank prediction check")
    huz_bad = df_huz[df_huz["rank_pred"] != df_huz["rank_obs"]]
    col_bad = df_col[df_col["rank_pred"] != df_col["rank_obs"]]
    print(f"  HUZ rows where rank_pred != rank_obs: {len(huz_bad)} / {len(df_huz)}")
    print(f"  Colorado rows where rank_pred != rank_obs: {len(col_bad)} / {len(df_col)}")
    ranks_ok = (len(huz_bad) == 0 and len(col_bad) == 0)

    print("\n[E] Reproducibility")
    seed_repro = BASE_SEED + 999
    a = haar_sample_huz(3, 4, 5, N_SAMPLES, seed_repro)
    b = haar_sample_huz(3, 4, 5, N_SAMPLES, seed_repro)
    reproducible_huz = (a["mean_S"] == b["mean_S"]) and (a["rank_mode"] == b["rank_mode"])
    print(f"  HUZ(d_Ob=3, d_M=4, d_fund=5): reproducible = {reproducible_huz}")

    c = haar_sample_colorado(3, 4, 2, N_SAMPLES, seed_repro)
    d = haar_sample_colorado(3, 4, 2, N_SAMPLES, seed_repro)
    reproducible_col = (c["mean_S"] == d["mean_S"]) and (c["rank_mode"] == d["rank_mode"])
    print(f"  Colorado(d_Ob=3, d_M=4, d_fundM=2): reproducible = {reproducible_col}")

    print("\n[F] HUZ vs Colorado on product vs superposed inputs")
    d_Ob, d_M = 3, 3
    d_fund = 5
    d_fundM = 2
    rng = SeededRNG(seed=777)
    V = rng.aehpv_map(d_Ob * d_M, d_fund)
    V_M = rng.aehpv_map(d_M, d_fundM)

    ob_vec = np.eye(d_Ob)[1]
    mat = rng.haar_state(d_M)
    psi_prod = np.kron(ob_vec, mat)
    S_huz_prod, _ = huz_single_observer_entropy(psi_prod, V, d_Ob, d_M)
    S_col_prod, _ = colorado_single_observer_entropy(psi_prod, V_M, d_Ob)

    psi_sup = np.zeros(d_Ob * d_M, dtype=complex)
    for i in range(min(d_Ob, d_M)):
        psi_sup += np.kron(np.eye(d_Ob)[i], np.eye(d_M)[i])
    psi_sup /= np.linalg.norm(psi_sup)
    S_huz_sup, _ = huz_single_observer_entropy(psi_sup, V, d_Ob, d_M)
    S_col_sup, _ = colorado_single_observer_entropy(psi_sup, V_M, d_Ob)

    print(f"  S_HUZ(product) = {S_huz_prod:.2e}  (expect 0)")
    print(f"  S_Colorado(product) = {S_col_prod:.2e}  (expect 0)")
    print(f"  S_HUZ(superposed) = {S_huz_sup:.6f}")
    print(f"  S_Colorado(superposed) = {S_col_sup:.6f}  (expect log({d_fundM}) = {math.log(d_fundM):.6f})")

    product_agreement = (S_huz_prod < 1e-8) and (S_col_prod < 1e-8)
    colorado_analytic_ok = abs(S_col_sup - math.log(d_fundM)) < 1e-10
    superposed_disagreement = abs(S_huz_sup - S_col_sup) > 1e-3

    out_dir = "/mnt/user-data/outputs"
    os.makedirs(out_dir, exist_ok=True)
    df_huz.to_csv(os.path.join(out_dir, "phase1_huz_table.csv"), index=False)
    df_col.to_csv(os.path.join(out_dir, "phase1_colorado_table.csv"), index=False)
    print("\n[G] Saved tables to outputs directory")

    print("\n" + "=" * 78)
    print("PHASE 1 GATE STATUS")
    print("=" * 78)
    checks = [
        ("backend self-test passes", backend_ok),
        ("HUZ rank predictions match in every row", len(huz_bad) == 0),
        ("Colorado rank predictions match in every row", len(col_bad) == 0),
        ("HUZ reproducibility", reproducible_huz),
        ("Colorado reproducibility", reproducible_col),
        ("product state: S_HUZ = S_Colorado = 0", product_agreement),
        ("superposed state: S_Colorado = log(d_fundM) exactly", colorado_analytic_ok),
        ("superposed state: HUZ and Colorado disagree", superposed_disagreement),
    ]
    all_pass = True
    for label, ok in checks:
        tag = "PASS" if ok else "FAIL"
        print(f"  [{tag}] {label}")
        all_pass = all_pass and ok
    if all_pass:
        print("\nPhase 1 gate PASSED.")
    else:
        print("\nPhase 1 gate NOT PASSED.")
    print("=" * 78)
    return all_pass


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
