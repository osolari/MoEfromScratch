# Section plan: Chapter 3.1 - Expert MLPs as named FFNs

## Local objective

Demystify experts by deriving them directly from the dense FFN module.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Clone the dense FFN four times and label the copies expert 0 through expert 3.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch03/fig-expert-mlps-as-named-ffns}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch03/eq-expert-mlps-as-named-ffns}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch03/lst-expert-mlps-as-named-ffns}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Experts need a token-dependent selection mechanism: the router.

## Planned artifacts

- `latex_book_skeleton/figures/ch03/fig-expert-mlps-as-named-ffns.tex` - TikZ. Shows: One dense FFN replaced by a bank of same-shape expert MLPs.. Caption placeholder included. Label: `fig:ch03-expert-mlps-as-named-ffns`.
- `latex_book_skeleton/tables/ch03/tab-expert-mlps-as-named-ffns.tex` - Table. Defines: Dense FFN versus expert bank parameters, active parameters, and outputs.. Caption placeholder included. Label: `tab:ch03-expert-mlps-as-named-ffns`.
- `latex_book_skeleton/listings/ch03/lst-expert-mlps-as-named-ffns.tex` - Python listing. Implements or sketches: ExpertMLP class with the same input-output contract as the dense FFN.. Caption placeholder included. Label: `lst:ch03-expert-mlps-as-named-ffns`.
- `latex_book_skeleton/equations/ch03/eq-expert-mlps-as-named-ffns.tex` - Equation. States: expert_i(x) maps R^D to R^D for every expert i.. Label: `eq:ch03-expert-mlps-as-named-ffns`.

## Code deliverable

Develop the code in `ch03/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Run all experts on the same token and compare output shapes.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
