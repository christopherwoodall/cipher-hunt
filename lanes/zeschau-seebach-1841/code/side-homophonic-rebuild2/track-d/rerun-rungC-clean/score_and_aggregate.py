#!/usr/bin/env python3
"""Mechanical scoring + aggregation for the rung-C clean re-run.

MECHANICAL ONLY — no verdict language. Scoring happens from checksummed disk
copies only. Any hardening-check failure HALTS with an explicit report.

Inputs (all in rerun-rungC-clean/):
  rungC-clean-pkg-{1,2,3}.json, rungC-clean-schedules.json,
  judge-log-clean-agent{1,2,3}.jsonl, handoff-checksums.json (judge-reported
  log sha256, transport), _KEY_V3C_CLEAN_DO_NOT_OPEN.json (opened last).

Outputs:
  INTEGRITY-MANIFEST.json, aggregation-clean.json, MECHANICAL-SUMMARY.md
"""
import json, os, sys, hashlib, re, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
TRACKD = os.path.dirname(HERE)
PROMPT_SHA = 'd907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e'
GATE = ['184201', '184202', '184203', '184204', '184206', '184207']
R5005 = re.compile(r'(?i)r5005|ct_r5005')
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def halt(msg):
    print(f'HALT: {msg}')
    sys.exit(2)

manifest = {'created_utc': now(), 'files': {}}

# --- 1. receipt: checksum every judge log BEFORE any read ---
logs = {}
handoff_path = os.path.join(HERE, 'handoff-checksums.json')
if not os.path.exists(handoff_path):
    halt('handoff-checksums.json missing — cannot perform handoff<->disk cross-check')
reported = json.load(open(handoff_path))
for n in (1, 2, 3):
    lp = os.path.join(HERE, f'judge-log-clean-agent{n}.jsonl')
    if not os.path.exists(lp):
        halt(f'judge log {n} missing')
    disk_sha = sha(lp)
    manifest['files'][f'judge-log-clean-agent{n}.jsonl'] = disk_sha
    rep = reported.get(str(n))
    if rep is None:
        halt(f'judge {n}: no handoff checksum reported')
    if rep != disk_sha:
        halt(f'judge {n}: handoff checksum {rep} != disk checksum {disk_sha}')
    print(f'judge {n}: handoff<->disk cross-check OK ({disk_sha[:16]}...)')
logs = {n: open(os.path.join(HERE, f'judge-log-clean-agent{n}.jsonl')).read().splitlines()
        for n in (1, 2, 3)}

# --- 2. tripwire on logs AFTER receipt (packages were checked pre-judge) ---
hits = []
for n, lines in logs.items():
    blob = '\n'.join(lines)
    for g in GATE:
        if g in blob: hits.append((n, 'gate-id', g))
    for m in R5005.finditer(blob): hits.append((n, 'r5005', m.group(0)))
if hits:
    halt(f'tripwire POST-judge hits: {hits}')
print('tripwire POST-judge CLEAR')

# --- 3. mechanical parse + schedule consistency ---
pkgs = {n: json.load(open(os.path.join(HERE, f'rungC-clean-pkg-{n}.json'))) for n in (1, 2, 3)}
scheds = json.load(open(os.path.join(HERE, 'rungC-clean-schedules.json')))
pair_lookup = {}
for n, p in pkgs.items():
    assert p['prompt_sha256'] == PROMPT_SHA, f'pkg{n} prompt sha mismatch'
    for pr in p['pairs']:
        pair_lookup[pr['pair_id']] = (pr['label_a'], pr['label_b'], pr['bout'])

