# Prompt 03 — Chapter integration pass

Use after all six sections of a chapter are drafted and committed.

```text
/moe-models-from-scratch-developer

Perform a Chapter <CHAPTER_NUMBER> integration pass.

Scope:

- latex_book_skeleton/chapters/chXX/chapter.tex
- latex_book_skeleton/chapters/chXX/sections/*.tex
- latex_book_skeleton/figures/chXX/*.tex
- latex_book_skeleton/tables/chXX/*.tex
- latex_book_skeleton/listings/chXX/*.tex
- latex_book_skeleton/equations/chXX/*.tex

Tasks:

1. Do not introduce new planned artifacts unless necessary.
2. Smooth transitions between sections.
3. Remove repeated explanations.
4. Check that notation is introduced before use.
5. Check that every figure/table/listing/equation is referenced in prose.
6. Check that diagnostics are falsifiable.
7. Preserve every `\input{...}` artifact pattern.
8. Compile the book.
9. Report changed files and remaining issues.

Do not rewrite the chapter from scratch.
```
