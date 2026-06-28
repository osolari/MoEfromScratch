---
name: moe-ch04-developer
description: use when developing chapter 4 of moe models from scratch, top-1 routing and switch-style dispatch, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 4 developer: Top-1 routing and Switch-style dispatch

Use this skill-style markdown when working on Chapter 4 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 4.1 | Why top-1 routing is the simplest sparse case | `../sections/ch04/01-why-top-1-routing-is-the-simplest-sparse-case.skill.md` | Verify each token has one expert and one scalar gate. |
| 4.2 | Assignment masks and expert buckets | `../sections/ch04/02-assignment-masks-and-expert-buckets.skill.md` | Sum the mask across experts to confirm each token is assigned once. |
| 4.3 | Dispatching tokens to selected experts | `../sections/ch04/03-dispatching-tokens-to-selected-experts.skill.md` | Assert output rows return to the original token order. |
| 4.4 | Capacity and dropped tokens | `../sections/ch04/04-capacity-and-dropped-tokens.skill.md` | Report dropped_token_count and per-expert accepted counts. |
| 4.5 | Load histograms and failure modes | `../sections/ch04/05-load-histograms-and-failure-modes.skill.md` | Save a histogram and a warning if max load is much larger than average load. |
| 4.6 | Chapter summary and handoff | `../sections/ch04/06-chapter-summary-and-handoff.skill.md` | Compare validation loss smoke run with dense baseline, without claiming quality superiority. |

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

# Chapter 4 development packet - Top-1 routing and Switch-style dispatch

Build the simplest sparse router and expose the expert-load problem.

## Chapter role

Teach top-1 sparse dispatch as the simplest end-to-end MoE routing case.

## Reader trajectory

- Enters: Reader can compute router scores and naive dispatch for selected experts.
- Leaves: Reader can implement Switch-style top-1 routing, expert buckets, capacity, and dropped-token diagnostics.
- Invariant: Each token chooses exactly one routed expert before capacity constraints are applied.
- Code area: `ch04/01_main-chapter-code/ with Top1Router, Top1MoELayer, capacity checks, and histograms.`

## Section order and brief paths

- **4.1 Why top-1 routing is the simplest sparse case** - `section_development_briefs/ch04/01-why-top-1-routing-is-the-simplest-sparse-case.md`
  - Objective: Use one-expert-per-token routing to reduce the dispatch problem to assignment plus combine.
  - Diagnostic: Verify each token has one expert and one scalar gate.
- **4.2 Assignment masks and expert buckets** - `section_development_briefs/ch04/02-assignment-masks-and-expert-buckets.md`
  - Objective: Convert token expert IDs into per-expert token groups.
  - Diagnostic: Sum the mask across experts to confirm each token is assigned once.
- **4.3 Dispatching tokens to selected experts** - `section_development_briefs/ch04/03-dispatching-tokens-to-selected-experts.md`
  - Objective: Run each expert only on the tokens assigned to it and scatter outputs back to token order.
  - Diagnostic: Assert output rows return to the original token order.
- **4.4 Capacity and dropped tokens** - `section_development_briefs/ch04/04-capacity-and-dropped-tokens.md`
  - Objective: Introduce the capacity factor and the consequences of too many tokens choosing the same expert.
  - Diagnostic: Report dropped_token_count and per-expert accepted counts.
- **4.5 Load histograms and failure modes** - `section_development_briefs/ch04/05-load-histograms-and-failure-modes.md`
  - Objective: Make expert collapse and underuse visible with simple diagnostics.
  - Diagnostic: Save a histogram and a warning if max load is much larger than average load.
- **4.6 Chapter summary and handoff** - `section_development_briefs/ch04/06-chapter-summary-and-handoff.md`
  - Objective: Consolidate top-1 routing as a working sparse layer and name its limitations.
  - Diagnostic: Compare validation loss smoke run with dense baseline, without claiming quality superiority.

## Chapter-level pitfalls

- Do not hide dropped tokens; visualize them and decide the residual/skip policy.
- Do not make top-1 look like final model quality; it is a teaching milestone.
- Distinguish assignment counts from probability mass.

## Chapter artifact style

Use active green for exactly one selected expert per token and imbalance red for drops or overload.
