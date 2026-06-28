from pathlib import Path
import csv, json, re, os, subprocess, zipfile

ROOT=Path(__file__).resolve().parents[1]
KIT=ROOT/'final_audited_artifacts'
errors=[]; warnings=[]; stats={}

def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)

# Section and artifact audit
idx=KIT/'section_data/section_brief_index.csv'
rows=list(csv.DictReader(open(idx)))
stats['sections']=len(rows)
stats['chapters']=len(set(r['chapter'] for r in rows))
for row in rows:
    for k in ['brief_path','session_starter_path','section_tex','figure','table','listing','equation']:
        p=KIT/row[k]
        if not p.exists(): err(f"missing {k}: {row[k]}")
    if (KIT/row['section_tex']).exists():
        t=(KIT/row['section_tex']).read_text(errors='replace')
        for k in ['figure','table','equation','listing']:
            rel=row[k].replace('latex_book_skeleton/','').replace('.tex','')
            if f"\\input{{{rel}}}" not in t: err(f"section {row['section']} missing {rel}")
        for env in ['figure','table','lstlisting','equation']:
            if re.search(r'\\begin\{'+env+r'\}', t): err(f"section {row['section']} inlines {env}")
    if (KIT/row['brief_path']).exists():
        t=(KIT/row['brief_path']).read_text(errors='replace')
        if 'default figure/table wrappers use `[H]`' not in t: err(f"brief missing final float rule: {row['brief_path']}")

# Wrapper audit
for d in ['figures','tables','listings','equations']:
    stats[f'{d}_wrappers']=len(list((KIT/'latex_book_skeleton'/d).glob('ch??/*.tex')))
figs=list((KIT/'latex_book_skeleton/figures').glob('ch??/*.tex'))
tabs=list((KIT/'latex_book_skeleton/tables').glob('ch??/*.tex'))
stats['tikz_figures']=sum('tikzpicture' in p.read_text(errors='replace') for p in figs)
stats['includegraphics_figures']=sum('includegraphics' in p.read_text(errors='replace') for p in figs)
stats['figure_wrappers_with_H']=sum('\\begin{figure}[H]' in p.read_text(errors='replace') for p in figs)
stats['table_wrappers_with_H']=sum('\\begin{table}[H]' in p.read_text(errors='replace') for p in tabs)
if stats['figure_wrappers_with_H'] != len(figs): err('not all figure wrappers use [H]')
if stats['table_wrappers_with_H'] != len(tabs): err('not all table wrappers use [H]')
main=(KIT/'latex_book_skeleton/main.tex').read_text(errors='replace')
for pkg in ['\\usepackage{float}','\\usepackage[section]{placeins}']:
    if pkg not in main: err(f'main.tex missing {pkg}')

# Check wrapper content
checks={
    'figure':['\\begin{figure}[H]','\\caption{','\\label{'],
    'table':['\\begin{table}[H]','\\caption{','\\label{'],
    'listing':['\\begin{lstlisting}','caption={','label={'],
    'equation':['\\begin{equation}','\\label{'],
}
for row in rows:
    for k,needles in checks.items():
        p=KIT/row[k]
        if p.exists():
            t=p.read_text(errors='replace')
            for n in needles:
                if n not in t: err(f"{row['section']} {k} missing {n}: {row[k]}")

# Skill audit
skill_zip=ROOT/'skill.zip'
stats['skill_zip_bytes']=skill_zip.stat().st_size if skill_zip.exists() else 0
if not skill_zip.exists(): err('missing top-level skill.zip')
if stats['skill_zip_bytes'] > 25_000_000: err('skill.zip exceeds 25 MB')
log=(ROOT/'validation/skill_package_phase7.log')
if not log.exists() or 'Successfully packaged skill' not in log.read_text(errors='replace'):
    err('skill_package_phase7.log does not confirm successful packaging')
