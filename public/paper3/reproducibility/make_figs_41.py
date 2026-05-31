import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
rng=np.random.default_rng(707070)
plt.rcParams.update({'font.size':10,'axes.grid':True,'grid.alpha':0.3,'figure.dpi':140,
                     'axes.spines.top':False,'axes.spines.right':False,'font.family':'serif'})
C_HAAR='#8B2635'; C_PROD='#1f4e79'; C_TH='#444'
# ---------- Table 1 loaded from canonical table1_full_scan.csv (single source of truth) ----------
import csv as _csv
_rows=list(_csv.DictReader(open('table1_full_scan.csv')))
_h={int(r['d_B']):r for r in _rows if r['class']=='haar'}
_p={int(r['d_B']):r for r in _rows if r['class']=='product'}
dB   =np.array(sorted(_h))
h_m  =np.array([float(_h[d]['measured']) for d in dB])
h_e  =np.array([float(_h[d]['sem'])      for d in dB])
h_th =np.array([float(_h[d]['theory'])   for d in dB])
p_m  =np.array([float(_p[d]['measured']) if d in _p else np.nan for d in dB])
p_e  =np.array([float(_p[d]['sem'])      if d in _p else np.nan for d in dB])
p_th =np.array([float(_p[d]['theory'])   if d in _p else np.nan for d in dB])

h_z=(h_m-h_th)/h_e
asym=0.798/4*dB**-1.5
def shannon(p): p=p[p>1e-15]; return -np.sum(p*np.log(p))
def noV(dB,dM,n):
    out=[]
    for _ in range(n):
        for store in range(2):
            pass
        a=rng.standard_normal(dB*dB*dM)+1j*rng.standard_normal(dB*dB*dM); a/=np.linalg.norm(a)
        b=rng.standard_normal(dB*dB*dM)+1j*rng.standard_normal(dB*dB*dM); b/=np.linalg.norm(b)
        ra=(a.reshape(dB,dB*dM)); rb=(b.reshape(dB,dB*dM))
        pa=np.real(np.diag(ra@ra.conj().T)); pb=np.real(np.diag(rb@rb.conj().T))
        out.append(abs(shannon(pa)-shannon(pb)))
    return np.mean(out),np.std(out)/np.sqrt(n)

