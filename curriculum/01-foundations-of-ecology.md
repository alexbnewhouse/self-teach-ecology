# Module 1: Foundations of Ecology

**Estimated time**: 80–100 hours  
**Prerequisites**: Module 0  
**Parallelizable with**: None (this is foundational)  
**Type**: Tier 1 core module  
**Assessment**: Reading synthesis + coding notebooks + module essay  
**Benchmark mapping**: UC Davis ECL 200A/B | Yale ENV core | Duke ENV 502 | ETH Ecology Foundations | Imperial core ecology

---

## Preamble: Leveraging Your Complex-Systems and Data-Science Background

You are entering ecology with two substantial advantages: (1) a PhD-level understanding of complex adaptive systems, network dynamics, regime shifts, and causal inference from political science; and (2) an MS-level command of statistics, machine learning, and programming from data science. This module is where you build the **domain knowledge** those skills need to become ecologically productive.

Many ecological concepts will feel structurally familiar:

- **Population dynamics** are governed by the same differential equations you've seen in conflict modeling. Exponential growth, logistic constraints, oscillatory predator-prey dynamics — these are ODEs you already know how to solve.
- **Network ecology** (food webs, mutualistic networks) uses centrality, modularity, and robustness analysis that directly parallels your social-network-analysis training. Keystone species ≈ high-betweenness nodes. Trophic cascades ≈ cascade failures.
- **Regime shifts** in ecosystems (lake eutrophication, coral collapse, savanna–forest transitions) are formally identical to the critical transitions in political systems you study. Scheffer's *Critical Transitions in Nature and Society* explicitly bridges both fields.
- **Spatial patterns** in species distributions connect to the georeferenced event data (ACLED, UCDP-GED) you've worked with. Species occurrence records (GBIF) are structured like conflict event data — georeferenced, zero-inflated, imperfectly detected.

**Where your intuition will mislead you**: Ecological systems have physical constraints (thermodynamics, dispersal limitation, evolutionary history) that social systems lack. Organisms cannot "choose" strategies the way political actors can. Evolutionary timescales add a dimension absent from most PSCI models. Pay close attention to where analogies break down — that is where the real ecological learning happens.

> → See the [PSCI–Ecology Concept Bridge](../resources/psci-ecology-bridge.md) for a full map of where your existing knowledge transfers and where it diverges.

---

## Study Guide: How to Approach This Module

### Pacing (suggested 10-week schedule)

| Week | Focus | Hours | Key Deliverable |
|------|-------|-------|-----------------|
| 1 | Unit 1.1: History & Scope | 6–8 | Reflection essay |
| 2–3 | Unit 1.2: Population Ecology | 14–18 | Exercise 1.1 notebook |
| 4–5 | Unit 1.3: Species Interactions | 14–18 | Exercise 1.2 notebook |
| 6–7 | Unit 1.4: Community Ecology | 14–18 | Exercise 1.3 notebook |
| 8 | Unit 1.5: Ecosystem Ecology | 10–12 | Exercise 1.4 notebook |
| 9 | Unit 1.6: Biogeography | 10–12 | Exercise 1.5 notebook |
| 10 | Review + Synthesis | 8–10 | Comprehension check + synthesis essay |

### How to read ecological literature as a non-biologist

1. **Primary texts** (Begon, Chapin, Lomolino): Read assigned chapters fully. These are textbook-level — not optional background.
2. **Seminal papers**: Read the full paper. Take notes on the core model or argument, the evidence used, and the influence (why is this cited thousands of times?).
3. **Supplementary readings**: Skim for the main argument. Return to them in depth when relevant to your exercises or synthesis essay.
4. **Don't skip the organism-level detail**: Your instinct may be to jump to the mathematical models and skip the biology. Resist this. Understanding *why* populations crash, *how* species interact, and *what* drives succession requires biological intuition that no amount of modeling can replace.

### Video lectures (recommended companions)

These are not required but significantly aid comprehension for self-directed learners:

