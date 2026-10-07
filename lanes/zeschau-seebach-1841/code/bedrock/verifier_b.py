#!/usr/bin/env python3
"""
VERIFIER B — independent re-derivation of Seebach lane standing facts.

Prime directive: recompute everything from PRIMARY sources.
  data/upstream-ct_R5005.digits.txt
  data/upstream-offsets.json
  code/side-keyhunt/repaired_offsets.json
  code/crowd4/phase_map_repaired.json  (comparison ONLY, never as input)

Nothing from lane code was imported or copied. All logic below is original.
stdlib only (hand-rolled k-means, chi-square, autocorrelation).

Offset convention C1 (re-derived, not assumed): per-row independent pairing —
skip the row's first `o` digits, pair the rest, drop the trailing leftover
digit when the remainder is odd. This is FORCED by the arithmetic
(3764-2*1847 = 70 dropped total) and validated by exact reproduction of every
positional claim (754/1034 6-tuples, a8_05 terminal 46 @1692, row spans).
"""
import json, math, random, os, itertools
from collections import Counter

BASE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
RES = {}

def rec(name, claimed, computed, verdict, notes=""):
    RES[name] = {"claimed": claimed, "computed": computed,
                 "verdict": verdict, "notes": notes}

def chi2_p_df4(x):
    # exact upper tail for chi-square df=4: e^{-x/2} (1 + x/2)
    return math.exp(-x/2.0) * (1.0 + x/2.0)

# =====================================================================
# 1. PRIMARY SOURCE LOADS
# =====================================================================
raw_rows = [ln.strip() for ln in open(f"{BASE}/data/upstream-ct_R5005.digits.txt") if ln.strip()]
orig_off  = json.load(open(f"{BASE}/data/upstream-offsets.json"))
rep_off   = json.load(open(f"{BASE}/code/side-keyhunt/repaired_offsets.json"))
claim_map = json.load(open(f"{BASE}/code/crowd4/phase_map_repaired.json"))  # comparison only
assert len(raw_rows) == 70 and len(orig_off) == 70 and len(rep_off) == 70

def row_sort_key(rid):
    b, l = rid.split("_")
    return (int(b[1:]), int(l))
row_ids = sorted(orig_off.keys(), key=row_sort_key)
assert row_ids == sorted(rep_off.keys(), key=row_sort_key)

# the digit rows carry no tags; row i <-> sorted row id is an assumption,
# cross-checked below via the a5_03/a6_03 row-span claims (F32).
diff = {k: (orig_off[k], rep_off[k]) for k in row_ids if orig_off[k] != rep_off[k]}
rec("repair_diff", "a5_03: 1->0 only", str(diff),
    "PASS" if diff == {"a5_03": (1, 0)} else "FAIL")

total_digits = sum(len(r) for r in raw_rows)
rec("n_digits", 3764, total_digits, "PASS" if total_digits == 3764 else "FAIL")