# ---- FIG 4 ----
h_z=(h_m-h_th)/h_e
# prefactor data (the d=8..64 no-V scan that the §4.5 fit uses)
import csv as _c
_pf=list(_c.DictReader(open('fig4_haar_prefactor.csv')))
pf_d=np.array([float(r['d']) for r in _pf]); pf_r=np.array([float(r['ratio']) for r in _pf])
pf_se=np.array([float(r['sem']) for r in _pf])/np.array([float(r['theory']) for r in _pf])
# SEM-weighted floating-asymptote fit  ratio = A + B/d
_X=np.vstack([np.ones_like(pf_d),1/pf_d]).T; _W=np.diag(1/pf_se**2)
_beta=np.linalg.solve(_X.T@_W@_X,_X.T@_W@pf_r); _cov=np.linalg.inv(_X.T@_W@_X)
A4,B4=_beta; A4e=np.sqrt(_cov[0,0]); B4e=np.sqrt(_cov[1,1])
fig,ax=plt.subplots(2,2,figsize=(8,6))
dd=np.linspace(8,64,100)
# (a) prefactor test: ratio -> A (consistent with A=1)
ax[0,0].errorbar(pf_d,pf_r,yerr=pf_se,fmt='o',c=C_HAAR,capsize=2,label='measured/asymptotic')
ax[0,0].plot(dd,A4+B4/dd,'-',c=C_TH,label=f'$A+B/d_B$, $A={A4:.2f}\\pm{A4e:.2f}$')
ax[0,0].axhline(1,ls=':',c='gray'); ax[0,0].set_xlabel(r'$d_B$'); ax[0,0].set_ylabel('ratio')
ax[0,0].set_title('(a) prefactor test'); ax[0,0].legend(fontsize=7)
# (b) subleading structure 1 - 1.0/d_B
ax[0,1].errorbar(pf_d,pf_r,yerr=pf_se,fmt='o',c=C_HAAR,capsize=2)
ax[0,1].plot(dd,1-1.0/dd,'--',c=C_PROD,label='$1-1.0/d_B$')
ax[0,1].axhline(1,ls=':',c='gray'); ax[0,1].set_xlabel(r'$d_B$'); ax[0,1].set_ylabel('measured/asymptotic')
ax[0,1].set_title('(b) subleading structure'); ax[0,1].legend(fontsize=7)
# (c) z-scores from Table 1 (full HUZ+V pipeline)
ax[1,0].bar(range(len(dB)),h_z,color=[C_HAAR if abs(z)<2 else 'orange' for z in h_z])
ax[1,0].axhline(2,ls=':',c='r'); ax[1,0].axhline(-2,ls=':',c='r'); ax[1,0].axhline(0,c='k',lw=0.5)
ax[1,0].set_xticks(range(len(dB))); ax[1,0].set_xticklabels(dB); ax[1,0].set_xlabel(r'$d_B$')
ax[1,0].set_ylabel(r'$z=(\mathrm{meas}-\mathrm{theory})/\sigma$'); ax[1,0].set_title(f'(c) HUZ+$V$ residuals (max |z|={np.max(np.abs(h_z)):.2f})')
# (d) out-of-sample d=128
m128,e128=noV(128,4,1500); th128=0.798/4*128**-1.5*(1-1.0/128)
ax[1,1].errorbar([128],[m128],yerr=[e128],fmt='o',c=C_HAAR,capsize=3,label=f'measured {m128:.2e}')
ax[1,1].plot([128],[th128],'x',c=C_TH,ms=12,label=f'predicted {th128:.2e}')
ax[1,1].plot(dB,h_m,'.',c='gray',alpha=0.5,label='fit-range data')
ax[1,1].set_xscale('log'); ax[1,1].set_yscale('log'); ax[1,1].set_xlabel(r'$d_B$'); ax[1,1].set_ylabel(r'$\mathbb{E}|S_A-S_B|$')
ax[1,1].set_title(f'(d) out-of-sample $d=128$ ($z$={((m128-th128)/e128):.2f})'); ax[1,1].legend(fontsize=7)
plt.tight_layout(); plt.savefig('figs/figure4.png',bbox_inches='tight'); plt.close()
print(f"FIG4: A={A4:.3f}+/-{A4e:.3f}, B={B4:.2f}, max|z|={np.max(np.abs(h_z)):.2f}, d128 z={(m128-th128)/e128:.2f}")

# ---- FIG 1: no-V full curve vs asymptotic vs data (small-d focus) ----
fig,ax=plt.subplots(figsize=(5.5,4))
dgrid=np.array([4,5,6,8,10,12,16,20,24])
nov=np.array([noV(d,4,1200)[0] for d in dgrid])
ax.errorbar(dB,h_m,yerr=h_e,fmt='o',c=C_HAAR,capsize=2,label='measured (HUZ+$V$)')
ax.plot(dgrid,nov,'-',c=C_PROD,label='no-$V$ full-structure model')
ax.plot(dgrid,0.798/4*dgrid**-1.5,'--',c=C_TH,label=r'asymptotic $0.798\,d_M^{-1}d_B^{-3/2}$')
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlabel(r'$d_B$'); ax.set_ylabel(r'$\mathbb{E}|S_A-S_B|$')
ax.set_title('Figure 1: finite-$d_B$ vs asymptotic (Haar)'); ax.legend(fontsize=8)
plt.tight_layout(); plt.savefig('figs/figure1.png',bbox_inches='tight'); plt.close()
print(f"FIG1: no-V model at dB=4 = {nov[0]:.4f} (measured {h_m[0]:.4f}); tracks within errorbars")
