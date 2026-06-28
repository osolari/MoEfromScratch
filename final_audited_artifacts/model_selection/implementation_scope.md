# Implementation scope

## What the book should implement directly

- Dense FFN baseline.
- Expert FFN modules.
- Naive all-experts mixture for intuition.
- Top-1 router and sparse dispatch.
- Top-2 router and weighted combine.
- Auxiliary load-balancing loss.
- Capacity factor and dropped-token accounting.
- Shared experts.
- Fine-grained routed experts.
- Dynamic router bias update.
- Full MiniDeepSeekMoE language model.
- Training loop on a small next-token dataset.
- Diagnostic plots and tables.

## What the book should explain but not make central

- Full DeepSeek-V3 scale.
- MLA, MTP, FP8, and distributed DualPipe-style systems details.
- Production all-to-all communication kernels.
- Expert parallelism across multi-node clusters.
- Quantization-specific MoE kernels.

These topics can appear as context boxes, appendices, or final-chapter bridges, but not as the core from-scratch path.

## Required chapter-code style

Each implementation should start as a minimal module, then be integrated into the model:

1. `ExpertFFN`
2. `Router`
3. `TopKRouter`
4. `SparseDispatcher`
5. `StandardMoELayer`
6. `DeepSeekStyleMoELayer`
7. `MiniDeepSeekMoEBlock`
8. `MiniDeepSeekMoEForCausalLM`

## Repository implication

The future codebase should keep the chapter-first layout from the attached repository but add a small shared package:

```text
moe-from-scratch/
├── ch01/
├── ch02/
├── ...
├── ch10/
├── src/minimoe/
│   ├── experts.py
│   ├── routers.py
│   ├── dispatch.py
│   ├── losses.py
│   ├── model.py
│   └── diagnostics.py
└── tests/
```

Early chapters can use notebooks, but the final model should live in importable `.py` files so each chapter can reuse tested components.
