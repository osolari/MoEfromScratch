# Phase 4 report - full book plan

Phase 4 converts the confirmed **MiniDeepSeekMoE** reference model into a complete LaTeX-first book blueprint.

## Main decision

The book should be organized as a progressive build, not a survey. Each chapter starts with a concrete bottleneck, introduces a visual mechanism, pins it down with tensor shapes/equations, implements the mechanism from scratch, and ends with a diagnostic or comparison.

## Planned structure

- 12 chapters across five parts
- 72 planned sections
- 288 LaTeX artifact placeholders generated as standalone `.tex` files
- 3 appendices planned for reproducibility, shapes, and validation

## Production rule confirmed

Every planned figure, table, listing, and equation placeholder lives in its own `.tex` file and is included from the section with `\input{...}`. Chapter and section prose do not contain raw figure, table, listing, or TikZ bodies.

## Package contents

```text
moe_from_scratch_phase4_complete/
├── PHASE_4_REPORT.md
├── overall_plan/
│   ├── book_plan.md
│   ├── chapter_sequence.md
│   ├── codebase_layout_plan.md
│   ├── latex_project_layout.md
│   ├── artifact_master_index.md
│   └── development_milestones.md
├── chapter_plans/ch01_*.md ... ch12_*.md
├── section_plans/ch01/*.md ... ch12/*.md
├── data/
│   ├── book_plan.json
│   ├── chapter_sequence.csv
│   ├── section_index.csv
│   └── artifact_index.csv
├── latex_book_skeleton/
│   ├── main.tex
│   ├── phase4_book_plan_preview.pdf
│   ├── chapters/chNN/chapter.tex
│   ├── chapters/chNN/sections/*.tex
│   ├── figures/chNN/*.tex
│   ├── tables/chNN/*.tex
│   ├── listings/chNN/*.tex
│   └── equations/chNN/*.tex
└── validation/
    ├── phase4_validation_notes.md
    ├── latex_compile.log
    └── rendered_preview/page-*.png
```

## What remains for the next phase

Phase 5 should convert these plans into section-development packs that can be handed to separate chat sessions, with stronger acceptance rubrics, section-specific writing prompts, and per-section implementation checklists. Phase 6 should package those development frameworks as skill-style `SKILL.md` files.

## Final validation

The LaTeX skeleton compiles successfully from a clean auxiliary state. The final validation pass reports zero missing `\input` targets and zero artifact-wrapper failures.

| Item | Count |
|---|---:|
| Chapters | 12 |
| Sections | 72 |
| Standalone artifacts | 288 |
| TikZ diagram figure wrappers | 59 |
| PDF figure wrappers with `\includegraphics` | 13 |
| Tables | 72 |
| Listings | 72 |
| Equations | 72 |
| Rendered preview pages checked | 10 |

The generated preview PDF is `latex_book_skeleton/phase4_book_plan_preview.pdf`.
