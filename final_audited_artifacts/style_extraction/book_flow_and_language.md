# Book flow and language extraction

## Reusable chapter rhythm

Use the following rhythm as the default for *MoE Models from Scratch*:

1. **Chapter title**: numbered, direct, and technical. The title names the bottleneck or mechanism, not only the component.
2. **This chapter covers**: three bullets. Each bullet should correspond to a reader outcome: intuition, mechanism, implementation/verification.
3. **Bridge paragraph**: connect the prior chapter's result to the new problem. The source book repeatedly uses this to make the book feel like one build rather than isolated essays.
4. **Roadmap or context figure**: show where the current topic fits in the whole model or training pipeline.
5. **Problem-first motivation**: make the computational bottleneck concrete before introducing the solution.
6. **Visual walkthrough**: use a schematic diagram before equations or code.
7. **Tensor/math walkthrough**: specify shapes, projections, losses, or routing equations.
8. **From-scratch implementation**: present compact PyTorch or Python code, with code annotations when the listing is dense.
9. **Check or comparison**: include a toy run, memory/FLOP comparison, load histogram, routing visualization, or benchmark-style table.
10. **Summary and bridge**: close by naming what was built and why the next chapter is needed.

## Voice rules to preserve

- Use first-person plural sparingly but consistently: "we build", "we trace", "we now have".
- Prefer direct transitions: "Let's trace the flow", "Now we hit the key problem", "This is where the router enters".
- Introduce abstractions through a concrete failure mode. Example pattern: dense FFNs are expensive -> sparse experts activate only a subset -> routing creates load-balancing problems.
- Keep the reader oriented with shapes, small examples, and one-sentence takeaways after diagrams.
- Avoid long theorem-style blocks. The source style is practical and explanatory, not proof-heavy.
- End sections with a local payoff: what the reader can now understand, implement, measure, or debug.

## Quantitative writing signals extracted

- Chapters use a consistent three-bullet opening summary.
- Paragraphs average about 42.0 words across parsed chapter body paragraphs, with a median of 41.0 words.
- Transition phrases are common enough to matter: "let's" (112), "however" (42), "to understand" (40), "as illustrated" (22), and "step" (200).
- The book relies heavily on figures: 190 figure containers across eight chapters, compared with 63 listing/code containers and 9 table containers.

## Section-level explanation loop

Each major section should generally include these beats:

| Beat | Purpose | MoE-book equivalent |
|---|---|---|
| Bottleneck | Explain why the dense or naive method fails | dense FFN cost, unstable routing, expert collapse, all-to-all overhead |
| Schematic | Show the moving parts | tokens -> router -> top-k experts -> weighted combine |
| Shapes | Prevent ambiguity | `(batch, seq, d_model)`, `(tokens, n_experts)`, expert capacity |
| Equation | Pin down the operation | router softmax, top-k mask, auxiliary loss, z-loss, capacity overflow |
| Code | Make it executable | small PyTorch module with explicit dimensions |
| Diagnostic | Make it trustworthy | histograms, expert load tables, gradient checks, sanity tests |
| Bridge | Explain why the next layer of complexity is needed | top-1 routing -> top-2 routing -> balancing -> distributed MoE |

## Style guardrails for new prose

- Prefer short setup examples: 4 tokens, 4 experts, top-2 routing, small hidden sizes.
- Introduce names only after the reader sees the problem they solve.
- Do not overload one section with both algorithm and systems details. Separate routing math, PyTorch implementation, and distributed execution.
- When a figure appears, its surrounding prose must answer: what should the reader notice, and what changes after this figure?