- **Yale EEB 122**: Stephen Stearns, *Principles of Evolution, Ecology, and Behavior* (Open Yale Courses, 36 lectures). Particularly lectures 17–36 covering population ecology, life histories, species interactions, community ecology, and biogeography. Free: https://oyc.yale.edu/ecology-and-evolutionary-biology/eeb-122
- **Crash Course Ecology** (Hank Green, 12 episodes, ~10 min each). Excellent quick introductions before diving into textbook chapters. Free on YouTube.
- **MIT OCW 7.014**: *Introductory Biology* — Lectures on ecology and evolution provide a solid biological foundation. Free: https://ocw.mit.edu/
- **Khan Academy: Ecology** — Short modules on population ecology, community ecology, biodiversity. Good for quick concept review.
- **Santa Fe Institute Complexity Explorer**: *Introduction to Complexity* (Melanie Mitchell). You may already know this, but it provides excellent context for how ecological systems function as complex adaptive systems.

---

## Learning Objectives

By the end of this module, you should be able to:

1. Explain the core principles of population, community, and ecosystem ecology
2. Describe and apply key ecological models (exponential/logistic growth, Lotka-Volterra, metapopulation dynamics)
3. Understand energy flow, nutrient cycling, and trophic dynamics in ecosystems
4. Explain the mechanisms and consequences of biodiversity at multiple scales
5. Read and critically evaluate primary ecological literature
6. Connect ecological theory to conservation applications
7. Identify structural parallels between ecological and political-social systems, and articulate where analogies hold and break down

---

## Unit 1.1: The Science of Ecology — History and Scope

### Readings

**Primary text**:
> Begon, M., Townsend, C.R., & Harper, J.L. (2006). *Ecology: From Individuals to Ecosystems* (4th ed.). Blackwell Publishing.
> - Chapter 1: Organisms in their environments — the evolutionary backdrop
> - Read carefully: this chapter frames the entire discipline

**Supplementary**:
> Kingsland, S.E. (2005). *The Evolution of American Ecology, 1890–2000*. Johns Hopkins University Press.
> - Chapters 1–3 (for historical context on ecology as a discipline)
> - Pay attention to how ecology professionalized and how political/institutional forces shaped its research agenda — you'll recognize parallels to PSCI disciplinary history

> McIntosh, R.P. (1985). *The Background of Ecology: Concept and Theory*. Cambridge University Press.
> - Skim chapters 1–4 for the intellectual history of ecological ideas; return to specific chapters as needed

**Recommended introductory text** (for non-biologists):
> Juniper, T. (2021). *The Ecology Book*. DK Publishing.
> - Quick visual reference; used by Imperial College as pre-reading for non-biology entrants

> MacKenzie, A., Ball, A.S., & Virdee, S.R. (2001). *BIOS Instant Notes in Ecology* (2nd ed.). Taylor & Francis.
> - Rapid-review format; useful as a reference throughout this module

### Key Concepts
- Ecology as a science: definition, scope, levels of organization (organism → population → community → ecosystem → biosphere)
- The Darwinian foundation of ecological thinking
- Proximate vs. ultimate explanations in ecology
- Abiotic vs. biotic factors
- The history of ecology: from natural history through "big ecology" to computational ecology
- The relationship between ecology and conservation biology

> **🔗 PSCI Connection**: Ecology's development as a discipline mirrors patterns you know from political science — paradigm debates (Clementsian vs. Gleasonian succession ≈ structuralism vs. rational choice), evolving relationships with adjacent disciplines, and political-institutional forces shaping research agendas. Kingsland's history reveals how funding, policy needs, and institutional politics shaped ecology's trajectory — territory familiar to anyone who has read Seidelman on APSA or Adcock on PSCI methods wars.

### Discussion Questions
1. How does ecology's level-of-organization framework (organism → biosphere) compare to levels of analysis in political science (individual → system)?
2. Why did ecology emerge relatively late as a formal science compared to physics or chemistry? What institutional and intellectual conditions were needed?
3. How might the "balance of nature" metaphor (now largely rejected in ecology) compare to "equilibrium" metaphors in political science?

### Exercise 1.0: History and scope reflection
Write a **1,000-word reflective essay** addressing:

> *"Based on the history readings and Chapter 1 of Begon, what is ecology's core intellectual project? How does its scope compare to political science — what are the analogous 'levels of analysis,' and where does ecology face methodological challenges similar to those in PSCI? Identify at least two structural parallels and two fundamental differences."*

**Deliverable**: Essay (1,000 words) saved to your portfolio.

---

## Unit 1.2: Population Ecology

### Readings

**Primary text** (Begon et al., 2006):
> - Chapter 4: Life, death, and life histories
> - Chapter 5: Intraspecific competition
> - Chapter 6: Dispersal, dormancy, and metapopulations

