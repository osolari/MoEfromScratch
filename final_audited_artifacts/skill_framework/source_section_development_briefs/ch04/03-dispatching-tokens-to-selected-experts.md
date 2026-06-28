# Detailed section development brief: Chapter 4.3 - Dispatching tokens to selected experts

Use this file as the complete handoff brief for developing this section in a separate chat session. It is intentionally self-contained: it repeats the local objective, LaTeX paths, artifact contracts, color map, code expectations, diagnostics, and proofreading checks.

## 1. Section identity

| Field | Value |
|---|---|
| Book | *MoE Models from Scratch* |
| Chapter | 4. Top-1 routing and Switch-style dispatch |
| Section | 4.3. Dispatching tokens to selected experts |
| Section label slug | `ch04-dispatching-tokens-to-selected-experts` |
| Section `.tex` target | `latex_book_skeleton/chapters/ch04/sections/03-dispatching-tokens-to-selected-experts.tex` |
| Planned section include | `\input{chapters/ch04/sections/03-dispatching-tokens-to-selected-experts}` |
| Previous handoff | Chapter 4.2 - Assignment masks and expert buckets |
| Next handoff | Chapter 4.4 - Capacity and dropped tokens |

## 2. Local objective

Run each expert only on the tokens assigned to it and scatter outputs back to token order.

**Reader promise:** by the end of this section, the reader should be able to explain the mechanism in plain language, trace the relevant tensor shapes, connect the equation to a runnable PyTorch fragment, and run the planned diagnostic without relying on hidden framework code.

**Mini-example to anchor the section:** Expert 0 receives token rows [0,3], expert 1 receives [1], and empty experts are skipped.

## 3. Role in the chapter and book

**Chapter role:** Teach top-1 sparse dispatch as the simplest end-to-end MoE routing case.

**Reader enters knowing:** Reader can compute router scores and naive dispatch for selected experts.

**Reader leaves with:** Reader can implement Switch-style top-1 routing, expert buckets, capacity, and dropped-token diagnostics.

**Chapter-level invariant:** Each token chooses exactly one routed expert before capacity constraints are applied.

**This section's bridge sentence:** Routing can overload an expert, so we need to define expert capacity.

## 4. Required development flow

Follow this sequence. The order matters because it matches the source-book pattern: visual intuition before heavy implementation, and diagnostics before the handoff.

1. **Problem opening.** Start with the concrete bottleneck, bug, inefficiency, or missing capability that makes this section necessary. Avoid starting with a definition.
2. **Visual anchor.** Insert the figure wrapper immediately after the opening setup. Use the diagram to name the moving parts before math.
3. **Shape-first mechanics.** Define tensor names, tensor ranks, and shape conventions before equations or code.
4. **Equation or algorithm.** Include the equation wrapper and explain each symbol in prose. Keep the equation local to the section objective.
5. **Implementation listing.** Include the listing wrapper after the reader has enough notation to read it. Annotate non-obvious lines rather than restating every line.
6. **Diagnostic check.** Use the table plus a runnable check to make the section falsifiable.
7. **Bridge.** End by naming the next unresolved issue and handing off to the next section.

### Suggested paragraph-level outline

1. **Opening paragraph.** State the concrete problem: Run each expert only on the tokens assigned to it and scatter outputs back to token order. Do not begin with a survey paragraph.
2. **Motivating example.** Use the mini-example exactly or as a close variant: Expert 0 receives token rows [0,3], expert 1 receives [1], and empty experts are skipped.
3. **Visual explanation.** Insert `\input{figures/ch04/fig-dispatching-tokens-to-selected-experts}` immediately after the setup.
4. **Shape and notation block.** Introduce symbols before the equation: B = batch size, T = sequence length, D = model width, N = B*T flattened token count, E = number of routed experts, k = number of selected routed experts.
5. **Mechanics and equation.** Insert `\input{equations/ch04/eq-dispatching-tokens-to-selected-experts}` and explain why it implements the local objective.
6. **Implementation.** Insert `\input{listings/ch04/lst-dispatching-tokens-to-selected-experts}` and annotate only the lines where a reader could make a shape, routing, or gradient mistake.
7. **Diagnostic.** Insert `\input{tables/ch04/tab-dispatching-tokens-to-selected-experts}` near the diagnostic discussion if the table is a contract/check table; otherwise place it before code as a notation table.
8. **Bridge.** End with the section bridge sentence above, revised only for grammar if surrounding prose requires it.

