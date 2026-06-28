# Section plan: Chapter 8.3 - The MiniDeepSeekMoE layer contract

## Local objective

Define the final layer interface that later chapters assemble into the full model.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use D=128, E=4 routed experts, one shared expert, and K=2 in the smoke config.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch08/fig-the-minideepseekmoe-layer-contract}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch08/eq-the-minideepseekmoe-layer-contract}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch08/lst-the-minideepseekmoe-layer-contract}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The forward pass computes shared and routed paths side by side.

## Planned artifacts

- `latex_book_skeleton/figures/ch08/fig-the-minideepseekmoe-layer-contract.tex` - TikZ. Shows: MiniDeepSeekMoE layer block with router, routed experts, shared experts, combine, and residual output.. Caption placeholder included. Label: `fig:ch08-the-minideepseekmoe-layer-contract`.
- `latex_book_skeleton/tables/ch08/tab-the-minideepseekmoe-layer-contract.tex` - Table. Defines: Final layer tensor contract and configuration fields.. Caption placeholder included. Label: `tab:ch08-the-minideepseekmoe-layer-contract`.
- `latex_book_skeleton/listings/ch08/lst-the-minideepseekmoe-layer-contract.tex` - Python listing. Implements or sketches: MiniDeepSeekMoELayer __init__ showing router, routed experts, and shared experts.. Caption placeholder included. Label: `lst:ch08-the-minideepseekmoe-layer-contract`.
- `latex_book_skeleton/equations/ch08/eq-the-minideepseekmoe-layer-contract.tex` - Equation. States: y = x + shared_out + routed_out when the block is shown with residual context.. Label: `eq:ch08-the-minideepseekmoe-layer-contract`.

## Code deliverable

Develop the code in `ch08/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Assert layer output shape equals input shape under smoke and default configs.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