**Seminal papers**:
> MacArthur, R.H., & Wilson, E.O. (1963). An equilibrium theory of insular zoogeography. *Evolution*, 17(4), 373–387.
> - The paper that launched island biogeography theory; read in full

> Hanski, I. (1998). Metapopulation dynamics. *Nature*, 396(6706), 41–49. https://doi.org/10.1038/23876
> - Concise review of metapopulation theory; connects to landscape fragmentation

> Stearns, S.C. (1992). *The Evolution of Life Histories*. Oxford University Press.
> - Chapters 1–4: life history theory (r vs. K selection, trade-offs, reproductive effort)

**Supplementary**:
> Turchin, P. (2003). *Complex Population Dynamics: A Theoretical/Empirical Synthesis*. Princeton University Press.
> - Chapters 1–5 especially relevant; connects mathematical models to real data
> - Highly recommended given your quantitative background — Turchin is also known for applying population dynamics to historical/social systems (*War and Peace and War*, *Historical Dynamics*)

> Gotelli, N.J. (2008). *A Primer of Ecology* (4th ed.). Sinauer Associates.
> - Chapters 1–4: clean mathematical treatment of exponential growth, logistic growth, metapopulations

> **Video**: Yale EEB 122 Lectures 17–22 (Stearns on population ecology and life history theory)

### Key Concepts
- Exponential and logistic growth models
- Life history theory (r-selection vs. K-selection, and its modern critiques)
- Density dependence and density independence
- Demographic stochasticity vs. environmental stochasticity
- Metapopulation theory (Levins model, source-sink dynamics)
- Island biogeography theory
- Minimum viable population (MVP)
- Allee effects

> **🔗 PSCI/DS Connection**: Population growth models are ODEs you've seen before. The logistic equation is identical in form to models of technology adoption or information diffusion. Metapopulation dynamics — fragmented subpopulations connected by dispersal — map directly onto your understanding of fragmented armed-group networks connected by recruitment and resource flows. Source-sink dynamics (some patches sustain populations, others drain them) have a clear parallel in rebel governance theory (some territories generate resources, others consume them). The math is the same; the entities and constraints differ.

### Discussion Questions
1. Under what conditions does the logistic growth model fail to describe real population dynamics? What biological mechanisms create departures from the smooth logistic curve?
2. How do Allee effects (positive density dependence at low population sizes) change conservation strategies compared to simple density-dependent models?
3. If habitat patches are "islands" in a fragmented landscape, what does island biogeography theory predict about species loss from habitat fragmentation? How well has this prediction held empirically?

### Exercise 1.1: Population Modeling
Using Python or R, implement the following models and visualize their dynamics:
1. **Exponential growth**: $N_{t+1} = N_t \cdot e^{r}$
2. **Logistic growth**: $\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$
3. **Logistic growth with Allee effect**: $\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)\left(\frac{N}{A} - 1\right)$ where $A$ is the Allee threshold
4. **Levins metapopulation model**: $\frac{dp}{dt} = cp(1-p) - ep$

For each model:
- Visualize dynamics over time for different parameter values
- Explore: How do parameter changes affect equilibrium?
- Add demographic and environmental stochasticity — how does this change outcomes, especially for small populations?
- For the metapopulation model: What is the extinction threshold? When does the metapopulation persist vs. collapse?

**Deliverable**: A Jupyter notebook or R Markdown document with annotated code, figures, and a 500-word discussion of ecological implications. Explicitly connect at least one model behavior to a parallel dynamic in PSCI/complex systems.

---

## Unit 1.3: Species Interactions

### Readings

**Primary text** (Begon et al., 2006):
> - Chapter 8: Interspecific competition
> - Chapter 9: The nature of predation
> - Chapter 10: The population dynamics of predation
> - Chapter 11: Decomposers and detritivores (skim)
> - Chapter 12: Parasitism and disease
> - Chapter 13: Symbiosis and mutualism

**Seminal papers**:
> Paine, R.T. (1966). Food web complexity and species diversity. *The American Naturalist*, 100(910), 65–75.
> - Read in full: introduces the keystone species concept via Pisaster ochraceus (sea star) removal experiments. One of ecology's most cited papers.

> Hairston, N.G., Smith, F.E., & Slobodkin, L.B. (1960). Community structure, population control, and competition. *The American Naturalist*, 94(879), 421–425.
> - "HSS" — the paper that asked "Why is the world green?" and launched decades of debate on top-down vs. bottom-up control

