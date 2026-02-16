# Curriculum Update & Enhancement Plan (2026 Revision)

This plan translates `enhancement_doc.md` into an implementation roadmap for revising and extending the existing self-taught master's curriculum.

## 1) Revision Goals

1. Align curriculum breadth with benchmark expectations from UC Davis, Yale, Duke, ETH Zurich, and Imperial.
2. Add stronger systems ecology/complexity and restoration depth.
3. Standardize module-level metadata (resource type, hours, prerequisites, assessment, benchmark mapping).
4. Increase applied practice (field methods, reproducible computational workflows, capstone rigor).
5. Improve governance: versioned updates, contributor workflow, and measurable competency milestones.

---

## 2) Current State Snapshot (What Exists)

The repository already has a strong base:

- 11 curriculum modules (`00`–`10`) covering foundations through capstone.
- Reading lists, exercises index, datasets/tools guide, and a progress tracker.
- Explicit tailoring to PSCI + data science background.
- Existing quantitative and rewilding coverage is solid.

Primary gaps relative to the enhancement brief:

- No explicit benchmark matrix mapping curriculum to specific MS-program requirements.
- No dedicated systems ecology/complexity track with canonical sequence (Odum → Meadows → Holling/Scheffer → network ecology).
- Restoration appears as an elective, but not as a fully structured standards-driven track with field protocol progression.
- Metadata format is not standardized across all modules/resources.
- No explicit “comprehensive exam” style milestone to validate master's-level synthesis.
- Community/process docs (`CONTRIBUTING`, `CHANGELOG`, versioning policy) are missing.

---

## 3) Scope of Revision

### In Scope

- Re-architect curriculum into a clearly signposted Tier 0–3 model without deleting existing module content.
- Add specialization tracks and benchmark mappings.
- Add assessment architecture: milestone exams, competency grid, capstone quality gates.
- Improve practical components (field and computational).
- Add maintenance/governance documentation.

### Out of Scope (for this revision cycle)

- Building a full website/app.
- Creating original datasets.
- Rewriting all module prose from scratch.

---

## 4) Workstreams and Deliverables

## Workstream A — Program Benchmarking & Standards Mapping

**Objective:** demonstrate equivalence to key master's competencies.

### Deliverables

1. `curriculum/11-benchmark-mapping.md`
   - Matrix: UC Davis, Yale, Duke, ETH, Imperial requirements vs. curriculum modules.
   - Four universal pillars coverage check: ecology theory, quant methods, research design, thesis/capstone.
2. `resources/competency-framework.md`
   - Beginner → proficient → advanced outcomes for theory, methods, field skills, policy/governance, synthesis.
3. README section update summarizing benchmark compliance.

### Acceptance Criteria

- Every benchmark program has explicit coverage mapping.
- At least one module/elective mapped to each benchmark requirement domain.

---

## Workstream B — Tiered Structure & Metadata Normalization

**Objective:** make curriculum easier to navigate and auditable.

### Deliverables

1. Revise `README.md` to use Tier 0/1/2/3 architecture:
   - Tier 0: Bridge/prerequisites
   - Tier 1: Core ecology + conservation
   - Tier 2: Specialization tracks
   - Tier 3: Capstone
2. Add `resources/module-template.md`
   - Required fields: title, type, links, estimated hours, prerequisites, assessments, benchmark mapping.
3. Apply standardized metadata block to all files in `curriculum/*.md`.

### Acceptance Criteria

- Every module starts with a consistent metadata block.
- Estimated effort is coherent at module and curriculum totals.

---

## Workstream C — Systems Ecology & Complexity Track

**Objective:** add master’s-level depth in systems/complexity/network ecology.

### Deliverables

1. `curriculum/tracks/systems-ecology-complexity.md`
   - Foundations: Odum, Meadows, Holling, Scheffer, Levin.
   - Network ecology: May, Dunne, Bascompte; methods with `igraph`/`bipartite`.
   - ABM pipeline: Railsback & Grimm, ODD protocol, NetLogo/Mesa.
2. Exercises package:
   - Regime-shift detection mini-project (early warning signals).
   - Food-web robustness simulation.
   - ODD-documented ABM build.
3. Add SFI Complexity Explorer and nonlinear dynamics resources to study sequence.

### Acceptance Criteria

- Track contains progressive sequence (concepts → methods → project).
- At least 3 graded rubrics/project prompts are included.

---

## Workstream D — Restoration Ecology Expansion

**Objective:** elevate restoration to standards-based practical specialization.

### Deliverables

1. `curriculum/tracks/restoration-ecology-advanced.md`
   - Core texts: Holl, Palmer et al., SER Standards, novel ecosystems debate.
   - Practice framework: reference ecosystems, recovery wheel, adaptive management.
2. Field-practice kit:
   - `resources/field-methods-checklists.md`
   - `exercises/restoration-practicum.md` (site audit, vegetation transects, photo points, monitoring plan).
3. Integrate UN Decade/Bonn Challenge context and peatland case module notes.

