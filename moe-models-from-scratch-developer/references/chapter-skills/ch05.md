---
name: moe-ch05-developer
description: use when developing chapter 5 of moe models from scratch, top-2 routing and weighted expert combination, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 5 developer: Top-2 routing and weighted expert combination

Use this skill-style markdown when working on Chapter 5 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 5.1 | Why top-2 changes the routing story | `../sections/ch05/01-why-top-2-changes-the-routing-story.skill.md` | Compare active expert calls per token for K=1 and K=2. |
| 5.2 | Normalizing selected router scores | `../sections/ch05/02-normalizing-selected-router-scores.skill.md` | Assert torch.allclose(gates.sum(-1), ones). |
| 5.3 | Dispatch for two expert paths per token | `../sections/ch05/03-dispatch-for-two-expert-paths-per-token.skill.md` | Check output changes when gates are manually swapped. |
| 5.4 | Comparing top-1 and top-2 diagnostics | `../sections/ch05/04-comparing-top-1-and-top-2-diagnostics.skill.md` | Save a comparison table and one histogram per routing mode. |
| 5.5 | Numerical stability in top-k gates | `../sections/ch05/05-numerical-stability-in-top-k-gates.skill.md` | Unit tests for finite gates and gradients under small scores. |
| 5.6 | Chapter summary and handoff | `../sections/ch05/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: explain why gates sum to one after selecting top-k only. |

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

# Chapter 5 development packet - Top-2 routing and weighted expert combination

Generalize sparse routing so each token can combine two expert transformations.

## Chapter role

Extend routing to top-2 so the reader sees weighted expert combination and prepares for MiniDeepSeekMoE top-k behavior.

## Reader trajectory

- Enters: Reader can run top-1 routing and understand expert buckets.
- Leaves: Reader can normalize selected router scores, dispatch two paths per token, and compare top-1/top-2 diagnostics.
- Invariant: A token may create k dispatch records, but the final combined output still has one vector per input token.
- Code area: `ch05/01_main-chapter-code/ with TopKRouter(k=2), Top2MoELayer, combine weights, and comparisons.`

## Section order and brief paths

- **5.1 Why top-2 changes the routing story** - `section_development_briefs/ch05/01-why-top-2-changes-the-routing-story.md`
  - Objective: Explain top-2 routing as sparse ensemble behavior at the token level.
  - Diagnostic: Compare active expert calls per token for K=1 and K=2.
- **5.2 Normalizing selected router scores** - `section_development_briefs/ch05/02-normalizing-selected-router-scores.md`
  - Objective: Turn top-2 scores into gates that sum to one for each token.
  - Diagnostic: Assert torch.allclose(gates.sum(-1), ones).
- **5.3 Dispatch for two expert paths per token** - `section_development_briefs/ch05/03-dispatch-for-two-expert-paths-per-token.md`
  - Objective: Adapt the dispatch loop so each selected expert path contributes to the same output row.
  - Diagnostic: Check output changes when gates are manually swapped.
- **5.4 Comparing top-1 and top-2 diagnostics** - `section_development_briefs/ch05/04-comparing-top-1-and-top-2-diagnostics.md`
  - Objective: Use the same metrics to show how K changes load, drop rate, and routing entropy.
  - Diagnostic: Save a comparison table and one histogram per routing mode.
- **5.5 Numerical stability in top-k gates** - `section_development_briefs/ch05/05-numerical-stability-in-top-k-gates.md`
  - Objective: Prevent gate normalization edge cases before they become training bugs.
  - Diagnostic: Unit tests for finite gates and gradients under small scores.
- **5.6 Chapter summary and handoff** - `section_development_briefs/ch05/06-chapter-summary-and-handoff.md`
  - Objective: Lock in the top-2 routing contract used by MiniDeepSeekMoE.
  - Diagnostic: Reader checkpoint: explain why gates sum to one after selecting top-k only.

## Chapter-level pitfalls

- Do not normalize over all experts after top-k; normalize only selected scores for combine.
- Do not lose token identity when one token has two expert paths.
- Mention numerical stability before training failures appear.

## Chapter artifact style

Use paired active green routes for top-2 and gold tags for selected top-k slots. Make weighted combine visible.
