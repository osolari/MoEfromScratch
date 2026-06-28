# Section plan: Chapter 9.2 - Router bias as non-trainable state

## Local objective

Define router bias as a per-expert control signal updated outside backpropagation.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use four experts with bias values that rise for underused experts and fall for overused experts.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch09/fig-router-bias-as-non-trainable-state}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch09/eq-router-bias-as-non-trainable-state}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch09/lst-router-bias-as-non-trainable-state}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The key implementation detail is that bias changes selection but not final gates.

## Planned artifacts

- `latex_book_skeleton/figures/ch09/fig-router-bias-as-non-trainable-state.tex` - TikZ. Shows: Bias vector nudging the score table before top-k selection.. Caption placeholder included. Label: `fig:ch09-router-bias-as-non-trainable-state`.
- `latex_book_skeleton/tables/ch09/tab-router-bias-as-non-trainable-state.tex` - Table. Defines: Router bias properties: shape, initialization, update timing, gradient status, checkpoint behavior.. Caption placeholder included. Label: `tab:ch09-router-bias-as-non-trainable-state`.
- `latex_book_skeleton/listings/ch09/lst-router-bias-as-non-trainable-state.tex` - Python listing. Implements or sketches: Register router_bias as a buffer and exclude it from optimizer gradients.. Caption placeholder included. Label: `lst:ch09-router-bias-as-non-trainable-state`.
- `latex_book_skeleton/equations/ch09/eq-router-bias-as-non-trainable-state.tex` - Equation. States: selection_score = score + router_bias.. Label: `eq:ch09-router-bias-as-non-trainable-state`.

## Code deliverable

Develop the code in `ch09/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Assert router_bias.requires_grad is false and optimizer does not update it.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
