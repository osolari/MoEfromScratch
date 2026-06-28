---
name: moe-ch03-developer
description: use when developing chapter 3 of moe models from scratch, experts, routers, and the first moe layer, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 3 developer: Experts, routers, and the first MoE layer

Use this skill-style markdown when working on Chapter 3 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 3.1 | Expert MLPs as named FFNs | `../sections/ch03/01-expert-mlps-as-named-ffns.skill.md` | Run all experts on the same token and compare output shapes. |
| 3.2 | Router scores and tensor shapes | `../sections/ch03/02-router-scores-and-tensor-shapes.skill.md` | Assert that the expert dimension equals n_experts and token dimension equals B*T. |
| 3.3 | Top-k selection without dispatch | `../sections/ch03/03-top-k-selection-without-dispatch.skill.md` | Verify that every token has exactly K selected expert IDs. |
| 3.4 | Naive token-by-token dispatch | `../sections/ch03/04-naive-token-by-token-dispatch.skill.md` | Compare output shape to dense FFN output and inspect gates per token. |
| 3.5 | Shape and gradient checks | `../sections/ch03/05-shape-and-gradient-checks.skill.md` | Count selected expert IDs and check nonzero gradients for selected expert parameters. |
| 3.6 | Chapter summary and handoff | `../sections/ch03/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: identify where routing, expert computation, and combine happen in code. |

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

# Chapter 3 development packet - Experts, routers, and the first MoE layer

Introduce the MoE layer as a transparent replacement for the dense FFN.

## Chapter role

Introduce experts and routers as explicit replacements for a dense FFN, first with naive readable code.

## Reader trajectory

- Enters: Reader has a dense FFN and can train a tiny model.
- Leaves: Reader can compute router scores, select experts, dispatch tokens naively, and verify shapes/gradients.
- Invariant: The first MoE layer must accept x with shape (B, T, D) and return y with the same shape plus routing metadata.
- Code area: `ch03/01_main-chapter-code/ with Router, ExpertMLP, and NaiveMoELayer prototypes.`

## Section order and brief paths

- **3.1 Expert MLPs as named FFNs** - `section_development_briefs/ch03/01-expert-mlps-as-named-ffns.md`
  - Objective: Demystify experts by deriving them directly from the dense FFN module.
  - Diagnostic: Run all experts on the same token and compare output shapes.
- **3.2 Router scores and tensor shapes** - `section_development_briefs/ch03/02-router-scores-and-tensor-shapes.md`
  - Objective: Define router logits, router probabilities, and the flattening convention used throughout the book.
  - Diagnostic: Assert that the expert dimension equals n_experts and token dimension equals B*T.
- **3.3 Top-k selection without dispatch** - `section_development_briefs/ch03/03-top-k-selection-without-dispatch.md`
  - Objective: Separate the selection problem from expert execution so readers can inspect router behavior first.
  - Diagnostic: Verify that every token has exactly K selected expert IDs.
- **3.4 Naive token-by-token dispatch** - `section_development_briefs/ch03/04-naive-token-by-token-dispatch.md`
  - Objective: Implement dispatch with loops first so the control flow is unmistakable.
  - Diagnostic: Compare output shape to dense FFN output and inspect gates per token.
- **3.5 Shape and gradient checks** - `section_development_briefs/ch03/05-shape-and-gradient-checks.md`
  - Objective: Make the first MoE layer testable before introducing more routing variants.
  - Diagnostic: Count selected expert IDs and check nonzero gradients for selected expert parameters.
- **3.6 Chapter summary and handoff** - `section_development_briefs/ch03/06-chapter-summary-and-handoff.md`
  - Objective: Summarize the first complete MoE layer and prepare for routing variants.
  - Diagnostic: Reader checkpoint: identify where routing, expert computation, and combine happen in code.

## Chapter-level pitfalls

- Do not vectorize too early; this chapter prioritizes correctness and observability.
- Do not confuse router logits, probabilities, selected gates, and expert outputs.
- Always flatten tokens deliberately and restore batch/time shape at the end.

## Chapter artifact style

Use router cyan and expert purple heavily. Show matrices with N tokens by E experts and preserve token identity in diagrams.
