# Proofread checklist

- The section opens from a concrete local problem.
- The figure appears before dense math or code.
- Every tensor in the equation and code listing has a shape or role.
- The diagnostic can catch a realistic implementation bug.
- The table adds structure rather than repeating prose.
- No raw figure/table/listing/equation environments are in section prose.
- All artifacts are included by `\input`.
- The final paragraph bridges to the next planned section.
- The MiniDeepSeekMoE invariant is preserved where relevant: router bias affects selection only, not unbiased combine weights.

## Float placement rule added in Phase 7

Keep `\usepackage{float}` and `\usepackage[section]{placeins}` active in `latex_book_skeleton/main.tex`. Planned teaching figures and tables should default to `[H]` placement inside their standalone wrappers so artifacts stay with the section that introduces them. If a developed section contains unusual float pressure, add an explicit `\FloatBarrier` at the end of that section after the final artifact discussion.