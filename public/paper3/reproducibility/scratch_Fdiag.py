"""Verify the diagonal-to-bulk replacement error F_diag is subleading.
F_diag = [H(diag rho_RA) - H(diag rho_RB)] - [H(P_A) - H(P_B)]
where P_X = diag(rho_X^bulk) = bulk-marginal block masses p_X^a, and
diag(rho_RX) = actual reduced-state diagonal. Check E[F_diag^2] vs signal ~ 1/(d^3 d_M^2)."""
import numpy as np
from scipy.stats import unitary_group
rng=np.random.default_rng(707070)
def shannon(p): p=np.real(p); p=p[p>1e-15]; return -np.sum(p*np.log(p))
def haar_bulk(d,dM):
    n=d*d*dM; z=rng.standard_normal(n)+1j*rng.standard_normal(n); return (z/np.linalg.norm(z)).reshape(d,d,dM)
def reduced_diag(psi,d,dM,V):  # actual diag of rho_RA and rho_RB (observer A traces R_B; B traces R_A)
    Vt=V.reshape(V.shape[0],d,d,dM); Z=np.real(np.vdot(V@psi.reshape(-1),V@psi.reshape(-1)))
    dA=np.array([np.real(sum(np.vdot(Vt[:,a,b,:]@psi[a,b,:],Vt[:,a,b,:]@psi[a,b,:]) for b in range(d))) for a in range(d)])/Z
    dB=np.array([np.real(sum(np.vdot(Vt[:,a,b,:]@psi[a,b,:],Vt[:,a,b,:]@psi[a,b,:]) for a in range(d)) ) for b in range(d)])/Z
    return dA,dB
print(f"{'d':>2} {'E[F_diag^2]':>13} {'signal~1/d^3dM^2':>16} {'ratio':>8} {'F_diag^2*d^4dM^2':>16}")
for d in [4,5,6]:
    dM=4; deff=d*d*dM; r=deff//2; M=400; F2=[]
    for _ in range(M):
        psi=haar_bulk(d,dM)
        pab=(np.abs(psi)**2).sum(2); pA=pab.sum(1); pB=pab.sum(0)  # bulk-marginal diagonals P_A,P_B
        U=unitary_group.rvs(deff,random_state=rng); V=U[:r,:]
        dA,dB=reduced_diag(psi,d,dM,V)  # actual diagonals
        Fdiag=(shannon(dA)-shannon(dB)) - (shannon(pA)-shannon(pB))
        F2.append(Fdiag**2)
    eF2=np.mean(F2); sig=1/(d**3*dM**2)
    print(f"{d:>2} {eF2:>13.3e} {sig:>16.3e} {eF2/sig:>8.4f} {eF2*d**4*dM**2:>16.3f}")

# --- verify diagonal-fluctuation variance scaling for Lemma C.6a ---
print("\n=== eta-variance: sum_a E[(eta_a)^2] vs d^-4 d_M^-1 ===")
print(f"{'d':>2} {'sum_a Var(eta)':>15} {'*d^4 d_M':>10}")
for d in [4,5,6]:
    dM=4; deff=d*d*dM; r=deff//2; M=400; acc=np.zeros(d)
    accsq=np.zeros(d); cnt=0
    for _ in range(M):
        psi=haar_bulk(d,dM); pab=(np.abs(psi)**2).sum(2); pA=pab.sum(1)
        U=unitary_group.rvs(deff,random_state=rng); V=U[:r,:]
        dA,_=reduced_diag(psi,d,dM,V)
        eta=dA-pA; acc+=eta; accsq+=eta**2; cnt+=1
    sumvar=np.sum(accsq/cnt - (acc/cnt)**2)
    print(f"{d:>2} {sumvar:>15.3e} {sumvar*d**4*dM:>10.3f}")
