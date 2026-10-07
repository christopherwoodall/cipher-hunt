#!/usr/bin/env python3
"""VERIFIER A -- independent bedrock re-derivation for the Seebach cipher lane.

Recomputes standing facts from PRIMARY sources only:
  data/upstream-ct_R5005.digits.txt   (raw digit rows, file order)
  data/upstream-offsets.json          (original per-row offset bits)
  code/side-keyhunt/repaired_offsets.json  (claimed one-bit repair a5_03 1->0)
  data/upstream-ct_R5005.txt          (tagged rows; used ONLY to check row order)

Pairing convention (from data/upstream-NOTES.md + REINDEX.md, re-derived here):
  each row is paired independently; offset=1 drops the row's first digit,
  then digits are paired left-to-right; a trailing digit is dropped when the
  remaining length is odd. Rows concatenate in file/tag order.

All parsing logic below is written fresh. Lane code was not imported or copied.
Prints PASS/FAIL per fact and writes verifier_a_results.json next to this file.
"""

import json
import re
from collections import Counter
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
DATA = LANE / "data"
OUT = Path(__file__).resolve().parent

RESULTS = []  # list of dicts


def record(fact, claimed, computed, verdict, notes=""):
    RESULTS.append({
        "fact": fact, "claimed": claimed, "computed": computed,
        "verdict": verdict, "notes": notes,
    })
    tag = {"PASS": "PASS", "FAIL": "FAIL"}.get(verdict, verdict)
    print(f"[{tag}] {fact}")
    print(f"       claimed={claimed} computed={computed}" + (f"  ({notes})" if notes else ""))


def load_sources():
    offsets_orig = json.loads((DATA / "upstream-offsets.json").read_text())
    offsets_rep = json.loads((LANE / "code/side-keyhunt/repaired_offsets.json").read_text())
    digit_lines = (DATA / "upstream-ct_R5005.digits.txt").read_text().split()
    tagged = {}
    for ln in (DATA / "upstream-ct_R5005.txt").read_text().splitlines():
        t, d = ln.split()
        tagged[t] = d
    tags = list(offsets_orig.keys())
    assert len(tags) == len(digit_lines) == len(tagged), "row-count mismatch across sources"
    for i, tag in enumerate(tags):
        assert tagged[tag] == digit_lines[i], f"row {i} tag/digits mismatch ({tag})"
    rows = [(tag, digit_lines[i]) for i, tag in enumerate(tags)]
    for ln in digit_lines:
        assert re.fullmatch(r"[0-9]+", ln), "non-digit row"
    return rows, offsets_orig, offsets_rep


def parse(rows, offsets):
    """Independent per-row pairing. Returns (pairs, stats).

    pairs: list of (group, row_tag). stats: digit accounting.
    """
    pairs = []
    dropped_by_offset = 0
    dropped_by_odd = 0
    for tag, line in rows:
        off = offsets[tag]
        assert off in (0, 1), f"bad offset bit for {tag}"
        body = line[off:]            # offset=1 discards the row's first digit
        dropped_by_offset += off
        n = len(body) // 2
        dropped_by_odd += len(body) % 2
        for k in range(n):
            pairs.append((body[2 * k:2 * k + 2], tag))
    total_digits = sum(len(line) for _, line in rows)
    dropped = dropped_by_offset + dropped_by_odd
    assert 2 * len(pairs) + dropped == total_digits, "digit accounting broken"
    return pairs, {
        "total_digits": total_digits,
        "n_pairs": len(pairs),
        "paired_digits": 2 * len(pairs),
        "dropped": dropped,
        "dropped_by_offset": dropped_by_offset,
        "dropped_by_odd": dropped_by_odd,
    }


def groups_of(pairs):
    return [g for g, _ in pairs]


def window_positions(gs, pattern):
    n = len(pattern)
    return [i for i in range(len(gs) - n + 1) if gs[i:i + n] == pattern]


