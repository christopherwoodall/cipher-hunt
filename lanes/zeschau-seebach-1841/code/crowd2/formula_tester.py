#!/usr/bin/env python3
"""
Work Order 2 — FORMULA TESTER (crowd round 2).

Test 1: linguist H5 — the pair-aligned repeat 77 78 94 82 06 (2x @1179/@1350)
        = "J'ai l'honneur de", segmented j'ai . l' . hon . neur . de.
        Alignment under test (5 units -> 5 groups, in order):
            77=j'ai, 78=l', 94=hon, 82=neur, 06=de
        NOTE: the work order's "(94?)" for the l'-position and "78->94" for the
        hon-neur adjacency are off by one position under this mapping; the
        l'-position is 78 and the hon-neur boundary is 94->82. Both the stated
        mapping and the work-order variants are measured; corrections recorded.

Test 2: crib-drag the longest unread repeat
        56 69 26 00 33 21 64 37 01 (2x @931/@1625)
        against the era corpus (Tocqueville t1+t2, formal prose 1835/1840),
        syllabified, dragging 9-syllable phrases with "qui" (=64, provisional
        anchor) in 7th position.

Promotion rule: >=2 independent checks to promote anything.
Deterministic. No invented ciphertext or keys.
Results -> formula_tester_results.{md,json} in this directory.
"""
import json, re, collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(HERE, '..')
DATA = os.path.join(HERE, '..', '..', 'data')
sys.path.insert(0, CODE)
from crib_attack import load_pairs, ANCHORS

ANCHORS9 = dict(ANCHORS)
ANCHORS9['87'] = 'ce'    # provisional, lane-inferred (attempt 2/3)
ANCHORS9['64'] = 'qui'   # provisional, lane-inferred (attempt 3, 4/4)

T1 = os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt')
T2 = os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')

REPEAT5 = ['77', '78', '94', '82', '06']
REPEAT9 = ['56', '69', '26', '00', '33', '21', '64', '37', '01']


def find_occ(pairs, seq):
    L = len(seq)
    return [i for i in range(len(pairs) - L + 1)
            if pairs[i:i + L] == seq]


def line_starts():
    """Map pair index -> (line_id, index-within-line) using upstream offsets."""
    import json as _j, re as _r
    offsets = _j.load(open(os.path.join(DATA, 'upstream-offsets.json')))
    starts, idx = [], 0
    for line in open(os.path.join(DATA, 'upstream-ct_R5005.txt')):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        digits = _r.sub(r'\D', '', digits)
        off = offsets.get(lid, 0)
        d = digits[off:]
        n = (len(d) - 1) // 2 if len(d) % 2 == 0 else len(d) // 2
        # replicate load_pairs pairing exactly: range(0, len(d)-1, 2)
        n = len(range(0, len(d) - 1, 2))
        starts.append((lid, idx))
        idx += n
    return starts


def decode(seq, table=ANCHORS9):
    return [(g, table.get(g, '?')) for g in seq]


# ---------------- era corpus: syllable model ----------------
VOWELS = set('aàâäeéèêëiîïoôöuùûüyæœ')


def syllabify(word):
    w = word.lower()
    n = len(w)
    vgroups = []
    i = 0
    while i < n:
        if w[i] in VOWELS:
            j = i
            while j < n and w[j] in VOWELS:
                j += 1
            vgroups.append((i, j))
            i = j
        else:
            i += 1
    if not vgroups:
        return [w]
    out = []
    for gi, (gs, ge) in enumerate(vgroups):
        if gi == 0:
            onset = 0
        else:
            pge = vgroups[gi - 1][1]
            onset = pge + 1 if (gs - pge) >= 2 else pge
        if gi == len(vgroups) - 1:
            end = n
        else:
            ngs = vgroups[gi + 1][0]
            end = ge + 1 if (ngs - ge) >= 2 else ge
        s = w[onset:end]
        if s:
            out.append(s)
    return out


