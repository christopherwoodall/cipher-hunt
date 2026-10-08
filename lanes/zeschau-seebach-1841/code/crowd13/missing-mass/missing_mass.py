#!/usr/bin/env python3
"""Missing-mass inventory — Seebach round 13, council work order 6.

Per PREREG.md: era syllable rates (clean diplomatic corpus, lane syllabifier)
vs observed rates of the 12 identified cells -> deficit table -> predicted
missing-homophone counts -> ranked candidate lists by contact-profile match.
Secondary: digit hunt on the 8 groups with n<5.

Writes JSON + MD artifacts into this directory. No value assignments made.
"""
import json, os, re, math, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
DATA = os.path.join(LANE, "data")
CORPUS = os.path.join(LANE, "code", "side-period", "corpus")
sys.path.insert(0, os.path.join(LANE, "code", "side-keyhunt"))
from build_syll_model import syllabify  # lane-established syllabifier

# ---------- 1. repaired 1,847-pair stream ----------
def load_repaired_pairs():
    base = json.load(open(os.path.join(DATA, "upstream-offsets.json")))
    assert base["a5_03"] == 1, "upstream EM choice changed; re-audit needed"
    off = dict(base); off["a5_03"] = 0
    pairs = []
    for line in open(os.path.join(DATA, "upstream-ct_R5005.txt")):
        line = line.strip()
        if not line: continue
        lid, digits = line.split()
        digits = re.sub(r"\D", "", digits)
        o = off[lid]
        pairs += [digits[i:i+2] for i in range(o, len(digits)-1, 2)]
    assert len(pairs) == 1847, len(pairs)
    assert len(set(pairs)) == 96, len(set(pairs))
    return pairs

# ---------- 2. corpus: French files only ----------
FRENCH_FILES = [
    "guizot-memoires-t1-gutenberg.txt", "guizot-memoires-t2-gutenberg.txt",
    "guizot-memoires-t3-gutenberg.txt", "guizot-memoires-t5-t6.txt",
    "nesselrode-v7.txt", "nesselrode-v8.txt", "nesselrode-v9.txt", "nesselrode-v10.txt",
    "pozzo-di-borgo-correspondance-v1.txt",
    "revue-deux-mondes-1841-q1.txt", "revue-deux-mondes-1841-q2.txt",
    "revue-deux-mondes-1841-q3.txt", "revue-deux-mondes-1841-q4.txt",
    "talleyrand-memoires-v1.txt",
]
WORD_RE = re.compile(r"[a-zàâäéèêëiîïoôöuùûüyçœæ]+")

def corpus_counts(cache_path):
    if os.path.exists(cache_path):
        return json.load(open(cache_path))
    syl = Counter(); wordtok = Counter(); n_words = 0; n_files = 0
    for fn in FRENCH_FILES:
        p = os.path.join(CORPUS, fn)
        if not os.path.exists(p):
            print("MISSING", fn); continue
        n_files += 1
        text = open(p, encoding="utf-8", errors="replace").read().lower()
        # elisions: split on apostrophes so "m'" -> "m", "qu'" -> "qu"
        text = re.sub(r"['’`]", " ", text)
        for m in WORD_RE.finditer(text):
            w = m.group(0); n_words += 1
            wordtok[w] += 1
            for s in syllabify(w):
                syl[s] += 1
    out = {"syllable_counts": dict(syl), "word_counts": dict(wordtok),
           "n_words": n_words, "n_files": n_files,
           "n_syllables": sum(syl.values())}
    json.dump(out, open(cache_path, "w"))
    return out

# ---------- 3. cipher-side stats ----------
IDENTIFIED = {  # group -> (value, tier); tiers per STATE/N52
    "11": ("la", "GT"), "70": ("pre", "GT"), "82": ("m", "GT"),
    "34": ("i", "GT"), "29": ("er", "GT"), "40": ("e", "GT"),
    "46": ("que", "GT"),
    "87": ("ce", "prov"), "64": ("qui", "prov"), "96": ("par", "prov"),
    "59": ("est", "prov"), "77": ("le", "prov-cond"),
}
# sensitivity variants (not part of the 12)
VARIANT_CELLS = {"94": ("ne", "prov-strong(reconstructor)"),
                 "00": ("pour", "STRONG-LEAD(islet2-residual)")}

