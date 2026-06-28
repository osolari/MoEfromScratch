# Section plan: Chapter 12.2 - Batching routed tokens at inference

## Local objective

Show why MoE inference wants tokens for the same expert to be grouped efficiently.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Two prompts in a batch route their next token to different experts.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch12/fig-batching-routed-tokens-at-inference}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch12/eq-batching-routed-tokens-at-inference}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch12/lst-batching-routed-tokens-at-inference}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Compute and memory estimates clarify where the toy implementation stops scaling.

## Planned artifacts

- `latex_book_skeleton/figures/ch12/fig-batching-routed-tokens-at-inference.tex` - TikZ. Shows: Inference batch tokens packed into expert-specific microbatches.. Caption placeholder included. Label: `fig:ch12-batching-routed-tokens-at-inference`.
- `latex_book_skeleton/tables/ch12/tab-batching-routed-tokens-at-inference.tex` - Table. Defines: Inference batching challenges: uneven loads, small expert batches, padding, latency.. Caption placeholder included. Label: `tab:ch12-batching-routed-tokens-at-inference`.
- `latex_book_skeleton/listings/ch12/lst-batching-routed-tokens-at-inference.tex` - Python listing. Implements or sketches: profile_inference_routes function collecting per-step expert batch sizes.. Caption placeholder included. Label: `lst:ch12-batching-routed-tokens-at-inference`.
- `latex_book_skeleton/equations/ch12/eq-batching-routed-tokens-at-inference.tex` - Equation. States: Expert batch size distribution at generation step s.. Label: `eq:ch12-batching-routed-tokens-at-inference`.

## Code deliverable

Develop the code in `ch12/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Histogram expert batch sizes over a generated sequence.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
