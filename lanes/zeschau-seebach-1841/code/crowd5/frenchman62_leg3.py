#!/usr/bin/env python3
"""FRENCHMAN round 5 — work order: INSTRUMENT-INDEPENDENT third leg for 62="on".

Status: 62="on" STRONG LEAD (N28). Legs 1 (ear lock) & 3 (ear subject
triangulation) share the ear instrument; red team denied promotion.
This script runs NON-ear checks against the REPAIRED 1,847-pair parse
(code/side-keyhunt/repaired_offsets.json), with era legs in WORD SPACE only
(F30: no era-syllable-conditionals on fragments; 40="e" excluded everywhere).

Checks:
  A. Era word-space unigram subject battery: f(62) vs era unigram rates of
     subject-position words + /o~/ rivals; word-space grammatical kills.
  B. "qu'on"-null corroboration: era P(on|que) predicts ~8-9 "qu'on"; the
     by-ear model predicted 46->62 = 0 (N28). Binomial test of 0/n(46).
  C. Mappable-cell follower/predecessor profile: anchor-mappable cells
     (94=[ne], 11=la GT, 46=que GT, 21=[me] LEAD) vs era P(w|on); grammatical
     negative cells (11->62, 96=[par]->62). Chi-square + per-cell Poisson.
  D. (corroboration, shares data with leg 3) 62->21 rate vs era P(me|on).
No invented ciphertext. Writes to code/crowd5/ only.
"""
import json, math, os, re, collections

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
DATA = os.path.join(LANE, "data")

# ---------- repaired canonical parse ----------
def load_repaired():
    rows = []
    for line in open(os.path.join(DATA, "upstream-ct_R5005.txt")):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r"\D", "", digits)))
    off = json.load(open(os.path.join(LANE, "code/side-keyhunt/repaired_offsets.json")))
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [(digits[i:i + 2], lid) for i in range(o, len(digits) - 1, 2)]
    return pairs

pairs = load_repaired()
seq = [g for g, _ in pairs]
assert len(pairs) == 1847, len(pairs)
assert seq[754:760] == ["11", "70", "82", "34", "29", "40"], seq[754:760]
assert seq[1034:1040] == ["11", "70", "82", "34", "29", "40"], seq[1034:1040]
n = len(pairs)

hits62 = [i for i, g in enumerate(seq) if g == "62"]
n62 = len(hits62)
pre = collections.Counter(seq[i - 1] for i in hits62 if i > 0)
fol = collections.Counter(seq[i + 1] for i in hits62 if i + 1 < n)

def bigram(a, b):
    return sum(1 for i in range(n - 1) if seq[i] == a and seq[i + 1] == b)

c_62_94 = bigram("62", "94")
c_46_62 = bigram("46", "62")
c_11_62 = bigram("11", "62")
c_96_62 = bigram("96", "62")
c_62_21 = bigram("62", "21")
c_62_11 = bigram("62", "11")
c_62_46 = bigram("62", "46")
n46 = seq.count("46")
n46_nonfinal = sum(1 for i in range(n - 1) if seq[i] == "46")

# ---------- era word-space model (Tocqueville t1+t2) ----------
def words(path):
    t = open(path, encoding="utf-8", errors="replace").read().lower()
    t = re.sub(r"[’']", "'", t)
    t = re.sub(r"\b([a-zàâäéèêëîïôöùûüç]+)'([a-zàâäéèêëîïôöùûüç]+)", r"\1' \2", t)
    return re.findall(r"[a-zàâäéèêëîïôöùûüç]+(?:'[a-zàâäéèêëîïôöùûüç]+)?", t)

toks = words(os.path.join(DATA, "gutenberg-30513-tocqueville-t1.txt")) + \
       words(os.path.join(DATA, "gutenberg-30514-tocqueville-t2.txt"))
