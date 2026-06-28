# Section plan: Chapter 8.2 - Fine-grained routed expert segmentation

## Local objective

Show how more smaller experts can replace fewer larger experts while preserving readable code.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Compare 4 large experts with hidden_dim=1024 to 16 smaller experts with hidden_dim=256.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch08/fig-fine-grained-routed-expert-segmentation}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch08/eq-fine-grained-routed-expert-segmentation}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch08/lst-fine-grained-routed-expert-segmentation}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The reference layer combines fine-grained routed experts with shared experts.

## Planned artifacts

- `latex_book_skeleton/figures/ch08/fig-fine-grained-routed-expert-segmentation.tex` - TikZ. Shows: Large expert blocks split into finer expert tiles.. Caption placeholder included. Label: `fig:ch08-fine-grained-routed-expert-segmentation`.
- `latex_book_skeleton/tables/ch08/tab-fine-grained-routed-expert-segmentation.tex` - Table. Defines: Expert count, hidden dimension, total parameters, and active parameters.. Caption placeholder included. Label: `tab:ch08-fine-grained-routed-expert-segmentation`.
- `latex_book_skeleton/listings/ch08/lst-fine-grained-routed-expert-segmentation.tex` - Python listing. Implements or sketches: ExpertBank configuration that changes n_experts and expert_hidden_dim together.. Caption placeholder included. Label: `lst:ch08-fine-grained-routed-expert-segmentation`.
- `latex_book_skeleton/equations/ch08/eq-fine-grained-routed-expert-segmentation.tex` - Equation. States: Expert-bank parameter estimate E * (D*H_e + H_e*D).. Label: `eq:ch08-fine-grained-routed-expert-segmentation`.

## Code deliverable

Develop the code in `ch08/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Compute total and active expert parameters for several segmentations.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
