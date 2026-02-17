# Exercises & Problem Sets

This directory contains all exercises from the curriculum modules, compiled for reference. Each exercise is described in detail within its parent module — this page serves as an index and provides additional guidance.

---

## Exercise Index

## Interactive Auto-Graded Exercises (MVP)

You can run objective and rubric-based interactive exercises with the local auto-grading tool:

- Tool docs: [Auto-Graded Interactive Exercises](auto-graded/README.md)
- Runner script: `auto-graded/autograde.py`
- Sample bank: `auto-graded/banks/module-01-foundations.json`
- Sample rubric: `auto-graded/rubrics/restoration-practicum.json`

Quick start from repo root:

```bash
python3 exercises/auto-graded/autograde.py list-banks
python3 exercises/auto-graded/autograde.py run --bank module-01-foundations.json --learner alex
```

Rubric check for restoration practicum drafts:

```bash
python3 exercises/auto-graded/autograde.py rubric \
	--rubric restoration-practicum.json \
	--submission exercises/restoration-practicum.md \
	--learner alex
```

Results are saved to `exercises/auto-graded/results/results.jsonl`.

### Module 0: Prerequisites
| Exercise | Type | Description |
|----------|------|-------------|
| [0.1](../curriculum/00-prerequisites.md) | Reflection | Connecting your disciplines to ecology |
| [0.2](../curriculum/00-prerequisites.md) | Paper response | Analyzing Ostrom (2009) social-ecological systems framework |

### Module 1: Foundations of Ecology
| Exercise | Type | Skills | Description |
|----------|------|--------|-------------|
| [1.1](../curriculum/01-foundations-of-ecology.md) | Coding | Python/R, modeling | Population growth models (exponential, logistic, metapopulation) |
| [1.2](../curriculum/01-foundations-of-ecology.md) | Coding | Python/R, ODEs | Lotka-Volterra predator-prey dynamics and phase portraits |
| [1.3](../curriculum/01-foundations-of-ecology.md) | Data analysis | R/Python, statistics | Biodiversity metrics (Shannon, Simpson, beta diversity) |
| [1.4](../curriculum/01-foundations-of-ecology.md) | Remote sensing | Python/R, spatial | NPP analysis using MODIS satellite data |

### Module 2: Conservation Biology
| Exercise | Type | Skills | Description |
|----------|------|--------|-------------|
| [2.1](../curriculum/02-conservation-biology.md) | Research | Literature review | Threatened species threat assessment using IUCN Red List |
| [2.2](../curriculum/02-conservation-biology.md) | Coding | Python/R, simulation | Population viability analysis (PVA) with Monte Carlo |
| [2.3](../curriculum/02-conservation-biology.md) | Spatial analysis | GIS/R, mapping | Protected area gap analysis with WDPA data |
| [2.4](../curriculum/02-conservation-biology.md) | Essay | Argumentation | Ecosystem services valuation: helpful or harmful? |

### Module 3: Rewilding
| Exercise | Type | Skills | Description |
|----------|------|--------|-------------|
| [3.1](../curriculum/03-rewilding-theory-practice.md) | Conceptual | Synthesis | Concept map of rewilding's intellectual history |
| [3.2](../curriculum/03-rewilding-theory-practice.md) | Critical review | Writing | Critical evaluation of Yellowstone trophic cascade evidence |
| [3.3](../curriculum/03-rewilding-theory-practice.md) | Case study | Research, PSCI | Comprehensive analysis of an active rewilding project |
| [3.4](../curriculum/03-rewilding-theory-practice.md) | Design | Methods | Designing a rewilding monitoring framework |

### Module 4: Landscape Ecology & Spatial Analysis
| Exercise | Type | Skills | Description |
|----------|------|--------|-------------|
| [4.1](../curriculum/04-landscape-ecology-spatial-analysis.md) | Spatial analysis | R/Python, GIS | Landscape connectivity analysis with Circuitscape |
| [4.2](../curriculum/04-landscape-ecology-spatial-analysis.md) | Remote sensing | GEE, Python/R | NDVI time series analysis for rewilding sites |
| [4.3](../curriculum/04-landscape-ecology-spatial-analysis.md) | Modeling | ML, SDM | Species distribution model for a rewilding candidate |
| [4.4](../curriculum/04-landscape-ecology-spatial-analysis.md) | Optimization | R, planning | Conservation prioritization using Marxan/prioritizr |