N = len(toks)
uni = collections.Counter(toks)
n_on = uni["on"]
n_que = uni["que"] + uni["qu"]
n_on_after_que = sum(1 for a, b in zip(toks, toks[1:]) if a in ("que", "qu") and b == "on")
pred_on = collections.Counter(a for a, b in zip(toks, toks[1:]) if b == "on")
fol_on = collections.Counter(b for a, b in zip(toks, toks[1:]) if a == "on")
n_ne_after_on = sum(1 for a, b in zip(toks, toks[1:]) if a == "on" and b in ("ne", "n"))

# era negative cells: "la on", "par on" bigrams (word space)
n_la_on = sum(1 for a, b in zip(toks, toks[1:]) if a == "la" and b == "on")
n_par_on = sum(1 for a, b in zip(toks, toks[1:]) if a == "par" and b == "on")

# (Check E "on vs il" differential computed after the era scalars below)

P_on_word = n_on / N
P_62 = n62 / n
P_ne_given_on = n_ne_after_on / n_on
P_on_given_que = n_on_after_que / n_que
p_pred_qu = (pred_on["qu"] + pred_on["que"]) / n_on

# ---------- Check A: subject battery ----------
SUBJECTS = ["on", "je", "il", "ils", "nous", "vous", "elle", "elles", "tu",
            "cela", "ceci", "qui"]
RIVALS_PHON = {"son": "possessive determiner - cannot be bare subject",
               "mon": "possessive determiner - cannot be bare subject",
               "nom": "noun - cannot be bare subject",
               "ont": "verb (3pl avoir) - cannot be subject",
               "ça": "register-killed: 47:1 cela:ca in 1835-50 print (linguist)"}
battery = []
for w in SUBJECTS:
    pw = uni[w] / N
    battery.append({"word": w, "era_n": uni[w], "era_P": round(pw, 6),
                    "ratio_cipher_over_era": round(P_62 / pw, 3) if pw else None})
for w, kill in RIVALS_PHON.items():
    pw = uni[w] / N
    battery.append({"word": w, "era_n": uni[w], "era_P": round(pw, 6),
                    "ratio_cipher_over_era": round(P_62 / pw, 3) if pw else None,
                    "grammatical_kill": kill})

# ---------- Check B: qu'on-null binomial ----------
# H0 (written-era): each 46 (=que, GT) has P(on|que) chance of ->62
p_quon = P_on_given_que
binom_p0 = (1 - p_quon) ** n46_nonfinal  # P(0/29 under H0)
expected_quon = n46_nonfinal * p_quon

# ---------- Check E (differential): "on" vs "il", the surviving unigram rival ----------
# era conditionals for "il" as subject
n_il = uni["il"]
n_ne_after_il = sum(1 for a, b in zip(toks, toks[1:]) if a == "il" and b in ("ne", "n"))
n_il_after_que = sum(1 for a, b in zip(toks, toks[1:]) if a in ("que", "qu") and b == "il")
P_ne_given_il = n_ne_after_il / n_il
P_il_given_que = n_il_after_que / n_que
E_il_after_que = n46_nonfinal * P_il_given_que
binom_p0_il = (1 - P_il_given_que) ** n46_nonfinal  # P(0/29) if 62="il" (no ear-merger)
# "qu'il" is written que+il in era orthography, so no merger excuse for "il"
checkE = {
    "era_n_il": n_il,
    "era_P_ne_given_il": round(P_ne_given_il, 4),
    "era_P_ne_given_on": round(P_ne_given_on, 4),
    "obs_P_94_given_62": round(c_62_94 / n62, 4),
    "ratio_vs_on": round(c_62_94 / n62 / P_ne_given_on, 3),
    "ratio_vs_il": round(c_62_94 / n62 / P_ne_given_il, 3),
    "era_P_il_given_que": round(P_il_given_que, 4),
    "E_46to62_if_il": round(E_il_after_que, 2),
    "E_46to62_if_on_written": round(expected_quon, 2),
    "binom_p_zero_if_il": binom_p0_il,
    "note": "qu'il is written que+il (no by-ear merger); qu'on=/kO~/ merges to one group",
}

