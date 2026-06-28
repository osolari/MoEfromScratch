---
name: moe-ch01-developer
description: use when developing chapter 1 of moe models from scratch, from dense compute to conditional compute, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 1 developer: From dense compute to conditional compute

Use this skill-style markdown when working on Chapter 1 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 1.1 | The dense FFN bottleneck | `../sections/ch01/01-the-dense-ffn-bottleneck.skill.md` | A small cost table proving that increasing H increases every token path. |
| 1.2 | Conditional compute as the central idea | `../sections/ch01/02-conditional-compute-as-the-central-idea.skill.md` | Compute the active fraction for E=4, K=2 and E=16, K=2. |
| 1.3 | A tiny routing story | `../sections/ch01/03-a-tiny-routing-story.skill.md` | Check that gates for each token sum to one after top-k normalization. |
| 1.4 | What from scratch means for this book | `../sections/ch01/04-what-from-scratch-means-for-this-book.skill.md` | Checklist that every chapter must include shapes, a code path, and a verification artifact. |
| 1.5 | The MiniDeepSeekMoE build ladder | `../sections/ch01/05-the-minideepseekmoe-build-ladder.skill.md` | Milestone checklist that marks which diagnostics appear by each chapter. |
| 1.6 | Chapter summary and handoff | `../sections/ch01/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: identify which part of the dense model will be replaced by MoE. |

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

# Chapter 1 development packet - From dense compute to conditional compute

Motivate MoE from the dense FFN bottleneck and establish the build ladder.

## Chapter role

Motivate MoE by making the dense FFN bottleneck visible before any router is introduced.

## Reader trajectory

- Enters: Reader knows basic decoder blocks at a high level but has not yet implemented a model in this book.
- Leaves: Reader understands the build ladder and can explain why conditional compute targets the FFN path.
- Invariant: The decoder interface remains x -> y with shape (B, T, D) even when compute becomes conditional.
- Code area: `ch01/01_main-chapter-code/ with small notebooks or scripts for cost estimates and hand-built routing tensors.`

## Section order and brief paths

- **1.1 The dense FFN bottleneck** - `section_development_briefs/ch01/01-the-dense-ffn-bottleneck.md`
  - Objective: Show that the dense feed-forward block is the natural place to introduce sparsity because every token pays for every hidden unit.
  - Diagnostic: A small cost table proving that increasing H increases every token path.
- **1.2 Conditional compute as the central idea** - `section_development_briefs/ch01/02-conditional-compute-as-the-central-idea.md`
  - Objective: Introduce MoE as selective FFN computation rather than a mysterious new model family.
  - Diagnostic: Compute the active fraction for E=4, K=2 and E=16, K=2.
- **1.3 A tiny routing story** - `section_development_briefs/ch01/03-a-tiny-routing-story.md`
  - Objective: Give readers a concrete token-by-token routing example before any model code appears.
  - Diagnostic: Check that gates for each token sum to one after top-k normalization.
- **1.4 What from scratch means for this book** - `section_development_briefs/ch01/04-what-from-scratch-means-for-this-book.md`
  - Objective: Define the implementation boundary: small readable modules, explicit tensors, and diagnostics before optimization.
  - Diagnostic: Checklist that every chapter must include shapes, a code path, and a verification artifact.
- **1.5 The MiniDeepSeekMoE build ladder** - `section_development_briefs/ch01/05-the-minideepseekmoe-build-ladder.md`
  - Objective: Preview the book path from dense baseline to shared experts, fine-grained experts, and router-bias balancing.
  - Diagnostic: Milestone checklist that marks which diagnostics appear by each chapter.
- **1.6 Chapter summary and handoff** - `section_development_briefs/ch01/06-chapter-summary-and-handoff.md`
  - Objective: Close the motivation chapter with the vocabulary and constraints the reader will reuse.
  - Diagnostic: Reader checkpoint: identify which part of the dense model will be replaced by MoE.

## Chapter-level pitfalls

- Do not imply that MoE reduces total parameters; it reduces activated compute per token for a larger parameter bank.
- Do not start with production distributed systems; keep the first chapter concrete and tensor-sized.
- Do not call routing magic; show an explicit score table and top-k choices.

## Chapter artifact style

Use simple blocks and arrows. Prefer token dots, a highlighted dense FFN path, and a roadmap ladder. No heatmaps yet.
