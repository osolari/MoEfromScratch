---
name: moe-ch10-developer
description: use when developing chapter 10 of moe models from scratch, assembling minideepseekmoe end to end, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 10 developer: Assembling MiniDeepSeekMoE end to end

Use this skill-style markdown when working on Chapter 10 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 10.1 | Configuration objects and model variants | `../sections/ch10/01-configuration-objects-and-model-variants.skill.md` | Print model summary and assert required fields exist. |
| 10.2 | Decoder block with dense prefix and MoE layers | `../sections/ch10/02-decoder-block-with-dense-prefix-and-moe-layers.skill.md` | List layer types during model initialization. |
| 10.3 | Forward pass outputs and loss dictionary | `../sections/ch10/03-forward-pass-outputs-and-loss-dictionary.skill.md` | Unit test for output keys under dense, auxiliary, and bias modes. |
| 10.4 | Training and sampling scripts | `../sections/ch10/04-training-and-sampling-scripts.skill.md` | Verify checkpoint reload produces logits of the same shape. |
| 10.5 | Full-model smoke tests | `../sections/ch10/05-full-model-smoke-tests.skill.md` | CI-style console summary for all smoke tests. |
| 10.6 | Chapter summary and handoff | `../sections/ch10/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: run the smoke model and inspect router metrics. |

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

# Chapter 10 development packet - Assembling MiniDeepSeekMoE end to end

Integrate the final MoE layer into a complete decoder-only language model.

## Chapter role

Assemble the final MiniDeepSeekMoE model, keeping configuration, outputs, losses, and smoke tests consistent.

## Reader trajectory

- Enters: Reader has all layer-level mechanisms needed for the final architecture.
- Leaves: Reader has a complete trainable decoder-only MiniDeepSeekMoE codebase with diagnostic outputs.
- Invariant: The model forward pass returns logits and, when requested, a structured auxiliary dictionary without breaking simple inference.
- Code area: `ch10/01_main-chapter-code/ with config.py, model.py, train.py, sample.py, and tests.`

## Section order and brief paths

- **10.1 Configuration objects and model variants** - `section_development_briefs/ch10/01-configuration-objects-and-model-variants.md`
  - Objective: Move from chapter-specific modules to a unified configuration-driven model.
  - Diagnostic: Print model summary and assert required fields exist.
- **10.2 Decoder block with dense prefix and MoE layers** - `section_development_briefs/ch10/02-decoder-block-with-dense-prefix-and-moe-layers.md`
  - Objective: Assemble layers so early dense computation can precede sparse MoE layers if configured.
  - Diagnostic: List layer types during model initialization.
- **10.3 Forward pass outputs and loss dictionary** - `section_development_briefs/ch10/03-forward-pass-outputs-and-loss-dictionary.md`
  - Objective: Return logits and structured losses/metrics without making training code guess where values live.
  - Diagnostic: Unit test for output keys under dense, auxiliary, and bias modes.
- **10.4 Training and sampling scripts** - `section_development_briefs/ch10/04-training-and-sampling-scripts.md`
  - Objective: Create runnable scripts that match the source codebase style: minimal, readable, and chapter-scoped.
  - Diagnostic: Verify checkpoint reload produces logits of the same shape.
- **10.5 Full-model smoke tests** - `section_development_briefs/ch10/05-full-model-smoke-tests.md`
  - Objective: Create a test suite that catches shape, routing, balancing, and serialization failures.
  - Diagnostic: CI-style console summary for all smoke tests.
- **10.6 Chapter summary and handoff** - `section_development_briefs/ch10/06-chapter-summary-and-handoff.md`
  - Objective: Summarize the complete implementation and separate code correctness from model quality.
  - Diagnostic: Reader checkpoint: run the smoke model and inspect router metrics.

## Chapter-level pitfalls

- Do not change APIs section by section; stabilize config and return dictionaries here.
- Do not hide dense prefix decisions; explain which layers are dense and which are MoE.
- Smoke tests must run without a GPU.

## Chapter artifact style

Use architecture diagrams, configuration tables, and API listings. Keep colors semantic, not decorative.
