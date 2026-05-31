"""
bh_lab_backend.py

Self-contained foundation library for the BH observer-complementarity
research program. Provides the API used by phase1_rules_canonical.py and
phase2_huz_verification.py.

This module is intentionally written to be free-standing: it uses only
numpy and the Python standard library. It can be run directly as a
self-test (`python bh_lab_backend.py`).

Exports:
  SeededRNG                       - reproducible Haar-random sampling
  huz_single_observer_entropy     - HUZ (2501.02359) observer rule, single observer
  colorado_single_observer_entropy- Colorado (2503.09681) observer rule
  apply_huz_single                - HUZ map, raw unnormalized output
  partial_trace                   - partial-trace utility for density matrices
  von_neumann_entropy             - von Neumann entropy of a density matrix
  aehpv_map                       - standalone Haar-projector constructor

Conventions:
  - Bulk state psi_bulk lives on H_Ob (x) H_M with dim d_Ob*d_M; the
    ordering is psi_bulk[o*d_M + m] = psi(o, m).
  - The HUZ map clones the observer label into a reference register R of
    dimension d_Ob, then applies V to the (Ob, M) factors:
        psi(o,m)  ->  sum_{o,m} psi(o,m) |o>_R (x) V|o,m>_fund
    The output state lives on H_fund (x) H_R with the convention
    psi_out[f*d_Ob + o] = sum_m psi(o,m) V[f, o*d_M + m].
  - V is taken as the first d_fund rows of a Haar-random unitary on
    U(d_eff) where d_eff = d_Ob * d_M. (This is the "aehpv_map" in
    AEHPV 2207.06536.)
"""

from __future__ import annotations

import math
import numpy as np


__all__ = [
    "SeededRNG",
    "huz_single_observer_entropy",
    "colorado_single_observer_entropy",
    "apply_huz_single",
    "partial_trace",
    "von_neumann_entropy",
    "aehpv_map",
]


# ----------------------------------------------------------------------------
# SeededRNG: deterministic Haar sampling
# ----------------------------------------------------------------------------

class SeededRNG:
    """Deterministic random sampler for Haar measure and complex Gaussians.

    Parameters
    ----------
    seed : int
        Integer seed for reproducibility.
    """

    def __init__(self, seed: int):
        self.seed = int(seed)
        self._rng = np.random.default_rng(self.seed)

    def standard_complex(self, shape):
        """Standard complex Gaussian: real and imag parts iid N(0, 1)."""
        re = self._rng.standard_normal(shape)
        im = self._rng.standard_normal(shape)
        return re + 1j * im

    def haar_unitary(self, d: int) -> np.ndarray:
        """Haar-random unitary on U(d), via QR of complex Gaussian.

        Uses the Mezzadri (2007) phase-correction trick: take QR of a
        d x d standard complex Gaussian, then diagonally rephase to
        get the correct Haar measure on U(d).
        """
        Z = self.standard_complex((d, d))
        Q, R = np.linalg.qr(Z)
        D = np.diag(R) / np.abs(np.diag(R))
        return Q * D[np.newaxis, :]

    def aehpv_map(self, d_eff: int, d_fund: int) -> np.ndarray:
        """Random non-isometric map V: H_eff -> H_fund.

        Constructed as the first d_fund rows of a Haar-random unitary on
        U(d_eff). V is d_fund x d_eff. The matrix V V^dagger = I_fund
        exactly (rows are orthonormal); V^dagger V is a random rank-d_fund
        orthogonal projector on H_eff (this is the AEHPV non-isometric
        encoding map at the "raw" level, before any additional cloning).
        """
        if d_fund > d_eff:
            raise ValueError(f"d_fund ({d_fund}) must be <= d_eff ({d_eff})")
        U = self.haar_unitary(d_eff)
        return U[:d_fund, :]

    def haar_state(self, d: int) -> np.ndarray:
        """Haar-random pure state on C^d (unit-norm complex vector)."""
        psi = self.standard_complex(d)
        psi /= np.linalg.norm(psi)
        return psi


# ----------------------------------------------------------------------------
# Standalone aehpv_map (module-level convenience function)
# ----------------------------------------------------------------------------