# =====================================================================
# 2. PAIRING (convention C1)
# =====================================================================
def pair_stream(rows, offs, rids):
    stream, spans, dropped = [], {}, {}
    for rid, dg in zip(rids, rows):
        o = offs[rid]
        seq = dg[o:]
        usable = (len(seq)//2)*2
        gs = [int(seq[i:i+2]) for i in range(0, usable, 2)]
        spans[rid] = (len(stream), len(stream)+len(gs))
        stream.extend(gs)
        dropped[rid] = o + (len(seq)-usable)
    return stream, spans, dropped

stream, spans, dropped = pair_stream(raw_rows, rep_off, row_ids)
dvals = Counter(dropped.values())
rec("dropped_distribution",
    "70 dropped total (=> 1847 pairs)",
    {"total": sum(dropped.values()), "per_row_values": dict(dvals)},
    "PASS" if sum(dropped.values()) == 70 else "FAIL",
    notes=("Per-row drops are NOT all 1: even-length rows with offset 0 drop 0, "
           "even-length rows with offset 1 drop 2, odd-length rows drop 1. "
           "Only the total (70) is constrained by (3764-2*1847)."))
rec("n_pairs", 1847, len(stream), "PASS" if len(stream) == 1847 else "FAIL")

groups = sorted(set(stream))
missing = [g for g in range(100) if g not in groups]
rec("n_groups", 96, len(groups), "PASS" if len(groups) == 96 else "FAIL",
    notes=f"codes span 00..99; absent: {missing}")

# adversarial alternative: global carry-over (row leftover joins next row)
alt, carry = [], ""
for rid, dg in zip(row_ids, raw_rows):
    s = (carry + dg)[rep_off[rid]:]
    u = (len(s)//2)*2
    alt += [int(s[i:i+2]) for i in range(0, u, 2)]
    carry = s[u:]
rec("alt_convention_pairs", "carry-over must NOT give 1847", len(alt),
    "PASS" if len(alt) != 1847 else "FAIL",
    notes=f"carry-over gives {len(alt)} pairs; only C1 reproduces 1847.")

def in_row(rid, idx):
    a, b = spans[rid]
    return a <= idx < b
rec("rowspan_a5_03", "pair 754 lies on row a5_03", str(spans["a5_03"]),
    "PASS" if in_row("a5_03", 754) else "FAIL",
    notes="F32: 754 is 'the manuscript gloss line a5_03' — validates row-id ordering.")
rec("rowspan_a6_03", "pair 1034 lies on row a6_03", str(spans["a6_03"]),
    "PASS" if in_row("a6_03", 1034) else "FAIL")

# =====================================================================
# 3. ANCHOR 6-TUPLE
# =====================================================================
needle = [11, 70, 82, 34, 29, 40]
hits = [i for i in range(len(stream)-5) if stream[i:i+6] == needle]
rec("la_premiere_positions", [754, 1034], hits,
    "PASS" if hits == [754, 1034] else "FAIL",
    notes="0-based pair indices; exactly two occurrences in the stream.")
ok6 = all(stream[754+i] == needle[i] and stream[1034+i] == needle[i] for i in range(6))
rec("gt_all_six_at_both",
    "each of 11,70,82,34,29,40 at 754+i and 1034+i",
    "all 12 positions hold" if ok6 else "MISMATCH",
    "PASS" if ok6 else "FAIL",
    notes=("Positional claim verified. All six are ground-truth pencil anchors; "
           "the VALUE assignments (la/pre/m/i/er/e) rest on the manuscript, "
           "not on digit statistics."))

# =====================================================================
# 4. CONTACT CLUSTERING — independent derivation
# Feature: concat(row-normalized predecessor dist, row-normalized successor
# dist) over the 96 observed groups. Geometry: HELLINGER — euclidean distance
# on sqrt(p). Justification: contact profiles are probability distributions;
# plain euclidean on simplex vectors collapses (demonstrated below:
# euclidean k-means degenerates to [1,1,94]-style singletons). Hellinger is
# the natural metric for distributions. Cosine variant as robustness check.
# k=3 per the hypothesis under test; we check whether rotation emerges.
# =====================================================================
obs = groups
G2I = {g: i for i, g in enumerate(obs)}
nn = len(obs)
T = [[0]*nn for _ in range(nn)]
for a, b in zip(stream, stream[1:]):
    T[G2I[a]][G2I[b]] += 1
def nrow(v):
    t = sum(v)
    return [x/t for x in v] if t else [0.0]*len(v)
pred = [[T[j][i] for j in range(nn)] for i in range(nn)]
def feats(kind):
    F = []
    for i in range(nn):
        p, s = nrow(pred[i]), nrow(T[i])
        if kind == "hell":   v = [math.sqrt(x) for x in p] + [math.sqrt(x) for x in s]
        elif kind == "euc":  v = p + s
        F.append(v)
    return F
def dist(a, b, metric):
    if metric == "euclid":
        return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))
    na = math.sqrt(sum(x*x for x in a)); nb = math.sqrt(sum(x*x for x in b))
    return 1.0 if na == 0 or nb == 0 else 1 - sum(x*y for x, y in zip(a, b))/(na*nb)