## 5. Required LaTeX assembly

The section prose must include artifacts through these exact `\input` commands. Do not inline the environments in the section file.

```latex
\input{figures/ch04/fig-dispatching-tokens-to-selected-experts}
\input{tables/ch04/tab-dispatching-tokens-to-selected-experts}
\input{equations/ch04/eq-dispatching-tokens-to-selected-experts}
\input{listings/ch04/lst-dispatching-tokens-to-selected-experts}
```

The figure/table/listing/equation wrappers already exist as placeholders in `latex_book_skeleton`. Replace their bodies during section development, but preserve paths, labels, and the standalone-wrapper structure.

## 6. Artifact specifications

### Figure placeholder

| Field | Requirement |
|---|---|
| Path | `latex_book_skeleton/figures/ch04/fig-dispatching-tokens-to-selected-experts.tex` |
| Include command | `\input{figures/ch04/fig-dispatching-tokens-to-selected-experts}` |
| Type | TikZ schematic wrapper |
| Label | `fig:ch04-dispatching-tokens-to-selected-experts` |
| Caption intent | Gather tokens into expert batches, process, then scatter back. |
| Wrapper contract | The figure file must contain a `tikzpicture` environment, caption, and label. |

**Figure content plan:** Gather tokens into expert batches, process, then scatter back.

**Visual construction notes:** Use active green for exactly one selected expert per token and imbalance red for drops or overload. Use semantic TikZ styles from `styles/tikzstyles.tex`. Do not use raw hex colors in the diagram body. If this is a generated PDF plot, save the plotted PDF under `figures/generated/ch04/` and keep the wrapper responsible only for `\includegraphics`, caption, and label.

### Table placeholder

| Field | Requirement |
|---|---|
| Path | `latex_book_skeleton/tables/ch04/tab-dispatching-tokens-to-selected-experts.tex` |
| Include command | `\input{tables/ch04/tab-dispatching-tokens-to-selected-experts}` |
| Label | `tab:ch04-dispatching-tokens-to-selected-experts` |
| Caption intent | Gather, expert batch, and scatter tensor shapes. |
| Required columns | Concept | Local definition | Shape/code object | Why it matters | Check |

**Planned table rows:**
- row 1: define the primary object for "Dispatching tokens to selected experts"
- row 2: define the companion tensor/code object used by the implementation
- row 3: define the diagnostic quantity that can catch incorrect behavior
- row 4: define the edge case or failure mode that the reader should watch

The table should be small enough to fit near the explanation. Prefer four to eight rows. Use it as a contract, shape table, diagnostic matrix, or comparison summary rather than as decoration.

### Equation placeholder

| Field | Requirement |
|---|---|
| Path | `latex_book_skeleton/equations/ch04/eq-dispatching-tokens-to-selected-experts.tex` |
| Include command | `\input{equations/ch04/eq-dispatching-tokens-to-selected-experts}` |
| Label | `eq:ch04-dispatching-tokens-to-selected-experts` |
| Equation intent | output[token_indices_i] = expert_i(x[token_indices_i]). |

**Symbols that must be introduced before the equation:**
- B = batch size
- T = sequence length
- D = model width
- N = B*T flattened token count
- E = number of routed experts
- k = number of selected routed experts

The equation should be locally useful. Do not include a broad derivation unless it directly helps the reader implement or test this section.

### Listing placeholder

| Field | Requirement |
|---|---|
| Path | `latex_book_skeleton/listings/ch04/lst-dispatching-tokens-to-selected-experts.tex` |
| Include command | `\input{listings/ch04/lst-dispatching-tokens-to-selected-experts}` |
| Label | `lst:ch04-dispatching-tokens-to-selected-experts` |
| Listing intent | Top1MoELayer dispatch and scatter implementation. |

**Code objects to develop or reference:**
- `Top1MoELayer.dispatch`
- `bucketed expert calls`

The listing should be runnable or very close to runnable. Keep it shorter than the full source file by showing the smallest fragment that teaches the new idea. Full code belongs in the chapter code directory.

## 7. Code development plan

**Primary code location:** `ch04/01_main-chapter-code/ with Top1Router, Top1MoELayer, capacity checks, and histograms.`

1. Start from the previous section's tested code, not from a fresh implementation.
2. Add only the minimal new object or function needed for **Dispatching tokens to selected experts**.
3. Write a CPU smoke test using the mini-example: Expert 0 receives token rows [0,3], expert 1 receives [1], and empty experts are skipped.
4. Preserve the chapter-level invariant: Each token chooses exactly one routed expert before capacity constraints are applied.
5. If a helper becomes reusable across later chapters, mark it with a comment such as `# promoted later to common/` but do not prematurely reorganize the codebase during the section draft.

