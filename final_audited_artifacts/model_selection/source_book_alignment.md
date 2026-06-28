# Alignment with the attached book's reasoning

## Reason 1 - start from a bottleneck

The source book motivates architecture from bottlenecks: KV-cache memory for attention, dense FFN compute for MoE, and training/inference efficiency for later optimizations. The MoE book should use the same pattern. MiniDeepSeekMoE begins with the dense FFN bottleneck and shows that FFN parameters dominate the computation of a Transformer block.

## Reason 2 - make sparsity visible

The attached Chapter 4 explains MoE by routing a few tokens through a small number of experts and showing top-k selection before presenting code. The new book should keep this small-example style. The first recurring toy example should use four tokens, four experts, and top-2 routing so figures, equations, and code can share the same objects.

## Reason 3 - teach mechanisms before scale

The source book repeatedly scales down production ideas so a reader can implement them. MiniDeepSeekMoE follows that rule: it keeps DeepSeekMoE's core concepts but shrinks the model to notebook scale.

## Reason 4 - compare against a simpler baseline

The attached Chapter 4 includes a head-to-head comparison between a standard MoE and a DeepSeek-style MoE. The new book should make that comparison a central recurring device. Every major improvement should have a table or plot that compares it to the previous simpler model.

## Reason 5 - focus on efficient specialization

The source Chapter 4 frames DeepSeekMoE around two problems: knowledge hybridity and knowledge redundancy. MiniDeepSeekMoE directly maps to those ideas:

| Source-book problem | MiniDeepSeekMoE mechanism |
|---|---|
| Knowledge hybridity | use more, smaller routed experts |
| Knowledge redundancy | use shared experts for common knowledge |
| Load imbalance | use diagnostics, balance losses, capacity, and finally dynamic bias |
| Implementation opacity | use explicit PyTorch dispatch and weighted combine |

## Language implications

The model should be described with the same practical voice as the source book:

- Begin with "The dense version works, but..." rather than abstract definitions.
- Use phrases like "Let's trace the flow" before diagrams.
- End sections with a concrete limitation that motivates the next mechanism.
- Keep shape annotations close to each figure and code listing.
