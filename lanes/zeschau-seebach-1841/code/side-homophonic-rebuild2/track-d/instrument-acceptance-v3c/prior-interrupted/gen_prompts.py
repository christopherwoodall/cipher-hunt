#!/usr/bin/env python3
"""Rung C judge harness: generate per-pass randomized prompts + manifest.
Usage: gen_prompts.py <pass_no> <seed>
Reads: ../prompt-v3C.txt, instrument-acceptance-v3c/rungC-pkg-2.json
Writes: /tmp/rungC_j2/prompts_pass<N>.txt, /tmp/rungC_j2/manifest_pass<N>.json
"""
import json, random, hashlib, sys, os

BASE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d")
pass_no = int(sys.argv[1])
seed = int(sys.argv[2])
OUT = "/tmp/rungC_j2"
os.makedirs(OUT, exist_ok=True)

prompt_path = os.path.join(BASE, "prompt-v3C.txt")
with open(prompt_path, "rb") as f:
    data = f.read()
sha = hashlib.sha256(data).hexdigest()
EXPECTED = "d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e"
assert sha == EXPECTED, f"SHA MISMATCH: {sha}"
template = data.decode("utf-8")

with open(os.path.join(BASE, "instrument-acceptance-v3c/rungC-pkg-2.json"), encoding="utf-8") as f:
    pairs = json.load(f)["pairs"]
assert len(pairs) == 14, f"expected 14 pairs, got {len(pairs)}"

rng = random.Random(seed)
order = list(range(len(pairs)))
rng.shuffle(order)

prompts_out = []
manifest = []
for seq, idx in enumerate(order):
    p = pairs[idx]
    pid = p["pair_id"]
    # independently shuffle X/Y presentation
    if rng.random() < 0.5:
        xa, ta, yb, tb = p["label_a"], p["text_a"], p["label_b"], p["text_b"]
    else:
        xa, ta, yb, tb = p["label_b"], p["text_b"], p["label_a"], p["text_a"]
    rendered = template.replace("{label_a}", xa).replace("{text_a}", ta) \
                       .replace("{label_b}", yb).replace("{text_b}", tb)
    prompts_out.append(f"=== PROMPT {seq+1}/14 :: pair_id={pid} :: X={xa} :: Y={yb} ===\n{rendered}\n")
    manifest.append({
        "seq": seq, "pair_id": pid,
        "label_x": xa, "label_y": yb,
        "presented_first": xa,  # X always appears first in template
        "pass_no": pass_no,
        "prompt_sha256": sha,
    })

with open(f"{OUT}/prompts_pass{pass_no}.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(prompts_out))
with open(f"{OUT}/manifest_pass{pass_no}.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=1)

print(f"pass {pass_no}: wrote {len(manifest)} prompts to {OUT}/prompts_pass{pass_no}.txt")
print(f"  sha asserted OK")
print(f"  order: {[m['pair_id'] for m in manifest]}")
