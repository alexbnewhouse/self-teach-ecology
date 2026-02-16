# Module 5: Quantitative Methods for Ecology

**Estimated time**: 60–80 hours  
**Prerequisites**: Module 1 + Data Science background  
**Parallelizable with**: Modules 3–4

---

## Preamble: Leveraging Your Data Science Background

With an MS in Data Science, you already have strong foundations in statistics, machine learning, and programming. This module focuses on **ecology-specific quantitative methods** — the tools and frameworks that ecologists use and that differ from (or extend) standard data science approaches. The emphasis is on ecological applications and the unique statistical challenges of ecological data (spatial autocorrelation, imperfect detection, zero-inflation, temporal dependence, small samples from rare species).

---

## Learning Objectives

By the end of this module, you should be able to:

1. Apply generalized linear models (GLMs) and mixed models to ecological count and proportion data
2. Design and analyze ecological surveys accounting for imperfect detection
3. Conduct population estimation using mark-recapture and occupancy models
4. Perform multivariate analysis of ecological communities (ordination, clustering)
5. Build and interpret mechanistic ecological models
6. Understand Bayesian approaches in ecology
7. Apply machine learning methods appropriately to ecological problems

---

## Unit 5.1: Ecological Statistics Foundations

### Readings

**Primary text**:
> Bolker, B.M. (2008). *Ecological Models and Data in R*. Princeton University Press.
> - **Highly recommended**: An excellent bridge between data science and ecology
> - Full text freely available: https://ms.mcmaster.ca/~bolker/emdbook/
> - Chapters 1–7, 9–10

**Supplementary**:
> Gotelli, N.J., & Ellison, A.M. (2013). *A Primer of Ecological Statistics* (2nd ed.). Sinauer Associates.
> - Chapters 1–4 (review), 7–12

> Zuur, A.F., Ieno, E.N., Walker, N.J., Saveliev, A.A., & Smith, G.M. (2009). *Mixed Effects Models and Extensions in Ecology with R*. Springer.
> - Chapters 1–5 (GLMs, mixed models); essential for ecological data

**Key paper**:
> Anderson, D.R. (2008). *Model Based Inference in the Life Sciences: A Primer on Evidence*. Springer.
> - AIC-based model selection philosophy; widely used in ecology

### Key Concepts
- GLMs for ecological data: Poisson, negative binomial, binomial, zero-inflated models
- Overdispersion and how to handle it
- Random effects and mixed models (GLMMs) — handling nested/hierarchical ecological data
- Model selection: AIC, BIC, cross-validation
- The p-value debate in ecology
- Effect sizes and confidence intervals over null hypothesis significance testing

### Exercise 5.1: GLM/GLMM Analysis
Using an ecological dataset (suggestions: bird counts, plant surveys, species abundance data from NEON):
1. Fit appropriate GLMs (Poisson, negative binomial) to count data
2. Check for overdispersion and zero-inflation
3. Fit a GLMM with random effects (e.g., site, year as random effects)
4. Compare models using AIC
5. Interpret ecological meaning of coefficients

**Deliverable**: R Markdown or Jupyter notebook with full analysis.

---

## Unit 5.2: Occupancy Modeling and Imperfect Detection

### Readings

> MacKenzie, D.I., Nichols, J.D., Royle, J.A., Pollock, K.H., Bailey, L.L., & Hines, J.E. (2018). *Occupancy Estimation and Modeling: Inferring Patterns and Dynamics of Species Occurrence* (2nd ed.). Academic Press.
> - Chapters 1–6

> MacKenzie, D.I., Nichols, J.D., Lachman, G.B., Droege, S., Royle, J.A., & Langtimm, C.A. (2002). Estimating site occupancy rates when detection probabilities are less than one. *Ecology*, 83(8), 2248–2255.
> - **Foundational paper** — introduced the occupancy modeling framework

> Kéry, M., & Royle, J.A. (2016). *Applied Hierarchical Modeling in Ecology: Analysis of Distribution, Abundance and Species Richness in R and BUGS. Volume 1*. Academic Press.
> - Chapters 1–4, 10