### Acceptance Criteria

- Track includes at least one field-forward practicum and one full restoration-plan deliverable.
- SER standards are explicitly used as grading criteria.

---

## Workstream E — Computational Ecology Deepening

**Objective:** maximize leverage of learner’s data science strengths.

### Deliverables

1. Add `curriculum/tracks/computational-ecology.md` with four method pathways:
   - SDM (MaxEnt/`maxnet`/`biomod2`)
   - Bayesian ecology (`brms`, Stan, PyMC)
   - Remote sensing (GEE + `geemap`/`terra`)
   - Ecological networks (`bipartite`, `igraph`, `NetworkX`)
2. Add reproducibility standards:
   - project templates, environment lockfile guidance, data provenance checklist.
3. Expand capstone examples with 10 project archetypes from the brief.

### Acceptance Criteria

- At least 1 end-to-end notebook template per method pathway.
- Capstone options include clear “minimum publishable” criteria.

---

## Workstream F — Assessment, Milestones, and Quality Gates

**Objective:** ensure mastery claims are evidence-based, not just completion-based.

### Deliverables

1. `assessments/comprehensive-exam-blueprint.md`
   - Written synthesis prompts across population, community, ecosystem, landscape, conservation, and methods.
2. `assessments/rubrics.md`
   - Rubrics for reading syntheses, computational projects, policy analyses, and capstone.
3. Update `PROGRESS.md` with milestone checkpoints:
   - Tier completion gates
   - Benchmark readiness checks
   - Portfolio artifact checklist

### Acceptance Criteria

- Progress tracker includes measurable pass/fail criteria per milestone.
- Capstone rubric supports external review by mentor/peer.

---

## Workstream G — Repository Governance & Contribution Workflow

**Objective:** make the curriculum maintainable and community-editable.

### Deliverables

1. `CONTRIBUTING.md`
   - Resource inclusion criteria, citation standards, issue templates.
2. `CHANGELOG.md`
   - Semantic versioning for curriculum releases (e.g., v1.1, v1.2).
3. Optional `.github/ISSUE_TEMPLATE/` for resource request and content correction.

### Acceptance Criteria

- Contributors can propose updates without ambiguity.
- Major curriculum revisions are traceable by version.

---

## 5) Implementation Sequence (Recommended)

## Phase 1 (High Priority, 1–2 weeks)

- Workstream A (benchmark mapping)
- Workstream B (tiering + metadata)
- Workstream F (assessment blueprint baseline)

## Phase 2 (Medium Priority, 2–3 weeks)

- Workstream C (systems/complexity track)
- Workstream D (restoration expansion)

## Phase 3 (Medium Priority, 1–2 weeks)

- Workstream E (computational deepening + templates)
- Workstream G (governance docs)

## Phase 4 (Polish, 1 week)

- Reading list refresh (core + journals)
- Link validation and duplication cleanup
- README simplification for first-time users

---

## 6) File-by-File Revision Plan

- `README.md`
  - Add Tier architecture, benchmark summary, and “how mastery is assessed” section.
- `curriculum/00-prerequisites.md`
  - Add non-biology bridge pathway with explicit organismal/field-methods prerequisites.
- `curriculum/01`–`08`
  - Add standardized metadata + benchmark mapping tags at top.
- `curriculum/09-electives.md`
  - Convert to specialization catalog that links out to track-specific files.
- `curriculum/10-capstone-project.md`
  - Expand with 10 capstone archetypes + reproducibility and publication-quality checklist.
- `reading-lists/core-texts.md`, `reading-lists/journal-articles.md`
  - Add systems/complexity and restoration frontier references from the brief.
- `resources/datasets-and-tools.md`
  - Add structured pathways by method + package stack by language.
- `PROGRESS.md`
  - Add competency milestones and comprehensive exam readiness checks.

---

## 7) Risks and Mitigations

- **Risk:** scope bloat from too many new resources.
  - **Mitigation:** keep one “primary” resource per concept + optional alternates.
- **Risk:** redundancy between modules and tracks.
  - **Mitigation:** treat tracks as depth layers; link back to core modules instead of duplicating theory.
- **Risk:** uneven rigor of assessments.
  - **Mitigation:** centralized rubric file used across all modules.

---

## 8) Definition of Done for This Revision Cycle

The revision cycle is complete when:

1. Tier 0–3 architecture is visible in README and module navigation.
2. Benchmark mapping document demonstrates coverage of MS-level expectations.
3. Systems ecology/complexity and restoration tracks are fully published.
4. Assessment blueprints and rubrics are integrated into progress tracking.
5. Governance docs (`CONTRIBUTING`, `CHANGELOG`) are in place.

---

## 9) Suggested Immediate Next Action

Start with **Phase 1** by creating:

1. `curriculum/11-benchmark-mapping.md`
2. `resources/module-template.md`
3. `assessments/comprehensive-exam-blueprint.md`

This yields the largest structural improvement early and makes all later content additions more consistent.