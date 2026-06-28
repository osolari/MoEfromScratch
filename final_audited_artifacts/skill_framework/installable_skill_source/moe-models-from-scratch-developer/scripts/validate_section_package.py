#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, sys
from pathlib import Path

def read(p: Path) -> str:
    try:
        return p.read_text(encoding='utf-8')
    except FileNotFoundError:
        return ''

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--book-root', required=True)
    ap.add_argument('--section-index', required=True)
    ap.add_argument('--section')
    args=ap.parse_args()
    root=Path(args.book_root)
    rows=list(csv.DictReader(Path(args.section_index).open(encoding='utf-8')))
    errors=[]; checked=0
    for r in rows:
        if args.section and r.get('section') != args.section: continue
        checked+=1
        sec=read(root/r['section_tex'])
        if not sec:
            errors.append(f"missing section file: {r['section_tex']}"); continue
        for key in ['figure','table','equation','listing']:
            inc='\\input{'+r[key].replace('latex_book_skeleton/','').replace('.tex','')+'}'
            if inc not in sec:
                errors.append(f"{r.get('section')}: missing {inc}")
            wrap=read(root/r[key])
            if not wrap:
                errors.append(f"{r.get('section')}: missing wrapper {r[key]}")
    if checked==0: errors.append('no matching sections')
    if errors:
        print('validation failed')
        for e in errors: print('- '+e)
        return 1
    print(f'validation passed for {checked} section(s)')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
