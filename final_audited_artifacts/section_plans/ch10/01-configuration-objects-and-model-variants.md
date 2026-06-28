# Section plan: Chapter 10.1 - Configuration objects and model variants

## Local objective

Move from chapter-specific modules to a unified configuration-driven model.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Define DenseBaselineConfig, MiniDeepSeekMoESmokeConfig, and MiniDeepSeekMoE16x2Config.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch10/fig-configuration-objects-and-model-variants}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch10/eq-configuration-objects-and-model-variants}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch10/lst-configuration-objects-and-model-variants}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The decoder block can now instantiate dense or MoE FFN paths from config.

## Planned artifacts

- `latex_book_skeleton/figures/ch10/fig-configuration-objects-and-model-variants.tex` - TikZ. Shows: Configuration tree controlling attention, FFN/MoE, routing, balancing, and diagnostics.. Caption placeholder included. Label: `fig:ch10-configuration-objects-and-model-variants`.
- `latex_book_skeleton/tables/ch10/tab-configuration-objects-and-model-variants.tex` - Table. Defines: Final configuration fields and default values.. Caption placeholder included. Label: `tab:ch10-configuration-objects-and-model-variants`.
- `latex_book_skeleton/listings/ch10/lst-configuration-objects-and-model-variants.tex` - Python listing. Implements or sketches: Dataclass or simple config object for MiniDeepSeekMoE.. Caption placeholder included. Label: `lst:ch10-configuration-objects-and-model-variants`.
- `latex_book_skeleton/equations/ch10/eq-configuration-objects-and-model-variants.tex` - Equation. States: Variant identity as a tuple of depth, width, expert count, K, and balancing method.. Label: `eq:ch10-configuration-objects-and-model-variants`.

## Code deliverable

Develop the code in `ch10/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Print model summary and assert required fields exist.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
