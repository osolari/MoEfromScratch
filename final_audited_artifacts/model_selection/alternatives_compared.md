# Alternatives compared

## Evaluation criteria

The reference model was scored against five criteria:

1. **Teachable from scratch** - Can the full path be implemented without a production framework?
2. **Modern relevance** - Does it connect to modern open MoE language models?
3. **Visual clarity** - Does it support clear diagrams and tensor walkthroughs?
4. **Experimental payoff** - Can readers measure load, speed, or loss differences?
5. **Alignment with the source book** - Does it preserve the source book's bottleneck-to-implementation flow?

## Candidate notes

### Dense Transformer FFN

A dense FFN is essential as the starting baseline. It gives the reader the cost profile that MoE is designed to change. It should not be the final reference model because it does not teach routing, sparse dispatch, expert specialization, or load balancing.

### Switch-style top-1 MoE

Switch-style routing is the best first sparse model because it has one selected expert per token. This makes routing and capacity easy to visualize. It should appear early, but top-1 routing does not teach weighted expert mixtures and does not carry the DeepSeek-specific reasons for shared experts and fine-grained segmentation.

### GShard/Mixtral-style top-2 MoE

Top-2 routing is the best bridge from simple sparse dispatch to weighted mixtures. It should be a major milestone. However, a pure top-2 Mixtral-like model does not address the source book's two DeepSeekMoE specialization problems as directly as a model with shared expert isolation and fine-grained routed experts.

### Full DeepSeek-V3

Full DeepSeek-V3 is the production-scale reference context, not the from-scratch build target. Its published model uses a very large parameter budget and combines several non-MoE optimizations. Teaching that as the first-class implementation would turn the book into a broad DeepSeek systems book rather than a focused MoE book.

### MiniDeepSeekMoE

MiniDeepSeekMoE is the best final reference because it can be built in layers and it naturally supports the source book's figure-first, code-first style. It also makes room for historical and modern alternatives as stepping stones rather than competitors.

## Decision matrix

| Candidate | Scratch teachability | Modern relevance | Visual clarity | Experimental payoff | Final role |
|---|---:|---:|---:|---:|---|
| Dense FFN | 5 | 2 | 4 | 4 | baseline |
| Switch top-1 | 5 | 4 | 5 | 5 | early milestone |
| GShard/Mixtral top-2 | 4 | 5 | 5 | 5 | middle milestone |
| Full DeepSeek-V3 | 1 | 5 | 3 | 2 | reference mapping |
| MiniDeepSeekMoE | 5 | 5 | 5 | 5 | final reference |