def main():
    pairs = load_repaired_pairs()
    N = len(pairs)
    groups = sorted(set(pairs))
    freq = Counter(pairs)
    MEAN_CELL = N / 96.0

    # contact vectors: concatenated pre + suc count vectors over group vocab
    gi = {g: i for i, g in enumerate(groups)}
    pre = defaultdict(Counter); suc = defaultdict(Counter)
    for a, b in zip(pairs[:-1], pairs[1:]):
        suc[a][b] += 1; pre[b][a] += 1
    def vec(g):
        v = [0.0] * (2 * 96)
        for h, c in pre[g].items(): v[gi[h]] = c
        for h, c in suc[g].items(): v[96 + gi[h]] = c
        return v
    V = {g: vec(g) for g in groups}
    def cos(a, b):
        va, vb = V[a], V[b]
        d = sum(x*x for x in va) ** 0.5 * sum(x*x for x in vb) ** 0.5
        return sum(x*y for x, y in zip(va, vb)) / d if d else 0.0

    phase = json.load(open(os.path.join(LANE, "code", "crowd4", "phase_map_repaired.json")))

    # ---------- 4. era syllable rates ----------
    cc = corpus_counts(os.path.join(HERE, "corpus_counts.json"))
    S = cc["n_syllables"]
    sylc = Counter(cc["syllable_counts"]); wordc = Counter(cc["word_counts"])
    era_rate = {s: c / S for s, c in sylc.items()}
    top15 = [s for s, _ in sylc.most_common(15)]

    # comparators for identified values
    # word-valued cells (que, qui never survive the syllabifier as syllables):
    word_valued = {"que": "que", "qui": "qui"}
    # by-ear letter cells: standalone token comparator (low confidence)
    letter_cells = {"m": "82", "i": "34", "e": "40"}

    def era_for(value, group):
        if value in word_valued:
            return wordc.get(word_valued[value], 0) / S, "word-token"
        if group in letter_cells.values() or value in letter_cells:
            return wordc.get(value, 0) / S, "standalone-letter-token(LOW-CONF)"
        return sylc.get(value, 0) / S, "syllable"

    rows = []
    # union: top-15 syllables + all identified values
    keys = list(dict.fromkeys(top15 + [v for v, t in IDENTIFIED.values()]))
    for s in keys:
        cov = [(g, v, t) for g, (v, t) in IDENTIFIED.items() if v == s]
        # variant cells never auto-cover; handled in sensitivity section
        obs_n = sum(freq[g] for g, _, _ in cov)
        obs_rate = obs_n / N
        er, kind = era_for(s, cov[0][0] if cov else None)
        era_n = er * N
        deficit_occ = era_n - obs_n
        z = (obs_n - era_n) / math.sqrt(era_n * (1 - er)) if era_n > 0 else 0.0
        missing_cells = deficit_occ / MEAN_CELL
        flag = deficit_occ >= MEAN_CELL and z < -2.0
        strong = deficit_occ >= 2 * MEAN_CELL or z < -3.0
        rows.append({"syllable": s, "era_rate": er, "era_kind": kind,
                     "cells": [(g, v, t, freq[g]) for g, v, t in cov],
                     "obs_n": obs_n, "obs_rate": obs_rate,
                     "era_n": era_n, "deficit_occ": deficit_occ,
                     "z": z, "missing_cells": missing_cells,
                     "flag": bool(flag), "strong": bool(strong and flag)})
    rows.sort(key=lambda r: -r["deficit_occ"])

    json.dump({"rows": rows, "N": N, "S": S, "mean_cell": MEAN_CELL,
               "top15": top15,
               "freq": {g: freq[g] for g in groups}},
              open(os.path.join(HERE, "deficit_table.json"), "w"), indent=1)

    # ---------- 5. ranked candidates for strong deficits ----------
    unidentified = [g for g in groups if g not in IDENTIFIED]
    cand = {}
    for r in rows:
        if not (r["strong"] and r["cells"]):
            continue
        g0 = r["cells"][0][0]
        sims = sorted(((cos(g0, g), g, freq[g], phase.get(g)) for g in unidentified),
                      key=lambda x: -x[0])
        cand[r["syllable"]] = {
            "known_cell": g0, "known_phase": phase.get(g0),
            "top": [{"group": g, "sim": round(s, 3), "n": n, "phase": ph,
                     "phase_match": ph == phase.get(g0)}
                    for s, g, n, ph in sims[:8]]}
    json.dump(cand, open(os.path.join(HERE, "candidate_rankings.json"), "w"), indent=1)

    # ---------- 6. digit hunt ----------
    low = [g for g in groups if freq[g] < 5]
    top20 = {g for g, _ in freq.most_common(20)}
    digit = {}
    for g in low:
        pos = [i for i, x in enumerate(pairs) if x == g]
        pre_set = set(pre[g]); suc_set = set(suc[g])
        digit[g] = {
            "n": freq[g], "phase": phase.get(g),
            "positions": pos,
            "start5pct": sum(1 for p in pos if p < 0.05 * N),
            "end5pct": sum(1 for p in pos if p > 0.95 * N),
            "distinct_pre": len(pre_set), "distinct_suc": len(suc_set),
            "pre": sorted(pre_set), "suc": sorted(suc_set),
            "contact_top20": sum(1 for h in pre_set | suc_set if h in top20),
            "adjacent_low": sum(1 for h in pre_set | suc_set if h in low and h != g),
        }
    # T1: digit-digit adjacency vs null
    lowpos = set(i for i, x in enumerate(pairs) if x in low)
    obs_adj = sum(1 for i in range(N - 1) if pairs[i] in low and pairs[i+1] in low)
    import random
    rng = random.Random(20261007)
    nulls = []
    idx = list(range(N))
    for _ in range(200):
        lp = set(rng.sample(idx, len(lowpos)))
        nulls.append(sum(1 for i in range(N - 1) if i in lp and i + 1 in lp))
    digit_meta = {"low_groups": {g: digit[g] for g in low},
                  "digit_digit_adjacent": obs_adj,
                  "null_mean": sum(nulls) / len(nulls),
                  "null_max": max(nulls)}
    json.dump(digit_meta, open(os.path.join(HERE, "digit_hunt.json"), "w"), indent=1)

    # ---------- 7. markdown render ----------
    with open(os.path.join(HERE, "DEFICIT.md"), "w") as f:
        f.write("# Missing-mass deficit table\n\n")
        f.write(f"Stream N={N} pairs, 96 groups, mean cell rate={MEAN_CELL:.2f}. "
                f"Corpus: {cc['n_files']} French files, {cc['n_words']:,} words, "
                f"{S:,} syllables (lane syllabifier).\n\n")
        f.write("| syllable | era rate | kind | identified cell(s) | obs n | "
                "era-expected n | deficit occ | z | missing cells | verdict |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---|\n")
        for r in rows:
            cells = ",".join(g for g, v, t, n in r["cells"]) or "—"
            ver = "STRONG" if r["strong"] else ("FLAG" if r["flag"] else
                  ("surplus" if r["deficit_occ"] < -MEAN_CELL else "ok"))
            f.write(f"| {r['syllable']} | {r['era_rate']:.4f} | {r['era_kind']} | "
                    f"{cells} | {r['obs_n']} | {r['era_n']:.1f} | "
                    f"{r['deficit_occ']:+.1f} | {r['z']:+.2f} | "
                    f"{r['missing_cells']:+.2f} | {ver} |\n")
        f.write("\nFLAG = deficit ≥ 1 mean cell AND z < −2. "
                "STRONG = ≥ 2 cells OR z < −3 (pre-registered).\n")
    with open(os.path.join(HERE, "CANDIDATES.md"), "w") as f:
        f.write("# Ranked homophone candidates (priors, NOT promotions)\n\n")
        for syl, c in cand.items():
            f.write(f"## {syl}-class (known cell {c['known_cell']}, phase {c['known_phase']})\n\n")
            f.write("| rank | group | cos-sim | n | phase | phase-match |\n|---|---|---|---|---|---|\n")
            for i, t in enumerate(c["top"], 1):
                f.write(f"| {i} | {t['group']} | {t['sim']} | {t['n']} | "
                        f"{t['phase']} | {'yes' if t['phase_match'] else 'no'} |\n")
            f.write("\n")
    with open(os.path.join(HERE, "DIGITS.md"), "w") as f:
        f.write("# Digit hunt\n\n")
        f.write(f"Low-n groups (n<5): {', '.join(sorted(low))}\n\n")
        f.write(f"Digit-digit adjacent pairs observed: {digit_meta['digit_digit_adjacent']} "
                f"vs null mean {digit_meta['null_mean']:.2f} / max {digit_meta['null_max']} "
                f"(200 permutations).\n\n")
        for g in sorted(low):
            d = digit[g]
            f.write(f"## {g} (n={d['n']}, phase {d['phase']})\n")
            f.write(f"- positions: {d['positions']}\n")
            f.write(f"- start-5%: {d['start5pct']}, end-5%: {d['end5pct']}\n")
            f.write(f"- distinct pre/suc: {d['distinct_pre']}/{d['distinct_suc']}; "
                    f"pre={d['pre']}, suc={d['suc']}\n")
            f.write(f"- contacts with top-20 core: {d['contact_top20']}; "
                    f"adjacent to other low-n: {d['adjacent_low']}\n\n")
    print("done. rows:", len(rows), "| strong:", sum(1 for r in rows if r["strong"]),
          "| flagged:", sum(1 for r in rows if r["flag"]))

if __name__ == "__main__":
    main()
