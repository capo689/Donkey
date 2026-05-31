---
title: "Appendix B — Reproducibility"
kind: "appendix"
paperNumber: 3
order: 3
subtitle: "Seeds, environment, manifest. Every CSV reproduces bit-identically from master seed 707070."
---


*Complete documentation of the computational program behind this paper:
software environment, seed conventions, sample sizes per data point,
and the file manifest. All numerical results in the main text are
reproducible from the artifacts documented here.*

---

## B.1 Software environment

All computations use the following package versions, pinned on a single
Linux machine (Ubuntu 24.04 LTS, Python 3.12.3):

| Package | Version | Use |
|---|---|---|
| `numpy` | 2.4.4 | linear algebra, random number generation |
| `scipy` | 1.17.1 | `unitary_group` (Haar-random unitaries), `ortho_group` (Haar-random orthogonals) |
| `pandas` | 3.0.2 | data tables and CSV I/O |
| `matplotlib` | 3.10.8 | figures |
| `mpmath` | 1.3.0 | exact evaluation of transcendental constants |
| `sympy` | 1.14.0 | analytic checkpoint computations |
| `statsmodels` | 0.14.6 | WLS and subleading-correction fits |

Every `pip install` used `--break-system-packages` as required by Ubuntu 24
system Python; all results are reproducible under any equivalent install of
the above versions.

## B.2 Seed conventions

All Monte Carlo draws route through either `numpy.random.default_rng(seed)`
or the project's `SeededRNG` wrapper (which threads a single
`default_rng` through both numpy and `scipy.stats.unitary_group` for a
unified stream):

```python
class SeededRNG:
    def __init__(self, seed: int = 0xBADC0DE):
        self.rng = np.random.default_rng(int(seed))
    def haar_unitary(self, n):
        return unitary_group.rvs(n, random_state=self.rng)
    def haar_state(self, d):
        # complex Gaussian then normalize
        ...
    def aehpv_map(self, d_eff, d_fund):
        # first d_fund rows of haar_unitary(d_eff)
        ...
```

Each phase uses a distinct `BASE_SEED` constant, with per-point seeds
derived deterministically from `BASE_SEED` and the relevant dimension
parameters so that every data point's sample stream is fully determined
by its nominal coordinates:

| Phase | `BASE_SEED` | Per-point seed formula |
|---|---:|---|
| Phase 1 (HUZ/Colorado tables)    | `424242` | `BASE + d_Ob*10000 + d_M*100 + d_fund` |
| Phase 2 (HUZ error scaling)      | `313131` | `BASE + d_Ob*131 + d_M*11 + d_fund` |
| Phase 3 (EGH reproduction)       | `202020` | `BASE + D_L*10000 + D_R*100 + D_C` |
| Phase 4 (two-observer setup)     | `414141` | `BASE + d_OA*1000 + d_OB*100 + d_M*10 + d_fund` |
| Phase 5 (money plot)             | `505050` | `BASE + d_B*10000 + batch_offset` |
| Phase 6 (state-class scan)       | `606060` | `BASE + d_B*100 + class_code` |
| Phase 7 (theorem verification)   | inline   | `77700 + d_B` or similar per-script |

The seed-to-data correspondence is bit-identical across reruns under
`numpy >= 2.0`: the same seed yields the same state vector, unitary, and
statistics down to the last bit.

## B.3 Sample sizes per data point

*Note on file names in §§B.3–B.4.* The phase-prefixed scripts and CSVs named below
(e.g. `phase5_boost_point.py`, `phase5_extended_scan.csv`, `phase5_money_plot.py`)
are **historical development artifacts** documenting how the data were produced; they
are **not part of the shipped `reproducibility/` bundle**, which contains the
consolidated regenerators and data listed in §B.5. They are referenced here only to
record the original sampling and wall-time methodology.


### Phase 5 extended scan (Haar bulk)

Nine points with cumulative sample counts from merged batches:

| $d_B$ | $N$ | notes |
|---:|---:|---|
| 4  | 300 | single batch |
| 6  | 300 | single batch |
| 8  | 300 | single batch |
| 10 | 300 | single batch |
| 12 | 300 | merged from 150 + 150 with `phase5_boost_point.py` |
| 14 | 200 | merged from 100 + 100 |
| 16 | 240 | merged from 120 + 120 |
| 20 | 190 | merged from 100 + 90 |
| 24 | 60  | single batch (compute-bound at $d_{\rm eff} = 2304$) |

Batch-merge metadata preserved in `phase5_extended_scan.csv`. Batch offsets
use independent seed streams (`BASE_SEED + d_B*10000 + batch_index`) to
guarantee statistical independence across batches.