# ---------- Check C: mappable-cell profile ----------
# follower cells: 94=[ne] prov-strong, 11=la GT, 46=que GT, 21=[me] LEAD
fol_cells = [
    ("ne", "94", c_62_94, (fol_on["ne"] + fol_on["n"]) / n_on, "provisional-strong"),
    ("me", "21", c_62_21, fol_on["me"] / n_on, "LEAD"),
    ("la", "11", c_62_11, fol_on["la"] / n_on, "ground-truth"),
    ("que", "46", c_62_46, (fol_on["que"] + fol_on["qu"]) / n_on, "ground-truth"),
]
p_other = 1 - sum(c[3] for c in fol_cells)
obs_other = n62 - sum(c[2] for c in fol_cells)
chi2 = 0.0
cells_out = []
for word, grp, obs, pexp, status in fol_cells + [("other", "-", obs_other, p_other, "catch-all")]:
    exp = round(n62 * pexp, 3)
    contrib = (obs - exp) ** 2 / exp if exp > 0 else float("inf")
    chi2 += contrib
    # Poisson two-sided-ish: P(X>=obs) if obs>exp else P(X<=obs)
    lam = exp
    if obs >= exp:
        tail = 1 - sum(math.exp(-lam) * lam ** k / math.factorial(k) for k in range(obs))
    else:
        tail = sum(math.exp(-lam) * lam ** k / math.factorial(k) for k in range(obs + 1))
    cells_out.append({"cell": word, "group": grp, "obs": obs, "exp": exp,
                      "era_P": round(pexp, 4), "chi2_contrib": round(contrib, 2),
                      "poisson_tail": round(tail, 4), "anchor_status": status})
df = len(cells_out) - 1
chi2_p = 1 - __import__("statistics").NormalDist().cdf(0)  # placeholder replaced below
# chi-square survival via incomplete gamma
def chi2_sf(x, k):
    # regularized upper gamma Q(k/2, x/2)
    s = k / 2.0
    z = x / 2.0
    # series for lower gamma then complement
    term = 1.0 / s
    total = term
    kk = 1
    while abs(term) > 1e-12 and kk < 1000:
        term *= z / (s + kk)
        total += term
        kk += 1
    lower = (z ** s) * math.exp(-z) * total
    return max(0.0, min(1.0, 1 - lower / math.gamma(s)))
chi2_p = chi2_sf(chi2, df)

# negative grammatical cells (word-space era rate 0)
neg_cells = [
    ("la->on", "11->62", c_11_62, n_la_on, n62),
    ("par->on", "96->62", c_96_62, n_par_on, n62),
]

# ---------- Check D: 62->21 vs era P(me|on) (shares data with leg 3; corroboration) ----------
P_me_given_on = fol_on["me"] / n_on
P_21_given_62 = c_62_21 / n62

out = {
    "parse": {"pairs": n, "f62": n62, "P_62": round(P_62, 6),
              "positions_62": hits62,
              "predecessors": dict(pre), "n_distinct_pre": len(pre),
              "followers": dict(fol), "n_distinct_fol": len(fol)},
    "key_bigrams": {"62->94": c_62_94, "P_94_given_62": round(c_62_94 / n62, 4),
                    "46->62": c_46_62, "n46_nonfinal": n46_nonfinal,
                    "11->62": c_11_62, "96->62": c_96_62,
                    "62->21": c_62_21, "62->11": c_62_11, "62->46": c_62_46},
    "era": {"words": N, "n_on": n_on, "P_on_word": round(P_on_word, 6),
            "n_que": n_que, "P_on_given_que": round(P_on_given_que, 4),
            "P_ne_given_on": round(P_ne_given_on, 4),
            "n_ne_after_on": n_ne_after_on,
            "P_me_given_on": round(P_me_given_on, 4),
            "n_la_on": n_la_on, "n_par_on": n_par_on,
            "P_pred_qu_given_on": round(p_pred_qu, 4),
            "n_pred_qu": pred_on["qu"] + pred_on["que"]},
    "checkA_subject_battery": battery,
    "checkB_quon_null": {"expected_under_written_era": round(expected_quon, 2),
                         "observed": c_46_62, "trials": n46_nonfinal,
                         "p_pred_qu_given_on": round(p_pred_qu, 4),
                         "binomial_p_zero": binom_p0},
    "checkC_profile": {"cells": cells_out, "chi2": round(chi2, 2), "df": df,
                       "chi2_p": chi2_p,
                       "negative_cells": [{"label": l, "cipher": f"{g}: {o}",
                                           "era_n": e, "note": "era word-space count 0"}
                                          for l, g, o, e, _ in neg_cells]},
    "checkD_on_me": {"P_21_given_62": round(P_21_given_62, 4),
                     "era_P_me_given_on": round(P_me_given_on, 4),
                     "ratio": round(P_21_given_62 / P_me_given_on, 3)
                     if P_me_given_on else None},
    "checkE_on_vs_il": checkE,
}
p = os.path.join(LANE, "code/crowd5/frenchman62_leg3_results.json")
json.dump(out, open(p, "w"), indent=1, ensure_ascii=False)
print("wrote", p)