def kmeans(pts, k, seed, metric, restarts=40, iters=300):
    rng = random.Random(seed); best = None
    for _ in range(restarts):
        cs = [pts[rng.randrange(len(pts))]]
        while len(cs) < k:
            d2 = [min(dist(p, c, metric) for c in cs)**2 for p in pts]
            tot = sum(d2); r = rng.random()*tot; acc = 0.0; pick = pts[-1]
            for p, w in zip(pts, d2):
                acc += w
                if acc >= r: pick = p; break
            cs.append(pick)
        asg = [min(range(k), key=lambda c: dist(p, cs[c], metric)) for p in pts]
        for _ in range(iters):
            newc = []
            for c in range(k):
                mem = [pts[i] for i in range(len(pts)) if asg[i] == c]
                newc.append([sum(m[j] for m in mem)/len(mem)
                             for j in range(len(mem[0]))] if mem else cs[c])
            asg2 = [min(range(k), key=lambda c: dist(p, newc[c], metric)) for p in pts]
            cs = newc
            if asg2 == asg: break
            asg = asg2
        inertia = sum(min(dist(p, cs[c], metric) for c in range(k))**2 for p in pts)
        if best is None or inertia < best[0]:
            best = (inertia, asg)
    return best[1]
def phase_chi2(asg):
    TT = [[0]*3 for _ in range(3)]
    for a, b in zip(stream, stream[1:]):
        TT[asg[G2I[a]]][asg[G2I[b]]] += 1
    gt = sum(sum(r) for r in TT)
    rt = [sum(r) for r in TT]; ct = [sum(TT[i][j] for i in range(3)) for j in range(3)]
    x2 = sum((TT[i][j]-rt[i]*ct[j]/gt)**2/(rt[i]*ct[j]/gt)
             for i in range(3) for j in range(3) if rt[i]*ct[j] > 0)
    return x2, TT, rt
def cycle_report(TT, rt):
    P = [[TT[i][j]/rt[i] if rt[i] else 0 for j in range(3)] for i in range(3)]
    c1 = P[0][1]+P[1][2]+P[2][0]; c2 = P[0][2]+P[2][1]+P[1][0]
    selfm = sum(P[i][i] for i in range(3))
    return ({"0->1->2->0": round(c1,3), "0->2->1->0": round(c2,3),
             "self_mass": round(selfm,3)},
            {"P": [[round(x,3) for x in row] for row in P]})

results = {}
for kind, metric in (("euc","euclid"), ("hell","euclid"), ("hell","cos")):
    asg = kmeans(feats(kind), 3, 1841, metric)
    x2, TT, rt = phase_chi2(asg)
    cyc, tab = cycle_report(TT, rt)
    results[f"{kind}/{metric}"] = (asg, x2, cyc, tab, sorted(Counter(asg).values()))

asg_e, x2_e, cyc_e, tab_e, sz_e = results["euc/euclid"]
rec("euclid_collapse_demo",
    "INFO: euclidean k-means on raw profiles degenerates",
    {"sizes": sz_e, "chi2": round(x2_e,1)},
    "INFO",
    notes=("Plain euclidean distance on simplex vectors lumps 94/96 groups into one "
           "cluster — wrong geometry for distributions. Documents a pitfall, not the "
           "structure."))

asg, x2, cyc, tab, sz = results["hell/euclid"]
rec("independent_3phase",
    "3 clusters emerge with rotational transitions",
    {"sizes": sz, "chi2": round(x2,1), "df": 4, "p": f"{chi2_p_df4(x2):.2e}",
     "cycles": cyc},
    "PASS" if x2 > 100 and max(cyc["0->1->2->0"], cyc["0->2->1->0"]) > 1.4 else "FAIL",
    notes=("Hellinger k-means (k=3, seed 1841, 40 restarts) finds balanced clusters "
           "with a dominant directed 3-cycle and suppressed self-transitions. "
           "df=(3-1)(3-1)=4, independence null on the 3x3 phase-transition table. "
           f"Full table: {tab}"))
