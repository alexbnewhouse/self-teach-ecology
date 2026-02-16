# Specialization: Conservation Data Science

**Duration:** 12-16 weeks  
**Prerequisites:** Module 3 (Ecological Data & Methods), basic programming in R or Python

## 📋 Overview

This specialization bridges data science and conservation, teaching you to apply modern computational and statistical methods to conservation challenges. You'll learn to work with large ecological datasets, build predictive models, apply machine learning, and create data-driven conservation tools.

## 🎯 Learning Objectives

By the end of this specialization, you should be able to:

1. Work with large, complex ecological and spatial datasets
2. Apply machine learning to conservation problems
3. Build species distribution models and predict range shifts
4. Analyze remote sensing data for habitat monitoring
5. Design and implement decision support systems
6. Communicate data insights effectively to diverse audiences
7. Apply reproducible research practices

## 📚 Reading Materials

### Core Texts

- **Zurell, D., et al. (2020).** "A standard protocol for reporting species distribution models." *Ecography* 43(9): 1261-1277.

- **Christin, S., Hervet, É., & Lecomte, N. (2019).** "Applications for deep learning in ecology." *Methods in Ecology and Evolution* 10(10): 1632-1644.

- **Joppa, L.N. (2017).** "The case for technology investments in the environment." *Nature* 552: 325-328.

### Key Papers

**Machine Learning in Ecology:**
- Elith, J. & Leathwick, J.R. (2009). "Species distribution models: Ecological explanation and prediction across space and time." *Annual Review of Ecology, Evolution, and Systematics* 40: 677-697.
- Cutler, D.R., et al. (2007). "Random forests for classification in ecology." *Ecology* 88(11): 2783-2792.
- Tabak, M.A., et al. (2019). "Machine learning to classify animal species in camera trap images: Applications in ecology." *Methods in Ecology and Evolution* 10(4): 585-590.

**Remote Sensing:**
- Pettorelli, N., et al. (2014). "Satellite remote sensing for applied ecologists: opportunities and challenges." *Journal of Applied Ecology* 51(4): 839-848.
- Nagendra, H., et al. (2013). "Remote sensing for conservation monitoring: Assessing protected areas, habitat extent, habitat condition, species diversity, and threats." *Ecological Indicators* 33: 45-59.

**Big Data & AI:**
- Jetz, W., et al. (2019). "Essential biodiversity variables for mapping and monitoring species populations." *Nature Ecology & Evolution* 3(4): 539-551.
- Schneider, F.D., et al. (2019). "Towards mapping the diversity of canopy structure from space with GEDI." *Environmental Research Letters* 14(11): 114014.

## 🔬 Core Skills & Tools

### Programming & Analysis
- **R:** Advanced tidyverse, spatial (sf, terra), modeling (tidymodels, caret)
- **Python:** pandas, scikit-learn, TensorFlow/PyTorch, geopandas
- **SQL:** For database queries
- **Git/GitHub:** Version control and collaboration

### Spatial & Remote Sensing
- **Google Earth Engine:** Large-scale remote sensing analysis
- **QGIS:** Open-source GIS
- **R/Python spatial packages:** terra, raster, sf, geopandas
- **Satellite imagery:** Landsat, Sentinel, MODIS

### Machine Learning
- **Classification:** Random forests, SVM, neural networks
- **Regression:** GLMs, GAMs, boosted regression trees
- **Deep Learning:** CNNs for image classification, RNNs for time series
- **Ensemble methods:** Model stacking and averaging

### Data Management & Visualization
- **Databases:** PostgreSQL/PostGIS
- **Visualization:** ggplot2, matplotlib, plotly, leaflet
- **Dashboards:** Shiny (R), Dash (Python), Tableau
- **Reproducibility:** R Markdown, Jupyter notebooks, Docker

## 💻 Projects & Exercises

### Project 1: Species Distribution Modeling (3-4 weeks)

**Goal:** Build and validate species distribution models (SDMs) using multiple algorithms.

