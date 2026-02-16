# Contributing to Self-Taught Conservation Ecology

Thank you for your interest in improving this curriculum! This is a community-driven project that benefits from diverse perspectives and experiences.

## 🎯 How You Can Contribute

### 1. Share Your Experience

**Learning Journey Reports:**
- Complete modules and share what worked/didn't work
- Suggest improvements to exercises
- Recommend additional resources you found helpful

**Create Issues for:**
- Broken links
- Outdated information
- Unclear instructions
- Missing prerequisites
- Suggested improvements

### 2. Improve Content

**Good First Contributions:**
- Fix typos and grammatical errors
- Update broken links
- Add references to recent papers (last 2-3 years)
- Improve clarity of existing content
- Add learning tips based on your experience

**Substantial Contributions:**
- Create new exercises or projects
- Develop new module content
- Add new specialization tracks
- Create video tutorials or guides
- Translate content to other languages

### 3. Expand Resources

**Add:**
- New datasets suitable for exercises
- Free online courses or textbooks
- Relevant software tools
- Case studies
- Open access papers

**Maintain:**
- Keep links current
- Update software installation instructions
- Refresh reading lists with recent publications

### 4. Build Community

- Answer questions from learners
- Share your projects and solutions
- Write blog posts about your learning journey
- Create study groups
- Mentor others

## 📝 Contribution Guidelines

### Before Contributing

1. **Check existing issues/PRs:** Someone may already be working on it
2. **Create an issue first:** For substantial changes, discuss the idea before investing time
3. **Stay focused:** Keep contributions specific and manageable

### Content Standards

**Quality Criteria:**
- **Accessible:** Assume master's level but explain technical terms
- **Evidence-based:** Cite peer-reviewed sources where appropriate
- **Practical:** Include actionable exercises and clear learning objectives
- **Inclusive:** Consider diverse backgrounds and learning styles
- **Current:** Use recent publications (prefer last 5-10 years unless classic papers)

**Writing Style:**
- Clear, concise, and engaging
- Use active voice
- Define jargon when first used
- Include examples
- Use headings and lists for readability

