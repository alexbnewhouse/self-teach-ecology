# Module 5: Landscape Ecology

**Duration:** 6 weeks  
**Effort:** 15-20 hours/week

## 📋 Overview

Landscape ecology examines spatial patterns, processes, and scales in ecosystems. This module teaches you to understand how landscape structure affects biodiversity, design corridors and connectivity networks, and apply landscape principles to conservation planning. Spatial thinking is crucial for effective conservation in fragmented landscapes.

## 🎯 Learning Objectives

By the end of this module, you should be able to:

1. Understand fundamental landscape ecology concepts and metrics
2. Analyze landscape patterns using GIS and spatial statistics
3. Assess habitat fragmentation and its effects on biodiversity
4. Model landscape connectivity for species conservation
5. Apply metapopulation theory to conservation
6. Design corridors and habitat networks
7. Integrate landscape ecology into conservation planning

## 📚 Required Reading

### Primary Textbook

- **Turner, M.G., Gardner, R.H., & O'Neill, R.V. (2015).** *Landscape Ecology in Theory and Practice* (3rd ed.). Springer.  
  *(Comprehensive and accessible, well-illustrated)*

**Alternative:**
- **Forman, R.T.T. (1995).** *Land Mosaics: The Ecology of Landscapes and Regions*. Cambridge University Press.  
  *(Classic text, more conceptual)*

**Reading Schedule:**
- **Weeks 1-2:** Landscape structure, pattern metrics, scale
- **Weeks 3-4:** Fragmentation, edges, matrix effects
- **Weeks 5-6:** Connectivity, metapopulations, corridors

### Key Papers (Required)

**Foundational Concepts:**
- Fahrig, L. (2003). "Effects of habitat fragmentation on biodiversity." *Annual Review of Ecology, Evolution, and Systematics* 34: 487-515.
- Fahrig, L. (2013). "Rethinking patch size and isolation effects: the habitat amount hypothesis." *Journal of Biogeography* 40(9): 1649-1663.
- With, K.A. & Crist, T.O. (1995). "Critical thresholds in species' responses to landscape structure." *Ecology* 76(8): 2446-2459.

**Metapopulations:**
- Hanski, I. (1998). "Metapopulation dynamics." *Nature* 396: 41-49.
- Hanski, I. & Ovaskainen, O. (2000). "The metapopulation capacity of a fragmented landscape." *Nature* 404: 755-758.

**Connectivity:**
- Taylor, P.D., et al. (1993). "Connectivity is a vital element of landscape structure." *Oikos* 68(3): 571-573.
- Crooks, K.R. & Sanjayan, M. (Eds.) (2006). *Connectivity Conservation*. Cambridge University Press. [Selected chapters]
- Rudnick, D.A., et al. (2012). "The role of landscape connectivity in planning and implementing conservation and restoration priorities." *Issues in Ecology* 16: 1-20.

**Applications:**
- Beier, P. & Noss, R.F. (1998). "Do habitat corridors provide connectivity?" *Conservation Biology* 12(6): 1241-1252.
- Hilty, J., et al. (2020). *Guidelines for conserving connectivity through ecological networks and corridors*. IUCN.
- Keeley, A.T.H., et al. (2021). "Connectivity metrics for conservation planning and monitoring." *Biological Conservation* 255: 109008.

## 💻 Exercises & Activities

### Week 1-2: Landscape Pattern Analysis

**Exercise 5.1: Landscape Metrics**
- Obtain land cover data for a region (e.g., NLCD, Copernicus)
- Calculate landscape metrics using FRAGSTATS or R
- Metrics: patch size, edge density, patch density, shape index, aggregation
- Compare metrics across different landscapes or time periods
- Interpret ecological meaning
- **Deliverable:** Landscape pattern analysis with metrics and interpretation
- **Tools:** R packages `landscapemetrics`, `SDMTools`; FRAGSTATS software

**Exercise 5.2: Scale Effects**
- Analyze landscape patterns at multiple spatial scales
- Vary grain size (resolution) and extent
- Assess how patterns change with scale
- Discuss implications for conservation planning
- **Deliverable:** Multi-scale analysis report with visualizations

### Week 3-4: Fragmentation & Habitat Quality

**Exercise 5.3: Fragmentation Analysis**
- Map habitat loss and fragmentation over time
- Use historical and current land cover data
- Quantify changes in: total habitat, patch size distribution, isolation
- Relate fragmentation to biodiversity data (if available)
- **Deliverable:** Fragmentation trend analysis with maps

**Exercise 5.4: Edge Effects Analysis**
- Calculate core area (habitat away from edges)
- Vary edge width based on species or process
- Assess proportion of habitat affected by edges
- Model species responses to edge effects
- **Deliverable:** Edge effects assessment with conservation implications

**Exercise 5.5: Matrix Quality Assessment**
- Evaluate landscape matrix quality for focal species
- Classify matrix by resistance or permeability
- Assess how matrix affects functional connectivity
- **Deliverable:** Matrix permeability map and analysis

### Week 5-6: Connectivity & Corridors

**Exercise 5.6: Structural Connectivity**
- Map potential movement corridors between habitat patches
- Use least-cost path analysis
- Create resistance surfaces based on land cover
- Identify critical linkages and bottlenecks
- **Tools:** R packages `gdistance`, `corridordesign`; QGIS; Linkage Mapper
- **Deliverable:** Corridor map with priority linkages identified

**Exercise 5.7: Circuit Theory Analysis**
- Apply circuit theory to model connectivity
- Identify pinch points and critical areas for connectivity
- Compare results with least-cost paths
- **Tools:** Circuitscape software or R package `circuitscape`
- **Deliverable:** Connectivity analysis using circuit theory