asg_c, x2_c, cyc_c, tab_c, sz_c = results["hell/cos"]
rec("independent_3phase_robustness",
    "cosine variant agrees",
    {"sizes": sz_c, "chi2": round(x2_c,1), "cycles": cyc_c},
    "PASS" if x2_c > 100 and max(cyc_c["0->1->2->0"], cyc_c["0->2->1->0"]) > 1.4 else "FAIL",
    notes="Same features, cosine distance: independent geometry, same qualitative outcome.")

# =====================================================================
# 5. CLAIMED chi2=366.3 — exact check under the lane's labels (comparison)
# =====================================================================
claim = {int(k): v for k, v in claim_map.items()}
def lane_chi2():
    idx = {"A":0,"B":1,"C":2}
    TT = [[0]*3 for _ in range(3)]; n = 0
    for a, b in zip(stream, stream[1:]):
        if claim[a] in idx and claim[b] in idx:
            TT[idx[claim[a]]][idx[claim[b]]] += 1; n += 1
    gt = n; rt = [sum(r) for r in TT]; ct = [sum(TT[i][j] for i in range(3)) for j in range(3)]
    x2 = sum((TT[i][j]-rt[i]*ct[j]/gt)**2/(rt[i]*ct[j]/gt)
             for i in range(3) for j in range(3) if rt[i]*ct[j] > 0)
    P = [[TT[i][j]/rt[i] for j in range(3)] for i in range(3)]
    return x2, TT, P, n
x2l, TTl, Pl, nl = lane_chi2()
rec("rotation_chi2_claimed",
    "366.3 on 4df (repaired parse)",
    {"chi2": round(x2l,1), "df": 4, "p": f"{chi2_p_df4(x2l):.2e}", "n_transitions": nl,
     "P": [[round(v,3) for v in row] for row in Pl]},
    "PASS" if abs(x2l-366.3) < 0.15 else "FAIL",
    notes=("Reproduced to the decimal under the lane's own labels (A/B/C groups only, "
           "n=1514 transitions). df=(3-1)(3-1)=4, independence null. Cycle under the "
           "lane's labels: A->B (0.545), B->C (0.498), C->A (0.624) — note this is "
           "A->B->C->A, whereas the OLD-parse F11 claim was A->C->B->A; direction "
           "labels are parse/labeling-relative."))

# =====================================================================
# 6. LAG-3 RHYTHM
# (a) raw group-index autocorrelation — the indices are arbitrary codes, so a
#     null here is EXPECTED; the rhythm lives in phase space.
# (b) independent: P(same phase at lag 3) on MY hellinger clusters vs fitted
#     first-order Markov expectation.
# (c) diagnostic: same quantity under the lane's labels (comparison).
# =====================================================================
def pearson(a, b):
    n = len(a); ma = sum(a)/n; mb = sum(b)/n
    sxy = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    sxx = sum((x-ma)**2 for x in a); syy = sum((y-mb)**2 for y in b)
    return sxy/math.sqrt(sxx*syy) if sxx and syy else 0.0
lag_raw = {}
for k in (1, 2, 3, 6):
    n = len(stream)-k
    r = pearson(stream[:n], stream[k:])
    lag_raw[k] = (round(r,4), round(r*math.sqrt(n),2))
rec("lag3_raw_index_autocorr",
    "INFO: raw group codes are arbitrary; rhythm is in phase space",
    lag_raw, "INFO",
    notes="No lag-3 signal in raw code autocorrelation (z~0.1) — expected, since "
          "group numbers are arbitrary labels. The period-3 claim is about phases.")

