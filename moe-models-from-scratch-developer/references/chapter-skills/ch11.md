---
name: moe-ch11-developer
description: use when developing chapter 11 of moe models from scratch, training, diagnostics, and controlled experiments, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 11 developer: Training, diagnostics, and controlled experiments

Use this skill-style markdown when working on Chapter 11 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 11.1 | Experiment design for a from-scratch book | `../sections/ch11/01-experiment-design-for-a-from-scratch-book.skill.md` | Check that every experiment saves config, seed, logs, and git/code snapshot note. |
| 11.2 | Dataset preparation and reproducibility | `../sections/ch11/02-dataset-preparation-and-reproducibility.skill.md` | Print token counts, split sizes, and a decoded sample from each split. |
| 11.3 | Loss curves and routing dashboards | `../sections/ch11/03-loss-curves-and-routing-dashboards.skill.md` | Save dashboard figures through LaTeX wrappers, never raw includegraphics in prose. |
| 11.4 | Ablation matrix: dense, top-1, top-2, shared, and bias-balanced | `../sections/ch11/04-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.skill.md` | Flag any run with unstable loss, high drop rate, or extreme expert collapse. |
| 11.5 | Interpreting expert behavior carefully | `../sections/ch11/05-interpreting-expert-behavior-carefully.skill.md` | Generate a routing trace table and a usage heatmap. |
| 11.6 | Chapter summary and handoff | `../sections/ch11/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: identify whether a routing issue is code, loss, capacity, or data related. |

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

# Chapter 11 development packet - Training, diagnostics, and controlled experiments

Use the model to answer concrete questions about routing, balance, and sparse capacity.

## Chapter role

Run controlled experiments and teach the reader how to interpret MoE diagnostics carefully.

## Reader trajectory

- Enters: Reader has a full model and needs evidence rather than anecdotes.
- Leaves: Reader has reproducible runs, ablations, diagnostic plots, and caution around expert-behavior interpretation.
- Invariant: Every comparison must hold dataset, token budget, optimizer settings, and evaluation protocol fixed unless the section says otherwise.
- Code area: `ch11/01_main-chapter-code/ with experiment configs, run scripts, result parsers, and plotting utilities.`

## Section order and brief paths

- **11.1 Experiment design for a from-scratch book** - `section_development_briefs/ch11/01-experiment-design-for-a-from-scratch-book.md`
  - Objective: Set realistic expectations for small-data experiments and define what can and cannot be concluded.
  - Diagnostic: Check that every experiment saves config, seed, logs, and git/code snapshot note.
- **11.2 Dataset preparation and reproducibility** - `section_development_briefs/ch11/02-dataset-preparation-and-reproducibility.md`
  - Objective: Make dataset setup deterministic and lightweight enough for readers to rerun.
  - Diagnostic: Print token counts, split sizes, and a decoded sample from each split.
- **11.3 Loss curves and routing dashboards** - `section_development_briefs/ch11/03-loss-curves-and-routing-dashboards.md`
  - Objective: Create consistent plots that make model behavior inspectable after every run.
  - Diagnostic: Save dashboard figures through LaTeX wrappers, never raw includegraphics in prose.
- **11.4 Ablation matrix: dense, top-1, top-2, shared, and bias-balanced** - `section_development_briefs/ch11/04-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.md`
  - Objective: Plan the central comparison table for the book without pretending small runs settle model quality.
  - Diagnostic: Flag any run with unstable loss, high drop rate, or extreme expert collapse.
- **11.5 Interpreting expert behavior carefully** - `section_development_briefs/ch11/05-interpreting-expert-behavior-carefully.md`
  - Objective: Teach readers to inspect expert usage without overclaiming that tiny experts learned semantic roles.
  - Diagnostic: Generate a routing trace table and a usage heatmap.
- **11.6 Chapter summary and handoff** - `section_development_briefs/ch11/06-chapter-summary-and-handoff.md`
  - Objective: Close the experimental part by identifying what the book has demonstrated mechanically.
  - Diagnostic: Reader checkpoint: identify whether a routing issue is code, loss, capacity, or data related.

## Chapter-level pitfalls

- Do not over-interpret expert specialization from a tiny dataset.
- Do not compare models with different token budgets without labeling the caveat.
- Do not report only final loss; include routing health.

## Chapter artifact style

Use generated PDF plots for loss curves, load histograms, and ablation dashboards. Tables should carry experiment controls.