**Tasks:**
1. Obtain species occurrence data (GBIF) and environmental predictors
2. Prepare data: clean occurrences, handle spatial bias, generate pseudo-absences
3. Build SDMs using multiple algorithms: GLM, GAM, Random Forest, MaxEnt, BRT
4. Evaluate models: AUC, TSS, cross-validation
5. Create ensemble predictions
6. Project future distributions under climate scenarios
7. Identify priority conservation areas

**Deliverables:**
- Reproducible analysis (R Markdown/Jupyter)
- Distribution maps (current and future)
- Model evaluation report
- Conservation recommendations

**Resources:**
- R packages: `dismo`, `biomod2`, `ENMeval`, `sdm`
- Python: `scikit-learn` for modeling, `gdal` for spatial data

---

### Project 2: Remote Sensing for Habitat Monitoring (3-4 weeks)

**Goal:** Use satellite imagery to monitor habitat change and assess conservation effectiveness.

**Tasks:**
1. Define study area and conservation question
2. Access satellite imagery (Landsat/Sentinel via Google Earth Engine)
3. Preprocess imagery: cloud masking, atmospheric correction
4. Calculate vegetation indices (NDVI, EVI, NBR)
5. Classify land cover using supervised classification
6. Detect changes over time
7. Assess habitat quality and fragmentation
8. Evaluate protected area effectiveness

**Deliverables:**
- Google Earth Engine scripts
- Land cover maps and change detection results
- Time series analysis of vegetation indices
- Protected area assessment report

