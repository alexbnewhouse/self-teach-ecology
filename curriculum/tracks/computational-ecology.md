# Specialization Track: Computational Ecology

**Type**: Tier 2 specialization track  
**Estimated time**: 80–120 hours  
**Prerequisites**: Modules 4, 5 (recommended: Module 7)  
**Competency target**: Domain 2 — Advanced level (see [Competency Framework](../../resources/competency-framework.md))

---

## Overview

This track is designed for someone with a data science background who wants to build **real, end-to-end ecological analysis pipelines** — not just understand the theory. Each pathway is a self-contained project arc: readings → setup → guided exercises → independent project → writeup. You choose **at least two** pathways, and one of your pathway projects should feed directly into your [capstone](../10-capstone-project.md).

**How this track differs from Modules 4–5**: Those modules introduce methods in the context of ecological concepts. *This track assumes you've done that work* and focuses on building production-quality pipelines, comparing methods head-to-head, and working with real data at scale. Everything here is meant to be run, not just read.

---

## Learning Outcomes

1. Build end-to-end computational workflows from ecological question to decision-relevant output.
2. Select among SDM, Bayesian, remote sensing, network, and forecasting approaches based on inference goals.
3. Document reproducibility with data provenance, environment management, and scripted reruns.
4. Communicate uncertainty in conservation-relevant terms.
5. Critically evaluate method assumptions against the realities of ecological data.
6. Produce at least one analysis that could serve as a writing sample or open-source contribution.

---

## Setup: Your Computational Environment

Before starting any pathway, set up a reproducible workspace. This is a one-time investment.

### Option A: R-Primary Stack
```bash
# Install R packages used across pathways (run in R console)
install.packages(c(
  "tidyverse", "sf", "terra", "stars",        # data wrangling + spatial
  "brms", "rstan", "loo",                      # Bayesian
  "dismo", "biomod2", "ENMeval", "maxnet",     # SDM
  "vegan", "indicspecies", "betapart",         # community ecology
  "unmarked",                                   # occupancy
  "landscapemetrics", "gdistance",             # landscape
  "igraph", "bipartite",                        # networks
  "rgee",                                       # Google Earth Engine
  "prioritizr",                                 # conservation planning
  "rmarkdown", "knitr"                          # reproducible reports
))
# For climate-ecological pathway:
install.packages(c("climateR", "AOI"))
# devtools::install_github("EcoForecast/ecoforecastR")
```

### Option B: Python-Primary Stack
```bash
# Create a conda environment
conda create -n comp-eco python=3.11
conda activate comp-eco

# Core scientific stack
conda install -c conda-forge numpy pandas scipy matplotlib seaborn jupyterlab

# Spatial / GIS
conda install -c conda-forge geopandas rasterio shapely fiona pyproj
pip install earthengine-api geemap pylandstats

# SDM
pip install elapid
conda install -c conda-forge scikit-learn xgboost

# Bayesian
conda install -c conda-forge pymc arviz

# Networks
conda install -c conda-forge networkx

# Climate data science
conda install -c conda-forge xarray dask netCDF4 zarr cartopy cfgrib
pip install intake-esm xesmf cdsapi verde

# Deep learning (optional, for remote sensing / camera traps)
conda install -c conda-forge pytorch torchvision
```

### Option C: Mixed (Recommended)
Use R for Bayesian ecology (`brms`/`Stan`), SDM (`biomod2`), and community analysis (`vegan`). Use Python for climate data (`xarray`), remote sensing (`geemap`), and networks (`networkx`). Both via Jupyter or RStudio.

### Project Structure Template
Every pathway project should follow this structure:
```
pathway-X-project/
├── README.md           # Question, data sources, workflow, how to rerun
├── environment.yml     # or renv.lock — exact package versions
├── data/
│   ├── raw/            # Unmodified downloads (or download scripts)
│   └── processed/      # Cleaned data ready for analysis
├── notebooks/
│   ├── 01-data-acquisition.ipynb
│   ├── 02-exploration.ipynb
│   ├── 03-analysis.ipynb
│   └── 04-results.ipynb
├── src/                # Reusable functions/modules
├── figures/            # Publication-ready outputs
└── LICENSE
```

---

## Pathway A: Species Distribution Modeling

**Time**: 20–30 hours  
**Builds on**: Module 4 Unit 4.4 (SDM introduction)  
**Language**: R (primary) or Python

### Readings

> Zurell, D., Franklin, J., König, C., et al. (2020). A standard protocol for reporting species distribution models. *Ecography*, 43(9), 1261–1277.
> - **Read first** — this is your quality checklist for the entire pathway

> Valavi, R., Elith, J., Lahoz-Monfort, J.J., & Guillera-Arroita, G. (2019). blockCV: An R package for generating spatially or environmentally separated folds for k-fold cross-validation of species distribution models. *Methods in Ecology and Evolution*, 10(2), 225–232.
> - Why standard cross-validation lies to you with spatial data

> Merow, C., Smith, M.J., & Silander, J.A. Jr. (2013). A practical guide to MaxEnt. *Ecography*, 36(10), 1058–1069.
> - Already read in Module 4; re-read with implementation focus

> Araújo, M.B., & New, M. (2007). Ensemble forecasting of species distributions. *Trends in Ecology & Evolution*, 22(1), 42–47.
> - Why single-algorithm SDMs are insufficient

> Liu, C., Berry, P.M., Dawson, T.P., & Pearson, R.G. (2005). Selecting thresholds of occurrence in the prediction of species distributions. *Ecography*, 28(3), 385–393.
> - Threshold selection matters more than you think

