# Chapter 8: Shared experts and fine-grained routed experts

**Part:** Part III - training routers and experts

**Role in the book:** Implement the DeepSeekMoE-inspired expert structure for the reference model.

## This chapter covers

- Why shared experts provide an always-on path for common knowledge.
- Why fine-grained routed experts encourage more specialized sparse computation.
- How shared and routed expert outputs combine in one MoE block.

## Implementation milestone

Implement SharedExpertMLP, FineGrainedExpertBank, and MiniDeepSeekMoELayer with shared plus routed outputs.

## Section-by-section plan

### 8.1 The role of shared experts

**Objective:** Explain the always-on expert path as a way to separate common processing from routed specialization.

**Mini-example:** Every token goes through one shared expert while also routing to two routed experts.

**Development flow:**

1. Open with the local problem: Explain the always-on expert path as a way to separate common processing from routed specialization.
2. Introduce the schematic: Parallel shared path and routed path merging at the MoE output.
3. Walk through mechanics and shapes using: shared_out = sum_s shared_expert_s(x).
4. Implement or pseudocode: SharedExpertMLP module and shared_out calculation.
5. Verify with: Verify shared experts receive gradients for every token, not only selected tokens.
6. Bridge: Routed experts can also be made finer-grained to increase specialization options.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch08/fig-the-role-of-shared-experts.tex` - TikZ figure. Caption placeholder: Parallel shared path and routed path merging at the MoE output. Label: `fig:ch08-the-role-of-shared-experts`.
- `latex_book_skeleton/tables/ch08/tab-the-role-of-shared-experts.tex` - Table. Caption placeholder: Shared expert path versus routed expert path responsibilities. Label: `tab:ch08-the-role-of-shared-experts`.
- `latex_book_skeleton/listings/ch08/lst-the-role-of-shared-experts.tex` - Python listing. Caption placeholder: SharedExpertMLP module and shared_out calculation. Label: `lst:ch08-the-role-of-shared-experts`.
- `latex_book_skeleton/equations/ch08/eq-the-role-of-shared-experts.tex` - Equation artifact. Placeholder: shared_out = sum_s shared_expert_s(x). Label: `eq:ch08-the-role-of-shared-experts`.

Detailed section file: `section_plans/ch08/01-the-role-of-shared-experts.md`

### 8.2 Fine-grained routed expert segmentation

**Objective:** Show how more smaller experts can replace fewer larger experts while preserving readable code.

**Mini-example:** Compare 4 large experts with hidden_dim=1024 to 16 smaller experts with hidden_dim=256.

**Development flow:**

1. Open with the local problem: Show how more smaller experts can replace fewer larger experts while preserving readable code.
2. Introduce the schematic: Large expert blocks split into finer expert tiles.
3. Walk through mechanics and shapes using: Expert-bank parameter estimate E * (D*H_e + H_e*D).
4. Implement or pseudocode: ExpertBank configuration that changes n_experts and expert_hidden_dim together.
5. Verify with: Compute total and active expert parameters for several segmentations.
6. Bridge: The reference layer combines fine-grained routed experts with shared experts.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch08/fig-fine-grained-routed-expert-segmentation.tex` - TikZ figure. Caption placeholder: Large expert blocks split into finer expert tiles. Label: `fig:ch08-fine-grained-routed-expert-segmentation`.
- `latex_book_skeleton/tables/ch08/tab-fine-grained-routed-expert-segmentation.tex` - Table. Caption placeholder: Expert count, hidden dimension, total parameters, and active parameters. Label: `tab:ch08-fine-grained-routed-expert-segmentation`.
- `latex_book_skeleton/listings/ch08/lst-fine-grained-routed-expert-segmentation.tex` - Python listing. Caption placeholder: ExpertBank configuration that changes n_experts and expert_hidden_dim together. Label: `lst:ch08-fine-grained-routed-expert-segmentation`.
- `latex_book_skeleton/equations/ch08/eq-fine-grained-routed-expert-segmentation.tex` - Equation artifact. Placeholder: Expert-bank parameter estimate E * (D*H_e + H_e*D). Label: `eq:ch08-fine-grained-routed-expert-segmentation`.

Detailed section file: `section_plans/ch08/02-fine-grained-routed-expert-segmentation.md`

### 8.3 The MiniDeepSeekMoE layer contract

**Objective:** Define the final layer interface that later chapters assemble into the full model.

**Mini-example:** Use D=128, E=4 routed experts, one shared expert, and K=2 in the smoke config.

**Development flow:**

