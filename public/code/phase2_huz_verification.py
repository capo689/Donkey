"""
phase2_huz_verification.py — Phase 2 deliverable.

Tests HUZ 2501.02359's claim that errors in the observer-dependent description
decay as e^{-S_Ob} = 1/d_Ob in finite-dim language.

We compute three error metrics:

  E_ovl = | <Psi1|Psi2>/(||Psi1|| ||Psi2||) - <psi1|psi2>_bulk |
      ^ most direct operationalization of HUZ's claim

  E_td  = (1/2) || rho_R^{true} - diag(p_ob) ||_1
      ^ trace distance between the HUZ-computed observer reduced state and
        the cloning-only prediction

  E_S   = | S(rho_R^{true}) - H(p_ob) |
       ^ entropy-level error

For all metrics we fit log(E) = alpha * log(d_Ob) + beta via OLS.
"""
from __future__ import annotations

import math
import os
import subprocess
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from bh_lab_backend import (
    SeededRNG,
    apply_huz_single,
    partial_trace,
    von_neumann_entropy,
)


def shannon_entropy(p: np.ndarray, eps: float = 1e-14) -> float:
    p = np.asarray(p, dtype=float)
    p = p[p > eps]
    if p.size == 0:
        return 0.0
    return float(-np.sum(p * np.log(p)))


def huz_observables(psi: np.ndarray, V: np.ndarray, d_Ob: int, d_M: int) -> dict:
    d_fund = V.shape[0]
    psi_out = apply_huz_single(psi, V, d_Ob, d_M)
    norm = math.sqrt(np.vdot(psi_out, psi_out).real)
    psi_norm = psi_out / norm
    rho_full = np.outer(psi_norm, psi_norm.conj())
    rho_R = partial_trace(rho_full, dims=[d_fund, d_Ob], keep=[1])
    p_ob = np.sum(np.abs(psi.reshape(d_Ob, d_M)) ** 2, axis=1)
    return {"psi_norm": psi_norm, "rho_R": rho_R, "p_ob": p_ob}


def error_sample(d_Ob: int, d_M: int, d_fund: int,
                 n_samples: int, seed: int) -> dict:
    rng = SeededRNG(seed=seed)
    errs_ovl = np.empty(n_samples)
    errs_td = np.empty(n_samples)
    errs_S = np.empty(n_samples)
    for i in range(n_samples):
        V = rng.aehpv_map(d_Ob * d_M, d_fund)
        psi1 = rng.haar_state(d_Ob * d_M)
        psi2 = rng.haar_state(d_Ob * d_M)

        o1 = huz_observables(psi1, V, d_Ob, d_M)
        o2 = huz_observables(psi2, V, d_Ob, d_M)

        O_fund = np.vdot(o1["psi_norm"], o2["psi_norm"])
        O_bulk = np.vdot(psi1, psi2)
        errs_ovl[i] = abs(O_fund - O_bulk)

        rho_naive = np.diag(o1["p_ob"].astype(complex))
        diff = o1["rho_R"] - rho_naive
        eig = np.linalg.eigvalsh(0.5 * (diff + diff.conj().T))
        errs_td[i] = 0.5 * float(np.sum(np.abs(eig)))

        S_true = von_neumann_entropy(o1["rho_R"])
        H_p = shannon_entropy(o1["p_ob"])
        errs_S[i] = abs(S_true - H_p)

    def _stat(x):
        m = float(np.mean(x)); s = float(np.std(x, ddof=1))
        return m, s / math.sqrt(n_samples)

    E_ovl_m, E_ovl_sem = _stat(errs_ovl)
    E_td_m, E_td_sem = _stat(errs_td)
    E_S_m, E_S_sem = _stat(errs_S)
    return {
        "E_ovl": E_ovl_m, "E_ovl_sem": E_ovl_sem,
        "E_td": E_td_m, "E_td_sem": E_td_sem,
        "E_S": E_S_m, "E_S_sem": E_S_sem,
    }


def fit_power_law(xs, ys, sems=None) -> dict:
    x = np.log(np.array(xs, dtype=float))
    y = np.log(np.array(ys, dtype=float))
    X = sm.add_constant(x)
    res = sm.OLS(y, X).fit()
    beta, alpha = res.params
    ci = res.conf_int(alpha=0.05)
    return {
        "alpha": float(alpha),
        "beta": float(beta),
        "alpha_lo": float(ci[1][0]),
        "alpha_hi": float(ci[1][1]),
        "R2": float(res.rsquared),
    }


CONFIGS = [
    {
        "name": "A",
        "desc": "d_M=4, d_fund=2*d_Ob",
        "d_M": 4,
        "d_fund_fn": lambda d_Ob: 2 * d_Ob,
        "d_Ob_list": [2, 3, 4, 6, 8, 10, 12, 16],
    },
    {
        "name": "B",
        "desc": "d_M=4, d_fund=3*d_Ob",
        "d_M": 4,
        "d_fund_fn": lambda d_Ob: 3 * d_Ob,
        "d_Ob_list": [2, 3, 4, 6, 8, 10, 12],
    },
    {
        "name": "C",
        "desc": "d_M=4, d_fund=d_Ob",
        "d_M": 4,
        "d_fund_fn": lambda d_Ob: d_Ob,
        "d_Ob_list": [2, 3, 4, 6, 8, 10, 12, 16],
    },
]

