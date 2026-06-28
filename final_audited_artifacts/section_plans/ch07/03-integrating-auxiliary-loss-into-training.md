# Section plan: Chapter 7.3 - Integrating auxiliary loss into training

## Local objective

Add routing losses to the model output dictionary without hiding the main language-model loss.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Return lm_loss, aux_loss, total_loss, and router_metrics from one forward pass.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch07/fig-integrating-auxiliary-loss-into-training}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch07/eq-integrating-auxiliary-loss-into-training}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch07/lst-integrating-auxiliary-loss-into-training}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Load balancing is one router signal; score scale can also create instability.

## Planned artifacts

- `latex_book_skeleton/figures/ch07/fig-integrating-auxiliary-loss-into-training.tex` - TikZ. Shows: Loss composition diagram from logits and router statistics to total loss.. Caption placeholder included. Label: `fig:ch07-integrating-auxiliary-loss-into-training`.
- `latex_book_skeleton/tables/ch07/tab-integrating-auxiliary-loss-into-training.tex` - Table. Defines: Loss terms, coefficients, default values, and logging names.. Caption placeholder included. Label: `tab:ch07-integrating-auxiliary-loss-into-training`.
- `latex_book_skeleton/listings/ch07/lst-integrating-auxiliary-loss-into-training.tex` - Python listing. Implements or sketches: Training step that combines lm_loss + aux_coef * aux_loss.. Caption placeholder included. Label: `lst:ch07-integrating-auxiliary-loss-into-training`.
- `latex_book_skeleton/equations/ch07/eq-integrating-auxiliary-loss-into-training.tex` - Equation. States: total_loss = lm_loss + lambda_aux * aux_loss.. Label: `eq:ch07-integrating-auxiliary-loss-into-training`.

## Code deliverable

Develop the code in `ch07/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Log individual losses separately so balancing cannot hide LM degradation.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
