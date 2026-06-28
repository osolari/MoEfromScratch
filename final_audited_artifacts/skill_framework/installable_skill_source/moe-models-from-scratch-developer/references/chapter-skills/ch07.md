---
name: moe-ch07-developer
description: use when developing chapter 7 of moe models from scratch, router training and load-balancing losses, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 7 developer: Router training and load-balancing losses

Use this skill-style markdown when working on Chapter 7 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 7.1 | Expert imbalance as a training problem | `../sections/ch07/01-expert-imbalance-as-a-training-problem.skill.md` | Report max_load/mean_load and number of empty experts. |
| 7.2 | Auxiliary load-balancing loss | `../sections/ch07/02-auxiliary-load-balancing-loss.skill.md` | Check loss is lower for balanced synthetic routing than collapsed routing. |
| 7.3 | Integrating auxiliary loss into training | `../sections/ch07/03-integrating-auxiliary-loss-into-training.skill.md` | Log individual losses separately so balancing cannot hide LM degradation. |
| 7.4 | Router score scale and z-loss | `../sections/ch07/04-router-score-scale-and-z-loss.skill.md` | Track router score max, entropy, and z-loss over training. |
| 7.5 | Routing dashboards and training logs | `../sections/ch07/05-routing-dashboards-and-training-logs.skill.md` | Generate a dashboard PDF or image after a short smoke run. |
| 7.6 | Chapter summary and handoff | `../sections/ch07/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: explain why aux_loss must be logged separately from LM loss. |

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

# Chapter 7 development packet - Router training and load-balancing losses

Teach the router to avoid expert collapse before moving to auxiliary-loss-free balancing.

## Chapter role

Show that routers are trainable systems with failure modes and balancing objectives, not just argmax functions.

## Reader trajectory

- Enters: Reader can route and dispatch tokens but has seen imbalance and overflow.
- Leaves: Reader can add an auxiliary load-balancing loss, z-loss, and routing dashboards to the training loop.
- Invariant: Balancing losses influence router training but should not change the model forward interface for inference.
- Code area: `ch07/01_main-chapter-code/ with losses.py, training integration, and log/dashboard generation.`

## Section order and brief paths

- **7.1 Expert imbalance as a training problem** - `section_development_briefs/ch07/01-expert-imbalance-as-a-training-problem.md`
  - Objective: Show that a technically correct router can still collapse onto a small number of experts.
  - Diagnostic: Report max_load/mean_load and number of empty experts.
- **7.2 Auxiliary load-balancing loss** - `section_development_briefs/ch07/02-auxiliary-load-balancing-loss.md`
  - Objective: Implement the classic balancing baseline as a transparent, measurable loss term.
  - Diagnostic: Check loss is lower for balanced synthetic routing than collapsed routing.
- **7.3 Integrating auxiliary loss into training** - `section_development_briefs/ch07/03-integrating-auxiliary-loss-into-training.md`
  - Objective: Add routing losses to the model output dictionary without hiding the main language-model loss.
  - Diagnostic: Log individual losses separately so balancing cannot hide LM degradation.
- **7.4 Router score scale and z-loss** - `section_development_briefs/ch07/04-router-score-scale-and-z-loss.md`
  - Objective: Introduce a simple regularizer for overly large router logits or scores.
  - Diagnostic: Track router score max, entropy, and z-loss over training.
- **7.5 Routing dashboards and training logs** - `section_development_briefs/ch07/05-routing-dashboards-and-training-logs.md`
  - Objective: Create the standard diagnostic views used for every later MoE experiment.
  - Diagnostic: Generate a dashboard PDF or image after a short smoke run.
- **7.6 Chapter summary and handoff** - `section_development_briefs/ch07/06-chapter-summary-and-handoff.md`
  - Objective: Frame auxiliary balancing as the baseline that auxiliary-loss-free balancing will later improve on.
  - Diagnostic: Reader checkpoint: explain why aux_loss must be logged separately from LM loss.

## Chapter-level pitfalls

- Do not claim auxiliary loss is free; it trades off with task loss and needs weighting.
- Do not use only mean load; include max load and entropy-like views.
- Keep routing metrics detached where appropriate to avoid accidental gradients.

## Chapter artifact style

Use diagnostic plots as PDF placeholders when the artifact is meant to come from code. Use red carefully for imbalance.
