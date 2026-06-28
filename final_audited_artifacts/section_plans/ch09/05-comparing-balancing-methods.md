# Section plan: Chapter 9.5 - Comparing balancing methods

## Local objective

Design a fair chapter experiment comparing no balance, auxiliary loss, and router-bias balancing.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Run three short smoke experiments with identical seeds and report the same diagnostics.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch09/fig-comparing-balancing-methods}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch09/eq-comparing-balancing-methods}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch09/lst-comparing-balancing-methods}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The next chapter assembles the full MiniDeepSeekMoE model around this final layer.

## Planned artifacts

- `latex_book_skeleton/figures/ch09/fig-comparing-balancing-methods.tex` - TikZ. Shows: Three-panel comparison of expert load histograms and validation loss curves.. Caption placeholder included. Label: `fig:ch09-comparing-balancing-methods`.
- `latex_book_skeleton/tables/ch09/tab-comparing-balancing-methods.tex` - Table. Defines: Experiment matrix with balancing method, objective terms, update rule, and expected diagnostics.. Caption placeholder included. Label: `tab:ch09-comparing-balancing-methods`.
- `latex_book_skeleton/listings/ch09/lst-comparing-balancing-methods.tex` - Python listing. Implements or sketches: run_balancing_ablation.py command presets.. Caption placeholder included. Label: `lst:ch09-comparing-balancing-methods`.
- `latex_book_skeleton/equations/ch09/eq-comparing-balancing-methods.tex` - Equation. States: Balance score based on max_load/mean_load or coefficient of variation.. Label: `eq:ch09-comparing-balancing-methods`.

## Code deliverable

Develop the code in `ch09/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Produce a table with LM loss, aux loss if used, load balance score, entropy, and drop rate.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
