# Module 6: Conservation Genetics

**Estimated time**: 40–60 hours  
**Prerequisites**: Modules 1–2 (plus basic genetics from Module 0)  
**Parallelizable with**: Modules 3–5, 7

---

## Learning Objectives

By the end of this module, you should be able to:

1. Explain how genetic diversity relates to population viability and adaptive potential
2. Apply population genetics principles to conservation problems
3. Understand molecular tools used in conservation (microsatellites, SNPs, genomics, eDNA)
4. Evaluate the genetic consequences of small population size, fragmentation, and bottlenecks
5. Assess the role of genetics in rewilding and reintroduction programs
6. Critically evaluate the emerging field of conservation genomics

---

## Unit 6.1: Population Genetics for Conservation

### Readings

**Primary text**:
> Frankham, R., Ballou, J.D., & Briscoe, D.A. (2010). *Introduction to Conservation Genetics* (2nd ed.). Cambridge University Press.
> - Chapters 1–5, 8–12
> - **The** standard textbook for this field

**Alternative text** (more recent):
> Allendorf, F.W., Luikart, G., & Aitken, S.N. (2013). *Conservation and the Genetics of Populations* (2nd ed.). Wiley-Blackwell.
> - Chapters 1–7, 18–20

**Foundational paper**:
> Frankham, R. (2005). Genetics and extinction. *Biological Conservation*, 126(2), 131–140. https://doi.org/10.1016/j.biocon.2005.05.002

### Key Concepts
- Genetic diversity: heterozygosity, allelic richness, nucleotide diversity
- Hardy-Weinberg equilibrium — and departures from it
- Genetic drift and effective population size (N_e)
- Inbreeding depression and its fitness consequences
- The 50/500 rule (Franklin, 1980) and its modern update to the "100/1000 rule"
  - Frankham, R., Bradshaw, C.J.A., & Brook, B.W. (2014). Genetics in conservation management: Revised recommendations for the 50/500 rules, Red List criteria and population viability analyses. *Biological Conservation*, 170, 56–63.
- Gene flow and its conservation importance
- Mutation-selection balance

---

## Unit 6.2: Genetic Consequences of Small Populations

### Readings

> Frankham et al. (2010), Chapters 8–12

> Crnokrak, P., & Roff, D.A. (1999). Inbreeding depression in the wild. *Heredity*, 83(3), 260–270.

> Saccheri, I., Kuussaari, M., Kankare, M., Vikman, P., Fortelius, W., & Hanski, I. (1998). Inbreeding and extinction in a butterfly metapopulation. *Nature*, 392(6675), 491–494.
> - Classic empirical demonstration that inbreeding increases extinction risk

> Spielman, D., Brook, B.W., & Frankham, R. (2004). Most species are not driven to extinction before genetic factors impact them. *Proceedings of the National Academy of Sciences*, 101(42), 15261–15264.

### Key Concepts
- Inbreeding coefficient (F) and its calculation
- Inbreeding depression: mechanisms (dominance, overdominance)
- Genetic drift in small populations
- Bottlenecks and founder effects
- Loss of heterozygosity over generations: $H_t = H_0 \left(1 - \frac{1}{2N_e}\right)^t$
- Genetic rescue (immigration to restore genetic diversity)
- The extinction vortex (Gilpin & Soulé, 1986)

### Exercise 6.1: Simulating Genetic Drift
Using Python or R:
1. Simulate genetic drift in populations of different sizes (N = 10, 50, 200, 1000)
2. Track allele frequencies over 100 generations
3. Calculate expected vs. observed heterozygosity loss
4. Simulate a population bottleneck and subsequent recovery
5. Explore: At what population size does drift become negligible?

**Deliverable**: Simulation notebook with figures and 500-word interpretation.

---

## Unit 6.3: Molecular Tools in Conservation

### Readings

> Allendorf et al. (2013), Chapters 3–4

> Shafer, A.B.A., Wolf, J.B.W., Alves, P.C., et al. (2015). Genomics and the challenging translation into conservation practice. *Trends in Ecology & Evolution*, 30(2), 78–87.

> Bohmann, K., Evans, A., Gilbert, M.T.P., et al. (2014). Environmental DNA for wildlife biology and biodiversity monitoring. *Trends in Ecology & Evolution*, 29(6), 358–367.