def aehpv_map(d_eff: int, d_fund: int, seed: int | None = None) -> np.ndarray:
    """Convenience wrapper: random non-isometric map V: H_eff -> H_fund.

    If seed is None, uses numpy's default RNG state (not reproducible).
    For reproducible sampling, use SeededRNG(seed).aehpv_map(...).
    """
    if seed is not None:
        return SeededRNG(seed=seed).aehpv_map(d_eff, d_fund)
    rng = np.random.default_rng()
    Z = rng.standard_normal((d_eff, d_eff)) + 1j * rng.standard_normal((d_eff, d_eff))
    Q, R = np.linalg.qr(Z)
    D = np.diag(R) / np.abs(np.diag(R))
    U = Q * D[np.newaxis, :]
    return U[:d_fund, :]


# ----------------------------------------------------------------------------
# Density-matrix utilities
# ----------------------------------------------------------------------------

def von_neumann_entropy(rho: np.ndarray, eps: float = 1e-12) -> float:
    """Von Neumann entropy in nats: S(rho) = -tr(rho log rho).

    Handles small eigenvalues by clipping below eps.
    """
    rho_h = 0.5 * (rho + rho.conj().T)  # symmetrize numerically
    e = np.linalg.eigvalsh(rho_h)
    e = e[e > eps]
    if e.size == 0:
        return 0.0
    return float(-np.sum(e * np.log(e)))


def partial_trace(rho: np.ndarray, dims: list[int], keep: list[int]) -> np.ndarray:
    """Partial trace of a density matrix over arbitrary subsystem indices.

    Parameters
    ----------
    rho : 2D array of shape (D, D), where D = prod(dims).
    dims : list of subsystem dimensions, in the order they appear in the
           tensor-product factorization.
    keep : list of subsystem indices (0-indexed into `dims`) to KEEP.

    Returns
    -------
    rho_kept : reduced density matrix on the kept subsystems.

    Convention: the basis ordering is row-major / standard kron, i.e.
    |i_0, i_1, ..., i_{n-1}> with the rightmost index varying fastest.
    """
    n = len(dims)
    D = int(np.prod(dims))
    assert rho.shape == (D, D), f"rho shape {rho.shape} doesn't match dims {dims}"

    keep_set = set(keep)
    trace_indices = [k for k in range(n) if k not in keep_set]
    keep_indices = list(keep)

    # Reshape rho to a 2n-dim tensor: rho[i_0, ..., i_{n-1}, j_0, ..., j_{n-1}]
    rho_t = rho.reshape(dims + dims)

    # Contract over traced subsystems: equate i_k = j_k and sum
    # Use einsum with shared labels for traced pairs and distinct labels for kept.
    n_keep = len(keep_indices)
    row_labels = ["a" + str(k) if k in keep_set else "t" + str(k) for k in range(n)]
    col_labels = ["b" + str(k) if k in keep_set else "t" + str(k) for k in range(n)]
    in_subscript = "".join(_label_to_einsum(L) for L in (row_labels + col_labels))
    out_row = "".join(_label_to_einsum("a" + str(k)) for k in keep_indices)
    out_col = "".join(_label_to_einsum("b" + str(k)) for k in keep_indices)
    out_subscript = out_row + out_col
    out = np.einsum(f"{in_subscript}->{out_subscript}", rho_t)

    d_keep = int(np.prod([dims[k] for k in keep_indices]))
    return out.reshape(d_keep, d_keep)


_label_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def _label_to_einsum(label: str) -> str:
    """Map a string label to a unique single character for einsum.
    Uses a small registry; raises if too many distinct labels."""
    if not hasattr(_label_to_einsum, "_registry"):
        _label_to_einsum._registry = {}
    reg = _label_to_einsum._registry
    if label not in reg:
        if len(reg) >= len(_label_chars):
            raise RuntimeError("Too many distinct partial-trace labels")
        reg[label] = _label_chars[len(reg)]
    return reg[label]


# ----------------------------------------------------------------------------
# HUZ observer rule (Harlow-Usatyuk-Zhao 2501.02359)
# ----------------------------------------------------------------------------

