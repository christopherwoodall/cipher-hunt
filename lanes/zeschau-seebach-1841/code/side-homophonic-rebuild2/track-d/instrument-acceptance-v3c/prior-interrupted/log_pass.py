#!/usr/bin/env python3
"""Rung C judge harness: mechanically parse responses and append JSONL log lines.
Usage: log_pass.py <pass_no>
Reads: /tmp/rungC_j2/manifest_pass<N>.json, /tmp/rungC_j2/responses_pass<N>.txt
  Responses file: 14 blocks in order; each block = exactly 3 lines
  (line1 label, line2 confidence int, line3 one sentence); blocks separated by a blank line.
Appends to instrument-acceptance-v3c/judge-log-rungC-agent2.jsonl
Mechanical parse only: no interpretation, no retries.
"""
import json, re, sys, os
from datetime import datetime, timezone

BASE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d")
OUT = "/tmp/rungC_j2"
LOG = os.path.join(BASE, "instrument-acceptance-v3c/judge-log-rungC-agent2.jsonl")
pass_no = int(sys.argv[1])

with open(f"{OUT}/manifest_pass{pass_no}.json", encoding="utf-8") as f:
    manifest = json.load(f)
with open(f"{OUT}/responses_pass{pass_no}.txt", encoding="utf-8") as f:
    raw = f.read().rstrip("\n")

blocks = re.split(r"\n\s*\n", raw)
assert len(blocks) == len(manifest), f"got {len(blocks)} response blocks, manifest has {len(manifest)}"

mode = "a" if os.path.exists(LOG) else "w"
with open(LOG, mode, encoding="utf-8") as log:
    for m, blk in zip(manifest, blocks):
        lines = blk.split("\n")
        raw_response = blk
        # line 1 -> choice
        line1 = lines[0].strip() if len(lines) >= 1 else ""
        if line1 in (m["label_x"], m["label_y"]):
            choice = line1
        else:
            choice = None  # VOID
        # line 2 -> confidence
        confidence = None
        if len(lines) >= 2 and re.fullmatch(r"\d+", lines[1].strip()):
            c = int(lines[1].strip())
            if 0 <= c <= 100:
                confidence = c
        # line 3 -> justification
        justification = lines[2] if len(lines) >= 3 else None
        # audit rule: any mismatch of choice/conf/just vs lines -> VOID record
        rec = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "pair_id": m["pair_id"],
            "label_x": m["label_x"],
            "label_y": m["label_y"],
            "presented_first": m["presented_first"],
            "pass_no": m["pass_no"],
            "prompt_sha256": m["prompt_sha256"],
            "raw_response": raw_response,
            "choice": choice,
            "confidence": confidence,
            "justification": justification,
        }
        log.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"pass {pass_no}: logged {len(manifest)} records to {LOG}")
