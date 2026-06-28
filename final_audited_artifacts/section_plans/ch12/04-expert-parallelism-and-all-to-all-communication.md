# Section plan: Chapter 12.4 - Expert parallelism and all-to-all communication

## Local objective

Explain the systems picture conceptually while keeping implementation out of scope.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Two devices each host two experts; tokens must move to the device containing their selected experts.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch12/fig-expert-parallelism-and-all-to-all-communication}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch12/eq-expert-parallelism-and-all-to-all-communication}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch12/lst-expert-parallelism-and-all-to-all-communication}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: This systems view helps map the toy model to public large-MoE architecture descriptions.

## Planned artifacts

- `latex_book_skeleton/figures/ch12/fig-expert-parallelism-and-all-to-all-communication.tex` - TikZ. Shows: Tokens routed across devices through an all-to-all exchange, expert compute, and return exchange.. Caption placeholder included. Label: `fig:ch12-expert-parallelism-and-all-to-all-communication`.
- `latex_book_skeleton/tables/ch12/tab-expert-parallelism-and-all-to-all-communication.tex` - Table. Defines: Single-device MoE versus expert-parallel MoE responsibilities.. Caption placeholder included. Label: `tab:ch12-expert-parallelism-and-all-to-all-communication`.
- `latex_book_skeleton/listings/ch12/lst-expert-parallelism-and-all-to-all-communication.tex` - Python listing. Implements or sketches: Conceptual pseudocode for distributed dispatch without runnable distributed code.. Caption placeholder included. Label: `lst:ch12-expert-parallelism-and-all-to-all-communication`.
- `latex_book_skeleton/equations/ch12/eq-expert-parallelism-and-all-to-all-communication.tex` - Equation. States: Communication volume depends on routed token count, D, K, and bytes per element.. Label: `eq:ch12-expert-parallelism-and-all-to-all-communication`.

## Code deliverable

Develop the code in `ch12/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Thought experiment table estimating routed activation traffic for a small config.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
