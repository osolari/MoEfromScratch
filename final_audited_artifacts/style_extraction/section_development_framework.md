# Section development framework extracted from the template book

This is a reusable section-development scaffold. It will become the basis for the section-by-section skill files in a later phase, after the MoE model and chapter plan are confirmed.

## Default section scaffold

1. **Local objective**: one paragraph that states what problem this section solves.
2. **Reader promise**: one sentence saying what the reader will be able to implement or reason about by the end.
3. **Mini-example**: a small, concrete token/expert/tensor setup.
4. **Diagram**: a TikZ schematic, included through a figure wrapper.
5. **Mechanics**: shape-aware explanation of the operation.
6. **Equation or algorithm**: only after the diagram has made the components intuitive.
7. **Code listing**: minimal executable code, included through a listing wrapper.
8. **Check**: a numerical sanity check, table, plot placeholder, or debugging rule.
9. **Bridge**: the limitation that motivates the next section.

## Artifact placeholders required in every detailed plan

Each future section plan should declare:

- Figures: filename, type (`TikZ` or external PDF), purpose, caption placeholder, label.
- Tables: filename, columns, row categories, caption placeholder, label.
- Listings: filename, language, function/class name, caption placeholder, label.
- Equations: label and notation dependencies.
- Diagnostics: plots, histograms, toy outputs, or tables needed to verify the implementation.

## Language pattern for section starts

Use a practical problem opening, then a visual anchor:

```text
The dense version works, but it pays the same cost for every token. To see why MoE changes that cost profile, we will route four tokens through a tiny bank of experts and track the shapes at each step.
```

Then immediately include the planned schematic with `\input{...}`.

## Language pattern for section endings

End with a bridge, not a generic summary:

```text
We can now route tokens to experts, but our router has no reason to use the experts evenly. The next section turns that failure into a measurable load-balancing objective.
```
