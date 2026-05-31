"""Lemma D.3 (fourth-moment projector estimate) + assembled E||E_X||^4 = O(1/(d^6 d_M^2)).
(1) E|Tr(Pi A)|^4 <= C_4 ||A||^4 / D^2 for traceless A; also kurtosis -> 3 (sub-Gaussian).
(2) Cross: E|Tr(Pi A)|^2|Tr(Pi B)|^2 <= sqrt(.|A|^4..)(.|B|^4.) (Cauchy-Schwarz check).
(3) Assembled E||E_X||_F^4 * d^6 d_M^2 bounded.
"""
import numpy as np
from scipy.stats import unitary_group
rng=np.random.default_rng(2718281)

print("=== (1) Lemma D.3: E|Tr(Pi A)|^4 vs ||A||^4/D^2 ; kurtosis ->3 ===")
print(f"  {'D':>4} {'C4=E|.|^4 D^2/||A||^4':>22} {'kurtosis E|X|^4/(E|X|^2)^2':>28}")
for D in [16,32,64]:
    r=D//2; rho=0.5; Np=20000
    # random traceless Hermitian A, normalized
    H=rng.standard_normal((D,D))+1j*rng.standard_normal((D,D)); A=(H+H.conj().T)/2; A-=np.trace(A)/D*np.eye(D)
    nA2=np.sum(np.abs(A)**2)
    x2=[]; x4=[]
    for _ in range(Np):
        U=unitary_group.rvs(D,random_state=rng); P=U[:r,:].conj().T@U[:r,:]; Pi=P-rho*np.eye(D)
        x=np.real(np.trace(Pi@A)); x2.append(x*x); x4.append(x**4)
    m2=np.mean(x2); m4=np.mean(x4)
    print(f"  {D:>4} {m4*D**2/nA2**2:>22.3f} {m4/m2**2:>28.3f}")

print("\n=== (2) Cauchy-Schwarz cross-term check (traceless A,B) ===")
D=32; r=D//2; rho=0.5; Np=12000
H=rng.standard_normal((D,D))+1j*rng.standard_normal((D,D)); A=(H+H.conj().T)/2; A-=np.trace(A)/D*np.eye(D)
H=rng.standard_normal((D,D))+1j*rng.standard_normal((D,D)); B=(H+H.conj().T)/2; B-=np.trace(B)/D*np.eye(D)
cross=[]; aa=[]; bb=[]
for _ in range(Np):
    U=unitary_group.rvs(D,random_state=rng); P=U[:r,:].conj().T@U[:r,:]; Pi=P-rho*np.eye(D)
    ta=np.abs(np.trace(Pi@A))**2; tb=np.abs(np.trace(Pi@B))**2
    cross.append(ta*tb); aa.append(ta*ta); bb.append(tb*tb)
print(f"  E[|TrPiA|^2|TrPiB|^2]={np.mean(cross):.4e} <= sqrt(E|.A|^4 E|.B|^4)={np.sqrt(np.mean(aa)*np.mean(bb)):.4e}  (CS holds: {np.mean(cross)<=np.sqrt(np.mean(aa)*np.mean(bb))})")

print("\n=== (3) Assembled E||E_X||_F^4 * d^6 d_M^2 ===")
def haar_bulk(d,d_M):
    nn=d*d*d_M; z=rng.standard_normal(nn)+1j*rng.standard_normal(nn); return (z/np.linalg.norm(z)).reshape(d,d,d_M)
def pipeA(psi,d,d_M,V):
    pt=psi; Vt=V.reshape(V.shape[0],d,d,d_M); Z=np.real(np.vdot(V@psi.reshape(-1),V@psi.reshape(-1)))
    rA=np.zeros((d,d),dtype=complex)
    for a in range(d):
        for ap in range(d):
            rA[a,ap]=sum(np.vdot(Vt[:,a,b,:]@pt[a,b,:],Vt[:,ap,b,:]@pt[ap,b,:]) for b in range(d))/Z
    return rA
for d,d_M in [(4,2),(5,2),(6,2)]:
    d_eff=d*d*d_M; r=d_eff//2; Npsi=10; M=400
    e4=[]
    for _ in range(Npsi):
        psi=haar_bulk(d,d_M); pA=(np.abs(psi)**2).sum((1,2)); DA=np.diag(pA)
        for _ in range(M):
            U=unitary_group.rvs(d_eff,random_state=rng); V=U[:r,:]
            EA=pipeA(psi,d,d_M,V)-DA
            e4.append(np.real(np.trace(EA@EA.conj().T))**2)
    print(f"  d={d}: E||E||^4 * d^6 d_M^2 = {np.mean(e4)*d**6*d_M**2:.3f}  (bounded => O(1/(d^6 d_M^2)))")

print("\n=== (5) bracket bound: E_psi[(Sum_aa' ||M_a'a||^2)^2] <= C/d^2 ===")
# bracket B = sum_{a,a'} ||M_{a'a}||^2 = sum_b[(p_B^b)^2 - W_B^b] (off) + sum_a Tr((Q~_a)^2) (diag)
def haar_bulk3(d,d_M):
    nn=d*d*d_M; z=rng.standard_normal(nn)+1j*rng.standard_normal(nn); return (z/np.linalg.norm(z)).reshape(d,d,d_M)
for d,d_M in [(4,2),(5,2),(6,2),(8,2)]:
    Npsi=4000; Bs=[]
    for _ in range(Npsi):
        psi=haar_bulk3(d,d_M); pab=(np.abs(psi)**2).sum(2)
        pA=pab.sum(1); pB=pab.sum(0); WA=(pab**2).sum(1); WB=(pab**2).sum(0); Wbl=(pab**2).sum()
        off=np.sum(pB**2)-np.sum(WB)
        diag=np.sum(WA*(1-2*pA)+pA**2*Wbl)
        Bs.append(off+diag)
    Bs=np.array(Bs)
    print(f"  d={d}: E[B]*d={np.mean(Bs)*d:.3f}  E[B^2]*d^2={np.mean(Bs**2)*d**2:.3f}  (both bounded => bracket=Theta(1/d), E[B^2]=O(1/d^2))")
