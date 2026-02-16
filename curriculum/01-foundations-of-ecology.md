# Module 1: Foundations of Ecology

**Estimated time**: 80–100 hours  
**Prerequisites**: Module 0  
**Parallelizable with**: None (this is foundational)

---

## Learning Objectives

By the end of this module, you should be able to:

1. Explain the core principles of population, community, and ecosystem ecology
2. Describe and apply key ecological models (exponential/logistic growth, Lotka-Volterra, metapopulation dynamics)
3. Understand energy flow, nutrient cycling, and trophic dynamics in ecosystems
4. Explain the mechanisms and consequences of biodiversity at multiple scales
5. Read and critically evaluate primary ecological literature
6. Connect ecological theory to conservation applications

---

## Unit 1.1: The Science of Ecology — History and Scope

### Readings

**Primary text**:
> Begon, M., Townsend, C.R., & Harper, J.L. (2006). *Ecology: From Individuals to Ecosystems* (4th ed.). Blackwell Publishing.
> - Chapter 1: Organisms in their environments — the evolutionary backdrop

**Supplementary**:
> Kingsland, S.E. (2005). *The Evolution of American Ecology, 1890–2000*. Johns Hopkins University Press.
> - Chapters 1–3 (for historical context on ecology as a discipline)

> McIntosh, R.P. (1985). *The Background of Ecology: Concept and Theory*. Cambridge University Press.
> - Useful reference for the intellectual history of ecological ideas

### Key Concepts
- Ecology as a science: definition, scope, levels of organization
- The Darwinian foundation of ecological thinking
- Proximate vs. ultimate explanations in ecology
- Abiotic vs. biotic factors

---

## Unit 1.2: Population Ecology

### Readings

**Primary text** (Begon et al., 2006):
> - Chapter 4: Life, death, and life histories
> - Chapter 5: Intraspecific competition
> - Chapter 6: Dispersal, dormancy, and metapopulations

**Seminal papers**:
> MacArthur, R.H., & Wilson, E.O. (1963). An equilibrium theory of insular zoogeography. *Evolution*, 17(4), 373–387.

> Hanski, I. (1998). Metapopulation dynamics. *Nature*, 396(6706), 41–49. https://doi.org/10.1038/23876

> Stearns, S.C. (1992). *The Evolution of Life Histories*. Oxford University Press. — Chapters 1–4

**Supplementary**:
> Turchin, P. (2003). *Complex Population Dynamics: A Theoretical/Empirical Synthesis*. Princeton University Press.
> - Excellent for those with a quantitative background; connects mathematical models to real data

### Key Concepts
- Exponential and logistic growth models
- Life history theory (r-selection vs. K-selection, and its modern critiques)
- Density dependence and density independence
- Metapopulation theory (Levins model, source-sink dynamics)
- Island biogeography theory
- Minimum viable population (MVP)

### Exercise 1.1: Population Modeling
Using Python or R, implement the following models and visualize their dynamics:
1. Exponential growth: $N_{t+1} = N_t \cdot e^{r}$
2. Logistic growth: $\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$
3. Levins metapopulation model: $\frac{dp}{dt} = cp(1-p) - ep$

Explore: How do parameter changes affect equilibrium? What happens when you add stochasticity?

**Deliverable**: A Jupyter notebook or R Markdown document with annotated code and figures.

---

## Unit 1.3: Species Interactions

### Readings

**Primary text** (Begon et al., 2006):
> - Chapter 8: Interspecific competition
> - Chapter 9: The nature of predation
> - Chapter 10: The population dynamics of predation
> - Chapter 11: Decomposers and detritivores
> - Chapter 12: Parasitism and disease
> - Chapter 13: Symbiosis and mutualism

**Seminal papers**:
> Paine, R.T. (1966). Food web complexity and species diversity. *The American Naturalist*, 100(910), 65–75.

> Hairston, N.G., Smith, F.E., & Slobodkin, L.B. (1960). Community structure, population control, and competition. *The American Naturalist*, 94(879), 421–425.

> Tilman, D. (1982). *Resource Competition and Community Structure*. Princeton University Press. — Chapters 1–5.

### Key Concepts
- Competition: exploitation vs. interference; the competitive exclusion principle (Gause)
- Lotka-Volterra competition and predator-prey models
- Keystone species and trophic cascades
- Mutualism, commensalism, parasitism
- Apparent competition
- Coexistence theory (modern approaches)

### Exercise 1.2: Lotka-Volterra Dynamics
Implement the Lotka-Volterra predator-prey model:

$$\frac{dN}{dt} = rN - aNP$$
$$\frac{dP}{dt} = baNP - mP$$

1. Visualize population cycles for prey (N) and predator (P)
2. Create a phase portrait
3. Add environmental stochasticity and compare outputs
4. Discuss: What are the assumptions of this model, and where do they break down in real ecosystems?

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
> - Introduces the niche concept — one of ecology's most important ideas

> Hubbell, S.P. (2001). *The Unified Neutral Theory of Biodiversity and Biogeography*. Princeton University Press.
> - Chapters 1–5; a controversial but foundational contribution

> Tilman, D. (1999). The ecological consequences of changes in biodiversity: A search for general principles. *Ecology*, 80(5), 1455–1474.

**Supplementary**:
> Vellend, M. (2016). *The Theory of Ecological Communities*. Princeton University Press.
> - An elegant modern synthesis of community ecology

