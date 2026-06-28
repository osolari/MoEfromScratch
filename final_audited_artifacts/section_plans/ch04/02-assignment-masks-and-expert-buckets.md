# Section plan: Chapter 4.2 - Assignment masks and expert buckets

## Local objective

Convert token expert IDs into per-expert token groups.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Bucket six token indices into four expert lists.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch04/fig-assignment-masks-and-expert-buckets}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch04/eq-assignment-masks-and-expert-buckets}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch04/lst-assignment-masks-and-expert-buckets}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Once tokens are bucketed, expert modules process only their assigned tokens.

## Planned artifacts

- `latex_book_skeleton/figures/ch04/fig-assignment-masks-and-expert-buckets.tex` - TikZ. Shows: Assignment mask as a sparse N by E matrix and as expert buckets.. Caption placeholder included. Label: `fig:ch04-assignment-masks-and-expert-buckets`.
- `latex_book_skeleton/tables/ch04/tab-assignment-masks-and-expert-buckets.tex` - Table. Defines: Mask representation versus bucket representation trade-offs.. Caption placeholder included. Label: `tab:ch04-assignment-masks-and-expert-buckets`.
- `latex_book_skeleton/listings/ch04/lst-assignment-masks-and-expert-buckets.tex` - Python listing. Implements or sketches: Build expert_to_token_indices from top-1 expert IDs.. Caption placeholder included. Label: `lst:ch04-assignment-masks-and-expert-buckets`.
- `latex_book_skeleton/equations/ch04/eq-assignment-masks-and-expert-buckets.tex` - Equation. States: mask_{t,i} = 1 when expert_idx_t = i.. Label: `eq:ch04-assignment-masks-and-expert-buckets`.

## Code deliverable

Develop the code in `ch04/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Sum the mask across experts to confirm each token is assigned once.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
