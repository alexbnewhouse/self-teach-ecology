# Comprehensive research brief for a self-directed master's curriculum in conservation ecology and rewilding

**This document assembles the specific courses, texts, papers, tools, datasets, and structural models needed for a coding agent to audit and revise a GitHub-based, master's-level curriculum in conservation ecology and rewilding.** The target learner holds a PhD-in-progress in Political Science (computational social science) and an MS in Data Science/Analytics, with strong Python, R, PyTorch, ML, and network analysis skills—but no formal ecology training. Every section below contains concrete, citation-level detail organized for direct use in a prompt.

---

## 1. What top ecology MS programs actually require

Analysis of eight leading programs—UC Davis Graduate Group in Ecology, Yale School of the Environment, University of Florida Wildlife Ecology and Conservation, Duke Nicholas School, ETH Zurich Environmental Sciences, University of Montana Wildlife Biology, UW-Madison Wildlife Ecology, and Imperial College Conservation Science—reveals a remarkably consistent core despite variation in structure. **Every program requires or strongly expects four pillars**: (1) core ecology theory (1–2 courses), (2) statistics/quantitative methods (at least 1 course), (3) research methods/design (at least 1 course), and (4) a thesis or capstone project. Most also require graduate seminars. Credit loads range from 30 semester-credits (Montana, UW-Madison) to 120 ECTS (ETH Zurich), typically spanning two years.

### Specific course requirements across programs

**UC Davis** requires ECL 200A and 200B (core ecology series) plus area-of-emphasis coursework across nine tracks including Conservation Ecology, Restoration Ecology, and Ecosystems & Landscape Ecology. Prerequisites include introductory biology, general chemistry, physics, calculus, statistics, and a dedicated intro-ecology course (ESP 100 or EVE 101).

**Yale's MEM** requires 48 credits with four first-year Perspectives & Foundations courses plus statistics, followed by 18 specialization credits. The Ecosystem Management & Conservation specialization includes natural science theory, social science/environmental anthropology theory, and quantitative analysis electives. Yale's MESc requires ENV 550 (Natural Science Research Methods) or ENV 551 (Qualitative Inquiry) plus 18+ thesis research credits.

**Duke's MEM** uses a dual-concentration model: one environmental concentration (Terrestrial & Freshwater Environments is closest to ecology) plus one management concentration (Environmental Analytics & Modeling is the computational option). Prerequisites: calculus and statistics for all students; ecology for the TFE track.

**ETH Zurich's Ecology & Evolution major** requires three foundation courses (Ecology, Evolution, Infectious Disease), ≥12 CP in Advanced Concepts, 6 CP in Technical Competencies spanning quantitative/computational, laboratory/field, and biological diversity expertise, plus a term paper, seminar, 18-week internship, and 6-month thesis.

**Imperial College's MSc Conservation Science** is notable for explicitly accepting students with a 2:1 degree in **any subject**. It provides a pre-course reading list for non-biologists and structures core modules around systems thinking, Theory of Change, decision-making, research methods, and a 5-month independent research project. Imperial's Living Planet MSc at Silwood Park begins with a 6-week skills induction covering ecology fundamentals, field ecology, R programming, statistics, spatial analysis/GIS, and genomics.

### Foundational knowledge assumed for non-biology entrants

Across programs, the assumed prerequisite knowledge includes general biology (1–2 courses), introductory ecology, statistics (descriptive statistics through linear regression), calculus (at least one semester), and often general chemistry. **For a student entering from outside ecology, the critical gaps are**: introductory ecology/general biology, organismal biology (vertebrate biology, plant identification), and field methods. The quantitative prerequisites (statistics, calculus) are already well exceeded by someone with an MS in Data Science.

### Bridge provisions for career-changers

