#!/usr/bin/env python3
"""test_table.py — Seebach key-hunt side fleet: TESTER harness.

Applies a candidate key table to the canonical R5005 pair sequence and
verifies it byte-for-byte against the known anchors.

Usage:
    python3 test_table.py --table path/to/table.json [--out report.json]
    python3 test_table.py --table '{"11": "la", ...}'

Table format: JSON object mapping two-digit group -> syllable string,
e.g. {"11": "la", "70": "pre", "82": "m", ...}.

Report contents:
  (a) anchor check — ground-truth anchors 11/70/82/34/29/40 (+46), whether
      pair 1033 (0-based) reads "la première", provisional 87/64/96 as
      secondary notes only (they never gate the verdict);
  (b) French-likeness of the expansion:
        - letter quadgram score per char (lane's french-quadgrams.json)
        - syllable-bigram score per syllable (side-keyhunt/syll_bigram.json,
          built from Tocqueville 1835-1840, same era/register)
      Unknown (unmapped) groups are excluded from scoring; coverage is
      reported separately so partial tables are judged honestly.

Verdict:
  HIT       — all 7 ground-truth anchors present and correct, pair 1033
              reads exactly "la première", ALL 96 groups mapped, quadgram
              score >= -5.5/char. (The coverage gate exists because a table
              that only re-states the 7 known anchors proves nothing.)
  NEAR-MISS — no anchor contradiction, but something is incomplete or the
              text does not score French. This is NOT a hit.
  MISS      — any ground-truth anchor contradiction, a broken "la première",
              or a non-French expansion score (< -6.5/char).
"""
import argparse
import json
import math
import os
import re
import sys
import unicodedata

import canonical

_HERE = os.path.dirname(__file__)
_DATA = os.path.normpath(os.path.join(_HERE, "..", "..", "data"))

_EXPECTED_LA_PREMIERE = ["la", "pre", "m", "i", "er", "e"]
_HIT_QGRAM = -5.5
_MISS_QGRAM = -6.5


def _strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def load_table(src):
    """Load a candidate table; return dict group(str) -> syllable(str)."""
    raw = json.loads(src) if src.lstrip().startswith("{") else \
        json.load(open(src, encoding="utf-8"))
    table = {}
    for g, v in raw.items():
        g = str(g).strip()
        v = str(v).strip().lower()
        if not re.fullmatch(r"\d{2}", g):
            raise ValueError(f"group key not a 2-digit group: {g!r}")
        if g in table:
            raise ValueError(f"duplicate group in table: {g}")
        table[g] = v
    return table


def load_quadgrams():
    q = json.load(open(os.path.join(_DATA, "french-quadgrams.json")))
    return q["logp"], q["floor"]


def quadgram_score(text, logp, floor):
    s = re.sub(r"[^A-Z]", "", _strip_accents(text).upper())
    if len(s) < 4:
        return None
    return sum(logp.get(s[i:i + 4], floor) for i in range(len(s) - 3)) / len(s)


def load_syll_model():
    m = json.load(open(os.path.join(_HERE, "syll_bigram.json"),
                       encoding="utf-8"))
    return m