def apply_huz_single(psi_bulk: np.ndarray, V: np.ndarray,
                     d_Ob: int, d_M: int) -> np.ndarray:
    """Apply the HUZ single-observer cloning + V map.

    Parameters
    ----------
    psi_bulk : 1D array of length d_Ob * d_M.
        Bulk state in the Ob (x) M factorization.
        Convention: psi_bulk[o*d_M + m] = psi(o, m).
    V : 2D array of shape (d_fund, d_Ob * d_M).
        Non-isometric map from H_eff to H_fund.
    d_Ob, d_M : int
        Subsystem dimensions.

    Returns
    -------
    psi_out : 1D array of length d_fund * d_Ob.
        Unnormalized output state on H_fund (x) H_R.
        psi_out[f*d_Ob + o] = sum_m psi(o,m) V[f, o*d_M + m].
    """
    d_fund = V.shape[0]
    assert V.shape[1] == d_Ob * d_M, "V shape inconsistent with d_Ob*d_M"
    assert psi_bulk.shape == (d_Ob * d_M,), "psi_bulk shape inconsistent"

    psi_t = psi_bulk.reshape(d_Ob, d_M)  # psi_t[o, m]

    # psi_out[f, o] = sum_m psi(o, m) V[f, o*d_M + m]
    V_t = V.reshape(d_fund, d_Ob, d_M)  # V_t[f, o, m]
    psi_out = np.einsum("om, fom -> fo", psi_t, V_t)  # shape (d_fund, d_Ob)
    return psi_out.reshape(-1)


def huz_single_observer_entropy(psi_bulk: np.ndarray, V: np.ndarray,
                                d_Ob: int, d_M: int) -> tuple[float, np.ndarray]:
    """HUZ single-observer entropy: S(rho_R) where R is the cloning register.

    Returns (S, rho_R).
    """
    psi_out = apply_huz_single(psi_bulk, V, d_Ob, d_M)
    norm_sq = float(np.vdot(psi_out, psi_out).real)
    if norm_sq < 1e-30:
        return 0.0, np.zeros((d_Ob, d_Ob), dtype=complex)
    psi_norm = psi_out / math.sqrt(norm_sq)
    d_fund = V.shape[0]
    rho_full = np.outer(psi_norm, psi_norm.conj())
    rho_R = partial_trace(rho_full, dims=[d_fund, d_Ob], keep=[1])
    S = von_neumann_entropy(rho_R)
    return S, rho_R


# ----------------------------------------------------------------------------
# Colorado observer rule (Akers-Bueller-DeWolfe-Higginbotham-Reinking-Rodriguez 2503.09681)
# ----------------------------------------------------------------------------

def colorado_single_observer_entropy(psi_bulk: np.ndarray, V_M: np.ndarray,
                                      d_Ob: int) -> tuple[float, np.ndarray]:
    """Colorado single-observer entropy.

    The Colorado rule applies a non-isometric map V_M only to the matter
    sector (not the observer sector), then takes the entropy of the
    reduced state on the observer subsystem.

    Parameters
    ----------
    psi_bulk : 1D array of length d_Ob * d_M.
        Bulk state with psi_bulk[o*d_M + m] = psi(o, m).
    V_M : 2D array of shape (d_fundM, d_M).
        Non-isometric map on the matter sector.
    d_Ob : int
        Observer dimension.

    Returns
    -------
    (S, rho_Ob) : entropy and reduced observer density matrix.
    """
    d_M = V_M.shape[1]
    d_fundM = V_M.shape[0]
    assert psi_bulk.shape == (d_Ob * d_M,), "psi_bulk shape inconsistent"

    psi_t = psi_bulk.reshape(d_Ob, d_M)  # psi_t[o, m]
    # Apply V_M to matter only: psi_out[o, fm] = sum_m V_M[fm, m] psi(o, m)
    psi_out_t = np.einsum("fm, om -> of", V_M, psi_t)  # shape (d_Ob, d_fundM)
    psi_out = psi_out_t.reshape(-1)
    norm_sq = float(np.vdot(psi_out, psi_out).real)
    if norm_sq < 1e-30:
        return 0.0, np.zeros((d_Ob, d_Ob), dtype=complex)
    psi_norm = psi_out / math.sqrt(norm_sq)
    rho_full = np.outer(psi_norm, psi_norm.conj())
    rho_Ob = partial_trace(rho_full, dims=[d_Ob, d_fundM], keep=[0])
    S = von_neumann_entropy(rho_Ob)
    return S, rho_Ob


# ----------------------------------------------------------------------------
# Self-test
# ----------------------------------------------------------------------------

