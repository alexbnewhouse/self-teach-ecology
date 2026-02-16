# Datasets, Tools & Software

A curated collection of openly available datasets, software tools, and platforms useful throughout this curriculum.

---

## Method Pathways (Quick Start)

Use these pathways to match tools and datasets to your analysis goals.

| Pathway | Core Tools | Starter Datasets | Primary Modules/Tracks |
|---|---|---|---|
| Species distribution modeling | MaxEnt, maxnet, biomod2, ENMeval | GBIF, WorldClim, CHELSA | Module 4, Computational Ecology track |
| Bayesian ecological inference | brms, Stan, PyMC | NEON, LTER, COMPADRE/COMADRE | Module 5, Computational Ecology track |
| Remote sensing and change detection | Google Earth Engine, geemap, terra, sf | Landsat, Sentinel, Global Forest Watch | Module 4, Restoration track |
| Ecological network analysis | igraph, bipartite, NetworkX | Web of Life, interaction datasets | Module 5, Systems track |
| Restoration monitoring | QGIS, field protocols, NDVI workflows | Site surveys, photo points, SoilGrids | Restoration track, practicum |

Related resources:

- [Systems Ecology and Complexity track](../curriculum/tracks/systems-ecology-complexity.md)
- [Restoration Ecology (Advanced) track](../curriculum/tracks/restoration-ecology-advanced.md)
- [Computational Ecology track](../curriculum/tracks/computational-ecology.md)
- [Assessment Rubrics](../assessments/rubrics.md)

---

## Ecological Datasets

### Biodiversity & Species Data

| Dataset | URL | Description | Modules |
|---------|-----|-------------|---------|
| **GBIF** | https://www.gbif.org/ | Global Biodiversity Information Facility — species occurrence records | 1, 4, 7 |
| **IUCN Red List** | https://www.iucnredlist.org/ | Species threat assessments and range maps | 2, 3 |
| **BioTIME** | https://biotime.st-andrews.ac.uk/ | Biodiversity time series database | 1, 5 |
| **NEON** | https://data.neonscience.org/ | US National Ecological Observatory Network | 1, 4, 5 |
| **eBird** | https://ebird.org/science | Bird occurrence data (citizen science) | 4, 5 |
| **iNaturalist** | https://www.inaturalist.org/ | Community naturalist observations | 4, Elective F |
| **Map of Life** | https://mol.org/ | Species range and richness maps | 1, 4 |
| **Living Planet Index** | https://www.livingplanetindex.org/ | Population trend data for vertebrates | 2, 7 |
| **PREDICTS** | https://www.predicts.org.uk/ | Project database on biodiversity responses to land use | 2, 7 |
| **TRY** | https://www.try-db.org/ | Global plant trait database | 1, 5 |
| **LILA** | https://lila.science/ | Labeled camera trap image datasets | 5, Elective F |
| **Movebank** | https://www.movebank.org/ | Animal movement and tracking data | Elective D |

### Spatial & Environmental Data

| Dataset | URL | Description | Modules |
|---------|-----|-------------|---------|
| **WorldClim** | https://www.worldclim.org/ | Global climate data (current and projected) | 4, 7 |
| **CHELSA** | https://chelsa-climate.org/ | High-resolution climate data | 4, 7 |
| **Copernicus Land Monitoring** | https://land.copernicus.eu/ | European land cover, vegetation, water | 4 |
| **NLCD** | https://www.mrlc.gov/ | US National Land Cover Database | 4 |
| **Global Forest Watch** | https://www.globalforestwatch.org/ | Near-real-time deforestation monitoring | 4, Elective F |
| **NASA Earthdata** | https://earthdata.nasa.gov/ | Satellite data (MODIS, Landsat, etc.) | 1, 4 |
| **USGS EarthExplorer** | https://earthexplorer.usgs.gov/ | Landsat, aerial photos, DEMs | 4 |
| **Copernicus Open Access Hub** | https://scihub.copernicus.eu/ | Sentinel satellite imagery | 4 |
| **SoilGrids** | https://soilgrids.org/ | Global soil property maps | 1, 4 |
| **HydroSHEDS** | https://www.hydrosheds.org/ | Hydrological data at global scale | Elective E |

### Protected Areas & Conservation Planning

| Dataset | URL | Description | Modules |
|---------|-----|-------------|---------|
| **WDPA** | https://www.protectedplanet.net/ | World Database on Protected Areas | 2, 4 |
| **KBA** | https://www.keybiodiversityareas.org/ | Key Biodiversity Areas database | 2 |
| **PADDD** | https://www.padddtracker.org/ | Protected area downgrading, downsizing, degazettement | 2, 8 |

---

## Software & Tools

### GIS & Spatial Analysis

| Tool | URL | Language | Description |
|------|-----|----------|-------------|
| **QGIS** | https://qgis.org/ | GUI | Free, open-source GIS platform |
| **Google Earth Engine** | https://earthengine.google.com/ | JS/Python | Cloud-based geospatial analysis |
| **Circuitscape** | https://circuitscape.org/ | Julia | Circuit theory connectivity modeling |
| **Linkage Mapper** | https://linkagemapper.org/ | ArcGIS/OS | Corridor modeling toolkit |

### R Packages

