# Session starter: Chapter 4.2 - Assignment masks and expert buckets

Develop only Chapter 4.2, **Assignment masks and expert buckets**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch04/02-assignment-masks-and-expert-buckets.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch04/sections/02-assignment-masks-and-expert-buckets.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch04/fig-assignment-masks-and-expert-buckets}`
- `\input{tables/ch04/tab-assignment-masks-and-expert-buckets}`
- `\input{equations/ch04/eq-assignment-masks-and-expert-buckets}`
- `\input{listings/ch04/lst-assignment-masks-and-expert-buckets}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
