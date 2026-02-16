# Module 4: Conservation Genetics

**Duration:** 6 weeks  
**Effort:** 15-20 hours/week

## 📋 Overview

Conservation genetics applies genetic principles to preserve biodiversity and manage threatened populations. This module explores how genetic diversity, population structure, and evolutionary processes inform conservation decisions. You'll learn to interpret genetic data and apply genetic tools to conservation challenges.

## 🎯 Learning Objectives

By the end of this module, you should be able to:

1. Understand the importance of genetic diversity for conservation
2. Analyze population genetic structure and gene flow
3. Assess inbreeding and genetic drift in small populations
4. Apply molecular methods to conservation problems
5. Evaluate genetic rescue and translocation strategies
6. Understand the role of genomics in conservation
7. Interpret population viability analyses incorporating genetics

## 📚 Required Reading

### Primary Textbook

- **Frankham, R., Ballou, J.D., & Briscoe, D.A. (2010).** *Introduction to Conservation Genetics* (2nd ed.). Cambridge University Press.  
  *(The standard textbook for conservation genetics)*

**Alternative:**
- **Allendorf, F.W., Luikart, G., & Aitken, S.N. (2013).** *Conservation and the Genetics of Populations* (2nd ed.). Wiley-Blackwell.  
  *(More quantitative, excellent for those with stronger math backgrounds)*

**Reading Schedule:**
- **Weeks 1-2:** Genetic diversity, mutation, drift, gene flow, selection
- **Weeks 3-4:** Population structure, inbreeding, effective population size
- **Weeks 5-6:** Applications: molecular tools, genetic rescue, hybridization

### Key Papers (Required)

**Foundations:**
- Frankham, R. (2005). "Genetics and extinction." *Biological Conservation* 126(2): 131-140.
- Spielman, D., et al. (2004). "Most species are not driven to extinction before genetic factors impact them." *PNAS* 101(42): 15261-15264.
- Lande, R. (1988). "Genetics and demography in biological conservation." *Science* 241(4872): 1455-1460.

**Population Structure & Gene Flow:**
- Palstra, F.P. & Ruzzante, D.E. (2008). "Genetic estimates of contemporary effective population size: what can they tell us about the importance of genetic stochasticity for wild population persistence?" *Molecular Ecology* 17(15): 3428-3447.
- Waples, R.S. & Do, C. (2008). "LDNE: a program for estimating effective population size from data on linkage disequilibrium." *Molecular Ecology Resources* 8(4): 753-756.

**Applied Conservation Genetics:**
- Hedrick, P.W. & Fredrickson, R. (2010). "Genetic rescue guidelines with examples from Mexican wolves and Florida panthers." *Conservation Genetics* 11(2): 615-626.
- vonHoldt, B.M., et al. (2008). "Genome-wide SNP and haplotype analyses reveal a rich history underlying dog domestication." *Nature* 464: 898-902.
- Allendorf, F.W., et al. (2001). "The problems with hybrids: setting conservation guidelines." *Trends in Ecology & Evolution* 16(11): 613-622.

**Conservation Genomics:**
- Shafer, A.B.A., et al. (2015). "Genomics and the challenging translation into conservation practice." *Trends in Ecology & Evolution* 30(2): 78-87.
- Hohenlohe, P.A., et al. (2021). "Genomics of climate change adaptation in threatened species." *Evolutionary Applications* 14(5): 1149-1167.

## 💻 Exercises & Activities

### Week 1-2: Genetic Diversity

**Exercise 4.1: Heterozygosity Calculations**
- Given allele frequency data for multiple populations
- Calculate: observed heterozygosity (Ho), expected heterozygosity (He), allelic richness
- Compare genetic diversity across populations
- Interpret patterns in conservation context
- **Deliverable:** Genetic diversity analysis report with interpretations

**Exercise 4.2: Hardy-Weinberg Equilibrium**
- Test genotype data for HWE departures
- Identify potential causes: inbreeding, population structure, selection
- Use R package: `adegenet`, `pegas`, or `genetics`
- **Deliverable:** HWE analysis with biological interpretations

### Week 3-4: Population Structure

**Exercise 4.3: Population Structure Analysis**
- Analyze microsatellite or SNP data using STRUCTURE or similar
- Determine optimal K (number of populations)
- Visualize population structure and admixture
- Interpret results for conservation management units
- Use R packages: `adegenet`, `hierfstat`, or online tools
- **Deliverable:** Population structure report with visualizations

**Exercise 4.4: Effective Population Size**
- Calculate Ne using multiple methods (heterozygosity excess, linkage disequilibrium, temporal)
- Compare Ne estimates with census size
- Assess population viability using Ne
- Use software: NeEstimator, COLONY, or R packages
- **Deliverable:** Ne estimation and viability assessment

**Exercise 4.5: Gene Flow & Isolation**
- Estimate migration rates between populations
- Calculate FST and related metrics
- Assess genetic isolation and connectivity
- Recommend management strategies for gene flow
- **Deliverable:** Gene flow analysis with management recommendations

### Week 5-6: Applied Conservation Genetics

**Exercise 4.6: Inbreeding Depression Analysis**
- Review data on fitness effects of inbreeding in wild populations
- Calculate inbreeding coefficients from pedigrees
- Analyze relationship between inbreeding and fitness
- Assess risk of inbreeding depression
- **Deliverable:** Inbreeding risk assessment

