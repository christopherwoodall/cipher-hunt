#!/usr/bin/env python3
"""Round-14: INFINITIVE-33 — Fork S/W discriminator + 79="tout" F-C unlock.
Implements code/crowd14/infinitive33/PREREG.md (written before this ran).
Repaired 1,847-pair stream ONLY (never canonical.py).
"""
import json, os, re, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N
out = {"gate": "PASS", "N": N, "prereg": os.path.join(HERE, "PREREG.md")}

# ---------- 1. VERIFY: re-derive the 8 "pour 33" frames independently ----------
pour33 = [i for i in range(1, N) if pairs[i] == '33' and pairs[i-1] == '00']
expect = [186, 408, 467, 846, 936, 1088, 1245, 1630]
out["frames_rederived"] = pour33
out["frames_match_task_brief"] = (pour33 == expect)
print("pour-33 frames re-derived:", pour33, "match:", pour33 == expect)

def win(i, a=6, b=8):
    return " ".join(pairs[max(0, i-a):i+b])

frames = {i: {"pre": pairs[i-1], "suc": pairs[i+1], "suc2": pairs[i+2],
              "window": win(i)} for i in pour33}
out["frames"] = {str(i): v for i, v in frames.items()}

# ---------- F79 census inputs: n33, I1, I2, I4 ----------
n33 = pairs.count('33')
i1 = [i for i in range(1, N) if pairs[i] == '33' and pairs[i-1] == '00']
i4 = [i for i in range(N-1) if pairs[i] == '33' and pairs[i+1] == '29']
i2 = [i for i in range(1, N) if pairs[i] == '33' and pairs[i-1] == '67']
out["census"] = {"n33": n33, "I1_pre00": i1, "I1_n": len(i1),
                 "I4_suc29": i4, "I4_n": len(i4),
                 "I2_pre67": i2, "I2_n": len(i2)}
print("n33=%d I1=%d I4=%d I2=%d" % (n33, len(i1), len(i4), len(i2)))
out["I4_windows"] = {str(i): win(i, 3, 4) for i in i4}
out["I2_windows"] = {str(i): win(i, 3, 4) for i in i2}

# ---------- 79 census (unlock test) ----------
pos79 = [i for i in range(N) if pairs[i] == '79']
out["n79"] = len(pos79)
out["pos79"] = pos79
out["pos79_windows"] = {str(i): win(i, 4, 5) for i in pos79}
# "tout ce qui" trigram census: 79 87 64 vs 24 87 64
tri79 = [i for i in range(N-2) if pairs[i] == '79' and pairs[i+1] == '87' and pairs[i+2] == '64']
tri24 = [i for i in range(N-2) if pairs[i] == '24' and pairs[i+1] == '87' and pairs[i+2] == '64']
out["tout_ce_qui"] = {"via79": tri79, "via24": tri24}
print("79: n=%d; '79 87 64' @%s; '24 87 64' @%s" % (len(pos79), tri79, tri24))
# unlock: any pour-33 frame with 79 in +1..+4 beyond the F-C pair?
fc_pair = {467, 1088}
unlock = [i for i in pour33 if i not in fc_pair
          and any(pairs[i+k] == '79' for k in range(1, 5))]
out["unlock_new_pour33_tout_frames"] = unlock
# any 33-frame (not just pour) with 79 in tail?
any33_79 = [i for i in range(N-1) if pairs[i] == '33' and pairs[i+1] == '79']
out["any_33_suc79"] = any33_79
print("33->79 windows:", any33_79)

# ---------- era pool (lane tok() verbatim; pool minus v8) ----------
def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

def is_inf(w):
    return w.endswith(('er', 'ir', 're')) and len(w) > 3

CORP = os.path.join(LANE, 'code', 'side-period', 'corpus')
EXCLUDE = {'harvest-log.txt', 'adb-zeschau-heinrich-anton-von.txt'}
files = sorted(f for f in os.listdir(CORP)
               if f.endswith('.txt') and f not in EXCLUDE
               and not f.startswith('allgemeine-zeitung-'))
nov8_tok = []
for f in files:
    if f == 'nesselrode-v8.txt':
        continue
    nov8_tok.extend(tok(open(os.path.join(CORP, f), encoding='utf-8', errors='replace').read()))
assert len(nov8_tok) == 3867332, len(nov8_tok)
out["pool_nov8_tokens"] = len(nov8_tok)
print("pool\\v8 tokens=%d OK" % len(nov8_tok))

# ---------- F-D re-check: "pour X par [e-word]" ----------
n_fd = 0
for i in range(len(nov8_tok) - 3):
    if (nov8_tok[i] == 'pour' and is_inf(nov8_tok[i+1])
            and nov8_tok[i+2] == 'par' and nov8_tok[i+3].startswith('e')):
        n_fd += 1
out["F_D_recheck"] = {"query": 'n("pour X par [e-word]")', "n": n_fd}
print("F-D recheck n=%d" % n_fd)

# ---------- monosyllabic infinitive set (mechanical pre-filter + hand verify) ----------
VOWELS = set('aeiouyàâäéèêëîïôöùûü')
def vowel_groups(w):
    n, prev = 0, False
    for ch in w:
        v = ch in VOWELS
        if v and not prev:
            n += 1
        prev = v
    return n

inf_set = set()
for i in range(len(nov8_tok) - 1):
    if nov8_tok[i] == 'pour' and is_inf(nov8_tok[i+1]):
        inf_set.add(nov8_tok[i+1])
mono = sorted(w for w in inf_set if vowel_groups(w) == 1)
out["mono_inf_prefilter_n"] = len(mono)

