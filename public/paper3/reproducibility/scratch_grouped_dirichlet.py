"""Verify the grouped-Dirichlet covariance structure for the Haar bulk marginal.
Haar |psi> on C^{d*d*dM} <=> |psi_abc|^2 ~ Dirichlet(1..1) on D=d^2 dM categories.
p_a = sum_{bc}|psi|^2 (A-marginal block mass), q_b = sum_{ac}|psi|^2 (B-marginal)."""
import numpy as np
rng=np.random.default_rng(707070)
def moments(d,dM,M=200000):
    D=d*d*dM
    # Dirichlet(1..1) via normalized Exp(1); reshape (a,b,c)
    x=rng.standard_exponential((M,d,d,dM)); x/=x.sum(axis=(1,2,3),keepdims=True)
    p=x.sum(axis=(2,3))  # (M,d) A-marginal
    q=x.sum(axis=(1,3))  # (M,d) B-marginal
    TA=(p**2).sum(1); TB=(q**2).sum(1)
    out={}
    out['Var(T_A)']=TA.var(); out['Cov(T_A,T_B)']=np.cov(TA,TB)[0,1]
    out['Var(T_A-T_B)']=(TA-TB).var()
    # off-diagonal Cov(p_a,p_a') a!=a'  and Cov(p_a,q_b)
    cp=np.cov(p.T); out['Cov(p_a,p_a\') a!=a\'']=cp[~np.eye(d,dtype=bool)].mean()
    cpq=np.array([[np.cov(p[:,a],q[:,b])[0,1] for b in range(d)] for a in range(d)])
    out['Cov(p_a,q_b) mean']=cpq.mean()
    # entropy difference variance
    def H(z): z=np.clip(z,1e-15,1); return -(z*np.log(z)).sum(1)
    out['Var(H(p)-H(q))']=(H(p)-H(q)).var()
    return out,TA,TB
print("=== d=4, dM=4 ===")
m,TA,TB=moments(4,4); 
for k,v in m.items(): print(f"  {k:28s} = {v:.4e}")
d,dM=4,4; D=d*d*dM
# reviewer's analytic formulas
VarTA_th=2*d*dM*(d-1)*(d*dM+1)/((D+1)**2*(D+2)*(D+3))
CovTATB_th=2*dM*(d-1)**2/((D+1)**2*(D+2)*(D+3))
VarTAmTB_th=4*dM*(d-1)/((D+1)*(D+2)*(D+3))
print(f"\n  THEORY Var(T_A)      = {VarTA_th:.4e}")
print(f"  THEORY Cov(T_A,T_B)  = {CovTATB_th:.4e}")
print(f"  THEORY Var(T_A-T_B)  = {VarTAmTB_th:.4e}   (~4/d^5 dM^2 = {4/(d**5*dM**2):.4e})")
print(f"  THEORY Var(H(p)-H(q))~ (d^2/4)Var(T_A-T_B) = {(d**2/4)*VarTAmTB_th:.4e}  (~1/d^3 dM^2={1/(d**3*dM**2):.4e})")
print(f"\n  check 2Var(T_A)-2Cov = {2*VarTA_th-2*CovTATB_th:.4e} vs Var(T_A-T_B)_th {VarTAmTB_th:.4e}")
