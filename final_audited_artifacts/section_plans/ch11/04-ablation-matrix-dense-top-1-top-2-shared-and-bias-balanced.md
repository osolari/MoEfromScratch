# Section plan: Chapter 11.4 - Ablation matrix: dense, top-1, top-2, shared, and bias-balanced

## Local objective

Plan the central comparison table for the book without pretending small runs settle model quality.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Run five variants for the same token budget and record comparable metrics.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch11/fig-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch11/eq-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch11/lst-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Expert behavior should be interpreted with both numbers and examples.

## Planned artifacts

- `latex_book_skeleton/figures/ch11/fig-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.tex` - TikZ. Shows: Ablation matrix with one row per model variant and columns for routing features.. Caption placeholder included. Label: `fig:ch11-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced`.
- `latex_book_skeleton/tables/ch11/tab-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.tex` - Table. Defines: Dense baseline versus MoE variants: parameters, active parameters, loss, load, entropy, drop rate.. Caption placeholder included. Label: `tab:ch11-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced`.
- `latex_book_skeleton/listings/ch11/lst-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.tex` - Python listing. Implements or sketches: run_ablation_matrix.py that launches or documents variant commands.. Caption placeholder included. Label: `lst:ch11-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced`.
- `latex_book_skeleton/equations/ch11/eq-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.tex` - Equation. States: Active parameter ratio for each sparse variant.. Label: `eq:ch11-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced`.

## Code deliverable

Develop the code in `ch11/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Flag any run with unstable loss, high drop rate, or extreme expert collapse.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
