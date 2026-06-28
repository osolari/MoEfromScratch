---
name: moe-ch11-s05-interpreting-expert-behavior-carefully
description: use when developing section 11.5, interpreting expert behavior carefully, for the latex-first book moe models from scratch. triggers include drafting this section, replacing its artifact wrappers, updating its local code, running its diagnostic, or proofreading its handoff.
---

# Section developer: Chapter 11.5 - Interpreting expert behavior carefully

Use this skill-style markdown as the single-section development framework for a separate chat session. It is intentionally self-contained and should be enough to draft, implement, test, and proofread the section without reopening the whole planning package.

## Scope lock

Develop only Section 11.5 of *MoE Models from Scratch*: **Interpreting expert behavior carefully**.

- Chapter: 11. Training, diagnostics, and controlled experiments
- Target section file: `latex_book_skeleton/chapters/ch11/sections/05-interpreting-expert-behavior-carefully.tex`
- Planned figure wrapper: `latex_book_skeleton/figures/ch11/fig-interpreting-expert-behavior-carefully.tex`
- Planned table wrapper: `latex_book_skeleton/tables/ch11/tab-interpreting-expert-behavior-carefully.tex`
- Planned equation wrapper: `latex_book_skeleton/equations/ch11/eq-interpreting-expert-behavior-carefully.tex`
- Planned listing wrapper: `latex_book_skeleton/listings/ch11/lst-interpreting-expert-behavior-carefully.tex`
- Required diagnostic: Generate a routing trace table and a usage heatmap.

## Non-negotiable development rules

- Develop the production book in LaTeX.
- Keep section prose in the planned `latex_book_skeleton/chapters/chXX/sections/*.tex` file.
- Do not inline `figure`, `table`, `lstlisting`, or `equation` environments in section prose.
- Do not allow figures or tables to float into a later section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active when compiling.
- Include every planned artifact through a standalone `.tex` wrapper and `\input{...}`.
- Use TikZ for mechanism schematics.
- Use generated PDF assets only for plots, dashboards, and diagnostics; include them through figure wrappers.
- Preserve the MiniDeepSeekMoE invariant wherever router bias appears: router bias affects selection only; final combine weights are computed from unbiased selected scores.
- Follow the teaching flow: problem opening -> visual anchor -> tensor/math mechanics -> implementation listing -> diagnostic -> bridge.
- Avoid broad surveys inside local sections; make every section falsifiable with its diagnostic.


## Required artifact inputs

The section prose must include these exact artifacts through `\input`, without inlining their environments:

```latex
\input{figures/ch11/fig-interpreting-expert-behavior-carefully}
\input{tables/ch11/tab-interpreting-expert-behavior-carefully}
\input{equations/ch11/eq-interpreting-expert-behavior-carefully}
\input{listings/ch11/lst-interpreting-expert-behavior-carefully}
```

## Local acceptance criteria

- The section opens with the concrete local problem rather than a broad survey.
- The planned figure appears before dense equations or code.
- The planned equation introduces only the symbols needed for this section.
- The planned listing is runnable or very close to runnable.
- The diagnostic can fail if the section's implementation is wrong.
- The final paragraph bridges to the next handoff named in the source brief.
- No raw `figure`, `table`, `lstlisting`, or `equation` environment appears inside the section prose file.

## Visual theme summary

Use semantic LaTeX color names only.

