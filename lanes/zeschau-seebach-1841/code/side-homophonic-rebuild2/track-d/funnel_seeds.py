#!/usr/bin/env python3
"""Track D -- funnel seed package generator (Smith rebuild fleet, step-4 funnel).

Generates the 200-seed package for the judge-driven funnel (PREREG-D-v2 Stage 1):
    100 random          -- hard pins fixed, rest uniform over inventory
     60 lexicon-seeded -- high-frequency by-ear words get 1-3 alias cells each, rest random
     40 crib-extended  -- formula-anchored (8 seeds x 5 formulae), rest lexicon+random

Every seed is a FULL 96-cell initial key (v1) plus polyvalence v2 for cell 67,
matching solver-cell/solver.py's key model (v1[g], v2[g]). Group labels are the
96 used two-digit groups (unused: 05/25/72/75). The funnel's
per-instance instantiation follows PREREG-D-v2's RNG convention
(random.Random(2000 + 100*inst_idx + i)); this package is instance-agnostic and
fully deterministic under its own master seed, logged in the manifest.

CONSTRAINTS (binding):
  * R5005 NEVER touched: the only inputs read are table-registry.json (the
    board) and solver-cell/inventory_data.json (static, crib-derived lexicon).
    No ciphertext/group files are opened; no search is executed.
  * Gate/control instances sealed: nothing is read from control/ or solver_inbox/.
  * Deterministic: random.Random(f"trackD-funnel|{MASTER_SEED}|{seed_id}");
    master seed logged in priors-manifest.json.
  * Seed GENERATION only: no scoring, no judge calls, no annealing.

Priors encoded (see priors-manifest.json for status of each):
  * 7 ratified hard pins (pencil ground truth): 11=la 70=pre 82=m 34=i 29=er 40=e 46=que
  * 8 soft priors (PROMOTE-grade/provisional, Bernoulli-sampled per seed):
    87=ce 64=qui 96=par 17=fois 59=est 77=le 47=ce(post-24 allophone) 79=tout
  * 6 lead priors (weak soft): 00=pour | 00=le (mutually exclusive), 24=en,
    62=on (fenced), 84=en (m'en), 06=ent (ment)
  * 5 word/frame rules, 67 et/veut sole polyvalence, 4 split homophone sets
    (exclusivity enforced + asserted), 1690 uniformity as alias-count prior,
    class tags for 31/32/33/37/19/66/89/78.
"""

import json
import random
import sys
from collections import Counter
from pathlib import Path

TRACKD = Path(__file__).resolve().parent
CODE = TRACKD.parent.parent                      # .../code
REGISTRY_PATH = CODE / "table-grid" / "table-registry.json"
INVENTORY_PATH = TRACKD / "solver-cell" / "inventory_data.json"
OUT_DIR = TRACKD / "funnel"

MASTER_SEED = 184101
# 96 of 100 two-digit groups used; unused: 05, 25, 72, 75 (per the control
# harness's public file header -- structural metadata only, not R5005).
UNUSED_GROUPS = {"05", "25", "72", "75"}
CELLS = [f"{i:02d}" for i in range(100) if f"{i:02d}" not in UNUSED_GROUPS]
N_RANDOM, N_LEXICON, N_CRIB = 100, 60, 40

# ---------------------------------------------------------------- priors ---
# Ratified hard pins (registry status "gt" = pencil ground truth). Verified
# against table-registry.json at generation time; mismatch aborts.
HARD_PINS = {"11": "la", "70": "pre", "82": "m", "34": "i",
             "29": "er", "40": "e", "46": "que"}

