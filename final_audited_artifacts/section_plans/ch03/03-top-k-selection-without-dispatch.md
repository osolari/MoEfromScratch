# Section plan: Chapter 3.3 - Top-k selection without dispatch

## Local objective

Separate the selection problem from expert execution so readers can inspect router behavior first.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Compute top-2 expert IDs and scores for a four-token, four-expert score table.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch03/fig-top-k-selection-without-dispatch}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch03/eq-top-k-selection-without-dispatch}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch03/lst-top-k-selection-without-dispatch}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Selection tells us where tokens should go; dispatch actually sends them there.

## Planned artifacts

- `latex_book_skeleton/figures/ch03/fig-top-k-selection-without-dispatch.tex` - TikZ. Shows: Score matrix with the top-k entries highlighted in each row.. Caption placeholder included. Label: `fig:ch03-top-k-selection-without-dispatch`.
- `latex_book_skeleton/tables/ch03/tab-top-k-selection-without-dispatch.tex` - Table. Defines: Manual top-k results for the toy score table.. Caption placeholder included. Label: `tab:ch03-top-k-selection-without-dispatch`.
- `latex_book_skeleton/listings/ch03/lst-top-k-selection-without-dispatch.tex` - Python listing. Implements or sketches: torch.topk example that returns topk_score and topk_idx.. Caption placeholder included. Label: `lst:ch03-top-k-selection-without-dispatch`.
- `latex_book_skeleton/equations/ch03/eq-top-k-selection-without-dispatch.tex` - Equation. States: S_t = topk(score_t, K), one selected set per token.. Label: `eq:ch03-top-k-selection-without-dispatch`.

## Code deliverable

Develop the code in `ch03/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Verify that every token has exactly K selected expert IDs.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