N_SAMPLES = 120
BASE_SEED = 313131


def main() -> bool:
    print("=" * 78)
    print("Phase 2 — HUZ error-scaling verification")
    print("=" * 78)

    print("\n[A] Backend self-test")
    rc = subprocess.run(
        [sys.executable, os.path.join(_HERE, "bh_lab_backend.py")],
        capture_output=True, text=True,
    ).returncode
    if rc != 0:
        print("  FAIL: backend self-test non-zero.")
        return False
    print("  backend self-test passed")

    all_dfs = {}
    all_fits = {}
    for cfg in CONFIGS:
        print(f"\n[B.{cfg['name']}] Config {cfg['name']}: {cfg['desc']}")
        rows = []
        for d_Ob in cfg["d_Ob_list"]:
            d_fund = cfg["d_fund_fn"](d_Ob)
            d_eff = d_Ob * cfg["d_M"]
            if d_fund >= d_eff:
                continue
            seed = BASE_SEED + d_Ob * 131 + cfg["d_M"] * 11 + d_fund
            stats = error_sample(d_Ob, cfg["d_M"], d_fund, N_SAMPLES, seed)
            rows.append({
                "d_Ob": d_Ob, "d_M": cfg["d_M"], "d_fund": d_fund, "d_eff": d_eff,
                "E_ovl": stats["E_ovl"], "E_ovl_sem": stats["E_ovl_sem"],
                "E_td":  stats["E_td"],  "E_td_sem":  stats["E_td_sem"],
                "E_S":   stats["E_S"],   "E_S_sem":   stats["E_S_sem"],
            })
        df = pd.DataFrame(rows)
        print(df.to_string(index=False))
        all_dfs[cfg["name"]] = df

        print(f"\n  Power-law fits:")
        fits = {}
        for metric in ["E_ovl", "E_td", "E_S"]:
            good = df[df[metric] > 0]
            if len(good) < 3:
                continue
            fit = fit_power_law(good["d_Ob"].values, good[metric].values)
            fits[metric] = fit
            print(f"    {metric:5s}: alpha = {fit['alpha']:+.3f}  R2 = {fit['R2']:.4f}")
        all_fits[cfg["name"]] = fits

    out_dir = "/mnt/user-data/outputs"
    os.makedirs(out_dir, exist_ok=True)
    for name, df in all_dfs.items():
        df.to_csv(os.path.join(out_dir, f"phase2_config_{name}.csv"), index=False)

    fit_rows = []
    for name, fits in all_fits.items():
        for metric, fit in fits.items():
            fit_rows.append({
                "config": name, "metric": metric,
                "alpha": fit["alpha"], "alpha_lo": fit["alpha_lo"],
                "alpha_hi": fit["alpha_hi"], "R2": fit["R2"],
            })
    fit_df = pd.DataFrame(fit_rows)
    print("\n[C] Summary of all power-law exponents")
    print(fit_df.to_string(index=False))
    fit_df.to_csv(os.path.join(out_dir, "phase2_exponents.csv"), index=False)

    print("\n[D] d_M dependence at fixed (d_Ob=4, r=2)")
    dM_rows = []
    d_Ob_fix = 4
    r_fix = 2
    for d_M in (2, 3, 4, 5, 6, 8):
        d_eff = d_Ob_fix * d_M
        d_fund = d_eff // r_fix
        if d_fund < 2 or d_eff % r_fix != 0:
            continue
        seed = BASE_SEED + 7777 + d_M * 31
        stats = error_sample(d_Ob_fix, d_M, d_fund, N_SAMPLES, seed)
        dM_rows.append({
            "d_Ob": d_Ob_fix, "d_M": d_M, "d_fund": d_fund, "d_eff": d_eff,
            "E_ovl": stats["E_ovl"], "E_td": stats["E_td"], "E_S": stats["E_S"],
            "E_td*sqrt(d_M)": stats["E_td"] * math.sqrt(d_M),
        })
    dM_df = pd.DataFrame(dM_rows)
    print(dM_df.to_string(index=False))
    dM_df.to_csv(os.path.join(out_dir, "phase2_dM_scan.csv"), index=False)

    fit_dM = fit_power_law(dM_df["d_M"].values, dM_df["E_td"].values)
    dM_scaling_ok = abs(fit_dM["alpha"] + 0.5) <= 0.15 and fit_dM["R2"] > 0.9

    eovl_ok = all(
        abs(all_fits[n]["E_ovl"]["alpha"] + 1.0) <= 0.10 and all_fits[n]["E_ovl"]["R2"] > 0.9
        for n in all_fits
    )
    td_saturated = all(abs(all_fits[n]["E_td"]["alpha"]) <= 0.15 for n in all_fits)
    S_saturated = all(abs(all_fits[n]["E_S"]["alpha"]) <= 0.15 for n in all_fits)

    checks = [
        ("E_ovl exponent ~ -1 in all configs (HUZ prediction)", eovl_ok),
        ("E_td saturates in d_Ob", td_saturated),
        ("E_S saturates in d_Ob", S_saturated),
        ("E_td ~ 1/sqrt(d_M) at fixed (d_Ob, r)", dM_scaling_ok),
    ]
    all_pass = True
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
        all_pass = all_pass and ok
    if all_pass:
        print("\nPhase 2 gate PASSED.")
    else:
        print("\nPhase 2 gate NOT PASSED.")
    print("=" * 78)
    return all_pass


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
