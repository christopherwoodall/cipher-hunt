#!/usr/bin/env python3
"""Track D judge instrument — mechanical aggregation + verification.

Reads a judge_log.jsonl (pilot format), re-derives every extracted
score from raw_response, and reports:
  - per-candidate median-of-3 and cross-pass range (flags range > 2)
  - completeness vs an expected work-item list (duplicates/missing)
  - prompt-hash uniformity (every entry must carry the frozen sha)
  - optional acceptance check vs pilot medians (needs --pilot-medians)

No judgment, no re-querying, no steering. Pure mechanics.
Usage:
  aggregate.py --log <judge_log.jsonl> [--expect <work_batches.json>]
      [--pilot-medians <json: {label: median}>] [--label-classes <json>]
      [--out <report.json>]
"""
import argparse
import hashlib
import json
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TRACKD = os.path.dirname(HERE)


def frozen_sha():
    reg = json.load(open(os.path.join(HERE, 'prompt_registry.json')))
    return reg['sha256']


def extract(raw):
    first = raw.split('\n', 1)[0].strip()
    m = re.fullmatch(r'\d+', first)
    if not m:
        return None
    v = int(m.group(0))
    return v if 0 <= v <= 100 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--log', required=True)
    ap.add_argument('--expect', default=None,
                    help='work_batches.json from judge_runner prepare')
    ap.add_argument('--pilot-medians', default=None,
                    help='JSON {label: pilot_median} for acceptance check')
    ap.add_argument('--label-classes', default=None,
                    help='JSON {label: truth|salad|paraphrase} for margin check')
    ap.add_argument('--out', default=None)
    args = ap.parse_args()

    sha = frozen_sha()
    entries, problems = [], []
    seen = {}
    for ln, line in enumerate(open(args.log), 1):
        line = line.strip()
        if not line:
            continue
        e = json.loads(line)
        # schema check (pilot format)
        for k in ('timestamp', 'candidate_label', 'pass_no',
                  'prompt_sha256', 'raw_response', 'extracted_score'):
            if k not in e:
                problems.append(f'line {ln}: missing key {k}')
        if e.get('prompt_sha256') != sha:
            problems.append(f'line {ln}: prompt_sha256 != frozen '
                            f'({str(e.get("prompt_sha256"))[:12]})')
        # re-derive score mechanically
        rederived = extract(e.get('raw_response', ''))
        if rederived is None:
            problems.append(f'line {ln}: extraction failed on '
                            f'{e.get("candidate_label")}/{e.get("pass_no")}')
        elif rederived != e.get('extracted_score'):
            problems.append(f'line {ln}: extracted_score {e.get("extracted_score")} '
                            f'!= rederived {rederived}')
        key = (e.get('candidate_label'), e.get('pass_no'))
        if key in seen:
            problems.append(f'line {ln}: DUPLICATE {key} (first at line {seen[key]})')
        seen[key] = ln
        entries.append(e)

    # per-candidate aggregation
    by_label = {}
    for e in entries:
        by_label.setdefault(e['candidate_label'], []).append(e)
    cands = {}
    for lab, es in sorted(by_label.items()):
        scores = sorted(e['extracted_score'] for e in es)
        passes = sorted(e['pass_no'] for e in es)
        rng = max(scores) - min(scores) if scores else None
        cands[lab] = {
            'n': len(es),
            'passes': passes,
            'scores': scores,
            'median': statistics.median(scores) if scores else None,
            'cross_pass_range': rng,
            'range_flag': (rng is not None and rng > 2),
        }

    # completeness vs expected work items
    completeness = None
    if args.expect:
        batches = json.load(open(args.expect))
        expected = set()
        for b in batches:
            for it in b['items']:
                expected.add((it['candidate_label'], it['pass_no']))
        got = set(seen)
        completeness = {
            'expected': len(expected),
            'logged': len(got),
            'missing': sorted(f'{a}/{p}' for a, p in (expected - got)),
            'unexpected': sorted(f'{a}/{p}' for a, p in (got - expected)),
        }

    # acceptance check vs pilot medians
    acceptance = None
    if args.pilot_medians:
        pm = json.load(open(args.pilot_medians))
        per_label = {}
        for lab, pmed in pm.items():
            c = cands.get(lab)
            if c is None or c['median'] is None:
                per_label[lab] = {'status': 'missing'}
            else:
                d = abs(c['median'] - pmed)
                per_label[lab] = {'pilot_median': pmed,
                                  'instrument_median': c['median'],
                                  'abs_diff': d,
                                  'within_3': d <= 3}
        acceptance = {'per_label': per_label,
                      'all_within_3': all(v.get('within_3', False)
                                          for v in per_label.values())}
        if args.label_classes:
            lc = json.load(open(args.label_classes))
            by_seed_class = {}
            for lab, cls in lc.items():
                # seed encoded in label_map; classes file maps label->(seed,class)
                by_seed_class.setdefault(cls, []).append(cands.get(lab, {}).get('median'))
            margins = {}
            # mT-mS per seed needs seed grouping; do it via label_classes
            # {label: [seed, class]}
            seeds = {}
            for lab, sc in lc.items():
                seed, cls = sc[0], sc[1]
                med = cands.get(lab, {}).get('median')
                seeds.setdefault(seed, {})[cls] = med
            for seed, d in sorted(seeds.items()):
                if d.get('truth') is not None and d.get('salad') is not None:
                    margins[seed] = {'mT': d['truth'], 'mS': d['salad'],
                                     'margin': d['truth'] - d['salad'],
                                     'ge_30': (d['truth'] - d['salad']) >= 30}
            acceptance['margins_mT_mS'] = margins
            acceptance['all_margins_ge_30'] = all(
                v['ge_30'] for v in margins.values()) if margins else False

    report = {
        'log': os.path.abspath(args.log),
        'n_entries': len(entries),
        'prompt_sha256': sha,
        'hash_uniform': all(e.get('prompt_sha256') == sha for e in entries),
        'problems': problems,
        'candidates': cands,
        'n_range_flags': sum(1 for c in cands.values() if c['range_flag']),
        'completeness': completeness,
        'acceptance': acceptance,
    }
    if args.out:
        json.dump(report, open(args.out, 'w'), indent=1)
        print(f'report -> {args.out}')
    # human summary
    print(f'entries={len(entries)} candidates={len(cands)} '
          f'hash_uniform={report["hash_uniform"]} problems={len(problems)}')
    for p in problems[:10]:
        print('  PROBLEM:', p)
    print(f'range flags (>2): {report["n_range_flags"]}')
    for lab, c in sorted(cands.items()):
        flag = '  <-- RANGE FLAG' if c['range_flag'] else ''
        print(f'  {lab}: n={c["n"]} median={c["median"]} range={c["cross_pass_range"]}{flag}')
    if completeness:
        print(f'completeness: expected={completeness["expected"]} '
              f'logged={completeness["logged"]} '
              f'missing={len(completeness["missing"])} '
              f'unexpected={len(completeness["unexpected"])}')
    if acceptance:
        print(f'acceptance: all_within_3={acceptance["all_within_3"]}')
        if acceptance.get('all_margins_ge_30') is not None:
            print(f'  all mT-mS >= 30: {acceptance["all_margins_ge_30"]}')
    return 0 if not problems else 1


if __name__ == '__main__':
    sys.exit(main())
