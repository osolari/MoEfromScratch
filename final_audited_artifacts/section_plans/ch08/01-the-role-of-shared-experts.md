# Section plan: Chapter 8.1 - The role of shared experts

## Local objective

Explain the always-on expert path as a way to separate common processing from routed specialization.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Every token goes through one shared expert while also routing to two routed experts.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch08/fig-the-role-of-shared-experts}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch08/eq-the-role-of-shared-experts}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch08/lst-the-role-of-shared-experts}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Routed experts can also be made finer-grained to increase specialization options.

## Planned artifacts

- `latex_book_skeleton/figures/ch08/fig-the-role-of-shared-experts.tex` - TikZ. Shows: Parallel shared path and routed path merging at the MoE output.. Caption placeholder included. Label: `fig:ch08-the-role-of-shared-experts`.
- `latex_book_skeleton/tables/ch08/tab-the-role-of-shared-experts.tex` - Table. Defines: Shared expert path versus routed expert path responsibilities.. Caption placeholder included. Label: `tab:ch08-the-role-of-shared-experts`.
- `latex_book_skeleton/listings/ch08/lst-the-role-of-shared-experts.tex` - Python listing. Implements or sketches: SharedExpertMLP module and shared_out calculation.. Caption placeholder included. Label: `lst:ch08-the-role-of-shared-experts`.
- `latex_book_skeleton/equations/ch08/eq-the-role-of-shared-experts.tex` - Equation. States: shared_out = sum_s shared_expert_s(x).. Label: `eq:ch08-the-role-of-shared-experts`.

## Code deliverable

Develop the code in `ch08/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Verify shared experts receive gradients for every token, not only selected tokens.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
