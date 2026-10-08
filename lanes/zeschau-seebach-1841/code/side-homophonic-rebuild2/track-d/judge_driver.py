#!/usr/bin/env python3
"""TRACK-D pilot judging driver.

Generates the 3-pass shuffled query order (seeded) and provides the
mechanical log appender. The operator judges each query with the FROZEN
prompt (judge_prompt.txt, sha256 390a1ec0...) and records score +
one-sentence justification; this script appends exactly that to
judge_log.jsonl with timestamp + prompt sha256. It never sees
label_map.json (only label->text).
"""
import hashlib
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PROMPT_PATH = os.path.join(HERE, 'judge_prompt.txt')
PROMPT_SHA = '390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d'
ORDER_SEED = 20261008


def check_prompt():
    h = hashlib.sha256(open(PROMPT_PATH, 'rb').read()).hexdigest()
    assert h == PROMPT_SHA, f'PROMPT CHANGED: {h}'
    return open(PROMPT_PATH).read()


def load_texts():
    doc = json.load(open(os.path.join(HERE, 'candidates.json')))
    return {lab: c['text'] for lab, c in doc['candidates'].items()}


def make_order():
    texts = load_texts()
    rng = random.Random(ORDER_SEED)
    labels = sorted(texts)
    order = []
    for p in (1, 2, 3):
        seq = list(labels)
        rng.shuffle(seq)
        for lab in seq:
            order.append({'pass_no': p, 'label': lab})
    return order


def log_judgment(label, pass_no, score, justification):
    assert isinstance(score, int) and 0 <= score <= 100, 'score out of range'
    assert justification and '\n' not in justification.strip()
    entry = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'candidate_label': label,
        'pass_no': pass_no,
        'prompt_sha256': PROMPT_SHA,
        'raw_response': f'{score}\n{justification.strip()}',
        'extracted_score': score,
    }
    with open(os.path.join(HERE, 'judge_log.jsonl'), 'a') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    return entry


def main():
    check_prompt()
    order = make_order()
    json.dump(order, open(os.path.join(HERE, 'query_order.json'), 'w'), indent=1)
    print(f'prompt OK ({PROMPT_SHA[:12]}...); {len(order)} queries in query_order.json')
    for i, q in enumerate(order):
        print(i, 'pass', q['pass_no'], q['label'])


if __name__ == '__main__':
    if len(sys.argv) == 5 and sys.argv[1] == 'log':
        # usage: judge_driver.py log <label> <pass_no> <score> ; justification via stdin
        _, _, label, pass_no, score = sys.argv
        just = sys.stdin.read()
        e = log_judgment(label, int(pass_no), int(score), just)
        print('logged:', e['candidate_label'], e['pass_no'], e['extracted_score'])
    else:
        main()