skill_root=KIT/'skill_framework/installable_skill_source/moe-models-from-scratch-developer'
skill_entry=skill_root/'SKILL.md'
if not skill_entry.exists(): err('missing installable skill SKILL.md')
else:
    t=skill_entry.read_text(errors='replace')
    if 'default figure/table wrappers use `[H]`' not in t: err('installable skill missing final [H] rule')
    refs=re.findall(r'`(references/[^`]+)`', t)
    miss=[]
    for ref in refs:
        if 'chXX' in ref: continue
        if not (skill_root/ref).exists(): miss.append(ref)
    if miss: err('missing skill refs: '+', '.join(miss[:5]))
    stats['skill_references_checked']=len(refs)-sum('chXX' in r for r in refs)
stats['standalone_section_skill_mds']=len(list((KIT/'skill_framework/standalone_skill_mds/sections').glob('ch??/*.skill.md')))
stats['literal_skill_md_mirrors']=len(list((KIT/'skill_framework/individual_skill_dirs').rglob('SKILL.md')))

# LaTeX/PDF audit
compile_log=ROOT/'validation/latex_compile_phase7.log'
if not compile_log.exists() or 'Output written on main.pdf' not in compile_log.read_text(errors='replace'):
    err('latex compile log does not confirm PDF output')
pdf=ROOT/'validation/phase7_latex_skeleton_preview.pdf'
if not pdf.exists(): err('missing phase7 preview PDF')
else:
    try:
        out=subprocess.check_output(['pdfinfo', str(pdf)], text=True)
        m=re.search(r'Pages:\s+(\d+)', out)
        if m: stats['preview_pdf_pages']=int(m.group(1))
    except Exception as e:
        warn('pdfinfo failed: '+str(e))
preview_text=ROOT/'validation/preview_text.txt'
if preview_text.exists():
    text=preview_text.read_text(errors='replace')
    order_items=['Figure 10.4','10.5\n\nFull-model smoke tests','Figure 10.5','10.6\n\nChapter summary and handoff','Figure 10.6']
    positions=[text.find(x) for x in order_items]
    stats['float_order_probe_positions']=positions
    if any(p<0 for p in positions) or positions != sorted(positions):
        err('float order probe failed for Chapter 10.4-10.6')
else:
    warn('preview_text.txt not found; float order probe skipped')
render_dir=ROOT/'validation/rendered_preview'
stats['rendered_preview_pages']=len(list(render_dir.glob('*.png'))) if render_dir.exists() else 0
if stats['rendered_preview_pages'] < 6: warn('fewer than 6 rendered preview pages found')

summary={'stats':stats,'error_count':len(errors),'warning_count':len(warnings),'errors':errors,'warnings':warnings,'overall_pass':not errors}
(ROOT/'validation/phase7_validation_summary.json').write_text(json.dumps(summary, indent=2))
with open(ROOT/'validation/phase7_validation_checks.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['check','status','detail'])
    w.writerow(['section_count','pass' if stats['sections']==72 else 'fail',stats['sections']])
    w.writerow(['artifact_counts','pass' if all(stats.get(f'{d}_wrappers')==72 for d in ['figures','tables','listings','equations']) else 'fail',json.dumps({k:v for k,v in stats.items() if k.endswith('_wrappers')})])
    w.writerow(['float_pinning','pass' if stats['figure_wrappers_with_H']==72 and stats['table_wrappers_with_H']==72 else 'fail',f"fig H={stats['figure_wrappers_with_H']}, tab H={stats['table_wrappers_with_H']}"])
    w.writerow(['skill_package','pass' if skill_zip.exists() and stats['skill_zip_bytes']<=25_000_000 else 'fail',stats['skill_zip_bytes']])
    w.writerow(['latex_compile','pass' if pdf.exists() else 'fail',stats.get('preview_pdf_pages','unknown')])
    w.writerow(['float_order_probe','pass' if 'float order probe failed for Chapter 10.4-10.6' not in errors else 'fail',stats.get('float_order_probe_positions')])
    w.writerow(['overall','pass' if not errors else 'fail',f"{len(errors)} errors"])
print(json.dumps(summary, indent=2))