| Role | LaTeX color | Hex | Use |
|---|---|---:|---|
| Main navy | `BookNavy` | `#000055` | chapter titles and structural headings |
| Deep blue | `BookDeepBlue` | `#141464` | neutral diagram text and arrows |
| Listing header | `BookListingHeader` | `#020056` | code listing title bars |
| Callout gray | `BookCalloutGray` | `#E6E6E6` | notes, checkpoints, and chapter-cover boxes |
| Code background | `BookCodeBg` | `#F2F2F2` | listing background |
| Token purple | `MoETokenPurple` | `#C060E0` | tokens and token-flow dots |
| Router cyan | `MoERouterCyan` | `#00A7C1` | routers, score matrices, dispatch arrows |
| Expert purple | `MoEExpertPurple` | `#9050FF` | generic routed experts |
| Active expert green | `MoEActiveGreen` | `#70D050` | selected experts and active routes |
| Output red | `MoEOutputRed` | `#F05050` | outputs, overflow, imbalance warnings |
| Capacity gold | `MoECapacityGold` | `#FFD080` | capacity, top-k slots, quotas, and bias state |
| Shared expert green | `MoESharedGreen` | `#A8DDA8` | shared experts and always-on paths |
| Muted gray | `MoEMutedGray` | `#D0D0D0` | inactive routes and background structures |
| Soft fill | `MoESoftFill` | `#F0F0FF` | grouping regions |

Use semantic TikZ styles from `styles/tikzstyles.tex`. Do not scatter raw hex colors through figure bodies.


## Ready-to-use separate-chat prompt

```text
Develop Section 11.5, "Interpreting expert behavior carefully", for MoE Models from Scratch. Use this skill markdown as the complete handoff. Produce LaTeX-first section prose, update only the artifact wrappers listed here, preserve every artifact through \input, and include a runnable or near-runnable diagnostic tied to the planned code path.
```

## Source session starter

# Session starter: Chapter 11.5 - Interpreting expert behavior carefully

Develop only Chapter 11.5, **Interpreting expert behavior carefully**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch11/05-interpreting-expert-behavior-carefully.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch11/sections/05-interpreting-expert-behavior-carefully.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch11/fig-interpreting-expert-behavior-carefully}`
- `\input{tables/ch11/tab-interpreting-expert-behavior-carefully}`
- `\input{equations/ch11/eq-interpreting-expert-behavior-carefully}`
- `\input{listings/ch11/lst-interpreting-expert-behavior-carefully}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.


## Full source section brief

# Detailed section development brief: Chapter 11.5 - Interpreting expert behavior carefully

Use this file as the complete handoff brief for developing this section in a separate chat session. It is intentionally self-contained: it repeats the local objective, LaTeX paths, artifact contracts, color map, code expectations, diagnostics, and proofreading checks.

## 1. Section identity

| Field | Value |
|---|---|
| Book | *MoE Models from Scratch* |
| Chapter | 11. Training, diagnostics, and controlled experiments |
| Section | 11.5. Interpreting expert behavior carefully |
| Section label slug | `ch11-interpreting-expert-behavior-carefully` |
| Section `.tex` target | `latex_book_skeleton/chapters/ch11/sections/05-interpreting-expert-behavior-carefully.tex` |
| Planned section include | `\input{chapters/ch11/sections/05-interpreting-expert-behavior-carefully}` |
| Previous handoff | Chapter 11.4 - Ablation matrix: dense, top-1, top-2, shared, and bias-balanced |
| Next handoff | Chapter 11.6 - Chapter summary and handoff |

## 2. Local objective

Teach readers to inspect expert usage without overclaiming that tiny experts learned semantic roles.

**Reader promise:** by the end of this section, the reader should be able to explain the mechanism in plain language, trace the relevant tensor shapes, connect the equation to a runnable PyTorch fragment, and run the planned diagnostic without relying on hidden framework code.

**Mini-example to anchor the section:** Look at expert IDs selected for a short prompt and compare across positions or token types.

## 3. Role in the chapter and book

**Chapter role:** Run controlled experiments and teach the reader how to interpret MoE diagnostics carefully.

**Reader enters knowing:** Reader has a full model and needs evidence rather than anecdotes.

**Reader leaves with:** Reader has reproducible runs, ablations, diagnostic plots, and caution around expert-behavior interpretation.

**Chapter-level invariant:** Every comparison must hold dataset, token budget, optimizer settings, and evaluation protocol fixed unless the section says otherwise.

