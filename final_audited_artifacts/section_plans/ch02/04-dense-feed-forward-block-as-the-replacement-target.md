# Section plan: Chapter 2.4 - Dense feed-forward block as the replacement target

## Local objective

Implement the dense FFN in a way that makes the later expert replacement obvious.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Apply the same MLP to every token in a B*T flattened view.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch02/fig-dense-feed-forward-block-as-the-replacement-target}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch02/eq-dense-feed-forward-block-as-the-replacement-target}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch02/lst-dense-feed-forward-block-as-the-replacement-target}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Attention and FFN combine inside a residual decoder block.

## Planned artifacts

- `latex_book_skeleton/figures/ch02/fig-dense-feed-forward-block-as-the-replacement-target.tex` - TikZ. Shows: Dense FFN applied independently to each token row.. Caption placeholder included. Label: `fig:ch02-dense-feed-forward-block-as-the-replacement-target`.
- `latex_book_skeleton/tables/ch02/tab-dense-feed-forward-block-as-the-replacement-target.tex` - Table. Defines: Dense FFN parameters compared with one future expert MLP.. Caption placeholder included. Label: `tab:ch02-dense-feed-forward-block-as-the-replacement-target`.
- `latex_book_skeleton/listings/ch02/lst-dense-feed-forward-block-as-the-replacement-target.tex` - Python listing. Implements or sketches: FeedForward module with Linear, activation, Linear.. Caption placeholder included. Label: `lst:ch02-dense-feed-forward-block-as-the-replacement-target`.
- `latex_book_skeleton/equations/ch02/eq-dense-feed-forward-block-as-the-replacement-target.tex` - Equation. States: FFN(x) = W_2 activation(W_1 x + b_1) + b_2.. Label: `eq:ch02-dense-feed-forward-block-as-the-replacement-target`.

## Code deliverable

Develop the code in `ch02/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Confirm FFN preserves the final D dimension.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