print(f"\n=== repaired parse: n={n}, f(62)={n62}, P(62)={P_62:.4%}")
print(f"62->94 x{c_62_94}  P={c_62_94/n62:.4f}  era P(ne|on)={P_ne_given_on:.4f}  ratio={c_62_94/n62/P_ne_given_on:.2f}x")
print(f"46->62 x{c_46_62}/{n46_nonfinal}  era P(on|que)={P_on_given_que:.4f}  E={expected_quon:.1f}  binom p={binom_p0:.2e}")
print(f"era P(on) word-space={P_on_word:.4%}  ratio cipher/era={P_62/P_on_word:.2f}x")
print(f"era P(que)={(n_que/N):.4%}  cipher P(46)={n46/n:.4%}  ratio={n46/n/(nque:=n_que/N):.2f}x")
print("\n--- Check A battery (ratio = P(62)/eraP(word)) ---")
for b in battery:
    tag = " [GRAM-KILLED: " + b["grammatical_kill"] + "]" if "grammatical_kill" in b else ""
    print(f"  {b['word']:>6}: era n={b['era_n']:>6} P={b['era_P']:.4%} ratio={b['ratio_cipher_over_era']}x{tag}")
print("\n--- Check C cells ---")
for c in cells_out:
    print(f"  {c['cell']:>5} ({c['group']} {c['anchor_status']}): obs={c['obs']} exp={c['exp']} "
          f"eraP={c['era_P']} chi2c={c['chi2_contrib']} poisson_tail={c['poisson_tail']}")
print(f"  chi2={chi2:.2f} df={df} p={chi2_p:.4f}")
print(f"--- Check D: P(21|62)={P_21_given_62:.4f} vs era P(me|on)={P_me_given_on:.4f} ratio={out['checkD_on_me']['ratio']}x")
print("--- Check E: on vs il differential ---")
print(f"  obs P(94|62)={checkE['obs_P_94_given_62']} era P(ne|on)={checkE['era_P_ne_given_on']} "
      f"({checkE['ratio_vs_on']}x) era P(ne|il)={checkE['era_P_ne_given_il']} ({checkE['ratio_vs_il']}x)")
print(f"  46->62: E_if_on_written={checkE['E_46to62_if_on_written']} (p0={binom_p0:.3f}); "
      f"E_if_il={checkE['E_46to62_if_il']} p0_if_il={checkE['binom_p_zero_if_il']:.2e}")
print("\n--- 62 windows (repaired indices) ---")
GT = {"11": "la", "70": "pre", "82": "m", "34": "i", "29": "er", "40": "e", "46": "que"}
PROV = {"87": "[ce]", "64": "[qui]", "96": "[par]", "94": "[ne]", "21": "[me]"}
for i in hits62:
    lo, hi = max(0, i - 3), min(n, i + 4)
    seg = " ".join((">>" + seq[j] + "<<") if j == i else GT.get(seq[j], PROV.get(seq[j], seq[j]))
                   for j in range(lo, hi))
    print(f"@{i:>4} {seg}")
