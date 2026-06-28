# Chapter layout matrix extracted from the template book
This file captures structure and artifact density. It is a structural reference, not prose to reuse.
| Ch. | Title | H2 | H3 | Figures | Code/listings | Tables | Callouts | Avg paragraph words |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Introduction to DeepSeek | 6 | 3 | 9 | 0 | 0 | 0 | 48.8 |
| 2 | Solving the inference bottleneck with the key-value cache | 9 | 21 | 25 | 5 | 0 | 3 | 38.5 |
| 3 | The DeepSeek breakthrough: Multi-Head Latent Attention (MLA) | 18 | 24 | 37 | 7 | 2 | 1 | 34.2 |
| 4 | Mixture-of-Experts (MoE) in DeepSeek: Scaling intelligence efficiently | 7 | 15 | 30 | 6 | 1 | 1 | 36.8 |
| 5 | Multi-token prediction and FP8 quantization | 6 | 17 | 31 | 6 | 0 | 1 | 38.6 |
| 6 | The DeepSeek training pipeline: Building a foundation model | 6 | 23 | 12 | 30 | 0 | 0 | 53.6 |
| 7 | Reinforcement learning: From policy gradients to GRPO | 16 | 28 | 15 | 5 | 4 | 0 | 50.9 |
| 8 | Knowledge distillation: Making powerful models practical | 9 | 28 | 31 | 4 | 2 | 8 | 47.3 |

## Extracted opening contract
- Every technical chapter opens with a numbered chapter title, then a compact **This chapter covers** block with exactly three bullets.
- The first paragraphs connect the previous chapter to the current bottleneck.
- Most chapters introduce or reuse a roadmap figure before the first major section.
- Explanations move from intuition to schematic, then to math or tensor shapes, then to implementation and empirical verification.

## Top-level section skeleton by chapter

### Chapter 1: Introduction to DeepSeek
- 1.1 Why DeepSeek? A turning point in open-source AI
- 1.2 The key innovations we will build
- 1.3 Book structure and scope
- 1.4 What this book will teach you and what it won’t
- 1.5 What you will need to follow along
- 1.6 Summary

### Chapter 2: Solving the inference bottleneck with the key-value cache
- 2.1 The LLM inference loop: Generating text one token at a time
- 2.2 The core task: Predicting the next token
- 2.3 The problem of redundant computations
- 2.4 The solution: Caching for efficiency
- 2.5 The dark side of the KV cache: The memory cost
- 2.6 The memory-first approach: Multi-Query Attention (MQA)
- 2.7 The middle ground: Grouped-Query Attention (GQA)
- 2.8 The performance vs. memory trade-off
- 2.9 Summary

### Chapter 3: The DeepSeek breakthrough: Multi-Head Latent Attention (MLA)
- 3.1 MLA: The best of both worlds
- 3.2 The MLA architecture: A visual walkthrough
- 3.3 The mathematical magic: How the latent matrix helps
- 3.4 The new inference loop with MLA
- 3.5 Quantifying the gains
- 3.6 Building an MLA module from scratch
- 3.7 The problem of order
- 3.8 Attempt #1: The naive approach - integer positional encodings
- 3.9 Attempt #2: A step forward - Binary positional encodings
- 3.10 Attempt #3: The "Attention Is All You Need" breakthrough - sinusoidal positional encodings
- 3.11 The state-of-the-art: Rotary Positional Encoding (RoPE)
- 3.12 The new challenge: Why standard RoPE and MLA don't mix
- 3.13 The incompatibility problem: Why standard MLA and RoPE don’t work together
- 3.14 The DeepSeek solution: Decoupled rotary position embedding
- 3.15 Quantifying the gains: The final cache memory comparison
- 3.16 Building MLA + decoupled RoPE from scratch
- 3.17 The Payoff: An Empirical Head-to-Head Comparison
- 3.18 Summary

### Chapter 4: Mixture-of-Experts (MoE) in DeepSeek: Scaling intelligence efficiently
- 4.1 The intuition behind mixture of experts
- 4.2 The mechanics of MoE: A hands-on mathematical walkthrough
- 4.3 The challenge of balance: Ensuring all experts contribute
- 4.4 The DeepSeek innovations: Towards ultimate expert specialization
- 4.5 Building a complete DeepSeek-MoE language model from scratch
- 4.6 The payoff: An empirical head-to-head comparison
- 4.7 Summary

### Chapter 5: Multi-token prediction and FP8 quantization
- 5.1 The core idea: From single-token to multi-token prediction
- 5.2 The four key advantages of MTP
- 5.3 The DeepSeek MTP architecture: A visual and mathematical walkthrough
- 5.4 Implementing a causal multi-token prediction module from scratch
- 5.5 Quantization: Trading precision for speed and memory
- 5.6 Summary

### Chapter 6: The DeepSeek training pipeline: Building a foundation model
- 6.1 The data foundation: Preparing the TinyStories dataset
- 6.2 Assembling the Mini-DeepSeek model
- 6.3 The training pipeline: Bringing the model to life
- 6.4 The engine of scale: Understanding DualPipe Parallelism
- 6.5 Model parallelism
- 6.6 Summary

### Chapter 7: Reinforcement learning: From policy gradients to GRPO
- 7.1 The reinforcement learning framework
- 7.2 Policy-gradient methods: Updating the LLM with rewards
- 7.3 Sampling actions instead of taking argmax
- 7.4 PPO: The standard practical baseline
- 7.5 GRPO: DeepSeek's value model simplification
- 7.6 Reinforcement learning with verifiable rewards
- 7.7 How reasoning emerges in DeepSeek-R1-Zero
- 7.8 DeepSeek-R1, R1-Zero, and Distill
- 7.9 Minimal chapter code
- 7.10 A worked GRPO example
- 7.11 From toy code to a real LLM trainer
- 7.12 What does this chapter add to the book?
- 7.13 A practical implementation checklist
- 7.14 Reading DeepSeek-R1 claims carefully
- 7.15 Common implementation pitfalls
- 7.16 Summary

### Chapter 8: Knowledge distillation: Making powerful models practical
- 8.1 Why 671 billion parameters won’t fit in your pocket
- 8.2 The teacher-student paradigm
- 8.3 Temperature and dark knowledge
- 8.4 Building the distillation loss: From naive to powerful
- 8.5 DeepSeek-R1’s distillation recipe
- 8.6 Implementing knowledge distillation in PyTorch
- 8.7 The payoff: An empirical head-to-head comparison
- 8.8 The limits of distillation
- 8.9 Summary

## Artifact count totals
| Artifact type | Count |
| --- | --- |
| figures | 190 |
| listings/code blocks | 63 |
| tables | 9 |
| callouts | 14 |
| equation blocks | 68 |
| images in EPUB | 225 |

## Common image dimensions
| Dimension | Count |
| --- | --- |
| 1042x581 | 38 |
| 1042x559 | 7 |
| 1042x584 | 4 |
| 1042x562 | 4 |
| 1042x444 | 4 |
| 1041x587 | 3 |
| 1042x570 | 3 |
| 1042x606 | 2 |
| 1042x620 | 2 |
| 1042x298 | 2 |
| 1022x904 | 2 |
| 1042x614 | 2 |