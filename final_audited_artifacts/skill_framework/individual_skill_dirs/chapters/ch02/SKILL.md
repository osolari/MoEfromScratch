---
name: moe-ch02-developer
description: use when developing chapter 2 of moe models from scratch, a dense transformer baseline from scratch, including latex section prose, standalone artifact wrappers, chapter code, diagnostics, and chapter handoffs.
---

# Chapter 2 developer: A dense Transformer baseline from scratch

Use this skill-style markdown when working on Chapter 2 as a whole. For actual section drafting, load the matching section skill file and use this chapter file only as context.

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
| 2.1 | Dataset and token batches | `../sections/ch02/01-dataset-and-token-batches.skill.md` | Print the first input-target pair and decode it to verify shifting. |
| 2.2 | Token and position embeddings | `../sections/ch02/02-token-and-position-embeddings.skill.md` | Assert output shape and confirm gradients flow to both embedding tables. |
| 2.3 | Causal self-attention as the context path | `../sections/ch02/03-causal-self-attention-as-the-context-path.skill.md` | Check that a token cannot attend to future positions. |
| 2.4 | Dense feed-forward block as the replacement target | `../sections/ch02/04-dense-feed-forward-block-as-the-replacement-target.skill.md` | Confirm FFN preserves the final D dimension. |
| 2.5 | Training loop and sampling baseline | `../sections/ch02/05-training-loop-and-sampling-baseline.skill.md` | Track train and validation loss plus samples at fixed intervals. |
| 2.6 | Baseline diagnostics and comparison slots | `../sections/ch02/06-baseline-diagnostics-and-comparison-slots.skill.md` | Write the first baseline row in the experiment comparison table. |

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

# Chapter 2 development packet - A dense Transformer baseline from scratch

Build a minimal decoder-only language model before replacing the FFN with MoE.

## Chapter role

Build the dense language-model baseline that every MoE replacement will be compared against.

## Reader trajectory

- Enters: Reader understands the conditional-compute motivation and needs a runnable Transformer baseline.
- Leaves: Reader has a CPU-smoke-testable decoder-only model, training loop, and diagnostic slots.
- Invariant: All baseline modules map (B, T, D) tensors to compatible shapes and preserve causal next-token training.
- Code area: `ch02/01_main-chapter-code/ with model.py, train.py or notebook equivalents for the dense baseline.`

## Section order and brief paths

- **2.1 Dataset and token batches** - `section_development_briefs/ch02/01-dataset-and-token-batches.md`
  - Objective: Create the small next-token prediction pipeline used for every model variant.
  - Diagnostic: Print the first input-target pair and decode it to verify shifting.
- **2.2 Token and position embeddings** - `section_development_briefs/ch02/02-token-and-position-embeddings.md`
  - Objective: Implement the entry point that maps integer token IDs to dense vectors.
  - Diagnostic: Assert output shape and confirm gradients flow to both embedding tables.
- **2.3 Causal self-attention as the context path** - `section_development_briefs/ch02/03-causal-self-attention-as-the-context-path.md`
  - Objective: Build enough attention to make the baseline a real decoder while keeping MoE focus on the FFN.
  - Diagnostic: Check that a token cannot attend to future positions.
- **2.4 Dense feed-forward block as the replacement target** - `section_development_briefs/ch02/04-dense-feed-forward-block-as-the-replacement-target.md`
  - Objective: Implement the dense FFN in a way that makes the later expert replacement obvious.
  - Diagnostic: Confirm FFN preserves the final D dimension.
- **2.5 Training loop and sampling baseline** - `section_development_briefs/ch02/05-training-loop-and-sampling-baseline.md`
  - Objective: Train the dense model long enough to create a trustworthy comparison anchor.
  - Diagnostic: Track train and validation loss plus samples at fixed intervals.
- **2.6 Baseline diagnostics and comparison slots** - `section_development_briefs/ch02/06-baseline-diagnostics-and-comparison-slots.md`
  - Objective: Prepare diagnostic hooks that will later compare dense and sparse models fairly.
  - Diagnostic: Write the first baseline row in the experiment comparison table.

## Chapter-level pitfalls

- Do not over-optimize; the baseline exists to anchor MoE changes.
- Do not introduce experts before the dense FFN contract is fully clear.
- Keep dataset/tokenization minimal and reproducible.

## Chapter artifact style

Use baseline Transformer schematics, shifted-token tables, and training-loop diagrams. Keep MoE colors reserved for future contrast.