> Tilman, D. (1982). *Resource Competition and Community Structure*. Princeton University Press.
> - Chapters 1–5: mechanistic theory of competition for shared resources

**Supplementary**:
> Chesson, P. (2000). Mechanisms of maintenance of species diversity. *Annual Review of Ecology and Systematics*, 31(1), 343–366.
> - Modern coexistence theory — how competing species can stably coexist

> Bascompte, J., & Jordano, P. (2007). Plant-animal mutualistic networks: The architecture of biodiversity. *Annual Review of Ecology, Evolution, and Systematics*, 38, 567–593.
> - Connects mutualism to network science — directly relevant to your network analysis skills

> **Video**: Yale EEB 122 Lectures 23–28 (Stearns on species interactions, coevolution)

### Key Concepts
- Competition: exploitation vs. interference; the competitive exclusion principle (Gause)
- Lotka-Volterra competition and predator-prey models
- Functional and numerical responses (Type I, II, III)
- Keystone species and trophic cascades
- Mutualism, commensalism, parasitism
- Apparent competition
- Coexistence theory (modern approaches: Chesson framework)
- Coevolutionary dynamics ("Red Queen" hypothesis)

> **🔗 PSCI/DS Connection**: Predator-prey oscillations are structurally identical to certain arms-race models. The keystone species concept (remove one species → community collapses) maps onto your understanding of critical nodes in political networks — the removal of a key broker or institution destabilizes the system. Coexistence theory asks "why don't competitors eliminate each other?" — the ecological version of "why does political pluralism persist?" The mathematical frameworks for coexistence (niche differentiation, frequency dependence) have direct parallels in evolutionary game theory, which you may have encountered through conflict modeling. Bascompte's mutualistic network analysis uses the same tools (nestedness, modularity) you'd apply to alliance networks.

### Discussion Questions
1. Paine's keystone species concept emerged from an intertidal removal experiment. How could you design an equivalent "removal experiment" in a social/political network? What are the ethical and practical constraints?
2. The "world is green" debate (HSS) asks whether top-down or bottom-up forces control ecosystems. Is there an analogous debate in political science about what controls political order?
3. What assumptions of Lotka-Volterra models are most unrealistic for real ecosystems? How do modern coexistence frameworks address these limitations?

### Exercise 1.2: Lotka-Volterra Dynamics
Implement the Lotka-Volterra predator-prey model:

$$\frac{dN}{dt} = rN - aNP$$
$$\frac{dP}{dt} = baNP - mP$$

1. Visualize population cycles for prey (N) and predator (P) over time
2. Create a phase portrait (N vs. P in state space)
3. Modify the model to include a Type II functional response: $\frac{aN}{1+ahN}$
4. Add environmental stochasticity and compare outputs to the deterministic model
5. Discuss: What are the assumptions of this model, and where do they break down in real ecosystems? How do the dynamics compare to oscillatory dynamics in conflict or political systems?

**Deliverable**: Annotated notebook with code, figures, and a 500-word discussion.

---

## Unit 1.4: Community Ecology

### Readings

**Primary text** (Begon et al., 2006):
> - Chapter 16: The nature of the community
> - Chapter 17: The flux of energy through ecosystems
> - Chapter 18: The flux of matter through ecosystems
> - Chapter 19: Patterns in species richness
> - Chapter 20: Biodiversity

**Seminal papers**:
> Hutchinson, G.E. (1957). Concluding remarks. *Cold Spring Harbor Symposia on Quantitative Biology*, 22, 415–427.
> - Read in full: introduces the niche concept — one of ecology's most important ideas

> Hubbell, S.P. (2001). *The Unified Neutral Theory of Biodiversity and Biogeography*. Princeton University Press.
> - Chapters 1–5; a controversial but foundational contribution. Neutral theory argues that species are functionally equivalent and diversity patterns arise from stochastic processes — a deliberate provocation to niche theory.

> Tilman, D. (1999). The ecological consequences of changes in biodiversity: A search for general principles. *Ecology*, 80(5), 1455–1474.
> - Foundational paper on the biodiversity-ecosystem function relationship

**Supplementary**:
> Vellend, M. (2016). *The Theory of Ecological Communities*. Princeton University Press.
> - An elegant modern synthesis: reduces community ecology to four processes (selection, drift, speciation, dispersal) — deliberately paralleling population genetics. Highly recommended.

> Magurran, A.E. (2004). *Measuring Biological Diversity*. Blackwell Publishing.
> - The reference guide for biodiversity metrics; read Chapters 1–4 for conceptual foundations

