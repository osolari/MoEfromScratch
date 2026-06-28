# Source checks used in Phase 3

## Attached book and codebase

- The attached source book's Chapter 4 presents MoE as an efficiency mechanism that replaces dense FFNs with sparse expert routing.
- The attached source book introduces the core DeepSeekMoE motivations as knowledge hybridity, knowledge redundancy, and load imbalance.
- The attached companion code already contains a small DeepSeek-style MoE implementation with routed experts, shared experts, top-k routing, and dynamic router bias logic.
- The attached comparison notebook uses a default small configuration close to `n_layer=6`, `n_head=8`, `n_embd=512`, `16` routed experts, top-2 routing, and `2` shared experts.

## External technical checks

- DeepSeekMoE paper: used to confirm fine-grained expert segmentation and shared expert isolation as the two defining DeepSeekMoE mechanisms.
- DeepSeek-V3 technical report: used to confirm that V3 combines DeepSeekMoE with auxiliary-loss-free load balancing and has a production-scale 671B/37B-active parameter profile.
- Mixtral paper: used to confirm a modern top-2 sparse MoE baseline with 8 experts.
- Switch Transformer paper: used to confirm top-1 routing as a simple early sparse-MoE milestone.
- Hugging Face DeepSeek-V3 config: used to confirm modern large-model configuration fields such as `n_routed_experts`, `n_shared_experts`, `num_experts_per_tok`, and `first_k_dense_replace`.

## Proofread correction

Do not describe the chosen teaching model as "DeepSeek-V3 from scratch." The correct phrasing is:

> MiniDeepSeekMoE is a DeepSeekMoE-inspired teaching model that maps cleanly to DeepSeek-style production ideas while remaining small enough to implement from scratch.
