# Module 3: Ecological Data & Methods

**Duration:** 6 weeks  
**Effort:** 15-20 hours/week

## 📋 Overview

This module bridges theory and practice by teaching you how ecologists collect, analyze, and interpret data. As someone with a data science background, you'll apply your quantitative skills to ecological contexts while learning domain-specific methods.

## 🎯 Learning Objectives

By the end of this module, you should be able to:

1. Design ecological sampling strategies appropriate for different questions
2. Understand common field methods for biodiversity assessment
3. Analyze ecological data using appropriate statistical methods
4. Interpret and critique ecological studies
5. Apply experimental design principles to ecological research
6. Use R or Python for ecological data analysis

## 📚 Required Reading

### Primary Textbooks

- **Krebs, C.J. (2014).** *Ecological Methodology* (3rd ed.). Benjamin Cummings.  
  *(Comprehensive guide to field methods and analysis)*

- **Quinn, G.P. & Keough, M.J. (2002).** *Experimental Design and Data Analysis for Biologists*. Cambridge University Press.  
  *(Excellent for statistical methods in ecology)*

**Reading Schedule:**
- **Weeks 1-2:** Sampling design, study design, bias and error
- **Weeks 3-4:** Field methods (vegetation, wildlife, aquatic surveys)
- **Weeks 5-6:** Data analysis and interpretation

### Key Papers

**Sampling & Design:**
- Yoccoz, N.G., et al. (2001). "Monitoring of biological diversity in space and time." *Trends in Ecology & Evolution* 16(8): 446-453.
- Sutherland, W.J. (Ed.) (2006). *Ecological Census Techniques: A Handbook* (2nd ed.). Cambridge University Press. [Selected chapters]
- MacKenzie, D.I., et al. (2002). "Estimating site occupancy rates when detection probabilities are less than one." *Ecology* 83(8): 2248-2255.

**Statistical Methods:**
- Bolker, B.M., et al. (2009). "Generalized linear mixed models: a practical guide for ecology and evolution." *Trends in Ecology & Evolution* 24(3): 127-135.
- Zuur, A.F., et al. (2010). "A protocol for data exploration to avoid common statistical problems." *Methods in Ecology and Evolution* 1(1): 3-14.

### Free Online Resources