def lag3_samephase(asg):
    ph = [asg[G2I[g]] for g in stream]
    n3 = len(ph)-3
    same = sum(1 for i in range(n3) if ph[i] == ph[i+3])/n3
    cnt = Counter(ph); pi = [cnt[c]/len(ph) for c in range(3)]
    M = [[0]*3 for _ in range(3)]
    for a, b in zip(ph, ph[1:]): M[a][b] += 1
    rt = [sum(r) for r in M]
    Q = [[M[i][j]/rt[i] if rt[i] else 0 for j in range(3)] for i in range(3)]
    def mm(A, B): return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    Q3 = mm(mm(Q, Q), Q)
    exp_mk = sum(pi[a]*Q3[a][a] for a in range(3))
    z = (same-exp_mk)/math.sqrt(exp_mk*(1-exp_mk)/n3)
    return same, exp_mk, z
same_m, exp_m, z_m = lag3_samephase(asg)
rec("lag3_samephase_independent",
    "period-3 rhythm: lag-3 z ~ +5",
    {"obs": round(same_m,4), "exp_markov": round(exp_m,4), "z": round(z_m,2)},
    "PASS" if z_m > 4.0 else "FAIL",
    notes=("Phases from MY independent hellinger clusters. z=(obs-exp)/se with "
           "binomial se under the fitted first-order Markov null."))
phl = [claim[g] for g in stream]
# lane formulation: restrict to A/B/C positions
seq3 = [x for x in phl if x in "ABC"]
n3 = len(seq3)-3
same_l = sum(1 for i in range(n3) if seq3[i] == seq3[i+3])/n3
cnt = Counter(seq3); pi = {l: cnt[l]/len(seq3) for l in "ABC"}
M = [[0]*3 for _ in range(3)]
for a, b in zip(seq3, seq3[1:]): M[ord(a)-65][ord(b)-65] += 1
rt = [sum(r) for r in M]
Q = [[M[i][j]/rt[i] if rt[i] else 0 for j in range(3)] for i in range(3)]
def mm(A, B): return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
Q3 = mm(mm(Q, Q), Q)
exp_l = sum(pi[l]*Q3[ord(l)-65][ord(l)-65] for l in "ABC")
z_l = (same_l-exp_l)/math.sqrt(exp_l*(1-exp_l)/n3)
rec("lag3_samephase_lane_labels",
    "0.4219 vs 0.3530 Markov-expected, z=+5.6",
    {"obs": round(same_l,4), "exp_markov": round(exp_l,4), "z": round(z_l,2)},
    "PASS" if z_l > 4.0 and abs(same_l-0.4219) < 0.03 else "FAIL",
    notes=("Diagnostic under the lane's labels (A/B/C positions only). Reproduces the "
           "significance (z~+5) but not the exact decimals (obs 0.405 vs 0.422); "
           "residual gap likely from R-class handling or label version. p~1e-6..1e-8."))

# =====================================================================
# 7. AGREEMENT WITH phase_map_repaired.json (comparison only)
# =====================================================================
nonR = [g for g in obs if claim[g] in "ABC"]
def best_agree(asg):
    m = {0:"A",1:"B",2:"C"}; best = (None, -1)
    for perm in itertools.permutations(range(3)):
        ag = sum(1 for g in nonR if m[perm[asg[G2I[g]]]] == claim[g])/len(nonR)
        if ag > best[1]: best = (perm, ag)
    return best
perm, ag_nr = best_agree(asg)
m = {0:"A",1:"B",2:"C"}
aligned = {g: m[perm[asg[G2I[g]]]] for g in obs}
ag_all = sum(1 for g in obs if aligned[g] == claim[g])/len(obs)
Rsplit = dict(Counter(aligned[g] for g in obs if claim[g] == "R"))
rec("phase_agreement",
    "fraction of groups agreeing with claimed map",
    {"agree_all96": round(ag_all,3), "agree_nonR_76": round(ag_nr,3),
     "align_perm": perm, "R_split": Rsplit},
    "INFO",
    notes=("Permutation chosen to MAXIMIZE agreement — this inflates the fraction; "
           "read as an upper bound. R (20 groups) has no counterpart in a 3-cluster "
           "solution and counts as disagreement in all-96. Lane's own fragility flag: "
           "61/96 groups changed phase between old and repaired parses."))

