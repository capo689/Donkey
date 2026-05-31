import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import unitary_group
rng=np.random.default_rng(707070)
plt.rcParams.update({'font.size':10,'axes.grid':True,'grid.alpha':0.3,'figure.dpi':140,
                     'axes.spines.top':False,'axes.spines.right':False,'font.family':'serif'})
C_HAAR='#8B2635'; C_PROD='#1f4e79'
def haar_bulk(d,dM):
    n=d*d*dM; z=rng.standard_normal(n)+1j*rng.standard_normal(n); return (z/np.linalg.norm(z)).reshape(d,d,dM)
def EV_rhoRA(psi,d,dM,nV):
    acc=np.zeros((d,d),dtype=complex); deff=d*d*dM; r=deff//2
    for _ in range(nV):
        U=unitary_group.rvs(deff,random_state=rng); V=U[:r,:].reshape(r,d,d,dM)
        Z=0; rA=np.zeros((d,d),dtype=complex)
        for a in range(d):
            for ap in range(d):
                rA[a,ap]=sum(np.vdot(V[:,a,b,:]@psi[a,b,:],V[:,ap,b,:]@psi[ap,b,:]) for b in range(d))
        Z=np.real(np.trace(rA)); acc+=rA/Z
    return acc/nV
def rhoA_bulk(psi,d):  # Tr_{B,C}
    p=psi.reshape(d,-1); return p@p.conj().T

dMs=4; xs=[]; ys=[]; offb=[]; offev=[]; labels=[]
for d in [4,6,8]:
    psi=haar_bulk(d,dMs)
    rb=rhoA_bulk(psi,d); ev=EV_rhoRA(psi,d,dMs, 250 if d<8 else 150)
    xs+=list(np.real(np.diag(rb))); ys+=list(np.real(np.diag(ev)))
    offmask=~np.eye(d,dtype=bool)
    offb.append(np.mean(np.abs(rb[offmask]))); offev.append(np.mean(np.abs(ev[offmask]))); labels.append(d)
xs=np.array(xs); ys=np.array(ys)

fig,ax=plt.subplots(1,2,figsize=(9,3.8))
# (a) diag E_V[rho_RA] vs diag(rho_A^bulk), 18 points
lim=[0,max(xs.max(),ys.max())*1.1]
ax[0].plot(lim,lim,'k--',alpha=0.5,label='$y=x$')
ax[0].scatter(xs,ys,c=C_HAAR,s=30,zorder=3,label='18 diagonal entries')
ax[0].set_xlabel(r'$\mathrm{diag}(\rho_A^{\rm bulk})$'); ax[0].set_ylabel(r'$\mathbb{E}_V[\rho_{R_A}]$ diagonal')
ax[0].set_title('(a) structural identity (Haar, $d_B\\in\\{4,6,8\\}$)'); ax[0].legend(fontsize=8)
# (b) off-diagonal suppression
x=np.arange(len(labels)); w=0.35
ax[1].bar(x-w/2,offb,w,color=C_PROD,label=r'$|\rho_A^{\rm bulk}|_{\rm off}$')
ax[1].bar(x+w/2,offev,w,color=C_HAAR,label=r'$|\mathbb{E}_V[\rho_{R_A}]|_{\rm off}$')
ax[1].set_yscale('log'); ax[1].set_xticks(x); ax[1].set_xticklabels([f'$d_B$={l}' for l in labels])
ax[1].set_ylabel('mean off-diagonal magnitude'); ax[1].set_title('(b) off-diagonal suppression'); ax[1].legend(fontsize=8)
plt.tight_layout(); plt.savefig('figs/figure2.png',bbox_inches='tight'); plt.close()
resid=(ys-xs)/np.maximum(xs,1e-9)
print(f"FIG2: 18 pts, max rel dev={np.max(np.abs(resid)):.3f}; offdiag suppression dB=4: bulk={offb[0]:.4f} EV={offev[0]:.2e} (factor {offb[0]/offev[0]:.0f})")
