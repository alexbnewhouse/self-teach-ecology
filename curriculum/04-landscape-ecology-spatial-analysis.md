# Module 4: Landscape Ecology & Spatial Analysis

**Estimated time**: 60–80 hours  
**Prerequisites**: Modules 1–2  
**Parallelizable with**: Modules 3, 5

---

## Learning Objectives

By the end of this module, you should be able to:

1. Apply landscape ecology theory to conservation and rewilding contexts
2. Quantify landscape pattern using spatial metrics (connectivity, fragmentation, patch dynamics)
3. Use GIS and remote sensing tools for ecological analysis
4. Conduct species distribution modeling (SDM) using your data science skills
5. Evaluate landscape-scale conservation planning approaches
6. Integrate spatial analysis with the rewilding frameworks from Module 3

---

## Unit 4.1: Landscape Ecology Theory

### Readings

**Primary text**:
> Turner, M.G., Gardner, R.H., & O'Neill, R.V. (2001). *Landscape Ecology in Theory and Practice: Pattern and Process*. Springer.
> - Chapters 1–5, 8–9

**Alternative/supplementary**:
> Forman, R.T.T. (1995). *Land Mosaics: The Ecology of Landscapes and Regions*. Cambridge University Press.
> - Chapters 1–6; classic comprehensive treatment

**Seminal papers**:
> With, K.A., & Crist, T.O. (1995). Critical thresholds in species' responses to landscape structure. *Ecology*, 76(8), 2446–2459.

> Fahrig, L. (2003). Effects of habitat fragmentation on biodiversity. *Annual Review of Ecology, Evolution, and Systematics*, 34, 487–515.

> Fahrig, L. (2017). Ecological responses to habitat fragmentation per se. *Annual Review of Ecology, Evolution, and Systematics*, 48, 1–23.
> - Important update: argues that fragmentation per se (independent of habitat loss) may not always be harmful

