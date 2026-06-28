# Section plan: Chapter 11.5 - Interpreting expert behavior carefully

## Local objective

Teach readers to inspect expert usage without overclaiming that tiny experts learned semantic roles.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Look at expert IDs selected for a short prompt and compare across positions or token types.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch11/fig-interpreting-expert-behavior-carefully}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch11/eq-interpreting-expert-behavior-carefully}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch11/lst-interpreting-expert-behavior-carefully}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The final chapter steps back from experiments to discuss inference and scaling limits.

## Planned artifacts

- `latex_book_skeleton/figures/ch11/fig-interpreting-expert-behavior-carefully.tex` - TikZ. Shows: Token-by-token routing trace over a prompt.. Caption placeholder included. Label: `fig:ch11-interpreting-expert-behavior-carefully`.
- `latex_book_skeleton/tables/ch11/tab-interpreting-expert-behavior-carefully.tex` - Table. Defines: Interpretation checklist: evidence, limitation, alternative explanation, next test.. Caption placeholder included. Label: `tab:ch11-interpreting-expert-behavior-carefully`.
- `latex_book_skeleton/listings/ch11/lst-interpreting-expert-behavior-carefully.tex` - Python listing. Implements or sketches: trace_prompt_routing.py that prints token, top-k experts, and gates.. Caption placeholder included. Label: `lst:ch11-interpreting-expert-behavior-carefully`.
- `latex_book_skeleton/equations/ch11/eq-interpreting-expert-behavior-carefully.tex` - Equation. States: Conditional expert frequency for a chosen token group.. Label: `eq:ch11-interpreting-expert-behavior-carefully`.

## Code deliverable

Develop the code in `ch11/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Generate a routing trace table and a usage heatmap.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
