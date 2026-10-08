#!/usr/bin/env python3
"""WORD SEGMENTER — Seebach round 13 council work order 5.

Segments the repaired 1,847-pair R5005 stream using confirmed multi-cell
words (compositional audit products from the Table Reconstructor's Step 2 +
french-blitz confirmations + crowd5 standing units).

Words are matched against the repaired stream; every position is re-derived
here (no banked positions trusted). Outputs:
  - word_boundaries.json : list of (start, end, word, gloss, tier, evidence)
  - coverage + consistency report printed to stdout

Indexing: 0-based pair positions on the repaired parse
(`code/side-keyhunt/repaired_offsets.json`, 1,847 pairs). start = inclusive,
end = exclusive.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))

def load_stream():
    dat = os.path.join(LANE, "data", "upstream-ct_R5005.txt")
    rows = []
    for line in open(dat):
        line = line.strip()
        if line:
            lid, digits = line.split()
            rows.append((lid, re.sub(r"\D", "", digits)))
    off = json.load(open(os.path.join(LANE, "code", "side-keyhunt",
                                      "repaired_offsets.json")))
    seq = []
    for lid, digits in rows:
        o = off[lid]
        seq += [digits[i:i + 2] for i in range(o, len(digits) - 1, 2)]
    assert len(seq) == 1847, len(seq)
    assert len(set(seq)) == 96, len(set(seq))
    return seq

# ---------------------------------------------------------------- word list
# tier: A+ = all-GT; A = GT-anchored conditioned; B = provisional-anchored;
#       C = provisional + MEDIUM/weak.
WORDS = [
    dict(pat=("11", "70", "82", "34", "29", "40"), gloss="la première",
         tier="A+", cells="11=la(GT) 70=pre(GT) 82=m(GT) 34=i(GT) 29=er(GT) 40=e(GT)",
         evidence="7 pencil GT cribs; repair_parse.py asserts exactly 2 pair-aligned "
                  "occurrences (no phantoms); rows a5_03/a6_03."),
    dict(pat=("82", "84"), gloss="m'en",
         tier="A", cells="82=m(GT); 84=\"en\" CONDITIONED iff pre=82",
         evidence="ISLET 1 (conditioner, adjudicator GRANT, F62): 84 reads 'en' iff "
                  "pre=82 — GT-anchored arm. Compositional audit (table-reconstruction §c): "
                  "the 'conditioning predecessor' 82 is the 'm' of the word, not a cell rule."),
    dict(pat=("82", "06"), gloss="ment",
         tier="A", cells="82=m(GT); 06=\"ent\" CONDITIONED iff pre=82",
         evidence="ISLET 3 (conditioner, adjudicator GRANT, F61): F33-form biconditional. "
                  "n=4 predicted windows W06. @1351: 78-94-82-06 = '[78] ne ment pas' (R5)."),
    dict(pat=("96", "00"), gloss="par le",
         tier="B", cells="96=par(PROV); 00=\"le\" CONDITIONED iff pre=96",
         evidence="ISLET 2 (F54, red-team GRANT): 00 reads 'le' (not 'pour') iff pre=96; "
                  "'par pour' ungrammatical at all windows. french-blitz formulae-inventory "
                  "§5 re-confirms ×3."),
    dict(pat=("24", "87"), gloss="en ce",
         tier="B", cells="24=\"en\"(STRONG, F31); 87=\"ce\"(PROV, positional allophone)",
         evidence="Table-reconstruction §c: 24 precedes 87 ten times; 87='ce' after 24 is the "
                  "'en' of 'en ce' — reframes the F56 merger kill as complementary distribution. "
                  "Corpus 'en ce' = 441 (frame59-map)."),
    dict(pat=("87", "01"), gloss="c'est",
         tier="C", cells="87=\"ce\"(PROV); 01=\"est\"(MEDIUM, confirmed)",
         evidence="crowd3 frenchman §4: 'c'est' solid (64-96-43-87-01 ×2 formula); "
                  "closer01: 01='est' CONFIRM at MEDIUM (adjudicator GRANT, round 8, "
                  "RULINGS-FINAL); crowd5 closer87_angles A1: 87->01 ×2 + 47->01 ×1."),
    dict(pat=("96", "87", "46"), gloss="par ce que",
         tier="B", cells="96=par(PROV); 87=\"ce\"(PROV); 46=que(GT)",
         evidence="french-blitz formulae-inventory §5: 'par ce que' ×3 — CONFIRMED formula, "
                  "GT-anchored (46=que GT). Crowd3 frenchman reads the same bytes as fused "
                  "'parce que' (PROVISIONAL per red-team)."),
    # ---- lane-standing bonus (not a round-13 council word; kept for completeness)
    dict(pat=("87", "11"), gloss="cela",
         tier="B*", cells="87=\"ce\"(PROV); 11=la(GT)",
         evidence="crowd5 unit_inventory §2 (ear-spelling regularity, frenchman-verified): "
                  "'cela' = 87-11 ×7; 87->11 P=0.219. Standing unit, not round-13 council work."),
]

BANKED = {
    "la première": {"n": 2, "starts": [754, 1034]},
    "m'en":        {"n": None, "starts": None},   # islet says GT-arm n_eff=1
    "ment":        {"n": 4, "starts": [579, 737, 1183, 1354]},
    "par le":      {"n": 3, "starts": [47, 465, 960]},
    "en ce":       {"n": 10, "starts": None},
    "c'est":       {"n": 2, "starts": [344, 1028]},
    "par ce que":  {"n": 3, "starts": [224, 952, 1526]},
    "cela":        {"n": 7, "starts": None},
}

def census(seq, pat):
    k = len(pat)
    return [i for i in range(len(seq) - k + 1) if tuple(seq[i:i + k]) == pat]

def main():
    seq = load_stream()
    N = len(seq)
    segments = []
    report = {"N": N, "words": {}, "overlaps": [], "consistency": {}}

    for w in WORDS:
        pat = w["pat"]; gloss = w["gloss"]
        hits = census(seq, pat)
        contexts = []
        for s in hits:
            pre = seq[s - 1] if s > 0 else None
            suc = seq[s + len(pat)] if s + len(pat) < N else None
            contexts.append({"start": s, "pre": pre, "suc": suc})
        segments += [dict(start=s, end=s + len(pat), word=list(pat),
                          gloss=gloss, tier=w["tier"], cells=w["cells"],
                          evidence=w["evidence"]) for s in hits]
        b = BANKED[gloss]
        match = True
        notes = []
        if b["n"] is not None and len(hits) != b["n"]:
            match = False; notes.append(f"COUNT MISMATCH: banked n={b['n']}, found {len(hits)}")
        if b["starts"] is not None:
            if sorted(hits) != sorted(b["starts"]):
                match = False
                notes.append(f"POSITION MISMATCH: banked {sorted(b['starts'])}, found {sorted(hits)}")
        report["words"][gloss] = {
            "pattern": list(pat), "tier": w["tier"], "n": len(hits),
            "starts": sorted(hits), "contexts": contexts,
            "banked_match": match, "banked_notes": notes,
        }
        print(f"{gloss:>12} {'-'.join(pat):<22} n={len(hits):>3} "
              f"starts={sorted(hits)} {'OK' if match else '*** MISMATCH: ' + '; '.join(notes)}")

    # ---- coverage (union of covered pairs)
    covered = [False] * N
    for s_ in segments:
        for i in range(s_["start"], s_["end"]):
            covered[i] = True
    cov = sum(covered)
    print(f"\nCOVERAGE: {cov}/{N} = {cov / N:.4f} ({100 * cov / N:.2f}%)")
    report["coverage"] = {"pairs": cov, "N": N, "fraction": cov / N}

    # per-tier coverage
    for t in ["A+", "A", "B", "B*", "C"]:
        cv = [False] * N
        for s_ in segments:
            if s_["tier"] == t:
                for i in range(s_["start"], s_["end"]):
                    cv[i] = True
        print(f"  tier {t:<3}: {sum(cv):>4} pairs ({100 * sum(cv) / N:.2f}%)")
    report["tier_coverage"] = {t: sum(
        any(i in range(s_["start"], s_["end"]) for s_ in segments if s_["tier"] == t)
        for i in range(N)) for t in ["A+", "A", "B", "B*", "C"]}

    # ---- per-segment status + conflict adjudication
    # status: live | live* (live with adjacency tension noted) |
    #         suspect (word boundary questionable) | superseded (boundary withdrawn)
    STATUS = {}
    def set_status(gloss, starts, status, note):
        for s in starts:
            STATUS[(gloss, s)] = (status, note)

    set_status("en ce", [73, 162, 829], "superseded",
        "87 contested by 'cela' (87-11): trigram 24-87-11 reads 'en cela' "
        "(period corpus: 'en cela' 8x, 'en ce la' 0x). 'en ce'+'la' is "
        "ungrammatical; 'en'+'cela' is grammatical. Boundary withdrawn; pairs "
        "remain covered by 'cela'.")
    set_status("en ce", [823], "live*",
        "Adjacent 59='est'(PROV)@825 collides: 'en ce est' ungrammatical "
        "('ce est'=0, frame59-map: window UNCLASSIFIED, value OPEN). Symmetric "
        "tension — constrains 59@825, does not falsify 'en ce'.")
    set_status("ment", [579, 1183], "suspect",
        "Followed by 06 (verb-stem class): 'ne ment [06]' lacks 'pas' (bare "
        "'ne ment' 0x period corpus vs 'il ne ment pas' attested RdM). Competing "
        "parse m|ent|[06-stem] ('m\\'entend'-type) — ISLET 3 'ent' reading at 06 "
        "stands; only the word boundary after 06 is suspect.")
    set_status("m'en", [166], "live*",
        "Left neighbor 24='en'(STRONG)@165 gives 'en m\\'en' (period corpus 0x). "
        "Pressures 24@165 (or the 94-24 junction), not the GT-anchored word.")
    set_status("par le", [47], "live*",
        "Left neighbor 62='on': pronoun reading gives 'on par le' "
        "(ungrammatical); resolved by 62's known syllable-'on' polyvalence "
        "(pers|on|ne @507, unit_inventory R2/R4). Not a boundary problem.")
    set_status("cela", [1242, 1403], "live*",
        "87's word-membership contested by council-drag lead 'le prince' "
        "(77-81-87@1240/@1401, drag_hits.json — LEAD, FDR 1.41/9, unconfirmed): "
        "'le prince'+'la' vs 'le [81]'+'cela'. Both windows byte-parallel "
        "(67-77-81-87-11-00). Neither parse breaks a board reading; unresolved "
        "at current board — 81 unidentified.")
    # drag 'tout ce qui' overlap (board-incompatible at 24-windows)
    set_status("en ce", [179, 1766, 1774], "live*",
        "Council-drag lead 'tout ce qui' (24-87-64) overlaps but requires "
        "24='tout', contradicting 24='en' STRONG (F31) — drag oracle does not "
        "encode 24, so it scored neutral. 'en ce qui' is board-clean and "
        "grammatical; drag lead survives only @1799 (79-87-64, 79 unidentified).")

    for s_ in segments:
        key = (s_["gloss"], s_["start"])
        s_["status"], s_["conflict_note"] = STATUS.get(key, ("live", ""))
    print("\nOVERLAPS (segments sharing >=1 pair):")
    segs = sorted(segments, key=lambda s: s["start"])
    for a in range(len(segs)):
        for b_ in range(a + 1, len(segs)):
            sa, sb = segs[a], segs[b_]
            if sb["start"] >= sa["end"]:
                break
            shared = list(range(max(sa["start"], sb["start"]), min(sa["end"], sb["end"])))
            if not shared:
                continue
            entry = {"seg_a": {k: sa[k] for k in ("start", "end", "gloss", "tier")},
                     "seg_b": {k: sb[k] for k in ("start", "end", "gloss", "tier")},
                     "shared_pairs": shared,
                     "shared_cells": [seq[i] for i in shared]}
            report["overlaps"].append(entry)
            print(f"  [{sa['start']},{sa['end']}) '{sa['gloss']}'({sa['tier']}) x "
                  f"[{sb['start']},{sb['end']}) '{sb['gloss']}'({sb['tier']}) "
                  f"share pairs {shared} = {entry['shared_cells']}")
    if not report["overlaps"]:
        print("  none")

    # ---- council-drag integration (drag_hits.json landed mid-task, 2026-10-07 23:06)
    report["council_drag"] = {
        "landed": True,
        "new_confirmed_words": [],
        "note": ("drag_hits.json (code/council/drag): 9 primary hits, FDR estimate "
                 "1.41, real does NOT beat all 20 shuffles — hits are LEADS, none "
                 "promoted to confirmed. Positive control 'par ce que' "
                 "@224/@952/@1526 PASS (independent re-confirmation of W7). "
                 "'tout ce qui'@179/@1766/@1774 overlaps 'en ce' but requires "
                 "24='tout' vs 24='en' STRONG (F31) — board-incompatible, dead at "
                 "those windows; survives only @1799 (79-87-64, 79 unidentified). "
                 "'le prince'@1240/@1401 overlaps 'cela'@1242/@1403 on 87 — genuine "
                 "word-membership ambiguity, flagged live*."),
        "null_report": ("null_report.json: h_real=9, fdr_estimate=1.411, "
                        "real_beats_all_shuffles=false")} 

    # ---- consistency checks
    print("\nCONSISTENCY CHECKS:")
    cons = report["consistency"]

    # C1: conditioned words must not occur outside their registered domain.
    # (bigrams are domain-defining by construction; the check is whether the
    #  conditioning cell shows unexpected contexts, e.g. 82-84 where 84 was
    #  banked as something else)
    # C2: no word may collide with a HIGHER-tier word on the same pair.
    tier_rank = {"A+": 4, "A": 3, "B": 2, "B*": 2, "C": 1}
    hi_conflicts = [o for o in report["overlaps"]
                    if tier_rank[o["seg_a"]["tier"]] != tier_rank[o["seg_b"]["tier"]]]
    cons["cross_tier_overlaps"] = hi_conflicts
    print(f"  C2 cross-tier overlaps: {len(hi_conflicts)}")
    for o in hi_conflicts:
        print(f"      {o}")

    # C3: every conditioned word's cells satisfy their islet conditions
    #     (tautological for bigrams, but verify the conditioning cell's OTHER
    #     occurrences don't sit inside a confirmed word under a false reading)
    # C4: check the 47-01 'c'est'-analog (47='ce' LEAD) does not collide
    alt_4701 = census(seq, ("47", "01"))
    cons["47-01_analog_starts"] = alt_4701
    print(f"  C4 47-01 'c\\'est'-analog (47=ce LEAD) starts: {alt_4701}")

    # C5: does 94-87 occur ('en ce' on the conditioned-94 arm — EXCLUDED variant)?
    v9487 = census(seq, ("94", "87"))
    cons["94-87_en-ce-variant_starts"] = v9487
    print(f"  C5 94-87 ('en ce' on conditioned-94 arm, EXCLUDED) starts: {v9487}")

    # C6: adjacency sanity — for each word occurrence, record whether the
    #     neighbor cells carry board values that would make the word's French
    #     reading locally ungrammatical (manual audit list, not auto-kill)
    cons["adjacency_note"] = ("adjacency contexts recorded per word above; "
        "no mechanical grammar oracle — the falsifier to watch is a confirmed "
        "word whose reading is contradicted by a GT/provisional neighbor "
        "(e.g. 'par le' followed by a verb, 'm\\'en' followed by a noun).")

    out = os.path.join(HERE, "word_boundaries.json")
    with open(out, "w") as f:
        json.dump({"meta": {
            "lane": "zeschau-seebach-1841", "round": "13-council",
            "parse": "repaired 1,847-pair (code/side-keyhunt/repaired_offsets.json), "
                     "0-based pair positions; start inclusive, end exclusive",
            "tiers": {"A+": "all cells GT", "A": "GT-anchored, conditioned reading",
                      "B": "provisional-anchored", "B*": "provisional, lane-standing "
                      "(crowd5, not council)", "C": "provisional + MEDIUM"},
            "n_segments": len(segments),
            "coverage_pairs": cov, "coverage_fraction": round(cov / N, 6)},
            "segments": sorted(segments, key=lambda s: s["start"]),
            "report": report}, f, indent=1)
    print(f"\nwrote {out} ({len(segments)} segments)")

if __name__ == "__main__":
    main()
