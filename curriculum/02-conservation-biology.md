# Module 2: Conservation Biology

**Estimated time**: 80–100 hours  
**Prerequisites**: Module 1  
**Parallelizable with**: None (required for Modules 3–8)
**Type**: Tier 1 core module  
**Assessment**: Applied analyses + policy/ecology synthesis essay  
**Benchmark mapping**: UC Davis | Yale | Duke | ETH | Imperial

---

## Learning Objectives

By the end of this module, you should be able to:

1. Articulate the intellectual origins and core principles of conservation biology as a crisis discipline
2. Analyze the drivers of biodiversity loss (habitat loss, overexploitation, invasive species, disease, climate change)
3. Apply population viability analysis (PVA) concepts to real species
4. Critically evaluate protected area design using ecological theory
5. Understand the IUCN Red List framework and extinction risk assessment
6. Engage with ethical and value-laden dimensions of conservation

---

## Unit 2.1: Conservation Biology as a Discipline

### Readings

**Primary text**:
> Primack, R.B. (2014). *Essentials of Conservation Biology* (6th ed.). Sinauer Associates.
> - Chapter 1: What is conservation biology?
> - Chapter 2: What is biodiversity?

**Alternative primary text** (either is suitable):
> Sodhi, N.S., & Ehrlich, P.R. (Eds.). (2010). *Conservation Biology for All*. Oxford University Press.
> - **Free**: Available at https://conbio.org/publications/free-textbook
> - Chapters 1–3

**Foundational papers**:
> Soulé, M.E. (1985). What is conservation biology? *BioScience*, 35(11), 727–734. https://doi.org/10.2307/1310054
> - **The** founding document of the discipline — essential reading

> Kareiva, P., & Marvier, M. (2012). What is conservation science? *BioScience*, 62(11), 962–969. https://doi.org/10.1525/bio.2012.62.11.5
> - A more recent, controversial perspective arguing for a human-centered conservation

> Doak, D.F., Bakker, V.J., Goldstein, B.E., & Hale, B. (2014). What is the future of conservation? *Trends in Ecology & Evolution*, 29(2), 77–81.
> - Response to the "new conservation" debate

### Key Concepts
- Conservation biology as a "crisis discipline" (Soulé, 1985)
- Mission-driven vs. curiosity-driven science
- The "new conservation" debate (Kareiva vs. Soulé)
- Biodiversity at genetic, species, and ecosystem levels
- Intrinsic vs. instrumental value of biodiversity

---

## Unit 2.2: Threats to Biodiversity

### Readings

**Primary text** (Primack, 2014):
> - Chapter 3: Threats to biodiversity: Habitat destruction
> - Chapter 4: Threats to biodiversity: Overexploitation, invasive species, and disease

**Seminal papers**:
> Diamond, J.M. (1989). The present, past and future of human-caused extinctions. *Philosophical Transactions of the Royal Society B*, 325(1228), 469–477.

> Wilcove, D.S., Rothstein, D., Dubow, J., Phillips, A., & Losos, E. (1998). Quantifying threats to imperiled species in the United States. *BioScience*, 48(8), 607–615.

> Díaz, S., Settele, J., Brondízio, E.S., et al. (2019). Pervasive human-driven decline of life on Earth points to the need for transformative change. *Science*, 366(6471), eaax3100. https://doi.org/10.1126/science.aax3100
> - Summary of the IPBES Global Assessment — landmark modern reference

