# vn_algebra: a finite-dim von Neumann algebra toolkit

Quick library built in one session to address whether the three missing pieces of algebraic QFT tooling could be built. Answer: two of three in finite dimensions, and one of those two approximates the physically interesting thing.

## What got built and what works

### `vnalgebra.py` — core library

Functions that work and are tested:

- **`commutant(generators, dim)`** — Given a set of operators, computes the commutant $\mathcal{M}'$ as a basis of matrices. Algorithm: solve the linear system $[A_i, B] = 0$ for all generators $A_i$, returning a null-space basis for $B$.

- **`algebra_closure(generators, dim)`** — Generates the $*$-algebra closure of a set of operators. This gives a basis for the von Neumann algebra $\mathcal{M}$.

- **`is_cyclic_separating(Omega, algebra_basis, dim)`** — Checks whether a vector is cyclic and separating for a given algebra. Cyclic: $\mathcal{M}\Omega$ spans $\mathcal{H}$. Separating: $a \mapsto a\Omega$ is injective.

- **`tomita_takesaki(algebra_basis, Omega, dim)`** — The main construction. Given a cyclic separating vector, returns the modular operator $\Delta$, modular conjugation $J$, and modular Hamiltonian $K = -\log\Delta$. All consistency checks ($S^2 = I$, $J$ antiunitary, $\Delta$ Hermitian positive) pass to $10^{-15}$.

- **`modular_flow(Delta, a, t)`** — Applies $\sigma_t(a) = \Delta^{it} a \Delta^{-it}$.

- **`algebra_type_finite_dim(algebra_basis, dim)`** — Reports structure in finite dim. In finite dim the answer is always Type I (since all finite-dim von Neumann algebras are direct sums of matrix algebras). The function reports the commutant dim, center dim, and whether the algebra is a factor.

### Tested cases

**Test 1: Two-qubit algebra with maximally entangled state.**
- $\mathcal{M} = \{A \otimes I : A \in M_2(\mathbb{C})\}$, $\Omega = (|00\rangle + |11\rangle)/\sqrt{2}$
- Result: $\Delta = I$ (all eigenvalues 1), modular flow trivial — correct for a tracial state.
- All Tomita-Takesaki consistency checks pass to $\sim 10^{-15}$.

**Test 2: Same algebra with TFD state at $\beta = 1.5$.**
- $\Omega_\mathrm{TFD} \propto e^{-\beta/2}|00\rangle + e^{\beta/2}|11\rangle$
- Result: $\Delta$ eigenvalues $\{e^{-2\beta}, 1, 1, e^{+2\beta}\}$, ratio $e^{4\beta}$ — matches theory.
- Modular Hamiltonian $K$: eigenvalues $\{-3, 0, 0, +3\}$, matching $\pm 2\beta$.

### `crossed_product.py` — crossed products

- **`crossed_product_Zn(...)`** — Builds $\mathcal{M} \rtimes_\alpha \mathbb{Z}_n$.
- **`verify_covariance(...)`** — Checks $U\pi(a)U^{-1} = \pi(\alpha(a))$.

### `trace_on_crossed.py` — the physics content

Demonstrates that the crossed product carries a canonical trace and that entropies are well-defined with respect to it.

## Honest summary

**For someone doing actual CLPW-style research:**

The library is useful as a sanity-checker. It does NOT replace pen-and-paper work in the infinite-dim case. The physically interesting phenomenon — Type III → Type II under crossed product with modular flow — is invisible in finite dim because finite-dim algebras are trivially Type I.

## Natural next steps

1. **Free field algebras.** Implement creation/annihilation operators on a Fock space.
2. **Type II_1 factor via Jones tower.** Construct as inductive limit of matrix algebras.
3. **Connes cocycle.** Given two states, compute the Connes cocycle unitary.
