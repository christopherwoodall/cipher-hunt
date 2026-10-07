#!/usr/bin/env python3
"""48 successor-word anchoring battery (round-11, anchorer48, work order 2).

Pre-registered in PREREG.md BEFORE any fresh era-count computation.
Repaired 1,847-pair parse via code/crowd7/keystruct/aliasing.load_stream().
Era: Nesselrode v8 strict (code/side-period/corpus/nesselrode-v8.txt),
elision-split tokenizer (code/crowd9/frenchman/corpus9.tokenize_elision).
All @-citations 0-based pair indices.

Paths:
  A: six "on 48" windows -> successor census + single-syllable coherence
     per S in the 10 S-syl shortlist (datum, F75).
  B: four 82->48 frames under the mandated "m'"-elision premise ->
     vowel-initial S coherence.
  D: 48="de"-CONDITIONAL narrow path (pronoun+infinitive) -> RUN or FENCE.
"""
import json, sys
from collections import Counter
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(LANE / "code" / "crowd7" / "keystruct"))
sys.path.insert(0, str(LANE / "code" / "crowd9" / "frenchman"))
from aliasing import load_stream
import corpus9

OUT = Path(__file__).parent
res = {"prereg": "PREREG.md (written before any fresh era-count computation)"}

# ---------------- stream: re-derive standing windows ----------------
pairs = load_stream()
N = len(pairs)
assert N == 1847, N
w48 = [i for i, x in enumerate(pairs) if x == 48]
assert len(w48) == 38, len(w48)

on48 = [(i, pairs[i + 1]) for i in w48 if pairs[i - 1] == 62]
m48 = [(i, pairs[i + 1]) for i in w48 if pairs[i - 1] == 82]
pro48 = [(i, pairs[i - 1], pairs[i + 1], pairs[i + 2]) for i in w48
         if pairs[i + 1] in (77, 11)]
pas48 = [i for i in w48 if pairs[i + 1] == 52]
assert [i for i, _ in on48] == [361, 426, 1316, 1350, 1465, 1570]
assert [i for i, _ in m48] == [126, 377, 398, 1229]
assert [i for i, _, _, _ in pro48] == [126, 1076, 1350]
assert pas48 == [283, 1737]
res["windows_rederived"] = {
    "on48": [{"pos": i, "suc": s} for i, s in on48],
    "m48": [{"pos": i, "suc": s} for i, s in m48],
    "pro48": [{"pos": i, "pre": p, "suc": s, "suc2": s2}
              for i, p, s, s2 in pro48],
    "pas48": pas48,
}
res["N"] = N
res["n48"] = len(w48)

# ---------------- corpus ----------------
corp = (LANE / "code" / "side-period" / "corpus" / "nesselrode-v8.txt").read_text(
    encoding="utf-8", errors="replace")
toks = corpus9.tokenize_elision(corp)
nt = len(toks)
assert nt == 92594, nt
res["corpus"] = {"file": "nesselrode-v8.txt", "n_tokens": nt,
                 "tokenizer": "corpus9.tokenize_elision"}

# ---------------- by-ear syllabifier v1.2 (verbatim from round-10 battery) ---
VOWELS = set("aàâäeéèêëiîïoôöuùûüy")

def byear_syllables(word):
    if "'" in word and len(word) <= 3:
        return [word]
    vs = [i for i, ch in enumerate(word) if ch in VOWELS]
    if not vs:
        return [word]
    nuclei = []
    for i in vs:
        if nuclei and i == nuclei[-1][-1] + 1:
            nuclei[-1].append(i)
        else:
            nuclei.append([i])
    nuc = [(n_[0], n_[-1]) for n_ in nuclei]
    cuts = []
    for (a0, a1), (b0, b1) in zip(nuc[:-1], nuc[1:]):
        c = b0 - a1 - 1
        cuts.append(a1 + 2 if c >= 1 else a1 + 1)
    parts, start = [], 0
    for cut in cuts:
        parts.append(word[start:cut])
        start = cut
    parts.append(word[start:])
    return [p for p in parts if p]

def first_syl(w):
    s = byear_syllables(w)
    return s[0] if s else w

def second_syl(w):
    s = byear_syllables(w)
    return s[1] if len(s) > 1 else None

def last_syl(w):
    s = byear_syllables(w)
    return s[-1] if s else w

SHORTLIST = ["à", "et", "de", "a", "es", "il", "les", "te", "un", "com"]
VOWEL_INIT = {"à", "a", "es", "et", "il", "un"}

# trigram / bigram indexes
tri = Counter(zip(toks[:-2], toks[1:-1], toks[2:]))
bi = Counter(zip(toks[:-1], toks[1:]))

def trig(a, b, c):
    return tri.get((a, b, c), 0)

