# Session starter: Chapter 7.1 - Expert imbalance as a training problem

Develop only Chapter 7.1, **Expert imbalance as a training problem**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch07/01-expert-imbalance-as-a-training-problem.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch07/sections/01-expert-imbalance-as-a-training-problem.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch07/fig-expert-imbalance-as-a-training-problem}`
- `\input{tables/ch07/tab-expert-imbalance-as-a-training-problem}`
- `\input{equations/ch07/eq-expert-imbalance-as-a-training-problem}`
- `\input{listings/ch07/lst-expert-imbalance-as-a-training-problem}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
