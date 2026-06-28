# Reference model specification

## Name

`MiniDeepSeekMoE`

## Model family

Decoder-only causal language model with sparse MoE feed-forward blocks.

## Default configuration

```yaml
model_name: MiniDeepSeekMoE-16x2
n_layer: 6
n_head: 8
d_model: 512
block_size: 256
vocab_size: 50257
attention: causal_mha
position_encoding: learned_positions_for_first_implementation
normalization: layer_norm_or_rms_norm_by_chapter_context
dense_prefix_layers: 1
moe_layer_frequency: 1
n_routed_experts: 16
n_shared_experts: 2
routed_experts_per_token: 2
routed_expert_hidden_dim: 512
shared_expert_hidden_dim: 1024
router_score_baseline: softmax
router_score_final: sigmoid_affinity
selection_rule: topk(score + router_bias)
combine_rule: normalize_unbiased_selected_scores
balance_baseline: auxiliary_load_balancing_loss
balance_final: auxiliary_loss_free_router_bias_update
diagnostics:
  - validation_loss_curve
  - expert_load_histogram
  - expert_probability_table
  - dropped_token_count_when_capacity_is_enabled
  - routing_entropy
```

## Smoke-test configuration

```yaml
model_name: MiniDeepSeekMoE-Smoke
n_layer: 2
n_head: 4
d_model: 128
block_size: 64
n_routed_experts: 4
n_shared_experts: 1
routed_experts_per_token: 2
routed_expert_hidden_dim: 128
shared_expert_hidden_dim: 256
```

Use this configuration for unit tests, shape checks, and CPU-only examples.

## Larger teaching configuration

```yaml
model_name: MiniDeepSeekMoE-64x6
n_layer: 8
n_head: 8
d_model: 768
block_size: 512
n_routed_experts: 64
n_shared_experts: 2
routed_experts_per_token: 6
routed_expert_hidden_dim: 384
shared_expert_hidden_dim: 1536
```

Use this configuration only for optional experiments and for explaining how the tiny model maps to DeepSeek-like settings.

## Tensor contracts

| Tensor | Shape | Meaning |
|---|---|---|
| `x` | `(B, T, D)` | token states entering the MoE layer |
| `x_flat` | `(B*T, D)` | flattened tokens for routing and dispatch |
| `router_logits` | `(B*T, E)` | raw expert scores before nonlinearity |
| `score` | `(B*T, E)` | affinity/probability score per expert |
| `router_bias` | `(E,)` | dynamic balance adjustment used only for selection |
| `topk_idx` | `(B*T, K)` | selected routed expert ids per token |
| `topk_score` | `(B*T, K)` | selected unbiased scores |
| `gate` | `(B*T, K)` | normalized selected scores for weighted combine |
| `routed_out` | `(B*T, D)` | accumulated routed expert outputs |
| `shared_out` | `(B*T, D)` | sum of shared expert outputs |
| `y` | `(B, T, D)` | output of the MoE layer |

## Implementation invariant

The output shape of every MoE layer must equal its input shape. All routing, dispatch, and expert computation is internal to the layer.

## Bias update invariant

The dynamic bias is not a trainable parameter and should not receive gradients. It is updated outside backpropagation from observed expert load.

```text
if load_i < target_load: bias_i += gamma
if load_i > target_load: bias_i -= gamma
```

The book should introduce this after the reader has already implemented auxiliary and load-balancing losses, because the contrast makes the reason for auxiliary-loss-free balancing clear.