# ================= PATH A =================
pathA = {"A0_census": res["windows_rederived"]["on48"]}
A1, A2 = {}, {}
for S in SHORTLIST:
    # A1: ("on", W, "le") with first_syl(W)==S  -- @1350-anchored
    hits1 = [(toks[i + 1]) for i in range(nt - 2)
             if toks[i] == "on" and toks[i + 2] == "le"
             and first_syl(toks[i + 1]) == S]
    # A2: ("on", W) with first_syl(W)==S  (+ proper-syllable decomposition:
    # W strictly longer than S, i.e. S functions as a syllable not the whole word)
    hits2 = [toks[i + 1] for i in range(nt - 1)
             if toks[i] == "on" and first_syl(toks[i + 1]) == S]
    proper2 = [w for w in hits2 if len(w) > len(S)]
    c1, c2, c2p = Counter(hits1), Counter(hits2), Counter(proper2)
    A1[S] = {"n": len(hits1), "top_W": c1.most_common(8),
             "verdict": "PASS" if len(hits1) >= 1 else "ADVERSE(fenced)"}
    A2[S] = {"n": len(hits2), "n_proper": len(proper2),
             "top_W": c2.most_common(8), "top_proper_W": c2p.most_common(8),
             "verdict": "PASS" if len(hits2) >= 1 else "ADVERSE(fenced)",
             "note": ("word-driven" if (len(hits2) >= 1 and len(proper2) == 0)
                      else "proper-syllable support" if len(proper2) >= 1 else "")}
pathA["A1_on_S_le"] = A1
pathA["A2_on_S"] = A2
pathA["A3_single_S_verdict"] = {
    S: ("COHERES" if (A1[S]["verdict"] == "PASS" and A2[S]["verdict"] == "PASS")
        else "FENCED")
    for S in SHORTLIST}
coh = [S for S in SHORTLIST if pathA["A3_single_S_verdict"][S] == "COHERES"]
pathA["A3_reading"] = ("COHERENT — %d S cohere: %s" % (len(coh), coh)) if coh \
    else "FENCED — no S coheres at the on-frames"
res["pathA"] = pathA

# ================= PATH B =================
pathB = {"B0_census": res["windows_rederived"]["m48"],
         "premise": "82=\"m'\" (elided me) => 48 vowel-initial (work-order-mandated, conditional)"}
B1, B2 = {}, {}
for S in sorted(VOWEL_INIT):
    # B1: ("m'", W, "la") with first_syl(W)==S  -- @126-anchored
    hits1 = [toks[i + 1] for i in range(nt - 2)
             if toks[i] == "m'" and toks[i + 2] == "la"
             and first_syl(toks[i + 1]) == S]
    # B2: ("m'",W1,W2) first_syl(W1)==S, first_syl(W2)=="er"  OR
    #     ("m'",W) first_syl(W)==S, second_syl(W)=="er"  -- @1229-anchored
    hits2a = [(toks[i + 1], toks[i + 2]) for i in range(nt - 2)
              if toks[i] == "m'" and first_syl(toks[i + 1]) == S
              and first_syl(toks[i + 2]) == "er"]
    hits2b = [toks[i + 1] for i in range(nt - 1)
              if toks[i] == "m'" and first_syl(toks[i + 1]) == S
              and second_syl(toks[i + 1]) == "er"]
    c1 = Counter(hits1)
    B1[S] = {"n": len(hits1), "top_W": c1.most_common(8),
             "verdict": "PASS" if len(hits1) >= 1 else "ADVERSE(fenced)"}
    B2[S] = {"n_parse_i": len(hits2a), "n_parse_ii": len(hits2b),
             "ex_parse_i": Counter(hits2a).most_common(5),
             "ex_parse_ii": Counter(hits2b).most_common(5),
             "verdict": ("PASS" if (len(hits2a) >= 1 or len(hits2b) >= 1)
                         else "ADVERSE(fenced)")}
pathB["B1_m_S_la"] = B1
pathB["B2_m_S_er"] = B2
pathB["B3_unidentified_sucs"] = {"377": "suc 0 (unidentified) — recorded, no bar",
                                 "398": "suc 6 (unidentified) — recorded, no bar"}
# premise-support diagnostic (interpretation aid, not a leg): ("m'", W) bigram
# productivity per vowel-initial S — is "m'"+S-word even attested?
B0 = {}
for S in sorted(VOWEL_INIT):
    hits0 = [toks[i + 1] for i in range(nt - 1)
             if toks[i] == "m'" and first_syl(toks[i + 1]) == S]
    B0[S] = {"n": len(hits0), "top_W": Counter(hits0).most_common(6)}
pathB["B0_m_S_bigram"] = B0
pathB["B4_single_S_verdict"] = {
    S: ("COHERES" if (B1[S]["verdict"] == "PASS" and B2[S]["verdict"] == "PASS")
        else "FENCED")
    for S in sorted(VOWEL_INIT)}