def syll_bigram_score(syls, model):
    """Mean log-p per syllable under the Tocqueville syllable-bigram model."""
    k, V = 0.5, model["n_distinct"]
    bigram, totals = model["bigram"], model["totals"]
    if len(syls) < 2:
        return None
    s = 0.0
    for a, b in zip(syls, syls[1:]):
        c = bigram.get(f"{a}\t{b}", 0)
        t = totals.get(a, 0)
        s += math.log((c + k) / (t + k * V))
    return s / (len(syls) - 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", required=True, help="table JSON file or inline JSON")
    ap.add_argument("--out", default=None, help="write JSON report here")
    ap.add_argument("--name", default=None, help="label for this candidate table")
    args = ap.parse_args()

    pairs = canonical.load_canonical_pairs()
    table = load_table(args.table)

    # ---- (a) anchor checks ----
    anchor_rows = []
    contradictions = []
    gt_ok, gt_missing = 0, []
    for g, want in canonical.GROUND_TRUTH.items():
        got = table.get(g)
        if got is None:
            anchor_rows.append((g, want, None, "MISSING"))
            gt_missing.append(g)
        elif got == want:
            anchor_rows.append((g, want, got, "OK"))
            gt_ok += 1
        else:
            anchor_rows.append((g, want, got, "CONTRADICTION"))
            contradictions.append((g, want, got))

    prov_rows = []
    for g, want in canonical.PROVISIONAL.items():
        got = table.get(g)
        prov_rows.append((g, want, got,
                          "OK" if got == want else ("MISSING" if got is None else "differs (not fatal)")))

    # pair 1033: does it read "la première"?
    idx = canonical.EXPECTED["anchor_index"]
    got_seq = [table.get(p) for p in pairs[idx:idx + 6]]
    lp_rows = list(zip(pairs[idx:idx + 6], _EXPECTED_LA_PREMIERE, got_seq))
    lp_missing = [p for p, _, got in lp_rows if got is None]
    lp_contrad = [(p, want, got) for p, want, got in lp_rows
                  if got is not None and got != want]
    lp_exact = (not lp_missing) and (not lp_contrad)
    lp_text = " ".join(got for got in got_seq if got is not None)

    # ---- expansion ----
    mapped = [p for p in pairs if p in table]
    coverage_pairs = len(mapped) / len(pairs)
    coverage_groups = len(set(mapped)) / len(set(pairs))
    syls = [table[p] for p in mapped]
    expansion = "".join(syls)

    logp, floor = load_quadgrams()
    qscore = quadgram_score(expansion, logp, floor)
    model = load_syll_model()
    sscore = syll_bigram_score(syls, model)

    # ---- verdict ----
    full_table = coverage_groups >= 1.0
    if contradictions or lp_contrad:
        verdict = "MISS"
        reason = ("anchor contradiction" if contradictions
                  else "'la première' sequence contradiction")
    elif qscore is not None and qscore < _MISS_QGRAM:
        verdict = "MISS"
        reason = f"expansion scores non-French ({qscore:.2f}/char < {_MISS_QGRAM})"
    elif (gt_ok == len(canonical.GROUND_TRUTH) and lp_exact and full_table
          and qscore is not None and qscore >= _HIT_QGRAM):
        verdict = "HIT"
        reason = ("all 7 ground-truth anchors, exact 'la première', "
                  "all 96 groups mapped, French expansion")
    else:
        verdict = "NEAR-MISS"
        bits = []
        if gt_missing:
            bits.append(f"anchors missing from table: {','.join(gt_missing)}")
        if lp_missing:
            bits.append("'la première' uncheckable (missing groups)")
        if not full_table:
            bits.append(f"partial table ({len(table)}/96 groups)")
        if qscore is not None and qscore < _HIT_QGRAM:
            bits.append(f"expansion score {qscore:.2f}/char below HIT bar {_HIT_QGRAM}")
        if not bits:
            bits.append("consistent but incomplete — no contradiction")
        reason = "; ".join(bits)

    report = {
        "name": args.name or args.table,
        "pairs": len(pairs),
        "table_groups": len(table),
        "anchors": [{"group": g, "expected": want, "table": got, "status": st}
                    for g, want, got, st in anchor_rows],
        "anchors_ok": gt_ok, "anchors_missing": gt_missing,
        "anchors_contradictions": [{"group": g, "expected": want, "table": got}
                                   for g, want, got in contradictions],
        "la_premiere": {
            "pair_index_0based": idx,
            "expected": _EXPECTED_LA_PREMIERE,
            "table_values": got_seq,
            "rows": [{"pair": p, "expected": w, "table": g}
                     for p, w, g in lp_rows],
            "exact": lp_exact,
            "readable": lp_text,
        },
        "provisional_secondary": [{"group": g, "expected": want, "table": got,
                                   "status": st} for g, want, got, st in prov_rows],
        "coverage": {"pairs_mapped": coverage_pairs,
                     "distinct_groups_mapped": coverage_groups},
        "scores": {"quadgram_per_char": qscore,
                   "syllable_bigram_per_syll": sscore,
                   "hit_bar_quadgram": _HIT_QGRAM, "miss_bar_quadgram": _MISS_QGRAM},
        "verdict": verdict,
        "verdict_reason": reason,
    }

    # ---- human-readable ----
    print(f"== Seebach key-hunt tester: {report['name']}")
    print(f"   canonical parse: {len(pairs)} pairs, {len(table)} groups in table, "
          f"coverage {coverage_pairs:.3f} of pairs / {coverage_groups:.3f} of groups")
    print("   anchors (ground truth):")
    for g, want, got, st in anchor_rows:
        print(f"     {g}: expected {want!r}, table {got!r} -> {st}")
    print(f"   pair {idx} (expect 'la première'):")
    for p, want, got in lp_rows:
        mark = "OK" if got == want else ("MISSING" if got is None else "CONTRADICTION")
        print(f"     {p}: expected {want!r}, table {got!r} -> {mark}")
    print(f"     readable: {lp_text!r}  exact={lp_exact}")
    print("   provisional (secondary, non-gating):")
    for g, want, got, st in prov_rows:
        print(f"     {g}: expected {want!r}, table {got!r} -> {st}")
    print(f"   French-likeness: quadgram {qscore if qscore is None else round(qscore, 3)}/char "
          f"(Tocqueville ref -4.25; gibberish -7.7; HIT bar {_HIT_QGRAM})")
    print(f"                    syll-bigram {sscore if sscore is None else round(sscore, 3)}/syll "
          f"(French ref -4.21; scrambled -7.04)")
    print(f"   VERDICT: {verdict} — {reason}")

    if args.out:
        with open(args.out, "w") as fh:
            json.dump(report, fh, indent=2, ensure_ascii=False)
        print(f"   report -> {args.out}")


if __name__ == "__main__":
    main()