# (cell, value, status, per-class Bernoulli p, evidence note)
SOFT_PRIORS = [
    ("87", "ce",   "PROMOTE-grade", {"random": 0.50, "lexicon": 0.65, "crib": 0.85},
     "87=ce battery-promoted; red-team ratification pending"),
    ("64", "qui",  "PROMOTE-grade", {"random": 0.50, "lexicon": 0.65, "crib": 0.85},
     "64=qui battery-promoted; red-team ratification pending"),
    ("96", "par",  "PROMOTE-grade", {"random": 0.50, "lexicon": 0.65, "crib": 0.85},
     "96=par battery-promoted; CAVEAT: 'ce qui 96 47 que' wants a verb (STATE R13)"),
    ("17", "fois", "PROMOTE-grade", {"random": 0.35, "lexicon": 0.50, "crib": 0.90},
     "17=fois new 4-leg battery; PROMOTE-grade awaiting adjudication"),
    ("59", "est",  "provisional",   {"random": 0.35, "lexicon": 0.50, "crib": 0.80},
     "59=est provisional; split-set {52,59} bars 52 from 'est' in every seed"),
    ("77", "le",   "provisional",   {"random": 0.35, "lexicon": 0.50, "crib": 0.75},
     "77=le provisional, CONDITIONED (not yet promoted)"),
    ("47", "ce",   "PROMOTE-grade", {"random": 0.40, "lexicon": 0.55, "crib": 0.70},
     "47=ce positional allophone AFTER 24=en; NOT a merge with 87 (allophony licensed)"),
    ("79", "tout", "PROMOTE-grade", {"random": 0.40, "lexicon": 0.55, "crib": 0.70},
     "79=tout PROMOTE-grade awaiting adjudication"),
]

# Weaker lead / formula-derived priors. 00=pour and 00=le are mutually
# exclusive per seed (first sampled wins; pour evaluated first = top-frequency lead).
LEAD_PRIORS = [
    ("00", "pour", "lead",        {"random": 0.25, "lexicon": 0.30, "crib": 0.35},
     "00=pour top-frequency lead; 00->46 x4 'pour que'; EXCLUSIVE with 00=le"),
    ("00", "le",   "formula",     {"random": 0.20, "lexicon": 0.25, "crib": 0.40},
     "00=le from 96-00='par le' word rule; EXCLUSIVE with 00=pour (tension documented)"),
    ("24", "en",   "lead-strong", {"random": 0.55, "lexicon": 0.65, "crib": 0.90},
     "24=en strong lead (24-87='en ce' frame rule)"),
    ("62", "on",   "fenced",      {"random": 0.30, "lexicon": 0.40, "crib": 0.50},
     "62=on FENCED: contained hypothesis, neither promoted nor killed"),
    ("84", "en",   "formula",     {"random": 0.25, "lexicon": 0.30, "crib": 0.35},
     "84 from 82-84=\"m'en\" word rule (82=m hard)"),
    ("06", "ent",  "formula",     {"random": 0.25, "lexicon": 0.30, "crib": 0.35},
     "06 from 82-06='ment' word rule; 06 verb-stem tension noted, value stays fragment"),
]

# 4 homophone sets SPLIT by red team: exclusivity enforced in every seed.
SPLIT_SETS = [["33", "86"], ["48", "94"], ["52", "59"], ["76", "78"]]

# Sole true polyvalence (registry): never collapsed to a single value.
POLYVALENCE_67 = ["et", "veut"]

# Class tags (constraints on cell class, NOT values) -- carried per seed.
CLASS_TAGS = {
    "31": ["VERBAL"], "33": ["INF"], "37": ["VERBAL", "ADJ"],
    "32": ["ADJ"], "19": ["ADJ"],
    "66": ["class-constraint"], "89": ["class-constraint"],
    "78": ["ver/er?", "lead"],
}

# Confirmed formulae anchoring the 40 crib-extended seeds.
# "cells": pinned values; "soft_cells": the ones that are soft (rest are hard pins).
FORMULAE = {
    "la-premiere-fois": {"cells": {"11": "la", "70": "pre", "82": "m", "34": "i",
                                  "29": "er", "40": "e", "17": "fois"},
                         "soft_cells": ["17"],
                         "note": "'la premiere' @pairs 754+1034 ground truth; 17=fois soft"},
    "par-ce-que": {"cells": {"96": "par", "87": "ce", "46": "que"},
                   "soft_cells": ["96", "87"],
                   "note": "'parce que' frame x3 (repaired syllabary-aware computation)"},
    "par-le":     {"cells": {"96": "par", "00": "le"},
                   "soft_cells": ["96", "00"],
                   "note": "96-00='par le' word/frame rule"},
    "en-cela":    {"cells": {"24": "en", "87": "ce", "11": "la"},
                   "soft_cells": ["24", "87"],
                   "note": "24-87='en ce' frame rule + 'cela'=87+11 rule"},
    "qui-est":    {"cells": {"64": "qui", "59": "est"},
                   "soft_cells": ["64", "59"],
                   "note": "64=qui / 59=est joint window"},
}