cohb = [S for S in sorted(VOWEL_INIT)
        if pathB["B4_single_S_verdict"][S] == "COHERES"]
pathB["B4_premise"] = ("premise LIVE — %d vowel-initial S cohere: %s"
                       % (len(cohb), cohb)) if cohb \
    else "premise FENCED for 48 — no vowel-initial S coheres at the m'-frames"
pathB["consonant_init_note"] = ("de/les/te/com INCOHERENT with m'-premise "
                                "(recorded; not killed as 48-values)")
res["pathB"] = pathB

# ================= PATH D =================
pathD = {"D0_footprint": res["windows_rederived"]["pro48"]}

# D1: "de le"+X and "de la"+X inventories — VERIFIED classification.
# Instrument repair (disclosed): the v1 heuristic's NOUN_STOP wrongly excluded
# "faire" (6x) from INF, flipping the bar. Per PREREG the ambiguous remainder
# is hand-verified with full per-X disclosure; hand-verdicts [FR-JUDGMENT].
# "de le"+X: all 19 distinct X hand-verified infinitives (frame forces verb).
DE_LE_X_INF = {"faire", "voir", "prévoir", "recevoir", "contrecarrer", "mettre",
               "laisser", "renouveler", "défendre", "rencontrer", "dénoncer",
               "proposer", "rappeler", "remettre", "gêner", "composer",
               "rehausser", "revoir", "croire"}  # [FR-JUDGMENT] each
# "de la"+X: hand-split INF (pronoun "la"+infinitive) vs NOUN/OTHER.
# NOUN/OTHER (article "la" or adjective): guerre, chambre, manière, dernière,
#   nature, lettre, frontière, première, rupture, circulaire, chaire,
#   tournure, terre, victoire, gloire, mnnière(=manière, OCR), nourriture,
#   nôtre, violoire(=victoire, OCR). [FR-JUDGMENT] each.
DE_LA_X_INF = {"voir", "soigner", "reprendre", "brûler", "rattacher",
               "défendre", "réaliser", "tirer", "faire", "refuser",
               "soutenir", "déclarer"}  # [FR-JUDGMENT] each
de_le_X = Counter(toks[i + 2] for i in range(nt - 2)
                  if toks[i] == "de" and toks[i + 1] == "le")
de_la_X = Counter(toks[i + 2] for i in range(nt - 2)
                  if toks[i] == "de" and toks[i + 1] == "la")
assert set(de_le_X) == DE_LE_X_INF, set(de_le_X) ^ DE_LE_X_INF
n_dl = sum(de_le_X.values())
n_dla_inf = sum(c for x, c in de_la_X.items() if x in DE_LA_X_INF)
# "de la"+X not in INF set and not hand-listed as noun: disclose for audit
de_la_other = sorted([(x, c) for x, c in de_la_X.items()
                      if x not in DE_LA_X_INF],
                     key=lambda kv: -kv[1])[:40]
pathD["D1"] = {
    "n_de_le": n_dl,
    "de_le_X": sorted(de_le_X.items(), key=lambda kv: -kv[1]),
    "de_le_all_INF_verified": True,
    "frac_de_le_INF": 1.0,
    "n_de_la": sum(de_la_X.values()),
    "de_la_INF_verified": sorted(
        [(x, de_la_X[x]) for x in DE_LA_X_INF], key=lambda kv: -kv[1]),
    "n_de_la_INF": n_dla_inf,
    "de_la_nonINF_top40": de_la_other,
    "classification": "hand-verified per-X [FR-JUDGMENT]; full lists disclosed",
}
licensed = (pathD["D1"]["frac_de_le_INF"] >= 0.90
            and pathD["D1"]["n_de_la_INF"] >= 1)
pathD["D1"]["licensed_bar"] = (
    "LICENSED" if licensed else "NOT-LICENSED (refute narrow path)")

# D2a: "on de" hits with context (pre-registered classification rule)
on_de_ctx = []
for i in range(nt - 1):
    if toks[i] == "on" and toks[i + 1] == "de":
        on_de_ctx.append(" | ".join(toks[max(0, i - 8):i + 6]))
pathD["D2a_on_de"] = {
    "n": len(on_de_ctx),
    "contexts": on_de_ctx,
    "classification": {
        "@6759": ("'notre excellent bai on de werther' — uninterpretable "
                  "OCR-adjacent/name context [FR-JUDGMENT]; NOT a clean "
                  "standalone-'on'+'de'"),
        "@48138": "'dit on de devenir' = 'dit-on' verb-inversion + 'de' "
                   "[FR-JUDGMENT]; NOT standalone subject 'on'",
    },
    "n_genuine_standalone_on_de": 0,
    "note": ("@1350's 'on de' needs >=1 genuine standalone-'on'+'de': 0/2. "
             "@1350 ALSO pre-excluded: R-c owns @1351-1356 (N51, settled); "
             "78=R-c-nominal _|_ 78=infinitive."),
    "at1350": "OUT of narrow path (R-c exclusion pre-registered; 'on de' unlicensed 0/2)",
}

