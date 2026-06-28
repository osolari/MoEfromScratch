# Section plan: Chapter 1.3 - A tiny routing story

## Local objective

Give readers a concrete token-by-token routing example before any model code appears.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use tokens [cat, sat, code, runs], four experts, and top-2 routing weights.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch01/fig-a-tiny-routing-story}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch01/eq-a-tiny-routing-story}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch01/lst-a-tiny-routing-story}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: This toy flow becomes the shape contract for every later implementation.

## Planned artifacts

- `latex_book_skeleton/figures/ch01/fig-a-tiny-routing-story.tex` - TikZ. Shows: A storyboard of router scores, selected experts, expert outputs, and weighted combine.. Caption placeholder included. Label: `fig:ch01-a-tiny-routing-story`.
- `latex_book_skeleton/tables/ch01/tab-a-tiny-routing-story.tex` - Table. Defines: Toy router-score matrix with top-2 expert choices and normalized gates.. Caption placeholder included. Label: `tab:ch01-a-tiny-routing-story`.
- `latex_book_skeleton/listings/ch01/lst-a-tiny-routing-story.tex` - Python listing. Implements or sketches: Manual PyTorch tensor example that applies torch.topk and normalized weights.. Caption placeholder included. Label: `lst:ch01-a-tiny-routing-story`.
- `latex_book_skeleton/equations/ch01/eq-a-tiny-routing-story.tex` - Equation. States: Weighted expert output y_t = sum gate_i expert_i(x_t).. Label: `eq:ch01-a-tiny-routing-story`.

## Code deliverable

Develop the code in `ch01/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Check that gates for each token sum to one after top-k normalization.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