records = []
for n, lines in logs.items():
    if len(lines) != 42:
        halt(f'judge {n}: {len(lines)} lines, expected 42')
    sched_seq = []
    for pno in range(3):
        sched_seq += scheds[str(n)][pno]
    for i, line in enumerate(lines):
        try:
            rec = json.loads(line)
        except Exception as e:
            halt(f'judge {n} line {i}: not JSON ({e})')
        exp = sched_seq[i]
        if rec.get('pair_id') != exp['pair_id'] or rec.get('pass') != (i // 14) + 1:
            halt(f'judge {n} line {i}: schedule order mismatch '
                 f'(got {rec.get("pair_id")}/pass{rec.get("pass")}, '
                 f'expected {exp["pair_id"]}/pass{(i//14)+1})')
        if rec.get('label_x') != exp['presented_first']:
            halt(f'judge {n} line {i}: label_x != schedule presented_first')
        if rec.get('prompt_sha256') != PROMPT_SHA:
            halt(f'judge {n} line {i}: prompt sha mismatch')
        raw = rec.get('raw_response', '').splitlines()
        if len(raw) < 3:
            halt(f'judge {n} line {i}: raw_response has {len(raw)} lines (<3)')
        l1, l2 = raw[0].strip(), raw[1].strip()
        la, lb, bout = pair_lookup[rec['pair_id']]
        if l1 not in (la, lb):
            halt(f'judge {n} line {i}: line1 "{l1}" not a pair label')
        try:
            conf = int(l2)
        except ValueError:
            halt(f'judge {n} line {i}: line2 "{l2}" not an integer')
        if rec.get('choice') != l1 or rec.get('confidence') != conf:
            halt(f'judge {n} line {i}: extracted fields != raw_response lines')
        records.append({'judge': n, 'pair_id': rec['pair_id'], 'pass': rec['pass'],
                        'bout': bout, 'choice_label': l1, 'confidence': conf,
                        'label_x': rec.get('label_x'),
                        'justification': raw[2] if len(raw) > 2 else ''})
print(f'mechanical parse OK: {len(records)} records')

# --- 4. completeness: 126/126 ---
if len(records) != 126:
    halt(f'completeness: {len(records)}/126')
b = [r for r in records if r['bout'] == 'binding']
d = [r for r in records if r['bout'] == 'diagnostic']
print(f'completeness: {len(records)}/126 (binding {len(b)}/108, diagnostic {len(d)}/18)')
if len(b) != 108 or len(d) != 18:
    halt('bout counts wrong')

# --- 5. label-blindness verification ---
key_path = os.path.join(HERE, '_KEY_V3C_CLEAN_DO_NOT_OPEN.json')
key_pre_sha = sha(key_path)
manifest['files']['_KEY_V3C_CLEAN_DO_NOT_OPEN.json (pre-open)'] = key_pre_sha
lmap = json.load(open(os.path.join(TRACKD, 'label_map.json')))
eternal = set(lmap)
seen = {r['choice_label'] for r in records} | {r['label_x'] for r in records}
if not seen <= set(json.load(open(key_path)).keys()):
    halt('log references label(s) not in sealed key')
if seen & eternal:
    halt('log references eternal ID(s)')
old_all = set(json.load(open(os.path.join(HERE, 'void-v3c-labels-collected.json'))))
for rel in ['instrument-acceptance/_KEY_DO_NOT_OPEN.json',
            'instrument-acceptance-v3a/_KEY_V3A_DO_NOT_OPEN.json',
            'instrument-acceptance-v3b/_KEY_V3B_DO_NOT_OPEN.json']:
    old_all |= set(json.load(open(os.path.join(TRACKD, rel))).keys())
if seen & old_all:
    halt('log references previously used blind label(s)')
blob_all = '\n'.join(l for n in logs for l in logs[n]).lower()
classword_hits = [w for w in ('"class"', 'salad', 'paraphrase', 'eternal') if w in blob_all]
print(f'label-blindness OK: {len(seen)} labels all fresh; class-word scan: {classword_hits}')

# --- 6. key opening (authorized, after 126/126 verified) ---
key = json.load(open(key_path))
key_open_utc = now()
print(f'key opened at {key_open_utc} (after 126/126 verified, pre-open sha {key_pre_sha[:16]}...)')

# --- 7. aggregation (mechanical) ---
by_pair = {}
for r in records:
    by_pair.setdefault(r['pair_id'], []).append(r)
pair_table = {}
truth_wins = 0
for pid, rs in sorted(by_pair.items()):
    assert len(rs) == 3, pid
    bout = rs[0]['bout']
    wins = {}
    confs = []
    for r in rs:
        cls = key[r['choice_label']]['class']
        wins[cls] = wins.get(cls, 0) + 1
        confs.append(r['confidence'])
    majority = max(wins, key=lambda c: (wins[c], c))
    pair_table[pid] = {'bout': bout, 'votes': wins, 'majority_class': majority,
                       'confidences': confs}
    if bout == 'binding' and majority == 'truth':
        truth_wins += 1

diag_by_seed = {}
for pid, pt in pair_table.items():
    if pt['bout'] == 'diagnostic':
        seeds = {key[r['choice_label']]['seed'] for r in by_pair[pid]}
        diag_by_seed[pid] = {'seed': next(iter(seeds)) if len(seeds) == 1 else sorted(seeds),
                             'majority_class': pt['majority_class'], 'votes': pt['votes']}

confs = [r['confidence'] for r in records]
confs_sorted = sorted(confs)
conf_stats = {'min': min(confs), 'max': max(confs),
              'median': confs_sorted[len(confs_sorted)//2],
              'mean': sum(confs)/len(confs),
              'hist_50_59': sum(50 <= c < 60 for c in confs),
              'hist_60_79': sum(60 <= c < 80 for c in confs),
              'hist_80_100': sum(80 <= c <= 100 for c in confs),
              'below_50': sum(c < 50 for c in confs)}

agg = {
    'trial': 'rung-C clean re-run (rerun-rungC-clean)',
    'prompt_sha256': PROMPT_SHA,
    'key_opened_utc': key_open_utc,
    'completeness': {'calls': len(records), 'expected': 126,
                     'binding': len(b), 'diagnostic': len(d)},
    'binding_truth_majority_wins': truth_wins,
    'binding_pairs': 36,
    'pair_table': pair_table,
    'diagnostic_by_seed': diag_by_seed,
    'confidence': conf_stats,
    'integrity': {'label_blindness': 'OK', 'tripwires': 'CLEAR pre+post',
                  'class_word_scan': classword_hits},
}
json.dump(agg, open(os.path.join(HERE, 'aggregation-clean.json'), 'w'), indent=1)

# --- manifest ---
for f in ['rungC-clean-pkg-1.json', 'rungC-clean-pkg-2.json', 'rungC-clean-pkg-3.json',
          'rungC-clean-schedules.json', 'build_rungC_clean.py', 'judge-brief.md',
          'score_and_aggregate.py', 'void-v3c-labels-collected.json', 'build.log']:
    manifest['files'][f] = sha(os.path.join(HERE, f))
manifest['files']['aggregation-clean.json'] = sha(os.path.join(HERE, 'aggregation-clean.json'))
json.dump(manifest, open(os.path.join(HERE, 'INTEGRITY-MANIFEST.json'), 'w'), indent=1)

# --- mechanical summary (no verdict language) ---
lines = ['# rung-C clean re-run — mechanical summary (no verdict)',
         f'generated_utc: {now()}',
         f'prompt_sha256: {PROMPT_SHA}',
         '',
         '## Completeness',
         f'- calls parsed: {len(records)}/126 (binding {len(b)}/108, diagnostic {len(d)}/18)',
         '',
         '## Binding pairs (truth vs salad)',
         f'- truth majority-wins: {truth_wins}/36',
         '',
         '## Per-pair table (pair_id: bout, votes, majority class, confidences)',
         ]
for pid, pt in pair_table.items():
    lines.append(f'- {pid}: {pt["bout"]}, votes={pt["votes"]}, majority={pt["majority_class"]}, conf={pt["confidences"]}')
lines += ['',
          '## Diagnostic bouts (truth vs paraphrase, by seed)',
          ]
for pid, dg in sorted(diag_by_seed.items()):
    lines.append(f'- {pid} (seed {dg["seed"]}): majority={dg["majority_class"]}, votes={dg["votes"]}')
lines += ['',
          '## Confidence distribution',
          f'- min={conf_stats["min"]} max={conf_stats["max"]} median={conf_stats["median"]} mean={conf_stats["mean"]:.1f}',
          f'- below_50={conf_stats["below_50"]} 50-59={conf_stats["hist_50_59"]} 60-79={conf_stats["hist_60_79"]} 80-100={conf_stats["hist_80_100"]}',
          '',
          '## Integrity checks',
          '- handoff<->disk cross-check: OK (3/3)',
          '- tripwire (R5005/gate IDs): CLEAR pre-judge and post-judge',
          f'- label blindness: OK ({len(seen)} fresh labels, zero old-label hits, no eternal IDs)',
          f'- class-word scan of logs: {classword_hits}',
          f'- key opened: {key_open_utc} (pre-open sha {key_pre_sha[:16]}...)',
          '- verdict: NOT DECLARED (red-team audit pending)',
          '']
open(os.path.join(HERE, 'MECHANICAL-SUMMARY.md'), 'w').write('\n'.join(lines))
print('\n'.join(lines))
