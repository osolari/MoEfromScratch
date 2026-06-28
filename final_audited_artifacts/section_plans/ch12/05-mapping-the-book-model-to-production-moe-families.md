# Section plan: Chapter 12.5 - Mapping the book model to production MoE families

## Local objective

Connect MiniDeepSeekMoE pieces to broader MoE designs while staying honest about omitted details.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Map top-k routing, shared experts, fine-grained experts, and router bias to the final reference model vocabulary.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch12/fig-mapping-the-book-model-to-production-moe-families}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch12/eq-mapping-the-book-model-to-production-moe-families}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch12/lst-mapping-the-book-model-to-production-moe-families}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The book closes by summarizing the reusable mental model.

## Planned artifacts

- `latex_book_skeleton/figures/ch12/fig-mapping-the-book-model-to-production-moe-families.tex` - TikZ. Shows: Concept map from book components to larger MoE system components.. Caption placeholder included. Label: `fig:ch12-mapping-the-book-model-to-production-moe-families`.
- `latex_book_skeleton/tables/ch12/tab-mapping-the-book-model-to-production-moe-families.tex` - Table. Defines: Book implementation feature, production analogue, and what remains out of scope.. Caption placeholder included. Label: `tab:ch12-mapping-the-book-model-to-production-moe-families`.
- `latex_book_skeleton/listings/ch12/lst-mapping-the-book-model-to-production-moe-families.tex` - Python listing. Implements or sketches: Config comparison snippet showing smoke, default, and larger teaching configs.. Caption placeholder included. Label: `lst:ch12-mapping-the-book-model-to-production-moe-families`.
- `latex_book_skeleton/equations/ch12/eq-mapping-the-book-model-to-production-moe-families.tex` - Equation. States: Scaling identity: same layer contract, larger E, larger D, more devices.. Label: `eq:ch12-mapping-the-book-model-to-production-moe-families`.

## Code deliverable

Develop the code in `ch12/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Reader checkpoint: identify which chapter implemented each production analogue.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
