# Section plan: Chapter 9.4 - Dynamic bias update from expert load

## Local objective

Add a simple no-gradient update that nudges underused experts up and overused experts down.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Compare observed loads [8,2,1,1] to target load 3 and update each bias.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch09/fig-dynamic-bias-update-from-expert-load}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch09/eq-dynamic-bias-update-from-expert-load}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch09/lst-dynamic-bias-update-from-expert-load}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Now we can compare auxiliary balancing and bias balancing using the same model and metrics.

## Planned artifacts

- `latex_book_skeleton/figures/ch09/fig-dynamic-bias-update-from-expert-load.tex` - TikZ. Shows: Feedback loop from observed expert histogram to router bias update.. Caption placeholder included. Label: `fig:ch09-dynamic-bias-update-from-expert-load`.
- `latex_book_skeleton/tables/ch09/tab-dynamic-bias-update-from-expert-load.tex` - Table. Defines: Bias update hyperparameters: gamma, target load, update interval, clamp range.. Caption placeholder included. Label: `tab:ch09-dynamic-bias-update-from-expert-load`.
- `latex_book_skeleton/listings/ch09/lst-dynamic-bias-update-from-expert-load.tex` - Python listing. Implements or sketches: update_router_bias(load, target, gamma) implemented under torch.no_grad().. Caption placeholder included. Label: `lst:ch09-dynamic-bias-update-from-expert-load`.
- `latex_book_skeleton/equations/ch09/eq-dynamic-bias-update-from-expert-load.tex` - Equation. States: b_i <- b_i + gamma if load_i < target, otherwise b_i <- b_i - gamma.. Label: `eq:ch09-dynamic-bias-update-from-expert-load`.

## Code deliverable

Develop the code in `ch09/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Track bias values over training beside expert loads.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
