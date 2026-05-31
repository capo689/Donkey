"""Faithful regeneration of Figures 1,3,4,5 from real data + leading-order models.
Fig 5: Table 1 (exact, from draft). Fig 3: Dirichlet(product) model. Fig 4: Haar model
+ Table1 Haar col. Fig 1: no-V model curve vs data."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import sem
rng=np.random.default_rng(707070)  # canonical seed
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

# ---------- leading-order models ----------
def shannon(p): p=p[p>0]; return -np.sum(p*np.log(p))
def product_HminusH(d,n):  # iid Dirichlet(1..1) Shannon entropies -> |H_A - H_B|
    a=rng.dirichlet(np.ones(d),n); b=rng.dirichlet(np.ones(d),n)
    HA=np.array([shannon(x) for x in a]); HB=np.array([shannon(x) for x in b])
    return HA-HB
def haar_marginal_diag(d,dM,n):  # near-max-mixed: diag of Haar marginal ~ Dirichlet(dM,..) scaled
    # leading-order Haar bulk marginal diagonal: p_a ~ (1/d)(1+delta), delta from Dirichlet(d_M) over d cats
    a=rng.dirichlet(dM*np.ones(d),n); return a

print("=== FIG 3 (product/Dirichlet model) numbers ===")
ds=np.array([4,8,16,32,64,128,256])
dvar=[]; ratio608=[]; gauss=[]
for d in ds:
    diff=product_HminusH(d, 4000 if d<=64 else 1500)
    # Var(H): need single-H variance
    a=rng.dirichlet(np.ones(d), 4000 if d<=64 else 1500); H=np.array([shannon(x) for x in a])
    dvar.append(d*np.var(H))
    ratio608.append(np.mean(np.abs(diff))/(0.608*d**-0.5))
    gauss.append(np.mean(np.abs(diff))/np.std(diff))
print(f"  d·Var(H): {np.round(dvar,4)}  -> target {np.pi**2/3-3:.5f}")
print(f"  ratio/(0.608 d^-1/2): {np.round(ratio608,4)} -> 1")
print(f"  Gaussian ratio: {np.round(gauss,4)} -> {np.sqrt(2/np.pi):.4f}")

# FIG 3
fig,ax=plt.subplots(2,2,figsize=(8,6))
ax[0,0].axhline(np.pi**2/3-3,ls='--',c=C_TH,label=r'$\pi^2/3-3$')
ax[0,0].plot(ds,dvar,'o-',c=C_PROD); ax[0,0].set_xscale('log',base=2)
ax[0,0].set_xlabel(r'$d$'); ax[0,0].set_ylabel(r'$d\cdot\mathrm{Var}(H)$'); ax[0,0].set_title('(a) variance asymptote'); ax[0,0].legend()
ax[0,1].axhline(1,ls='--',c=C_TH); ax[0,1].plot(ds,ratio608,'o-',c=C_PROD); ax[0,1].set_xscale('log',base=2)
ax[0,1].set_xlabel(r'$d$'); ax[0,1].set_ylabel(r'$\mathbb{E}|H_A-H_B|/(0.608\,d^{-1/2})$'); ax[0,1].set_title('(b) prefactor convergence')
ax[1,0].axhline(np.sqrt(2/np.pi),ls='--',c=C_TH,label=r'$\sqrt{2/\pi}$'); ax[1,0].plot(ds,gauss,'o-',c=C_PROD); ax[1,0].set_xscale('log',base=2)
ax[1,0].set_xlabel(r'$d$'); ax[1,0].set_ylabel(r'$\mathbb{E}|H_A-H_B|/\sigma$'); ax[1,0].set_title('(c) Gaussian-limit ratio'); ax[1,0].legend()
# (d) zero-param: model |S_A-S_B| vs 0.608 d^-1/2 across Table1 product d
dpd=dB[~np.isnan(p_m)]; mod=[np.mean(np.abs(product_HminusH(d,3000))) for d in dpd]
ax[1,1].plot(dpd,0.608*dpd**-0.5,'--',c=C_TH,label=r'$0.608\,d_B^{-1/2}$')
ax[1,1].plot(dpd,mod,'s',c=C_PROD,label='leading-order MC'); ax[1,1].set_xscale('log'); ax[1,1].set_yscale('log')
ax[1,1].set_xlabel(r'$d_B$'); ax[1,1].set_ylabel(r'$\mathbb{E}|H_A-H_B|$'); ax[1,1].set_title('(d) zero-parameter check'); ax[1,1].legend()
plt.tight_layout(); plt.savefig('figs/figure3.png',bbox_inches='tight'); plt.close()
print("  -> figs/figure3.png")

# FIG 5: Table 1 log-log + ratio
fig,ax=plt.subplots(1,2,figsize=(9,3.8))
ax[0].errorbar(dB,h_m,yerr=h_e,fmt='o',c=C_HAAR,label='Haar (measured)',capsize=2)
ax[0].plot(dB,h_th,'-',c=C_HAAR,alpha=0.6,label='Haar theory')
m=~np.isnan(p_m)
ax[0].errorbar(dB[m],p_m[m],yerr=p_e[m],fmt='s',c=C_PROD,label='Product (measured)',capsize=2)
ax[0].plot(dB[m],p_th[m],'-',c=C_PROD,alpha=0.6,label='Product theory')
ax[0].set_xscale('log'); ax[0].set_yscale('log'); ax[0].set_xlabel(r'$d_B$'); ax[0].set_ylabel(r'$\mathbb{E}|S_A-S_B|$')
# slope triangles
ax[0].plot([10,20],[0.011,0.011*2**-1.5],'k-',lw=1); ax[0].text(13,0.007,'$-3/2$',fontsize=8)
ax[0].plot([10,20],[0.16,0.16*2**-0.5],'k-',lw=1); ax[0].text(13,0.14,'$-1/2$',fontsize=8)
ax[0].set_title('(a) both classes vs theory'); ax[0].legend(fontsize=7)
ratio=p_m/h_m
ax[1].plot(dB[m],ratio[m],'o',c='#5a3d6b'); ax[1].plot(dB,dB*(ratio[0]/dB[0]),'--',c=C_TH,label=r'$\propto d_B^{+1}$')
ax[1].set_xscale('log'); ax[1].set_yscale('log'); ax[1].set_xlabel(r'$d_B$'); ax[1].set_ylabel('Product/Haar ratio')
ax[1].set_title('(b) exponent gap'); ax[1].legend(fontsize=8)
plt.tight_layout(); plt.savefig('figs/figure5.png',bbox_inches='tight'); plt.close()
print(f"=== FIG 5: ratio at dB=4: {ratio[0]:.1f}, at dB=24: {ratio[-1]:.1f} -> figs/figure5.png")