### Key Concepts
- The niche concept (Hutchinsonian niche, fundamental vs. realized)
- Species diversity indices (Shannon, Simpson, species richness)
- Alpha, beta, and gamma diversity
- Succession theory (primary, secondary; Clementsian vs. Gleasonian views)
- Neutral theory of biodiversity
- Energy flow and food webs
- Nutrient cycling in ecosystems

### Exercise 1.3: Biodiversity Analysis
Using a publicly available ecological dataset (suggestions below), calculate and compare diversity metrics:
1. Calculate Shannon diversity (H'), Simpson's diversity (1-D), and species richness for multiple sites
2. Calculate beta diversity between sites (Jaccard and Bray-Curtis)
3. Create a rank-abundance diagram (Whittaker plot)
4. Discuss: What do different metrics reveal about community structure?

**Suggested datasets**:
- [GBIF: Global Biodiversity Information Facility](https://www.gbif.org/) — Species occurrence data
- [BioTIME database](https://biotime.st-andrews.ac.uk/) — Biodiversity time series
- [NEON: National Ecological Observatory Network](https://data.neonscience.org/) — Standardized ecological data

**Deliverable**: Annotated notebook with analysis and a 500-word interpretation.

---

## Unit 1.5: Ecosystem Ecology

### Readings

**Primary text**:
> Chapin, F.S. III, Matson, P.A., & Vitousek, P.M. (2011). *Principles of Terrestrial Ecosystem Ecology* (2nd ed.). Springer.
> - Chapters 1–3, 5–7, 9–10

**Seminal papers**:
> Likens, G.E., Bormann, F.H., Johnson, N.M., Fisher, D.W., & Pierce, R.S. (1970). Effects of forest cutting and herbicide treatment on nutrient budgets in the Hubbard Brook watershed-ecosystem. *Ecological Monographs*, 40(1), 23–47.

> Vitousek, P.M., Aber, J.D., Howarth, R.W., Likens, G.E., Matson, P.A., Schindler, D.W., Schlesinger, W.H., & Tilman, D. (1997). Human alteration of the global nitrogen cycle: Sources and consequences. *Ecological Applications*, 7(3), 737–750.

### Key Concepts
- Primary production (GPP, NPP) and its controls
- Decomposition and nutrient mineralization
- Carbon, nitrogen, and phosphorus cycles
- Ecosystem services: concept and debate
- Ecosystem engineers
- Resilience, resistance, and regime shifts

### Exercise 1.4: Ecosystem Data Exploration
Using NASA MODIS satellite data (freely available):
1. Download and visualize Net Primary Productivity (NPP) data for a region of interest
2. Examine seasonal and interannual variation in NPP
3. Compare NPP across different biomes or land-use types
4. Discuss: What controls spatial variation in primary productivity?

**Data source**: [NASA Earthdata](https://earthdata.nasa.gov/) — MODIS NPP product (MOD17)

**Deliverable**: Notebook with spatial data analysis and interpretation.

---

## Unit 1.6: Biogeography

### Readings

**Primary text**:
> Lomolino, M.V., Riddle, B.R., & Whittaker, R.J. (2017). *Biogeography: Biological Diversity across Space and Time* (5th ed.). Sinauer Associates.
> - Chapters 1–4, 10–13

**Seminal work**:
> MacArthur, R.H., & Wilson, E.O. (1967). *The Theory of Island Biogeography*. Princeton University Press.
> - Read in full — this is one of ecology's most influential works and directly relevant to conservation (habitat fragments as "islands")

### Key Concepts
- Historical vs. ecological biogeography
- Dispersal, vicariance, and speciation
- Species-area relationships
- Island biogeography theory and its conservation applications
- Latitudinal diversity gradient
- Biome classification

---

## Comprehension Check

After completing Module 1, you should be able to answer:

1. Why is the logistic growth model both useful and insufficient for real populations?
2. What is the competitive exclusion principle, and when does coexistence occur despite competition?
3. Explain the concept of a trophic cascade with a real-world example.
4. How does island biogeography theory apply to habitat fragmentation?
5. What is the difference between ecosystem resistance and resilience?
6. Compare and contrast the Clementsian and Gleasonian views of ecological succession. Which has more modern support?
7. How do neutral theory and niche theory offer different explanations for biodiversity patterns?

---

## Synthesis Prompt

**Write a 1,500–2,000 word essay** addressing:

> *"How do ecological principles at the population, community, and ecosystem levels interact to shape biodiversity patterns? Use specific models and examples, and identify where ecological theory has direct implications for conservation."*

This essay should demonstrate integration across the module's units and begin building toward Module 2.

---

## Self-Evaluation Rubric

| Criterion | Developing | Proficient | Advanced |
|-----------|-----------|-----------|---------|
| Ecological vocabulary | Can define key terms | Can use terms precisely in context | Can explain nuances and debates around terminology |
| Mathematical models | Can describe models conceptually | Can implement and interpret models | Can critically evaluate model assumptions and limitations |
| Literature engagement | Has read assigned texts | Can summarize key arguments | Can connect papers to each other and identify gaps |
| Quantitative analysis | Can run provided code | Can adapt analyses to new data | Can design appropriate analyses for ecological questions |

---

→ Next: [Module 2: Conservation Biology](02-conservation-biology.md)