**Exercise 4.7: Genetic Rescue Evaluation**
- Analyze a case study of genetic rescue (e.g., Florida panther)
- Evaluate evidence for fitness improvement
- Assess risks (outbreeding depression, loss of local adaptation)
- Design genetic rescue strategy for a hypothetical population
- **Deliverable:** Genetic rescue case study and strategy

**Exercise 4.8: Hybridization Policy**
- Examine hybridization between endangered species and related taxa
- Evaluate genetic, ecological, and policy considerations
- Develop management recommendations
- Address ethical dimensions
- **Deliverable:** Hybridization policy analysis

## 🧬 Capstone Project

**Project 4: Conservation Genetics Case Study**

Choose an endangered species or population and conduct comprehensive genetic assessment:

1. **Background Research**
   - Review species biology, threats, population status
   - Summarize existing genetic studies

2. **Genetic Data Analysis** (Choose one approach):
   - **Option A:** Analyze published genetic data (microsatellites or SNPs)
   - **Option B:** Simulate genetic data under different scenarios
   - **Option C:** Meta-analysis of multiple genetic studies

3. **Genetic Assessment**
   - Quantify genetic diversity
   - Assess population structure
   - Estimate effective population size
   - Evaluate inbreeding risk
   - Assess gene flow patterns

4. **Conservation Recommendations**
   - Identify conservation units
   - Recommend translocation strategies
   - Assess need for genetic rescue
   - Propose genetic monitoring plan

5. **Population Viability Assessment**
   - Integrate genetic factors into PVA (if possible)
   - Assess extinction risk with/without management

**Deliverable:** 
- Genetic analysis (code and results)
- Conservation genetics report (3000-4000 words)
- Management recommendations document

## ✅ Self-Assessment

After completing this module, you should be able to:

- [ ] Explain the importance of genetic diversity for population persistence
- [ ] Calculate and interpret genetic diversity metrics
- [ ] Analyze population genetic structure
- [ ] Estimate effective population size
- [ ] Assess inbreeding risk and depression
- [ ] Evaluate genetic rescue strategies
- [ ] Understand when and how to apply molecular tools
- [ ] Integrate genetics into conservation planning
- [ ] Interpret population genetic analyses in papers

## 🔗 Moving Forward

**Prerequisites satisfied for:**
- Module 6: Ecosystem Restoration (genetics of restoration)
- Module 7: Rewilding (reintroduction genetics)

**Related specializations:**
- Wildlife Conservation & Management
- Quantitative Ecology & Modeling

## 🧪 Software & Tools

**Population Genetics:**
- **R packages:** `adegenet`, `hierfstat`, `pegas`, `poppr`, `diveRsity`
- **STRUCTURE:** Population structure analysis
- **GENEPOP:** Population genetics tests
- **Arlequin:** Population genetics statistics

**Effective Population Size:**
- **NeEstimator:** Ne estimation
- **COLONY:** Pedigree and relatedness
- **ONeSAMP:** Ne from single samples

**Phylogenetics & Relationships:**
- **BEAST:** Bayesian phylogenetics
- **RAxML:** Maximum likelihood trees
- **FigTree:** Tree visualization

**Genomics:**
- **GATK:** Variant calling from sequence data
- **VCFtools:** VCF file manipulation
- **PLINK:** SNP data analysis

## 📊 Data Sources

**Example Datasets:**
- **Dryad:** Published genetic datasets
- **NCBI GenBank:** Sequence data
- **PopGen R package:** Example datasets
- **Conservation Genetics Resources:** Supplementary data from papers

**Species Examples with Good Data:**
- Florida panther (genetic rescue)
- Mexican wolf (reintroduction genetics)
- Greater prairie chicken (population decline)
- Cheetah (low genetic diversity)
- Island foxes (recovery and genetics)

## 💡 Study Tips for This Module

1. **Brush up on probability:** Genetics is probabilistic—review basic probability
2. **Practice with simulations:** Use R to simulate genetic processes
3. **Read methods sections carefully:** Genetics methods can be technical
4. **Connect to evolution:** Conservation genetics is applied population genetics
5. **Think about timescales:** Genetic processes operate across generations
6. **Don't get lost in details:** Focus on concepts and conservation applications

## 📖 Additional Resources

**Books:**
- Avise, J.C. & Hamrick, J.L. (1996). *Conservation Genetics: Case Histories from Nature*
- Hartl, D.L. & Clark, A.G. (2007). *Principles of Population Genetics* (background)

**Reviews:**
- Allendorf, F.W. (2017). "Genetics and the conservation of natural populations: allozymes to genomes." *Molecular Ecology* 26(2): 420-430.
- Garner, B.A., et al. (2016). "Genomics in conservation: case studies and bridging the gap between data and application." *Trends in Ecology & Evolution* 31(2): 81-83.

**Online Resources:**
- **Conservation Genetics Resources (journal):** Methods and case studies
- **R Genetics Package Documentation**
- **Molecular Ecology Resources:** Software notes

**Online Courses:**
- Coursera: "Introduction to Genetics and Evolution" (Duke)
- EdX: Various genetics courses

---

*Previous Module: [03 - Ecological Data & Methods](03-ecological-methods.md)*  
*Next Module: [05 - Landscape Ecology](05-landscape-ecology.md)*