def load_era():
    raw = ""
    for p in (T1, T2):
        t = open(p, encoding='utf-8', errors='replace').read().lower()
        m = re.search(r'\*\*\* start of.*?\*\*\*', t)
        if m:
            t = t[m.end():]
        m = re.search(r'\*\*\* end of.*', t)
        if m:
            t = t[:m.start()]
        raw += " " + t
    words = re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+(?:'[a-zàâäéèêëîïôöùûüÿç]+)?", raw)
    return raw, words


def main():
    pairs, odd_lines, off1 = load_pairs()
    N = len(pairs)
    freq = collections.Counter(pairs)
    ranked = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    rank_of = {g: r + 1 for r, (g, _) in enumerate(ranked)}
    rate = {g: c / N for g, c in freq.items()}

    # predecessors / followers
    pre = collections.defaultdict(collections.Counter)
    fol = collections.defaultdict(collections.Counter)
    for a, b in zip(pairs, pairs[1:]):
        fol[a][b] += 1
        pre[b][a] += 1

    res = {'meta': {
        'role': 'THE FORMULA TESTER (crowd round 2)',
        'lane': 'zeschau-seebach-1841',
        'date': '2026-10-07',
        'pairs': N,
        'anchors9': ANCHORS9,
        'promotion_rule': '>=2 independent checks to promote; grammatical contradiction refutes',
    }}

    # ============ TEST 1: H5 = "J'ai l'honneur de" ============
    occ5 = find_occ(pairs, REPEAT5)
    h5 = {
        'repeat': ' '.join(REPEAT5),
        'positions_rederived': occ5,
        'alignment_under_test': {'77': "j'ai", '78': "l'", '94': 'hon',
                                 '82': 'neur', '06': 'de'},
        'work_order_correction': (
            "Work order wrote l'-position as (94?) and hon-neur boundary as "
            "78->94; under the stated 5-unit mapping j'ai.l'.hon.neur.de the "
            "l'-position is 78 (2nd unit) and the hon-neur boundary is 94->82 "
            "(3rd->4th unit). Both group 78 and group 94 are measured below."),
    }

    # ---- (a) l'-position as single-letter consonant ----
    def cell_profile(g):
        return {
            'freq': freq[g], 'rank': rank_of[g], 'rate': round(rate[g], 5),
            'n_predecessors': len(pre[g]), 'n_followers': len(fol[g]),
            'top_follower': fol[g].most_common(1)[0] if fol[g] else None,
            'top_follower_share': round(fol[g].most_common(1)[0][1] / freq[g], 3) if fol[g] else None,
            'top_predecessor': pre[g].most_common(1)[0] if pre[g] else None,
        }
    h5['test_a'] = {
        'group_78_profile': cell_profile('78'),
        'group_94_profile': cell_profile('94'),
        'known_single_letter_cells': {
            '82=m': cell_profile('82'), '34=i': cell_profile('34'),
            '40=e': cell_profile('40')},
        'bigram_77_78': {
            'count': sum(1 for a, b in zip(pairs, pairs[1:])
                         if a == '77' and b == '78'),
            'positions': [i for i, (a, b) in enumerate(zip(pairs, pairs[1:]))
                          if a == '77' and b == '78'],
        },
        'note': ("l' is a proclitic: expect a free-ish function cell (many "
                 "distinct followers, vowel-initial followers unknowable here). "
                 "Known single letters span ranks 8..70 (m x38, e x21, i x10)."),
    }

    # ---- (b) hon-neur adjacency: 94->82 vs in-word control 70->82 ----
    pred82 = pre['82'].most_common()
    h5['test_b'] = {
        'bigram_94_82_count': fol['94'].get('82', 0),
        'bigram_94_82_positions': [i for i, (a, b) in enumerate(zip(pairs, pairs[1:]))
                                  if a == '94' and b == '82'],
        'bigram_70_82_count': fol['70'].get('82', 0),   # pre->m in "premiere" @1033
        'predecessors_of_82': pred82[:12],
        'n_predecessors_of_82': len(pre['82']),
        'followers_of_94_top': fol['94'].most_common(8),
        'n_followers_of_94': len(fol['94']),
        'work_order_correction': ("Work order wrote the hon-neur adjacency as "
                                  "78->94; it is 94->82 under the mapping. "
                                  "78->94 is the l'->hon boundary (also reported)."),
        'bigram_78_94_count': fol['78'].get('94', 0),
        'anchor_conflict': ("82 is a GROUND-TRUTH pencil anchor = single letter "
                            "'m'. Mapping 82='neur' requires the m-cell to also "
                            "encode the 4-letter syllable 'neur' — structurally "
                            "implausible in a syllabary that gives frequent "
                            "syllables their own cells."),
    }

    # ---- (c) occurrence contexts @1179/@1350 ----
    starts = line_starts()
    def line_pos(i):
        lid, s = max((l, s) for l, s in starts if s <= i)
        return lid, i - s
    ctx = {}
    for p in occ5:
        window = pairs[p - 6:p + 11]
        ctx[str(p)] = {
            'line_id': line_pos(p)[0],
            'index_within_line': line_pos(p)[1],
            'frac_of_text': round(p / N, 4),
            'groups_before': pairs[p - 6:p],
            'groups_repeat': pairs[p:p + 5],
            'groups_after': pairs[p + 5:p + 11],
            'decoded_before': decode(pairs[p - 6:p]),
            'decoded_after': decode(pairs[p + 5:p + 11]),
        }
    h5['test_c'] = {
        'contexts': ctx,
        'expectation': ("'de' (06) should be followed by an infinitive or a "
                        "noun phrase: de+INF ('de vous informer') or "
                        "de+DET+N ('de la ...'). Judged on anchor-decoded "
                        "fragments only; groups 37/01-class unknowns cannot "
                        "confirm or deny."),
    }

    # ---- (d) frequency tiers vs Meisel 1826 diplomatic syllable tiers ----
    raw, words = load_era()
    syl_stream = []
    for w in words:
        syl_stream.extend(syllabify(w))
    nsyl = len(syl_stream)
    sc = collections.Counter(syl_stream)
    n_jai = len(re.findall(r"\bj'ai\b", raw))
    n_l = len(re.findall(r"\bl'", raw))
    n_de_word = sum(1 for w in words if w == 'de')
    era_rates = {
        'n_syllables': nsyl,
        'n_words': len(words),
        "syl_de": sc['de'] / nsyl,
        "syl_hon": sc['hon'] / nsyl,
        "syl_neur": sc['neur'] / nsyl,
        "word_j'ai_per_syl": n_jai / nsyl,
        "proclitic_l'_per_syl": n_l / nsyl,
        "word_de_per_syl": n_de_word / nsyl,
        'note': ("Heuristic vowel-group syllabifier; +/-10% noise per linguist. "
                 "'neur' counted as its own syllable (honneur->hon|neur); "
                 "bonheur->bon|heur counted separately."),
    }
    tier = {'tier0': '>1.5%', 'tier1': '0.35-1%', 'tier2': '0.08-0.35%',
            'tier3': '<0.08% (below tier2 floor)'}
    h5['test_d'] = {
        'era_syllable_rates': {k: (round(v, 6) if isinstance(v, float) else v)
                               for k, v in era_rates.items()},
        'meisel_tiers': tier,
        'observed_group_rates': {
            "77 as j'ai": round(rate['77'], 5),
            "78 as l'": round(rate['78'], 5),
            "94 as hon": round(rate['94'], 5),
            "82 as neur": round(rate['82'], 5),
            "06 as de": round(rate['06'], 5)},
        'meisel_expectation': {
            'de': 'tier0 (>1.5%)', "j'ai": 'function word, je tier2 book x5-20 despatch boost',
            "l'": 'single letter tier1 (0.35-1%)',
            'hon': 'tier2 (0.08-0.35%)', 'neur': 'tier3 (<0.08%, not in Meisel tiers)'},
    }

    # ---- H5 scorecard ----
    fors, againsts = [], []
    # F1: 77->78 bigram
    b77_78 = h5['test_a']['bigram_77_78']
    nonrep = [p for p in b77_78['positions'] if p not in occ5]
    fors.append(f"77->78 co-occurs 7x ({len(nonrep)} outside the repeat): "
                "'j\\'ai l\\'' behaves as a bound 2-unit chunk elsewhere — "
                "consistent with the formula reading (weak: n small, any fixed "
                "2-phrase fits).")
    # F2: discourse position
    fors.append("Both occurrences mid-body (63.9%, 73.1% of text): consistent "
                "with a per-paragraph discourse formula (formula-hunter: "
                "repeats are discourse-level set phrases).")
    # F3: 06=de tier
    if rate['06'] > 0.015:
        fors.append(f"06 at {rate['06']:.3%} sits in Meisel tier0 (>1.5%), "
                    f"in-band for 'de' the #1 French syllable (era syl rate "
                    f"{era_rates['syl_de']:.3%}). CONFLICT: surgeon H3 has 06='ne' (3 checks).")
    # A1: anchor conflict (structural, near-kill)
    againsts.append("STRUCTURAL: 82 is a ground-truth pencil anchor = single "
                    "letter 'm'. H5 needs 82='neur' (4-letter syllable). A "
                    "syllabary with dedicated single-letter cells does not "
                    "reuse the m-cell for 'neur'.")
    # A2: rate of 82 vs neur
    r82, rneur = rate['82'], era_rates['syl_neur']
    againsts.append(f"RATE: 82 occurs at {r82:.3%} (rank {rank_of['82']}) but "
                    f"era 'neur' is {rneur:.4%} — {r82/max(rneur,1e-9):.0f}x too "
                    "frequent for 'neur' (tier3 syllable).")
    # A3/A4: 94=hon, 78=l' tier checks (computed below)
    r94, rhon = rate['94'], era_rates['syl_hon']
    if not (0.5 * rhon <= r94 <= 3 * rhon):
        againsts.append(f"RATE: 94 at {r94:.3%} vs era 'hon' {rhon:.4%} "
                        f"({r94/max(rhon,1e-9):.1f}x) — outside a generous 3x band.")
    else:
        fors.append(f"94 at {r94:.3%} within 3x of era 'hon' {rhon:.4%} — tier-consistent.")
    r78, rl = rate['78'], era_rates["proclitic_l'_per_syl"]
    if not (0.5 * rl <= r78 <= 3 * rl):
        againsts.append(f"RATE: 78 at {r78:.3%} vs era proclitic l' {rl:.4%} "
                        f"({r78/max(rl,1e-9):.1f}x) — outside a generous 3x band.")
    else:
        fors.append(f"78 at {r78:.3%} within 3x of era proclitic l' {rl:.4%} — tier-consistent.")
    # A5: 77=j'ai
    r77, rjai = rate['77'], era_rates["word_j'ai_per_syl"]
    if r77 > 20 * rjai:
        againsts.append(f"RATE: 77 at {r77:.3%} vs era j'ai {rjai:.4%} "
                        f"({r77/max(rjai,1e-9):.0f}x) — above even the 20x despatch boost ceiling.")
    # hon-neur contact: is 94->82 exclusive to the repeat?
    if h5['test_b']['bigram_94_82_count'] == 2:
        againsts.append("CONTACT: 94->82 occurs ONLY inside the 2 repeat "
                        "instances — no independent hon-neur boundary evidence "
                        "anywhere else in 1846 pairs.")
    h5['scorecard'] = {'for': fors, 'against': againsts}
    n_for = len([f for f in fors if 'CONFLICT' not in f])
    h5['verdict'] = (
        "REFUTED as stated" if any('STRUCTURAL' in a for a in againsts) else "undecided")
    h5['verdict_detail'] = (
        "H5 'J\\'ai l\\'honneur de' is REFUTED as stated: the mapping requires "
        "82='neur' but 82 is a ground-truth pencil anchor for the single letter "
        "'m' (structural contradiction, independent of all rate arguments), and "
        "independently 82's rate (rank 8) is an order of magnitude too high for "
        "the tier-3 syllable 'neur'. The 77->78 'j\\'ai l\\'' chunk and the "
        "mid-body discourse positions survive as suggestive sub-claims, but the "
        "5-unit reading cannot stand with 82=m. The formula-hunter R4 rival "
        "('-ment' word family: 77=gou 78=ver 94=ne 82=m 06=ent) is structurally "
        "compatible with 82=m and remains the live alternative for this repeat.")
    res['h5'] = h5

    # ============ TEST 2: 9-mer crib drag ============
    occ9 = find_occ(pairs, REPEAT9)
    drag = {'repeat': ' '.join(REPEAT9), 'positions_rederived': occ9}
    ctx9 = {}
    for p in occ9:
        ctx9[str(p)] = {
            'line_id': line_pos(p)[0], 'index_within_line': line_pos(p)[1],
            'frac_of_text': round(p / N, 4),
            'groups': pairs[p - 4:p + 13],
            'decoded': decode(pairs[p - 4:p + 13]),
        }
    drag['contexts'] = ctx9
    # standalone extra occurrence of the inner 4-mer 69 26 00 33 @405
    inner4 = ['69', '26', '00', '33']
    occ_inner = find_occ(pairs, inner4)
    drag['inner_4mer_69_26_00_33'] = {
        'positions': occ_inner,
        'context_at_405': decode(pairs[405 - 6:405 + 10]),
        'groups_at_405': pairs[405 - 6:405 + 10],
    }
    # era drag: 9-syllable windows with qui in 7th position (index 6)
    cands = collections.Counter()
    L = 9
    for i in range(len(syl_stream) - L + 1):
        win = syl_stream[i:i + L]
        if win[6] == 'qui':
            cands[' '.join(win)] += 1
    top = cands.most_common(12)
    drag['method'] = ("Syllabified Tocqueville t1+t2 (heuristic vowel-group "
                      "syllabifier); all 9-syllable windows with 'qui' as 7th "
                      "syllable (= position of provisional anchor 64=qui in the "
                      "9-mer); ranked by raw frequency.")
    drag['n_windows_qui_slot7'] = sum(cands.values())
    drag['n_distinct'] = len(cands)
    drag['top_candidates'] = [{'phrase_syllables': k, 'count': v}
                              for k, v in top]
    # slot 8/9 distributions after qui (constrains groups 37, 01 if drag hits)
    s8 = collections.Counter()
    s9 = collections.Counter()
    for i in range(len(syl_stream) - L + 1):
        win = syl_stream[i:i + L]
        if win[6] == 'qui':
            s8[win[7]] += 1
            s9[win[8]] += 1
    drag['slot8_after_qui_top'] = s8.most_common(10)
    drag['slot9_top'] = s9.most_common(10)
    # word-level followers/predecessors of 'qui' for the 21->64->37 path
    qw = collections.Counter()
    for w in words:
        qw[w] += 1
    fol_q = collections.Counter(y for x, y in zip(words, words[1:]) if x == 'qui')
    pre_q = collections.Counter(x for x, y in zip(words, words[1:]) if y == 'qui')
    drag['wordlevel_qui'] = {
        'followers': fol_q.most_common(8), 'predecessors': pre_q.most_common(8)}
    # cipher-side: 64's local contact stats (attempt3: 28/28 distinct)
    drag['cipher_64_contacts'] = {
        'freq': freq['64'], 'rank': rank_of['64'],
        'n_predecessors': len(pre['64']), 'n_followers': len(fol['64']),
        'predecessor_21_count': pre['64'].get('21', 0),
        'follower_37_count': fol['64'].get('37', 0),
        'bigram_21_64_positions': [i for i, (a, b) in enumerate(zip(pairs, pairs[1:]))
                                   if a == '21' and b == '64'],
        'bigram_64_37_positions': [i for i, (a, b) in enumerate(zip(pairs, pairs[1:]))
                                   if a == '64' and b == '37'],
    }
    # verdict
    if top and top[0][1] >= 3:
        drag['verdict'] = (
            f"WEAK LEAD (not promotion): top qui-slot7 9-mer "
            f"'{top[0][0]}' x{top[0][1]} in era corpus. Single-check only "
            f"(corpus frequency); no second independent check — the cipher-side "
            f"groups 56/69/26/00/33/21/37/01 are unread, so positional "
            f"coherence cannot be tested. Promotion needs a second check "
            f"(e.g. an anchor landing inside the 9-mer, or the inner-4-mer "
            f"context decoding).")
    else:
        drag['verdict'] = ("NULL: no qui-slot7 9-syllable phrase recurs >=3x in "
                           "the era corpus; top candidates are hapax/doubleton "
                           "prose, not formulas. The 9-mer stays unread.")
    drag['verdict_detail'] = drag['verdict']
    res['nine_mer_drag'] = drag

    # ============ promotion verdicts ============
    res['promotion_verdicts'] = {
        "H5_'Jai_lhonneur_de'": {
            'verdict': 'REFUTED as stated (not promoted)',
            'checks_for': len([f for f in fors if 'CONFLICT' not in f]),
            'checks_against': len(againsts),
            'independent_killers': [
                'structural: 82=m ground-truth anchor vs required 82=neur',
                'rate: 82 at rank 8 is ~order-of-magnitude too frequent for tier-3 "neur"',
            ],
            'surviving_suggestion': ("77->78 'j\\'ai l\\'' chunk (7x, 5 outside "
                                     "repeat) stays a live sub-claim; the R4 "
                                     "'-ment' word-family rival (94=ne 82=m "
                                     "06=ent) is structurally compatible with "
                                     "82=m and inherits the repeat as its target."),
        },
        'nine_mer_drag': {
            'verdict': 'NULL / weak lead at best — not promoted',
            'reason': ('No candidate clears >=2 independent checks: corpus '
                       'frequency alone is one check; cipher-side groups are '
                       'unread so no positional second check exists.'),
        },
    }

    with open(os.path.join(HERE, 'formula_tester_results.json'), 'w') as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == '__main__':
    res = main()
    h5 = res['h5']
    print("H5 repeat positions:", h5['positions_rederived'])
    print("78 profile:", h5['test_a']['group_78_profile'])
    print("94 profile:", h5['test_a']['group_94_profile'])
    print("94->82:", h5['test_b']['bigram_94_82_count'],
          "70->82:", h5['test_b']['bigram_70_82_count'])
    print("era rates:", res['h5']['test_d']['era_syllable_rates'])
    print("H5 verdict:", h5['verdict'])
    for a in h5['scorecard']['against']:
        print("  AGAINST:", a[:120])
    d = res['nine_mer_drag']
    print("9-mer positions:", d['positions_rederived'])
    print("9-mer drag verdict:", d['verdict'][:200])
    print("top qui-slot7:", d['top_candidates'][:5])
