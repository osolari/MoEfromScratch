# Section plan: Chapter 2.1 - Dataset and token batches

## Local objective

Create the small next-token prediction pipeline used for every model variant.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Load a short text corpus, tokenize it, and create B=2, T=8 training examples.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch02/fig-dataset-and-token-batches}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch02/eq-dataset-and-token-batches}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch02/lst-dataset-and-token-batches}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Token IDs become vectors through embeddings and positions.

## Planned artifacts

- `latex_book_skeleton/figures/ch02/fig-dataset-and-token-batches.tex` - TikZ. Shows: Text to token IDs to input-target shifted batches.. Caption placeholder included. Label: `fig:ch02-dataset-and-token-batches`.
- `latex_book_skeleton/tables/ch02/tab-dataset-and-token-batches.tex` - Table. Defines: Batch tensor shapes and dataloader responsibilities.. Caption placeholder included. Label: `tab:ch02-dataset-and-token-batches`.
- `latex_book_skeleton/listings/ch02/lst-dataset-and-token-batches.tex` - Python listing. Implements or sketches: Minimal get_batch function with input and target shifts.. Caption placeholder included. Label: `lst:ch02-dataset-and-token-batches`.
- `latex_book_skeleton/equations/ch02/eq-dataset-and-token-batches.tex` - Equation. States: Next-token objective index relation target[t] = input[t+1].. Label: `eq:ch02-dataset-and-token-batches`.

## Code deliverable

Develop the code in `ch02/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Print the first input-target pair and decode it to verify shifting.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
