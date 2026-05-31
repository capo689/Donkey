"""Verify the centered-operator proof of C.6:
  eta_a^X = (1/rho) Tr[(P-rho I) Q_X^(a)] + norm remainder
  L_A-L_B = -(d/rho) Tr[(P-rho I)(G_A-G_B)] + remainder,  G_X=sum_a delta_a^X Qtil_X^(a)
  E_V[(L_A-L_B)^2|psi] <= C (d^2/D) Tr[(G_A-G_B)^2]
  E_psi Tr[(G_A-G_B)^2] = O(d^-4 dM^-1)  => E[(L_A-L_B)^2]=O(d^-4 dM^-2)."""
import numpy as np
from scipy.stats import unitary_group
rng=np.random.default_rng(707070)
rho=0.5
def setup(psi,d,dM):
    # phi_ab = vector in C^{D} (the bulk col for fixed a,b over c), D=d*d*dM
    D=d*d*dM
    phi={}
    for a in range(d):
        for b in range(d):
            v=np.zeros(D,dtype=complex); 
            # embed psi[a,b,:] into the (a,b) block of the D-dim space
            idx=(a*d+b)*dM
            v[idx:idx+dM]=psi[a,b,:]
            phi[(a,b)]=v
    return phi,D
def Qblock(phi,d,a):  # Q_X^(a) for X=A: sum_b |phi_ab><phi_ab|
    D=len(phi[(0,0)]); Q=np.zeros((D,D),dtype=complex)
    for b in range(d): Q+=np.outer(phi[(a,b)],phi[(a,b)].conj())
    return Q
def QblockB(phi,d,b):  # Q_B^(b): sum_a |phi_ab><phi_ab|
    D=len(phi[(0,0)]); Q=np.zeros((D,D),dtype=complex)
    for a in range(d): Q+=np.outer(phi[(a,b)],phi[(a,b)].conj())
    return Q

print(f"{'d':>2} {'corr(L_rep,L_dir)':>17} {'E[(LA-LB)^2]*d^4dM^2':>21} {'E Tr[(GA-GB)^2]*d^4dM':>22}")
for d in [4,5]:
    dM=4; D=d*d*dM; r=int(round(rho*D)); nV=300; npsi=40
    L2s=[]; corr_acc=[]; tr_acc=[]
    Ldir_all=[]; Lrep_all=[]
    for _ in range(npsi):
        z=rng.standard_normal(d*d*dM)+1j*rng.standard_normal(d*d*dM); psi=(z/np.linalg.norm(z)).reshape(d,d,dM)
        phi,_=setup(psi,d,dM)
        pab=np.array([[np.vdot(phi[(a,b)],phi[(a,b)]).real for b in range(d)] for a in range(d)])
        pA=pab.sum(1); pB=pab.sum(0); dA=pA-1.0/d; dB=pB-1.0/d
        Qtot=sum(Qblock(phi,d,a) for a in range(d))
        GA=sum(dA[a]*(Qblock(phi,d,a)-pA[a]*Qtot) for a in range(d))
        GB=sum(dB[b]*(QblockB(phi,d,b)-pB[b]*Qtot) for b in range(d))
        tr_GAB=np.real(np.trace((GA-GB)@(GA-GB)))
        tr_acc.append(tr_GAB)
        for _ in range(nV):
            U=unitary_group.rvs(D,random_state=rng); V=U[:r,:]; P=V.conj().T@V
            # direct eta_a, L_A-L_B
            Z=np.real(np.trace(P@Qtot))
            etaA=np.array([np.real(np.trace(P@Qblock(phi,d,a)))/Z - pA[a] for a in range(d)])
            etaB=np.array([np.real(np.trace(P@QblockB(phi,d,b)))/Z - pB[b] for b in range(d)])
            Ldir=-d*(np.dot(dA,etaA)-np.dot(dB,etaB))
            # representation
            Lrep=-(d/rho)*np.real(np.trace((P-rho*np.eye(D))@(GA-GB)))
            Ldir_all.append(Ldir); Lrep_all.append(Lrep); L2s.append(Ldir**2)
    Ldir_all=np.array(Ldir_all); Lrep_all=np.array(Lrep_all)
    corr=np.corrcoef(Ldir_all,Lrep_all)[0,1]
    print(f"{d:>2} {corr:>17.4f} {np.mean(L2s)*d**4*dM**2:>21.3f} {np.mean(tr_acc)*d**4*dM:>22.3f}")