> IPBES. (2019). *Global Assessment Report on Biodiversity and Ecosystem Services*. Bonn, Germany.
> - Read: Summary for Policymakers (freely available at https://ipbes.net/global-assessment)

**Supplementary**:
> Clavero, M., & García-Berthou, E. (2005). Invasive species are a leading cause of animal extinctions. *Trends in Ecology & Evolution*, 20(3), 110.

### Key Concepts
- The "Evil Quartet" (Diamond, 1984): habitat loss, overexploitation, introduced species, chains of extinction
- Updated to the "Evil Quintet" (adding climate change and pollution)
- Habitat fragmentation vs. habitat loss (distinct but related)
- Extinction debt
- Defaunation
- Novel ecosystems and invasive species ecology

### Exercise 2.1: Threat Analysis
Choose an endangered species from the [IUCN Red List](https://www.iucnredlist.org/). Conduct a structured threat analysis:
1. Identify the species, its IUCN status, and geographic range
2. Document all identified threats using the IUCN Threats Classification Scheme
3. Assess which threats are primary vs. secondary drivers of decline
4. Review 3–5 recent papers (last 10 years) on this species' conservation status
5. Write a 1,000-word threat assessment report

**Deliverable**: Structured threat assessment report with citations.

---

## Unit 2.3: Small Population Biology

### Readings

**Primary text** (Primack, 2014):
> - Chapter 5: The problems of small populations

**Seminal papers**:
> Caughley, G. (1994). Directions in conservation biology. *Journal of Animal Ecology*, 63(2), 215–244.
> - The "small population paradigm" vs. "declining population paradigm" — enormously influential framework

> Shaffer, M.L. (1981). Minimum population sizes for species conservation. *BioScience*, 31(2), 131–134.
> - Introduced the concept of minimum viable population (MVP)

> Frankham, R. (2005). Genetics and extinction. *Biological Conservation*, 126(2), 131–140. https://doi.org/10.1016/j.biocon.2005.05.002

> Traill, L.W., Bradshaw, C.J.A., & Brook, B.W. (2007). Minimum viable population size: A meta-analysis of 30 years of published estimates. *Biological Conservation*, 139(1-2), 159–166.

### Key Concepts
- Environmental, demographic, and genetic stochasticity
- Allee effects
- Inbreeding depression and genetic drift in small populations
- Effective population size (N_e) vs. census population size (N)
- Minimum viable population (MVP) and the 50/500 rule (and its critiques)
- Population viability analysis (PVA) — basic framework

### Exercise 2.2: Population Viability Analysis (Simplified)
Using Python or R, build a simple individual-based or matrix population model:
1. Implement a stochastic population projection with demographic and environmental stochasticity
2. Run Monte Carlo simulations (1,000+ iterations) to estimate extinction probability over 100 years
3. Explore the effect of different initial population sizes on extinction risk
4. Determine an approximate MVP for your simulated species
5. Discuss: What are the limitations of PVA? When is it useful for conservation decisions?

**Useful R package**: `popbio` (Stubben & Milligan, 2007) for matrix population models

**Deliverable**: Annotated notebook with simulations, figures, and 500-word discussion.

---

## Unit 2.4: Protected Areas and Reserve Design

### Readings

**Primary text** (Primack, 2014):
> - Chapter 8: Protected areas

**Seminal papers**:
> Diamond, J.M. (1975). The island dilemma: Lessons of modern biogeographic studies for the design of natural reserves. *Biological Conservation*, 7(2), 129–146.
> - The "SLOSS" debate begins (Single Large Or Several Small)

> Margules, C.R., & Pressey, R.L. (2000). Systematic conservation planning. *Nature*, 405(6783), 243–253. https://doi.org/10.1038/35012251
> - Landmark paper on how to prioritize areas for conservation

> Watson, J.E.M., Dudley, N., Segan, D.B., & Hockings, M. (2014). The performance and potential of protected areas. *Nature*, 515(7525), 67–73.

> Rodrigues, A.S.L., et al. (2004). Effectiveness of the global protected area network in representing species diversity. *Nature*, 428(6983), 640–643.

**Supplementary**:
> Saura, S., Bertzky, B., Bastin, L., Battistella, L., Mandrici, A., & Dubois, G. (2018). Protected area connectivity: Shortfalls in global targets and country-level priorities. *Biological Conservation*, 219, 53–67.

### Key Concepts
- IUCN Protected Area Categories (I–VI)
- The SLOSS debate and its resolution
- Systematic conservation planning (Margules & Pressey framework)
- Gap analysis
- Connectivity and corridors
- The 30×30 target (Kunming-Montreal Global Biodiversity Framework, 2022)
- "Paper parks" and effectiveness of protection
- Marine protected areas

### Exercise 2.3: Reserve Design Analysis
Using GIS tools (QGIS is free) or R (`sf`, `terra` packages):
1. Select a region of conservation importance
2. Map existing protected areas using the [World Database on Protected Areas (WDPA)](https://www.protectedplanet.net/)
3. Overlay with species richness data or habitat data
4. Identify coverage gaps — are high-biodiversity areas adequately protected?
5. Propose a reserve expansion or corridor using ecological criteria

**Deliverable**: A brief (2–3 page) reserve design report with maps and justification.

---

## Unit 2.5: Species-Level Conservation

### Readings

**Primary text** (Primack, 2014):
> - Chapter 6: Conservation at the species and population level
> - Chapter 7: Ex situ conservation strategies

**Key papers**:
> Caughley, G., & Gunn, A. (1996). *Conservation Biology in Theory and Practice*. Blackwell.
> - Chapters 1–4; excellent framework for thinking about why species decline

> Hayward, M.W., & Somers, M.J. (Eds.). (2009). *Reintroduction of Top-Order Predators*. Wiley-Blackwell.
> - Chapters on wolves, big cats, and other carnivore reintroductions

> Seddon, P.J., Armstrong, D.P., & Maloney, R.F. (2007). Developing the science of reintroduction biology. *Conservation Biology*, 21(2), 303–312.

> IUCN/SSC. (2013). *Guidelines for Reintroductions and Other Conservation Translocations*. Version 1.0. IUCN.
> - Free at: https://portals.iucn.org/library/node/10386

### Key Concepts
- Ex situ vs. in situ conservation
- Captive breeding programs and their challenges
- Reintroduction biology: success factors and monitoring
- Translocation, assisted migration, de-extinction debates
- IUCN Red List criteria and categories
- Recovery planning

---

## Unit 2.6: Ecosystem Services and Valuation

### Readings

**Seminal works**:
> Costanza, R., d'Arge, R., de Groot, R., et al. (1997). The value of the world's ecosystem services and natural capital. *Nature*, 387(6630), 253–260.
> - One of the most cited ecology papers ever; controversial but foundational

> Daily, G.C. (Ed.). (1997). *Nature's Services: Societal Dependence on Natural Ecosystems*. Island Press.

> Millennium Ecosystem Assessment. (2005). *Ecosystems and Human Well-being: Synthesis*. Island Press.
> - Free at: https://www.millenniumassessment.org/

**Critical perspectives**:
> McCauley, D.J. (2006). Selling out on nature. *Nature*, 443(7107), 27–28.

> Silvertown, J. (2015). Have ecosystem services been oversold? *Trends in Ecology & Evolution*, 30(11), 641–648.

### Key Concepts
- Categories of ecosystem services (provisioning, regulating, cultural, supporting)
- Payment for ecosystem services (PES)
- Natural capital accounting
- Critiques of commodifying nature
- The relationship between biodiversity and ecosystem function (BEF)

### Exercise 2.4: Ecosystem Services Assessment
Choose a specific ecosystem (e.g., a local wetland, forest, or coastal area):
1. Identify and categorize the ecosystem services it provides
2. Review 3–5 papers on ecosystem services valuation in that ecosystem type
3. Discuss the methodological challenges of valuation
4. Take a position: Is valuation helpful or harmful for conservation? Write a 1,000-word argument

**Deliverable**: Argumentative essay with citations.

---

## Unit 2.7: Conservation Ethics and Values

### Readings

> Callicott, J.B. (1990). Whither conservation ethics? *Conservation Biology*, 4(1), 15–20.

> Sandler, R. (2012). *The Ethics of Species: An Introduction*. Cambridge University Press.
> - Chapters 1–4

> Vucetich, J.A., Bruskotter, J.T., & Nelson, M.P. (2015). Evaluating whether nature's intrinsic value is an axiom of or anathema to conservation. *Conservation Biology*, 29(2), 321–332.

> Mace, G.M. (2014). Whose conservation? *Science*, 345(6204), 1558–1560. https://doi.org/10.1126/science.1254704
> - Excellent overview of how conservation values have shifted through history

### Key Concepts
- Anthropocentrism vs. biocentrism vs. ecocentrism
- Intrinsic value arguments
- Environmental justice in conservation
- Indigenous and local community perspectives
- "Fortress conservation" and its critique
- Convivial conservation

---

## Comprehension Check

1. What is the difference between the small-population paradigm and the declining-population paradigm (Caughley, 1994)?
2. Explain the SLOSS debate and how modern conservation planning has moved beyond it.
3. What are the five major drivers of biodiversity loss identified by IPBES (2019)?
4. How does effective population size differ from census size, and why does this matter for conservation?
5. What is extinction debt, and why is it relevant to current land-use change?
6. Describe the core tensions in the "new conservation" debate.
7. What criteria does the IUCN use to classify species as critically endangered?

---

## Synthesis Prompt

**Write a 2,000–2,500 word essay** addressing:

> *"Conservation biology claims to be a 'crisis discipline' (Soulé, 1985) that integrates science and values. Critically evaluate this claim. How do scientific evidence and ethical values interact in conservation decision-making? Use specific examples from the readings to illustrate your argument. Where does your political science training inform your analysis?"*

---

## Self-Evaluation Rubric

| Criterion | Developing | Proficient | Advanced |
|-----------|-----------|-----------|---------|
| Threat analysis | Can name major threats | Can analyze threats for specific species/regions | Can evaluate relative importance and interactions among threats |
| Quantitative tools | Understands PVA conceptually | Can conduct basic PVA simulations | Can critically evaluate PVA methodology and assumptions |
| Conservation debate | Knows major positions | Can articulate arguments on multiple sides | Can critically synthesize and take an informed position |
| Policy interface | Recognizes conservation involves policy | Can connect ecology to specific policy tools | Can analyze the political economy of conservation decisions |

---

→ Next: [Module 3: Rewilding: Theory & Practice](03-rewilding-theory-practice.md)
