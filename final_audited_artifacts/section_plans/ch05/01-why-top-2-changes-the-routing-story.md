# Section plan: Chapter 5.1 - Why top-2 changes the routing story

## Local objective

Explain top-2 routing as sparse ensemble behavior at the token level.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use four tokens and four experts; each token chooses two experts with different weights.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch05/fig-why-top-2-changes-the-routing-story}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch05/eq-why-top-2-changes-the-routing-story}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch05/lst-why-top-2-changes-the-routing-story}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: To make top-2 work, selected scores must become stable combine weights.

## Planned artifacts

- `latex_book_skeleton/figures/ch05/fig-why-top-2-changes-the-routing-story.tex` - TikZ. Shows: Token routes split into two weighted paths.. Caption placeholder included. Label: `fig:ch05-why-top-2-changes-the-routing-story`.
- `latex_book_skeleton/tables/ch05/tab-why-top-2-changes-the-routing-story.tex` - Table. Defines: Top-1 versus top-2 routing behavior, cost, and diagnostics.. Caption placeholder included. Label: `tab:ch05-why-top-2-changes-the-routing-story`.
- `latex_book_skeleton/listings/ch05/lst-why-top-2-changes-the-routing-story.tex` - Python listing. Implements or sketches: Config switch from K=1 to K=2 and resulting tensor shapes.. Caption placeholder included. Label: `lst:ch05-why-top-2-changes-the-routing-story`.
- `latex_book_skeleton/equations/ch05/eq-why-top-2-changes-the-routing-story.tex` - Equation. States: Each selected set S_t contains K=2 expert IDs.. Label: `eq:ch05-why-top-2-changes-the-routing-story`.

## Code deliverable

Develop the code in `ch05/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Compare active expert calls per token for K=1 and K=2.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
