# MoE Models from Scratch - overall book plan

## Book premise

*MoE Models from Scratch* teaches mixture-of-experts language models by rebuilding the sparse feed-forward path one mechanism at a time. The reader starts with a dense decoder baseline, replaces the FFN with routed experts, learns how routing fails, adds balancing and diagnostics, and finishes with a MiniDeepSeekMoE implementation that keeps the core ideas visible.

## Reference architecture

The book uses `MiniDeepSeekMoE-16x2` as the final target: a decoder-only causal language model with 16 routed experts, 2 shared experts, top-2 routed experts per token, fine-grained routed expert dimensions, and auxiliary-loss-free router-bias balancing. The smoke configuration uses 4 routed experts and 1 shared expert for CPU-friendly tests.

## Editorial rhythm

Every chapter follows this loop:

1. Start from a concrete bottleneck or failure mode.
2. Anchor the mechanism with a schematic diagram.
3. Specify tensor shapes before writing code.
4. Implement the smallest readable PyTorch version.
5. Add a diagnostic that can catch mistakes.
6. End by naming the limitation that motivates the next chapter.

## Part structure

### Part I - foundations and baseline

**Chapter 1: From dense compute to conditional compute** - Motivate MoE from the dense FFN bottleneck and establish the build ladder.

**Chapter 2: A dense Transformer baseline from scratch** - Build a minimal decoder-only language model before replacing the FFN with MoE.

### Part II - routing mechanics from scratch

**Chapter 3: Experts, routers, and the first MoE layer** - Introduce the MoE layer as a transparent replacement for the dense FFN.

**Chapter 4: Top-1 routing and Switch-style dispatch** - Build the simplest sparse router and expose the expert-load problem.

**Chapter 5: Top-2 routing and weighted expert combination** - Generalize sparse routing so each token can combine two expert transformations.

**Chapter 6: Vectorized dispatch, capacity, and routing efficiency** - Move from readable loops to scalable tensor operations without changing the MoE math.

### Part III - training routers and experts

**Chapter 7: Router training and load-balancing losses** - Teach the router to avoid expert collapse before moving to auxiliary-loss-free balancing.

**Chapter 8: Shared experts and fine-grained routed experts** - Implement the DeepSeekMoE-inspired expert structure for the reference model.

**Chapter 9: Auxiliary-loss-free load balancing** - Replace auxiliary balancing with a router-bias mechanism that affects selection but not combine weights.

### Part IV - assembling and training the model

**Chapter 10: Assembling MiniDeepSeekMoE end to end** - Integrate the final MoE layer into a complete decoder-only language model.

**Chapter 11: Training, diagnostics, and controlled experiments** - Use the model to answer concrete questions about routing, balance, and sparse capacity.

### Part V - inference and scale

**Chapter 12: Inference, performance, and scaling beyond the toy model** - Connect the from-scratch implementation to systems concerns without turning the book into a distributed-systems text.

## Appendices

- **Appendix A: LaTeX artifact and diagram rules** - Document the color map, input-only artifact rule, label conventions, and TikZ patterns.
- **Appendix B: Tensor shape checklist** - Collect every tensor symbol and shape used in routing, dispatch, balancing, and diagnostics.
- **Appendix C: Codebase smoke tests and reproducibility checklist** - Provide a compact checklist for validating notebooks, scripts, tests, figures, and LaTeX builds.
