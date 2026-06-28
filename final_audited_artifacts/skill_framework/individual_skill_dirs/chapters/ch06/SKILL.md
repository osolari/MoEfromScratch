---
name: moe-ch06-developer
description: use when developing chapter 6 of moe models from scratch, vectorized dispatch, capacity, and routing efficiency, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 6 developer: Vectorized dispatch, capacity, and routing efficiency

Use this skill-style markdown when working on Chapter 6 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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


## Chapter sections

| Section | Title | Section skill file | Diagnostic |
|---:|---|---|---|
| 6.1 | Flattened tokens as the dispatch unit | `../sections/ch06/01-flattened-tokens-as-the-dispatch-unit.skill.md` | Round-trip flatten/unflatten equality check. |
| 6.2 | Expert batch construction | `../sections/ch06/02-expert-batch-construction.skill.md` | Ensure each accepted route has exactly one expert slot. |
| 6.3 | Capacity factors and overflow policy | `../sections/ch06/03-capacity-factors-and-overflow-policy.skill.md` | Log overflow route count and overflow fraction. |
| 6.4 | Unpacking and weighted combine | `../sections/ch06/04-unpacking-and-weighted-combine.skill.md` | Compare vectorized output to naive output when capacity is large enough for no overflow. |
| 6.5 | Equivalence tests against the naive layer | `../sections/ch06/05-equivalence-tests-against-the-naive-layer.skill.md` | Fail if max_abs_diff exceeds tolerance in no-overflow settings. |
| 6.6 | Chapter summary and handoff | `../sections/ch06/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: identify where dropped routes enter the output calculation. |

## Chapter workflow

1. Confirm the target section and load its section skill file.
2. Preserve the previous/next handoff chain from the section brief.
3. Keep chapter code changes cumulative and testable.
4. Do not import future mechanisms before their planned chapter unless explicitly labelled as a preview.
5. End each section by setting up the next section's unresolved issue.

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


## Chapter packet

# Chapter 6 development packet - Vectorized dispatch, capacity, and routing efficiency

Move from readable loops to scalable tensor operations without changing the MoE math.

## Chapter role

Replace naive dispatch with vectorized token packing, capacity-aware expert batches, and equivalence tests.

## Reader trajectory

- Enters: Reader can implement top-2 naively and understands the expected outputs.
- Leaves: Reader can build vectorized dispatch tensors and prove equivalence against the naive reference layer.
- Invariant: Vectorization may change order and layout, but it must not change mathematical output when no overflow occurs.
- Code area: `ch06/01_main-chapter-code/ with vectorized_dispatch.py, capacity utilities, and equivalence tests.`

## Section order and brief paths

- **6.1 Flattened tokens as the dispatch unit** - `section_development_briefs/ch06/01-flattened-tokens-as-the-dispatch-unit.md`
  - Objective: Standardize on N=B*T flattened tokens so routing code ignores batch layout until the final reshape.
  - Diagnostic: Round-trip flatten/unflatten equality check.
- **6.2 Expert batch construction** - `section_development_briefs/ch06/02-expert-batch-construction.md`
  - Objective: Build dense per-expert mini-batches from sparse token assignments.
  - Diagnostic: Ensure each accepted route has exactly one expert slot.
- **6.3 Capacity factors and overflow policy** - `section_development_briefs/ch06/03-capacity-factors-and-overflow-policy.md`
  - Objective: Explain how capacity controls memory and what the implementation does with overflow routes.
  - Diagnostic: Log overflow route count and overflow fraction.
- **6.4 Unpacking and weighted combine** - `section_development_briefs/ch06/04-unpacking-and-weighted-combine.md`
  - Objective: Scatter expert-batch outputs back to token rows and apply route weights correctly.
  - Diagnostic: Compare vectorized output to naive output when capacity is large enough for no overflow.
- **6.5 Equivalence tests against the naive layer** - `section_development_briefs/ch06/05-equivalence-tests-against-the-naive-layer.md`
  - Objective: Prove the vectorized implementation matches the simple implementation in the no-overflow case.
  - Diagnostic: Fail if max_abs_diff exceeds tolerance in no-overflow settings.
- **6.6 Chapter summary and handoff** - `section_development_briefs/ch06/06-chapter-summary-and-handoff.md`
  - Objective: Summarize the efficient routing pipeline and the new capacity diagnostics.
  - Diagnostic: Reader checkpoint: identify where dropped routes enter the output calculation.

## Chapter-level pitfalls

- Do not introduce performance claims without equivalence tests.
- Do not let capacity logic silently change gate normalization.
- Keep token index, expert index, and slot index visibly separate.

## Chapter artifact style

Use slot grids, packed expert batches, and muted gray for inactive capacity slots. The diagram should clarify indices.
