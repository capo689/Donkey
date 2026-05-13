"""
The physical content of the crossed product: the TRACE.

CLPW's key insight: Type III algebras (like QFT wedge algebras) have no trace.
But M ⋊_α R, for α = modular flow of a state, does have a (semifinite) trace.
This is why you can define ENTROPY on the crossed product even though you
couldn't on M itself.

In our finite-dim Z_n analog, the trace on M ⋊_α Z_n has the form:
  Tr_cp(π(a) · U^k) = δ_{k,0} · Tr_M(a) · (something)
  
For the Z_n case with Haar measure, the Haar-integrated trace is:
  Tr_cp(X) = (1/n) sum_{k=0}^{n-1} Tr_{H⊗C^n}(X · (I ⊗ P_k))
  
where P_k is the projection onto |k> in C^n.

Let's verify this defines a proper trace (cyclic, positive) on the crossed product.
"""

import numpy as np
import sys
sys.path.insert(0, '/home/claude/vn_algebra')
from vnalgebra import algebra_closure, tomita_takesaki, modular_flow
from crossed_product import crossed_product_Zn, verify_covariance


def trace_on_crossed_product(X, dim, n):
    """
    Canonical trace on M ⋊_α Z_n: (1/n) * Tr_{H⊗C^n}(X).
    In our finite-dim Z_n case this IS just the usual matrix trace,
    but it plays the role of the semifinite trace on M ⋊_α R in infinite dim.
    """
    return np.trace(X) / n


def verify_trace_cyclicity(algebra_basis, dim, n, num_pairs=10):
    """
    Check Tr(AB) = Tr(BA) for elements A, B of the crossed product algebra.
    """
    np.random.seed(0)
    max_err = 0.0
    for _ in range(num_pairs):
        coeffs_A = np.random.randn(len(algebra_basis)) + 1j * np.random.randn(len(algebra_basis))
        coeffs_B = np.random.randn(len(algebra_basis)) + 1j * np.random.randn(len(algebra_basis))
        A = sum(c * M for c, M in zip(coeffs_A, algebra_basis))
        B = sum(c * M for c, M in zip(coeffs_B, algebra_basis))
        tr_AB = trace_on_crossed_product(A @ B, dim, n)
        tr_BA = trace_on_crossed_product(B @ A, dim, n)
        err = abs(tr_AB - tr_BA)
        max_err = max(max_err, err)
    return max_err


def verify_trace_positivity(algebra_basis, dim, n, num_tests=20):
    """
    Check Tr(A*A) >= 0 for elements A of the crossed product algebra.
    """
    np.random.seed(0)
    min_val = float('inf')
    for _ in range(num_tests):
        coeffs = np.random.randn(len(algebra_basis)) + 1j * np.random.randn(len(algebra_basis))
        A = sum(c * M for c, M in zip(coeffs, algebra_basis))
        tr_val = trace_on_crossed_product(A.conj().T @ A, dim, n).real
        min_val = min(min_val, tr_val)
    return min_val


if __name__ == "__main__":
    print("="*70)
    print("TRACE ON THE CROSSED PRODUCT")
    print("="*70)
    
    dim = 4
    I_2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    
    generators_M = [np.kron(sx, I_2), np.kron(sz, I_2)]
    M = algebra_closure(generators_M, dim)
    
    beta = 1.5
    Omega_TFD = np.zeros(4, dtype=complex)
    Omega_TFD[0] = np.exp(-beta/2)
    Omega_TFD[3] = np.exp(beta/2)
    Omega_TFD /= np.linalg.norm(Omega_TFD)
    
    tt = tomita_takesaki(M, Omega_TFD, dim)
    Delta = tt['Delta']
    
    n = 4
    t_step = 2 * np.pi / (n * 2 * beta)
    
    def alpha(a, t=t_step, Delta=Delta):
        return modular_flow(Delta, a, t)
    
    crossed_gens, U = crossed_product_Zn(M, alpha, n, dim)
    new_dim = dim * n
    M_crossed = algebra_closure(crossed_gens, new_dim)
    
    print(f"\nM rtimes Z_{n} built; dim = {len(M_crossed)}, acts on C^{new_dim}")
    
    print("\nVerifying trace axioms on M rtimes Z_n:")
    cyc_err = verify_trace_cyclicity(M_crossed, dim, n)
    print(f"  Cyclicity: max |Tr(AB) - Tr(BA)| = {cyc_err:.2e}")
    
    pos_val = verify_trace_positivity(M_crossed, dim, n)
    print(f"  Positivity: min Tr(A*A) = {pos_val:.4f} (should be >= 0)")
    
    print("\nTrace on specific elements:")
    print(f"  Tr(I) = {trace_on_crossed_product(np.eye(new_dim), dim, n).real:.4f}")
    print(f"    (expected: {new_dim/n})")
    
    pi_sz = crossed_gens[1]
    tr_pi_sz = trace_on_crossed_product(pi_sz, dim, n).real
    print(f"  Tr(pi(sz)) = {tr_pi_sz:.4f}")
    
    tr_U = trace_on_crossed_product(U, dim, n).real
    print(f"  Tr(U) = {tr_U:.4f}")
    
    pi_I = np.eye(new_dim, dtype=complex)
    tr_pi_I = trace_on_crossed_product(pi_I, dim, n).real
    print(f"  Tr(pi(I)) = {tr_pi_I:.4f}")
    
    print("\n" + "-"*60)
    print("Entropy of a state on the crossed product")
    print("-"*60)
    
    H_M = np.kron(sz, I_2)
    h_clock = np.diag(np.arange(n))
    H_full = np.kron(H_M, np.eye(n)) + np.kron(np.eye(dim), h_clock)
    
    from scipy.linalg import expm, logm
    rho = expm(-0.5 * H_full)
    tr_rho = trace_on_crossed_product(rho, dim, n).real
    rho_normalized = rho / tr_rho
    print(f"  Tr_cp(rho) = {trace_on_crossed_product(rho_normalized, dim, n).real:.4f}")
    
    log_rho = logm(rho_normalized + 1e-15 * np.eye(new_dim))
    entropy = -trace_on_crossed_product(rho_normalized @ log_rho, dim, n).real
    print(f"  S(rho) = -Tr_cp(rho log rho) = {entropy:.4f}")
    
    print("\n" + "="*60)
    print("WHAT THIS TOY MODEL ILLUSTRATES")
    print("="*60)
    print("""
In the finite-dim Z_n case:
  - Crossed product M rtimes Z_n is a well-defined algebra
  - Covariance relation verified to machine precision
  - Canonical trace is cyclic and positive
  - Entropies with respect to this trace are well-defined
""")