# 1690 uniformity: prior on alias-count DISTRIBUTIONS, not hard assignments.
ALIAS_COUNT_DIST = {1: 0.45, 2: 0.35, 3: 0.20}
MAX_ALIASES_PER_UNIT = 5


# ------------------------------------------------------------- inventory ---
def load_inputs():
    """Read ONLY the board registry and the static lexicon. No cipher data."""
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    inv = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
    return registry, inv


def check_hard_pins(registry):
    cells = registry["cells"]
    bad = []
    for cell, val in HARD_PINS.items():
        entry = cells.get(cell)
        if not entry or entry[0] != val or entry[1] != "gt":
            bad.append((cell, val, entry))
    if bad:
        raise SystemExit(f"ABORT: hard-pin mismatch vs registry: {bad}")


def build_pools(inv):
    """Lexicon pools from the lane's static inventory artifacts.

    POOL: units + tier3_top200, minus multi-char banked/soft/lead strings so
    random fill cannot dilute anchors (single letters stay: letter cells exist).
    LEX_CORE: multi-char alphabetic tier3 head words for lexicon seeding.
    """
    units = inv["units"]
    tier3 = inv["tier3_top200"]
    banked_strings = {v for v in HARD_PINS.values()}
    banked_strings |= {val for (_, val, _, _, _) in SOFT_PRIORS + LEAD_PRIORS}
    banked_strings |= {"et", "veut"}  # 67 polyvalence values (licensed separately)
    excluded = {s for s in banked_strings if len(s) > 1}
    pool = sorted({u for u in units + tier3 if u not in excluded})
    lex_core = sorted({w for w in tier3[:80]
                       if len(w) >= 2 and w.isalpha() and w not in excluded})
    return pool, lex_core, excluded


# ------------------------------------------------------------ generation ---
def alias_k(rng):
    r = rng.random()
    cum = 0.0
    for k in (1, 2, 3):
        cum += ALIAS_COUNT_DIST[k]
        if r < cum:
            return k
    return 1


def gen_seed(seed_id, cls, pool, lex_core, formula=None):
    rng = random.Random(f"trackD-funnel|{MASTER_SEED}|{seed_id}")
    v1, soft_applied = {}, {}
    counts = Counter()

    def place(cell, val):
        v1[cell] = val
        counts[val] += 1

    def draw_unit(forbid=frozenset()):
        for _ in range(200):
            cand = rng.choice(pool)
            if cand in forbid:
                continue
            if counts[cand] >= MAX_ALIASES_PER_UNIT:
                continue
            return cand
        return rng.choice(pool)  # degenerate fallback; still deterministic

    # 1. hard pins (ratified) -- every seed, immutable
    for c, val in HARD_PINS.items():
        place(c, val)

    # 2. formula anchor (crib-extended only)
    if formula:
        F = FORMULAE[formula]
        for c, val in F["cells"].items():
            if c in v1:
                continue
            place(c, val)
            if c in F["soft_cells"]:
                soft_applied[c] = {"value": val, "status": "formula-anchored",
                                  "source": formula}

    # 3. soft / lead priors, Bernoulli-sampled (weighted, not fixed)
    for (cell, val, status, probs, _note) in SOFT_PRIORS + LEAD_PRIORS:
        if cell in v1:
            continue  # also enforces 00 pour/le mutual exclusivity
        if rng.random() < probs[cls]:
            place(cell, val)
            soft_applied[cell] = {"value": val, "status": status}

    # 4. 67 sole polyvalence: v1 sampled, v2 = the other; never collapsed
    pick = rng.choice(POLYVALENCE_67)
    place("67", pick)
    v2_67 = POLYVALENCE_67[1] if pick == POLYVALENCE_67[0] else POLYVALENCE_67[0]

    # 5. lexicon core (lexicon-seeded + crib-extended): alias blocks of
    #    high-frequency by-ear words, alias counts per uniformity prior
    remaining = [c for c in CELLS if c not in v1]
    rng.shuffle(remaining)
    if cls in ("lexicon", "crib"):
        n_words = rng.randint(10, 16)
        for w in rng.sample(lex_core, min(n_words, len(lex_core))):
            k = alias_k(rng)
            for _ in range(k):
                if not remaining:
                    break
                c = remaining.pop()
                if c == "67":
                    continue
                place(c, w)

    # 6. random fill for everything left (uniform over inventory pool)
    for c in remaining:
        if c in v1 or c == "67":
            continue
        place(c, draw_unit())

    # 7. split-set exclusivity: resample the second cell on collision
    for a, b in SPLIT_SETS:
        if v1[a] == v1[b]:
            for _ in range(200):
                cand = draw_unit(forbid={v1[a]})
                if cand != v1[a]:
                    counts[v1[b]] -= 1
                    place(b, cand)
                    break

    alias_hist = {u: n for u, n in sorted(counts.items())}
    seed = {
        "seed_id": seed_id,
        "class": cls,
        "sub_seed": f"trackD-funnel|{MASTER_SEED}|{seed_id}",
        "formula": formula,
        "pins": dict(HARD_PINS),
        "soft_applied": soft_applied,
        "polyvalence": {"67": POLYVALENCE_67},
        "v1": {c: v1[c] for c in CELLS},
        "v2": {"67": v2_67},
        "class_tags": CLASS_TAGS,
        "alias_counts": alias_hist,
        "notes": ("47=ce positional allophone applies post-24 (decode-time rule); "
                  "00 pour/le mutually exclusive; split sets exclusive; "
                  "1690 uniformity via alias-count prior, cap "
                  f"{MAX_ALIASES_PER_UNIT}/unit."),
    }
    return seed


