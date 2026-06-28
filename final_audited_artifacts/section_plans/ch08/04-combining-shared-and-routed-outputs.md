# Section plan: Chapter 8.4 - Combining shared and routed outputs

## Local objective

Implement the forward pass that sums shared expert output and weighted routed output.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Trace one token through shared expert s0 and routed experts e2/e7.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch08/fig-combining-shared-and-routed-outputs}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch08/eq-combining-shared-and-routed-outputs}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch08/lst-combining-shared-and-routed-outputs}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: With two expert paths, diagnostics should separate shared and routed behavior.

## Planned artifacts

- `latex_book_skeleton/figures/ch08/fig-combining-shared-and-routed-outputs.tex` - TikZ. Shows: Shared output and routed weighted output merged before projection back to the decoder block.. Caption placeholder included. Label: `fig:ch08-combining-shared-and-routed-outputs`.
- `latex_book_skeleton/tables/ch08/tab-combining-shared-and-routed-outputs.tex` - Table. Defines: Output components: shared_out, routed_out, residual, and final block output.. Caption placeholder included. Label: `tab:ch08-combining-shared-and-routed-outputs`.
- `latex_book_skeleton/listings/ch08/lst-combining-shared-and-routed-outputs.tex` - Python listing. Implements or sketches: Forward pass for shared+routed MoE layer.. Caption placeholder included. Label: `lst:ch08-combining-shared-and-routed-outputs`.
- `latex_book_skeleton/equations/ch08/eq-combining-shared-and-routed-outputs.tex` - Equation. States: moe_out_t = shared_out_t + sum_j gate_{tj} routed_expert_{idx_{tj}}(x_t).. Label: `eq:ch08-combining-shared-and-routed-outputs`.

## Code deliverable

Develop the code in `ch08/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Ablate shared_out to zero and routed_out to zero to confirm both paths affect output.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
