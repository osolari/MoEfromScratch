# Source anchor map

Use these primary sources to keep mechanism descriptions accurate. Do not turn the tutorial into a literature review.

## shazeer2017
- Title: Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer
- Use: conditional computation, trainable sparse gating, expert bank motivation
- URL: https://arxiv.org/abs/1701.06538

## gshard2020
- Title: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding
- Use: top-2 routing precedent, dispatch/capacity framing, expert-parallel motivation
- URL: https://arxiv.org/abs/2006.16668

## switch2021
- Title: Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
- Use: top-1 routing, auxiliary load-balancing loss, training stability motivation
- URL: https://arxiv.org/abs/2101.03961

## expertchoice2022
- Title: Mixture-of-Experts with Expert Choice Routing
- Use: optional contrast for token-choice versus expert-choice routing
- URL: https://arxiv.org/abs/2202.09368

## mixtral2024
- Title: Mixtral of Experts
- Use: modern sparse MoE LLM with two selected experts per token
- URL: https://arxiv.org/abs/2401.04088

## deepseekmoe2024
- Title: DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models
- Use: fine-grained routed experts, shared experts, specialization and redundancy motivation
- URL: https://arxiv.org/abs/2401.06066

## deepseekv3_2024
- Title: DeepSeek-V3 Technical Report
- Use: auxiliary-loss-free balancing, non-trainable router bias, production-scale mapping
- URL: https://arxiv.org/abs/2412.19437
