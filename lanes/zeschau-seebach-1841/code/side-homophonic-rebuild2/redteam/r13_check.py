#!/usr/bin/env python3
# R13 acceptance-test adjudication. Independent code, no track imports.
import json, statistics, hashlib, collections
from pathlib import Path

BASE = Path.home() / "workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/instrument-acceptance"

key = json.loads((BASE / "_KEY_DO_NOT_OPEN.json").read_text())
labels = list(key)

# parse the 3 logs
logs = []
for i in (1, 2, 3):
    for line in (BASE / f"judge-log-agent{i}.jsonl").read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        logs.append((i, json.loads(line)))

print("total log lines:", len(logs))

PROMPT = "390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d"
prompt_ok = all(e["prompt_sha256"] == PROMPT for _, e in logs)
print("prompt sha256 asserted in all 54 calls:", prompt_ok)

# per-candidate per-pass scores
per = collections.defaultdict(dict)  # label -> pass_no -> score
for agent, e in logs:
    lbl = e["candidate_label"]
    per[lbl][e["pass_no"]] = e["extracted_score"]

print("candidates seen:", len(per))
dups = sum(1 for lbl, d in per.items() if len(d) != 3)
print("candidates with !=3 passes:", dups)

# median per candidate; compare vs expected within ±3
rows = []
for lbl in labels:
    scores = sorted(per[lbl].values())
    med = statistics.median(scores)
    exp = key[lbl]["expected_median"]
    rows.append((lbl, key[lbl]["old_label"], scores, med, exp, abs(med - exp) <= 3))

within3 = sum(1 for r in rows if r[5])
print("within ±3:", within3, "/", len(rows))
for lbl, old, scores, med, exp, ok in rows:
    print(f"{'OK ' if ok else 'MISS'} new={lbl} old={old} scores={scores} med={med} expected={exp} delta={med-exp:+}")

# map old labels to pilot classes. Pilot per-query table (corrected): truth labels
# 1386766b, c0733a7d, fe847630, 2a87b7a9, b1eee668, 99a93f79 (medians 64,61,61,63,62,62)
# salad: d38a1821, 19f3bb19, d24f0ea5, a1cd2087, 1c2498b4, fc12e892 (21,20,22,20,21,20)
# paraphrase: fed88338, ecf4db34, d666c7df, 7e5bbba0, 5888ca6b, 264710b9 (90,90,91,91,92,92)
truth_old = {"1386766b","c0733a7d","fe847630","2a87b7a9","b1eee668","99a93f79"}
salad_old = {"d38a1821","19f3bb19","d24f0ea5","a1cd2087","1c2498b4","fc12e892"}
para_old  = {"fed88338","ecf4db34","d666c7df","7e5bbba0","5888ca6b","264710b9"}
cls = {}
for r in rows:
    old = r[1]
    cls[r[0]] = "truth" if old in truth_old else ("salad" if old in salad_old else ("para" if old in para_old else "??"))
print("class coverage:", collections.Counter(cls.values()))

for cname in ("truth","salad","para"):
    cs = [r for r in rows if cls[r[0]]==cname]
    print(cname, "medians:", [r[3] for r in cs], "expected:", [r[4] for r in cs],
          "ranges:", [max(r[2])-min(r[2]) for r in cs])
    tm = statistics.median([r[3] for r in cs])
    print("  class median:", tm)

# mT-mS per seed: group by seed via label_map if present; else order rows by seed index in PILOT table.
# Use track-d label_map.json for seed assignment (allowed: reading files, not track code)
lm = json.loads(Path.home().joinpath("workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/label_map.json").read_text())
# lm: old_label -> seed? or label->seed; inspect keys
print("label_map sample:", json.dumps(lm)[:300])

seed_of_old = {}
for lbl, info in lm.items():
    # info maps new? just detect
    pass
