# Section plan: Chapter 4.5 - Load histograms and failure modes

## Local objective

Make expert collapse and underuse visible with simple diagnostics.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Create a synthetic router that sends most tokens to one expert and plot the load.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch04/fig-load-histograms-and-failure-modes}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch04/eq-load-histograms-and-failure-modes}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch04/lst-load-histograms-and-failure-modes}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Top-1 is simple but brittle; top-2 routing gives each token a backup path and a weighted combine.

## Planned artifacts

- `latex_book_skeleton/figures/ch04/fig-load-histograms-and-failure-modes.tex` - TikZ. Shows: Expert-load histogram with one overloaded expert highlighted in imbalance red.. Caption placeholder included. Label: `fig:ch04-load-histograms-and-failure-modes`.
- `latex_book_skeleton/tables/ch04/tab-load-histograms-and-failure-modes.tex` - Table. Defines: Failure modes: expert collapse, empty experts, high drop rate, low entropy.. Caption placeholder included. Label: `tab:ch04-load-histograms-and-failure-modes`.
- `latex_book_skeleton/listings/ch04/lst-load-histograms-and-failure-modes.tex` - Python listing. Implements or sketches: Function that computes expert_load, load_fraction, and routing_entropy.. Caption placeholder included. Label: `lst:ch04-load-histograms-and-failure-modes`.
- `latex_book_skeleton/equations/ch04/eq-load-histograms-and-failure-modes.tex` - Equation. States: load_fraction_i = count_i / N.. Label: `eq:ch04-load-histograms-and-failure-modes`.

## Code deliverable

Develop the code in `ch04/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Save a histogram and a warning if max load is much larger than average load.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
