# MoE Models from Scratch — Claude Code Memory

We are developing a LaTeX-first technical book: *MoE Models from Scratch*.

## Source of truth

Use these files as the canonical planning artifacts:

- `latex_book_skeleton/main.tex`
- `planning_guides/latex_artifact_contract.md`
- `planning_guides/visual_theme_contract.md`
- `planning_guides/proofread_checklist.md`
- `section_data/section_brief_index.csv`
- `section_development_briefs/`
- `.claude/skills/moe-models-from-scratch-developer/SKILL.md`

## Non-negotiable rules

- Work one section at a time unless explicitly asked to do a chapter-level integration pass.
- Keep section prose in `latex_book_skeleton/chapters/chXX/sections/*.tex`.
- Do not inline `figure`, `table`, `lstlisting`, or equation environments inside section prose.
- Every artifact must be included through `\input{...}`.
- Figure, table, listing, and equation wrappers must remain standalone `.tex` files.
- TikZ is used for mechanism diagrams.
- Generated PDF assets are used only for plots, diagnostics, or dashboards.
- Preserve the MiniDeepSeekMoE invariant: router bias affects expert selection only; final combine weights use unbiased selected scores.
- Follow the teaching flow: problem opening -> visual anchor -> tensor/math mechanics -> implementation listing -> diagnostic -> bridge.
- Do not add broad survey material unless the section brief explicitly requires it.

## Validation commands

After editing a section, run:

```bash
python .claude/skills/moe-models-from-scratch-developer/scripts/validate_section_package.py \
  --book-root . \
  --section-index section_data/section_brief_index.csv \
  --section <SECTION_NUMBER>
```

Then compile the book:

```bash
cd latex_book_skeleton
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

If `latexmk` is unavailable, use `pdflatex` twice.

## Reporting

At the end of each task, report:

- files changed
- validation command and result
- LaTeX compile command and result
- unresolved issues, if any