### Key Concepts
- The detection process: why failing to detect a species ≠ species absent
- Single-season occupancy models
- Multi-season (dynamic) occupancy models — colonization and extinction
- N-mixture models for abundance estimation
- Survey design for occupancy studies
- Camera trap data and occupancy modeling

### Exercise 5.2: Occupancy Model
Using the R package `unmarked` or Python equivalent:
1. Use a camera trap or survey dataset (simulated or from [LILA](https://lila.science/) camera trap repositories)
2. Fit a single-season occupancy model
3. Estimate detection probability and occupancy probability
4. Explore how covariates affect detection and occupancy
5. Discuss: Why is accounting for imperfect detection critical for conservation monitoring?

**Deliverable**: Analysis notebook with model results and ecological interpretation.

---

## Unit 5.3: Population Estimation and Mark-Recapture

### Readings

> Williams, B.K., Nichols, J.D., & Conroy, M.J. (2002). *Analysis and Management of Animal Populations*. Academic Press.
> - Chapters 14–18 (mark-recapture theory)

> Royle, J.A., & Dorazio, R.M. (2008). *Hierarchical Modeling and Inference in Ecology*. Academic Press.
> - Chapters 5–7

**Key papers**:
> Jolly, G.M. (1965). Explicit estimates from capture-recapture data with both death and immigration-stochastic model. *Biometrika*, 52(1/2), 225–247.

> Seber, G.A.F. (1965). A note on the multiple-recapture census. *Biometrika*, 52(1/2), 249–259.

### Key Concepts
- Lincoln-Petersen estimator and its assumptions
- Jolly-Seber open population models
- Robust design for population estimation
- Spatial capture-recapture (SCR) models
- Distance sampling
- eDNA-based detection and abundance estimation

---

## Unit 5.4: Multivariate Community Ecology

### Readings

> Legendre, P., & Legendre, L. (2012). *Numerical Ecology* (3rd English ed.). Elsevier.
> - Chapters 1–2, 7–9; the definitive reference for multivariate ecological methods

> Borcard, D., Gillet, F., & Legendre, P. (2018). *Numerical Ecology with R* (2nd ed.). Springer.
> - Practical companion to Legendre & Legendre; all analyses in R

### Key Concepts
- Distance/dissimilarity measures for ecological data (Bray-Curtis, Jaccard, UniFrac)
- Ordination methods: PCA, CA, NMDS, RDA, CCA
- Permutational MANOVA (PERMANOVA/ADONIS)
- Indicator species analysis
- Beta diversity partitioning
- Community-level habitat associations

### Exercise 5.3: Community Analysis
Using a multivariate ecological dataset (e.g., from BioTIME, NEON, or vegan package example data):
1. Calculate community dissimilarity matrices
2. Perform NMDS ordination and interpret axes
3. Test for community differences across groups (PERMANOVA)
4. Identify indicator species
5. Relate community composition to environmental gradients (CCA/RDA)

**Tools**: R packages `vegan`, `indicspecies`, `betapart`

**Deliverable**: Community analysis notebook with ordination plots and interpretation.

---

## Unit 5.5: Bayesian Methods in Ecology

### Readings

> Kéry, M. (2010). *Introduction to WinBUGS for Ecologists: Bayesian Approach to Regression, ANOVA, Mixed Models and Related Analyses*. Academic Press.
> - Chapters 1–8; gentle introduction with ecological examples

> Hobbs, N.T., & Hooten, M.B. (2015). *Bayesian Models: A Statistical Primer for Ecologists*. Princeton University Press.
> - Chapters 1–7; more theoretical depth

> Ellison, A.M. (2004). Bayesian inference in ecology. *Ecology Letters*, 7(6), 509–520.

### Key Concepts
- Bayesian inference: priors, likelihoods, posteriors
- MCMC sampling (Gibbs, Metropolis-Hastings, Hamiltonian MC)
- Hierarchical/multilevel models in a Bayesian framework
- Informative vs. non-informative priors in ecology
- Model comparison: DIC, WAIC, LOO-CV
- When Bayesian analysis is particularly useful (small samples, prior information, complex hierarchies)

### Exercise 5.4: Bayesian Ecological Model
Using Stan (`rstan`/`pystan`) or JAGS:
1. Refit one of your earlier models in a Bayesian framework
2. Specify ecologically meaningful priors
3. Assess convergence (Rhat, trace plots, effective sample size)
4. Compare posterior estimates with frequentist results
5. Discuss: When does a Bayesian approach add value in ecological studies?

**Deliverable**: Bayesian analysis notebook with model code, diagnostics, and comparison.

---

## Unit 5.6: Ecological Modeling and Simulation

### Readings

> Soetaert, K., & Herman, P.M.J. (2009). *A Practical Guide to Ecological Modelling*. Springer.
> - Chapters 1–6; introduction to mechanistic modeling

> Railsback, S.F., & Grimm, V. (2019). *Agent-Based and Individual-Based Modeling: A Practical Introduction* (2nd ed.). Princeton University Press.
> - Chapters 1–8; for building agent-based ecological models

> Grimm, V., Berger, U., Bastiansen, F., et al. (2006). A standard protocol for describing individual-based and agent-based models. *Ecological Modelling*, 198(1-2), 115–126.
> - The "ODD protocol" for documenting ecological simulations

### Key Concepts
- Mechanistic vs. statistical models
- Differential equation models in ecology
- Individual-based models (IBMs) / agent-based models (ABMs)
- Sensitivity analysis and parameter estimation
- Scenario modeling for conservation
- Coupled human-natural systems models

### Exercise 5.5: Agent-Based Ecological Model
Using NetLogo, Mesa (Python), or R:
1. Build an agent-based model of a predator-prey system or a rewilding scenario
2. Include spatial heterogeneity (habitat quality variation)
3. Implement and test a rewilding intervention (e.g., predator reintroduction, corridor creation)
4. Run sensitivity analysis on key parameters
5. Document using the ODD protocol

**Deliverable**: Model code, ODD documentation, and 1,000-word results summary.

---

## Unit 5.7: Machine Learning in Ecology

### Readings

> Christin, S., Hervet, É., & Lecomte, N. (2019). Applications for deep learning in ecology. *Methods in Ecology and Evolution*, 10(10), 1632–1644.

> Tabak, M.A., Norouzzadeh, M.S., Wolfson, D.W., et al. (2019). Machine learning to classify animal species in camera trap images: Applications in ecology. *Methods in Ecology and Evolution*, 10(4), 585–590.

> Lucas, T.C.D. (2020). A translucent box: Interpretable machine learning in ecology. *Ecological Monographs*, 90(4), e01422.

### Key Concepts
- Random forests and gradient boosting for ecological prediction
- Deep learning for image classification (camera traps, remote sensing)
- Acoustic monitoring and automated species identification
- eDNA metabarcoding analysis
- When ML is appropriate vs. when traditional statistical models are better
- Interpretability and ecological insight from ML models

---

## Comprehension Check

1. Why are standard linear models often inappropriate for ecological count data?
2. What is the consequence of ignoring imperfect detection in species surveys?
3. Explain the difference between occupancy and abundance, and how each is estimated.
4. When would you choose NMDS over PCA for community analysis?
5. What is the ecological advantage of hierarchical/multilevel models?
6. How do Bayesian priors interact with data, and when are priors particularly influential?
7. When is a machine learning approach more appropriate than a mechanistic model (and vice versa)?

---

## Synthesis Prompt

**Design and execute a complete quantitative ecological analysis** (2,000+ words with code):

> *"Using a publicly available ecological dataset, address a conservation-relevant question. Your analysis should include appropriate data exploration, model selection, parameter estimation, and ecological interpretation. Justify every methodological choice. This should read like the Methods and Results sections of a peer-reviewed paper."*

---

→ Next: [Module 6: Conservation Genetics](06-conservation-genetics.md)
