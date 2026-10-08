"""Analysis 2: genre-matched (Nesselrode v8) sensitivity, coarse-class variants,
independent validation of reconstructor §b proposal sets, 94=ne variant,
and function-word-centroid priors for uncovered syllables."""
import sys, re, json, math, os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
DATA = os.path.join(LANE, "data")
CORPUS = os.path.join(LANE, "code", "side-period", "corpus")
sys.path.insert(0, os.path.join(LANE, "code", "side-keyhunt"))
from build_syll_model import syllabify

WORD_RE = re.compile(r"[a-zàâäéèêëiîïoôöuùûüyçœæ]+")
APOS = re.compile("['’`]")
IDENTIFIED = {"11": "la", "70": "pre", "82": "m", "34": "i", "29": "er",
              "40": "e", "46": "que", "87": "ce", "64": "qui", "96": "par",
              "59": "est", "77": "le"}

def load_pairs():
    base = json.load(open(os.path.join(DATA, "upstream-offsets.json")))
    off = dict(base); off["a5_03"] = 0
    pairs = []
    for line in open(os.path.join(DATA, "upstream-ct_R5005.txt")):
        line = line.strip()
        if not line: continue
        lid, digits = line.split(); digits = re.sub(r"\D", "", digits)
        o = off[lid]
        pairs += [digits[i:i+2] for i in range(o, len(digits)-1, 2)]
    return pairs

def v8_counts(cache):
    if os.path.exists(cache):
        return json.load(open(cache))
    syl = Counter(); word = Counter(); nw = 0
    text = open(f"{CORPUS}/nesselrode-v8.txt", encoding="utf-8", errors="replace").read().lower()
    text = APOS.sub(" ", text)
    for m in WORD_RE.finditer(text):
        w = m.group(0); nw += 1; word[w] += 1
        for s in syllabify(w): syl[s] += 1
    out = {"syll": dict(syl), "word": dict(word), "n_words": nw,
           "n_syll": sum(syl.values())}
    json.dump(out, open(cache, "w")); return out

