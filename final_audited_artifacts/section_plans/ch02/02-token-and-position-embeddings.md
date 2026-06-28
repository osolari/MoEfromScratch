# Section plan: Chapter 2.2 - Token and position embeddings

## Local objective

Implement the entry point that maps integer token IDs to dense vectors.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use vocab_size=32, block_size=8, and d_model=16 to inspect embedding shapes.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch02/fig-token-and-position-embeddings}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch02/eq-token-and-position-embeddings}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch02/lst-token-and-position-embeddings}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The embedded sequence now enters causal self-attention.

## Planned artifacts

- `latex_book_skeleton/figures/ch02/fig-token-and-position-embeddings.tex` - TikZ. Shows: Token IDs and position IDs summed into the model input tensor.. Caption placeholder included. Label: `fig:ch02-token-and-position-embeddings`.
- `latex_book_skeleton/tables/ch02/tab-token-and-position-embeddings.tex` - Table. Defines: Embedding parameter counts and output shapes.. Caption placeholder included. Label: `tab:ch02-token-and-position-embeddings`.
- `latex_book_skeleton/listings/ch02/lst-token-and-position-embeddings.tex` - Python listing. Implements or sketches: Embedding module forward pass returning x with shape (B,T,D).. Caption placeholder included. Label: `lst:ch02-token-and-position-embeddings`.
- `latex_book_skeleton/equations/ch02/eq-token-and-position-embeddings.tex` - Equation. States: x = token_embedding(idx) + position_embedding(pos).. Label: `eq:ch02-token-and-position-embeddings`.

## Code deliverable

Develop the code in `ch02/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Assert output shape and confirm gradients flow to both embedding tables.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