def _self_test():
    """Run a few sanity checks on the backend. Exit code 0 if all pass."""
    import sys
    print("bh_lab_backend.py — self-test")
    print("-" * 60)

    rng = SeededRNG(seed=42)

    # Test 1: Haar unitary unitarity
    U = rng.haar_unitary(8)
    err = np.max(np.abs(U @ U.conj().T - np.eye(8)))
    ok1 = err < 1e-10
    print(f"  [1] haar_unitary unitarity:       err = {err:.3e}  {'OK' if ok1 else 'FAIL'}")

    # Test 2: aehpv_map rows orthonormal
    V = rng.aehpv_map(d_eff=16, d_fund=8)
    err = np.max(np.abs(V @ V.conj().T - np.eye(8)))
    ok2 = err < 1e-10
    print(f"  [2] aehpv_map row orthonormality: err = {err:.3e}  {'OK' if ok2 else 'FAIL'}")

    # Test 3: haar_state norm
    psi = rng.haar_state(20)
    n = abs(np.vdot(psi, psi).real - 1.0)
    ok3 = n < 1e-12
    print(f"  [3] haar_state unit norm:         err = {n:.3e}  {'OK' if ok3 else 'FAIL'}")

    # Test 4: HUZ single-observer on product state — entropy in [0, log(d_Ob)]
    psi_a = rng.haar_state(3); psi_a /= np.linalg.norm(psi_a)
    psi_b = rng.haar_state(4); psi_b /= np.linalg.norm(psi_b)
    psi_prod = np.kron(psi_a, psi_b)
    V_prod = rng.aehpv_map(d_eff=12, d_fund=6)
    S_prod, rho_R = huz_single_observer_entropy(psi_prod, V_prod, d_Ob=3, d_M=4)
    # For HUZ cloning, the state |sum_o psi_a(o)|o>_R |o>_Ob |psi_b>_M post-V has
    # rho_R of rank up to d_Ob = 3, so 0 <= S <= log(3). Check trace = 1 too.
    tr = np.trace(rho_R).real
    ok4 = (0.0 <= S_prod <= math.log(3) + 1e-6) and (abs(tr - 1.0) < 1e-10)
    print(f"  [4] HUZ on product state: S = {S_prod:.4f} in [0, log(3)={math.log(3):.4f}], tr(rho_R) = {tr:.6f}  {'OK' if ok4 else 'FAIL'}")

    # Test 5: Colorado on product state — rho_Ob should be pure (rank 1, S=0)
    psi_prod = np.kron(psi_a, psi_b)
    V_M = rng.aehpv_map(d_eff=4, d_fund=2)
    S_col, rho_Ob = colorado_single_observer_entropy(psi_prod, V_M, d_Ob=3)
    # Colorado: V_M acts only on M, so the post-V state is psi_a ⊗ (V_M psi_b),
    # still a product state on Ob ⊗ fundM. rho_Ob = |psi_a><psi_a|, pure, S=0.
    ok5 = S_col < 1e-8
    print(f"  [5] Colorado on product state: S = {S_col:.3e}  {'OK (S=0)' if ok5 else 'FAIL'}")

    # Test 6: partial_trace identity check
    rho_a = np.outer(psi_a, psi_a.conj())
    rho_b = np.outer(psi_b, psi_b.conj())
    rho_ab = np.kron(rho_a, rho_b)
    rho_a_recovered = partial_trace(rho_ab, dims=[3, 4], keep=[0])
    err6 = np.max(np.abs(rho_a_recovered - rho_a))
    ok6 = err6 < 1e-12
    print(f"  [6] partial_trace recovers marginals: err = {err6:.3e}  {'OK' if ok6 else 'FAIL'}")

    # Test 7: von Neumann entropy of maximally mixed
    d = 8
    rho_mix = np.eye(d) / d
    S_mix = von_neumann_entropy(rho_mix)
    err7 = abs(S_mix - math.log(d))
    ok7 = err7 < 1e-10
    print(f"  [7] vN entropy of I/{d}: S = {S_mix:.6f}, expected log({d}) = {math.log(d):.6f}, err = {err7:.3e}  {'OK' if ok7 else 'FAIL'}")

    # Test 8: HUZ on entangled bulk state — finite entropy
    psi_ent = rng.haar_state(12)
    V_ent = rng.aehpv_map(d_eff=12, d_fund=6)
    S_ent, _ = huz_single_observer_entropy(psi_ent, V_ent, d_Ob=3, d_M=4)
    ok8 = 0.0 <= S_ent <= math.log(3) + 1e-6
    print(f"  [8] HUZ on entangled state: S = {S_ent:.4f} in [0, log(3)] = [0, {math.log(3):.4f}]  {'OK' if ok8 else 'FAIL'}")

    all_ok = all([ok1, ok2, ok3, ok4, ok5, ok6, ok7, ok8])
    print("-" * 60)
    print(f"  RESULT: {'ALL PASS' if all_ok else 'SOME FAIL'}")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    _self_test()