def main():
    pairs = load_pairs(); N = len(pairs)
    groups = sorted(set(pairs)); freq = Counter(pairs)
    gi = {g: i for i, g in enumerate(groups)}
    pre = defaultdict(Counter); suc = defaultdict(Counter)
    for a, b in zip(pairs[:-1], pairs[1:]):
        suc[a][b] += 1; pre[b][a] += 1
    def vec(g):
        v = [0.0]*(2*96)
        for h, c in pre[g].items(): v[gi[h]] = c
        for h, c in suc[g].items(): v[96+gi[h]] = c
        return v
    V = {g: vec(g) for g in groups}
    def cos(a, b):
        va, vb = V[a], V[b]
        na = sum(x*x for x in va)**0.5; nb = sum(x*x for x in vb)**0.5
        return sum(x*y for x, y in zip(va, vb))/(na*nb) if na and nb else 0.0
    phase = json.load(open(os.path.join(LANE, "code", "crowd4", "phase_map_repaired.json")))
    MEAN = N/96.0

    # ---- A. v8-only genre-matched rates ----
    v8 = v8_counts(os.path.join(HERE, "v8_counts.json"))
    S8 = v8["n_syll"]; syl8 = v8["syll"]; word8 = v8["word"]
    print(f"v8: {v8['n_words']:,} words, {S8:,} syllables")
    cmp14 = json.load(open(os.path.join(HERE, "corpus_counts.json")))
    S14 = cmp14["n_syllables"]; syl14 = cmp14["syllable_counts"]; word14 = cmp14["word_counts"]
    print(f"\n{'syl':6s} {'v8_rate':>8s} {'mix14_rate':>10s}  (genre drift check)")
    for s in ["de","le","la","en","ne","les","te","et","re","que","qui","ce","par","est","ou","on","nous","dans","pas","tout","ils","elle","son","sa","aux","des","une","pour"]:
        r8 = syl8.get(s, 0)/S8; r14 = syl14.get(s, 0)/S14
        flag = " <<<" if abs(r8-r14) > 0.15*max(r8, r14, 1e-9) and max(r8, r14) > 0.003 else ""
        print(f"{s:6s} {r8:8.4f} {r14:10.4f}{flag}")

    # ---- B. v8 deficit table for identified values (coarse bundles) ----
    # bundles: cipher-plausible coarse classes for each identified value
    BUNDLES = {
        "11": (["la"], "syl"), "70": (["pre", "pré"], "syl"),
        "82": (["m"], "word-letter"), "34": (["i"], "word-letter"),
        "29": (["er", "re", "é"], "syl"), "40": (["e", "é", "è", "ê"], "syl"),
        "46": (["que"], "word+qu"), "87": (["ce", "se"], "syl"),
        "64": (["qui"], "word"), "96": (["par"], "syl"),
        "59": (["est"], "syl"), "77": (["le"], "syl"),
    }
    def bundle_rate(items, kind, syl, word, S):
        if kind == "word": return word.get(items[0], 0)/S
        if kind == "word+qu": return (word.get("que", 0)+word.get("qu", 0))/S
        if kind == "word-letter": return word.get(items[0], 0)/S
        return sum(syl.get(x, 0) for x in items)/S
    print(f"\n{'grp':4s} {'val':4s} {'bundle':22s} {'obs':>4s} {'v8_exp':>6s} {'mix_exp':>7s} {'v8_def':>7s} {'v8_z':>6s}")
    v8def = {}
    for g, val in IDENTIFIED.items():
        items, kind = BUNDLES[g]
        r8 = bundle_rate(items, kind, syl8, word8, S8)
        r14 = bundle_rate(items, kind, syl14, word14, S14)
        e8, e14 = r8*N, r14*N
        d8 = e8 - freq[g]
        z8 = (freq[g]-e8)/math.sqrt(e8*(1-r8)) if e8 > 0 else 0
        v8def[val] = (d8, z8)
        print(f"{g:4s} {val:4s} {'+'.join(items):22s} {freq[g]:4d} {e8:6.1f} {e14:7.1f} {d8:+7.1f} {z8:+6.2f}")
    json.dump({k: {"deficit_occ": d, "z": z} for k, (d, z) in v8def.items()},
              open(os.path.join(HERE, "v8_deficit.json"), "w"), indent=1)

    # ---- C. independent validation of reconstructor §b proposal sets ----
    PROPOSED = [("33","86"),("48","94"),("47","87"),("52","59"),("76","78"),
                ("12","32"),("82","42"),("17","67"),("24","79"),("06","44"),
                ("40","80"),("85","87"),("66","86")]
    print("\n§b set validation (independent sims; mutual-NN rank among 96 groups):")
    print(f"{'set':10s} {'sim':>6s} {'mutual?':>8s} {'r_ab':>5s} {'r_ba':>5s} {'phase':>7s} {'n_a':>4s} {'n_b':>4s}")
    setval = {}
    for a, b in PROPOSED:
        s = cos(a, b)
        ra = sorted(groups, key=lambda g: -cos(a, g)).index(b) + 1
        rb = sorted(groups, key=lambda g: -cos(b, g)).index(a) + 1
        mut = "YES" if ra == 1 and rb == 1 else ("~" if ra <= 3 and rb <= 3 else "no")
        setval[f"{a},{b}"] = {"sim": round(s,3), "rank_ab": ra, "rank_ba": rb,
                              "mutual": mut, "phase": f"{phase.get(a)}/{phase.get(b)}",
                              "n": [freq[a], freq[b]]}
        print(f"{a+','+b:10s} {s:6.3f} {mut:>8s} {ra:5d} {rb:5d} {phase.get(a)}/{phase.get(b):>5s} {freq[a]:4d} {freq[b]:4d}")
    json.dump(setval, open(os.path.join(HERE, "set_validation.json"), "w"), indent=1)

    # ---- D. 94=ne variant: rank unidentified by sim to 94 ----
    unid = [g for g in groups if g not in IDENTIFIED]
    r94 = sorted(((cos("94", g), g) for g in unid), key=lambda x: -x[0])
    print("\n94=ne variant — unidentified groups ranked by sim to 94 (n, phase):")
    for s, g in r94[:10]:
        print(f"  {g}: sim={s:.3f} n={freq[g]} phase={phase.get(g)}")
    json.dump([{"group": g, "sim": round(s,3), "n": freq[g], "phase": phase.get(g)}
               for s, g in r94[:15]], open(os.path.join(HERE, "ne_candidates.json"), "w"), indent=1)

    # ---- E. function-word centroid priors for uncovered top syllables ----
    FW = ["11", "87", "46", "64", "96", "77", "94"]  # la ce que qui par le ne(prov-strong)
    cen = [0.0]*(2*96)
    for g in FW:
        v = V[g]
        for i in range(2*96): cen[i] += v[i]
    nc = sum(x*x for x in cen)**0.5; cen = [x/nc for x in cen]
    def cosc(g):
        v = V[g]; nv = sum(x*x for x in v)**0.5
        return sum(x*y for x, y in zip(cen, v))/nv if nv else 0.0
    frank = sorted(((cosc(g), g) for g in unid), key=lambda x: -x[0])
    print("\nFunction-word centroid ranking (top 20 unidentified):")
    for s, g in frank[:20]:
        print(f"  {g}: sim={s:.3f} n={freq[g]} phase={phase.get(g)}")
    json.dump([{"group": g, "sim": round(s,3), "n": freq[g], "phase": phase.get(g)}
               for s, g in frank],
              open(os.path.join(HERE, "fw_centroid_ranking.json"), "w"), indent=1)

    # uncovered-syllable cell-count priors (from deficit_table.json)
    dtab = json.load(open(os.path.join(HERE, "deficit_table.json")))
    print("\nUncovered-syllable missing-cell priors:")
    for r in dtab["rows"]:
        if r["flag"] and not r["cells"]:
            print(f"  {r['syllable']:5s}: deficit {r['deficit_occ']:+.1f} occ -> "
                  f"{r['missing_cells']:.1f} cells | fw-centroid top3: " +
                  ", ".join(f"{g}(n={freq[g]})" for _, g in frank[:3]))

if __name__ == "__main__":
    main()