> Holyoak, M., Leibold, M.A., & Holt, R.D. (Eds.). (2005). *Metacommunities: Spatial Dynamics and Ecological Communities*. University of Chicago Press.
> - Chapters 1–3: metacommunity theory extends metapopulation thinking to entire communities

> **Video**: Yale EEB 122 Lectures 29–32 (Stearns on community ecology, food webs, biodiversity)

### Key Concepts
- The niche concept (Hutchinsonian niche, fundamental vs. realized)
- Species diversity indices (Shannon, Simpson, species richness)
- Alpha, beta, and gamma diversity
- Rank-abundance distributions (geometric, log-series, lognormal, broken-stick)
- Succession theory (primary, secondary; Clementsian vs. Gleasonian views; intermediate disturbance hypothesis)
- Neutral theory of biodiversity
- Metacommunity theory (species sorting, mass effects, patch dynamics, neutral)
- Energy flow and food webs
- The biodiversity-ecosystem function (BEF) relationship

> **🔗 PSCI/DS Connection**: Vellend's four-process framework (selection, drift, speciation, dispersal) is a deliberate analogy to evolutionary biology, but it also maps loosely onto political science: selection ≈ competition/power, drift ≈ stochastic events/contingency, dispersal ≈ diffusion of ideas/practices, speciation ≈ emergence of new actors/institutions. Neutral theory — the claim that species are interchangeable and patterns arise from randomness — has a parallel in arguments about whether political outcomes are driven by structural forces or historical contingency. The niche vs. neutral debate is ecology's version of structure vs. agency. Community diversity metrics (Shannon, Simpson) are information-theoretic measures you already know from data science.

### Discussion Questions
1. Vellend reduces community ecology to four processes. Does this simplification gain or lose important explanatory power? What would a four-process framework for political communities look like?
2. How does neutral theory challenge traditional ecological thinking? Under what conditions might neutral processes dominate? When would niche processes clearly dominate?
3. What does the biodiversity-ecosystem function relationship (Tilman 1999) imply for conservation? If species loss reduces ecosystem function, is this a stronger argument for conservation than ethical arguments alone?
4. Compare Clementsian (communities as "superorganisms") and Gleasonian (communities as loose assemblages of individual species) views. Which has more empirical support, and why does this matter for conservation?

### Exercise 1.3: Biodiversity Analysis
Using a publicly available ecological dataset (suggestions below), calculate and compare diversity metrics:

