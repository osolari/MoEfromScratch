# Prompt 04 — Technical review pass

Use this in a separate Claude Code session or clean worktree.

```text
/moe-models-from-scratch-developer

Review Chapter <CHAPTER_NUMBER> as a technical editor.

Do not edit files first.

Check for:

1. mathematical inaccuracies,
2. missing tensor shapes,
3. incorrect routing terminology,
4. broken MiniDeepSeekMoE invariants,
5. artifact/prose mismatch,
6. weak or unfalsifiable diagnostics,
7. LaTeX compilation risks,
8. places where prose drifts into survey mode instead of from-scratch build mode.

Return a concrete issue list with file paths and recommended fixes.

After I approve the fixes, apply them and compile.
```