| Package | Purpose | Module |
|---------|---------|--------|
| `vegan` | Community ecology ordination, diversity | 1, 5 |
| `unmarked` | Occupancy and N-mixture models | 5 |
| `dismo` | Species distribution modeling | 4 |
| `biomod2` | Ensemble SDM platform | 4 |
| `ENMeval` | MaxEnt model tuning | 4 |
| `landscapemetrics` | Landscape pattern metrics (FRAGSTATS equivalent) | 4 |
| `sf` | Spatial features and GIS operations | 4 |
| `terra` | Raster and vector spatial data | 4 |
| `gdistance` | Distance-based spatial analysis | 4 |
| `prioritizr` | Systematic conservation planning | 4 |
| `popbio` | Matrix population models | 2 |
| `adehabitatHR` | Home range analysis | Elective D |
| `ctmm` | Continuous-time movement modeling | Elective D |
| `betapart` | Beta diversity partitioning | 1, 5 |
| `indicspecies` | Indicator species analysis | 5 |
| `rstan` / `brms` | Bayesian modeling via Stan | 5 |
| `rgee` | R interface to Google Earth Engine | 4 |

### Python Libraries

| Library | Purpose | Module |
|---------|---------|--------|
| `scikit-learn` | Machine learning | 4, 5, Elective F |
| `xgboost` | Gradient boosting | 4, 5 |
| `tensorflow` / `pytorch` | Deep learning (camera traps, remote sensing) | Elective F |
| `rasterio` | Raster data I/O | 4 |
| `geopandas` | Spatial dataframes | 4 |
| `shapely` | Geometric operations | 4 |
| `earthengine-api` | Google Earth Engine Python API | 4 |
| `pylandstats` | Landscape metrics in Python | 4 |
| `networkx` | Network/graph analysis | 4 |
| `elapid` | Species distribution modeling | 4 |
| `mesa` | Agent-based modeling | 5 |
| `pystan` | Bayesian modeling | 5 |
| `matplotlib` / `seaborn` | Data visualization | All |

### Conservation Planning Software

| Tool | URL | Description |
|------|-----|-------------|
| **Marxan** | https://marxansolutions.org/ | Systematic conservation planning (reserve selection) |
| **Zonation** | https://zonationteam.github.io/Zonation5/ | Spatial conservation prioritization |
| **Wallace EcoMod** | https://wallaceecomod.github.io/ | User-friendly SDM platform (R/Shiny) |

### Population Modeling

| Tool | URL | Description |
|------|-----|-------------|
| **VORTEX** | https://scti.tools/vortex/ | Individual-based PVA simulation |
| **RAMAS** | https://www.ramas.com/ | Spatial population viability analysis |
| **NetLogo** | https://ccl.northwestern.edu/netlogo/ | Agent-based modeling platform |

### Reference Management

| Tool | URL | Description |
|------|-----|-------------|
| **Zotero** | https://www.zotero.org/ | Free, open-source reference manager |
| **Connected Papers** | https://www.connectedpapers.com/ | Visual literature discovery |
| **Semantic Scholar** | https://www.semanticscholar.org/ | AI-powered paper search |
| **Google Scholar** | https://scholar.google.com/ | Standard academic search |

---

## Online Courses & Lectures

### Ecology Foundations

| Course | Platform | Notes |
|--------|----------|-------|
| [EEB 122: Principles of Evolution, Ecology and Behavior](https://oyc.yale.edu/ecology-and-evolutionary-biology/eeb-122) | Yale Open Courses | Full lecture series by Stephen Stearns |
| [MIT 7.014: Introductory Biology](https://ocw.mit.edu/courses/7-014-introductory-biology-spring-2005/) | MIT OCW | Ecology-focused intro bio |
| [Crash Course: Ecology](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNdTKZkV_GiIYXpV9w18s3) | YouTube | Quick concept refresher |
| [Khan Academy: Biology / Ecology](https://www.khanacademy.org/science/biology/ecology) | Khan Academy | Accessible fundamentals |

### Conservation & GIS

| Course | Platform | Notes |
|--------|----------|-------|
| [Spatial Data Science with R](https://rspatial.org/) | Free online | Comprehensive spatial analysis in R |
| [Google Earth Engine Tutorials](https://developers.google.com/earth-engine/tutorials) | Google | Official GEE learning path |
| [Introduction to GIS (QGIS)](https://docs.qgis.org/3.28/en/docs/training_manual/) | QGIS Docs | Official QGIS training |
| [Data Carpentry: Ecology Lessons](https://datacarpentry.org/lessons/#ecology-workshop) | Data Carpentry | R-based ecological data analysis |

---

## Field Guides & Identification Resources

| Resource | URL | Description |
|----------|-----|-------------|
| **iNaturalist** | https://www.inaturalist.org/ | AI-assisted species identification |
| **Merlin Bird ID** | https://merlin.allaboutbirds.org/ | Sound and image-based bird ID |
| **BirdNET** | https://birdnet.cornell.edu/ | Acoustic bird species identification |
| **PlantNet** | https://plantnet.org/ | Plant identification app |
| **Seek by iNaturalist** | https://www.inaturalist.org/pages/seek_app | Real-time species ID using camera |

---

## Key Organizations & Newsletters

| Organization | URL | Why Follow |
|-------------|-----|-----------|
| Society for Conservation Biology (SCB) | https://conbio.org/ | Field's professional society |
| IUCN | https://www.iucn.org/ | Global conservation authority |
| Rewilding Europe | https://rewildingeurope.com/ | Leading European rewilding org |
| American Prairie | https://www.americanprairie.org/ | North American rewilding in action |
| Tompkins Conservation | https://www.tompkinsconservation.org/ | South American rewilding |
| Convention on Biological Diversity | https://www.cbd.int/ | International policy framework |
| IPBES | https://ipbes.net/ | Science-policy interface |
| WildLabs | https://wildlabs.net/ | Conservation technology community |

---

→ Return to [Main Curriculum](../README.md)
