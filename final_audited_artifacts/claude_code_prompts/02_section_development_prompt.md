# Prompt 02 — Develop one section

Replace `<SECTION_NUMBER>`, `<brief path>`, and `<target section file>` before pasting into Claude Code.

```text
/moe-models-from-scratch-developer

Develop Section <SECTION_NUMBER> only.

Target brief:
<brief path>

Target section file:
<target section file>

Instructions:

1. Read the section brief completely.
2. Read the relevant chapter packet if needed.
3. Edit only the target section file and the planned artifact wrappers named in the brief.
4. Keep figure/table/listing/equation environments out of the section prose.
5. Include artifacts only with the planned `\input{...}` lines.
6. Implement the planned TikZ figure/table/equation/listing placeholders as real teaching artifacts.
7. Preserve the visual theme and color map from the planning guide.
8. Add or update code only if the section brief requires it.
9. Run the section validator for section <SECTION_NUMBER>.
10. Compile the LaTeX book.
11. Report changed files and paste the validation/compile evidence.

Do not edit any other section.
```

Example for Section 3.2:

```text
/moe-models-from-scratch-developer

Develop Section 3.2 only.

Target brief:
section_development_briefs/ch03/02-router-scores-and-tensor-shapes.md

Target section file:
latex_book_skeleton/chapters/ch03/sections/02-router-scores-and-tensor-shapes.tex

Instructions:

1. Read the section brief completely.
2. Read the relevant chapter packet if needed.
3. Edit only the target section file and the planned artifact wrappers named in the brief.
4. Keep figure/table/listing/equation environments out of the section prose.
5. Include artifacts only with the planned `\input{...}` lines.
6. Implement the planned TikZ figure/table/equation/listing placeholders as real teaching artifacts.
7. Preserve the visual theme and color map from the planning guide.
8. Add or update code only if the section brief requires it.
9. Run the section validator for section 3.2.
10. Compile the LaTeX book.
11. Report changed files and paste the validation/compile evidence.

Do not edit any other section.
```
