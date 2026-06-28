# Session starter: Chapter 11.1 - Experiment design for a from-scratch book

Develop only Chapter 11.1, **Experiment design for a from-scratch book**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch11/01-experiment-design-for-a-from-scratch-book.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch11/sections/01-experiment-design-for-a-from-scratch-book.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch11/fig-experiment-design-for-a-from-scratch-book}`
- `\input{tables/ch11/tab-experiment-design-for-a-from-scratch-book}`
- `\input{equations/ch11/eq-experiment-design-for-a-from-scratch-book}`
- `\input{listings/ch11/lst-experiment-design-for-a-from-scratch-book}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