Programs handle non-traditional entrants in several ways. Imperial provides a structured reading list (Tony Juniper's *The Ecology Book*; Aulay MacKenzie's *BIOS Instant Notes in Ecology*; David Macdonald's *Biodiversity Conservation: A Very Short Introduction*). Yale offers pre-enrollment MODs workshops (plant identification, ecosystems management, land measurement). UC Davis directs students to community college courses to fill gaps. ETH Zurich is the least flexible, requiring a strong natural science bachelor's. Montana and UW-Madison allow prerequisite coursework during the program but expect foundational ecology knowledge.

---

## 2. Systems ecology, complexity science, and network ecology

### Foundational texts

- **H.T. Odum (2007)**, *Environment, Power, and Society for the Twenty-First Century*. Columbia University Press. Updated edition of the 1971 original linking energy flows to ecological and social systems.
- **H.T. Odum (1994)**, *Ecological and General Systems: An Introduction to Systems Ecology*. University Press of Colorado. Revised version of the 1983 *Systems Ecology*.
- **Donella Meadows (2008)**, *Thinking in Systems: A Primer*. Chelsea Green Publishing. Accessible introduction to stocks, flows, feedback loops, and leverage points.
- **Gunderson, L.H. & Holling, C.S., Eds. (2002)**, *Panarchy: Understanding Transformations in Human and Natural Systems*. Island Press. The definitive book on panarchy theory and the adaptive cycle (r → K → Ω → α).
- **Sven Erik Jørgensen (2012)**, *Introduction to Systems Ecology*. CRC Press. Integrates thermodynamics, biochemistry, and network theory.

### Seminal papers on resilience and regime shifts

- **Holling, C.S. (1973)**. "Resilience and stability of ecological systems." *Annual Review of Ecology and Systematics* 4: 1–23. The foundational paper introducing ecological resilience.
- **Holling, C.S. (2001)**. "Understanding the complexity of economic, ecological, and social systems." *Ecosystems* 4: 390–405. Introduces panarchy formally.
- **Scheffer, M. et al. (2001)**. "Catastrophic shifts in ecosystems." *Nature* 413: 591–596. Landmark review of regime shifts.
- **Scheffer, M. et al. (2009)**. "Early-warning signals for critical transitions." *Nature* 461: 53–59. Generic early warning signals including critical slowing down and rising variance.
- **Folke, C. (2006)**. "Resilience: The emergence of a perspective for social-ecological systems analyses." *Global Environmental Change* 16(3): 253–267.
- **Walker, B. et al. (2004)**. "Resilience, adaptability and transformability in social-ecological systems." *Ecology and Society* 9(2): 5.

**Key book on tipping points**: Scheffer, M. (2009), *Critical Transitions in Nature and Society*. Princeton University Press. Covers bifurcations, catastrophe theory, and examples from lakes, climate, and society.

### Complexity theory applied to ecosystems

- **Levin, S.A. (1998)**. "Ecosystems and the biosphere as complex adaptive systems." *Ecosystems* 1(5): 431–436. Foundational CAS-ecology paper.
- **Levin, S.A. (1992)**. "The problem of pattern and scale in ecology." *Ecology* 73(6): 1943–1967. MacArthur Award lecture.
- **Solé, R.V. & Bascompte, J. (2006)**, *Self-Organization in Complex Ecosystems*. Princeton University Press. Covers criticality, fractal patterns, and network dynamics.
- **Mitchell, M. (2009)**, *Complexity: A Guided Tour*. Oxford University Press. General introduction.

### Network ecology

**Food webs**: May, R.M. (1972), "Will a large complex system be stable?" *Nature* 238: 413–414. May, R.M. (1973/2001), *Stability and Complexity in Model Ecosystems*, Princeton. Williams, R.J. & Martinez, N.D. (2000), "Simple rules yield complex food webs," *Nature* 404: 180–183. Dunne, J.A., Williams, R.J. & Martinez, N.D. (2002), "Food-web structure and network theory," *PNAS* 99(20): 12917–12922.

**Mutualistic networks**: Bascompte, J. & Jordano, P. (2014), *Mutualistic Networks*, Princeton University Press. Bascompte, J. et al. (2003), "The nested assembly of plant–animal mutualistic networks," *PNAS* 100(16): 9383–9387. Bascompte, J. & Jordano, P. (2007), "Plant-animal mutualistic networks: The architecture of biodiversity," *Annual Review of Ecology, Evolution, and Systematics* 38: 567–593.

**Edited volume**: Pascual, M. & Dunne, J.A., Eds. (2006), *Ecological Networks: Linking Structure to Dynamics in Food Webs*, Oxford University Press.

**Network science foundations**: Barabási, A.-L. (2016), *Network Science*, Cambridge University Press (free online at networksciencebook.com). Newman, M.E.J. (2018), *Networks*, 2nd ed., Oxford University Press.

### Agent-based modeling in ecology

- **Railsback, S.F. & Grimm, V. (2019)**, *Agent-Based and Individual-Based Modeling: A Practical Introduction*, 2nd ed. Princeton University Press. Standard textbook using NetLogo. Companion website: railsback-grimm-abm-book.com.
- **ODD Protocol**: Grimm, V. et al. (2006), *Ecological Modelling* 198: 115–126 (original); Grimm et al. (2010), *Ecological Modelling* 221: 2760–2768 (first update); Grimm et al. (2020), *JASSS* 23(2): 7 (second update).
- **NetLogo**: Free, open-source. URL: https://ccl.northwestern.edu/netlogo/. Includes extensive Models Library with ecological models (predator-prey, fire, disease, flocking).

### Open courseware for this area

**Santa Fe Institute Complexity Explorer** (https://www.complexityexplorer.org): Introduction to Complexity (Melanie Mitchell), Introduction to Agent-Based Modeling (Bill Rand), Nonlinear Dynamics, Fractals and Scaling, Dynamical Systems and Chaos. All free, self-paced, with certificates.

**Other**: Coursera's "Model Thinking" by Scott Page (Michigan); Strogatz, S.H. (2015), *Nonlinear Dynamics and Chaos*, 2nd ed., CRC Press; Hiroki Sayama's free textbook *Introduction to the Modeling and Analysis of Complex Systems* (https://textbooks.opensuny.org/introduction-to-the-modeling-and-analysis-of-complex-systems/).

---

## 3. Restoration ecology

### Core textbooks

- **Palmer, M.A., Zedler, J.B. & Falk, D.A., Eds. (2016)**, *Foundations of Restoration Ecology*, 2nd ed. Island Press. 18 chapters covering ecological dynamics, biodiversity, landscape ecology, population genetics, community assembly, nutrient dynamics, climate change.
- **Holl, K.D. (2020)**, *Primer of Ecological Restoration*. Island Press. 12 chapters; ideal introductory text. Companion teaching resources available online.
- **Howell, E.A., Harrington, J.A. & Glass, S.B. (2012)**, *An Introduction to Restoration Ecology*. Island Press. Developed from 30+ years teaching at UW-Madison; step-by-step framework.
- **Hobbs, R.J., Higgs, E.S. & Hall, C.M., Eds. (2013)**, *Novel Ecosystems: Intervening in the New Ecological World Order*. Wiley-Blackwell. Ecological, social, ethical, and policy dimensions of novel ecosystems.
- **Clewell, A.F. & Aronson, J. (2013)**, *Ecological Restoration: Principles, Values and Structure of an Emerging Profession*, 2nd ed. Island Press.
- **Temperton, V.M. et al., Eds. (2004)**, *Assembly Rules and Restoration Ecology: Bridging the Gap Between Theory and Practice*. Island Press. Key text on community assembly in restoration.

### Key concepts and associated literature

**Reference ecosystems and restoration targets**: Gann, G.D. et al. (2019) SER International Standards (see below); Egan, D. & Howell, E.A., Eds. (2005), *The Historical Ecology Handbook*, Island Press.

**Succession theory**: Walker, L.R. & del Moral, R. (2003), *Primary Succession and Ecosystem Rehabilitation*, Cambridge University Press. Poorter, L. et al. (2023), "Successional theories," *Biological Reviews* 98(6): 2049–2077. Classic models include primary/secondary succession, old-field succession, and the intermediate disturbance hypothesis (Connell, 1978).

**Soil ecology in restoration**: Arbuscular mycorrhizal fungi are critical for plant establishment. Whole-soil microbiome inoculation can accelerate recovery (Wubs et al., 2016). Watson, C.D. et al. (2022), "Global meta-analysis shows progress towards recovery of soil microbiota following revegetation," *Biological Conservation* 272: 109592.

**Plant community assembly**: Three main filters—dispersal limitations, environmental/abiotic filtering, biotic interactions. Priority effects: Weidlich, E.W.A. et al. (2021), *Restoration Ecology* 29: e13317.

**Novel ecosystems debate**: Hobbs, R.J., Higgs, E. & Harris, J.A. (2009), "Novel ecosystems: implications for conservation and restoration," *Trends in Ecology & Evolution* 24(11): 599–605. Critique: Murcia, C. et al. (2014), *TREE* 29(10): 548–553.

### SER standards and frameworks

- **SER International Standards for the Practice of Ecological Restoration**, 2nd ed.: Gann, G.D. et al. (2019), *Restoration Ecology* 27: S1–S46 (open access: https://onlinelibrary.wiley.com/doi/10.1111/rec.13035). Provides the Recovery Wheel, eight guiding principles, six key ecosystem attributes, and adaptive management framework.
- **SER Primer on Ecological Restoration** (2004): Clewell, Aronson & Winterhalder. PDF: https://www.ctahr.hawaii.edu/littonc/PDFs/682_SERPrimer.pdf.
- **FAO, SER & IUCN CEM (2023)**: "Standards of practice to guide ecosystem restoration" for the UN Decade.
- SER website: https://www.ser.org. Certified Ecological Restoration Practitioner (CERP) program available.

### Current debates and frontier research

**Novel ecosystems vs. historical fidelity** remains the central debate. **Large-scale restoration initiatives** include the UN Decade on Ecosystem Restoration (2021–2030, co-led by UNEP and FAO; 1 billion hectares pledged) and the Bonn Challenge (350 million hectares by 2030; 210+ million pledged by 60+ countries). **Peatland rewetting** is a frontier: drained peatlands emit ~2 Gt CO₂/year despite occupying 0.3% of land; Günther, A. et al. (2020), *Nature Communications* 11: 1644, showed rewetting's climate benefits outweigh methane emissions.

### Practical components for self-directed learning

Field skills expected of restoration ecologists include botanical identification, soil sampling, vegetation surveys (quadrat/transect methods), seed ecology, GIS mapping, prescribed fire basics, invasive species management, and monitoring protocol design. Self-directed exercises should include: selecting a local degraded site and documenting conditions using QGIS; establishing photo-monitoring points; conducting vegetation surveys with diversity indices; writing a complete restoration plan following SER standards; and contributing to citizen science via iNaturalist, eBird, or USA National Phenology Network.

---

## 4. Rewilding

### History, theory, and the evolving concept

The term "rewilding" was coined by Dave Foreman in 1992. **Soulé, M. & Noss, R. (1998)**, "Rewilding and Biodiversity: Complementary Goals for Continental Conservation," *Wild Earth* 8(Fall): 18–28, articulated the **"3 C's" framework: Cores, Corridors, and Carnivores**. The concept has evolved through four recognized framings:

1. **Original rewilding** (Soulé & Noss 1998): Continental-scale networks of cores, corridors, and large carnivores.
2. **Pleistocene rewilding** (Donlan et al. 2005/2006): Using extant species as ecological proxies for extinct Pleistocene megafauna. Key papers: Donlan, J. et al. (2005), "Re-wilding North America," *Nature* 436: 913–914; Donlan, C.J. et al. (2006), "Pleistocene Rewilding: An Optimistic Agenda for Twenty-First Century Conservation," *The American Naturalist* 168(5): 660–681.
3. **Trophic rewilding** (Svenning et al. 2016): Species introductions to restore top-down trophic interactions. Svenning, J.-C. et al. (2016), "Science for a Wilder Anthropocene," *PNAS* 113(4): 898–906.
4. **Process-oriented rewilding** (Perino et al. 2019): Three critical interacting processes—trophic complexity, natural disturbances, and dispersal. Perino, A. et al. (2019), "Rewilding Complex Ecosystems," *Science* 364(6438): eaav5570.

### Schools of rewilding and key organizations

**North American**: Wildlands Network (https://wildlandsnetwork.org, founded 1991 as Wildlands Project); The Rewilding Institute (https://rewilding.org, founded 2003 by Foreman). Focus on Eastern/Western Wildways, continental carnivore corridors.

**European**: Rewilding Europe (https://rewildingeurope.com, founded 2011), active in 10+ landscapes across 12 countries. Key initiatives include European Wildlife Bank, Tauros Programme, European Rewilding Network. Rewilding Britain (https://www.rewildingbritain.org.uk, founded 2015), targeting 1 million hectares rewilded; operates the Rewilding Network.

**Passive rewilding**: Navarro, L.M. & Pereira, H.M. (2012), "Rewilding Abandoned Landscapes in Europe," *Ecosystems* 15: 900–912.

### Key books

- **Monbiot, George (2013)**, *Feral: Searching for Enchantment on the Frontiers of Rewilding*. Allen Lane/Penguin. Inspired founding of Rewilding Britain.
- **Tree, Isabella (2018)**, *Wilding: The Return of Nature to a British Farm*. Picador. About the Knepp Estate.
- **Tree, Isabella & Burrell, Charlie (2023)**, *The Book of Wilding: A Practical Guide to Rewilding Big and Small*. Picador.
- **Foreman, Dave (2004)**, *Rewilding North America: A Vision for Conservation in the 21st Century*. Island Press.
- **Stolzenburg, William (2008)**, *Where the Wild Things Were: Life, Death, and Ecological Wreckage in a Land of Vanishing Predators*. Bloomsbury USA.
- **Pettorelli, N., Durant, S.M. & du Toit, J.T., Eds. (2019)**, *Rewilding* (Ecological Reviews). Cambridge University Press. 20 chapters covering history, trophic rewilding, decolonizing rewilding, urban rewilding, auditing rewilding.
- **Vera, F.W.M. (2000)**, *Grazing Ecology and Forest History*. CABI Publishing. Foundational for Oostvaardersplassen and wood-pasture theory.

### Flagship case studies

**Yellowstone wolf reintroduction (1995–96)**: 31 gray wolves reintroduced after ~70-year absence. Tri-trophic cascade: wolves → elk behavioral/population changes → recovery of aspen, cottonwood, willows → return of beavers and songbirds. Key research: Ripple, W.J. & Beschta, R.L. (2012), *Biological Conservation* 145: 205–213. Ripple et al. (2025) reported ~1,500% increase in willow crown volume over 20 years, surpassing 82% of global trophic cascade studies.

**Oostvaardersplassen (Netherlands)**: ~5,600 ha on reclaimed polder. Instigated by Frans Vera to test open wood-pasture hypothesis. Introduced Heck cattle, Konik horses, red deer. Non-intervention policy led to mass starvation (winter 2017–18: ~3,300 animals died), public outcry, and termination as rewilding experiment in 2018. **Cautionary tale** about scale, corridors, predators, and public engagement—but credited with inspiring European rewilding.

**Knepp Estate (UK)**: 3,500-acre former dairy farm in West Sussex, rewilding since 2001 under Isabella Tree and Charlie Burrell. Free-roaming Exmoor ponies, Longhorn cattle, Tamworth pigs, deer. Extraordinary biodiversity recovery including turtle doves, nightingales, purple emperor butterflies, first white storks to breed in UK in centuries. 2024 carbon report showed rewilding sequesters carbon at rates comparable to newly planted native woodland.

**Iberá Wetlands (Argentina)**: 1.3–1.8 million hectares. Led by Fundación Rewilding Argentina. Species reintroduced since 2007: giant anteater, pampas deer, collared peccary, bare-faced curassow, red-and-green macaw, giant river otter. World's first jaguar reintroduction where locally extinct (~70 years); first release January 2021. By 2025, **35+ jaguars roam freely with cubs born in the wild**.

**Pleistocene Park (Siberia)**: 144–160 km² reserve on the Kolyma River, founded by Sergey Zimov. Tests hypothesis that reintroducing large herbivores restores mammoth steppe, compacting snow to stabilize permafrost. Species: Yakutian horses, reindeer, musk ox, European bison, Bactrian camels, yak, plains bison (2023).

**European bison**: Extinct in wild by 1927 (saved from 54 captive animals); first reintroduced to Białowieża Forest (Poland) in 1954. Global free-roaming population grew from ~2,500 to ~7,000–8,000 over the last decade. Yale/Rewilding Europe study (2024) estimated bison capture ~54,000 tonnes CO₂/year in Romania's Țarcu Mountains.

### Current debates

**Ethics**: Oostvaardersplassen raised welfare concerns. Kopina et al. proposed adding "Compassion" as fourth C. **Human dimensions**: Risk of "fortress conservation"; Pettorelli et al. (2019) chapter on "Decolonising Rewilding." **Anthropocene baselines**: Perino et al. (2019) advocate process-oriented approaches over fixed historical targets. **Rewilding vs. traditional conservation**: Mutillod et al. (2024), "Ecological Restoration and Rewilding: Two Approaches with Complementary Goals?" *Biological Reviews* 99(3): 820–836.

### Rewilding and climate

Carbon sequestration through rewilding is documented at multiple scales. Svenning et al. (2018), *Phil. Trans. R. Soc. B* 373: 20170440, found Serengeti wildebeest restoration eliminated wildfire risk capturing 2M tonnes CO₂/year; Congo basin elephant restoration could increase forest carbon by 310M tonnes CO₂/year. The Global Rewilding Alliance (130+ organizations, 70 countries, 100M+ hectares) launched the "Animate the Carbon Cycle" initiative at COP26 led by Prof. Oswald Schmitz (Yale).

---

## 5. Computational and quantitative ecology

This section maps directly to the student's existing computational strengths, identifying how Python, R, PyTorch, ML, and network analysis skills translate to ecological applications.

### Population modeling

**Textbooks**: Caswell, H. (2001), *Matrix Population Models*, 2nd ed., Sinauer/OUP (722 pp., the definitive reference for Leslie matrix models, sensitivity/elasticity analysis). Gotelli, N.J. (2008), *A Primer of Ecology*, 4th ed., Sinauer/OUP (exponential/logistic growth, metapopulations, competition, predation). Morris, W.F. & Doak, D.F. (2002), *Quantitative Conservation Biology*, Sinauer (companion to popbio R package).

**R packages**: `popbio` (matrix-based PVA, Leslie matrices); **VORTEX** (standalone PVA software, most widely used for threatened species); **RAMAS GIS** (commercial PVA with spatial integration).

### Species distribution modeling (SDM)

**MaxEnt**: Java-based software from AMNH (http://biodiversityinformatics.amnh.org/open_source/maxent). Key papers: Phillips, S.J. et al. (2006), *Ecological Modelling* 190: 231–259; Elith, J. et al. (2011), *Diversity and Distributions* 17: 43–57.

**R packages**: `dismo` (SDM with MaxEnt interface, Bioclim, BRT), `biomod2` (ensemble platform running 10+ algorithms), `ENMeval` (automated MaxEnt complexity tuning), `maxnet` (MaxEnt via glmnet, no Java), `sdm` (extensible OO platform), `flexsdm`, `geodata` (downloads WorldClim/CHELSA directly). **Wallace** (https://wallaceecomod.github.io/) is an R Shiny app guiding users from GBIF data acquisition through MaxEnt/maxnet modeling to interactive map projections. Citation: Kass, J.M. et al. (2023), *Ecography* 2023(3): e06547.

**Python**: scikit-learn for RF/BRT/SVM-based SDMs; `elapid` for MaxEnt-style models; R-Python interop via `rpy2`.

### Ecological network analysis

**R packages**: `bipartite` (bipartite networks—pollination, food webs; nestedness, modularity, robustness simulations; Dormann et al., 2008), `igraph` (general network analysis), `enaR` (ecosystem network analysis for energy/nutrient flows; Borrett & Lau, 2014), `cheddar` (food web data), `econetwork`.

**Python**: `igraph` (python-igraph), `NetworkX`, `graph-tool` (C++ with Python bindings). The student's existing network analysis skills in Python transfer directly.

### Remote sensing and GIS

**Google Earth Engine**: https://code.earthengine.google.com (JavaScript), Python API via `earthengine-api`, interactive mapping via `geemap`. Open textbook: Cardille et al. (2024), *Cloud-Based Remote Sensing with Google Earth Engine*, Springer (open access, 55 chapters). NASA ARSET training: https://appliedsciences.nasa.gov.

**R**: `terra` (modern raster/vector, successor to `raster`), `sf` (simple features), `stars` (spatiotemporal arrays), `rgee` (R interface to GEE). **Python**: `rasterio`, `geopandas`, `xarray`, `rioxarray`, `sentinelsat`. **QGIS**: Open-source desktop GIS (https://qgis.org), PyQGIS scripting, integrates GRASS/SAGA/GDAL.

### Machine learning in ecology

**Key review**: Pichler, M. & Hartig, F. (2023), "Machine learning and deep learning—A review for ecologists," *Methods in Ecology and Evolution* 14: 994–1016. Comprehensive starting point.

**Application areas**: Camera trap species ID (CNNs with transfer learning from ImageNet/iNaturalist; Microsoft's **MegaDetector** for automated animal detection); land cover classification (RF, U-Net on Landsat/Sentinel via GEE); acoustic monitoring (**BirdNET** from Cornell Lab for bird sound ID); ecological forecasting (LSTMs, physics-informed neural networks). Tools: PyTorch, TensorFlow, fastai, Hugging Face pre-trained models.

### Core R packages for ecology

| Package | Purpose |
|---------|---------|
| `vegan` | Community ecology: ordination (PCA, NMDS, CCA), diversity, permutation tests |
| `bipartite` | Bipartite ecological network analysis |
| `ape`, `phytools` | Phylogenetics |
| `unmarked` | Occupancy modeling, N-mixture models (frequentist) |
| `ubms` | Bayesian occupancy models via Stan |
| `Distance` | Distance sampling |
| `lme4` | Linear/generalized linear mixed models |
| `brms` | Bayesian multilevel models via Stan |
| `MuMIn` | Multi-model inference |
| `popbio` | Matrix population models |
| `MARSS` | Multivariate autoregressive state-space models |

### Bayesian methods in ecology

**Textbooks**: Hobbs, N.T. & Hooten, M.B. (2015/2024), *Bayesian Models: A Statistical Primer for Ecologists*, Princeton (conceptual introduction, MCMC, model selection). Kéry, M. & Royle, J.A. (2016/2021), *Applied Hierarchical Modeling in Ecology*, Vols. 1–2, Academic Press (distribution/abundance modeling in R and BUGS; companion package `AHMbook`). Kéry, M. (2024), *Applied Statistical Modelling for Ecologists*, Academic Press (Bayesian/likelihood using R, JAGS, NIMBLE, Stan, TMB).

**Software**: Stan (https://mc-stan.org; R via `rstan`/`cmdstanr`, Python via `PyStan`/`CmdStanPy`). `brms` for lme4-like formula syntax with Stan backend. JAGS via `rjags`/`jagsUI`. NIMBLE for flexible compiled models. **Python Bayesian**: PyMC, NumPyro, CmdStanPy.

### Time series analysis for ecological data

**MARSS** package (R): Multivariate autoregressive state-space models (Holmes, Ward & Wills, 2012, *The R Journal* 4(1): 11–19). Applied Time Series Analysis course materials free at https://atsa-es.github.io/atsa-labs/. Other packages: `dlm`, `KFAS`, `bsts`, `mvgam` (GAMs for time series with Stan).

### Open datasets for practice

| Dataset | URL | Access | Description |
|---------|-----|--------|-------------|
| **GBIF** | https://www.gbif.org | R: `rgbif`; Python: `pygbif` | >2 billion occurrence records globally |
| **NEON** | https://www.neonscience.org | R: `neonUtilities` | 81 US field sites, standardized ecological data |
| **eBird** | https://ebird.org | R: `auk`, `rebird` | >1.3 billion bird records |
| **LTER** | https://lternet.edu | Via EDI portal | Decades of data from 28 sites |
| **DataONE** | https://www.dataone.org | R: `dataone` | Federated ecological data repository |
| **Movebank** | https://www.movebank.org | R: `move2` | >7,500 animal tracking studies |
| **LILA** | https://lila.science | Web | Labeled camera trap image datasets |
| **Snapshot Serengeti** | https://lila.science/datasets/snapshot-serengeti/ | Web | ~2.65M sequences, 7.1M images |
| **WorldClim** | https://worldclim.org | R: `geodata` | 19 bioclimatic variables at ~1 km |
| **CHELSA** | https://chelsa-climate.org | Web | Climate data with orographic correction |
| **COMPADRE/COMADRE** | compadre-db.org | R | Plant and animal demographic matrices |
| **Web of Life** | www.web-of-life.es | Web | Ecological interaction networks |
| **TRY** | try-db.org | Web | 3M+ plant trait records |

---

## 6. Conservation biology foundations

### Core textbooks

- **Primack, R.B. (2014)**, *Essentials of Conservation Biology*, 6th ed. Sinauer/OUP. 603 pp. Most comprehensive single-author text.
- **Primack, R.B. & Sher, A.**, *An Introduction to Conservation Biology*, 2nd ed. Sinauer/OUP. Adds chapters on population biology tools and restoration.
- **Sodhi, N.S. & Ehrlich, P.R., Eds. (2010)**, *Conservation Biology for All*. Oxford University Press. **Freely available PDF**: https://conbio.org/publications/free-textbook/.
- **Groom, M.J., Meffe, G.K. & Carroll, C.R. (2006)**, *Principles of Conservation Biology*, 3rd ed. Sinauer. The most comprehensive graduate-level text; 18 chapters.
- **Frankham, R., Ballou, J.D. & Briscoe, D.A. (2010)**, *Introduction to Conservation Genetics*, 2nd ed. Cambridge University Press. 618 pp. The standard for conservation genetics.
- **Turner, M.G., Gardner, R.H. & O'Neill, R.V. (2001/2015)**, *Landscape Ecology in Theory and Practice*, Springer. Foundational for landscape connectivity.

### Island biogeography

MacArthur, R.H. & Wilson, E.O. (1967), *The Theory of Island Biogeography*, Princeton (reprinted 2001 in Princeton Landmarks in Biology). The **species-area relationship** S = cA^z (z typically 0.2–0.35) provides the theoretical basis for understanding how habitat fragments function as ecological "islands." Diamond (1975), "The island dilemma," *Biological Conservation* 7: 129–146, applied the theory to reserve design. The Biological Dynamics of Forest Fragments Project near Manaus (est. 1979 by Lovejoy & Bierregaard) remains the major long-term study of fragmentation effects.

### Metapopulation theory

Hanski, I. (1999), *Metapopulation Ecology*, Oxford University Press. The definitive text covering the Levins model, the incidence function model, and the Glanville fritillary case study. **Source-sink dynamics**: Pulliam, H.R. (1988), "Sources, sinks, and population regulation," *American Naturalist* 132: 652–661. Four conditions for metapopulation persistence: patchy habitat, no single population large enough for long-term survival, no patch too isolated for recolonization, asynchronous local dynamics.

### Minimum viable populations and the 50/500 rule

Shaffer, M.L. (1981), "Minimum population sizes for species conservation," *BioScience* 31: 131–134, introduced the MVP concept. The classic 50/500 rule (Ne ≥ 50 for short-term inbreeding avoidance, Ne ≥ 500 for long-term evolutionary potential) was proposed by Franklin (1980) and Soulé (1980). **This has been updated**: Frankham et al. (2014), *Biological Conservation* 170: 56–63, demonstrated Ne ≥ 50 is inadequate (should be **≥100**) and Ne ≥ 500 is too low (should be **≥1,000**)—effectively a **100/1,000 rule**. The Ne/N ratio averages ~0.10–0.14 across species.

### Landscape connectivity

**Circuitscape** (https://circuitscape.org/): Open-source software modeling connectivity via circuit theory. Based on McRae, B.H. & Beier, P. (2007), *PNAS* 104: 19885–19890. Incorporates multiple dispersal pathways simultaneously. Other tools: Linkage Mapper, Marxan with Zones, Zonation (Moilanen et al., 2009). Fragmentation synthesis: Fahrig, L. (2017), "Ecological responses to habitat fragmentation per se," *AREES* 48: 1–23.

### Conservation genetics essentials

Core concepts: genetic drift (stronger in small populations), inbreeding depression (Florida panther, Isle Royale wolves), **genetic rescue** (introduction of outbred genetic material; Whiteley et al., 2015, *TREE* 30: 42–49), effective population size. **Environmental DNA (eDNA)**: Non-invasive monitoring via genetic material shed into environment; species-specific qPCR and metabarcoding for multi-species detection.

### Threatened species assessment

**IUCN Red List** (https://www.iucnredlist.org/): Nine categories (EX through NE); five quantitative criteria (A–E) covering population reduction, geographic range, small/declining populations, very small populations, and quantitative extinction analysis. Over 172,600 species assessed; ~44,000+ threatened. The newer **IUCN Green Status of Species** assesses recovery and conservation success on an eight-category scale from Extinct in the Wild to Fully Recovered.

**Other frameworks**: CITES (https://cites.org/, Appendices I–III regulating trade), Convention on Biological Diversity (https://www.cbd.int/), **Kunming-Montreal Global Biodiversity Framework** (adopted December 2022; 4 goals, 23 targets for 2030).

### Protected area design

The **SLOSS debate** (Single Large Or Several Small) originated with Diamond (1975) and Simberloff & Abele (1976). Current synthesis: Fahrig (2022), *Biological Reviews* 97: 99–114. **IUCN Protected Area Categories** I–VI range from Strict Nature Reserve to Protected Area with Sustainable Use. **Systematic conservation planning**: Margules, C.R. & Pressey, R.L. (2000), "Systematic conservation planning," *Nature* 405: 243–253. Software: Marxan, Zonation, `prioritizR`. The **30x30 initiative** (Target 3 of the Kunming-Montreal GBF) aims for 30% of terrestrial and marine areas effectively conserved by 2030; currently 17.6% of land and 8.4% of ocean are protected.

### Human dimensions of conservation

Conservation social science: Bennett, N.J. et al. (2017), "Conservation social science," *Biological Conservation* 205: 93–108. Fortress conservation critiques: Brockington, D. (2002), *Fortress Conservation*; Dowie, M. (2009), *Conservation Refugees*. Community-based conservation: Berkes, F. (2004), *Conservation Biology* 18: 621–630. Human-wildlife conflict/coexistence: Nyhus, P.J. (2016), *AREE* 41: 143–171. Environmental justice: Schlosberg, D. (2007), *Defining Environmental Justice*, OUP. The Kunming-Montreal GBF explicitly recognizes Indigenous peoples' rights (Targets 3, 21, 22).

---

## 7. Recommended open educational resources

### MOOCs and online courses

| Course | Platform | Institution | URL |
|--------|----------|-------------|-----|
| Ecology: Ecosystem Dynamics and Conservation | Coursera | AMNH/HHMI | https://www.coursera.org/learn/ecology-conservation |
| Introduction to Biology: Ecology | Coursera | Rice University | https://www.coursera.org/learn/introduction-to-biology-ecology |
| Landscape Ecology | edX | ETH Zurich | https://www.edx.org/learn/environmental-science/eth-zurich-landscape-ecology |
| Environmental DNA | edX | ETH Zurich | https://www.edx.org/learn/ecosystems/ethx-environmental-dna |
| Ecology I: The Earth System | MIT OCW | MIT | https://ocw.mit.edu/courses/1-018j-ecology-i-the-earth-system-fall-2009/ |
| Ecology II: Engineering for Sustainability | MIT OCW | MIT | https://ocw.mit.edu/courses/1-020-ecology-ii-engineering-for-sustainability-spring-2008/ |
| Principles of Evolution, Ecology and Behavior | Yale Open | Yale (Stearns) | https://oyc.yale.edu/ecology-and-evolutionary-biology/eeb-122 |
| Ecology and Wildlife Conservation | FutureLearn | Leeds | https://www.futurelearn.com/courses/ecology-and-wildlife-conservation |
| Introduction to Complexity | SFI | Santa Fe Institute | https://www.complexityexplorer.org |
| Introduction to Agent-Based Modeling | SFI | Santa Fe Institute (Rand) | https://www.complexityexplorer.org/courses/214-introduction-to-agent-based-modeling |
| Model Thinking | Coursera | Michigan (Page) | Coursera |
| Data Science for Ecologists | Edinburgh | Coding Club | https://ourcodingclub.github.io/course.html |

### NCEAS and DataONE

**NCEAS Learning Hub** (https://www.nceas.ucsb.edu/learning-hub): coreR (5-day R immersive), Reproducible Research in R (2-day workshop), Open Science for Synthesis (3-week intensive), Data Management Skillbuilding. Materials available online.

**DataONE** (https://www.dataone.org/training/): 10 CC0-licensed education modules on data management. Skillbuilding Hub: https://dataoneorg.github.io/Education/.

### Open textbooks

- **Environmental Biology** by Matthew R. Fisher (ed.): https://openoregon.pressbooks.pub/envirobiology/ (CC BY 4.0)
- **OpenStax Biology 2e** ecology chapters 44–47: https://openstax.org/books/biology-2e/ (CC BY 4.0)
- **Network Science** by Barabási: http://networksciencebook.com/ (free online)
- Sayama's *Introduction to the Modeling and Analysis of Complex Systems*: https://textbooks.opensuny.org/introduction-to-the-modeling-and-analysis-of-complex-systems/
- **Conservation Biology for All** (Sodhi & Ehrlich): https://conbio.org/publications/free-textbook/ (free PDF)

### YouTube lecture series

- **Crash Course Ecology** (12 episodes by Hank Green, based on Campbell Biology): https://thecrashcourse.com/topic/ecology/
- **Crash Course Biology** (2024, with HHMI BioInteractive): includes ecology, population ecology, conservation biology episodes
- **Yale EEB 122** (Prof. Stephen Stearns): ~36 full university lectures, available at oyc.yale.edu
- **HHMI BioInteractive**: Short films, animations, virtual labs at https://www.biointeractive.org/
- **Complexity Explorer YouTube** channel: Full SFI lecture playlists

### Applied Time Series Analysis for ecology

Free online labs and lectures at https://atsa-es.github.io/atsa-labs/ (Holmes, Ward & Scheuerell, NOAA). Excellent for state-space models, dynamic factor analysis, and multivariate ecological time series.

---

## 8. Self-directed learning pathway models

### The OSSU model as structural template

The **Open Source Society University** Computer Science curriculum (https://github.com/ossu/computer-science, 201k stars) provides the gold standard for GitHub-based self-directed curricula. Key structural elements worth replicating:

- **Four-tier organization**: Intro → Core → Advanced (elective specializations) → Final Project
- **Per-course metadata**: Title with link, provider/platform, prerequisites, estimated duration, recommended sequence
- **Progress tracking**: Google Sheets template for checking off completed courses
- **Quality criteria stated explicitly**: Open enrollment, regular availability, high quality, aligned with published curriculum guidelines
- **Community**: Discord server, GitHub Issues for questions
- **Contributing guidelines** for community improvement

OSSU also maintains **OSSU Bioinformatics** (https://github.com/ossu/bioinformatics)—the closest existing analog to an ecology curriculum—and **OSSU Data Science** (https://github.com/ossu/data-science).

### Existing ecology-relevant GitHub resources

- **Coding Club: Data Science for Ecologists** (University of Edinburgh): https://ourcodingclub.github.io/course.html. 16 core tutorials, 16 quizzes, 3 practical challenges. Three streams: Stats from Scratch, Wiz of Data Vis, Mastering Modelling. Free, self-paced, certificate available.
- **Data Science in Ecology and Environmental Science** (Edinburgh): https://datascienceees.github.io/ — full university course with GitHub Classroom integration.
- **EECB 703** (University of Nevada): https://kevintshoemaker.github.io/EECB-703/ — graduate-level overview of ecology, evolution, conservation.
- **DataONE Education** (GitHub): https://github.com/DataONEorg/Education — open data management modules.

### Best practices for GitHub curriculum design

Successful curricula share these patterns: curated (single best course per topic rather than exhaustive lists), guided by established academic standards, free-first philosophy with cost notes, an Extras section for supplementary resources, contributing guidelines, FAQ, and a changelog. The **OSSU Bioinformatics** model with Trello-based progress tracking and project-based culmination is particularly relevant as a cross-disciplinary science curriculum analogue.

---

## 9. Assessment and capstone project design

### Demonstrating master's-level competency

Comprehensive exams in ecology MS programs typically cover: population ecology (Lotka-Volterra, population growth, life history), community ecology (species interactions, neutral theory, assembly), ecosystem ecology (biogeochemical cycles, trophic dynamics), landscape/spatial ecology, conservation biology (PVA, fragmentation, invasive species), and quantitative methods. A self-directed learner should demonstrate **synthesis across subdisciplines**, critical evaluation of theory and evidence, and ability to design research addressing fundamental ecological questions.

### Self-assessment framework

Research shows people are poor at self-assessment (Kruger & Dunning, 1999), so structured approaches are essential. Recommended framework for this curriculum:

- **Competency grid**: Map skills (statistical analysis, field methods, ecological theory, computational tools) on a beginner-to-expert progression
- **E-portfolio on GitHub**: Document completed projects, annotated reading lists, code, analyses, and written reflections
- **Peer feedback**: Engage with EcoEvoRxiv, ecology communities on Bluesky/Mastodon, R-sig-ecology
- **Capstone project**: Culminating integrative project producing publication-quality output
- **Self-assessment rubric**: Mapped against published comprehensive exam topics from programs like UNR, Dartmouth, UC Santa Cruz

### Ten capstone project ideas combining computation with ecology

1. **Species distribution models for threatened species**: GBIF occurrence data + WorldClim bioclimatic variables → MaxEnt/RF/BRT models projecting climate change impacts on habitat suitability. Skills: SDM, spatial statistics, conservation planning.

2. **Ecological network analysis**: Web of Life or mangal.io interaction network data → nestedness, modularity, robustness simulations, extinction cascade modeling. Skills: Network science, graph theory, stability-complexity debate.

3. **Remote sensing analysis of restoration sites**: Google Earth Engine + Landsat/Sentinel → NDVI time series, change detection, vegetation recovery assessment. Skills: Remote sensing, time series analysis, conservation effectiveness.

4. **Agent-based models of rewilding scenarios**: COMPADRE/COMADRE demographic data + landscape GIS → NetLogo/Mesa simulations of predator-prey reintroduction dynamics. Skills: Simulation, population ecology, trophic interactions.

5. **Network analysis of habitat connectivity**: WDPA protected area shapefiles + land cover data → Circuitscape circuit-theory connectivity, identification of critical corridors. Skills: Landscape ecology, graph theory, conservation planning.

6. **ML for camera trap species ID**: LILA/Snapshot Serengeti datasets → PyTorch transfer learning with ResNet/EfficientNet, occupancy modeling from detections. Skills: Deep learning, computer vision, ecological monitoring.

7. **Time series analysis of LTER data**: Long-term ecological datasets → state-space models, regime shift detection, Bayesian structural time series. Skills: Time series, Bayesian statistics, long-term ecological research.

8. **NLP of conservation policy documents**: ECOLEX/CBD National Reports → topic modeling, sentiment analysis, policy language evolution. Skills: NLP, text mining, interdisciplinary policy analysis. *Uniquely leverages the student's social science background.*

9. **Bayesian population viability analysis**: COMPADRE/COMADRE matrices → hierarchical Bayesian PVA in Stan, comparing management scenarios. Skills: Bayesian statistics, population ecology, uncertainty quantification.

10. **Social-ecological network analysis**: Governance network data + ecological monitoring → two-mode networks, ERGMs, multilayer network analysis. *Best leverages the student's combined computational social science and ecology skills.* Skills: Social-ecological systems, network science, interdisciplinary research.

---

## 10. Academic societies, journals, and conferences

### Key societies

| Society | Website | Student Membership | Key Benefit |
|---------|---------|-------------------|-------------|
| **Ecological Society of America (ESA)** | https://esa.org/ | ~$39/year | SEEDS program, ECOLOG-L, 6 journals |
| **British Ecological Society (BES)** | https://www.britishecologicalsociety.org/ | First 12 months FREE | Research grants, 7 journals |
| **Society for Conservation Biology (SCB)** | https://conbio.org/ | $30/year (low-income) | Free textbook, job board, policy program |
| **Society for Ecological Restoration (SER)** | https://www.ser.org/ | Reduced student rates | Restoration standards, CERP certification |
| **INTECOL** | http://intecol.org/ | Via national societies | International congress |
| **ATBC** | https://tropicalbiology.org/ | Reduced rates | Biotropica journal, tropical focus |

### Key journals ranked by approximate impact

| Journal | IF (approx.) | Publisher/Society | Scope |
|---------|-------------|-------------------|-------|
| Nature Ecology & Evolution | ~10.7 | Springer Nature | Broad high-impact |
| Trends in Ecology & Evolution | ~10.4 | Elsevier/Cell Press | Reviews/opinions |
| Ecology Letters | ~8.0 | Wiley/BES/CNRS | Short high-impact letters |
| Conservation Letters | ~7.7 | Wiley/SCB | Conservation-policy interface |
| Global Change Biology | ~5.0 | Wiley | Climate change × ecosystems |
| Frontiers in Ecology & Environment | High | Wiley/ESA | Accessible broad ecology |
| Global Ecology & Biogeography | ~6.2 | Wiley | Macroecology, biogeography |
| Conservation Biology | ~5.2 | Wiley/SCB | Conservation science |
| Methods in Ecology & Evolution | ~5.5 | Wiley/BES | New methods and tools |
| Journal of Applied Ecology | ~5.0 | Wiley/BES | Applied ecological research |
| Ecological Applications | ~4.6 | Wiley/ESA | Applied ecology |
| Ecology | ~4.4 | Wiley/ESA | Fundamental ecology |
| Biological Conservation | ~4.9 | Elsevier | Broad conservation |
| Restoration Ecology | ~2.5 | Wiley/SER | Restoration practice |
| Ecography | ~4.5 | Wiley/Nordic Soc. | Spatial ecology |

### Major conferences

- **ESA Annual Meeting 2026**: July 26–31, Salt Lake City, Utah. Theme: "Ecology in an Era of Uncertainty." ~3,500 attendees. Abstract deadline: February 19, 2026.
- **NACCR 2026** (North American Congress for Conservation & Restoration): July 12–16, Milwaukee, Wisconsin. Co-hosted by SER and SCB.
- **BES Annual Meeting**: December annually (Edinburgh in 2025; 2026 TBD). ~1,500 delegates. Virtual attendance available.
- **ICCB**: Biennial (2025 Brisbane; 2027 Mexico). Has offered fully virtual options.
- **SFI Complex Systems Summer School**: Annual 3-week intensive for grad students; faculty includes Jennifer Dunne (food webs) and Sonia Kéfi (resilience).

### Preprint servers

**EcoEvoRxiv** (https://ecoevorxiv.org/): Not-for-profit preprint server run by SORTEE, hosted by California Digital Library. Accepts preprints in English, Spanish, Portuguese, French; integrates with Peer Community In review service. **bioRxiv** ecology section is more widely known. ~72.5% of ecology journals explicitly permit preprint posting.

---

## Recommended curriculum structure for the coding agent

Based on the research above, the coding agent should audit and organize the curriculum into a structure mirroring the OSSU model with ecology-specific adaptations:

**Tier 0 — Prerequisites/Bridge (for non-biologists)**
Fill gaps in general biology, introductory ecology, and organismal biology using open resources (OpenStax Biology 2e, Crash Course Ecology, Yale EEB 122, MIT OCW Ecology I). Estimated 2–3 months at 15 hrs/week.

**Tier 1 — Core Ecology & Conservation (required)**
Population ecology, community ecology, ecosystem ecology, landscape ecology, conservation biology, statistics for ecologists, research methods. Use Gotelli's *Primer of Ecology*, Primack's *Essentials of Conservation Biology*, Sodhi & Ehrlich's *Conservation Biology for All* (free). Estimated 6–8 months.

**Tier 2 — Specialization Tracks (choose 2–3)**
- Systems ecology & complexity (Meadows, Scheffer, Holling/Gunderson, SFI courses)
- Restoration ecology (Holl, Palmer et al., SER standards)
- Rewilding (Pettorelli et al., Monbiot, Tree, case studies)
- Computational ecology (SDM, Bayesian methods, ecological networks, remote sensing)
- Conservation genetics & genomics

**Tier 3 — Capstone Project**
One major integrative project from the ten options above, producing publication-quality output hosted on GitHub with full reproducibility.

**Per-course metadata should include**: Title, resource type (textbook/MOOC/paper), URL, estimated hours, prerequisites, assessment method (quiz/project/reading reflection), and relevance to which program requirements it maps to (referencing UC Davis, Yale, Duke, ETH, Imperial as benchmarks).

The coding agent should verify that the curriculum covers at least the same breadth as ETH Zurich's Ecology & Evolution major, achieves the competency expectations of UC Davis ECL 200A/B, and provides the practical/applied focus of Imperial's Conservation Science MSc—while maximally leveraging the student's pre-existing computational strengths through the computational ecology track and computationally-oriented capstone projects.