1. **Alpha diversity**: Calculate Shannon diversity (H'), Simpson's diversity (1-D), and species richness for multiple sites
2. **Beta diversity**: Calculate Jaccard and Bray-Curtis dissimilarity between sites
3. **Visualization**: Create a rank-abundance diagram (Whittaker plot) for each site
4. **Rarefaction**: Build species accumulation curves and rarefaction curves to assess sampling completeness
5. **Statistical comparison**: Test whether diversity differs significantly between habitat types or treatments
6. **Interpretation**: Discuss what different metrics reveal about community structure. Which index is most informative for conservation planning, and why?

**Suggested datasets**:
- [GBIF: Global Biodiversity Information Facility](https://www.gbif.org/) — Species occurrence data
- [BioTIME database](https://biotime.st-andrews.ac.uk/) — Biodiversity time series
- [NEON: National Ecological Observatory Network](https://data.neonscience.org/) — Standardized ecological data across US sites
- R package `vegan` includes example datasets ideal for this exercise (BCI, dune, mite)

**R packages**: `vegan`, `iNEXT`, `BiodiversityR`  
**Python packages**: `scikit-bio`, `scipy.spatial.distance`

**Deliverable**: Annotated notebook with analysis, figures, and a 500-word interpretation of ecological patterns.

---

## Unit 1.5: Ecosystem Ecology

### Readings

**Primary text**:
> Chapin, F.S. III, Matson, P.A., & Vitousek, P.M. (2011). *Principles of Terrestrial Ecosystem Ecology* (2nd ed.). Springer.
> - Chapters 1–3: The ecosystem concept, Earth's climate system, geology and soils
> - Chapters 5–7: Carbon cycling, plant nutrient use, decomposition
> - Chapters 9–10: Nutrient cycling, trophic dynamics
> - Read these thoroughly — ecosystem ecology provides the physical/chemical foundation that your PSCI training lacks

**Seminal papers**:
> Likens, G.E., Bormann, F.H., Johnson, N.M., Fisher, D.W., & Pierce, R.S. (1970). Effects of forest cutting and herbicide treatment on nutrient budgets in the Hubbard Brook watershed-ecosystem. *Ecological Monographs*, 40(1), 23–47.
> - One of ecology's most important long-term experiments: how deforestation disrupts nutrient cycles. Read in full.

> Vitousek, P.M., Aber, J.D., Howarth, R.W., Likens, G.E., Matson, P.A., Schindler, D.W., Schlesinger, W.H., & Tilman, D. (1997). Human alteration of the global nitrogen cycle: Sources and consequences. *Ecological Applications*, 7(3), 737–750.
> - How human activity has doubled global nitrogen fixation, with cascading effects on ecosystems

> Scheffer, M., Carpenter, S., Foley, J.A., Folke, C., & Walker, B. (2001). Catastrophic shifts in ecosystems. *Nature*, 413, 591–596.
> - Regime shifts across ecosystem types — a paper you'll find structurally very familiar from your complex-systems background

**Supplementary**:
> Schlesinger, W.H., & Bernhardt, E.S. (2020). *Biogeochemistry: An Analysis of Global Change* (4th ed.). Academic Press.
> - Chapters 5–8 for global biogeochemical cycles; reference-level depth

> **Video**: Crash Course Ecology #7–10 (ecosystem ecology, nutrient cycling, biogeochemistry)

### Key Concepts
- Primary production (GPP, NPP) and its controls (light, water, nutrients, temperature)
- Decomposition and nutrient mineralization
- Carbon, nitrogen, and phosphorus cycles — global-scale
- Ecosystem services: concept, classification, and debate
- Ecosystem engineers (organisms that physically modify, maintain, or create habitats)
- Resilience, resistance, and regime shifts
- Trophic levels and energy transfer efficiency (~10% rule)
- Biogeochemical cycles and human perturbation

> **🔗 PSCI/DS Connection**: Regime shifts in ecosystems (Scheffer et al., 2001) are the concept you already understand best. Lake eutrophication, coral reef collapse, and savanna–forest transitions are formally identical to political regime transitions: the system crosses a threshold and reorganizes around a new attractor. Hysteresis means recovery requires more effort than the original disturbance — this is why rewilding is hard and expensive. Your complex-systems intuition about tipping points, early warning signals, and path dependence applies directly. The MODIS satellite data in Exercise 1.4 connects to your experience with georeferenced data — you'll use the same spatial-data skills applied to a physical rather than social phenomenon.

### Discussion Questions
1. Why is the Hubbard Brook experiment considered a landmark study? What does it reveal about the coupling between biotic and abiotic processes?
2. How do regime shifts in ecosystems compare to political regime transitions? Where does the analogy hold tightly, and where does it break down?
3. Ecosystem services valuation puts a price on nature. Is this helpful or dangerous for conservation? What would a political economist say about commodifying nature?
4. If human nitrogen fixation has doubled the natural rate, what cascading effects would you predict across terrestrial and aquatic ecosystems?

### Exercise 1.4: Ecosystem Data Exploration
Using NASA MODIS satellite data (freely available):

1. **Download and visualize** Net Primary Productivity (NPP) data for a region of interest using Python (`xarray`, `rasterio`, `matplotlib`) or R (`terra`, `raster`)
2. **Examine seasonal and interannual variation** in NPP — plot time series and identify patterns
3. **Compare NPP across biomes or land-use types** — visualize differences between forest, grassland, cropland, and urban areas
4. **Correlate NPP with climate variables** — download temperature and precipitation data (WorldClim or CRU) and explore relationships
5. **Disturbance detection** (optional): Can you identify fire scars, deforestation, or other disturbances in the NPP time series?
6. **Discuss**: What controls spatial variation in primary productivity? How does this connect to global patterns of biodiversity?

**Data sources**:
- [NASA Earthdata](https://earthdata.nasa.gov/) — MODIS NPP product (MOD17A3HGF)
- [Google Earth Engine](https://earthengine.google.com/) — Simplifies access to MODIS and other satellite datasets
- [AppEEARS](https://appeears.earthdatacloud.nasa.gov/) — Point-and-click extraction of MODIS data

**Deliverable**: Notebook with spatial data analysis, figures, and ecological interpretation.

---

## Unit 1.6: Biogeography

### Readings

**Primary text**:
> Lomolino, M.V., Riddle, B.R., & Whittaker, R.J. (2017). *Biogeography: Biological Diversity across Space and Time* (5th ed.). Sinauer Associates.
> - Chapters 1–4: The science of biogeography, geographic setting, dispersal
> - Chapters 10–13: Island biogeography, species-area relationships, community assembly on islands

**Seminal work**:
> MacArthur, R.H., & Wilson, E.O. (1967). *The Theory of Island Biogeography*. Princeton University Press.
> - Read in full — one of ecology's most influential works. The core model (equilibrium between immigration and extinction rates) is beautifully simple and directly relevant to conservation (habitat fragments as "islands"). This book also pioneered the use of mathematical modeling in ecology.

**Supplementary**:
> Whittaker, R.J., & Fernández-Palacios, J.M. (2007). *Island Biogeography: Ecology, Evolution, and Conservation* (2nd ed.). Oxford University Press.
> - Chapters 1–4 and 10 for modern updates and conservation applications of island biogeography

> Ricketts, T.H. (2001). The Matrix Matters: Effective Isolation in Fragmented Landscapes. *The American Naturalist*, 158(1), 87–99.
> - Challenges the simple "island in a sea of inhospitable matrix" assumption — the landscape between fragments matters

> Haddad, N.M., et al. (2015). Habitat fragmentation and its lasting impact on Earth's ecosystems. *Science Advances*, 1(2), e1500052.
> - Comprehensive review of fragmentation effects globally

> **Video**: Yale EEB 122 Lectures 33–34 (Stearns on biogeography, species-area relationships)

### Key Concepts
- Historical vs. ecological biogeography
- Dispersal, vicariance, and speciation
- Species-area relationships: $S = cA^z$
- Island biogeography theory: equilibrium between immigration and extinction
- Conservation applications: habitat fragments as islands
- The matrix between fragments and its ecological importance
- Latitudinal diversity gradient (why are tropics more diverse?)
- Biome classification and its climatic determinants

> **🔗 PSCI/DS Connection**: Island biogeography theory is a spatial equilibrium model — structurally similar to models of state formation on geographic islands or the diffusion of institutional forms across isolated polities. The species-area relationship ($S = cA^z$) is a power law, and you know how power laws work from network science. The application of island biogeography to habitat fragmentation is directly relevant to your later work on landscape ecology (Module 4) and has direct policy implications: how large must a protected area be to sustain its species? This is a question with identical mathematical structure to "how large must a territory be to sustain a state?"

### Discussion Questions
1. Why has island biogeography theory been so influential in conservation biology? What are its limitations when applied to habitat fragments on continents?
2. The species-area relationship is a power law. What mechanisms generate this pattern? How does the value of the exponent $z$ change between true islands and habitat fragments?
3. Ricketts (2001) argues that "the matrix matters." How does the habitat between fragments affect conservation planning?
4. What are the implications of biogeography for rewilding? How does understanding dispersal, speciation, and extinction inform restoration strategies?

### Exercise 1.5: Island Biogeography and Fragmentation Analysis
Using the species-area relationship and publicly available data:

1. **Model fitting**: Using data from island or fragment surveys (suggestions below), fit the species-area relationship $\log(S) = \log(c) + z \cdot \log(A)$ and estimate $c$ and $z$
2. **Prediction**: Use your fitted model to predict species richness for fragments of different sizes. What size fragment would you need to protect to conserve 90% of the regional species pool?
3. **Island vs. fragment comparison**: If available, compare $z$ values between true islands and habitat fragments in the same region. What does the difference tell you about the isolation effect?
4. **Visualization**: Create a species-area curve with confidence intervals. Map the study area if spatial data are available.
5. **Conservation application**: Given a conservation budget that allows protecting either one large or several small fragments of equal total area (the SLOSS debate), what does your analysis recommend?

**Suggested data sources**:
- [GBIF](https://www.gbif.org/) — Species records for islands or defined areas
- [PREDICTS database](https://www.nhm.ac.uk/our-science/data/predicts.html) — Global dataset of biodiversity in response to land use
- MacArthur & Wilson's original island data (reproduced in Lomolino et al., Table 13.1)
- Classic datasets available in R package `vegan`

**Deliverable**: Annotated notebook with analysis, species-area curves, and a 500-word discussion of conservation implications.

---

## Comprehension Check

After completing Module 1, you should be able to answer:

1. Why is the logistic growth model both useful and insufficient for real populations?
2. What is the competitive exclusion principle, and when does coexistence occur despite competition?
3. Explain the concept of a trophic cascade with a real-world example (Paine's intertidal system or Yellowstone wolves are classic choices).
4. How does island biogeography theory apply to habitat fragmentation?
5. What is the difference between ecosystem resistance and resilience? How do regime shifts relate to these concepts?
6. Compare and contrast the Clementsian and Gleasonian views of ecological succession. Which has more modern support, and why?
7. How do neutral theory and niche theory offer different explanations for biodiversity patterns? Can they be reconciled?
8. What is the biodiversity-ecosystem function (BEF) relationship, and why does it matter for conservation arguments?
9. How do human alterations to global biogeochemical cycles (nitrogen, carbon, phosphorus) cascade through ecosystems?
10. Identify three structural parallels between ecological systems and political systems, and explain where each analogy breaks down.

---

## Synthesis Prompt

**Write a 1,500–2,000 word essay** addressing:

> *"Ecology studies the distribution and abundance of organisms and the interactions that determine them (Krebs, 2001). Political science studies the distribution of power and resources and the interactions that determine them. Drawing on the foundational concepts covered in this module — population dynamics, species interactions, community assembly, ecosystem function, and biogeography — identify three cases where ecological theory and political-social theory share deep structural parallels. For each, explain the parallel, assess how far the analogy extends, and identify where it breaks down. Conclude by reflecting on what ecology's conceptual toolkit adds to your existing understanding of complex systems."*

Use specific citations from the module readings. This essay is your first opportunity to articulate how your PSCI/DS background intersects with ecology — a skill that will define your career trajectory.

---

## Self-Evaluation Rubric

| Criterion | Developing | Proficient | Advanced |
|-----------|-----------|-----------|---------|
| **Ecological theory** | Can name major concepts (niche, trophic cascade, succession) | Can explain mechanisms and apply to specific systems | Can critically evaluate competing theories (niche vs. neutral, Clementsian vs. Gleasonian) and identify conditions where each applies |
| **Mathematical modeling** | Understands equations conceptually | Can implement and analyze models computationally | Can modify models, add realism (stochasticity, spatial structure), and critically evaluate assumptions |
| **Literature engagement** | Has read assigned texts | Can summarize key arguments and evidence | Can critically evaluate papers, identify limitations, and connect across readings |
| **Interdisciplinary bridges** | Recognizes vague parallels between ecology and PSCI | Can articulate specific structural parallels with evidence | Can identify where parallels hold, where they break down, and why — and use this to generate novel questions |
| **Data analysis** | Can run provided code | Can adapt code to new datasets and interpret results | Can choose appropriate methods, troubleshoot analysis problems, and derive ecological meaning from results |

---

## Supplementary Resources

### Online simulations and tools
- **NetLogo Models Library**: Population dynamics, predator-prey, competition, evolution — free interactive models for building intuition. https://ccl.northwestern.edu/netlogo/models/
- **EcoBeaker**: Virtual ecology lab exercises (some free). http://www.ecobeaker.com/
- **PopDynamics Shiny App**: Interactive R Shiny apps for population ecology models. Search "shiny app population ecology" on GitHub.
- **Island Biogeography Simulator**: Interactive tool for exploring MacArthur-Wilson dynamics. Available via the Biogeography textbook companion site.

### Key journals for this module
- *Ecology* (ESA)
- *Ecology Letters*
- *The American Naturalist*
- *Journal of Ecology* (BES)
- *Trends in Ecology & Evolution* (TREE) — review articles especially useful for catching up on debates

### Cross-references
- → [PSCI–Ecology Concept Bridge](../resources/psci-ecology-bridge.md) — Full mapping of your existing knowledge to ecological concepts
- → [Datasets & Tools](../resources/datasets-and-tools.md) — Python and R packages for ecological analysis
- → [Module 2: Conservation Biology](02-conservation-biology.md) — Applies the ecology you learn here to conservation problems
- → [Module 4: Landscape Ecology](04-landscape-ecology-spatial-analysis.md) — Extends biogeography into spatial analysis
- → [Module 5: Quantitative Ecology](05-quantitative-ecology.md) — Builds on the modeling exercises here with ecology-specific statistical methods
- → [Track: Systems Ecology & Complexity](tracks/systems-ecology-complexity.md) — For deeper engagement with complex-systems approaches

---

→ Next: [Module 2: Conservation Biology](02-conservation-biology.md)
