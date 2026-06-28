# HOWTOEDIT.md — Editing *MoE Models from Scratch* with Claude Code

This file explains what **you** should do, what to ask **Claude Code** to do, and which prompts to use while completing the book from the audited artifacts.

The safest workflow is **not** “ask Claude Code to write the whole book.” Use Claude Code as a section-by-section LaTeX production agent:

```text
one section brief
→ one section draft
→ artifact wrappers completed
→ diagnostics/code updated
→ validator passes
→ LaTeX compiles
→ commit
→ next section
```

## 1. Your one-time setup

Start from the Phase 7 final package.

```bash
unzip moe_from_scratch_phase7.zip
cd moe_from_scratch_phase7_final/final_audited_artifacts

git init
git add .
git commit -m "Initialize audited MoE Models from Scratch book skeleton"
```

Install the Claude Code skill from the extracted skill source, not from the top-level `skill.zip`:

```bash
mkdir -p .claude/skills
cp -R skill_framework/installable_skill_source/moe-models-from-scratch-developer \
  .claude/skills/
```

Copy the included Claude memory file into the repo root:

```bash
cp claude_code_prompts/CLAUDE.md ./CLAUDE.md
git add CLAUDE.md .claude/skills claude_code_prompts HOWTOEDIT.md
git commit -m "Add Claude Code editing workflow"
```

Then start Claude Code from the repo root:

```bash
claude
```

## 2. Your normal editing loop

Use this order for every section:

1. Pick one section from `section_data/section_brief_index.csv`.
2. Open a fresh Claude Code session or continue the current chapter session.
3. Paste the section-development prompt from `claude_code_prompts/02_section_development_prompt.md`.
4. Replace the section number, brief path, and target section file.
5. Let Claude Code edit only the target section and its planned artifact wrappers.
6. Require it to run the validator and compile the book.
7. Review the diff yourself.
8. Commit only when the section compiles and the prose/artifacts are acceptable.

Recommended commit pattern:

```bash
git status
git diff --stat
git diff
# read the PDF preview if needed
git add latex_book_skeleton codebase_or_scripts_if_added
git commit -m "Draft section 03.02 router scores and tensor shapes"
```

## 3. What you should not ask Claude Code to do

Avoid prompts like these:

```text
Write the whole book.
Finish all chapters.
Make it better.
Expand every section.
Rewrite the LaTeX skeleton.
Ignore the planned artifact structure.
```

Those prompts are too broad. They encourage drift, repeated explanations, broken artifact paths, and inconsistent notation.

## 4. What Claude Code should do

Claude Code should:

- read the relevant section brief before editing;
- edit only the target section and planned wrappers;
- keep `figure`, `table`, `lstlisting`, and equation environments out of section prose;
- include artifacts only with `\input{...}`;
- keep wrappers standalone;
- preserve `[H]` float placement for planned teaching figures/tables;
- use TikZ for mechanism diagrams;
- use generated PDF assets only for plots, dashboards, and diagnostics;
- preserve the MiniDeepSeekMoE invariant:

```text
router bias affects expert selection only;
final combine weights are computed from unbiased selected scores.
```

## 5. First Claude Code prompt

Use this first, before any edits:

```text
/moe-models-from-scratch-developer

Do not edit files yet.

Inspect the project structure and read these files:

- README_START_HERE.md if present
- latex_book_skeleton/main.tex
- planning_guides/latex_artifact_contract.md
- planning_guides/visual_theme_contract.md
- planning_guides/proofread_checklist.md
- section_data/section_brief_index.csv
- .claude/skills/moe-models-from-scratch-developer/SKILL.md

Then report:

1. the book production workflow,
2. the exact validation commands you will use,
3. the section-by-section development protocol,
4. any missing tools or environment issues.

Do not make changes until I approve the protocol.
```

This same prompt is saved as:

```text
claude_code_prompts/01_setup_and_protocol_prompt.md
```

## 6. Section-development prompt

Use this template for each section:

```text
/moe-models-from-scratch-developer

Develop Section <SECTION_NUMBER> only.

Target brief:
<section_development_briefs/chXX/NN-section-slug.md>

Target section file:
latex_book_skeleton/chapters/chXX/sections/NN-section-slug.tex

Instructions:

1. Read the section brief completely.
2. Read the relevant chapter packet if needed.
3. Edit only the target section file and the planned artifact wrappers named in the brief.
4. Keep figure/table/listing/equation environments out of the section prose.
5. Include artifacts only with the planned `\input{...}` lines.
6. Implement the planned TikZ figure/table/equation/listing placeholders as real teaching artifacts.
7. Preserve the visual theme and color map from the planning guide.
8. Add or update code only if the section brief requires it.
9. Run the section validator for section <SECTION_NUMBER>.
10. Compile the LaTeX book.
11. Report changed files and paste the validation/compile evidence.

Do not edit any other section.
```

