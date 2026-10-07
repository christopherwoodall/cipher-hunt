#!/usr/bin/env python3
"""PHONETICIAN — CV-structure tests of the rotation (side-rotation fleet).

Pre-registration: code/side-rotation/prereg_phonetician.md (written BEFORE running).
Fisher exact (Freeman-Halton, probability definition) via full enumeration of
fixed-margin tables. No ciphertext/keys invented; phases read from
code/crowd4/phase_map_repaired.json; phonetic values from the crib-learned
inventory (F44) + Frenchman ear checks (borrowed, not re-staffed).
"""
import json, math, itertools, random
from collections import Counter

LANE = "/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841"

# Pre-registered test set: group -> (value, status, open/closed, sonority, tier)
TESTSET = {
    "11": ("la",  "GT-crib",        "open",   "balanced", "Tier0"),
    "70": ("pre", "GT-crib",        "open",   "heavy",    "Tier0"),
    "82": ("m",   "GT-crib",        "closed", "heavy",    "Tier0"),
    "34": ("i",   "GT-crib",        "open",   "light",    "Tier0"),
    "29": ("er",  "GT-crib",        "closed", "balanced", "Tier0"),
    "40": ("e",   "GT-crib",        "open",   "light",    "Tier0"),
    "46": ("que", "GT-crib",        "open",   "balanced", "Tier0"),
    "87": ("ce",  "PROVISIONAL",    "open",   "balanced", "Prov"),
    "64": ("qui", "PROVISIONAL",    "open",   "balanced", "Prov"),
    "96": ("par", "PROVISIONAL",    "closed", "heavy",    "Prov"),
    "94": ("ne",  "PROVISIONAL-strong", "open", "balanced", "Prov"),
    "77": ("le",  "LEAD",           "open",   "balanced", "Lead"),
    "62": ("on",  "STRONG-LEAD",    "open",   "light",    "Lead"),
    "78": ("me",  "LEAD",           "open",   "balanced", "Lead"),
    "47": ("ce",  "LEAD",           "open",   "balanced", "Lead"),
    "52": ("pas", "STRONG-bounded", "open",   "balanced", "Lead"),
}
PHASE_ORDER = ["A", "B", "C"]

def load_phases():
    pm = json.load(open(f"{LANE}/code/crowd4/phase_map_repaired.json"))
    c = Counter(pm.values())
    assert c == Counter({"A": 32, "B": 27, "R": 20, "C": 17}), f"phase map drift: {c}"
    return pm

def tabulate(rowkey, colkey, groups, pm, rowvals):
    rows = {v: [0]*3 for v in rowvals}
    for g in groups:
        rows[getattr_row(g, rowkey)][PHASE_ORDER.index(pm[g])] += 1
    return rows

def getattr_row(g, key):
    return TESTSET[g][{"open": 2, "son": 3, "tier": 4}[key]]

def table_prob(t, r, c, n):
    # multinomial: P = (prod r_i! prod c_j!) / (n! prod t_ij!)
    num = sum(math.lgamma(x + 1) for x in r) + sum(math.lgamma(x + 1) for x in c)
    den = math.lgamma(n + 1) + sum(math.lgamma(x + 1) for row in t for x in row)
    return math.exp(num - den)

def enumerate_tables(r, c):
    """Yield all r x c tables with row sums r, col sums c."""
    nrows, ncols = len(r), len(c)
    if nrows == 1:
        if sum(c) == r[0]:
            yield [list(c)]
        return
    # fill first row: compositions of r[0] bounded by remaining col sums
    def row_comps(rem, cols, idx, cur):
        if idx == ncols - 1:
            if rem <= cols[idx]:
                yield cur + [rem]
            return
        for v in range(0, min(rem, cols[idx]) + 1):
            yield from row_comps(rem - v, cols, idx + 1, cur + [v])
    for first in row_comps(r[0], c, 0, []):
        c2 = [c[j] - first[j] for j in range(ncols)]
        for rest in enumerate_tables(r[1:], c2):
            yield [first] + rest

def fisher_exact(rows, rowvals):
    t = [rows[v] for v in rowvals]
    r = [sum(row) for row in t]
    c = [sum(t[i][j] for i in range(len(t))) for j in range(len(t[0]))]
    n = sum(r)
    p_obs = table_prob(t, r, c, n)
    p = 0.0
    for tab in enumerate_tables(r, c):
        pt = table_prob(tab, r, c, n)
        if pt <= p_obs * (1 + 1e-9):
            p += pt
    return p, t, r, c, n

def fmt(t, rowvals):
    return {v: t[i] for i, v in enumerate(rowvals)}

def run_test(name, rowkey, rowvals, groups, pm):
    rows = {v: [0]*3 for v in rowvals}
    for g in groups:
        rows[TESTSET[g][{"open":2,"son":3,"tier":4}[rowkey]]][PHASE_ORDER.index(pm[g])] += 1
    p, t, r, c, n = fisher_exact(rows, rowvals)
    return {"name": name, "p": p, "table": fmt(t, rowvals), "row_marginals": r,
            "col_marginals": c, "n": n}

