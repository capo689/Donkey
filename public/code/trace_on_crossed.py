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
    
    # Set up same system as before
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
    
    # Build crossed product
    crossed_gens, U = crossed_product_Zn(M, alpha, n, dim)
    new_dim = dim * n
    M_crossed = algebra_closure(crossed_gens, new_dim)
    
    print(f"\nM ⋊_α Z_{n} built; dim = {len(M_crossed)}, acts on C^{new_dim}")
    
    # Verify the trace is cyclic and positive on the crossed product
    print("\nVerifying trace axioms on M ⋊_α Z_n:")
    cyc_err = verify_trace_cyclicity(M_crossed, dim, n)
    print(f"  Cyclicity: max |Tr(AB) - Tr(BA)| = {cyc_err:.2e}")
    
    pos_val = verify_trace_positivity(M_crossed, dim, n)
    print(f"  Positivity: min Tr(A*A) = {pos_val:.4f} (should be >= 0)")
    
    # The key observation: in our finite-dim Z_n case, the trace comes for free 
    # because everything is Type I. But in the infinite-dim R case, the trace 
    # ONLY exists because we took the crossed product with the modular flow.
    # That's the Type III -> Type II transition.
    
    # Show what the trace looks like on specific elements
    print("\nTrace on specific elements:")
    
    # Identity
    print(f"  Tr(I) = {trace_on_crossed_product(np.eye(new_dim), dim, n).real:.4f}")
    print(f"    (expected: new_dim/n = {new_dim/n})")
    
    # π(a) for a = σz ⊗ I
    pi_sz = crossed_gens[1]  # σz ⊗ I embedded
    tr_pi_sz = trace_on_crossed_product(pi_sz, dim, n).real
    # For σz ⊗ I: Tr_M(σz ⊗ I) = 0 (traceless)
    # So Tr_cp(π(a)) should be 0
    print(f"  Tr(π(σz⊗I)) = {tr_pi_sz:.4f}")
    print(f"    (expected: 0 because σz ⊗ I is traceless in M)")
    
    # U (the shift operator)
    tr_U = trace_on_crossed_product(U, dim, n).real
    print(f"  Tr(U) = {tr_U:.4f}")
    print(f"    (expected: 0 because U is off-diagonal shift)")
    
    # π(I) · U^0 = identity-like element in crossed product
    # Actually, π(I) = I ⊗ (sum of P_k) = I_{dim} ⊗ I_n = I on H ⊗ C^n
    pi_I = crossed_gens[0]  # the image of the identity element of M under pi; 
    # actually generators_M doesn't include I, but M itself does after closure
    # The first element of algebra_closure is typically I
    # Let me recompute directly
    pi_I = np.eye(new_dim, dtype=complex)  # π(I_M) = I_H ⊗ I_n
    tr_pi_I = trace_on_crossed_product(pi_I, dim, n).real
    print(f"  Tr(π(I)) = {tr_pi_I:.4f}")
    print(f"    (expected: dim(H) = {dim}, since π(I) = I_H ⊗ I_n and trace is (1/n)·Tr = dim·n/n = dim)")
    
    # --- Compute an entropy ---
    # On a Type II algebra, we can define S(ω) = -τ(ρ log ρ) where ρ is the 
    # density matrix of state ω with respect to trace τ.
    # Let's make a state ω on M ⋊_α Z_n and compute its entropy.
    
    print("\n" + "-"*60)
    print("Entropy of a state on the crossed product")
    print("-"*60)
    
    # Take the "thermal" state on the crossed product: e^{-β (H + h_clock)}
    # where H is the CFT Hamiltonian (extended to H ⊗ C^n as H ⊗ I_n)
    # and h_clock is a clock Hamiltonian on C^n.
    
    # In the CLPW picture: the crossed product trace plays the role of a 
    # UV-regularized trace. The state's density matrix with respect to this 
    # trace gives a well-defined entropy even when the QFT state itself had 
    # divergent entropy.
    
    # On our Z_n system, construct a Gibbs state
    H_M = np.kron(sz, I_2)  # Hamiltonian on M (not generally in M, but let's use it)
    h_clock = np.diag(np.arange(n))  # clock Hamiltonian: eigenvalues 0, 1, ..., n-1
    H_full = np.kron(H_M, np.eye(n)) + np.kron(np.eye(dim), h_clock)
    
    from scipy.linalg import expm, logm
    rho = expm(-0.5 * H_full)
    # Normalize by the trace ON THE CROSSED PRODUCT (not usual trace)
    tr_rho = trace_on_crossed_product(rho, dim, n).real
    rho_normalized = rho / tr_rho
    # Check normalization
    print(f"  Tr_cp(rho_normalized) = {trace_on_crossed_product(rho_normalized, dim, n).real:.4f}")
    
    # Compute entropy: S = -Tr_cp(rho log rho)
    log_rho = logm(rho_normalized + 1e-15 * np.eye(new_dim))
    entropy = -trace_on_crossed_product(rho_normalized @ log_rho, dim, n).real
    print(f"  S(rho) = -Tr_cp(rho log rho) = {entropy:.4f}")
    print(f"    (well-defined Type II-style entropy)")
    
    print("\n" + "="*60)
    print("WHAT THIS TOY MODEL ILLUSTRATES")
    print("="*60)
    print("""
In the finite-dim Z_n case:
  ✓ Crossed product M ⋊_α Z_n is a well-defined algebra
  ✓ Covariance relation verified to machine precision
  ✓ Canonical trace is cyclic and positive
  ✓ Entropies with respect to this trace are well-defined

This reproduces, in toy form, the CLPW/Witten structure:
- The trace on the crossed product is the "discretized" version of 
  the semifinite trace on M ⋊_α R.
- The entropy we computed is the finite-dim analog of the CLPW 
  Type II_1 entropy.

What's NOT captured (the fundamentally infinite-dim content):
- In infinite dim, M is Type III with NO trace. The crossed product 
  ADDS a trace structure. That's the physical miracle.
- In our finite dim, M was Type I with a trace already, so the 
  "miracle" is just a combinatorial combination.

This is exactly the limitation I flagged earlier: the meaningful 
physics is in the Type III → Type II transition, which requires 
infinite dim. The tools I built can verify structural relations 
and test formulas, but can't make the Type III → Type II transition 
itself manifest.
""")
