# Proofread checklist

- The section opens from a concrete local problem.
- The figure appears before dense math or code.
- Every tensor in the equation and code listing has a shape or role.
- The diagnostic can catch a realistic implementation bug.
- The table adds structure rather than repeating prose.
- No raw figure/table/listing/equation environments are in section prose.
- All artifacts are included by `\input`.
- The final paragraph bridges to the next planned section.
- The MiniDeepSeekMoE invariant is preserved where relevant: router bias affects selection only, not unbiased combine weights.