def bigram_positions(gs, a, b):
    return [i for i in range(len(gs) - 1) if gs[i] == a and gs[i + 1] == b]


def main():
    rows, offsets_orig, offsets_rep = load_sources()

    # ---- 1. transcription ----
    total_digits = sum(len(line) for _, line in rows)
    record("transcription_digits", 3764, total_digits,
           "PASS" if total_digits == 3764 else "FAIL")
    record("transcription_rows", 70, len(rows),
           "PASS" if len(rows) == 70 else "FAIL")

    # ---- 2. canonical parses ----
    pairs_rep, st_rep = parse(rows, offsets_rep)
    pairs_orig, st_orig = parse(rows, offsets_orig)
    gs_rep = groups_of(pairs_rep)
    gs_orig = groups_of(pairs_orig)

    record("repaired_pairs", 1847, st_rep["n_pairs"],
           "PASS" if st_rep["n_pairs"] == 1847 else "FAIL")
    distinct_rep = len(set(gs_rep))
    record("repaired_distinct_groups", 96, distinct_rep,
           "PASS" if distinct_rep == 96 else "FAIL")
    missing = sorted({f"{a}{b}" for a in "0123456789" for b in "0123456789"} - set(gs_rep))
    record("digit_accounting_repaired",
           {"paired": 3694, "dropped": 70},
           {"paired": st_rep["paired_digits"], "dropped": st_rep["dropped"],
            "dropped_by_offset": st_rep["dropped_by_offset"],
            "dropped_by_odd": st_rep["dropped_by_odd"]},
           "PASS" if (st_rep["paired_digits"], st_rep["dropped"]) == (3694, 70) else "FAIL",
           f"unobserved groups: {missing}")
    record("original_pairs", 1846, st_orig["n_pairs"],
           "PASS" if st_orig["n_pairs"] == 1846 else "FAIL",
           "sanity: 1846->1847 is the repair's +1")

    # repair-region boundaries, derived (first pair index of row a5_03 in each parse)
    b_rep = next(i for i, (_, t) in enumerate(pairs_rep) if t == "a5_03")
    b_orig = next(i for i, (_, t) in enumerate(pairs_orig) if t == "a5_03")
    n_a503_rep = sum(1 for _, t in pairs_rep if t == "a5_03")
    n_a503_orig = sum(1 for _, t in pairs_orig if t == "a5_03")
    before_ok = [g for g, _ in pairs_rep[:b_rep]] == [g for g, _ in pairs_orig[:b_orig]]
    after_ok = ([g for g, _ in pairs_rep[b_rep + n_a503_rep:]] ==
                [g for g, _ in pairs_orig[b_orig + n_a503_orig:]])
    record("repair_locality",
           {"a5_03_start_rep": 748, "a5_03_start_orig": 748,
            "a5_03_pairs_rep": 26, "a5_03_pairs_orig": 25,
            "before_identical": True, "after_identical": True},
           {"a5_03_start_rep": b_rep, "a5_03_start_orig": b_orig,
            "a5_03_pairs_rep": n_a503_rep, "a5_03_pairs_orig": n_a503_orig,
            "before_identical": before_ok, "after_identical": after_ok},
           "PASS" if (b_rep, b_orig, n_a503_rep, n_a503_orig, before_ok, after_ok)
           == (748, 748, 26, 25, True, True) else "FAIL",
           "repair touches only row a5_03; delta is even so downstream phases hold")

    # ---- 3. the repair's validity ----
    raw = "".join(line for _, line in rows)
    crib = "117082342940"
    raw_hits = [m.start() for m in re.finditer(f"(?={crib})", raw)]
    record("raw_crib_positions", [1532, 2108], raw_hits,
           "PASS" if raw_hits == [1532, 2108] else "FAIL",
           "0-based index into concatenated digit stream")

    crib_groups = ["11", "70", "82", "34", "29", "40"]
    rep_crib = window_positions(gs_rep, crib_groups)
    rep_crib_tags = sorted({pairs_rep[i][1] for i in rep_crib})
    record("repaired_crib_pairs", {"positions": [754, 1034], "rows": ["a5_03", "a6_03"]},
           {"positions": rep_crib, "rows": rep_crib_tags},
           "PASS" if rep_crib == [754, 1034] and rep_crib_tags == ["a5_03", "a6_03"] else "FAIL")

    orig_crib = window_positions(gs_orig, crib_groups)
    record("original_crib_pairs",
           {"n_occurrences": 1, "old_index": 1033, "note": "task text says 1034 = NEW-index value"},
           {"n_occurrences": len(orig_crib), "old_positions": orig_crib},
           "PASS" if orig_crib == [1033] else "FAIL",
           "old 1033 + 1 (repair shift) = new 1034")

    # the crib starts at within-row offset 12 of a5_03; under original offsets
    # (phase 1) the crib's first pair is the row's 6th pair (global old 753)
    orig_a503_offphase = gs_orig[b_orig + 5:b_orig + 12]
    record("original_a5_03_offphase_read",
           ["71", "17", "08", "23", "42", "94", "02"], orig_a503_offphase,
           "PASS" if orig_a503_offphase == ["71", "17", "08", "23", "42", "94", "02"] else "FAIL",
           "crib read off-phase: row pairs 5..11 under original offsets (global old 753..759)")

    # raw position 1532 lands inside row a5_03 and is even-phase under repaired offsets
    cum = 0
    row_of_1532 = row_of_2108 = None
    for tag, line in rows:
        if cum <= 1532 < cum + len(line):
            row_of_1532 = (tag, 1532 - cum)
        if cum <= 2108 < cum + len(line):
            row_of_2108 = (tag, 2108 - cum)
        cum += len(line)
    record("gloss_line_premise_check",
           "N/A (no manuscript images available to the lane)",
           {"raw1532_row": row_of_1532, "raw2108_row": row_of_2108,
            "raw1532_at_pair_start_under_repaired_offsets": row_of_1532[1] % 2 == 0},
           "N/A",
           "VALID-GIVEN-PREMISE: crib occurs twice raw; repaired parse puts "
           "11 70 82 34 29 40 on rows a5_03/a6_03 exactly. UNVERIFIABLE PREMISE: "
           "whether the erased pencil gloss really sits over row a5_03 cannot be "
           "checked from available sources (no manuscript images re-examined).")

    # ---- 4. group frequencies (repaired stream) ----
    freq = Counter(gs_rep)
    assert sum(freq.values()) == 1847 and len(freq) == 96
    headline = {"62": 35, "24": 52, "52": 27, "06": 44, "78": 31,
                "87": 32, "64": 46, "96": 21}
    freq_orig = Counter(gs_orig)
    for g, claimed in headline.items():
        ok = freq[g] == claimed
        stale = (not ok) and freq_orig[g] == claimed
        record(f"n{g}", claimed, freq[g],
               "PASS" if ok else "FAIL",
               "STALE PRE-REPAIR CLAIM" if stale else "")
    # further counts stated in NOTES.md (Phase-A block, lines 24-25; F17 line 187)
    extra = {"00": 54, "11": 44, "70": 15, "82": 38, "34": 10,
             "29": 47, "40": 21, "46": 29}
    freq_orig = Counter(gs_orig)
    for g, claimed in extra.items():
        ok = freq[g] == claimed
        stale = (not ok) and freq_orig[g] == claimed
        record(f"n{g}", claimed, freq[g],
               "PASS" if ok else "FAIL",
               "STALE PRE-REPAIR CLAIM" if stale else "")
    # rank sanity on the repaired parse (competition ranking)
    ranked = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    comp_rank = {g: 1 + sum(1 for h in freq if freq[h] > c) for g, c in freq.items()}
    top10 = [(g, freq[g], comp_rank[g]) for g, _ in ranked[:10]]
    record("rank_00_leads", {"group": "00", "rank": 1}, {"group": ranked[0][0], "rank": comp_rank["00"]},
           "PASS" if ranked[0][0] == "00" else "FAIL",
           f"top10 (group,count,rank): {top10}")
    record("rank_24_second", 2, comp_rank["24"],
           "PASS" if comp_rank["24"] == 2 else "FAIL",
           f"n24={freq['24']}")
    # n77/n47/n67/n43/n84/n59: no explicit unigram claims found in NOTES.md
    for g in ["77", "47", "67", "43", "84", "59"]:
        record(f"n{g}", "no explicit claim in NOTES.md", freq[g], "N/A",
               "pre-repair B_scan (npairs=1846) gave 77=44, 59=26; others unstated")

    # ---- 5. windows / bigrams / trigrams (repaired stream, 0-based) ----
    w = window_positions(gs_rep, ["62", "94"])
    record("windows_62_94",
           [100, 508, 761, 840, 1329, 1362, 1686, 1704, 1772], w,
           "PASS" if w == [100, 508, 761, 840, 1329, 1362, 1686, 1704, 1772] else "FAIL",
           "old onne_at [100,508,839,1328,1361,1685,1703,1771] remapped +1 for >=773, plus 9th @761")

    t = window_positions(gs_rep, ["24", "87", "64"])
    record("trigram_24_87_64", [179, 1766, 1774], t,
           "PASS" if t == [179, 1766, 1774] else "FAIL",
           "position = index of the 24")

    f = window_positions(gs_rep, ["64", "96", "43", "87", "01"])
    record("formula_64_96_43_87_01", [341, 1025], f,
           "PASS" if f == [341, 1025] else "FAIL",
           "F18 claimed @341/@1024 on the 1846 parse; 1024>=773 so +1")

    b = bigram_positions(gs_rep, "06", "29")
    record("bigram_06_29_count", 4, len(b),
           "PASS" if len(b) == 4 else "FAIL",
           f"positions={b}")

    b = bigram_positions(gs_rep, "00", "86")
    record("bigram_00_86_count", 12, len(b),
           "PASS" if len(b) == 12 else "FAIL",
           f"positions={b}")

    b = bigram_positions(gs_rep, "00", "06")
    record("bigram_00_06_count", 0, len(b),
           "PASS" if len(b) == 0 else "FAIL",
           f"positions={b}")

    b = bigram_positions(gs_rep, "77", "86")
    b_orig = bigram_positions(gs_orig, "77", "86")
    record("bigram_77_86_positions", [430, 798, 877, 950, 1133], b,
           "PASS" if b == [430, 798, 877, 950, 1133] else "FAIL",
           f"original-parse positions={b_orig}; the N25 'new' = new-indexing, verified")

    b = bigram_positions(gs_rep, "77", "78")
    record("bigram_77_78_count", 7, len(b),
           "PASS" if len(b) == 7 else "FAIL",
           f"positions={b}")

    b = bigram_positions(gs_rep, "94", "82")
    record("bigram_94_82_positions", [578, 1182, 1353, 1742], b,
           "PASS" if b == [578, 1182, 1353, 1742] else "FAIL",
           "F24 claimed @[578,1181,1352,1741] on the 1846 parse; +1 for >=773")

    w = window_positions(gs_rep, ["87", "64", "77", "84"])
    record("window_87_64_77_84", [1800], w,
           "PASS" if w == [1800] else "FAIL")

    w = window_positions(gs_rep, ["11", "67"])
    record("window_11_67_la_veut", [1044], w,
           "PASS" if w == [1044] else "FAIL",
           "unique 'la veut'")

    (OUT / "verifier_a_results.json").write_text(json.dumps(RESULTS, indent=1) + "\n")
    fails = [r for r in RESULTS if r["verdict"] == "FAIL"]
    print(f"\n==== {len(RESULTS) - len(fails)}/{len(RESULTS)} PASS, {len(fails)} FAIL ====")
    for r in fails:
        print("FAIL:", r["fact"])


if __name__ == "__main__":
    main()