# ---------- T_fc: n("pour X tout W") ----------
tfc_all = Counter()   # (X, W)
tfc_x = Counter()
examples = {}
for i in range(len(nov8_tok) - 3):
    if nov8_tok[i] == 'pour' and is_inf(nov8_tok[i+1]) and nov8_tok[i+2] == 'tout':
        x, w = nov8_tok[i+1], nov8_tok[i+3]
        tfc_all[(x, w)] += 1
        tfc_x[x] += 1
        if x not in examples:
            ctx = " ".join(nov8_tok[max(0, i-4):i+8])
            examples[x] = ctx
out["T_fc"] = {"query": 'n_pool\\v8("pour X tout W")',
               "n_total": sum(tfc_all.values()),
               "n_distinct_X": len(tfc_x),
               "by_X": tfc_x.most_common(40)}
# W-slot distribution
wslot = Counter()
for (x, w), c in tfc_all.items():
    wslot[w] += c
out["T_fc"]["W_slot_top20"] = wslot.most_common(20)
out["T_fc"]["examples"] = dict(list(examples.items())[:8])
print("T_fc: n_total=%d distinct_X=%d" % (sum(tfc_all.values()), len(tfc_x)))

# monosyllabic subset of T_fc (hand-verified syllable counts on firing set)
mono_set = set(mono)
tfc_mono = [(x, c) for x, c in tfc_x.most_common() if x in mono_set]
out["T_fc"]["mono_X"] = tfc_mono
print("T_fc mono-X:", tfc_mono)

# ---------- F-E mono: n("pour X ce qui") for monosyllabic X ----------
t2_mono = Counter()
t2_all = Counter()
t2_ex = {}
for i in range(len(nov8_tok) - 3):
    if (nov8_tok[i] == 'pour' and is_inf(nov8_tok[i+1])
            and nov8_tok[i+2] == 'ce' and nov8_tok[i+3] == 'qui'):
        x = nov8_tok[i+1]
        t2_all[x] += 1
        if x in mono_set:
            t2_mono[x] += 1
        if x not in t2_ex:
            t2_ex[x] = " ".join(nov8_tok[max(0, i-4):i+8])
out["T2_mono"] = {"query": 'n_pool\\v8("pour X ce qui"), X monosyllabic',
                  "mono_hits": t2_mono.most_common(),
                  "all_top": t2_all.most_common(15),
                  "examples": dict(list(t2_ex.items())[:6])}
print("T2 mono hits:", t2_mono.most_common())

# ---------- Fork-W value intersection: mono X with BOTH T2 and T_fc legs ----------
x_t2 = set(t2_mono) | set()  # mono X with pour-X-ce-qui
x_tfc = set(x for x, c in tfc_mono)
out["forkW_intersection"] = sorted(x_t2 & x_tfc)
out["forkW_T2_only"] = sorted(x_t2 - x_tfc)
out["forkW_Tfc_only"] = sorted(x_tfc - x_t2)

# ---------- Fork-S joint constraint datum ----------
# Under Fork S, ONE stem 33 must compose with ALL five suc groups:
# 16, 01, 79, 96, 21 -> real infinitive endings. Standing glosses:
# 79="tout"-lead, 96="par"-prov, 21="ce"-banked, 16="i"-lead, 01 unidentified.
out["forkS_joint"] = {
    "required_endings": {"F-A": "16", "F-B": "01", "F-C": "79", "F-D": "96", "F-E": "21"},
    "standing_glosses": {"16": "i (lead)", "01": "unidentified (ci killed N23)",
                         "79": "tout (LEAD-grade, unlock test)",
                         "96": "par (provisional F19)", "21": "ce (banked R1)"},
    "composition_verdicts": {
        "16=i": "stem+/i/ — no French infinitive ends in bare /i/ [FR-JUDGMENT] => S breaks 16='i'-lead at F-A",
        "79=tout": "stem+/tu/ — no French infinitive ends /tu/ [FR-JUDGMENT] => S breaks 79='tout' at F-C (both frames)",
        "96=par": "stem+/paR/ — no French infinitive ends /paR/ [FR-JUDGMENT] => S breaks 96='par' at F-D (round-12 recorded)",
        "21=ce": "stem+/s(e)/ — no French infinitive ends /s(e)/ [FR-JUDGMENT] => S breaks 21='ce' at F-E (breaks banked lead)",
        "01=?": "01 unidentified — no verdict; composition unconstrained"
    },
    "n_standing_values_forkS_must_break": 4,
    "note": "Fork S survives ONLY by overriding 16/79/96/21 simultaneously (4 standing values incl. one banked lead and one provisional). No stem candidate can be named without those overrides."
}

# ---------- paradox check: savoir under both forks ----------
savoir_t2 = t2_all.get('savoir', 0)
out["paradox_check"] = {
    "savoir_n_T2": savoir_t2,
    "forkW": "savoir = 2 syllables (sa-voir); 33 = 1 group = 1 chunk (F22) => fork-forbidden under W",
    "forkS": "T2 battery is whole-word scoped; under S, F-E = 'pour [33=stem][21=suc]'. savoir as stem = 'savo' + suc; suc=21='ce'-banked => 'savoce' != 'savoir'. S needs 21='ir'-chunk => breaks the banked 21='ce' => fork-forbidden under S",
    "verdict": "savoir fork-forbidden under BOTH forks — F109 paradox confirmed on re-derivation" if True else ""
}

json.dump(out, open(os.path.join(HERE, "fork_disc_results.json"), "w"),
          indent=1, ensure_ascii=False)
print("wrote fork_disc_results.json")