1. Open with the local problem: Define the final layer interface that later chapters assemble into the full model.
2. Introduce the schematic: MiniDeepSeekMoE layer block with router, routed experts, shared experts, combine, and residual output.
3. Walk through mechanics and shapes using: y = x + shared_out + routed_out when the block is shown with residual context.
4. Implement or pseudocode: MiniDeepSeekMoELayer __init__ showing router, routed experts, and shared experts.
5. Verify with: Assert layer output shape equals input shape under smoke and default configs.
6. Bridge: The forward pass computes shared and routed paths side by side.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch08/fig-the-minideepseekmoe-layer-contract.tex` - TikZ figure. Caption placeholder: MiniDeepSeekMoE layer block with router, routed experts, shared experts, combine, and residual output. Label: `fig:ch08-the-minideepseekmoe-layer-contract`.
- `latex_book_skeleton/tables/ch08/tab-the-minideepseekmoe-layer-contract.tex` - Table. Caption placeholder: Final layer tensor contract and configuration fields. Label: `tab:ch08-the-minideepseekmoe-layer-contract`.
- `latex_book_skeleton/listings/ch08/lst-the-minideepseekmoe-layer-contract.tex` - Python listing. Caption placeholder: MiniDeepSeekMoELayer __init__ showing router, routed experts, and shared experts. Label: `lst:ch08-the-minideepseekmoe-layer-contract`.
- `latex_book_skeleton/equations/ch08/eq-the-minideepseekmoe-layer-contract.tex` - Equation artifact. Placeholder: y = x + shared_out + routed_out when the block is shown with residual context. Label: `eq:ch08-the-minideepseekmoe-layer-contract`.

Detailed section file: `section_plans/ch08/03-the-minideepseekmoe-layer-contract.md`

### 8.4 Combining shared and routed outputs

**Objective:** Implement the forward pass that sums shared expert output and weighted routed output.

**Mini-example:** Trace one token through shared expert s0 and routed experts e2/e7.

**Development flow:**

1. Open with the local problem: Implement the forward pass that sums shared expert output and weighted routed output.
2. Introduce the schematic: Shared output and routed weighted output merged before projection back to the decoder block.
3. Walk through mechanics and shapes using: moe_out_t = shared_out_t + sum_j gate_{tj} routed_expert_{idx_{tj}}(x_t).
4. Implement or pseudocode: Forward pass for shared+routed MoE layer.
5. Verify with: Ablate shared_out to zero and routed_out to zero to confirm both paths affect output.
6. Bridge: With two expert paths, diagnostics should separate shared and routed behavior.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch08/fig-combining-shared-and-routed-outputs.tex` - TikZ figure. Caption placeholder: Shared output and routed weighted output merged before projection back to the decoder block. Label: `fig:ch08-combining-shared-and-routed-outputs`.
- `latex_book_skeleton/tables/ch08/tab-combining-shared-and-routed-outputs.tex` - Table. Caption placeholder: Output components: shared_out, routed_out, residual, and final block output. Label: `tab:ch08-combining-shared-and-routed-outputs`.
- `latex_book_skeleton/listings/ch08/lst-combining-shared-and-routed-outputs.tex` - Python listing. Caption placeholder: Forward pass for shared+routed MoE layer. Label: `lst:ch08-combining-shared-and-routed-outputs`.
- `latex_book_skeleton/equations/ch08/eq-combining-shared-and-routed-outputs.tex` - Equation artifact. Placeholder: moe_out_t = shared_out_t + sum_j gate_{tj} routed_expert_{idx_{tj}}(x_t). Label: `eq:ch08-combining-shared-and-routed-outputs`.

Detailed section file: `section_plans/ch08/04-combining-shared-and-routed-outputs.md`

### 8.5 Specialization diagnostics

**Objective:** Plan diagnostics that reveal whether routed experts are used differently across tokens.

**Mini-example:** Group tokens by simple categories or positions and inspect selected expert frequencies.

**Development flow:**

1. Open with the local problem: Plan diagnostics that reveal whether routed experts are used differently across tokens.
2. Introduce the schematic: Expert usage heatmap by token group or position bucket.
3. Walk through mechanics and shapes using: Conditional usage frequency p(expert | token_group).
4. Implement or pseudocode: collect_expert_usage_by_token helper.
5. Verify with: Generate expert usage heatmaps without overclaiming semantic specialization.
6. Bridge: The layer architecture is now complete; the next chapter replaces auxiliary loss with dynamic router bias balancing.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch08/fig-specialization-diagnostics.tex` - TikZ figure. Caption placeholder: Expert usage heatmap by token group or position bucket. Label: `fig:ch08-specialization-diagnostics`.
- `latex_book_skeleton/tables/ch08/tab-specialization-diagnostics.tex` - Table. Caption placeholder: Specialization probes: token string, position, loss contribution, selected experts. Label: `tab:ch08-specialization-diagnostics`.
- `latex_book_skeleton/listings/ch08/lst-specialization-diagnostics.tex` - Python listing. Caption placeholder: collect_expert_usage_by_token helper. Label: `lst:ch08-specialization-diagnostics`.
- `latex_book_skeleton/equations/ch08/eq-specialization-diagnostics.tex` - Equation artifact. Placeholder: Conditional usage frequency p(expert | token_group). Label: `eq:ch08-specialization-diagnostics`.

Detailed section file: `section_plans/ch08/05-specialization-diagnostics.md`

### 8.6 Chapter summary and handoff

**Objective:** Confirm that the final expert structure is implemented before changing balancing strategy.

**Mini-example:** Run one batch through MiniDeepSeekMoELayer and print all returned metrics.

**Development flow:**

1. Open with the local problem: Confirm that the final expert structure is implemented before changing balancing strategy.
2. Introduce the schematic: Completed MiniDeepSeekMoE layer with diagnostic outputs attached.
3. Walk through mechanics and shapes using: Layer output decomposition into shared and routed components.
4. Implement or pseudocode: Smoke test instantiating the final layer contract.
5. Verify with: Reader checkpoint: distinguish shared expert compute from routed active compute.
6. Bridge: The next chapter keeps this architecture and changes how expert balance is enforced.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch08/fig-chapter-summary-and-handoff.tex` - TikZ figure. Caption placeholder: Completed MiniDeepSeekMoE layer with diagnostic outputs attached. Label: `fig:ch08-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch08/tab-chapter-summary-and-handoff.tex` - Table. Caption placeholder: Components completed so far and balancing method still used. Label: `tab:ch08-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch08/lst-chapter-summary-and-handoff.tex` - Python listing. Caption placeholder: Smoke test instantiating the final layer contract. Label: `lst:ch08-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch08/eq-chapter-summary-and-handoff.tex` - Equation artifact. Placeholder: Layer output decomposition into shared and routed components. Label: `eq:ch08-chapter-summary-and-handoff`.

Detailed section file: `section_plans/ch08/06-chapter-summary-and-handoff.md`
