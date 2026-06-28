---
name: moe-ch08-developer
description: use when developing chapter 8 of moe models from scratch, shared experts and fine-grained routed experts, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 8 developer: Shared experts and fine-grained routed experts

Use this skill-style markdown when working on Chapter 8 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 8.1 | The role of shared experts | `../sections/ch08/01-the-role-of-shared-experts.skill.md` | Verify shared experts receive gradients for every token, not only selected tokens. |
| 8.2 | Fine-grained routed expert segmentation | `../sections/ch08/02-fine-grained-routed-expert-segmentation.skill.md` | Compute total and active expert parameters for several segmentations. |
| 8.3 | The MiniDeepSeekMoE layer contract | `../sections/ch08/03-the-minideepseekmoe-layer-contract.skill.md` | Assert layer output shape equals input shape under smoke and default configs. |
| 8.4 | Combining shared and routed outputs | `../sections/ch08/04-combining-shared-and-routed-outputs.skill.md` | Ablate shared_out to zero and routed_out to zero to confirm both paths affect output. |
| 8.5 | Specialization diagnostics | `../sections/ch08/05-specialization-diagnostics.skill.md` | Generate expert usage heatmaps without overclaiming semantic specialization. |
| 8.6 | Chapter summary and handoff | `../sections/ch08/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: distinguish shared expert compute from routed active compute. |

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

# Chapter 8 development packet - Shared experts and fine-grained routed experts

Implement the DeepSeekMoE-inspired expert structure for the reference model.

## Chapter role

Introduce shared experts and fine-grained routed experts, the DeepSeekMoE-inspired mechanisms in the teaching model.

## Reader trajectory

- Enters: Reader has top-k MoE with trainable balancing and diagnostic habits.
- Leaves: Reader can implement the MiniDeepSeekMoE layer contract with shared plus routed expert paths.
- Invariant: Shared experts are always active; routed experts remain sparse and selected through top-k routing.
- Code area: `ch08/01_main-chapter-code/ with SharedExpertMLP, fine-grained ExpertBank, and MiniDeepSeekMoELayer.`

## Section order and brief paths

- **8.1 The role of shared experts** - `section_development_briefs/ch08/01-the-role-of-shared-experts.md`
  - Objective: Explain the always-on expert path as a way to separate common processing from routed specialization.
  - Diagnostic: Verify shared experts receive gradients for every token, not only selected tokens.
- **8.2 Fine-grained routed expert segmentation** - `section_development_briefs/ch08/02-fine-grained-routed-expert-segmentation.md`
  - Objective: Show how more smaller experts can replace fewer larger experts while preserving readable code.
  - Diagnostic: Compute total and active expert parameters for several segmentations.
- **8.3 The MiniDeepSeekMoE layer contract** - `section_development_briefs/ch08/03-the-minideepseekmoe-layer-contract.md`
  - Objective: Define the final layer interface that later chapters assemble into the full model.
  - Diagnostic: Assert layer output shape equals input shape under smoke and default configs.
- **8.4 Combining shared and routed outputs** - `section_development_briefs/ch08/04-combining-shared-and-routed-outputs.md`
  - Objective: Implement the forward pass that sums shared expert output and weighted routed output.
  - Diagnostic: Ablate shared_out to zero and routed_out to zero to confirm both paths affect output.
- **8.5 Specialization diagnostics** - `section_development_briefs/ch08/05-specialization-diagnostics.md`
  - Objective: Plan diagnostics that reveal whether routed experts are used differently across tokens.
  - Diagnostic: Generate expert usage heatmaps without overclaiming semantic specialization.
- **8.6 Chapter summary and handoff** - `section_development_briefs/ch08/06-chapter-summary-and-handoff.md`
  - Objective: Confirm that the final expert structure is implemented before changing balancing strategy.
  - Diagnostic: Reader checkpoint: distinguish shared expert compute from routed active compute.

## Chapter-level pitfalls

- Do not describe shared experts as residual replacements; they are an additional always-on expert path.
- Do not mix routed expert hidden size with dense FFN hidden size without stating the parameter trade-off.
- Keep shared and routed diagnostics separate.

## Chapter artifact style

Use shared green for shared experts and expert purple/active green for routed expert groups. Show parallel shared+routed paths.
