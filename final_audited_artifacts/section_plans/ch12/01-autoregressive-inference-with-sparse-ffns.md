# Section plan: Chapter 12.1 - Autoregressive inference with sparse FFNs

## Local objective

Explain what changes and what stays the same when a trained MoE model generates text one token at a time.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Generate one new token and trace attention, router, selected experts, and logits.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch12/fig-autoregressive-inference-with-sparse-ffns}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch12/eq-autoregressive-inference-with-sparse-ffns}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch12/lst-autoregressive-inference-with-sparse-ffns}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Batching multiple requests complicates the expert batches.

## Planned artifacts

- `latex_book_skeleton/figures/ch12/fig-autoregressive-inference-with-sparse-ffns.tex` - TikZ. Shows: One-token inference path through attention cache and MoE layer.. Caption placeholder included. Label: `fig:ch12-autoregressive-inference-with-sparse-ffns`.
- `latex_book_skeleton/tables/ch12/tab-autoregressive-inference-with-sparse-ffns.tex` - Table. Defines: Training-time versus inference-time routing tensors.. Caption placeholder included. Label: `tab:ch12-autoregressive-inference-with-sparse-ffns`.
- `latex_book_skeleton/listings/ch12/lst-autoregressive-inference-with-sparse-ffns.tex` - Python listing. Implements or sketches: generate function with routing metrics optionally returned per step.. Caption placeholder included. Label: `lst:ch12-autoregressive-inference-with-sparse-ffns`.
- `latex_book_skeleton/equations/ch12/eq-autoregressive-inference-with-sparse-ffns.tex` - Equation. States: Per-step active expert calls equal layers_with_moe * K for one token.. Label: `eq:ch12-autoregressive-inference-with-sparse-ffns`.

## Code deliverable

Develop the code in `ch12/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Print selected experts for each generated token in a short sample.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
