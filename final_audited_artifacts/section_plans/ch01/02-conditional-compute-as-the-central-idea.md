# Section plan: Chapter 1.2 - Conditional compute as the central idea

## Local objective

Introduce MoE as selective FFN computation rather than a mysterious new model family.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Route four tokens to two of four available experts and compare activated parameters against total parameters.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch01/fig-conditional-compute-as-the-central-idea}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch01/eq-conditional-compute-as-the-central-idea}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch01/lst-conditional-compute-as-the-central-idea}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Selective compute creates a new component: the router, which needs its own tensor contract.

## Planned artifacts

- `latex_book_skeleton/figures/ch01/fig-conditional-compute-as-the-central-idea.tex` - TikZ. Shows: Tokens split through a router into a sparse subset of experts, then recombine.. Caption placeholder included. Label: `fig:ch01-conditional-compute-as-the-central-idea`.
- `latex_book_skeleton/tables/ch01/tab-conditional-compute-as-the-central-idea.tex` - Table. Defines: Dense versus conditional-compute vocabulary: FFN, expert, router, active parameters, total parameters.. Caption placeholder included. Label: `tab:ch01-conditional-compute-as-the-central-idea`.
- `latex_book_skeleton/listings/ch01/lst-conditional-compute-as-the-central-idea.tex` - Python listing. Implements or sketches: Pseudocode that chooses expert IDs for tokens and reports active expert count.. Caption placeholder included. Label: `lst:ch01-conditional-compute-as-the-central-idea`.
- `latex_book_skeleton/equations/ch01/eq-conditional-compute-as-the-central-idea.tex` - Equation. States: Activated-parameter view: total expert bank versus top-k expert use per token.. Label: `eq:ch01-conditional-compute-as-the-central-idea`.

## Code deliverable

Develop the code in `ch01/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Compute the active fraction for E=4, K=2 and E=16, K=2.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
