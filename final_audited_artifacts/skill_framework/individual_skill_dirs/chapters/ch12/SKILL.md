---
name: moe-ch12-developer
description: use when developing chapter 12 of moe models from scratch, inference, performance, and scaling beyond the toy model, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 12 developer: Inference, performance, and scaling beyond the toy model

Use this skill-style markdown when working on Chapter 12 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 12.1 | Autoregressive inference with sparse FFNs | `../sections/ch12/01-autoregressive-inference-with-sparse-ffns.skill.md` | Print selected experts for each generated token in a short sample. |
| 12.2 | Batching routed tokens at inference | `../sections/ch12/02-batching-routed-tokens-at-inference.skill.md` | Histogram expert batch sizes over a generated sequence. |
| 12.3 | Compute, memory, and active-parameter accounting | `../sections/ch12/03-compute-memory-and-active-parameter-accounting.skill.md` | Check estimates against model.count_parameters breakdown. |
| 12.4 | Expert parallelism and all-to-all communication | `../sections/ch12/04-expert-parallelism-and-all-to-all-communication.skill.md` | Thought experiment table estimating routed activation traffic for a small config. |
| 12.5 | Mapping the book model to production MoE families | `../sections/ch12/05-mapping-the-book-model-to-production-moe-families.skill.md` | Reader checkpoint: identify which chapter implemented each production analogue. |
| 12.6 | Book summary and next steps | `../sections/ch12/06-book-summary-and-next-steps.skill.md` | Final self-test: build, train smoke, inspect routing, sample text, and explain limitations. |

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

# Chapter 12 development packet - Inference, performance, and scaling beyond the toy model

Connect the from-scratch implementation to systems concerns without turning the book into a distributed-systems text.

## Chapter role

Explain inference and scaling implications after the from-scratch model exists, without turning the book into a systems textbook.

## Reader trajectory

- Enters: Reader can train and inspect MiniDeepSeekMoE.
- Leaves: Reader understands sparse inference accounting, batching, expert parallelism concepts, and how the teaching model maps to production families.
- Invariant: Inference still produces one next-token distribution per sequence step even though expert computation is sparse internally.
- Code area: `ch12/01_main-chapter-code/ with inference benchmarks, active-parameter calculators, and conceptual scaling demos.`

## Section order and brief paths

- **12.1 Autoregressive inference with sparse FFNs** - `section_development_briefs/ch12/01-autoregressive-inference-with-sparse-ffns.md`
  - Objective: Explain what changes and what stays the same when a trained MoE model generates text one token at a time.
  - Diagnostic: Print selected experts for each generated token in a short sample.
- **12.2 Batching routed tokens at inference** - `section_development_briefs/ch12/02-batching-routed-tokens-at-inference.md`
  - Objective: Show why MoE inference wants tokens for the same expert to be grouped efficiently.
  - Diagnostic: Histogram expert batch sizes over a generated sequence.
- **12.3 Compute, memory, and active-parameter accounting** - `section_development_briefs/ch12/03-compute-memory-and-active-parameter-accounting.md`
  - Objective: Give readers a sober way to discuss total parameters, active parameters, and practical memory costs.
  - Diagnostic: Check estimates against model.count_parameters breakdown.
- **12.4 Expert parallelism and all-to-all communication** - `section_development_briefs/ch12/04-expert-parallelism-and-all-to-all-communication.md`
  - Objective: Explain the systems picture conceptually while keeping implementation out of scope.
  - Diagnostic: Thought experiment table estimating routed activation traffic for a small config.
- **12.5 Mapping the book model to production MoE families** - `section_development_briefs/ch12/05-mapping-the-book-model-to-production-moe-families.md`
  - Objective: Connect MiniDeepSeekMoE pieces to broader MoE designs while staying honest about omitted details.
  - Diagnostic: Reader checkpoint: identify which chapter implemented each production analogue.
- **12.6 Book summary and next steps** - `section_development_briefs/ch12/06-book-summary-and-next-steps.md`
  - Objective: End with a coherent picture of MoE as a route-execute-combine layer embedded in a decoder.
  - Diagnostic: Final self-test: build, train smoke, inspect routing, sample text, and explain limitations.

## Chapter-level pitfalls

- Do not imply the toy code is production efficient.
- Do not equate fewer active parameters with lower wall-clock time without batching and communication context.
- Keep all production-model comparisons clearly labeled as mapping, not replication.

## Chapter artifact style

Use compute-accounting diagrams and system schematics. Keep distributed-system diagrams conceptual and clearly labeled.
