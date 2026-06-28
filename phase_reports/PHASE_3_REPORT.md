# Phase 3 report - Reference MoE model decision

## Decision

Use **MiniDeepSeekMoE** as the book's reference architecture.

MiniDeepSeekMoE is a small decoder-only language model whose feed-forward sublayers are replaced by a DeepSeekMoE-inspired sparse expert layer. It is not a literal DeepSeek-V3 clone. It is a teachable reference model that preserves the mechanisms that matter for a book about MoE models from scratch:

- dense FFN baseline for comparison,
- standard top-k sparse MoE routing,
- top-1 and top-2 router variants for historical grounding,
- fine-grained routed experts,
- shared expert isolation,
- auxiliary-loss-free bias-based load balancing,
- token dispatch and weighted combine implemented explicitly in PyTorch,
- routing diagnostics and expert-utilization visualizations.

## Recommended default implementation profile

| Role | Value |
|---|---:|
| Teaching name | `MiniDeepSeekMoE-16x2` |
| Model type | decoder-only causal LM |
| Attention | ordinary causal multi-head attention in the main path; MLA can remain optional/contextual rather than central |
| Transformer depth | 6 layers in the default notebook-sized run |
| Embedding width | 512 |
| Heads | 8 |
| Dense prefix | first 1 block stays dense in the teaching model; larger configs may use more dense prefix layers |
| Routed experts | 16 |
| Shared experts | 2 |
| Experts per token | 2 routed experts plus all shared experts |
| Routed expert hidden dim | 512 |
| Shared expert hidden dim | 1024 |
| Router score | sigmoid affinity for the DeepSeek-style final model; softmax in earlier baseline chapters |
| Selection rule | top-k on `score + router_bias` |
| Combine rule | normalize the unbiased selected scores, then weighted-sum selected expert outputs |
| Balance mechanism | auxiliary loss for standard baseline, dynamic bias update for final MiniDeepSeekMoE |
| Dataset target | TinyStories or another small next-token dataset |

## Why this model is suitable

The attached book repeatedly chooses mechanisms by starting from a bottleneck, then building the efficient replacement from scratch. Chapter 4 does this especially clearly for MoE: it starts with dense FFN cost, introduces sparse expert activation, derives routing and top-k selection, then adds load balancing and DeepSeek-specific expert specialization. MiniDeepSeekMoE preserves that explanatory ladder and makes it the central architecture of the new book.

The full DeepSeek-V3 architecture is too large and includes mechanisms outside the narrow MoE scope: MLA, FP8 infrastructure, multi-token prediction, large-scale distributed training, and production-scale routing kernels. Those are important context, but using the full model as the primary build would distract from the MoE learning path. MiniDeepSeekMoE keeps the same architectural ideas while making every part small enough to implement, test, diagram, and train in chapter code.

## Alternatives evaluated

| Candidate | Use in book | Reason not chosen as final reference |
|---|---|---|
| Dense Transformer FFN | baseline only | necessary contrast, but not an MoE model |
| Switch Transformer style top-1 MoE | early chapter milestone | simple and historically important, but too narrow for a full MoE-from-scratch book |
| GShard/Mixtral style top-2 MoE | middle chapter milestone | excellent weighted-routing bridge, but lacks DeepSeek-style shared experts and fine-grained segmentation |
| Full DeepSeek-V3 | reference context and appendix-level mapping | production-scale model is not a practical from-scratch teaching target |
| MiniDeepSeekMoE | final reference architecture | preserves the important DeepSeekMoE ideas while remaining executable and explainable |

## Phase 3 deliverables

```text
moe_from_scratch_phase3_complete/
├── PHASE_3_REPORT.md
├── model_selection/
│   ├── model_choice.md
│   ├── source_book_alignment.md
│   ├── alternatives_compared.md
│   ├── reference_model_spec.md
│   ├── implementation_scope.md
│   ├── diagnostic_requirements.md
│   └── source_checks.md
├── data/
│   └── phase3_model_decision.json
├── latex_model_contract/
│   ├── main.tex
│   ├── phase3_model_choice_preview.pdf
│   ├── styles/
│   ├── chapters/model-choice.tex
│   ├── figures/fig-model-ladder.tex
│   ├── figures/fig-minideepseekmoe-block.tex
│   ├── tables/tab-candidate-models.tex
│   ├── tables/tab-reference-configs.tex
│   ├── tables/tab-source-book-reasons.tex
│   ├── listings/lst-router-contract.tex
│   └── equations/eq-minideepseekmoe-layer.tex
└── validation/
    ├── proofread_notes_phase3.md
    ├── latex_compile.log
    └── rendered_preview/page-*.png
```

## Proofread conclusion

I checked the model choice against the source book's extracted flow and the attached Chapter 4 treatment. The model decision is internally consistent: the final architecture is DeepSeekMoE-inspired, but the book still has room to teach Switch/GShard/Mixtral-style variants as stepping stones. The main correction made during proofreading was to avoid calling the model a full DeepSeek-V3 clone; it should be described as a scaled teaching architecture with a clear mapping to DeepSeekMoE/V3 features. The LaTeX preview was compiled and rendered after fixing table-color and figure-width issues.
