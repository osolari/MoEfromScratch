# Section plan: Chapter 10.3 - Forward pass outputs and loss dictionary

## Local objective

Return logits and structured losses/metrics without making training code guess where values live.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Forward pass returns logits, lm_loss, total_loss, router_metrics, and optional aux_loss.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch10/fig-forward-pass-outputs-and-loss-dictionary}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch10/eq-forward-pass-outputs-and-loss-dictionary}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch10/lst-forward-pass-outputs-and-loss-dictionary}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Training and sampling scripts can now be shared across variants.

## Planned artifacts

- `latex_book_skeleton/figures/ch10/fig-forward-pass-outputs-and-loss-dictionary.tex` - TikZ. Shows: Forward output dictionary with model outputs and nested per-layer router metrics.. Caption placeholder included. Label: `fig:ch10-forward-pass-outputs-and-loss-dictionary`.
- `latex_book_skeleton/tables/ch10/tab-forward-pass-outputs-and-loss-dictionary.tex` - Table. Defines: Output dictionary keys, shapes, and when they are present.. Caption placeholder included. Label: `tab:ch10-forward-pass-outputs-and-loss-dictionary`.
- `latex_book_skeleton/listings/ch10/lst-forward-pass-outputs-and-loss-dictionary.tex` - Python listing. Implements or sketches: MiniDeepSeekMoE.forward implementation with metric aggregation.. Caption placeholder included. Label: `lst:ch10-forward-pass-outputs-and-loss-dictionary`.
- `latex_book_skeleton/equations/ch10/eq-forward-pass-outputs-and-loss-dictionary.tex` - Equation. States: total_loss depends on selected balancing mode.. Label: `eq:ch10-forward-pass-outputs-and-loss-dictionary`.

## Code deliverable

Develop the code in `ch10/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Unit test for output keys under dense, auxiliary, and bias modes.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
