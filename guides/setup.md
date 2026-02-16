# Setup Guide

This guide helps you set up your learning environment for the Self-Taught Conservation Ecology curriculum.

## 📋 Essential Setup

### 1. Create Your Learning Repository

Create a GitHub repository to track your progress and store your work:

```bash
# Create a new repository on GitHub (via web interface)
# Clone it locally
git clone https://github.com/YOUR_USERNAME/conservation-ecology-journey.git
cd conservation-ecology-journey

# Create initial structure
mkdir -p modules/{01-ecology,02-conservation,03-methods,04-genetics,05-landscape,06-restoration,07-rewilding,08-policy,09-capstone}
mkdir -p specializations
mkdir -p reading-notes
mkdir -p projects
mkdir -p resources

# Create a README
echo "# My Conservation Ecology Journey" > README.md
git add .
git commit -m "Initial structure"
git push
```

### 2. Programming Environment

#### Option A: R Setup (Recommended for most modules)

**Install R and RStudio:**
1. Download R: [https://cran.r-project.org/](https://cran.r-project.org/)
2. Download RStudio: [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/)

**Essential R Packages:**
```r
# Data manipulation and visualization
install.packages("tidyverse")  # includes ggplot2, dplyr, tidyr, etc.

# Ecological analysis
install.packages("vegan")      # community ecology
install.packages("BiodiversityR") # biodiversity analysis
install.packages("iNEXT")      # biodiversity estimation
install.packages("unmarked")   # occupancy/abundance models

# Spatial analysis
install.packages("sf")         # spatial data
install.packages("terra")      # raster data
install.packages("raster")     # raster data (older package)
install.packages("rgdal")      # spatial data I/O
install.packages("leaflet")    # interactive maps

# Statistical modeling
install.packages("lme4")       # mixed models
install.packages("glmmTMB")    # generalized mixed models
install.packages("MuMIn")      # model selection
install.packages("DHARMa")     # model diagnostics

# Species distribution modeling
install.packages("dismo")
install.packages("biomod2")
install.packages("ENMeval")

# Reproducible research
install.packages("rmarkdown")
install.packages("knitr")
```

#### Option B: Python Setup (Alternative or complementary)

**Install Python using Anaconda:**
1. Download Anaconda: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
2. Create environment for ecology work:

```bash
# Create new environment
conda create -n ecology python=3.10
conda activate ecology

# Install essential packages
conda install pandas numpy scipy matplotlib seaborn
conda install -c conda-forge geopandas rasterio fiona
conda install scikit-learn jupyter notebook

# Install ecology-specific packages
pip install scikit-bio
pip install pysal
pip install movingpandas
```

**Jupyter Setup:**
```bash
# Install Jupyter Lab
conda install -c conda-forge jupyterlab

# Launch Jupyter
jupyter lab
```

### 3. Reference Management

Choose a reference manager to organize scientific papers:

**Zotero (Recommended - Free):**
- Download: [https://www.zotero.org/](https://www.zotero.org/)
- Install browser connector
- Create collections for each module
- Use Zotero's PDF reader and annotation tools

**Mendeley (Alternative):**
- Download: [https://www.mendeley.com/](https://www.mendeley.com/)

**Tips:**
- Create a collection for each module
- Tag papers by topic
- Make notes as you read
- Export citations for your reports

### 4. Note-Taking & Documentation

**For Code & Analysis:**
- **R Markdown:** Built into RStudio, great for reproducible research
- **Jupyter Notebooks:** For Python, also supports R

**For General Notes:**
- **Obsidian:** Markdown-based, great for connecting ideas [https://obsidian.md/](https://obsidian.md/)
- **Notion:** All-in-one workspace
- **Plain text/Markdown:** Simple and portable

**Recommended Structure:**
```
notes/
├── ecology-fundamentals/
│   ├── population-ecology.md
│   ├── community-ecology.md
│   └── ecosystem-ecology.md
├── conservation-biology/
│   ├── biodiversity-crisis.md
│   └── conservation-strategies.md
└── concepts/
    ├── trophic-cascades.md
    ├── island-biogeography.md
    └── rewilding-approaches.md
```

### 5. Spatial Data & GIS

**QGIS (Free, Open-Source):**
- Download: [https://qgis.org/](https://qgis.org/)
- Great for visualization and analysis
- Extensive plugin ecosystem

**Google Earth Engine (For Remote Sensing):**
- Sign up: [https://earthengine.google.com/](https://earthengine.google.com/)
- Complete tutorials: [https://developers.google.com/earth-engine/tutorials](https://developers.google.com/earth-engine/tutorials)
- Use JavaScript or Python API

### 6. Data Access Setup

Register for accounts to access ecological data:

**Biodiversity Data:**
- **GBIF:** [https://www.gbif.org/](https://www.gbif.org/) (species occurrences)
- **eBird:** [https://ebird.org/](https://ebird.org/) (bird observations)
- **iNaturalist:** [https://www.inaturalist.org/](https://www.inaturalist.org/) (citizen science)
- **IUCN Red List:** [https://www.iucnredlist.org/](https://www.iucnredlist.org/) (species threat status)

**Environmental Data:**
- **WorldClim:** [https://www.worldclim.org/](https://www.worldclim.org/) (climate data)
- **CHELSA:** [https://chelsa-climate.org/](https://chelsa-climate.org/) (high-resolution climate)
- **EarthEnv:** [http://www.earthenv.org/](http://www.earthenv.org/) (environmental layers)

**Ecological Research Data:**
- **Dryad:** [https://datadryad.org/](https://datadryad.org/)
- **figshare:** [https://figshare.com/](https://figshare.com/)
- **EDI:** [https://environmentaldatainitiative.org/](https://environmentaldatainitiative.org/)
- **LTER:** [https://lternet.edu/](https://lternet.edu/)

## 🎓 Optional Tools

### Academic Paper Access

**For Journal Access:**
- Check if your local library has access
- Use **Unpaywall** browser extension for legal open-access versions
- **Google Scholar:** Often links to free PDFs
- **ResearchGate:** Request papers from authors
- Contact authors directly via email

### Time Management

**Pomodoro Technique:**
- Use timer apps (Forest, Pomofocus)
- 25 min focused work, 5 min break

**Project Management:**
- **Trello:** Kanban boards for tracking progress
- **Notion:** Database for tracking readings, exercises, projects
- Simple checklist in your learning repository

### Community Engagement

**Join Online Communities:**
- **r/ecology** (Reddit)
- **Conservation Biology Stack Exchange**
- **Twitter:** Follow #ConservationScience, #Ecology hashtags
- **iNaturalist:** Join local or taxonomic groups

**Academic Social Media:**
- **ResearchGate:** Follow conservation researchers
- **Twitter/X:** Follow ecologists and conservation scientists
- **Mastodon:** Federated science community (fediscience.org)

## 🚀 Getting Started Checklist

Before starting Module 1, ensure you have:

- [ ] Created your learning repository on GitHub
- [ ] Installed R and RStudio (or Python/Anaconda)
- [ ] Installed essential packages
- [ ] Set up reference manager (Zotero or Mendeley)
- [ ] Created note-taking structure
- [ ] Registered for GBIF account
- [ ] Joined at least one online community
- [ ] Set up regular study schedule (15-20 hrs/week)
- [ ] Created a learning journal (physical or digital)

## 📱 Recommended Mobile Apps

- **iNaturalist:** Species identification and recording
- **eBird:** Bird observation logging
- **Seek by iNaturalist:** Plant and animal ID
- **Merlin Bird ID:** Bird identification
- **Obsidian:** Mobile note-taking (syncs with desktop)
- **Forest:** Focus timer and phone usage management

## 💡 Learning Environment Tips

1. **Dedicated Study Space:** Create a consistent, comfortable workspace
2. **Regular Schedule:** Set specific days/times for study
3. **Minimize Distractions:** Use website blockers during study time
4. **Physical Materials:** Print key papers for annotation
5. **Backup Everything:** Use GitHub + cloud storage (Google Drive, Dropbox)
6. **Health:** Take breaks, exercise, maintain work-life balance

## 🆘 Troubleshooting

### R Package Installation Issues

**Problem:** Package won't install  
**Solutions:**
- Update R to latest version
- Install dependencies manually
- On Mac: Install Xcode command line tools
- On Windows: Install Rtools
- Try installing from source: `install.packages("pkg", type="source")`

### Python Package Issues

**Problem:** Import errors  
**Solutions:**
- Ensure correct environment is activated
- Reinstall package: `pip install --upgrade --force-reinstall package`
- Check Python version compatibility

### Spatial Data Issues

**Problem:** CRS/projection errors  
**Solutions:**
- Ensure all layers use same CRS: `st_transform()` in R, `to_crs()` in Python
- Use EPSG codes for consistency (e.g., EPSG:4326 for WGS84)

## 📚 Additional Resources

**R Learning:**
- **R for Data Science:** [https://r4ds.had.co.nz/](https://r4ds.had.co.nz/)
- **Advanced R:** [https://adv-r.hadley.nz/](https://adv-r.hadley.nz/)
- **Geocomputation with R:** [https://r.geocompx.org/](https://r.geocompx.org/)

**Python Learning:**
- **Python for Data Analysis:** [https://wesmckinney.com/book/](https://wesmckinney.com/book/)
- **GeoPandas Documentation:** [https://geopandas.org/](https://geopandas.org/)

**Statistics Refresher:**
- **Seeing Theory:** Visual introduction to probability and statistics
- **StatQuest:** YouTube channel with clear explanations

---

Ready to begin? Head to [Module 1: Ecology Fundamentals](../modules/01-ecology-fundamentals.md)

*Back to [Main Curriculum](../README.md)*