### Module 5: Quantitative Methods
| Exercise | Type | Skills | Description |
|----------|------|--------|-------------|
| [5.1](../curriculum/05-quantitative-ecology.md) | Statistics | R, GLMs | GLM/GLMM analysis of ecological count data |
| [5.2](../curriculum/05-quantitative-ecology.md) | Modeling | R, `unmarked` | Occupancy modeling with imperfect detection |
| [5.3](../curriculum/05-quantitative-ecology.md) | Multivariate | R, `vegan` | Community ecology ordination and PERMANOVA |
| [5.4](../curriculum/05-quantitative-ecology.md) | Bayesian | Stan/JAGS | Bayesian ecological model with prior specification |
| [5.5](../curriculum/05-quantitative-ecology.md) | Simulation | NetLogo/Python | Agent-based model of rewilding scenario |

### Module 6: Conservation Genetics
| Exercise | Type | Skills | Description |
|----------|------|--------|-------------|
| [6.1](../curriculum/06-conservation-genetics.md) | Simulation | Python/R | Genetic drift simulation across population sizes |
| [6.2](../curriculum/06-conservation-genetics.md) | Management plan | Research, writing | Genetic management plan for a reintroduction program |

### Module 7: Climate Change Ecology
| Exercise | Type | Skills | Description |
|----------|------|--------|-------------|
| [7.1](../curriculum/07-climate-change-ecology.md) | Analysis | R/Python, SDM | Climate-driven range shift analysis |
| [7.2](../curriculum/07-climate-change-ecology.md) | Planning | Research, writing | Climate-adaptive conservation plan |

### Module 8: Conservation Policy & Governance
| Exercise | Type | Skills | Description |
|----------|------|--------|-------------|
| [8.1](../curriculum/08-conservation-policy-governance.md) | Policy analysis | PSCI frameworks | Analysis of Kunming-Montreal Framework |
| [8.2](../curriculum/08-conservation-policy-governance.md) | Institutional analysis | Ostrom IAD | Commons analysis of a conservation dilemma |
| [8.3](../curriculum/08-conservation-policy-governance.md) | Stakeholder analysis | PSCI, governance | Governance analysis of a rewilding project |
| [8.4](../curriculum/08-conservation-policy-governance.md) | Comparative politics | PSCI | Comparative conservation policy analysis |

### Tier 2 and Assessment Extensions
| Exercise | Type | Skills | Description |
|----------|------|--------|-------------|
| [Restoration Practicum](restoration-practicum.md) | Field/design | Monitoring, restoration | Standards-based restoration plan with monitoring protocol |
| [Comprehensive Exam Prep](../assessments/comprehensive-exam-blueprint.md) | Synthesis | Integration, writing | Four-part master-level synthesis exam blueprint |

---

## Exercise Types

| Type | Description | Expected Output |
|------|-------------|-----------------|
| **Coding** | Implement models, run simulations, analyze data | Jupyter notebook or R Markdown with annotated code |
| **Data analysis** | Work with real ecological datasets | Notebook with figures, tables, and interpretation |
| **Spatial analysis** | GIS and remote sensing tasks | Maps, spatial statistics, and interpretation |
| **Research** | Literature review and synthesis | Written report (1,000–3,000 words) with citations |
| **Essay** | Argumentative or reflective writing | Essay (1,000–2,500 words) with citations |
| **Critical review** | Evaluate evidence and arguments | Critical analysis (1,500–2,000 words) |
| **Case study** | In-depth analysis of a specific case | Comprehensive report (2,500–3,000 words) |
| **Design** | Create a plan, framework, or protocol | Structured document with clear specifications |
| **Policy analysis** | Apply PSCI frameworks to conservation | Policy paper (2,000–3,000 words) |
| **Simulation** | Build and run computational models | Code + documentation + results summary |

---

## Guidelines for All Exercises

### Coding Exercises
- Use **Jupyter notebooks** (Python) or **R Markdown** for reproducibility
- Include comments explaining your reasoning, not just code
- Interpret results ecologically — don't just run the code
- Include error handling and sensitivity checks where appropriate
- Store notebooks in a `notebooks/` directory in this repo

### Written Exercises
- Use proper academic citation format (APA 7th edition recommended)
- Back claims with evidence from the literature
- Engage with counterarguments and alternative interpretations
- Write for an interdisciplinary audience (don't assume ecology expertise)
- Store written work in a `portfolio/` directory in this repo

### General
- Quality over quantity — a thoughtful 1,000-word essay beats a superficial 3,000-word one
- It's fine to revisit and improve exercises as you learn more
- Cross-reference between exercises — later work should build on earlier foundations
- Keep a research log documenting your learning process

---

## Suggested Directory Structure

```
self-teach-ecology/
├── notebooks/           # Jupyter/R Markdown exercise notebooks
│   ├── module-01/
│   ├── module-02/
│   ├── ...
│   └── capstone/
├── portfolio/           # Written exercises and essays
│   ├── module-02/
│   ├── module-03/
│   ├── ...
│   └── capstone/
├── data/                # Downloaded datasets (add to .gitignore if large)
└── figures/             # Generated maps and visualizations
```

---

→ Return to [Main Curriculum](../README.md)