# ------------------------------------------------------------ validation ---
def validate(seeds, pool, lex_core, excluded):
    allowed = set(pool) | set(lex_core)
    allowed |= {v for v in HARD_PINS.values()}
    allowed |= {val for (_, val, _, _, _) in SOFT_PRIORS + LEAD_PRIORS}
    allowed |= set(POLYVALENCE_67)
    errs = []
    for s in seeds:
        v1 = s["v1"]
        if set(v1) != set(CELLS):
            errs.append((s["seed_id"], "cell coverage"))
        for c, val in HARD_PINS.items():
            if v1[c] != val:
                errs.append((s["seed_id"], f"hard pin {c}"))
        for a, b in SPLIT_SETS:
            if v1[a] == v1[b]:
                errs.append((s["seed_id"], f"split collision {a}/{b}={v1[a]}"))
        if not (s["v1"]["67"] in POLYVALENCE_67 and
                s["v2"]["67"] in POLYVALENCE_67 and
                s["v1"]["67"] != s["v2"]["67"]):
            errs.append((s["seed_id"], "67 polyvalence"))
        if v1["52"] == "est":
            errs.append((s["seed_id"], "52=est violates {52,59} split"))
        for c, val in v1.items():
            if val not in allowed:
                errs.append((s["seed_id"], f"unknown value {val!r}"))
                break
            if (len(val) > 1 and val in excluded and c not in HARD_PINS
                    and c not in s["soft_applied"] and c != "67"):
                errs.append((s["seed_id"], f"unlicensed banked string {val!r} on {c}"))
                break
        for c, meta in s["soft_applied"].items():
            if v1[c] != meta["value"]:
                errs.append((s["seed_id"], f"soft_applied mismatch {c}"))
    return errs