**This section's bridge sentence:** The final chapter steps back from experiments to discuss inference and scaling limits.

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

1. **Opening paragraph.** State the concrete problem: Teach readers to inspect expert usage without overclaiming that tiny experts learned semantic roles. Do not begin with a survey paragraph.
2. **Motivating example.** Use the mini-example exactly or as a close variant: Look at expert IDs selected for a short prompt and compare across positions or token types.
3. **Visual explanation.** Insert `\input{figures/ch11/fig-interpreting-expert-behavior-carefully}` immediately after the setup.
4. **Shape and notation block.** Introduce symbols before the equation: B = batch size, T = sequence length, D = model width, N = B*T flattened token count, E = number of routed experts, k = number of selected routed experts, C = per-expert capacity or slot count, s = expert slot index, S = number of shared experts or shared expert output, b_e = non-trainable router bias for expert e.
5. **Mechanics and equation.** Insert `\input{equations/ch11/eq-interpreting-expert-behavior-carefully}` and explain why it implements the local objective.
6. **Implementation.** Insert `\input{listings/ch11/lst-interpreting-expert-behavior-carefully}` and annotate only the lines where a reader could make a shape, routing, or gradient mistake.
7. **Diagnostic.** Insert `\input{tables/ch11/tab-interpreting-expert-behavior-carefully}` near the diagnostic discussion if the table is a contract/check table; otherwise place it before code as a notation table.
8. **Bridge.** End with the section bridge sentence above, revised only for grammar if surrounding prose requires it.

## 5. Required LaTeX assembly

The section prose must include artifacts through these exact `\input` commands. Do not inline the environments in the section file.

```latex
\input{figures/ch11/fig-interpreting-expert-behavior-carefully}
\input{tables/ch11/tab-interpreting-expert-behavior-carefully}
\input{equations/ch11/eq-interpreting-expert-behavior-carefully}
\input{listings/ch11/lst-interpreting-expert-behavior-carefully}
```

The figure/table/listing/equation wrappers already exist as placeholders in `latex_book_skeleton`. Replace their bodies during section development, but preserve paths, labels, and the standalone-wrapper structure.

## 6. Artifact specifications

### Figure placeholder

| Field | Requirement |
|---|---|
| Path | `latex_book_skeleton/figures/ch11/fig-interpreting-expert-behavior-carefully.tex` |
| Include command | `\input{figures/ch11/fig-interpreting-expert-behavior-carefully}` |
| Type | TikZ schematic wrapper |
| Label | `fig:ch11-interpreting-expert-behavior-carefully` |
| Caption intent | Token-by-token routing trace over a prompt. |
| Wrapper contract | The figure file must contain a `tikzpicture` environment, caption, and label. |

**Figure content plan:** Token-by-token routing trace over a prompt.

**Visual construction notes:** Use generated PDF plots for loss curves, load histograms, and ablation dashboards. Tables should carry experiment controls. Use semantic TikZ styles from `styles/tikzstyles.tex`. Do not use raw hex colors in the diagram body. If this is a generated PDF plot, save the plotted PDF under `figures/generated/ch11/` and keep the wrapper responsible only for `\includegraphics`, caption, and label.

### Table placeholder

| Field | Requirement |
|---|---|
| Path | `latex_book_skeleton/tables/ch11/tab-interpreting-expert-behavior-carefully.tex` |
| Include command | `\input{tables/ch11/tab-interpreting-expert-behavior-carefully}` |
| Label | `tab:ch11-interpreting-expert-behavior-carefully` |
| Caption intent | Interpretation checklist: evidence, limitation, alternative explanation, next test. |
| Required columns | Concept | Local definition | Shape/code object | Why it matters | Check |

**Planned table rows:**
- row 1: define the primary object for "Interpreting expert behavior carefully"
- row 2: define the companion tensor/code object used by the implementation
- row 3: define the diagnostic quantity that can catch incorrect behavior
- row 4: define the edge case or failure mode that the reader should watch