### Phase 6 state-class scan

Haar and Product classes, six primary points plus Product extension:

| $d_B$ | Haar $N$ | Product $N$ |
|---:|---:|---:|
| 4  | 150 | 150 |
| 6  | 150 | 150 |
| 8  | 150 | 150 |
| 10 | 150 | 150 |
| 12 | 150 | 150 |
| 16 | 100 | 150 |
| 20 | —   | 40  (out-of-sample extension) |
| 24 | —   | 20  (out-of-sample extension) |

### Phase 7 theorem verification

Per-figure sample sizes:

**Figure 3 (Theorem 1, Product):**
- Panel (a) Dirichlet variance: $N \in \{10^5, 10^5, 10^5, 10^5, 5 \cdot 10^4, 5 \cdot 10^4, 2.5 \cdot 10^4, 1.5 \cdot 10^4, 10^4\}$ for $d \in \{4, 8, 16, 32, 64, 128, 256, 512, 1024\}$.
- Panel (b) prefactor: $N \in \{10^5, 5 \cdot 10^4, 5 \cdot 10^4, 3 \cdot 10^4, 2.5 \cdot 10^4, 1.5 \cdot 10^4, 1.5 \cdot 10^4, 8 \cdot 10^3\}$.
- Panel (c) Gaussian ratio: same as (b).
- Panel (d) Phase-6 theory: $N = 30\,000$ per theory point, paired with Phase 6 data.

**Figure 4 (Theorem 2, Haar):**
- Panels (a, b) large-$d$ scan: $N \in \{3 \cdot 10^4, 1.5 \cdot 10^4, 10^4, 6 \cdot 10^3, 4 \cdot 10^3, 2 \cdot 10^3\}$ for $d \in \{16, 24, 32, 48, 64, 96\}$.
- Panel (c) Phase-5 comparison: matched to Phase 5 $N$ values in §B.3 above.
- Panel (d) out-of-sample: $d = 128$ at $N = 3000$; $d_B = 18$ at $N = 60$ (full HUZ + $V$ pipeline).

### Structural identity verification (Figure 2)

Haar-$V$ averages at $d_B \in \{4, 6, 8\}$ with $N_V \in \{500, 300, 200\}$
Haar-$V$ draws per point, two bulk state classes. 18 diagonal entries
compared per class (6 at $d_B = 4$, 6 at $d_B = 6$, 6 at $d_B = 8$).

## B.4 Per-batch wall-time budget

The execution environment imposed a wall-time ceiling of approximately
5 minutes per bash invocation. This ruled out single-shot runs at large
$d_B$ (where per-sample cost scales as $d_{\rm eff}^3 = (d_B^2 d_M)^3$ for
the full two-observer HUZ + $V$ simulation). Three workarounds enabled
the large-$d_B$ scan:

1. **Checkpoint-every-N-samples** (`phase5_boost_point.py`): pickle
   partial results to `phase5_cache/point_dB{N}.pkl` every 25–50 samples
   so a timeout at sample $k$ loses at most 50 samples, not the full run.
2. **Independent batch seeds**: each invocation uses
   `BASE_SEED + d_B*10000 + batch_index` so running the same command twice
   extends the sample count rather than duplicating samples.
3. **Efficient two-observer entropy computation**
   (`two_observer_entropies_fast` in `phase5_money_plot.py`): replaces the
   naïve formation of the full joint density matrix (which would require
   $\sim 270$ GB at $d_B = 16$) with direct einsum contractions on the
   state tensor, reducing memory to $\sim 2$ MB at $d_B = 16$. Bit-identical
   to the naïve computation on five cross-checked test cases.

All Phase 5, 6, and 7 data was collected under these three mechanisms.
A single fresh machine with no wall-time limits could reproduce the full
scan in approximately 3–4 CPU-days on a single core.

## B.5 File manifest (bundled `reproducibility/` directory)

The accompanying package ships a consolidated, self-contained artifact set
sufficient to regenerate every figure and Table 1 from the documented seeds.
It does **not** ship the full phase-by-phase development tree; the files below
are exactly what is included.

### Backend
- `bh_lab_backend.py` — `SeededRNG`, `aehpv_map`, and the two-observer HUZ
  reduced-state machinery used by all drivers.

### Figure generators (canonical seed 707070)
- `make_fig2.py` — Figure 2 (structural identity, Lemma 1): diagonal agreement
  and off-diagonal suppression.