# -------------------------------------------------------------- manifest ---
def build_manifest(pool, lex_core, excluded, registry, inv):
    def prior_entry(cell, val, status, probs, note):
        return {"cell": cell, "value": val, "status": status,
                "encoding": "soft Bernoulli per seed",
                "p_random": probs["random"], "p_lexicon": probs["lexicon"],
                "p_crib": probs["crib"], "note": note}

    priors = [{"cell": c, "value": v, "status": "ratified (pencil ground truth)",
               "encoding": "HARD constraint: fixed in all 200 seeds, solver-immutable",
               "registry_status": "gt"}
              for c, v in HARD_PINS.items()]
    priors += [prior_entry(c, v, st, p, n) for (c, v, st, p, n) in SOFT_PRIORS]
    priors += [prior_entry(c, v, st, p, n) for (c, v, st, p, n) in LEAD_PRIORS]

    return {
        "meta": {
            "package": "Track D step-4 funnel seed package (Smith rebuild fleet)",
            "generated_by": "track-d/funnel_seeds.py",
            "master_seed": MASTER_SEED,
            "sub_seed_scheme": "random.Random(f'trackD-funnel|{MASTER_SEED}|{seed_id}')",
            "n_seeds": 200,
            "composition": {"random": N_RANDOM, "lexicon_seeded": N_LEXICON,
                            "crib_extended": N_CRIB,
                            "crib_formulae": {f: 8 for f in FORMULAE}},
            "inputs_read": [str(REGISTRY_PATH), str(INVENTORY_PATH)],
            "r5005_contact": "NONE. No ciphertext/group files opened; seeds built "
                             "from board priors + static lexicon only. No search executed.",
            "gate_instances": "sealed; nothing read from control/ or solver_inbox/ "
                              "(group label set 96/100 from the control harness's public "
                              "file header only -- no keys/plaintexts)",
            "inventory_provenance": inv.get("provenance", {}),
            "pool_size": len(pool), "lex_core_size": len(lex_core),
        },
        "priors": priors,
        "word_frame_rules": [
            {"rule": "82-84 = m'en", "encoding": "82=m hard; 84=en lead-soft p=0.25-0.35"},
            {"rule": "82-06 = ment", "encoding": "82=m hard; 06=ent lead-soft p=0.25-0.35 "
             "(fragment value; 06 verb-stem tension noted)"},
            {"rule": "96-00 = par le", "encoding": "96=par PROMOTE-soft; 00=le formula-soft, "
             "mutually exclusive with 00=pour per seed"},
            {"rule": "24-87 = en ce", "encoding": "24=en lead-strong; 87=ce PROMOTE-soft; "
             "jointly pinned in 'en-cela' crib seeds"},
            {"rule": "cela = 87+11", "encoding": "structural consistency note: 87=ce soft + 11=la hard"},
        ],
        "polyvalence": {"67": {"values": POLYVALENCE_67, "status": "sole true polyvalence",
                               "encoding": "v1 sampled per seed, v2=the other; never collapsed"}},
        "split_sets": [{"cells": s, "status": "SPLIT (red-team adjudicated)",
                        "encoding": "exclusivity enforced at generation + asserted in validation"}
                       for s in SPLIT_SETS],
        "uniformity_prior_1690": {
            "statement": "homophone sets must be uniform -- encoded as a prior on "
                         "alias-count DISTRIBUTIONS, not hard assignments",
            "alias_count_dist": {str(k): p for k, p in ALIAS_COUNT_DIST.items()},
            "max_aliases_per_unit": MAX_ALIASES_PER_UNIT,
            "random_class": "uniform over inventory pool (Poisson-ish alias counts + cap)",
        },
        "class_tags": {c: {"classes": t, "encoding": "carried per seed; not a value assignment"}
                       for c, t in CLASS_TAGS.items()},
        "formulae": {f: {"cells": d["cells"], "soft_cells": d["soft_cells"], "note": d["note"]}
                     for f, d in FORMULAE.items()},
        "hot_biases": {
            "37": "verb/adjective tension -> class tag only, no value seeded",
            "32/19": "predicative adjectives -> class tags only",
            "00=pour": "top-frequency lead, p=0.25-0.35",
            "24=en": "strong lead, p=0.55-0.90",
            "62=on": "fenced, p=0.30-0.50",
        },
        "ambiguities_resolved": [
            {"ambiguity": "00 = 'pour' (lead, top frequency) vs 'le' (96-00='par le' rule)",
             "resolution": "mutually exclusive per-seed Bernoulli (pour first, p=0.25-0.35; "
             "le second, p=0.20-0.40); neither fixed; both stay soft pending adjudication"},
            {"ambiguity": "47=ce vs 87=ce looks like a homophone merge",
             "resolution": "encoded as POSITIONAL ALLOPHONE: 47 carries decode-time rule "
             "'applies after 24=en'; 87 unconditioned; splits/aliases unaffected"},
            {"ambiguity": "17=fois inside the 'confirmed' formula 'la premiere fois'",
             "resolution": "formula pins 17 as SOFT (p=0.90 in la-premiere-fois crib seeds, "
             "0.35-0.50 elsewhere), never hard; PROMOTE status unchanged"},
            {"ambiguity": "59=est provisional + {52,59} split",
             "resolution": "52 explicitly barred from 'est' in all seeds; collision "
             "resampled at generation and asserted in validation"},
            {"ambiguity": "77=le (conditioned provisional) vs 00=le (formula lead)",
             "resolution": "both soft; allowed to co-occur (homophony is legal in a "
             "homophonic table); neither fixed"},
            {"ambiguity": "96=par vs STATE round-13 tension ('ce qui 96 47 que' wants a verb)",
             "resolution": "moderate weight p=0.50-0.85 with the caveat recorded in the "
             "prior note; not hard, flagged for the funnel's judge triage"},
            {"ambiguity": "24=en now vs refuted 24='est' (N10)",
             "resolution": "'est' appears NOWHERE in seeds; 24=en is a fresh lead prior, "
             "not a resurrection of the killed hypothesis"},
            {"ambiguity": "banked-value aliasing (should random cells get 'le','e',...?)",
             "resolution": "conservative: multi-char banked/soft/lead strings excluded from "
             "random fill (single letters stay -- letter cells exist); extra aliases only "
             "via licensed priors (47=ce). Solver moves (alias-split+merge) may create "
             "aliases during the climb."},
            {"ambiguity": "lexicon provenance / register",
             "resolution": "static lane artifacts (inventory_data.json: units from "
             "data/upstream-syll.py + by-ear tier3_top200); NOT cipher-fitted; "
             "register is generic French by-ear, flagged provisional-infrastructure"},
        ],
        "determinism": {"master_seed": MASTER_SEED, "rng": "random.Random (str seed, "
                        "version-stable)", "seed_logged": True,
                        "per_instance_convention": "funnel generator uses "
                        "random.Random(2000 + 100*inst_idx + i) per PREREG-D-v2"},
    }