# D2b: @1076 era context — L1 distribution of "de le"+INF (what licenses it?)
de_le_L1 = Counter(toks[i - 1] for i in range(1, nt - 2)
                   if toks[i] == "de" and toks[i + 1] == "le")
pathD["D2b_at1076"] = {
    "frame": "12-48-77-78 (pre=12 unidentified, suc2=78 unidentified)",
    "de_le_L1_top": de_le_L1.most_common(12),
    "de_le_L1_note": ("context for ML-2: the era licensors of 'de le [inf]' — "
                      "pre=12 must be verb/verb-final of this class"),
    "status": "IN-PENDING",
    "missing": ["ML-1: identify @1077 (grp 78 here) as infinitive(-initial)",
                "ML-2: identify pre=12 as verb/verb-final licensing '[V] de le [inf]'"],
}

# D2c: @126 — "[m-final word] de la" + INF era check (verified INF set)
m_de_la_inf = Counter()
m_de_la_all = 0
m_de_la_ex = []
for i in range(nt - 2):
    if toks[i + 1] == "de" and toks[i + 2] == "la" and toks[i].endswith("m") \
            and len(toks[i]) > 1 and "'" not in toks[i]:
        m_de_la_all += 1
        x = toks[i + 3] if i + 3 < nt else None
        if x and x in DE_LA_X_INF:
            m_de_la_inf[toks[i]] += 1
        if len(m_de_la_ex) < 10:
            m_de_la_ex.append(" ".join(toks[i:i + 4]))
pathD["D2c_at126"] = {
    "frame": "82-48-11-2 (82='m' GT, 48->11=la GT, @127=grp 2 unidentified)",
    "n_mword_de_la": m_de_la_all,
    "mword_de_la_examples": m_de_la_ex,
    "mword_de_la_plus_INF": dict(m_de_la_inf),
    "n_mword_de_la_plus_INF": sum(m_de_la_inf.values()),
    "status": ("IN-PENDING (ML-3: identify @127=grp 2)"
               if sum(m_de_la_inf.values()) >= 1 else "OUT (left context unlicensed)"),
}

# D3: Gate-5 sweep (recorded)
pathD["D3_gate5"] = {
    "missing_ne_veto": "does not fire — 48='de' is not a verb/verb-stem",
    "clitic_order_veto": ("stays BANKED — conditional on 48=transitive-verb; "
                          "48='de' is not a transitive verb; no trip"),
    "V1_48pas": ("conditional does not claim @283/@1737 — escape via "
                 "conditioning (recorded)"),
}

# D4: promotion audit
licensed = pathD["D1"]["licensed_bar"] == "LICENSED"
fits = [k for k in ("D2b_at1076", "D2c_at126")
        if pathD[k]["status"].startswith("IN-PENDING")]
if not licensed:
    pathD["D4"] = "REFUTED — D1 construction not licensed; kill the conditional"
elif fits:
    pathD["D4"] = ("FENCED — construction licensed (D1) but no claiming window "
                   "has >=2 independent checks; missing legs: " +
                   "; ".join(sum([pathD[k]["missing"] if "missing" in pathD[k]
                                         else ["ML-3: identify @127=grp 2"]
                                         for k in fits], [])))
else:
    pathD["D4"] = "FENCED — construction licensed but no claiming window"
res["pathD"] = pathD

# out-of-scope note: 48->47 ("de ce")
ce48 = [(i, pairs[i + 2] if i + 2 < N else None) for i in w48 if pairs[i + 1] == 47]
res["note_de_ce"] = {
    "windows_48_47": ce48,
    "note": ("'de ce' x2 (@863, @1658) is a DIFFERENT construction "
             "('de ce que'/'de ce + noun'), not pronoun+infinitive — "
             "out of scope for the narrow path; recorded only."),
}

with open(OUT / "anchor48_results.json", "w") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
print("wrote anchor48_results.json")
print("PATH A3:", pathA["A3_reading"])
print("PATH B4:", pathB["B4_premise"])
print("PATH D1:", pathD["D1"]["licensed_bar"],
      "frac_de_le_INF=%.3f" % (pathD["D1"]["frac_de_le_INF"] or -1),
      "n_de_la_INF=", pathD["D1"]["n_de_la_INF"])
print("PATH D2c:", pathD["D2c_at126"]["status"],
      "n=", pathD["D2c_at126"]["n_mword_de_la_plus_INF"])
print("PATH D4:", pathD["D4"][:120])