### Key Concepts
- Landscape structure: patch, matrix, corridor, mosaic
- Scale dependence: grain, extent, and the modifiable areal unit problem
- Landscape heterogeneity and its ecological effects
- Habitat fragmentation vs. habitat loss (Fahrig's important distinction)
- Percolation theory and connectivity thresholds
- Edge effects and patch shape
- Landscape-scale disturbance regimes (fire, flood, wind)

---

## Unit 4.2: Connectivity and Corridors

### Readings

> Crooks, K.R., & Sanjayan, M. (Eds.). (2006). *Connectivity Conservation*. Cambridge University Press.
> - Chapters 1–4, 17–19

> Saura, S., & Pascual-Hortal, L. (2007). A new habitat availability index to integrate connectivity in landscape conservation planning: Comparison with existing indices and application to a case study. *Landscape and Urban Planning*, 83(2-3), 91–103.

> McRae, B.H., Dickson, B.G., Keitt, T.H., & Shah, V.B. (2008). Using circuit theory to model connectivity in ecology, evolution, and conservation. *Ecology*, 89(10), 2712–2724. https://doi.org/10.1890/07-1861.1

> Hilty, J., Worboys, G.L., Keeley, A., Woodley, S., Lausche, B., Locke, H., ... & Tabor, G.M. (2020). Guidelines for conserving connectivity through ecological networks and corridors. *IUCN Best Practice Protected Area Guidelines Series No. 30*. IUCN.

### Key Concepts
- Structural vs. functional connectivity
- Wildlife corridors: design principles and evidence
- Graph theory and network analysis in landscape ecology
- Circuit theory for modeling movement (Circuitscape)
- Stepping stones and habitat networks
- Connectivity conservation for rewilding (linking cores — the "3 Cs")

### Exercise 4.1: Connectivity Analysis
Using Python or R with spatial packages:
1. Obtain land cover data for a region (e.g., from [Copernicus Land Monitoring](https://land.copernicus.eu/) or [NLCD](https://www.mrlc.gov/))
2. Classify habitat vs. non-habitat for a focal species
3. Calculate landscape connectivity metrics (e.g., using `landscapemetrics` R package or `pylandstats` Python package)
4. Identify potential corridors using least-cost path or circuit theory (Circuitscape)
5. Discuss: How does connectivity relate to rewilding goals?

**Tools**:
- [Circuitscape](https://circuitscape.org/) — Circuit-theory-based connectivity modeling
- [Linkage Mapper](https://linkagemapper.org/) — ArcGIS/open-source corridor modeling
- R packages: `landscapemetrics`, `gdistance`, `igraph`
- Python: `pylandstats`, `networkx`, `rasterio`

**Deliverable**: Spatial analysis notebook with maps and 800-word interpretation.

---

## Unit 4.3: Remote Sensing for Ecology

### Readings

> Pettorelli, N. (2013). *The Normalized Difference Vegetation Index*. Oxford University Press.
> - Concise, accessible introduction to NDVI and remote sensing in ecology

> Turner, W., Spector, S., Gardiner, N., Fladeland, M., Sterling, E., & Steininger, M. (2003). Remote sensing for biodiversity science and conservation. *Trends in Ecology & Evolution*, 18(6), 306–314.

> Rose, R.A., Byler, D., Eastman, J.R., et al. (2015). Ten ways remote sensing can contribute to conservation. *Conservation Biology*, 29(2), 350–359.

> Jetz, W., McGowan, J., Rinnan, D.S., et al. (2022). Include biodiversity representation indicators in area-based conservation targets. *Nature Ecology & Evolution*, 6(2), 123–126.

### Key Concepts
- Satellite imagery types (optical, radar, LiDAR)
- Vegetation indices: NDVI, EVI, and their ecological applications
- Land cover classification
- Change detection (deforestation, habitat loss monitoring)
- Spatial and temporal resolution trade-offs
- Drone-based ecological monitoring
- Google Earth Engine for large-scale analysis

### Exercise 4.2: Remote Sensing Analysis
Using Google Earth Engine (free), Python (`earthengine-api`), or R (`rgee`):
1. Select a rewilding or conservation area
2. Calculate NDVI trends over the past 20 years using Landsat or Sentinel-2 data
3. Detect land cover change (e.g., forest regrowth, urbanization)
4. Compare vegetation dynamics inside vs. outside protected areas
5. Discuss: What can remote sensing tell us about rewilding progress?

**Resources**:
- [Google Earth Engine](https://earthengine.google.com/) — Cloud-based geospatial analysis
- [Copernicus Open Access Hub](https://scihub.copernicus.eu/) — Sentinel satellite data
- [USGS EarthExplorer](https://earthexplorer.usgs.gov/) — Landsat and other satellite data

**Deliverable**: Analysis notebook with temporal NDVI maps and interpretation.

---

## Unit 4.4: Species Distribution Modeling

### Readings

**Primary text** (leveraging your ML/stats background):
> Franklin, J. (2010). *Mapping Species Distributions: Spatial Inference and Prediction*. Cambridge University Press.
> - Chapters 1–6, 8–9

**Key papers**:
> Elith, J., & Leathwick, J.R. (2009). Species distribution models: Ecological explanation and prediction across space and time. *Annual Review of Ecology, Evolution, and Systematics*, 40, 677–697.

> Elith, J., Phillips, S.J., Hastie, T., Dudík, M., Chee, Y.E., & Yates, C.J. (2011). A statistical explanation of MaxEnt for ecologists. *Diversity and Distributions*, 17(1), 43–57.

> Merow, C., Smith, M.J., & Silander, J.A. Jr. (2013). A practical guide to MaxEnt for modeling species' distributions: What it does, and why inputs and settings matter. *Ecography*, 36(10), 1058–1069.

> Zurell, D., Franklin, J., König, C., et al. (2020). A standard protocol for reporting species distribution models. *Ecography*, 43(9), 1261–1277.

### Key Concepts
- Presence-only vs. presence-absence models
- Environmental predictors (climate, topography, land cover, soil)
- MaxEnt: the most widely used SDM algorithm
- Ensemble modeling approaches
- Model evaluation: AUC, TSS, calibration
- Spatial autocorrelation and its effects on SDMs
- Projecting distributions under climate change scenarios
- Conservation applications: identifying priority areas, predicting range shifts

### Exercise 4.3: Species Distribution Model
Build a species distribution model using your ML background:
1. Select a species relevant to rewilding (e.g., a candidate for reintroduction)
2. Obtain occurrence data from [GBIF](https://www.gbif.org/)
3. Obtain environmental predictors from [WorldClim](https://www.worldclim.org/) and/or [CHELSA](https://chelsa-climate.org/)
4. Build an SDM using MaxEnt or an ensemble approach (random forest, BRT, GLM)
5. Evaluate model performance
6. Project current and future suitable habitat
7. Discuss conservation implications

**Tools**:
- R: `dismo`, `biomod2`, `ENMeval`, `sdm`
- Python: `elapid`, `scikit-learn`, `xgboost`
- [Wallace EcoMod](https://wallaceecomod.github.io/) — User-friendly SDM platform built in R/Shiny

**Deliverable**: Full SDM analysis notebook with maps, model diagnostics, and 1,000-word discussion.

---

## Unit 4.5: Landscape-Scale Conservation Planning

### Readings

> Margules, C.R., & Pressey, R.L. (2000). Systematic conservation planning. *Nature*, 405(6783), 243–253.
> - Already encountered in Module 2; re-read with deeper spatial analysis focus

> Moilanen, A., Wilson, K.A., & Possingham, H.P. (Eds.). (2009). *Spatial Conservation Prioritization: Quantitative Methods and Computational Tools*. Oxford University Press.
> - Chapters 1–5, 12–15

> Beyer, H.L., Dujardin, Y., Watts, M.E., & Possingham, H.P. (2016). Solving conservation planning problems with integer linear programming. *Ecological Modelling*, 328, 14–22.

**Conservation planning tools**:
> Ball, I.R., Possingham, H.P., & Watts, M. (2009). Marxan and relatives: Software for spatial conservation prioritisation. In *Spatial Conservation Prioritization* (pp. 185–195). Oxford University Press.

### Key Concepts
- Systematic conservation planning framework
- Complementarity and irreplaceability
- Cost-effectiveness in reserve design
- Marxan and Zonation software
- Integrating connectivity into spatial planning
- Conservation planning under climate change

### Exercise 4.4: Conservation Prioritization
Using Marxan, Zonation, or the R package `prioritizr`:
1. Define conservation features (species, habitat types) for a region
2. Set representation targets (e.g., protect 30% of each habitat type)
3. Include cost data (e.g., land values, opportunity costs)
4. Run the optimization and map priority areas
5. Compare results with existing protected area networks
6. Discuss: How would you incorporate rewilding objectives into spatial planning?

**Deliverable**: Spatial planning analysis with maps and 1,000-word report.

---

## Comprehension Check

1. What is the difference between structural and functional connectivity?
2. Explain Fahrig's distinction between habitat fragmentation and habitat loss. Why does this matter for conservation?
3. How does circuit theory improve on least-cost path analysis for modeling animal movement?
4. What are the strengths and limitations of NDVI as an ecological indicator?
5. Why is spatial autocorrelation a problem for species distribution models?
6. Explain the concept of complementarity in systematic conservation planning.
7. How does landscape ecology inform rewilding design (think: cores, corridors, connectivity)?

---

## Synthesis Prompt

**Write a 2,000-word essay or create a technical report** addressing:

> *"Design a landscape-scale rewilding plan for a region of your choice. Integrate spatial analysis (connectivity, SDMs, land cover) with ecological principles (trophic rewilding, corridor design). Justify your choices with reference to landscape ecology theory and include at least one map produced from your own analysis."*

---

→ Next: [Module 5: Quantitative Methods for Ecology](05-quantitative-ecology.md)
