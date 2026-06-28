# Section plan: Chapter 1.4 - What from scratch means for this book

## Local objective

Define the implementation boundary: small readable modules, explicit tensors, and diagnostics before optimization.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Contrast a one-line library MoE call with a transparent router, dispatch, expert, and combine pipeline.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch01/fig-what-from-scratch-means-for-this-book}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch01/eq-what-from-scratch-means-for-this-book}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch01/lst-what-from-scratch-means-for-this-book}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: With the boundary defined, we can plan the exact model we will build.

## Planned artifacts

- `latex_book_skeleton/figures/ch01/fig-what-from-scratch-means-for-this-book.tex` - TikZ. Shows: Layered build approach from scalar example to vectorized PyTorch to training script.. Caption placeholder included. Label: `fig:ch01-what-from-scratch-means-for-this-book`.
- `latex_book_skeleton/tables/ch01/tab-what-from-scratch-means-for-this-book.tex` - Table. Defines: Included and excluded scope for the book, including distributed training and production kernels.. Caption placeholder included. Label: `tab:ch01-what-from-scratch-means-for-this-book`.
- `latex_book_skeleton/listings/ch01/lst-what-from-scratch-means-for-this-book.tex` - Python listing. Implements or sketches: Skeleton class layout for Router, ExpertMLP, MoELayer, and MiniDeepSeekMoE.. Caption placeholder included. Label: `lst:ch01-what-from-scratch-means-for-this-book`.
- `latex_book_skeleton/equations/ch01/eq-what-from-scratch-means-for-this-book.tex` - Equation. States: Interface invariant: MoE layer maps (B,T,D) to (B,T,D).. Label: `eq:ch01-what-from-scratch-means-for-this-book`.

## Code deliverable

Develop the code in `ch01/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Checklist that every chapter must include shapes, a code path, and a verification artifact.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
