# Session starter: Chapter 3.3 - Top-k selection without dispatch

Develop only Chapter 3.3, **Top-k selection without dispatch**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch03/03-top-k-selection-without-dispatch.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch03/sections/03-top-k-selection-without-dispatch.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch03/fig-top-k-selection-without-dispatch}`
- `\input{tables/ch03/tab-top-k-selection-without-dispatch}`
- `\input{equations/ch03/eq-top-k-selection-without-dispatch}`
- `\input{listings/ch03/lst-top-k-selection-without-dispatch}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
