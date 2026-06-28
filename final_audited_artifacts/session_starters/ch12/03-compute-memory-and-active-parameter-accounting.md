# Session starter: Chapter 12.3 - Compute, memory, and active-parameter accounting

Develop only Chapter 12.3, **Compute, memory, and active-parameter accounting**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch12/03-compute-memory-and-active-parameter-accounting.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch12/sections/03-compute-memory-and-active-parameter-accounting.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch12/fig-compute-memory-and-active-parameter-accounting}`
- `\input{tables/ch12/tab-compute-memory-and-active-parameter-accounting}`
- `\input{equations/ch12/eq-compute-memory-and-active-parameter-accounting}`
- `\input{listings/ch12/lst-compute-memory-and-active-parameter-accounting}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