# ------------------------------------------------------------------ main ---
def main():
    registry, inv = load_inputs()
    check_hard_pins(registry)
    pool, lex_core, excluded = build_pools(inv)

    seeds = []
    for i in range(1, N_RANDOM + 1):
        seeds.append(gen_seed(f"RND-{i:03d}", "random", pool, lex_core))
    for i in range(1, N_LEXICON + 1):
        seeds.append(gen_seed(f"LEX-{i:03d}", "lexicon", pool, lex_core))
    formulae = list(FORMULAE)
    k = 0
    for i in range(1, N_CRIB + 1):
        f = formulae[(i - 1) % len(formulae)]  # 8 seeds per formula
        k += 1
        seeds.append(gen_seed(f"CRB-{i:03d}", "crib", pool, lex_core, formula=f))

    errs = validate(seeds, pool, lex_core, excluded)
    if errs:
        for e in errs[:20]:
            print(f"VALIDATION FAIL: {e}", file=sys.stderr)
        raise SystemExit(f"ABORT: {len(errs)} validation errors")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    seeds_doc = {"meta": {"master_seed": MASTER_SEED, "n_seeds": len(seeds),
                          "composition": {"random": N_RANDOM, "lexicon": N_LEXICON,
                                          "crib": N_CRIB},
                          "r5005_contact": "none",
                          "key_model": "v1[g] full 96-cell initial key + v2[67] "
                                       "polyvalence (solver-cell/solver.py compatible)"},
                 "seeds": seeds}
    (OUT_DIR / "seeds.json").write_text(
        json.dumps(seeds_doc, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    (OUT_DIR / "priors-manifest.json").write_text(
        json.dumps(build_manifest(pool, lex_core, excluded, registry, inv),
                   ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")

    # ---- composition stats ----
    by_cls = Counter(s["class"] for s in seeds)
    soft_rate = Counter()
    soft_n = Counter()
    for s in seeds:
        soft_n[s["class"]] += 1
        for c in s["soft_applied"]:
            soft_rate[(s["class"], c)] += 1
    alias_means = {}
    for cls in ("random", "lexicon", "crib"):
        hs = [s["alias_counts"] for s in seeds if s["class"] == cls]
        alias_means[cls] = sum(len(h) for h in hs) / len(hs)
    print(f"seeds: {len(seeds)} {dict(by_cls)}")
    print(f"validation: PASS ({len(errs)} errors)")
    print("soft-prior application rate by class:")
    for cls in ("random", "lexicon", "crib"):
        cells = sorted({c for (cl, c) in soft_rate if cl == cls})
        rates = {c: round(soft_rate[(cls, c)] / soft_n[cls], 2) for c in cells}
        print(f"  {cls}: {rates}")
    print(f"mean distinct values/seed: {alias_means}")
    print(f"67 polyvalence v1 split: {Counter(s['v1']['67'] for s in seeds)}")
    print(f"wrote: {OUT_DIR/'seeds.json'}")
    print(f"wrote: {OUT_DIR/'priors-manifest.json'}")


if __name__ == "__main__":
    main()
