#!/usr/bin/env python3
"""Rung C mechanical logger + aggregator.

Usage: log_rungC.py <agent_no> <responses_file>
- responses_file: the judge's 42 response blocks (3 lines each, blank-line separated)
  in schedule order (pass 1..3, each in its scheduled pair order).
- Appends 42 records to instrument-acceptance-v3c/judge-log-rungC-agentN.jsonl.
- Then: aggregate.py mode (same script, --aggregate) reads all 3 logs + sealed key
  and reports per-pair majorities vs the binding bar. The KEY IS ONLY OPENED
  when all 126 calls are logged (enforced by --aggregate refusing otherwise).

Mechanical parse per v3c-logger-pin.md: no interpretation, no retries, VOID on mismatch.
"""
import json, os, re, sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
V3C = os.path.join(HERE, 'instrument-acceptance-v3c')
PROMPT_SHA = 'd907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e'


def log_agent(agent_no, responses_path):
    sched = json.load(open(os.path.join(V3C, 'rungC-schedules.json')))[str(agent_no)]
    pkg = json.load(open(os.path.join(V3C, f'rungC-pkg-{agent_no}.json')))
    byid = {p['pair_id']: p for p in pkg['pairs']}
    raw = open(responses_path).read().rstrip('\n')
    blocks = re.split(r'\n\s*\n', raw)
    assert len(blocks) == 42, f'agent{agent_no}: got {len(blocks)} blocks, expected 42'
    log_path = os.path.join(V3C, f'judge-log-rungC-agent{agent_no}.jsonl')
    mode = 'a' if os.path.exists(log_path) else 'w'
    n = 0
    with open(log_path, mode) as log:
        for pno, seq in enumerate(sched, start=1):
            for k, e in enumerate(seq):
                blk = blocks[(pno - 1) * 14 + k]
                lines = blk.split('\n')
                p = byid[e['pair_id']]
                xa = e['presented_first']
                ya = p['label_b'] if xa == p['label_a'] else p['label_a']
                line1 = lines[0].strip() if len(lines) >= 1 else ''
                choice = line1 if line1 in (xa, ya) else None
                conf = None
                if len(lines) >= 2 and re.fullmatch(r'\d+', lines[1].strip()):
                    c = int(lines[1].strip())
                    if 0 <= c <= 100:
                        conf = c
                just = lines[2] if len(lines) >= 3 else None
                rec = {
                    'timestamp': datetime.now(timezone.utc).isoformat(),
                    'pair_id': e['pair_id'],
                    'label_x': xa, 'label_y': ya,
                    'presented_first': xa,
                    'pass_no': pno,
                    'prompt_sha256': PROMPT_SHA,
                    'raw_response': blk,
                    'choice': choice, 'confidence': conf, 'justification': just,
                }
                log.write(json.dumps(rec, ensure_ascii=False) + '\n')
                n += 1
    print(f'agent{agent_no}: logged {n} records -> {log_path}')


def aggregate():
    logs = {}
    for j in (1, 2, 3):
        lp = os.path.join(V3C, f'judge-log-rungC-agent{j}.jsonl')
        recs = [json.loads(l) for l in open(lp)]
        logs[j] = recs
    total = sum(len(v) for v in logs.values())
    if total != 126:
        raise SystemExit(f'REFUSE: only {total}/126 calls logged; key stays sealed')
    key = json.load(open(os.path.join(V3C, '_KEY_V3C_DO_NOT_OPEN.json')))
    truth_of = {lab: (v['class'] == 'truth') for lab, v in key.items()}
    # per-pair majority of 3
    bypair = {}
    for j, recs in logs.items():
        for r in recs:
            bypair.setdefault(r['pair_id'], []).append(r)
    binding_wins, binding_total, flips, details = 0, 0, [], []
    diag_wins, diag_total = 0, 0
    void_count = 0
    for pid, recs in sorted(bypair.items()):
        assert len(recs) == 3, (pid, len(recs))
        votes = [r['choice'] for r in recs]
        if any(v is None for v in votes):
            void_count += 1
        maj = max(set(votes), key=votes.count)
        if votes.count(maj) < 2:
            maj = None  # no majority
        bout = 'binding' if pid.startswith('P') else 'diagnostic'
        truth_lab = next(lab for lab in (recs[0]['label_x'], recs[0]['label_y']) if truth_of.get(lab))
        won = (maj == truth_lab)
        details.append({'pair_id': pid, 'bout': bout, 'votes': votes,
                        'truth_label': truth_lab, 'majority': maj, 'truth_won': won,
                        'confidences': [r['confidence'] for r in recs]})
        if bout == 'binding':
            binding_total += 1
            if won: binding_wins += 1
            else: flips.append(pid)
        else:
            diag_total += 1
            if won: diag_wins += 1
    print(f'binding: truth won {binding_wins}/{binding_total}; flips: {flips}')
    print(f'diagnostic (truth-vs-paraphrase, truth wins): {diag_wins}/{diag_total} (non-binding; paraphrase expected to win)')
    print(f'void records: {void_count}')
    print(f'BAR: truth wins >=35/36 binding pairs -> {"PASS" if binding_wins >= 35 else "FAIL"}')
    json.dump(details, open(os.path.join(V3C, 'rungC-pair-outcomes.json'), 'w'), indent=1)
    return binding_wins, flips


if __name__ == '__main__':
    if len(sys.argv) == 3:
        log_agent(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == '--aggregate':
        aggregate()
    else:
        raise SystemExit('usage: log_rungC.py <agent_no> <responses_file> | --aggregate')