- `make_figs_1345.py` — Figures 3 and 5 (product Dirichlet model; the Table 1
  log-log landscape and exponent-gap ratio). Loads Table 1 from
  `table1_full_scan.csv`.
- `make_figs_41.py` — Figures 1 and 4 (finite-$d_B$ vs asymptotic; the Haar
  prefactor test, subleading structure, HUZ+$V$ residuals, and out-of-sample
  $d=128$). Loads Table 1 from `table1_full_scan.csv` and the prefactor scan
  from `fig4_haar_prefactor.csv`.

### Proof-verification scripts
- `scratch_fourth_moment.py` — the fourth-moment projector estimate (Lemma C.5)
  and assembled off-diagonal bound.
- `scratch_Fdiag.py` — direct Monte-Carlo verification of $F_{\rm diag}$ and of
  the diagonal-to-bulk error $F_{\rm diag}$ (Lemma C.6).
- `scratch_grouped_dirichlet.py` — verification of the grouped-Dirichlet moments
  of Lemma 3 (Var$(T_A)$, Cov$(T_A,T_B)$, Var$(T_A-T_B)$, and the negative
  off-diagonal / vanishing $p$–$q$ covariances).
- `scratch_centered_C6.py` — confirms the centered-operator representation of
  Lemma C.6 ($L_A-L_B = -(d/\rho)\mathrm{Tr}[(P-\rho I)(G_A-G_B)]$, correlation
  $>0.999$ with the direct linear error) and the resulting $O(d^{-4}d_M^{-2})$ scaling.
- `scratch_Mdom.py` — *diagnostic only* (not used by any proof): inspects the
  conditional diagonal-covariance matrix; retained for completeness.

### Data (one row per figure/table point)
- `table1_full_scan.csv` — the single source of truth for Table 1 (Haar +
  product, measured / sem / theory / $z$); consumed by both figure generators.
- `fig1_full_V.csv`, `fig1_no_V.csv` — Figure 1 curves.
- `fig2_struct_identity.csv`, `fig2_offdiag.csv` — Figure 2 panels.
- `fig3_dirichlet_var.csv`, `fig3_prefactor.csv`, `fig3_gaussian_ratio.csv`, `fig3_panel_d.csv` — Figure 3 panels.
- `fig4_haar_prefactor.csv`, `fig4_full_V.csv`, `fig4_out_of_sample.csv` — Figure 4 panels.
- `fig5_class_ratio.csv` — Figure 5 ratio panel.
- `entropy_replacement.csv` — $F_{AB}$ end-to-end check (§C.7).
- `phase2_dM_scan.csv`, `phase2_exponents.csv` — $d_M$-dependence and fitted exponents.

## B.6 Reproducibility verification

Two classes of checks were run. The first concerns the artifacts **shipped in
`reproducibility/`**: each figure and Table 1 regenerates from the bundled CSVs
and generators under the documented environment and seed, and the proof-verification
scripts reproduce the quoted numbers (e.g. `scratch_grouped_dirichlet.py` reproduces
the Lemma 3 moments to $<1\%$, `scratch_centered_C6.py` the Lemma C.6
representation and scaling, and `scratch_Fdiag.py` the $F_{\rm diag}$ ratios;
`scratch_Mdom.py` is a diagnostic and supports no proof step).

The second class is a record of the broader **development program** (the historical
phase scripts, which are *not* part of the shipped bundle): all non-trivial data
points were spot-checked there for bit-identical reproducibility — integer rank
predictions; error-scaling and EGH verifications to $\le 10^{-12}$; the extended
Haar scan within a batch (merged-batch means reproducible to $\le 10^{-10}$); and
the Dirichlet-variance check (Lemma 4) to $\le 10^{-13}$. The one caveat there:
merged-batch means are reproducible in aggregate but not strictly bit-identical
across batch-execution orderings, as summation order shifts the accumulated mean by
$\le 10^{-14}$.

## B.7 Data and code availability

The reproducibility artifacts are provided as supplementary material with
this submission, in the `reproducibility/` directory of the accompanying
package: the unified backend `bh_lab_backend.py` (containing `SeededRNG`,
`aehpv_map`, and the two-observer HUZ machinery), the figure-generation
scripts, the verification scripts referenced in §B.5, and the CSV data files
underlying every figure and table. A public archival deposit (Zenodo or
equivalent) with a DOI is planned at time of journal submission; until then
the bundled `reproducibility/` directory is the authoritative artifact set.
The phase-by-phase script names in §B.5 reflect the development history; the
consolidated, self-contained scripts in `reproducibility/` are sufficient to
regenerate all figures and the Table 1 scan from the documented seeds.