**Exercise 5.8: Network Analysis**
- Represent landscape as a graph (nodes = patches, edges = connections)
- Calculate network metrics: centrality, modularity, resilience
- Identify critical nodes and links
- Simulate effects of node removal (habitat loss)
- **Tools:** R packages `igraph`, `grainscape`
- **Deliverable:** Landscape network analysis with vulnerability assessment

## 🗺️ Capstone Project

**Project 5: Landscape Conservation Design**

Design a conservation landscape for a focal species or ecosystem:

1. **Study Area Selection & Background**
   - Choose region and conservation target
   - Review landscape context and threats
   - Identify existing protected areas

2. **Landscape Pattern Analysis**
   - Map current land cover and habitat
   - Calculate landscape metrics
   - Assess temporal trends in fragmentation

3. **Habitat Suitability Modeling**
   - Build habitat suitability model for focal species
   - Identify high-quality habitat patches
   - Assess habitat availability and configuration

4. **Connectivity Analysis**
   - Model structural and functional connectivity
   - Identify corridors and linkages
   - Map critical areas for connectivity
   - Assess connectivity under future scenarios (optional)

5. **Conservation Network Design**
   - Prioritize patches for protection
   - Design corridor network
   - Identify restoration opportunities
   - Create spatial conservation priorities map

6. **Implementation Strategy**
   - Assess feasibility (land ownership, threats, costs)
   - Propose conservation mechanisms
   - Develop monitoring plan
   - Address potential conflicts

**Deliverable:**
- Series of maps showing analysis results
- Technical report (4000-5000 words)
- Conservation design document with recommendations

## ✅ Self-Assessment

After completing this module, you should be able to:

- [ ] Calculate and interpret landscape metrics
- [ ] Assess habitat fragmentation and its effects
- [ ] Understand scale-dependence in landscape ecology
- [ ] Model landscape connectivity using multiple methods
- [ ] Apply metapopulation concepts to real landscapes
- [ ] Design habitat corridors and networks
- [ ] Use GIS and R for landscape analysis
- [ ] Integrate landscape ecology into conservation planning
- [ ] Critically evaluate corridor and connectivity studies

## 🔗 Moving Forward

**Prerequisites satisfied for:**
- Module 6: Ecosystem Restoration (landscape-scale restoration)
- Module 7: Rewilding (connectivity for large carnivores)
- Module 9: Capstone Project

**Related specializations:**
- Quantitative Ecology & Modeling
- Wildlife Conservation & Management
- Conservation Data Science

## 🗺️ Software & Tools

**GIS:**
- **QGIS:** Free, open-source GIS software
- **ArcGIS:** Industry standard (requires license)
- **Google Earth Engine:** Cloud-based geospatial analysis

**R Packages:**
- `landscapemetrics` - Calculate landscape metrics
- `gdistance` - Least-cost paths and connectivity
- `raster`, `terra` - Raster data manipulation
- `sf` - Vector spatial data
- `igraph` - Network analysis
- `grainscape` - Landscape connectivity analysis

**Specialized Software:**
- **FRAGSTATS:** Landscape metrics (free)
- **Circuitscape:** Circuit theory connectivity (free)
- **Conefor:** Landscape connectivity and networks (free)
- **Linkage Mapper:** Corridor design (QGIS/ArcGIS plugin)
- **Zonation:** Spatial conservation prioritization (free)

## 📊 Data Sources

**Land Cover:**
- **National Land Cover Database (NLCD):** US land cover
- **Copernicus Land Monitoring:** European land cover
- **ESA WorldCover:** Global land cover (10m)
- **Global Forest Watch:** Forest change data

**Habitat Data:**
- **IUCN Habitat Classification**
- **GAP Analysis Project:** US habitat/species data
- **NatureServe:** Species habitat requirements

**Protected Areas:**
- **Protected Planet (WDPA):** Global protected areas database

## 💡 Study Tips for This Module

1. **Think spatially:** Develop intuition for spatial patterns
2. **Use real landscapes:** Apply concepts to places you know
3. **Visualize everything:** Maps are crucial for understanding
4. **Start simple:** Master basic metrics before advanced methods
5. **Understand assumptions:** All connectivity models make assumptions
6. **Connect to theory:** Link landscape patterns to ecological processes
7. **Practice GIS:** Hands-on experience is essential

## 📖 Additional Resources

**Books:**
- Dale, V.H. & Haeuber, R.A. (2001). *Applying Ecological Principles to Land Management*
- Wiens, J.A. & Moss, M.R. (2005). *Issues and Perspectives in Landscape Ecology*
- Wu, J. & Hobbs, R.J. (2007). *Key Topics in Landscape Ecology*

**Reviews & Perspectives:**
- McGarigal, K. & Cushman, S.A. (2002). "Comparative evaluation of experimental approaches to the study of habitat fragmentation effects." *Ecological Applications* 12(2): 335-345.
- Fletcher, R.J., et al. (2018). "Is habitat fragmentation good for biodiversity?" *Biological Conservation* 226: 9-15.

**Tutorials:**
- **landscapemetrics R package vignette:** Excellent tutorials
- **Connectivity conservation online courses**
- **FRAGSTATS documentation**

**Online Courses:**
- Various universities offer landscape ecology MOOCs

---

*Previous Module: [04 - Conservation Genetics](04-conservation-genetics.md)*  
*Next Module: [06 - Ecosystem Restoration](06-ecosystem-restoration.md)*