**Expected code deliverable:** Top1MoELayer dispatch and scatter implementation.

## 8. Diagnostic requirement

Assert output rows return to the original token order.

Make the diagnostic falsifiable. A reader should be able to intentionally break one line of code and see this diagnostic fail. The diagnostic may be an assertion, a tiny printed table, a unit-test-like function, or a generated plot depending on the section.

Suggested diagnostic checks:

- Verify the output shape and dtype that the section claims.
- Verify at least one edge case from the table.
- Verify the routing/load/score quantity named in the local objective.
- Use a fixed random seed when comparing against a reference implementation.

## 9. Common inaccuracies to avoid

- Do not hide dropped tokens; visualize them and decide the residual/skip policy.
- Do not make top-1 look like final model quality; it is a teaching milestone.
- Distinguish assignment counts from probability mass.

## 10. Reproducible visual theme

Use this color map exactly. Refer to macros by name in TikZ and LaTeX; do not hand-code hex values in artifacts.

| Color macro | Hex | Use |
|---|---:|---|
| `BookNavy` | `#000055` | chapter titles, primary headings, rule accents |
| `BookDeepBlue` | `#141464` | diagram outlines, table header text, normal arrows |
| `BookListingHeader` | `#020056` | listing title/header accents |
| `BookCalloutGray` | `#E6E6E6` | chapter-cover boxes, note boxes, checkpoint boxes |
| `BookCodeBg` | `#F2F2F2` | code listing background |
| `MoETokenPurple` | `#C060E0` | tokens, token batches, token-flow dots |
| `MoERouterCyan` | `#00A7C1` | routers, score matrices, dispatch arrows |
| `MoEExpertPurple` | `#9050FF` | inactive or generic routed experts |
| `MoEActiveGreen` | `#70D050` | selected experts, active routes, passing tests |
| `MoESharedGreen` | `#A8DDA8` | shared experts and dense shared paths |
| `MoEOutputRed` | `#F05050` | outputs, warnings, failure highlights when red is not used for imbalance |
| `MoEImbalanceRed` | `#E03030` | expert imbalance, overflow, dropped tokens, unsafe conclusions |
| `MoECapacityGold` | `#FFD080` | capacity slots, top-k slots, roadmap milestones |
| `MoEMutedGray` | `#D0D0D0` | inactive paths, non-selected experts, background grid |
| `MoESoftFill` | `#F0F0FF` | soft fill for generic blocks |

## 11. Writing voice and explanation style

- Use the source-book flow: concrete problem, visual explanation, shape-aware mechanics, code, diagnostic, summary bridge.
- Prefer implementation language over survey language.
- Introduce terms only when they appear in a figure, equation, table, or listing.
- Keep paragraphs short enough that artifacts carry the teaching load.
- Use careful claims. For example, say that MoE changes activated compute per token, not that it automatically makes wall-clock runtime lower.

## 12. Acceptance checklist

- [ ] The section starts from a concrete problem or missing capability.
- [ ] The first substantial artifact is the planned visual figure.
- [ ] All tensor names have shapes before the listing appears.
- [ ] The equation is referenced and explained in prose.
- [ ] The listing teaches one new implementation idea and is CPU-smoke-testable.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] The table is useful as a contract, comparison, or diagnostic aid.
- [ ] All artifacts are standalone `.tex` wrappers included through `\input`.
- [ ] Figures and tables stay in their owning section; default figure/table wrappers use `[H]`, and `placeins`/`\FloatBarrier` remains active in the compiled book.
- [ ] TikZ diagrams use semantic styles and PDF plots use `\includegraphics[width=\BookFigureWidth]` inside their wrapper.
- [ ] The final paragraph bridges to: Chapter 4.4 - Capacity and dropped tokens.

## 13. Ready-to-use prompt for the section-development chat

```text
Develop Chapter 4.3, "Dispatching tokens to selected experts", for MoE Models from Scratch using this brief. Produce LaTeX-first section prose and update only the standalone artifact wrappers listed here. Follow the required flow: problem opening -> visual anchor -> tensor/math mechanics -> implementation listing -> diagnostic -> bridge. Keep all figures/tables/listings/equations included via \input and preserve the color/theme contract.
```