**Resources:**
- **Google Earth Engine:** [https://earthengine.google.com/](https://earthengine.google.com/)
- Tutorials: [https://developers.google.com/earth-engine/tutorials](https://developers.google.com/earth-engine/tutorials)
- R package: `rgee` (GEE in R)

---

### Project 3: Camera Trap Image Classification (3-4 weeks)

**Goal:** Build a deep learning model to automatically classify wildlife in camera trap images.

**Tasks:**
1. Obtain camera trap dataset (e.g., Snapshot Serengeti, LILA BC)
2. Explore data: species distribution, image quality, class imbalance
3. Preprocess images: resize, augmentation, normalization
4. Build CNN classifier (transfer learning with ResNet/VGG/EfficientNet)
5. Handle class imbalance and rare species
6. Evaluate model performance by species
7. Implement model deployment strategy

**Deliverables:**
- Trained model with documentation
- Model evaluation metrics and confusion matrices
- Deployment guide for conservation practitioners
- Discussion of limitations and improvements

**Resources:**
- **LILA BC:** Labeled camera trap datasets [https://lila.science/](https://lila.science/)
- TensorFlow/Keras or PyTorch
- Pre-trained models: ImageNet weights

---

### Project 4: Conservation Decision Support Tool (4-5 weeks)

**Goal:** Create an interactive tool to support conservation planning decisions.

**Tasks:**
1. Define decision context and stakeholders
2. Integrate multiple data sources: species, threats, costs, opportunities
3. Implement prioritization algorithms (e.g., Zonation, Marxan principles)
4. Build interactive dashboard/web app
5. Include scenario analysis capabilities
6. Create user documentation
7. Test with potential users

**Deliverables:**
- Interactive web application (Shiny, Dash, or standalone)
- User guide and documentation
- GitHub repository with code
- Presentation for stakeholders

**Resources:**
- **Shiny (R):** [https://shiny.rstudio.com/](https://shiny.rstudio.com/)
- **Dash (Python):** [https://plotly.com/dash/](https://plotly.com/dash/)
- Spatial optimization: `prioritizr` (R), `Marxan`

---

### Project 5: Biodiversity Data Integration & Analysis (3-4 weeks)

**Goal:** Integrate and analyze biodiversity data from multiple sources to assess trends.

**Tasks:**
1. Access data from multiple sources: GBIF, IUCN, Living Planet Database, eBird
2. Clean, harmonize, and integrate datasets
3. Calculate biodiversity indicators (species richness trends, Living Planet Index)
4. Analyze spatial and temporal patterns
5. Identify data gaps and biases
6. Visualize trends for communication
7. Provide recommendations for monitoring

**Deliverables:**
- Data integration pipeline (code)
- Biodiversity trend analysis
- Interactive visualizations
- Data quality assessment report

**Resources:**
- **GBIF API:** `rgbif` (R), `pygbif` (Python)
- **eBird API:** `rebird` (R), `ebird-api` (Python)
- **Living Planet Database:** Available from Living Planet Index

## 📊 Additional Topics (Choose 2-3)

### A. Acoustic Monitoring & Bioacoustics
- Process audio recordings for species detection
- Build acoustic classifiers for birds, bats, amphibians
- Analyze soundscape ecology
- **Tools:** `seewave` (R), `librosa` (Python), BirdNET

### B. Movement Ecology & Telemetry Data
- Analyze GPS tracking data
- Model animal movement and space use
- Assess connectivity and corridors
- **Tools:** `move` (R), `movebank` API, `ctmm` (R)

### C. eDNA Metabarcoding Analysis
- Process high-throughput sequencing data
- Taxonomic assignment and community analysis
- Compare eDNA with traditional surveys
- **Tools:** `dada2` (R), `QIIME2`, `phyloseq` (R)

### D. Social Media & Citizen Science Data
- Mine Twitter/iNaturalist for biodiversity information
- Handle data quality and bias
- Engagement analysis
- **Tools:** Twitter API, iNaturalist API, `rinat` (R)

### E. Optimization for Conservation Planning
- Linear programming for reserve selection
- Multi-objective optimization
- Spatial prioritization algorithms
- **Tools:** `prioritizr` (R), Marxan, Zonation

## ✅ Self-Assessment Checklist

After completing this specialization, you should be able to:

- [ ] Build and validate species distribution models
- [ ] Process and analyze satellite imagery for conservation
- [ ] Apply machine learning to ecological problems
- [ ] Work with big biodiversity data (GBIF, eBird, etc.)
- [ ] Create interactive data visualizations and dashboards
- [ ] Implement deep learning for image/audio classification
- [ ] Design reproducible research workflows
- [ ] Communicate data insights to non-technical audiences
- [ ] Evaluate data quality and bias in ecological datasets
- [ ] Integrate multiple data sources for conservation decisions

## 🌐 Resources & Community

**Online Courses:**
- **Coursera:** "Applied Data Science with Python" (University of Michigan)
- **DataCamp:** "Machine Learning for Ecologists in R"
- **Fast.ai:** Deep learning courses
- **Google Earth Engine:** Official tutorials

**Conferences & Competitions:**
- **GEO for Good Summit:** Earth Engine user conference
- **GBIF Data Challenge:** Annual biodiversity data competition
- **Wildlife Insights:** Camera trap AI challenges
- **Kaggle:** Ecology and conservation competitions

**Communities:**
- **rOpenSci:** R packages for open science
- **EcoDataScience:** UCSB data science group (open materials)
- **SORTEE:** Society for Open, Reliable, and Transparent Ecology and Evolutionary Biology
- **AI for Earth:** Microsoft program supporting conservation tech

**GitHub Organizations:**
- **ropensci:** R packages for data access and analysis
- **pyOpenSci:** Python tools for scientific data
- **Conservation Ecology GitHub Topic:** Explore repositories

## 📖 Additional Reading

**Books:**
- Zurell, D., et al. (2020). *Computational Ecology and Software*.
- Fletcher, R. & Fortin, M.J. (2018). *Spatial Ecology and Conservation Modeling*. Springer.
- Hollister, J. (2020). *Data Science in R: A Gentle Introduction*. Chapman & Hall/CRC.

**Blogs & Websites:**
- **Methods in Ecology and Evolution:** Application papers
- **Towards Data Science:** Machine learning tutorials
- **Google Earth Engine Blog:** Earth observation applications

## 💡 Career Paths

This specialization prepares you for roles such as:
- Conservation Data Scientist
- Remote Sensing Analyst for Conservation
- Biodiversity Informatics Specialist
- Conservation Technology Developer
- Wildlife Monitoring Specialist
- GIS Analyst in Conservation
- Ecological Modeler

---

*Back to [Main Curriculum](../README.md)*
