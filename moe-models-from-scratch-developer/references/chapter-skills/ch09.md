---
name: moe-ch09-developer
description: use when developing chapter 9 of moe models from scratch, auxiliary-loss-free load balancing, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 9 developer: Auxiliary-loss-free load balancing

Use this skill-style markdown when working on Chapter 9 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 9.1 | The limitation of auxiliary balancing | `../sections/ch09/01-the-limitation-of-auxiliary-balancing.skill.md` | Compare LM loss and load balance separately, not only total loss. |
| 9.2 | Router bias as non-trainable state | `../sections/ch09/02-router-bias-as-non-trainable-state.skill.md` | Assert router_bias.requires_grad is false and optimizer does not update it. |
| 9.3 | Biased selection and unbiased combine | `../sections/ch09/03-biased-selection-and-unbiased-combine.skill.md` | Unit test that changing bias can change expert IDs while gate values still come from raw scores. |
| 9.4 | Dynamic bias update from expert load | `../sections/ch09/04-dynamic-bias-update-from-expert-load.skill.md` | Track bias values over training beside expert loads. |
| 9.5 | Comparing balancing methods | `../sections/ch09/05-comparing-balancing-methods.skill.md` | Produce a table with LM loss, aux loss if used, load balance score, entropy, and drop rate. |
| 9.6 | Chapter summary and handoff | `../sections/ch09/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: explain why bias should not be included in combine weights. |

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

# Chapter 9 development packet - Auxiliary-loss-free load balancing

Replace auxiliary balancing with a router-bias mechanism that affects selection but not combine weights.

## Chapter role

Replace auxiliary balancing with auxiliary-loss-free router-bias balancing for the final reference model.

## Reader trajectory

- Enters: Reader understands auxiliary balancing and the MiniDeepSeekMoE layer contract.
- Leaves: Reader can implement non-trainable router bias updates, biased selection, and unbiased combine weights.
- Invariant: Router bias affects expert selection only; final combine weights are computed from unbiased selected scores.
- Code area: `ch09/01_main-chapter-code/ with RouterBiasState, update rules, and balancing-method comparisons.`

## Section order and brief paths

- **9.1 The limitation of auxiliary balancing** - `section_development_briefs/ch09/01-the-limitation-of-auxiliary-balancing.md`
  - Objective: Explain why a separate balancing mechanism is attractive after readers have implemented auxiliary losses.
  - Diagnostic: Compare LM loss and load balance separately, not only total loss.
- **9.2 Router bias as non-trainable state** - `section_development_briefs/ch09/02-router-bias-as-non-trainable-state.md`
  - Objective: Define router bias as a per-expert control signal updated outside backpropagation.
  - Diagnostic: Assert router_bias.requires_grad is false and optimizer does not update it.
- **9.3 Biased selection and unbiased combine** - `section_development_briefs/ch09/03-biased-selection-and-unbiased-combine.md`
  - Objective: Implement the central invariant of the final reference model.
  - Diagnostic: Unit test that changing bias can change expert IDs while gate values still come from raw scores.
- **9.4 Dynamic bias update from expert load** - `section_development_briefs/ch09/04-dynamic-bias-update-from-expert-load.md`
  - Objective: Add a simple no-gradient update that nudges underused experts up and overused experts down.
  - Diagnostic: Track bias values over training beside expert loads.
- **9.5 Comparing balancing methods** - `section_development_briefs/ch09/05-comparing-balancing-methods.md`
  - Objective: Design a fair chapter experiment comparing no balance, auxiliary loss, and router-bias balancing.
  - Diagnostic: Produce a table with LM loss, aux loss if used, load balance score, entropy, and drop rate.
- **9.6 Chapter summary and handoff** - `section_development_briefs/ch09/06-chapter-summary-and-handoff.md`
  - Objective: Lock the final router behavior and document the invariants required by the complete model.
  - Diagnostic: Reader checkpoint: explain why bias should not be included in combine weights.

## Chapter-level pitfalls

- Do not let the bias receive gradients.
- Do not use biased scores for final weighted combination.
- Do not update bias from a single tiny batch without explaining noise and smoothing options.

## Chapter artifact style

Use cyan for unbiased router scores, gold for bias offsets, active green for selected routes, and red only for imbalanced loads.