- **R for Data Science:** [https://r4ds.had.co.nz/](https://r4ds.had.co.nz/)
- **Environmental Computing:** [http://environmentalcomputing.net/](http://environmentalcomputing.net/)
- **The Analysis of Biological Data (Whitlock & Schluter):** Companion website with tutorials
- **DataCamp:** Environmental Data Analysis courses

## 💻 Exercises & Activities

### Week 1-2: Study Design & Sampling

**Exercise 3.1: Sampling Design Critique**
- Review 5 published ecological studies
- Evaluate sampling designs: randomization, replication, controls
- Identify potential biases and confounding factors
- Propose improvements
- **Deliverable:** Critical review document

**Exercise 3.2: Power Analysis & Sample Size**
- For a hypothetical study, conduct power analysis
- Determine required sample size for detecting effects of interest
- Explore trade-offs between power, effect size, and resources
- Use R packages: `pwr`, `simr`
- **Deliverable:** Power analysis report with code

**Exercise 3.3: Design Your Own Study**
- Formulate an ecological research question
- Design a sampling strategy (plot placement, sample size, timing)
- Create data collection protocol
- Anticipate challenges and propose solutions
- **Deliverable:** Detailed study design proposal

### Week 3-4: Field Methods

**Exercise 3.4: Survey Method Selection**
- For different taxa (plants, birds, mammals, insects, aquatic), identify appropriate survey methods
- Compare advantages/disadvantages of each method
- Consider detection probability, cost, expertise required
- **Deliverable:** Survey method comparison matrix

**Exercise 3.5: Biodiversity Estimation**
- Using published data or simulated data, estimate species richness
- Apply multiple estimators: rarefaction, Chao, jackknife, bootstrap
- Compare estimates and discuss assumptions
- Use R packages: `vegan`, `iNEXT`, `SpadeR`
- **Deliverable:** Biodiversity estimation analysis with visualizations

**Exercise 3.6: Occupancy Modeling**
- Analyze detection/non-detection data accounting for imperfect detection
- Fit single-season occupancy models
- Interpret occupancy and detection probabilities
- Use R package: `unmarked` or Python: `pyoccupancy`
- **Deliverable:** Occupancy analysis with biological interpretation

### Week 5-6: Data Analysis

**Exercise 3.7: Ecological Data Exploration**
- Work with a real ecological dataset (from Dryad, EDI, or LTER)
- Conduct exploratory data analysis following Zuur et al. (2010) protocol
- Check assumptions, identify outliers, assess collinearity
- Create effective visualizations
- **Deliverable:** Annotated R Markdown or Jupyter notebook

**Exercise 3.8: GLM/GLMM Analysis**
- Analyze count or presence/absence ecological data
- Fit appropriate models (Poisson, negative binomial, binomial)
- Include random effects if hierarchical structure exists
- Model selection using AIC, validation using residual diagnostics
- Use R packages: `lme4`, `glmmTMB`, or Python: `statsmodels`
- **Deliverable:** Complete analysis with interpretation

**Exercise 3.9: Multivariate Analysis**
- Analyze community composition data
- Apply ordination techniques (PCA, NMDS, RDA)
- Test for differences between groups (PERMANOVA)
- Use R package: `vegan`
- **Deliverable:** Multivariate analysis with ecological interpretation

## 🔬 Practical Project

**Project 3: Data Analysis Pipeline**

Create a complete analysis pipeline for an ecological dataset:
1. Define research question and hypotheses
2. Explore and clean data
3. Choose and justify analytical methods
4. Conduct analysis with appropriate statistics
5. Create publication-quality figures
6. Write results section with interpretation
7. Discuss limitations and assumptions

**Deliverable:** Complete reproducible analysis (R Markdown or Jupyter notebook) + 2000-word report

## ✅ Self-Assessment

After completing this module, you should be able to:

- [ ] Design ecologically sound sampling schemes
- [ ] Recognize and avoid common sampling biases
- [ ] Select appropriate field methods for different taxa
- [ ] Account for imperfect detection in biodiversity surveys
- [ ] Conduct power analyses and determine sample sizes
- [ ] Apply GLMs and GLMMs to ecological data
- [ ] Perform multivariate analyses of community data
- [ ] Create reproducible analyses with R or Python
- [ ] Critically evaluate methods sections in papers

## 🔗 Moving Forward

**Prerequisites satisfied for:**
- Module 5: Landscape Ecology
- Specialization: Quantitative Ecology & Modeling
- Specialization: Conservation Data Science

## 📊 Essential R Packages for Ecology

**Data manipulation & visualization:**
- `tidyverse` (dplyr, ggplot2, tidyr, etc.)
- `sf` (spatial data)
- `raster` (raster data)

**Ecological analysis:**
- `vegan` (community ecology, ordination, diversity)
- `unmarked` (occupancy, abundance models)
- `lme4`, `glmmTMB` (mixed models)
- `iNEXT` (biodiversity estimation)
- `MuMIn` (model selection)
- `DHARMa` (residual diagnostics for GLMs)

**Spatial analysis:**
- `sp`, `sf`, `terra` (spatial objects)
- `rgdal`, `rgeos` (spatial operations)
- `raster` (raster analysis)

## 💡 Study Tips for This Module

1. **Code along:** Don't just read—type and run every example
2. **Use real data:** Apply methods to datasets from your interests
3. **Build a methods library:** Save code snippets for future use
4. **Visualize everything:** Plots help you understand data and results
5. **Read the documentation:** Understanding function arguments prevents errors
6. **Peer review:** Share code and get feedback from others

## 📖 Additional Resources

**Books:**
- Bolker, B.M. (2008). *Ecological Models and Data in R*. Princeton University Press.
- Zuur, A.F., et al. (2009). *Mixed Effects Models and Extensions in Ecology with R*. Springer.
- Royle, J.A. & Dorazio, R.M. (2008). *Hierarchical Modeling and Inference in Ecology*. Academic Press.

**Online Resources:**
- **NEON (National Ecological Observatory Network):** Teaching materials and datasets
- **ESA (Ecological Society of America):** Data papers and teaching resources
- **rOpenSci:** R packages for ecological research
- **GitHub:** Explore repositories with ecological analyses

**Online Courses:**
- DataCamp: "Ecological Models and Data in R"
- Coursera: "Statistics with R Specialization" (Duke University)

---

*Previous Module: [02 - Conservation Biology](02-conservation-biology.md)*  
*Next Module: [04 - Conservation Genetics](04-conservation-genetics.md)*