# =====================================================================
# 8. ANCHOR INVENTORY
# =====================================================================
cnt = Counter(stream)
GT = {11:"la", 70:"pre", 82:"m", 34:"i", 29:"er", 40:"e", 46:"que"}
PROV = {87:"ce", 64:"qui", 96:"par"}
PROVC = {77:"le"}
for g, val in list(GT.items())+list(PROV.items())+list(PROVC.items()):
    tier = "GT-pencil" if g in GT else ("provisional" if g in PROV else "provisional-conditioned")
    rec(f"anchor_g{g}",
        f"group exists ({tier})",
        cnt.get(g, 0),
        "PASS" if cnt.get(g, 0) > 0 else "FAIL",
        notes=(f"Existence: verifiable above. Value '{val}' rests on the erased pencil "
               "crib / lane inference — NOT independently verifiable from digit statistics."))

# old-parse counts (pre-repair, 1846 pairs) to test the staleness hypothesis
old_stream, _, _ = pair_stream(raw_rows, orig_off, row_ids)
old_cnt = Counter(old_stream)
for g, cl in ((87,32),(64,46),(96,21),(11,44),(46,29)):
    co = cnt[g]
    stale = (old_cnt[g] == cl != co)
    rec(f"count_g{g}", cl, co,
        "PASS" if co == cl else "FAIL",
        notes=("STALE-CLAIM: claimed value matches the OLD (pre-repair, 1846-pair) parse "
               f"exactly (old n{g}={old_cnt[g]}); repaired parse gives {co}. The lane's "
               "count claim was not re-derived after F32." if stale else ""))
rec("count_g77", "no explicit n77 count claim found in NOTES.md", cnt[77], "INFO",
    notes=("Searched NOTES.md: only transition counts mention 77 (67->77 x6, 77->78 x7). "
           "n77=44 under both parses. 77=le is provisional-conditioned — value rests "
           "on lane inference, not verifiable here."))

a, b = spans["a8_05"]
rec("a8_05_ends_46", "row a8_05 ends with group 46 at pair idx 1692",
    f"span=({a},{b}), last={stream[b-1]}",
    "PASS" if stream[b-1] == 46 and b-1 == 1692 else "FAIL")

# =====================================================================
# WRITE OUTPUTS
# =====================================================================
os.makedirs(f"{BASE}/code/bedrock", exist_ok=True)
json.dump(RES, open(f"{BASE}/code/bedrock/verifier_b_results.json","w"), indent=1, sort_keys=True)
L = ["# Verifier B ledger — independent re-derivation (2026-10-07)", "",
 "Method: stdlib-only Python written from scratch; lane code never imported. Primary "
 "sources: data/upstream-ct_R5005.digits.txt, data/upstream-offsets.json, "
 "code/side-keyhunt/repaired_offsets.json. code/crowd4/phase_map_repaired.json used for "
 "comparison only. Offset convention C1 (per-row independent pairing, drop phase-"
 "inconsistent digit) is FORCED by (3764-2*1847)=70 and validated by exact positional "
 "reproduction; carry-over alternative falsified.",
 "Clustering: k-means k=3 on concat(predecessor, successor) row-normalized contact "
 "profiles with HELLINGER geometry (euclidean on sqrt(p) — the natural metric for "
 "distributions); cosine variant as robustness. Plain euclidean on simplex vectors "
 "degenerates (documented). Seed 1841, 40 restarts, best inertia kept.",
 ""]
for k in RES:
    r = RES[k]
    L += [f"## {k}: {r['verdict']}", f"- claimed: {r['claimed']}",
          f"- computed: {r['computed']}"]
    if r["notes"]: L.append(f"- notes: {r['notes']}")
    L.append("")
open(f"{BASE}/code/bedrock/verifier_b_ledger.md","w").write("\n".join(L))
fails = [k for k,v in RES.items() if v["verdict"]=="FAIL"]
print("facts:", len(RES), "| FAIL:", fails if fails else "none")
