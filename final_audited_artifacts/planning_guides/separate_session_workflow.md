# Separate-session workflow

Use this process when developing a single section in a new chat session.

1. Open the relevant file in `section_development_briefs/chXX/`.
2. Use the `Separate-chat handoff prompt` at the bottom of that brief.
3. Edit the section `.tex` file and its four artifact wrappers only.
4. Develop the matching code in the chapter code target listed in the brief.
5. Keep the artifact paths and labels stable.
6. Compile from `latex_book_skeleton/` and run the local smoke diagnostic.
7. Proofread against the acceptance checklist before moving to another section.

## Float placement rule added in Phase 7

Keep `\usepackage{float}` and `\usepackage[section]{placeins}` active in `latex_book_skeleton/main.tex`. Planned teaching figures and tables should default to `[H]` placement inside their standalone wrappers so artifacts stay with the section that introduces them. If a developed section contains unusual float pressure, add an explicit `\FloatBarrier` at the end of that section after the final artifact discussion.