# Visual design system for the LaTeX book

This file converts the EPUB/CSS extraction into a reproducible LaTeX visual contract for *MoE Models from Scratch*.

## Color map

### CSS-derived book palette

| LaTeX color | Hex | Use |
| --- | --- | --- |
| BookNavy | #000055 | main headings and callout titles |
| BookDeepBlue | #141464 | secondary headings, figure/table caption labels, links |
| BookListingHeader | #020056 | code listing title bar |
| BookCalloutGray | #E6E6E6 | definition/note background |
| BookCodeBg | #F2F2F2 | code block background and table header gray |
| BookTextBlack | #000000 | body text, diagram arrows, outlines |
| BookPaperWhite | #FFFFFF | page and diagram panel background |

### MoE semantic diagram palette

| LaTeX color | Hex | Use |
| --- | --- | --- |
| MoETokenPurple | #C060E0 | input token embeddings and token rows |
| MoERouterCyan | #00A7C1 | router path, selected-token branch, dispatch lines |
| MoEActiveGreen | #70D050 | active expert neurons or selected capacity |
| MoEOutputRed | #F05050 | expert outputs or final aggregated tensors |
| MoEExpertPurple | #9050FF | expert blocks and expert identity |
| MoECapacityGold | #FFD080 | capacity, top-k weights, roadmap stage bands |
| MoESharedGreen | #A8DDA8 | shared expert path and always-on expert |
| MoEImbalanceRed | #E03030 | overloaded experts, imbalance warnings |
| MoEMutedGray | #D0D0D0 | inactive experts, background grid, faint references |
| MoESoftFill | #F0F0FF | neutral model blocks |

The semantic palette extends the source book's schematic style. It should remain stable across all chapters so the reader learns visual meaning: purple means tokens/experts, cyan means routing, green means selected/active, red means outputs or imbalance, gold means capacity/weights.

## Figure style rules

- Default figure aspect ratio: 16:9 or near the source book's common `1042x581` canvas.
- Prefer a white diagram panel with black outlines and a small number of semantic accent colors.
- Use thick arrows and large labels. Diagrams should remain readable when printed at `0.9\textwidth`.
- Use rows of dots for tensors when exact values are not the point; use small matrices only when the numbers matter.
- Every chapter should include at least one context/roadmap diagram and several mechanism diagrams.
- Captions should explain the takeaway, not merely name the image.

## Table style rules

- The EPUB uses simple black-bordered tables with gray header cells.
- The LaTeX version should use `booktabs` for print-quality tables while preserving the gray-header semantics when useful.
- Use tables for comparisons, hyperparameter summaries, routing diagnostics, and chapter checklists.
- Keep wide implementation comparisons to 2-4 columns; split large comparison tables rather than shrinking text.

## Code listing style rules

- Code background: `BookCodeBg` (`#F2F2F2`).
- Listing title/header: `BookListingHeader` (`#020056`) with white text where a title bar is used.
- Monospace preference: JetBrains Mono if available; otherwise `Consolas`, `Liberation Mono`, or LaTeX default typewriter.
- Use numbered listings for durable code readers will refer back to.
- Use unnumbered shell blocks for setup commands and short terminal outputs.
- Dense listings should include callout comments or a follow-up explanation table, mirroring the source book's annotated-code style.

## Callout style rules

- Callouts use a light gray background and a bold uppercase head such as `Definition`, `Note`, `Warning`, `Checklist`, or `Sanity check`.
- Use callouts for vocabulary, implementation pitfalls, and reader checkpoints.
- Avoid turning ordinary paragraphs into callouts; reserve them for concepts the reader will need repeatedly.

## Reproducibility requirements

- All figures, tables, listings, and callouts that are substantial enough to reference must live in standalone `.tex` files.
- Chapters must include artifacts with `\input{...}`, not inline artifact bodies.
- TikZ diagrams must be saved as `.tex` wrapper files containing the full `figure` environment, caption, and label.
- External PDF graphics must be included only through a `.tex` wrapper containing `\includegraphics`, caption, and label.