> Thomsen, P.F., & Willerslev, E. (2015). Environmental DNA — An emerging tool in conservation for monitoring past and present biodiversity. *Biological Conservation*, 183, 4–18.

### Key Concepts
- Molecular markers: microsatellites, SNPs, whole-genome sequencing
- Population structure analysis (F_ST, STRUCTURE, PCA of genotypes)
- Phylogeography and its conservation applications
- Environmental DNA (eDNA) — detecting species from water/soil samples
- eDNA metabarcoding for community-level monitoring
- Ancient DNA and historical baselines
- Landscape genetics: combining spatial and genetic data

---

## Unit 6.4: Genetics in Reintroduction and Rewilding

### Readings

> Jamieson, I.G., & Lacy, R.C. (2012). Managing genetic issues in reintroduction biology. In J.G. Ewen, D.P. Armstrong, K.A. Parker, & P.J. Seddon (Eds.), *Reintroduction Biology: Integrating Science and Management* (pp. 441–475). Wiley-Blackwell.

> Frankham, R. (2015). Genetic rescue of small inbred populations: Meta-analysis reveals large and consistent benefits of gene flow. *Molecular Ecology*, 24(11), 2610–2618.

> Whiteley, A.R., Fitzpatrick, S.W., Funk, W.C., & Tallmon, D.A. (2015). Genetic rescue to the rescue. *Trends in Ecology & Evolution*, 30(1), 42–49.

> Johnson, W.E., Onorato, D.P., Roelke, M.E., et al. (2010). Genetic restoration of the Florida panther. *Science*, 329(5999), 1641–1645.
> - A celebrated case of genetic rescue in practice

### Key Concepts
- Source population selection for reintroductions
- Genetic management of captive breeding programs (minimizing kinship)
- Genetic rescue: introducing individuals to restore diversity
- Admixture and outbreeding depression risks
- Managing genetic diversity in fragmented populations
- Assisted gene flow and managed relocation

### Exercise 6.2: Genetic Management Plan
Choose a species with an active reintroduction or captive breeding program:
1. Review the species' genetic status (published studies on genetic diversity, N_e, population structure)
2. Evaluate the genetic management strategies currently in use
3. Assess risks (inbreeding depression, outbreeding depression, genetic drift)
4. Propose a genetic management plan: source populations, number of founders, gene flow strategy
5. How would you use genomic data to improve management?

**Suggested species**: Florida panther, California condor, black-footed ferret, European bison, Iberian lynx, kakapo

**Deliverable**: 2,000-word genetic management plan with citations.

---

## Unit 6.5: Conservation Genomics

### Readings

> Hohenlohe, P.A., Funk, W.C., & Rajora, O.P. (2021). Population genomics for wildlife conservation and management. *Molecular Ecology*, 30(1), 62–82.

> Supple, M.A., & Shapiro, B. (2018). Conservation of biodiversity in the genomics era. *Genome Biology*, 19, 131.

> Garner, B.A., Hand, B.K., Amish, S.J., et al. (2016). Genomics in conservation: Case studies and bridging the gap between data and application. *Trends in Ecology & Evolution*, 31(2), 81–83.

### Key Concepts
- Whole-genome sequencing for conservation
- Adaptive genetic variation and local adaptation
- Genotype-environment associations (GEA)
- Genomic vulnerability to climate change
- CRISPR and gene drives: potential conservation applications and risks
- Ethical considerations in genetic intervention

---

## Comprehension Check

1. Why is effective population size (N_e) typically much smaller than census size (N)?
2. Explain how inbreeding depression occurs at the molecular level.
3. What is genetic rescue, and what conditions make it advisable vs. risky?
4. How does eDNA detection work, and what are its advantages and limitations for biodiversity monitoring?
5. Why is genetic diversity important for long-term population viability?
6. What genetic considerations should guide the selection of source populations for reintroduction?
7. What is landscape genetics, and how does it integrate with rewilding planning?

---

## Synthesis Prompt

**Write a 1,500–2,000 word essay** addressing:

> *"Evaluate the role of genetics and genomics in 21st-century rewilding. How should genetic data inform decisions about species reintroductions, population management, and habitat connectivity? Use specific examples and consider both the potential and the limitations of genomic approaches."*

---

→ Next: [Module 7: Climate Change Ecology](07-climate-change-ecology.md)