Saved as:

```text
claude_code_prompts/02_section_development_prompt.md
```

## 7. Chapter integration pass

After all six sections of a chapter are drafted and committed, use:

```text
/moe-models-from-scratch-developer

Perform a Chapter <CHAPTER_NUMBER> integration pass.

Scope:

- latex_book_skeleton/chapters/chXX/chapter.tex
- latex_book_skeleton/chapters/chXX/sections/*.tex
- latex_book_skeleton/figures/chXX/*.tex
- latex_book_skeleton/tables/chXX/*.tex
- latex_book_skeleton/listings/chXX/*.tex
- latex_book_skeleton/equations/chXX/*.tex

Tasks:

1. Do not introduce new planned artifacts unless necessary.
2. Smooth transitions between sections.
3. Remove repeated explanations.
4. Check that notation is introduced before use.
5. Check that every figure/table/listing/equation is referenced in prose.
6. Check that diagnostics are falsifiable.
7. Preserve every `\input{...}` artifact pattern.
8. Compile the book.
9. Report changed files and remaining issues.

Do not rewrite the chapter from scratch.
```

Saved as:

```text
claude_code_prompts/03_chapter_integration_prompt.md
```

## 8. Technical review pass

Use a separate Claude Code session or a clean worktree for review:

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

Saved as:

```text
claude_code_prompts/04_chapter_review_prompt.md
```

## 9. Safe parallel work

Parallelize by chapter, not by section inside the same chapter and not by shared files.

Example:

```bash
git worktree add ../moe-ch03 ch03-draft
cd ../moe-ch03
claude
```

Ask that session to work only on Chapter 3. Do not let multiple Claude Code sessions edit `main.tex`, shared style files, or the same chapter at the same time.

## 10. Final whole-book audit

After all chapter branches are merged:

```text
/moe-models-from-scratch-developer

Perform the final whole-book production audit.

Scope:
latex_book_skeleton/

Tasks:

1. Compile the full book.
2. Check all section files for raw figure/table/listing/equation environments.
3. Check that all planned artifact wrappers exist.
4. Check that every wrapper has a caption and label where appropriate.
5. Check that TikZ figures follow the visual theme.
6. Check that all MiniDeepSeekMoE invariants are preserved.
7. Check that Chapter 9 never uses router bias to compute final combine weights.
8. Check notation consistency across chapters.
9. Check code listing consistency with the codebase.
10. Produce a final punch list before making edits.

Do not make broad rewrites unless they address a concrete issue.
```

Saved as:

```text
claude_code_prompts/05_final_whole_book_audit_prompt.md
```

## 11. Required validation commands

Ask Claude Code to use these commands after each section edit.

Section validator:

```bash
python .claude/skills/moe-models-from-scratch-developer/scripts/validate_section_package.py \
  --book-root . \
  --section-index section_data/section_brief_index.csv \
  --section <SECTION_NUMBER>
```

LaTeX compile:

```bash
cd latex_book_skeleton
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Fallback if `latexmk` is unavailable:

```bash
cd latex_book_skeleton
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## 12. Your acceptance checklist before committing

Before committing a section, check:

- the section did not edit unrelated chapters;
- section prose contains only prose plus planned `\input{...}` lines;
- artifact wrappers are standalone and compile;
- every figure/table/listing/equation is referenced in prose;
- the diagnostic is concrete and falsifiable;
- all tensor shapes are defined before use;
- router-bias behavior is correct;
- the full LaTeX book compiles;
- the Git diff is small enough to review.

## 13. Suggested section order

Draft in chapter order unless there is a strong reason not to:

```text
Chapter 1 → Chapter 2 → ... → Chapter 12
```

Within each chapter, draft sections 1 through 6, then run the chapter integration pass.

## 14. Emergency recovery

If Claude Code makes a broad or messy edit:

```bash
git status
git diff --stat
git restore <bad-file>
# or abandon all uncommitted changes:
git restore .
```

Then restart with a narrower prompt that names exactly one section file and its planned wrappers.