### Key Concepts Beyond Module 4
- Spatial blocking for honest cross-validation (blockCV)
- Multicollinearity diagnosis and variable selection (VIF, ecological rationale)
- Ensemble SDMs: combining MaxEnt + BRT + GLM + RF
- Threshold selection: MaxSSS, equal sensitivity-specificity, and why it's a conservation decision
- Projecting under future climate scenarios with proper uncertainty propagation
- Model transferability across space and time
- The ODMAP (Overview, Data, Model, Assessment, Prediction) reporting standard

### Exercise A.1: Single-Species Ensemble SDM (Guided)
**Species**: European lynx (*Lynx lynx*) — relevant to rewilding and has abundant GBIF data.

Step-by-step:
1. **Data acquisition**: Download occurrence records from [GBIF](https://www.gbif.org/) using `rgbif` (R) or the GBIF API. Clean: remove duplicates, fossils, and records with coordinate uncertainty > 10 km. Thin spatially to 1 record per 10 km grid cell.
2. **Predictor variables**: Download bioclimatic variables from [CHELSA](https://chelsa-climate.org/) at 1 km resolution. Add land cover from Copernicus. Select 6–8 uncorrelated predictors (VIF < 10) with ecological rationale.
3. **Background/pseudo-absence sampling**: Generate 10,000 background points within a biologically reasonable buffer (e.g., 500 km from occurrences). Compare with target-group background if possible.
4. **Model fitting**: Fit 4 algorithms: MaxEnt (`maxnet`), BRT (`dismo::gbm.step`), GLM (with quadratic terms), and RF (`ranger` or `randomForest`). Use spatially blocked cross-validation via `blockCV`.
5. **Evaluation**: Calculate AUC, TSS, and Boyce index for each algorithm. Examine response curves. Identify which predictors drive each model.
6. **Ensemble**: Build a weighted ensemble (weights = TSS) using `biomod2`. Map mean ensemble prediction and coefficient of variation.
7. **Future projection**: Project ensemble under SSP2-4.5 and SSP5-8.5 for 2041–2060 using CHELSA future bioclim layers. Map areas of gain, loss, and stability. Quantify agreement across GCMs.
8. **Conservation interpretation**: Where does the model predict suitable but currently unoccupied habitat? How does this relate to ongoing European rewilding initiatives?

**Tools**: R packages `rgbif`, `CoordinateCleaner`, `spThin`, `terra`, `sf`, `maxnet`, `biomod2`, `ENMeval`, `blockCV`, `ecospat`

**Deliverable**: Full analysis notebook + 1,500-word report following ODMAP structure.

### Exercise A.2: Independent SDM Project
Choose your own species relevant to a conservation or rewilding question you care about. Follow the same workflow but make and justify your own decisions at each step. Candidates:
- A reintroduction candidate (gray wolf, bison, beaver) — model habitat suitability
- An invasive species — model spread potential
- A climate-sensitive species — model range contraction

**Deliverable**: Complete reproducible project folder (see template above) + 2,000-word report.

---

## Pathway B: Bayesian Ecology

**Time**: 20–30 hours  
**Builds on**: Module 5 Units 5.1 and 5.5  
**Language**: R (`brms`/`Stan`) primary, Python (`PyMC`) alternative

### Readings

> McElreath, R. (2020). *Statistical Rethinking* (2nd ed.). CRC Press.
> - Chapters 1–9, 11–14. [Free lectures](https://www.youtube.com/playlist?list=PLDcUM9US4XdPz-KxHM4XHt7uUVGWWVSus)
> - **Work through the exercises** — this book is designed as a course

> Kéry, M., & Royle, J.A. (2016). *Applied Hierarchical Modeling in Ecology. Vol. 1*. Academic Press.
> - Chapters 1–4, 6, 10 — for occupancy/abundance applications

> Gabry, J., Simpson, D., Vehtari, A., Betancourt, M., & Gelman, A. (2019). Visualization in Bayesian workflow. *Journal of the Royal Statistical Society A*, 182(2), 389–402.
> - How to actually check if your model makes sense

> Conn, P.B., Johnson, D.S., Williams, P.J., Melin, S.R., & Hooten, M.B. (2018). A guide to Bayesian model checking for ecologists. *Ecological Monographs*, 88(4), 526–542.
> - Posterior predictive checks, specifically for ecological models

### Key Concepts Beyond Module 5
- Generative modeling: simulate data before fitting models (McElreath's approach)
- Prior predictive simulation: are your priors ecologically reasonable?
- Posterior predictive checks: does your model generate data that look like your real data?
- Hierarchical/multilevel structure for ecological data (sites within regions, years within sites)
- Zero-inflated and hurdle models for ecological count data
- Model comparison: LOO-CV via `loo` package, stacking
- When Stan gives you divergent transitions and what to actually do about it

### Exercise B.1: Hierarchical Abundance Model (Guided)
**Dataset**: NEON small mammal trapping data (freely available at [data.neonscience.org](https://data.neonscience.org/)).

Step-by-step:
1. **Data acquisition**: Download small mammal box trapping data from 3–5 NEON sites across different ecoregions. Aggregate to species-level capture counts per site per trapping bout.
2. **Exploratory analysis**: Visualize count distributions. Note zero-inflation, overdispersion, nested structure (bouts within plots within sites).
3. **Prior predictive simulation**: Before fitting, simulate data from your proposed model with different prior choices. Do the simulated counts look ecologically reasonable (not predicting negative animals or billions)?
4. **Model building (progressive)**:
   - Model 1: Simple Poisson GLM
   - Model 2: Negative binomial to handle overdispersion
   - Model 3: Negative binomial GLMM with site as random intercept (`brms`)
   - Model 4: Add plot-level random effects (nested within site)
   - Model 5: Add environmental covariates (elevation, vegetation type from NEON)
5. **Diagnostics**: For each model — trace plots, Rhat, ESS, posterior predictive check (does the model reproduce the zero-inflation? the right tail?).
6. **Model comparison**: Compare all 5 models via LOO-CV (`loo` package). Interpret the differences.
7. **Ecological interpretation**: Which covariates matter? How much variation is at site vs. plot level? What does the random effects structure tell you about spatial scale?
8. **Visualization**: Posterior distributions for key effects, conditional effects plots, model-predicted vs. observed counts.

```r
# Example brms model syntax for Model 4:
library(brms)

m4 <- brm(
  count ~ 1 + (1 | site / plot),
  data = mammal_data,
  family = negbinomial(),
  prior = c(
    prior(normal(2, 1), class = "Intercept"),  # log-scale: exp(2) ≈ 7 individuals
    prior(exponential(1), class = "sd"),
    prior(gamma(0.01, 0.01), class = "shape")
  ),
  chains = 4, iter = 4000, warmup = 2000,
  control = list(adapt_delta = 0.95)
)
```

**Tools**: R packages `brms`, `loo`, `bayesplot`, `tidybayes`, `neonUtilities`

**Deliverable**: Progressive model-building notebook with diagnostics at every step + 1,500-word interpretation.

### Exercise B.2: Occupancy Model with Imperfect Detection
**Dataset**: eBird or camera trap data for a rare/elusive species.

1. Structure data as detection/non-detection histories across repeated visits
2. Fit a single-season occupancy model in a Bayesian framework (Stan or `ubms`)
3. Include site-level covariates (habitat type, distance to water) and detection covariates (survey effort, season)
4. Estimate occupancy and detection probability separately
5. Map predicted occupancy across the study area
6. Compare: How do results differ if you ignore imperfect detection?

**Deliverable**: Analysis notebook + 1,000-word discussion of detection bias implications for conservation.

### Exercise B.3: Independent Bayesian Project
Design your own analysis using a Bayesian framework for an ecological question. Good candidates:
- Population trend estimation from count time series (state-space model)
- Survival analysis from mark-recapture data (CJS model in Stan)
- Multispecies occupancy model
- Bayesian species distribution model with spatial random effects

**Deliverable**: Complete project folder + 2,000-word methods-and-results writeup.

---

## Pathway C: Remote Sensing for Biodiversity and Restoration

**Time**: 20–30 hours  
**Builds on**: Module 4 Unit 4.3 (remote sensing introduction)  
**Language**: Python (`geemap`/`earthengine-api`) primary, R (`rgee`/`terra`) alternative

### Readings

> Pettorelli, N., Wegmann, M., Skidmore, A., et al. (2016). Framing the concept of satellite remote sensing essential biodiversity variables. *Remote Sensing in Ecology and Conservation*, 2(3), 122–131.
> - The RS-EBV framework: connecting pixels to biodiversity

> Wulder, M.A., Loveland, T.R., Roy, D.P., et al. (2019). Current status of Landsat program, science, and applications. *Remote Sensing of Environment*, 225, 231–251.
> - Know your sensor

> Gorelick, N., Hancher, M., Dixon, M., et al. (2017). Google Earth Engine: Planetary-scale geospatial analysis for everyone. *Remote Sensing of Environment*, 202, 18–27.
> - The tool you'll live in for this pathway

> Gao, Y., Skutsch, M., Paneque-Gálvez, J., & Ghilardi, A. (2020). Remote sensing of forest degradation: A review. *Environmental Research Letters*, 15(10), 103001.
> - Critical for restoration monitoring applications

### Key Concepts Beyond Module 4
- Time series analysis of satellite imagery (BFAST, LandTrendr algorithms)
- Spectral mixture analysis and sub-pixel land cover
- SAR (Synthetic Aperture Radar) for cloud-prone tropical regions
- Linking spectral indices to field-measured biodiversity metrics
- Canopy height and structure from GEDI LiDAR
- Phenology extraction from satellite time series
- Validation: ground-truthing remote sensing products with field data

### Exercise C.1: Rewilding Progress Detection (Guided)
**Site**: Knepp Estate, UK (well-documented rewilding) or Oostvaardersplassen, Netherlands.

Using Google Earth Engine via `geemap` (Python) or `rgee` (R):

1. **Define AOI**: Delineate the rewilding site boundary. Also define a control area (nearby conventional farmland).
2. **Landsat time series**: Build a cloud-masked annual composite time series (1985–present) for NDVI, EVI, and NBR.
3. **Trend analysis**: Fit per-pixel linear trends in NDVI over the full time series. Map areas of greening vs. browning. Apply the Mann-Kendall test for significance.
4. **Change detection**: Use a breakpoint algorithm (BFAST or LandTrendr via GEE) to identify the year of land-use change (when rewilding began).
5. **Land cover classification**: Classify a recent Sentinel-2 image into habitat types (grassland, scrub, woodland, water, bare) using a supervised Random Forest classifier trained on visual interpretation.
6. **Comparison**: Contrast NDVI trajectories and land cover between the rewilding site and the control area. Quantify habitat heterogeneity using landscape metrics (`pylandstats` or `landscapemetrics`).
7. **GEDI integration** (optional): Extract canopy height estimates from NASA GEDI data to assess vertical habitat structure.

```python
# Example: NDVI time series in geemap
import ee
import geemap

ee.Initialize()

# Define AOI (Knepp Estate approximate bounds)
aoi = ee.Geometry.Rectangle([-0.42, 50.92, -0.32, 50.97])

# Annual Landsat NDVI composites
def annual_ndvi(year):
    start = ee.Date.fromYMD(year, 4, 1)
    end = ee.Date.fromYMD(year, 9, 30)
    composite = (ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
                 .filterBounds(aoi)
                 .filterDate(start, end)
                 .map(lambda img: img.normalizedDifference(['SR_B5', 'SR_B4']).rename('NDVI'))
                 .median())
    return composite.set('year', year)

ndvi_collection = ee.ImageCollection(
    [annual_ndvi(y) for y in range(2013, 2026)]
)
```

**Tools**: `geemap`, `earthengine-api`, `rasterio`, `pylandstats` (Python) or `rgee`, `terra`, `landscapemetrics` (R)

**Deliverable**: Analysis notebook with time series plots, maps, and 1,500-word interpretation connecting spectral trends to ecological processes.

### Exercise C.2: Deforestation Monitoring Dashboard
Using GEE and Global Forest Watch data:
1. Select a tropical forest frontier (e.g., Brazilian arc of deforestation, Borneo, Congo Basin)
2. Map annual forest loss (Hansen Global Forest Change dataset)
3. Analyze proximity to roads, protected areas, and indigenous territories
4. Build an interactive map (using `geemap` or `folium`) showing hotspots
5. Calculate deforestation rates inside vs. outside protected areas

**Deliverable**: Interactive notebook with maps + 1,000-word analysis of drivers.

### Exercise C.3: Independent Remote Sensing Project
Design your own remote sensing analysis for a conservation question. Candidates:
- Fire regime analysis and post-fire recovery using MODIS/VIIRS
- Wetland extent change detection for restoration monitoring
- Urban sprawl encroachment on habitat corridors
- Agricultural intensification impacts on surrounding habitat (NDVI buffer analysis)

**Deliverable**: Complete project folder + 2,000-word report.

---

## Pathway D: Ecological Network Analysis

**Time**: 15–25 hours  
**Builds on**: Module 5 Units 5.4 and 5.6  
**Language**: Python (`networkx`) or R (`igraph`, `bipartite`)

### Readings

> Bascompte, J., & Jordano, P. (2007). Plant-animal mutualistic networks: The architecture of biodiversity. *Annual Review of Ecology, Evolution, and Systematics*, 38, 567–593.
> - Foundational: nestedness, modularity, and what they mean

> Dunne, J.A., Williams, R.J., & Martinez, N.D. (2002). Food-web structure and network theory. *Journal of Theoretical Biology*, 214(3), 405–412.
> - Key concepts: degree distribution, connectance, robustness

> Poisot, T., Stouffer, D.B., & Gravel, D. (2015). Beyond species: Why ecological interaction networks vary through space and time. *Oikos*, 124(3), 243–251.
> - Network beta-diversity: networks aren't static

> Tylianakis, J.M., Laliberté, E., Nielsen, A., & Bascompte, J. (2010). Conservation of species interaction networks. *Biological Conservation*, 143(10), 2270–2279.
> - Why conserving species isn't enough — you need to conserve their interactions

> Memmott, J., Waser, N.M., & Price, M.V. (2004). Tolerance of pollination networks to species extinctions. *Proceedings of the Royal Society B*, 271(1557), 2605–2611.
> - Simulating extinction cascades through pollination networks

### Key Concepts
- Network representations: adjacency matrices, bipartite graphs, weighted/unweighted
- Structural metrics: connectance, nestedness (NODF), modularity, degree distribution
- Robustness simulations: random vs. targeted species removal
- Bipartite networks (plant-pollinator, host-parasite) vs. food webs
- Network motifs and their ecological meaning
- Rewiring and interaction turnover under environmental change
- Connecting network structure to ecosystem function and stability

### Exercise D.1: Food Web Robustness (Guided)
**Dataset**: Download a food web from the [Web of Life](https://www.web-of-life.es/) database or use a classic dataset (e.g., Ythan Estuary, Serengeti).

Step-by-step:
1. **Load and visualize**: Import the interaction matrix. Draw the network with node size proportional to degree. Color by trophic level.
2. **Structural analysis**: Calculate connectance, link density, mean degree, degree distribution. Is the degree distribution scale-free? Test with a power-law fit.
3. **Nestedness and modularity**: Calculate NODF (nestedness) and modularity (Louvain or simulated annealing). Interpret ecologically.
4. **Robustness simulation**: Simulate sequential species removal under three scenarios:
   - Random removal
   - Most-connected first (targeted attack)
   - Removal of apex predators first (trophic cascade scenario)
   
   Track secondary extinctions (species that lose all prey items). Plot robustness curves.
5. **Rewilding scenario**: Simulate adding back an extinct apex predator (e.g., wolf) with plausible trophic links. How does network robustness change?
6. **Comparison**: Compare structural metrics before and after the rewilding addition.

```python
# Example: Food web robustness in NetworkX
import networkx as nx
import numpy as np

def simulate_removal(G, order='random', n_reps=100):
    """Simulate sequential node removal and track network collapse."""
    results = []
    nodes = list(G.nodes())
    for rep in range(n_reps):
        H = G.copy()
        if order == 'random':
            np.random.shuffle(nodes)
        elif order == 'targeted':
            nodes = sorted(nodes, key=lambda n: G.degree(n), reverse=True)
        
        removals, remaining = [], []
        for node in nodes:
            if node in H:
                H.remove_node(node)
                # Remove nodes with no remaining links (secondary extinction)
                isolates = list(nx.isolates(H))
                H.remove_nodes_from(isolates)
                removals.append(node)
                remaining.append(H.number_of_nodes())
        results.append(remaining)
    return results
```

**Tools**: Python `networkx`, `matplotlib` | R `igraph`, `bipartite`, `cheddar`

**Deliverable**: Network analysis notebook with visualizations, robustness curves, and 1,500-word ecological interpretation.

### Exercise D.2: Pollination Network Under Climate Change
Using a plant-pollinator interaction dataset from Web of Life:
1. Compute baseline network metrics (nestedness, modularity, specialization H2')
2. Simulate phenological mismatch: randomly disconnect 10%, 20%, 30% of interactions (representing timing shifts)
3. Compute how network metrics degrade
4. Identify keystone species: which species' removal causes the most cascading loss?
5. Discuss: What does this mean for pollination services under warming?

**Deliverable**: Analysis notebook + 1,000-word discussion.

### Exercise D.3: Independent Network Project
Design your own ecological network analysis. Candidates:
- Seed dispersal network resilience in defaunated tropical forests
- Parasite-host network structure and disease emergence
- Spatial network of habitat patches (landscape connectivity as a graph problem)
- Trophic network comparison across biomes

**Deliverable**: Complete project folder + 1,500-word report.

---

## Pathway E: Climate-Ecological Modeling & Forecasting

**Time**: 25–35 hours  
**Builds on**: Module 7 Units 7.5 and 7.6  
**Language**: Python (primary; `xarray` ecosystem) and R (`ecoforecastR`)

### Readings

> Dietze, M.B. (2017). *Ecological Forecasting*. Princeton University Press.
> - **The core text**. Chapters 1–16. Free lectures + code: https://ecoforecast.org/
> - Work through at least chapters 1–5 (conceptual), 6–9 (state-space models), 14 (data assimilation)

> Bonan, G.B. (2019). *Climate Change and Terrestrial Ecosystem Modeling*. Cambridge University Press.
> - Chapters 1–4 (how climate models work), 17–20 (ecosystem model representation)

> Wikle, C.K., Zammit-Mangion, A., & Cressie, N. (2019). *Spatio-Temporal Statistics with R*. CRC Press.
> - Free at https://spacetimewithr.org/ — Chapters 1–4, 7

> Dietze, M.C., et al. (2018). Iterative near-term ecological forecasting. *PNAS*, 115(7), 1424–1432.
> - The manifesto for this approach

> White, E.P., et al. (2019). Developing an automated iterative near-term forecasting system. *Methods in Ecology and Evolution*, 10(3), 332–344.
> - Practical implementation example

> Fer, I., et al. (2021). Beyond ecosystem modeling: A roadmap to community cyberinfrastructure for ecological data-model integration. *Global Change Biology*, 27(1), 13–26.

### Key Concepts
- CMIP6 architecture: GCMs vs. ESMs, SSP scenarios, model ensembles
- Accessing and processing climate data: NetCDF/Zarr formats, xarray workflows
- Downscaling: statistical (BCSD, delta method) vs. dynamical (regional climate models)
- Bias correction of GCM output against observations
- State-space models: separating process from observation error
- Data assimilation: Kalman filter, ensemble Kalman filter, particle filter
- Uncertainty partitioning: initial conditions, parameters, process, drivers, observation
- Near-term iterative forecasting: the forecast → evaluate → update cycle
- Proper scoring rules for probabilistic forecasts (CRPS, log score)

### Exercise E.1: Climate Data Pipeline (Guided)
Build a reusable pipeline for accessing and processing climate data for ecological work.

Step-by-step:
1. **ERA5 reanalysis**: Use `cdsapi` to download ERA5 monthly temperature and precipitation for a study region (1980–present). Load into `xarray`. Calculate climatology, anomalies, and trends.
2. **CMIP6 projections**: Use `intake-esm` to access CMIP6 data from the Pangeo cloud catalog. Load surface temperature from 3–5 GCMs under SSP2-4.5 and SSP5-8.5. Regrid to a common grid using `xesmf`.
3. **Bias correction**: Bias-correct CMIP6 output against ERA5 observations using quantile mapping. Validate by comparing bias-corrected historical period to observed.
4. **Ecologically relevant metrics**: Compute growing degree days, frost-free season length, climatic water deficit, and heat wave frequency from daily data.
5. **Visualization**: Map multi-model ensemble mean and inter-model spread for 2050 vs. baseline. Create time series plots showing the trajectory with uncertainty fans.

```python
# Example: Loading CMIP6 data via intake-esm
import intake
import xarray as xr

catalog = intake.open_esm_datastore(
    "https://storage.googleapis.com/cmip6/pangeo-cmip6.json"
)

# Search for monthly surface temperature
query = catalog.search(
    experiment_id=["historical", "ssp245", "ssp585"],
    variable_id="tas",
    table_id="Amon",
    source_id=["CESM2", "GFDL-ESM4", "MPI-ESM1-2-HR", "UKESM1-0-LL"],
    member_id="r1i1p1f1"
)

datasets = query.to_dataset_dict(zarr_kwargs={"consolidated": True})
```

**Tools**: Python `xarray`, `intake-esm`, `cdsapi`, `xesmf`, `cartopy`, `dask`

**Deliverable**: Documented and reusable climate data pipeline notebook.

### Exercise E.2: State-Space Ecological Forecast (Guided)
**Dataset**: NEON phenology data (green chromatic coordinate from PhenoCam) or water quality (chlorophyll-a).

Following Dietze (2017) chapters 6–9:
1. **Data**: Download the target variable from [NEON](https://data.neonscience.org/) for one site. Plot the time series with annotations for data gaps and anomalies.
2. **Process model**: Write a simple process model (e.g., logistic growth for greenness, or a temperature-driven phenology model). Simulate from the process model and compare to observations.
3. **State-space formulation**: Reformulate as a state-space model separating:
   - Process model: $x_{t+1} = f(x_t, \theta) + \epsilon_{\text{process}}$
   - Observation model: $y_t = x_t + \epsilon_{\text{obs}}$
4. **Fit**: Fit the state-space model via MCMC (Stan or JAGS via `ecoforecastR`). Assess convergence.
5. **Forecast**: Generate 14-day-ahead probabilistic forecasts. Quantify and partition uncertainty (initial conditions, parameters, process, driver).
6. **Evaluate**: Compare forecasts against held-out observations using CRPS and coverage probability. How does forecast skill decay with lead time?

**Tools**: R `ecoforecastR`, `rjags` or `rstan`, `neonUtilities` | Python `pymc`, `neon-utilities`

**Deliverable**: Forecast analysis notebook with uncertainty decomposition visualizations + 1,500-word discussion.

### Exercise E.3: EFI/NEON Forecasting Challenge
Participate in the real, ongoing [Ecological Forecasting Initiative NEON Challenge](https://projects.ecoforecast.org/neon4cast-ci/):

1. **Choose a theme**: Aquatics (water temp, dissolved O₂), Phenology (gcc_90), Terrestrial (NEE, LE), Ticks, or Beetles.
2. **Build a baseline**: Start with a simple null model (climatology or persistence). Submit and get scored.
3. **Iterate**: Build a more complex model (add weather drivers, use ML, or build a process model). Submit again. Compare skill improvement.
4. **Document**: Keep a model development log. Record what you tried, what worked, and what didn't.
5. **Compare approaches**: If time allows, build both a process-based and an ML-based forecast for the same target. When does each win?

The challenge has [detailed documentation](https://projects.ecoforecast.org/neon4cast-ci/) and [example code](https://github.com/eco4cast/neon4cast-ci) in both R and Python.

**Deliverable**: At least 2 forecast submissions + model development log + 2,000-word comparative analysis.

### Exercise E.4: Independent Climate-Ecology Project
Design your own end-to-end analysis connecting climate data to ecological outcomes. Candidates:
- Climate velocity map for a biodiversity hotspot with species richness overlay
- Historical climate driver attribution for an observed ecological shift (correlating ERA5 trends with GBIF occurrence changes)
- Carbon flux forecast for a NEON site combining flux tower data with climate projections
- Climate-envelope analysis of a rewilding candidate species under multiple SSPs

**Deliverable**: Complete project folder + 2,000-word report.

---

## Cross-Pathway Integration

After completing at least two pathways, do one of the following integration exercises:

### Option 1: Methods Comparison Memo (1,500 words)
Choose a single ecological question and analyze it using methods from two different pathways. For example:
- **SDM + Bayesian**: Fit an SDM using MaxEnt, then refit as a Bayesian PPM with `brms`. Compare predictions, uncertainty estimates, and interpretability.
- **Remote sensing + Networks**: Use remote sensing to map habitat loss, then model how that loss propagates through an ecological network.
- **Climate + SDM**: Build an SDM, project under CMIP6 scenarios processed in Pathway E, and quantify how climate data uncertainty propagates into habitat predictions.

Address: When would you use each approach? What are the trade-offs? Where do they agree and disagree?

### Option 2: Reproducible Reanalysis
Find a published ecological study (from your [journal articles list](../../reading-lists/journal-articles.md)) that uses computational methods. Reproduce their core analysis using open data, then extend it with one improvement (better cross-validation, updated data, additional uncertainty quantification). Document where the original methods fall short.

---

## Reproducibility Standard

Every project in this track must meet the following bar. This is non-negotiable — it's what separates hobby analysis from professional work.

| Requirement | Details |
|---|---|
| **README** | Research question, data sources (with URLs and access dates), analysis workflow, instructions to rerun |
| **Environment lock** | `environment.yml` (conda) or `renv.lock` (R) — exact package versions pinned |
| **Data provenance** | Raw data download scripts (not manual downloads). Note licenses. Include DOIs for GBIF downloads. |
| **Scripted rerun** | A single command (`make all`, `snakemake`, or `bash run.sh`) should reproduce all results from raw data |
| **Code quality** | Functions over copy-paste. Docstrings/comments for non-obvious steps. No hardcoded paths. |
| **Version control** | Git repository with meaningful commit messages. `.gitignore` for data/outputs. |

**Recommended workflow tools**:
- [Snakemake](https://snakemake.readthedocs.io/) or [targets](https://docs.ropensci.org/targets/) (R) for pipeline management
- [Quarto](https://quarto.org/) for cross-language literate programming
- [DVC](https://dvc.org/) for data version control (when datasets are too large for Git)

---

## Deliverables Summary

| Requirement | Minimum |
|---|---|
| Completed pathway projects | 2 pathways, each with at least the guided exercise + independent project |
| Cross-pathway integration | 1 methods comparison memo OR 1 reproducible reanalysis |
| Capstone proposal | 1 proposal (1,000 words) for your [capstone project](../10-capstone-project.md) using computational methods from this track |
| Reproducibility standard | Met for all projects |

### Suggested Combinations by Interest

| Interest | Recommended Pathways | Capstone Direction |
|---|---|---|
| **Rewilding assessment** | A (SDM) + C (Remote Sensing) | Habitat suitability + rewilding progress for a species/site |
| **Climate adaptation** | A (SDM) + E (Climate Forecasting) | Climate-projected range shifts with uncertainty for a conservation plan |
| **Ecosystem monitoring** | C (Remote Sensing) + E (Climate Forecasting) | Satellite-derived ecological forecast for restoration or PA management |
| **Biodiversity modeling** | B (Bayesian) + D (Networks) | Hierarchical community model + interaction network resilience |
| **Conservation planning** | A (SDM) + B (Bayesian) | Bayesian SDM ensemble with proper uncertainty for spatial prioritization |
| **Climate + biodiversity** | D (Networks) + E (Climate Forecasting) | How climate change disrupts ecological interactions |
| **Conservation AI** | F (ML/AI) + C (Remote Sensing) | Deep learning for satellite change detection or camera trap pipelines |
| **Policy + data science** | F (ML/AI) + D (Networks) | NLP on conservation policy + social-ecological network analysis |

---

## Pathway F: Machine Learning and AI for Conservation

**Time**: 25–35 hours  
**Builds on**: Module 5, your existing ML/DS background  
**Language**: Python (primary; PyTorch/TensorFlow ecosystem)

This pathway fills a critical gap between your data science/ML expertise and conservation-specific applications. The field of conservation AI is growing rapidly, and most ecologists lack the ML depth you already have. Your job here is to learn the *domain-specific problems* and *ecological data peculiarities* that make conservation ML different from standard ML.

### Readings

> Tuia, D., Kellenberger, B., Beery, S., Costelloe, B.R., Zuffi, S., Risse, B., ... & Berger-Wolf, T. (2022). Perspectives in machine learning for wildlife conservation. *Nature Communications*, 13, 792.
> - **Read first** — the landscape paper. Maps the entire conservation ML field.

> Beery, S., Van Horn, G., & Perona, P. (2018). Recognition in terra incognita. *ECCV*.
> - The domain shift problem in wildlife image classification. Why standard CV doesn't transfer to new camera trap locations.

> Weinstein, B.G. (2018). A computer vision for animal ecology. *Journal of Animal Ecology*, 87(3), 533–545.

> Christin, S., Hervet, É., & Bhatt, N. (2019). Applications of deep learning in ecology. *Methods in Ecology and Evolution*, 10(10), 1632–1644.
> - Survey of ecological deep learning applications

> Jetz, W., McGowan, J., Rinnan, D.S., et al. (2022). Include biodiversity representation indicators in area-based conservation targets. *Nature Ecology & Evolution*, 6, 123–126.
> - Conservation planning algorithms — connects to spatial prioritization

> Silvestro, D., Goria, S., Sterner, T., & Antonelli, A. (2022). Improving biodiversity protection through artificial intelligence. *Nature Sustainability*, 5, 415–424.

> Lamba, A., Cassey, P., Segaran, R.R., & Koh, L.P. (2019). Deep learning for environmental conservation. *Current Biology*, 29(19), R977–R982.

**NLP for conservation**:
> Di Marco, M., Chapman, S.,';"; et al. (2017). Changing trends and persisting biases in three decades of conservation science. *Global Ecology and Conservation*, 10, 32–42.

> Chowdhury, S., et al. (2023). Three-quarters of insect species are insufficiently represented by protected areas. *One Earth*, 6(2), 139–146.
> - Example of text-mining/data compilation for conservation gaps

### Key Concepts
- **Domain shift**: Why ML models trained on one camera trap location fail at another
- **Long-tailed distributions**: Most species are rare; class imbalance is extreme in ecological data
- **Temporal non-stationarity**: Ecological systems change — models trained on past may not generalize to future
- **Spatial autocorrelation in training/test splits**: Standard random splits lie about performance (see also Pathway A's spatial blocking)
- **Active learning**: Using ML to prioritize which images/samples a human should label
- **Explainability in conservation**: Stakeholders need to understand *why* a model recommends something
- **The Microsoft Planetary Computer and Google Earth Engine**: Cloud platforms for conservation ML
- **Conservation AI platforms**: Wildlife Insights, MegaDetector, BirdNET, Merlin

### Setup: ML Environment Extension

Add to your existing Python environment:
```bash
# Deep learning
conda install -c conda-forge pytorch torchvision torchaudio
pip install timm                 # pretrained image models
pip install ultralytics          # YOLOv8 for detection
pip install segment-anything     # Meta's SAM for segmentation

# NLP
pip install transformers datasets tokenizers
pip install sentence-transformers
pip install spacy && python -m spacy download en_core_web_sm

# Conservation-specific
pip install megadetector          # Microsoft camera trap detector
pip install opensoundscape       # bioacoustics ML

# Geospatial ML
pip install torchgeo             # geospatial deep learning datasets + models
pip install planetary-computer pystac

# Experiment tracking
pip install wandb                # or mlflow
```

### Exercise F.1: Camera Trap ML Pipeline (Guided)
**Task**: Build an end-to-end camera trap image classification pipeline.

This is one of the highest-demand conservation ML applications. You'll go from raw images to species-level classifications with ecological output.

Step-by-step:
1. **Data**: Download a labeled camera trap dataset from [LILA](https://lila.science/) (start with Snapshot Serengeti or Caltech Camera Traps).
2. **MegaDetector**: Run Microsoft's [MegaDetector](https://github.com/microsoft/CameraTraps) to separate empty images from those containing animals. Evaluate: What's the false negative rate? What types of animals does it miss?
3. **Species classification**: Fine-tune a pretrained image classifier (ResNet-50 or EfficientNet via `timm`) for species ID on the non-empty images.
4. **Domain shift experiment**: Train on one location's images, test on another location. Measure the performance drop. Try domain adaptation strategies (fine-tuning, data augmentation, domain-adversarial training).
5. **Long-tail handling**: The dataset will have many images of common species and few of rare ones. Compare strategies: class-weighted loss, oversampling, focal loss.
6. **Ecological output**: Convert model predictions into ecologically useful summaries:
   - Species richness and relative activity index per camera station
   - Temporal activity patterns (which species are diurnal vs. nocturnal?)
   - Occupancy input data format (detection/non-detection histories for Bayesian occupancy models from Pathway B)
7. **Uncertainty quantification**: Implement MC Dropout or temperature scaling to get calibrated confidence scores. Flag low-confidence predictions for human review.

**Deliverable**: End-to-end pipeline notebook + 1,500-word report on domain shift and long-tail challenges.

### Exercise F.2: Deep Learning for Satellite Change Detection
**Task**: Use deep learning to detect restoration or degradation from satellite imagery.

1. **Data**: Use `torchgeo` to load a land use change dataset (e.g., EuroSAT for classification, or SpaceNet for segmentation, or build your own using GEE + labeled polygons for a restoration site from Pathway C).
2. **Baseline**: Train a CNN classifier (or U-Net for segmentation) to categorize land cover types.
3. **Temporal**: Implement a change detection approach:
   - Siamese network comparing two time periods
   - Or temporal stack of multispectral imagery fed to a ConvLSTM
4. **Restoration monitoring application**: Apply to a known restoration site. Can the model detect vegetation recovery? Compare DL-derived change maps to NDVI-based analysis from Pathway C.
5. **Planetary Computer**: Use Microsoft Planetary Computer to access Sentinel-2 imagery and run analysis at scale.

```python
# Example: TorchGeo dataset access
from torchgeo.datasets import EuroSAT
from torchgeo.datamodules import EuroSATDataModule
from torch.utils.data import DataLoader

dataset = EuroSAT(root="data/", download=True)
datamodule = EuroSATDataModule(root="data/", batch_size=32)
```

**Deliverable**: Model training notebook + comparison with traditional remote sensing methods + 1,500-word analysis.

### Exercise F.3: NLP for Conservation Policy and Discourse
**Task**: Apply text analysis to conservation policy or discourse — bridging your PSCI training with ML.

This exercise is uniquely suited to your background. Most conservation ML people can't do NLP; most NLP people don't know conservation policy.

1. **Corpus assembly**: Choose one of:
   - IPBES report sections + CBD COP decisions (multilateral policy)
   - US Endangered Species Act listing decisions (regulatory text)
   - Conservation NGO annual reports over time (organizational discourse)
   - News coverage of rewilding projects (media framing)
   - Academic abstracts from conservation journals (research discourse trends)
2. **Preprocessing**: Clean, tokenize, handle domain-specific vocabulary.
3. **Analysis (choose 2+)**:
   - **Topic modeling**: LDA or BERTopic to identify latent themes. How do topics shift across time, institutions, or geographies?
   - **Semantic similarity**: Use sentence-transformers to measure how policy language converges or diverges across institutions
   - **Named entity recognition**: Extract species names, place names, institutional actors. Build a co-occurrence network.
   - **Sentiment/framing analysis**: How is rewilding framed? What emotional valence do different actors use?
   - **Zero-shot classification**: Use a large language model to classify policy text by conservation strategy type without labeled training data
4. **Political ecology interpretation**: Connect the NLP results to political ecology theory. Whose language dominates? What narratives are reproduced? What is absent?

**Deliverable**: Computational notebook + 2,000-word analytical memo with political ecology framing.

### Exercise F.4: Bioacoustics and Soundscape Ecology (Optional)
**Task**: Use ML for biodiversity monitoring via audio.

1. **Data**: Download labeled audio from [Xeno-canto](https://xeno-canto.org/) (birds) or use [opensoundscape](https://opensoundscape.org/) sample data.
2. **Feature extraction**: Convert audio to spectrograms. Extract acoustic indices (ACI, NDSI, biophony index).
3. **Species detection**: Fine-tune a BirdNET model or train a custom CNN on spectrograms.
4. **Soundscape analysis**: Calculate biodiversity indices from acoustic monitoring across times of day.
5. **Restoration application**: How could soundscape monitoring track restoration success? Design a monitoring protocol.

**Deliverable**: Analysis notebook + 1,000-word protocol proposal.

### Exercise F.5: Independent Conservation ML Project
Design your own project applying ML to a conservation problem. Strong candidates for your profile:
- **Social-ecological NLP**: Text-mine IUCN Red List assessments to extract threat attribution patterns, link to governance data
- **Conflict prediction**: Adapt conflict modeling methods from your PSCI work to predict human-wildlife conflict hotspots using ecological + socioeconomic data
- **Restoration outcome prediction**: Train models to predict restoration success from site characteristics using multi-site restoration databases
- **Conservation planning optimization**: ML-assisted spatial conservation prioritization (extending `prioritizr` with learned cost surfaces)

**Deliverable**: Complete project folder + 2,000-word report.

---

## Recommended Timeline

For someone working through this track alongside other curriculum components:

| Week | Activity |
|---|---|
| 1 | Environment setup. Skim all pathway readings. Choose your two pathways. |
| 2–3 | Pathway 1: readings + guided exercise |
| 4–5 | Pathway 1: independent project |
| 6–7 | Pathway 2: readings + guided exercise |
| 8–9 | Pathway 2: independent project |
| 10 | Cross-pathway integration exercise |
| 11 | Capstone proposal draft |
| 12 | Polish all deliverables, ensure reproducibility standard is met |

Adjust pace as needed. The guided exercises are more structured and faster; the independent projects are where you'll learn the most.

---

→ Return to [Electives and Specializations](../09-electives.md)