**Markdown Formatting:**
- Use proper heading hierarchy (# for title, ## for sections, ### for subsections)
- Include tables of contents for long documents
- Use code blocks with language specification
- Include links to external resources
- Add emoji sparingly for visual interest

### Citation Guidelines

**When adding papers:**
- Use consistent citation format: Author(s). (Year). "Title." *Journal* Volume(Issue): Pages.
- Prefer open access when available
- Note if subscription required
- Include DOI links when possible

**Example:**
```markdown
- Smith, J.A. & Jones, B.C. (2023). "Conservation in the Anthropocene." *Conservation Biology* 37(2): 123-145. [Open Access] https://doi.org/10.xxxx/xxxxx
```

### Code & Data

**If contributing code:**
- Follow existing style conventions
- Comment your code
- Test on your system before submitting
- Use relative paths
- Include package/library requirements

**If contributing datasets:**
- Ensure proper licensing for sharing
- Document data source and collection methods
- Provide metadata and data dictionary
- Keep file sizes reasonable (<10MB if possible)
- Use standard formats (CSV, GeoJSON, etc.)

## 🔄 Pull Request Process

### 1. Fork the Repository

```bash
# Fork via GitHub interface, then clone your fork
git clone https://github.com/YOUR_USERNAME/self-teach-ecology.git
cd self-teach-ecology
```

### 2. Create a Branch

```bash
# Create descriptive branch name
git checkout -b add-marine-conservation-specialization
# or
git checkout -b fix-broken-links-module-03
```

### 3. Make Your Changes

- Edit files using your preferred text editor
- Keep commits focused and atomic
- Write clear commit messages

```bash
git add path/to/changed/file.md
git commit -m "Add marine conservation specialization track"
```

### 4. Test Your Changes

- Check all links work
- Verify markdown renders correctly (use GitHub preview or local renderer)
- Ensure code examples run
- Proofread for typos

### 5. Submit Pull Request

```bash
git push origin your-branch-name
```

Then create PR via GitHub interface with:
- **Clear title:** What does this PR do?
- **Description:** Why is this change needed? What does it improve?
- **Checklist:** Confirm you've followed guidelines

**PR Template:**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (broken link, typo)
- [ ] New content (module, exercise, resources)
- [ ] Enhancement (improved clarity, additional examples)
- [ ] Documentation

## Checklist
- [ ] I've tested all links
- [ ] I've checked markdown formatting
- [ ] I've followed citation guidelines
- [ ] I've proofread my changes
```

### 6. Respond to Feedback

- Maintainers may request changes
- Address feedback promptly
- Ask for clarification if needed
- Be open to suggestions

## 🚫 What Not to Contribute

**Avoid:**
- Promotional content for paid courses/products
- Copyrighted material without permission
- Very specific/niche content without broad relevance
- Personal opinions without scientific backing
- Content requiring expensive software/subscriptions
- Very large files (>10MB)

## 🎓 Content Organization

### File Structure

```
self-teach-ecology/
├── README.md (main curriculum overview)
├── modules/ (required core modules)
│   ├── 01-ecology-fundamentals.md
│   ├── 02-conservation-biology.md
│   └── ...
├── specializations/ (optional tracks)
│   ├── conservation-data-science.md
│   └── ...
├── guides/ (how-to guides)
│   ├── setup.md
│   ├── community.md
│   └── ...
├── exercises/ (shared exercise resources)
├── resources/ (datasets, templates, etc.)
└── CONTRIBUTING.md (this file)
```

### Module Template

Each module should include:
1. Duration and effort estimate
2. Overview and learning objectives
3. Required reading with schedule
4. Exercises and projects
5. Self-assessment checklist
6. Prerequisites and next steps
7. Additional resources

## 💡 Ideas for Contributions

### High Priority

- [ ] Create remaining core modules (04, 05, 06, 09)
- [ ] Develop additional specialization tracks
- [ ] Add more coding exercises with solutions
- [ ] Create video walkthroughs for complex exercises
- [ ] Translate content to other languages

### Medium Priority

- [ ] Curate datasets for exercises
- [ ] Create templates for reports/projects
- [ ] Write guides for specific tools (QGIS, GEE, etc.)
- [ ] Develop assessment rubrics
- [ ] Add career advice section

### Ongoing

- Keep reading lists current
- Update software versions and installation guides
- Maintain link validity
- Respond to learner questions in issues

## 🏆 Recognition

Contributors will be acknowledged in:
- Contributors list (added automatically by GitHub)
- Acknowledgments section of README (for substantial contributions)
- Individual module credits (for module creators)

## 📞 Questions?

- **Quick questions:** Open an issue with "Question:" prefix
- **Ideas to discuss:** Open an issue with "Discussion:" prefix
- **Problems with contribution:** Mention @maintainer in your PR

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring environment for all contributors. We pledge to:
- Be respectful and inclusive
- Welcome diverse perspectives and experiences
- Accept constructive criticism gracefully
- Focus on what's best for the community and learners

### Unacceptable Behavior

- Harassment, discrimination, or exclusionary behavior
- Trolling, insulting, or derogatory comments
- Publishing others' private information
- Other conduct inappropriate in a professional setting

### Enforcement

Violations can be reported to project maintainers. All complaints will be reviewed and investigated promptly and fairly. Maintainers have the right to remove, edit, or reject contributions that violate this code of conduct.

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as the project (CC BY-SA 4.0). This means:
- Your contributions can be freely shared and adapted
- Attribution must be given
- Derivative works must use the same license

---

**Thank you for helping build a better conservation ecology curriculum!** 🌍🌱

Every contribution, no matter how small, helps make conservation education more accessible to everyone.

*Back to [Main Curriculum](README.md)*
