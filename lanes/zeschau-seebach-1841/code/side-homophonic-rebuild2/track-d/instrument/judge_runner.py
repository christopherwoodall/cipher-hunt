#!/usr/bin/env python3
"""Track D automated judge instrument — runner.

Two phases (spawning is done by the operating agent; this script handles
everything mechanical):

  prepare : verify frozen prompt hash (ABORT on mismatch), run the
            R5005 self-check grep over candidate texts (ABORT on hit),
            build seeded work items (fresh random order per pass),
            apply resume filtering, write worker briefs.
  collect : read worker return JSONs, mechanical first-line-int
            extraction, append to judge_log.jsonl in the pilot's exact
            format, run aggregation + verification.

Usage:
  judge_runner.py prepare --package <pkg.json> --outdir <run_dir>
      [--passes 3] [--batch-size 1] [--seed 9001] [--resume-from <log>]
      [--labels a,b,c] [--mode-label dry-run]
  judge_runner.py collect --rundir <run_dir> --results <results_dir>

The prompt is FROZEN (prompt_registry.json). Any hash mismatch aborts.
R5005 candidates never enter: the prepare phase greps every candidate
text for r5005|R5005|ct_R5005 and aborts on any hit.
"""
import argparse
import hashlib
import json
import os
import random
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
TRACKD = os.path.dirname(HERE)
PROMPT_PATH = os.path.join(TRACKD, 'judge_prompt.txt')
REGISTRY_PATH = os.path.join(HERE, 'prompt_registry.json')
TEMPLATE_PATH = os.path.join(HERE, 'worker_brief_template.md')

R5005_PAT = re.compile(r'r5005|R5005|ct_R5005')


def load_registry():
    return json.load(open(REGISTRY_PATH))


def verify_prompt():
    """Returns (prompt_text, sha). ABORTS (SystemExit) on mismatch."""
    reg = load_registry()
    raw = open(PROMPT_PATH, 'rb').read()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != reg['sha256']:
        print(f'FATAL: prompt hash mismatch.\n  expected: {reg["sha256"]}\n  computed: {sha}',
              file=sys.stderr)
        print('The prompt is FROZEN. Any change = re-registration + new pilot.', file=sys.stderr)
        sys.exit(2)
    print(f'prompt OK: sha256 {sha[:16]}... (frozen {reg["frozen_date"]})')
    return raw.decode('utf-8'), sha


def r5005_selfcheck(texts):
    """ABORTS on any R5005 marker in candidate texts. Logs the grep."""
    hits = [lab for lab, t in texts.items() if R5005_PAT.search(t)]
    print(f'R5005 self-check: scanned {len(texts)} candidate texts, '
          f'{len(hits)} hits: {hits if hits else "none"}')
    if hits:
        print('FATAL: R5005 marker in candidate texts. Control instances only.',
              file=sys.stderr)
        sys.exit(3)
    return True


def load_package(path):
    doc = json.load(open(path))
    if isinstance(doc, dict) and 'candidates' in doc:
        # pilot candidates.json shape: {candidates: {label: {text...}}, meta}
        cands = doc['candidates']
        texts = {}
        for lab, c in cands.items():
            texts[lab] = c['text'] if isinstance(c, dict) else c
        return texts, doc.get('meta', {})
    # flat shape: {label: text}
    return {k: (v['text'] if isinstance(v, dict) else v) for k, v in doc.items()}, {}


def already_logged(log_path):
    done = set()
    if log_path and os.path.exists(log_path):
        for line in open(log_path):
            line = line.strip()
            if not line:
                continue
            e = json.loads(line)
            done.add((e['candidate_label'], e['pass_no']))
    return done


def build_work_items(labels, passes, seed):
    """Fresh random order per pass, seeded. Returns list of dicts."""
    items = []
    for p in range(1, passes + 1):
        rng = random.Random(seed + p)
        seq = list(labels)
        rng.shuffle(seq)
        for lab in seq:
            items.append({'candidate_label': lab, 'pass_no': p})
    return items


