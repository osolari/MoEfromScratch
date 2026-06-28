# Phase 6 report - section-by-section skill framework

Phase 6 converts the LaTeX-first section development briefs for *MoE Models from Scratch* into skill-oriented markdown files.

## Deliverables

| Deliverable | Count |
|---|---:|
| Overall book-development skill-style markdown | 1 |
| Chapter-level skill-style markdown files | 12 |
| Section-level skill-style markdown files | 72 |
| Literal `SKILL.md` mirror files | 85 |
| Installable ChatGPT skill source directory | 1 |
| Referenced section briefs inside installable skill | 72 |

## Key design choice

The package contains both standalone skill markdown files and a single uploadable skill. The standalone files are best for opening one section in a new chat. The uploadable skill is best for reuse inside ChatGPT because it uses progressive loading: load the overall `SKILL.md`, then load only the relevant chapter or section reference.

## Preserved constraints

- Book development is LaTeX-first.
- Every artifact remains a separate `.tex` wrapper included through `\input`.
- TikZ is required for mechanism schematics.
- Generated plots and dashboards are included as PDF assets through wrapper files.
- MiniDeepSeekMoE remains the reference model.
- Router bias affects selection only; unbiased selected scores determine combine weights.

## How to use in a separate section-development chat

1. Open the matching file under `standalone_skill_mds/sections/chXX/` or `individual_skill_dirs/sections/chXX/slug/SKILL.md`.
2. Paste it as the section-development framework.
3. Ask the chat to develop that exact section in LaTeX.
4. Require updates only to the listed `.tex` section and artifact wrapper paths.
5. Run the diagnostic named in the skill markdown.

## Validation summary

See `validation/phase6_validation_notes.md` and `validation/phase6_final_validation.json`.

## Packaging validation

The consolidated skill was packaged with the official `package_skill.py` validator. Result: passed. Package: `skill.zip` (549,785 bytes).
