"""Check the conditional covariance matrix M_{aa'}=Cov_V(eta_a,eta_a'|psi) is
diagonal-dominant, so delta^T M delta ~ sum_a delta_a^2 M_aa (the clean d^-4 route)."""
import numpy as np
from scipy.stats import unitary_group
rng=np.random.default_rng(707070)
def reduced_diagA(psi,d,dM,V):
    Vt=V.reshape(V.shape[0],d,d,dM); Z=np.real(np.vdot(V@psi.reshape(-1),V@psi.reshape(-1)))
    return np.array([np.real(sum(np.vdot(Vt[:,a,b,:]@psi[a,b,:],Vt[:,a,b,:]@psi[a,b,:]) for b in range(d))) for a in range(d)])/Z
print(f"{'d':>2} {'mean|M_aa|':>11} {'mean|M_offd|':>12} {'ratio off/diag':>14} {'lam_max/M_aa':>13}")
for d in [4,5,6]:
    dM=4; deff=d*d*dM; r=deff//2; nV=600
    # fix one psi (Haar), sample V to estimate M conditional on psi
    z=rng.standard_normal(d*d*dM)+1j*rng.standard_normal(d*d*dM); psi=(z/np.linalg.norm(z)).reshape(d,d,dM)
    pab=(np.abs(psi)**2).sum(2); pA=pab.sum(1)
    H=[]
    for _ in range(nV):
        U=unitary_group.rvs(deff,random_state=rng); V=U[:r,:]
        H.append(reduced_diagA(psi,d,dM,V)-pA)
    H=np.array(H); M=np.cov(H.T)
    diag=np.mean(np.abs(np.diag(M)))
    off=np.mean(np.abs(M[~np.eye(d,dtype=bool)]))
    lam=np.max(np.linalg.eigvalsh(M))
    print(f"{d:>2} {diag:>11.3e} {off:>12.3e} {off/diag:>14.3f} {lam/diag:>13.3f}")
