# Phase 2 report - book layout, language, and visual style extraction

## Scope

Phase 2 extracts the compiled book's structural and stylistic patterns so the new book can be developed natively in LaTeX. The extracted style is a production guide, not a reuse of the source prose.

## Core finding

The source book is organized as a progressive build. Chapters are not isolated tutorials; each chapter starts from a bottleneck left by the previous chapter, introduces a mechanism with diagrams, grounds it with tensor shapes or math, implements it from scratch, verifies behavior, and then bridges to the next mechanism.

## Layout pattern to reuse

1. Numbered chapter title.
2. `This chapter covers` box with three bullets.
3. Prior-chapter bridge and current bottleneck.
4. Roadmap/context figure.
5. Intuition and conceptual contrast.
6. Visual walkthrough.
7. Mathematical/tensor-shape walkthrough.
8. From-scratch code listing.
9. Diagnostic comparison, table, plot, or toy run.
10. Summary and bridge.

## Visual theme to reuse in LaTeX

- Headings and caption accents use deep navy/blue from the EPUB CSS.
- Code uses a light gray background and a dark navy listing header.
- Callouts use a gray background with bold uppercase headings.
- Figures are schematic, high-contrast, and pedagogical: blocks, arrows, matrices/dots, and color-coded paths.
- Tables are simple comparison tools; in LaTeX they should use `booktabs` but preserve gray header semantics when useful.

## Artifact density extracted

| Artifact type | Count |
| --- | --- |
| figures | 190 |
| listings/code blocks | 63 |
| tables | 9 |
| callouts | 14 |
| equation blocks | 68 |
| images in EPUB | 225 |

## Chapter metric table

| Ch. | Title | H2 | H3 | Figures | Code/listings | Tables | Callouts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Introduction to DeepSeek | 6 | 3 | 9 | 0 | 0 | 0 |
| 2 | Solving the inference bottleneck with the key-value cache | 9 | 21 | 25 | 5 | 0 | 3 |
| 3 | The DeepSeek breakthrough: Multi-Head Latent Attention (MLA) | 18 | 24 | 37 | 7 | 2 | 1 |
| 4 | Mixture-of-Experts (MoE) in DeepSeek: Scaling intelligence efficiently | 7 | 15 | 30 | 6 | 1 | 1 |
| 5 | Multi-token prediction and FP8 quantization | 6 | 17 | 31 | 6 | 0 | 1 |
| 6 | The DeepSeek training pipeline: Building a foundation model | 6 | 23 | 12 | 30 | 0 | 0 |
| 7 | Reinforcement learning: From policy gradients to GRPO | 16 | 28 | 15 | 5 | 4 | 0 |
| 8 | Knowledge distillation: Making powerful models practical | 9 | 28 | 31 | 4 | 2 | 8 |

## LaTeX-first decisions for the MoE book

- Every chapter will be developed as `chapters/chNN/chapter.tex` plus section files under `chapters/chNN/sections/`.
- Every planned figure/table/listing will be a standalone `.tex` wrapper and included with `\input`.
- TikZ will be the default for schematics.
- External images or generated plots will be included only through wrapper `.tex` files containing `\includegraphics`, caption, and label.
- The global color map lives in `styles/colors.tex`; this Phase 2 seed stores TikZ styles and artifact macros in `styles/theme_macros.tex` (these may be split into `macros.tex` and `tikzstyles.tex` in the final book template).

## Deliverables in this package

```text
moe_from_scratch_phase2/
├── PHASE_2_REPORT.md
├── style_extraction/
│   ├── book_flow_and_language.md
│   ├── chapter_layout_matrix.md
│   ├── latex_artifact_contract.md
│   ├── section_development_framework.md
│   ├── source_inventory.md
│   └── visual_design_system.md
├── data/
│   ├── callout_inventory.csv
│   ├── chapter_metrics.csv
│   ├── chapter_outline.json
│   ├── figure_inventory.csv
│   ├── image_dimensions.csv
│   ├── listing_inventory.csv
│   └── table_inventory.csv
└── latex_theme_contract/
    ├── main.tex
    ├── phase2_theme_preview.pdf
    ├── styles/colors.tex
    ├── styles/theme_macros.tex
    ├── figures/fig-router-token-flow.tex
    ├── tables/tab-artifact-roles.tex
    └── listings/lst-router-pseudocode.tex
```

## Phase 2 conclusion

The new *MoE Models from Scratch* book should be a LaTeX-native, figure-heavy, code-driven build. The style should preserve the source book's strongest teaching pattern: motivate every component as a response to a concrete bottleneck, show it schematically, implement it in small PyTorch steps, and verify it with diagnostics.
