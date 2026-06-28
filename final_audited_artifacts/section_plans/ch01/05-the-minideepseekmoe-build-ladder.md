# Section plan: Chapter 1.5 - The MiniDeepSeekMoE build ladder

## Local objective

Preview the book path from dense baseline to shared experts, fine-grained experts, and router-bias balancing.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use the smoke-test configuration with two layers, four routed experts, and one shared expert.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch01/fig-the-minideepseekmoe-build-ladder}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch01/eq-the-minideepseekmoe-build-ladder}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch01/lst-the-minideepseekmoe-build-ladder}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The first build step is a dense Transformer baseline that gives the MoE layer somewhere to live.

## Planned artifacts

- `latex_book_skeleton/figures/ch01/fig-the-minideepseekmoe-build-ladder.tex` - TikZ. Shows: Roadmap ladder: dense baseline, top-1, top-2, capacity, auxiliary loss, shared experts, bias balancing, full model.. Caption placeholder included. Label: `fig:ch01-the-minideepseekmoe-build-ladder`.
- `latex_book_skeleton/tables/ch01/tab-the-minideepseekmoe-build-ladder.tex` - Table. Defines: Chapter-by-chapter implementation milestones and expected code outputs.. Caption placeholder included. Label: `tab:ch01-the-minideepseekmoe-build-ladder`.
- `latex_book_skeleton/listings/ch01/lst-the-minideepseekmoe-build-ladder.tex` - Python listing. Implements or sketches: Configuration dictionary for MiniDeepSeekMoE-Smoke and MiniDeepSeekMoE-16x2.. Caption placeholder included. Label: `lst:ch01-the-minideepseekmoe-build-ladder`.
- `latex_book_skeleton/equations/ch01/eq-the-minideepseekmoe-build-ladder.tex` - Equation. States: Final layer formula combining residual, shared expert output, and routed expert output.. Label: `eq:ch01-the-minideepseekmoe-build-ladder`.

## Code deliverable

Develop the code in `ch01/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Milestone checklist that marks which diagnostics appear by each chapter.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
