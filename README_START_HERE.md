# Start here - MoE Models from Scratch final audited kit

This package is the final Phase 7 handoff for developing *MoE Models from Scratch* in LaTeX.

Start with these paths:

```text
final_audited_artifacts/latex_book_skeleton/main.tex
final_audited_artifacts/section_development_briefs/
final_audited_artifacts/skill_framework/
skill.zip
```

Use one section brief per new development chat. Each brief names the exact section `.tex` file, the exact artifact wrappers, the required `\input{...}` lines, the visual theme, the planned code path, and the diagnostic that must pass.

The final proofreading pass added a production fix: planned teaching figures and tables now use `[H]` placement with `\usepackage{float}` and `\usepackage[section]{placeins}` so artifacts stay with their owning section.

The installable skill is the top-level `skill.zip`.
