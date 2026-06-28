# Session starter: Chapter 1.4 - What from scratch means for this book

Develop only Chapter 1.4, **What from scratch means for this book**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch01/04-what-from-scratch-means-for-this-book.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch01/sections/04-what-from-scratch-means-for-this-book.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch01/fig-what-from-scratch-means-for-this-book}`
- `\input{tables/ch01/tab-what-from-scratch-means-for-this-book}`
- `\input{equations/ch01/eq-what-from-scratch-means-for-this-book}`
- `\input{listings/ch01/lst-what-from-scratch-means-for-this-book}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
