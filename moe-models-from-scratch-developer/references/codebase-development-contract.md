# Codebase development contract

The companion repository should remain chapter-first, matching the attached source codebase style.

- Earlier chapters may use notebooks for visual walkthroughs.
- Later chapters should use scripts and smoke tests for repeatability.
- Promote code to `common/` only after at least two chapters reuse it.
- All tensor operations shown in prose should have shape assertions, diagnostics, or both.
- Keep listings in the book short and aligned with runnable code.
- Prefer readable PyTorch over optimized kernels until the inference/scaling chapter.