def min_attainable_p(rowvals, groups, pm, rowkey):
    # minimum p-value any table with these margins could yield
    rows = {v: [0]*3 for v in rowvals}
    for g in groups:
        rows[TESTSET[g][{"open":2,"son":3,"tier":4}[rowkey]]][PHASE_ORDER.index(pm[g])] += 1
    t = [rows[v] for v in rowvals]
    r = [sum(row) for row in t]
    c = [sum(t[i][j] for i in range(len(t))) for j in range(len(t[0]))]
    n = sum(r)
    best = 1.0
    for tab in enumerate_tables(r, c):
        p_obs = table_prob(tab, r, c, n)
        p = sum(table_prob(tb, r, c, n) for tb in enumerate_tables(r, c)
                if table_prob(tb, r, c, n) <= p_obs * (1 + 1e-9))
        if p < best:
            best = p
    return best

def power_sim(rowkey, rowvals, groups, pm, alt, nsim=20000, seed=1841):
    """Simulate power under a stated alternative: alt = dict value -> phase probs."""
    rng = random.Random(seed)
    pm_ph = [pm[g] for g in groups]
    hits = 0
    for _ in range(nsim):
        sim_rows = {v: [0]*3 for v in rowvals}
        for g in groups:
            v = TESTSET[g][{"open":2,"son":3,"tier":4}[rowkey]]
            probs = alt.get(v, alt.get("default"))
            ph = PHASE_ORDER[rng.choices(range(3), weights=probs)[0]]
            sim_rows[v][PHASE_ORDER.index(ph)] += 1
        p, *_ = fisher_exact(sim_rows, rowvals)
        if p < 0.05:
            hits += 1
    return hits / nsim

def main():
    pm = load_phases()
    groups = list(TESTSET.keys())
    assert all(pm[g] in "ABC" for g in groups), "an anchor is R-phase!"

    results = {}
    # --- Primary tests ---
    results["T-Pa"] = run_test("T-Pa open/closed x phase", "open",
                               ["open", "closed"], groups, pm)
    results["T-Pb"] = run_test("T-Pb tier x phase", "tier",
                               ["Tier0", "Prov", "Lead"], groups, pm)
    results["T-Pc"] = run_test("T-Pc sonority x phase", "son",
                               ["light", "balanced", "heavy"], groups, pm)

    # --- Pre-registered robustness variants ---
    gtprov = [g for g in groups if TESTSET[g][4] in ("Tier0", "Prov")]  # n=11
    results["T-Pa2"] = run_test("T-Pa2 open/closed x phase, GT+prov only", "open",
                                ["open", "closed"], gtprov, pm)
    # sensitivity: 78 as rival "ver" (closed)
    saved = TESTSET["78"]
    TESTSET["78"] = ("ver", "LEAD", "closed", "balanced", "Lead")
    results["T-Pa3"] = run_test("T-Pa3 78 recoded ver/closed", "open",
                                ["open", "closed"], groups, pm)
    TESTSET["78"] = saved
    results["T-Pc2"] = run_test("T-Pc2 sonority x phase, GT+prov only", "son",
                                ["light", "balanced", "heavy"], gtprov, pm)

    # --- Power notes ---
    results["min_p_T-Pa"] = min_attainable_p(["open", "closed"], groups, pm, "open")
    results["min_p_T-Pc"] = min_attainable_p(["light","balanced","heavy"], groups, pm, "son")

    # Strong alternative A: all 3 closed units in phase C, open at observed phase rates
    open_ph = Counter(pm[g] for g in groups if TESTSET[g][2] == "open")
    tot_o = sum(open_ph.values())
    altA = {"open": [open_ph["A"]/tot_o, open_ph["B"]/tot_o, open_ph["C"]/tot_o],
            "closed": [0.0, 0.0, 1.0]}
    results["power_T-Pa_all-closed-in-C"] = power_sim("open", ["open","closed"],
                                                     groups, pm, altA)
    # Strong alternative C: heavy units all in A
    son_ph = {v: Counter(pm[g] for g in groups if TESTSET[g][3] == v)
              for v in ["light","balanced","heavy"]}
    altC = {}
    for v in ["light","balanced","heavy"]:
        t = sum(son_ph[v].values())
        altC[v] = [son_ph[v]["A"]/t, son_ph[v]["B"]/t, son_ph[v]["C"]/t]
    altC["heavy"] = [1.0, 0.0, 0.0]
    results["power_T-Pc_all-heavy-in-A"] = power_sim("son", ["light","balanced","heavy"],
                                                    groups, pm, altC)

    # --- assert pre-registered tables match ---
    assert results["T-Pa"]["table"] == {"open":[4,6,3], "closed":[1,0,2]}, results["T-Pa"]["table"]
    assert results["T-Pb"]["table"] == {"Tier0":[2,4,1], "Prov":[1,2,1], "Lead":[2,0,3]}, results["T-Pb"]["table"]
    assert results["T-Pc"]["table"] == {"light":[2,1,0], "balanced":[2,4,4], "heavy":[1,1,1]}, results["T-Pc"]["table"]

    out = {"tests": results, "groups": {g: {"value": v[0], "status": v[1], "phase": pm[g],
                                            "shape": v[2], "sonority": v[3], "tier": v[4]}
                                        for g, v in TESTSET.items()}}
    with open(f"{LANE}/code/side-rotation/phonetician/phonetician_results.json", "w") as f:
        json.dump(out, f, indent=2)
    for k, r in results.items():
        if isinstance(r, dict) and "p" in r:
            print(f"{k}: p={r['p']:.4f} n={r['n']} table={r['table']}")
        else:
            print(f"{k}: {r:.4f}")

if __name__ == "__main__":
    main()
