#!/usr/bin/env python3
r"""Census for battery governed-excl-inf-topic-audit.

Reproduces battery-disloc-governed-excl-prose-recall's corpus gate and CTRL
(register-control) pattern byte-verbatim, but captures EVERY distinct
"pour/de [inf] !" control string with its first byte offset and ±150-char
context so the worker can classify topic shapes by hand.

Corpus gate (identical to parent):
  - 18-file 1841-register prose set name-pinned from
    disloc-demonstrative-reinforced_census.json (byte-asserted total chars)
  - 3 wider files (byte-asserted)
  - assert the 231 reinforced-head-comma hits reproduce (drift check)
  - assert the register-control total reproduces 236 distinct per-file hits

CTRL pattern (verbatim from parent):
  r"\b(?:pour|de)\s+[a-zàâäçéèêëîïôöùûü']{2,}(?:er|ir|re|oir)\b[^!?.]{0,60}!"
  case-insensitive, distinct lowercased strings per file.

Output: gov-excl-inf-topic-audit_census.json with, per distinct string:
  match, file, first_offset, context (±150 chars, newlines as "/"),
  plus per-file hit counts and a cross-file membership map.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS1841 = os.path.join(LANE, "code/side-period/corpus")
NT = os.path.join(LANE, "code/crowd17/next-token")

_parent = json.load(open(os.path.join(NT, "disloc-demonstrative-reinforced_census.json")))
PARENT_FILES = sorted(x["file"] for x in _parent["census_1841_register"]["files"])
PARENT_TOTAL = _parent["census_1841_register"]["total_chars"]
WIDER_PARENT = _parent["census_wider_19c"]
WIDER_FILES = sorted(x["file"] for x in WIDER_PARENT["files"])
WIDER_TOTAL = WIDER_PARENT["total_chars"]

DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)
# CTRL verbatim from disloc_governed_excl_prose_recall_census.py
CTRL = re.compile(
    r"\b(?:pour|de)\s+[a-zàâäçéèêëîïôöùûü']{2,}(?:er|ir|re|oir)\b[^!?.]{0,60}!",
    re.IGNORECASE)


def main():
    c1841 = [os.path.join(CORPUS1841, f) for f in PARENT_FILES]
    missing = [p for p in c1841 if not os.path.exists(p)]
    assert not missing, "GATE FAIL: " + ", ".join(missing)
    cwider = [os.path.join(LANE, p) for p in
              ["data/gutenberg-17489-miserables1.txt",
               "data/gutenberg-30513-tocqueville-t1.txt",
               "data/gutenberg-30514-tocqueville-t2.txt"]]
    missing = [p for p in cwider if not os.path.exists(p)]
    assert not missing, "GATE FAIL: " + ", ".join(missing)
    got = sum(len(open(p, encoding="utf-8", errors="replace").read()) for p in c1841)
    assert got == PARENT_TOTAL, f"corpus drift (1841): {got} != {PARENT_TOTAL}"
    gotw = sum(len(open(p, encoding="utf-8", errors="replace").read()) for p in cwider)
    assert gotw == WIDER_TOTAL, f"corpus drift (wider): {gotw} != {WIDER_TOTAL}"

    seen = {}          # (file, match) -> record (first offset + context)
    per_file = []      # {file, hits}
    total, nhits = 0, 0
    texts = {}
    for p in c1841 + cwider:
        fname = os.path.basename(p)
        text = open(p, encoding="utf-8", errors="replace").read()
        texts[fname] = text
        total += len(text)
        nhits += len(DEM_REINF.findall(text))
        uniq = {}
        for m in CTRL.finditer(text):
            key = m.group(0).lower()
            if key not in uniq:
                uniq[key] = m.start()
        for key, off in uniq.items():
            c0 = max(0, off - 150)
            ctx = text[c0:off + len(key) + 150].replace("\n", "/")
            seen[(fname, key)] = {"match": key, "file": fname,
                                  "first_offset": off, "context": ctx}
        per_file.append({"file": fname, "chars": len(text),
                         "pour_de_inf_excl_hits": len(uniq)})
    print(f"corpus identity OK: {total} chars, {nhits} dem-comma hits")
    assert nhits == 231, f"dem-comma drift: {nhits} != 231"
    total_controls = sum(x["pour_de_inf_excl_hits"] for x in per_file)
    print(f"register-control distinct per-file hits: {total_controls}")
    assert total_controls == 236, f"control drift: {total_controls} != 236"

    # cross-file dedupe for classification (same string in >1 file classified once)
    by_string = {}
    for (fname, key), rec in sorted(seen.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        by_string.setdefault(key, []).append(rec)

    records = []
    for key in sorted(by_string):
        recs = by_string[key]
        r0 = recs[0]
        records.append({"match": key, "n_files": len(recs),
                        "files": [r["file"] for r in recs],
                        "first_file": r0["file"], "first_offset": r0["first_offset"],
                        "context": r0["context"]})

    out = os.path.join(NT, "gov-excl-inf-topic-audit_census.json")
    json.dump({"total_chars": total, "dem_comma_hits": nhits,
               "per_file": per_file, "total_controls": total_controls,
               "n_distinct_strings": len(records),
               "records": records,
               "note": "distinct lowercased 'pour/de [inf] !' strings per file, "
                       "verbatim CTRL pattern from "
                       "disloc_governed_excl_prose_recall_census.py"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {out}: {len(records)} distinct strings, "
          f"{total_controls} per-file hits")
    # per-file table for the report
    for x in per_file:
        if x["pour_de_inf_excl_hits"]:
            print(f"  {x['file']}: {x['pour_de_inf_excl_hits']}")


if __name__ == "__main__":
    main()
