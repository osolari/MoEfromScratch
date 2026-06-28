# Section plan: Chapter 3.2 - Router scores and tensor shapes

## Local objective

Define router logits, router probabilities, and the flattening convention used throughout the book.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Flatten x from (B,T,D) to (N,D) and compute router_logits with E=4 experts.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch03/fig-router-scores-and-tensor-shapes}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch03/eq-router-scores-and-tensor-shapes}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch03/lst-router-scores-and-tensor-shapes}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Scores become sparse when we select only the top experts per token.

## Planned artifacts

- `latex_book_skeleton/figures/ch03/fig-router-scores-and-tensor-shapes.tex` - TikZ. Shows: Flattened token matrix multiplied by a router projection to produce an N by E score table.. Caption placeholder included. Label: `fig:ch03-router-scores-and-tensor-shapes`.
- `latex_book_skeleton/tables/ch03/tab-router-scores-and-tensor-shapes.tex` - Table. Defines: Router tensor shape contract for x, x_flat, logits, scores, topk_idx, and gates.. Caption placeholder included. Label: `tab:ch03-router-scores-and-tensor-shapes`.
- `latex_book_skeleton/listings/ch03/lst-router-scores-and-tensor-shapes.tex` - Python listing. Implements or sketches: Router module that returns logits and score tensors.. Caption placeholder included. Label: `lst:ch03-router-scores-and-tensor-shapes`.
- `latex_book_skeleton/equations/ch03/eq-router-scores-and-tensor-shapes.tex` - Equation. States: router_logits = x_flat W_r + b_r.. Label: `eq:ch03-router-scores-and-tensor-shapes`.

## Code deliverable

Develop the code in `ch03/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Assert that the expert dimension equals n_experts and token dimension equals B*T.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