The table should be small enough to fit near the explanation. Prefer four to eight rows. Use it as a contract, shape table, diagnostic matrix, or comparison summary rather than as decoration.

### Equation placeholder

| Field | Requirement |
|---|---|
| Path | `latex_book_skeleton/equations/ch11/eq-interpreting-expert-behavior-carefully.tex` |
| Include command | `\input{equations/ch11/eq-interpreting-expert-behavior-carefully}` |
| Label | `eq:ch11-interpreting-expert-behavior-carefully` |
| Equation intent | Conditional expert frequency for a chosen token group. |

**Symbols that must be introduced before the equation:**
- B = batch size
- T = sequence length
- D = model width
- N = B*T flattened token count
- E = number of routed experts
- k = number of selected routed experts
- C = per-expert capacity or slot count
- s = expert slot index
- S = number of shared experts or shared expert output
- b_e = non-trainable router bias for expert e

The equation should be locally useful. Do not include a broad derivation unless it directly helps the reader implement or test this section.

### Listing placeholder

| Field | Requirement |
|---|---|
| Path | `latex_book_skeleton/listings/ch11/lst-interpreting-expert-behavior-carefully.tex` |
| Include command | `\input{listings/ch11/lst-interpreting-expert-behavior-carefully}` |
| Label | `lst:ch11-interpreting-expert-behavior-carefully` |
| Listing intent | trace_prompt_routing.py that prints token, top-k experts, and gates. |

**Code objects to develop or reference:**
- `expert behavior report`
- `caution checklist`

The listing should be runnable or very close to runnable. Keep it shorter than the full source file by showing the smallest fragment that teaches the new idea. Full code belongs in the chapter code directory.

## 7. Code development plan

**Primary code location:** `ch11/01_main-chapter-code/ with experiment configs, run scripts, result parsers, and plotting utilities.`

1. Start from the previous section's tested code, not from a fresh implementation.
2. Add only the minimal new object or function needed for **Interpreting expert behavior carefully**.
3. Write a CPU smoke test using the mini-example: Look at expert IDs selected for a short prompt and compare across positions or token types.
4. Preserve the chapter-level invariant: Every comparison must hold dataset, token budget, optimizer settings, and evaluation protocol fixed unless the section says otherwise.
5. If a helper becomes reusable across later chapters, mark it with a comment such as `# promoted later to common/` but do not prematurely reorganize the codebase during the section draft.

**Expected code deliverable:** trace_prompt_routing.py that prints token, top-k experts, and gates.

## 8. Diagnostic requirement

Generate a routing trace table and a usage heatmap.

Make the diagnostic falsifiable. A reader should be able to intentionally break one line of code and see this diagnostic fail. The diagnostic may be an assertion, a tiny printed table, a unit-test-like function, or a generated plot depending on the section.

Suggested diagnostic checks:

- Verify the output shape and dtype that the section claims.
- Verify at least one edge case from the table.
- Verify the routing/load/score quantity named in the local objective.
- Use a fixed random seed when comparing against a reference implementation.

## 9. Common inaccuracies to avoid

- Do not over-interpret expert specialization from a tiny dataset.
- Do not compare models with different token budgets without labeling the caveat.
- Do not report only final loss; include routing health.

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
- [ ] The final paragraph bridges to: Chapter 11.6 - Chapter summary and handoff.

## 13. Ready-to-use prompt for the section-development chat

```text
Develop Chapter 11.5, "Interpreting expert behavior carefully", for MoE Models from Scratch using this brief. Produce LaTeX-first section prose and update only the standalone artifact wrappers listed here. Follow the required flow: problem opening -> visual anchor -> tensor/math mechanics -> implementation listing -> diagnostic -> bridge. Keep all figures/tables/listings/equations included via \input and preserve the color/theme contract.
```
