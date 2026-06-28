# Session starter: Chapter 11.4 - Ablation matrix: dense, top-1, top-2, shared, and bias-balanced

Develop only Chapter 11.4, **Ablation matrix: dense, top-1, top-2, shared, and bias-balanced**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch11/04-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch11/sections/04-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch11/fig-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced}`
- `\input{tables/ch11/tab-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced}`
- `\input{equations/ch11/eq-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced}`
- `\input{listings/ch11/lst-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
