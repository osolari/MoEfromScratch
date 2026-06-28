# Section plan: Chapter 6.2 - Expert batch construction

## Local objective

Build dense per-expert mini-batches from sparse token assignments.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Create an expert batch tensor with shape (E, capacity, D).

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch06/fig-expert-batch-construction}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch06/eq-expert-batch-construction}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch06/lst-expert-batch-construction}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Fixed-size expert batches require a capacity rule.

## Planned artifacts

- `latex_book_skeleton/figures/ch06/fig-expert-batch-construction.tex` - TikZ. Shows: Sparse token assignments packed into a fixed-size expert batch grid.. Caption placeholder included. Label: `fig:ch06-expert-batch-construction`.
- `latex_book_skeleton/tables/ch06/tab-expert-batch-construction.tex` - Table. Defines: expert_batch, combine_weights, token_indices, and slot_indices shapes.. Caption placeholder included. Label: `tab:ch06-expert-batch-construction`.
- `latex_book_skeleton/listings/ch06/lst-expert-batch-construction.tex` - Python listing. Implements or sketches: pack_tokens_by_expert function for top-k assignments.. Caption placeholder included. Label: `lst:ch06-expert-batch-construction`.
- `latex_book_skeleton/equations/ch06/eq-expert-batch-construction.tex` - Equation. States: expert_batch[i, slot, :] = x_flat[token_idx].. Label: `eq:ch06-expert-batch-construction`.

## Code deliverable

Develop the code in `ch06/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Ensure each accepted route has exactly one expert slot.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