def cmd_prepare(args):
    prompt_text, sha = verify_prompt()
    texts, meta = load_package(args.package)
    if args.labels:
        want = set(args.labels.split(','))
        texts = {k: v for k, v in texts.items() if k in want}
        missing = want - set(texts)
        if missing:
            print(f'FATAL: labels not in package: {missing}', file=sys.stderr)
            sys.exit(4)
    print(f'package: {args.package} -> {len(texts)} candidates')
    r5005_selfcheck(texts)

    labels = sorted(texts)
    items = build_work_items(labels, args.passes, args.seed)
    print(f'work items: {len(items)} ({len(labels)} labels x {args.passes} passes, '
          f'order seed {args.seed})')

    # resume: skip already-logged (label, pass_no)
    log_path = os.path.join(args.outdir, 'judge_log.jsonl')
    done = already_logged(log_path if args.resume_from else None)
    if args.resume_from and args.resume_from != log_path:
        done |= already_logged(args.resume_from)
    if done:
        before = len(items)
        items = [it for it in items
                 if (it['candidate_label'], it['pass_no']) not in done]
        print(f'resume: skipped {before - len(items)} already-logged, '
              f'{len(items)} remaining')

    # batch into workers
    briefs_dir = os.path.join(args.outdir, 'briefs')
    os.makedirs(briefs_dir, exist_ok=True)
    template = open(TEMPLATE_PATH).read()
    # BYTE CONTRACT: the worker verifies the prompt by hashing the FILE
    # at PROMPT_ABSPATH (shared filesystem) and comparing to the
    # registry sha256. The brief also embeds the prompt text for
    # reference, but the file is authoritative. The runner verified the
    # file hash in verify_prompt() before building any brief.
    prompt_block = prompt_text
    brief_abspath = os.path.abspath(PROMPT_PATH)
    batches, brief_paths = [], []
    for i in range(0, len(items), args.batch_size):
        chunk = items[i:i + args.batch_size]
        wid = f'w{i // args.batch_size:04d}'
        assigns = [{'candidate_label': it['candidate_label'],
                    'pass_no': it['pass_no'],
                    'text': texts[it['candidate_label']]} for it in chunk]
        brief = (template
                 .replace('{PROMPT_SHA256}', sha)
                 .replace('{PROMPT_ABSPATH}', brief_abspath)
                 .replace('{N_ASSIGNMENTS}', str(len(assigns)))
                 .replace('{ASSIGNMENTS_JSON}', json.dumps(assigns, ensure_ascii=False, indent=1))
                 .replace('{PROMPT_TEXT}', prompt_block)
                 .replace('{WORKER_ID}', wid))
        bp = os.path.join(briefs_dir, f'brief-{wid}.md')
        open(bp, 'w').write(brief)
        brief_paths.append(bp)
        batches.append({'worker_id': wid, 'brief': bp, 'items': chunk})

    manifest = {
        'mode': args.mode_label,
        'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'package': os.path.abspath(args.package),
        'package_meta': meta,
        'prompt_sha256': sha,
        'prompt_path': os.path.abspath(PROMPT_PATH),
        'passes': args.passes,
        'order_seed': args.seed,
        'batch_size': args.batch_size,
        'labels': labels,
        'n_work_items': len(items),
        'n_workers': len(batches),
        'r5005_selfcheck': 'pass (0 hits)',
        'briefs': brief_paths,
    }
    os.makedirs(args.outdir, exist_ok=True)
    json.dump(manifest, open(os.path.join(args.outdir, 'manifest.json'), 'w'), indent=1)
    json.dump(batches, open(os.path.join(args.outdir, 'work_batches.json'), 'w'), indent=1)
    print(f'wrote {len(batches)} worker briefs -> {briefs_dir}/')
    print(f'manifest -> {args.outdir}/manifest.json')
    print('NEXT: spawn one worker subagent per brief (brief text = the '
          'subagent task), collect their JSON returns into <results_dir>/, '
          'then run: judge_runner.py collect')


def extract_score(raw_response):
    """Mechanical first-line-int extraction. Returns int or raises."""
    first = raw_response.split('\n', 1)[0].strip()
    m = re.fullmatch(r'\d+', first)
    if not m:
        raise ValueError(f'first line not a bare integer: {first!r}')
    v = int(m.group(0))
    if not (0 <= v <= 100):
        raise ValueError(f'score out of range 0-100: {v}')
    return v


def cmd_collect(args):
    prompt_text, sha = verify_prompt()  # re-verify at collect time too
    manifest = json.load(open(os.path.join(args.rundir, 'manifest.json')))
    if manifest['prompt_sha256'] != sha:
        print('FATAL: prompt changed between prepare and collect.', file=sys.stderr)
        sys.exit(2)

    # read worker returns
    results = []
    rdir = args.results
    for fn in sorted(os.listdir(rdir)):
        if not fn.endswith('.json'):
            continue
        doc = json.load(open(os.path.join(rdir, fn)))
        if doc.get('aborted'):
            print(f'FATAL: worker {fn} aborted: {doc.get("reason")}', file=sys.stderr)
            sys.exit(5)
        if doc.get('prompt_sha256_computed') != sha:
            print(f'FATAL: worker {fn} computed prompt hash '
                  f'{doc.get("prompt_sha256_computed")} != frozen {sha}', file=sys.stderr)
            sys.exit(6)
        for r in doc['results']:
            r['_worker_id'] = doc.get('worker_id', fn)
            results.append(r)
    print(f'collected {len(results)} judgments from {rdir}/')

    # mechanical extraction + append in pilot format
    log_path = os.path.join(args.rundir, 'judge_log.jsonl')
    seen = already_logged(log_path)
    n_new, n_fail = 0, 0
    with open(log_path, 'a') as f:
        for r in results:
            key = (r['candidate_label'], r['pass_no'])
            if key in seen:
                print(f'  SKIP duplicate: {key}')
                continue
            try:
                score = extract_score(r['raw_response'])
            except ValueError as e:
                # EXTRACTION-FAILED: logged, excluded, never re-queried
                n_fail += 1
                print(f'  EXTRACTION-FAILED {key}: {e} (logged, excluded, no re-query)')
                continue
            entry = {
                'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
                'candidate_label': r['candidate_label'],
                'pass_no': r['pass_no'],
                'prompt_sha256': sha,
                'raw_response': r['raw_response'],
                'extracted_score': score,
            }
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
            seen.add(key)
            n_new += 1
    print(f'appended {n_new} entries to {log_path} '
          f'({n_fail} extraction-failed, excluded per protocol)')
    print('NEXT: run aggregate.py for medians, range checks, completeness.')


def main():
    ap = argparse.ArgumentParser(description='Track D judge instrument runner')
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('prepare')
    p.add_argument('--package', required=True)
    p.add_argument('--outdir', required=True)
    p.add_argument('--passes', type=int, default=3)
    p.add_argument('--batch-size', type=int, default=1)
    p.add_argument('--seed', type=int, default=9001)
    p.add_argument('--resume-from', default=None)
    p.add_argument('--labels', default=None)
    p.add_argument('--mode-label', default='run')
    c = sub.add_parser('collect')
    c.add_argument('--rundir', required=True)
    c.add_argument('--results', required=True)
    args = ap.parse_args()
    if args.cmd == 'prepare':
        cmd_prepare(args)
    else:
        cmd_collect(args)


if __name__ == '__main__':
    main()
