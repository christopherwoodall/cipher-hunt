#!/usr/bin/env python3
"""SLIDER pass 1 — Seebach side-path crib-bootstrap slide.

Implements code/sidepath/prereg_pass1.md AS AMENDED by prereg_pass1_v11.md
(frame correction only). Frozen: weights, thresholds, acceptance criteria,
window inventory (frame-corrected positions), candidate inventory, rule names.
Nothing here tunes to data; the control (3 shuffles, seed 1841) gates all claims.

Pipeline:
  canonical parse (load_pairs-identical) -> windows (a..f) -> candidates
  (ERA-VOCAB + SURVIVING FORMULAE + 1841 COLLOCATIONS) -> fuzzy scoring ->
  slide_pass1.json. Same pipeline rerun on 3 shuffled controls.
"""
import json, math, os, random, re, sys, unicodedata
from collections import Counter
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(LANE, 'data')
CROWD3 = os.path.join(LANE, 'code', 'crowd3')

# ---------------- 1. canonical parse (identical to code/crib_attack.py::load_pairs)
def load_pairs():
    offsets = json.load(open(os.path.join(DATA, 'upstream-offsets.json')))
    pairs = []
    for line in open(os.path.join(DATA, 'upstream-ct_R5005.txt')):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        digits = re.sub(r'\D', '', digits)
        d = digits[offsets.get(lid, 0):]
        for i in range(0, len(d) - 1, 2):
            pairs.append(d[i:i + 2])
    return pairs

PAIRS = load_pairs()
assert len(PAIRS) == 1846, len(PAIRS)
assert len(set(PAIRS)) == 96, len(set(PAIRS))

# ---------------- 2. inventory (from skeleton.json — the side-path's applied ledger)
sk = json.load(open(os.path.join(HERE, 'skeleton.json')))
INV = sk['inventory']  # group -> {value, status}
BANNED = sk.get('not_applied', [])

# phonetic compatibility sets over the by-ear pronounced form.
# Primary = endorsed value; alternates = lane-attested polyvalence (R5, not contradictions).
COMPAT = {
    '11': {'la'},
    '70': {'pre'},
    '82': {'m'},
    '34': {'i', 'y'},
    '29': {'er'},
    '40': {'e'},
    '46': {'que'},
    '87': {'ce', 'se'},
    '64': {'qui'},
    '96': {'par'},
    '94': {'ne', 'n'},
    '62': {'on'},
    '78': {'me', 'm'},
    '52': {'pas'},
    '24': {'en', 'an'},   # 'an' via NASAL-VAR (by-ear nasal)
    '67': {'veu', 'veut', 'veux'},
}
ATT_ALT = {  # attested polyvalent alternates (R5) — logged UNCONFIRMED, never contradictions
    '52': {'so'},   # 'personne' = 93-52-94 @160
    '94': {'en'},   # 'en' islets @1168, @1575
}
RIVALS = {'94': {'re'}, '64': {'meme'}}  # live rivals -> RIVAL-NOTE, forced fail in pass 1
PRIMARY = {g: next(iter(v)) for g, v in COMPAT.items()}

# ---------------- 3. by-ear pronounced form + syllable units (phonetician R1-R11)
def fold_acc(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('\u0153', 'oe').replace('\u00e6', 'ae')

VOW = set('aeiouy')
CONS = set('bcdfghjklmnpqrstvwxz')
LIQ2 = {'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
        'tr', 'vr', 'ch', 'ph', 'th', 'gn', 'dj'}
LIQ3 = {'str', 'spr', 'scr', 'chr', 'phr'}

def pronounced(word):
    """By-ear pronounced letter string. Returns (pron, had_double)."""
    w = fold_acc(word.lower())
    w = w.replace("'", '').replace('\u2019', '')
    had_double = bool(re.search(r'([bcdfghjklmnpqrstvwxz])\1', w))
    w = re.sub(r'([bcdfghjklmnpqrstvwxz])\1', r'\1', w)  # R8 doubles spelled once
    if len(w) > 2 and w[-1] in 'sxz' and w[-2] in CONS:
        w = w[:-1]  # silent plural / final s,x,z (R3/R11)
    return w, had_double

def syllabify(p):
    """Maximal-onset unit spans tiling p; final mute -e is its own unit (R1)."""
    if not p:
        return []
    units = []
    core, tail = p, None
    if len(p) > 2 and p[-1] == 'e' and p[-2] in CONS:
        core, tail = p[:-1], (len(p) - 1, len(p))
    nuclei = [i for i, ch in enumerate(core) if ch in VOW]
    if not nuclei:
        units.append((0, len(core)))
    else:
        cuts = [0]
        for a, b in zip(nuclei, nuclei[1:]):
            between = core[a + 1:b]
            if len(between) <= 1:
                cuts.append(a + 1)
            else:
                nl = 1
                if between[-2:] in LIQ2:
                    nl = 2
                if len(between) >= 3 and between[-3:] in LIQ3:
                    nl = 3
                cuts.append(b - nl)
        cuts.append(len(core))
        units = list(zip(cuts, cuts[1:]))
    if tail:
        units.append(tail)
    return units

def is_mute_e_word(word, pron):
    return len(pron) > 2 and pron[-1] == 'e' and pron[-2] in CONS

# ---------------- 4. era vocabulary
def build_vocab():
    raw_counter = Counter()
    for f in ['gutenberg-30513-tocqueville-t1.txt', 'gutenberg-30514-tocqueville-t2.txt']:
        txt = open(os.path.join(DATA, f), encoding='utf-8', errors='replace').read().lower()
        raw_counter.update(re.findall(r"[a-z\u00e0\u00e2\u00e4\u00e9\u00e8\u00ea\u00eb\u00ee\u00ef\u00f4\u00f6\u00f9\u00fb\u00fc\u00ff\u00e7\u0153\u00e6']+", txt))
    vocab = {}   # word -> dict(pron, units, nunits, had_double, folded_hit)
    for w, n in raw_counter.items():
        if n < 3:
            continue
        if '\u00e7a' in w:  # 'ca' banned outright (prereg) — check pre-fold below
            pass
        p, hd = pronounced(w)
        if not p:
            continue
        u = syllabify(p)
        vocab[w] = {'pron': p, 'units': u, 'nunits': len(u), 'had_double': hd,
                    'mute_e': is_mute_e_word(w, p), 'count': n}
    return vocab, raw_counter

VOCAB, RAW_COUNTER = build_vocab()
FOLDED = {}
for w in VOCAB:
    FOLDED.setdefault(fold_acc(w), []).append(w)

def attested(word):
    """Era attestation: exact or era-orthography (folded) normalization. Returns (hit, via_fold)."""
    if word in VOCAB:
        return True, False
    if fold_acc(word) in FOLDED:
        return True, True
    return False, False

# ---------------- 5. phase map + boundary signal (segmenter, canonical frame)
cj = json.load(open(os.path.join(LANE, 'code', 'crowd', 'contactor_results.json')))
cs12 = cj['jaccard_clusters']['12']
A_, B_, C_ = (set(x['members']) for x in cs12[:3])
REST = set().union(*[set(x['members']) for x in cs12[3:]])
PHASE = {}
for g in A_:
    PHASE[g] = 'A'
for g in B_:
    PHASE[g] = 'B'
for g in C_:
    PHASE[g] = 'C'
for g in REST:
    PHASE[g] = 'R'
assert len(PHASE) == 96
assert PHASE['11'] == 'A' and PHASE['70'] == 'A' and PHASE['82'] == 'B'
assert PHASE['29'] == 'C' and PHASE['96'] == 'C' and PHASE['87'] == 'B'

seg = json.load(open(os.path.join(CROWD3, 'segmenter_results.json')))
BC = seg['boundary_confidence_STRUCT']  # len 1845: boundary between pair i and i+1
S_TOP = dict((e, v) for v, e in seg['struct_edge_model']['s_top_boundary'])
assert abs(S_TOP['R->C'] - 12.621) < 0.01 and abs(S_TOP['B->B'] - 12.531) < 0.01
BOUND_FAVOR = {'R->C', 'B->B'}

def edge_trans(pairs, i):
    """Phase transition at boundary between pair i and i+1."""
    return PHASE[pairs[i]] + '->' + PHASE[pairs[i + 1]]

def flank_conf(s, e):
    left = BC[s - 1] if s > 0 else 1.0
    right = BC[e] if e < len(BC) else 1.0
    return [left, right]

def bound_fit(pairs, s, e):
    fl = flank_conf(s, e)
    b_align = 0
    if s > 0 and edge_trans(pairs, s - 1) in BOUND_FAVOR:
        b_align += 1
    if e < len(BC) and edge_trans(pairs, e) in BOUND_FAVOR:
        b_align += 1
    b_cross = sum(1 for i in range(s, e) if edge_trans(pairs, i) in BOUND_FAVOR)
    v = sum(fl) / 2.0 + 0.25 * b_align - 0.50 * b_cross
    return max(0.0, min(1.0, v)), {'flank': fl, 'b_align': b_align, 'b_cross': b_cross}

# ---------------- 6. window inventory (frame-corrected per prereg v1.1)
def build_windows(pairs):
    wins = []
    # (a) 25 segmenter crib-drag targets — canonical frame already; verify byte-exact
    tgts = seg['crib_drag_targets_STRUCT']
    assert len(tgts) == 25
    for k, t in enumerate(tgts, 1):
        s, e = t['start_pair'], t['end_pair']
        gs = pairs[s:e + 1]
        assert gs == t['groups'], (k, gs, t['groups'])
        ph = ''.join(PHASE[g] for g in gs)
        assert ph == t['phases'], (k, ph, t['phases'])
        fl = flank_conf(s, e)
        assert all(abs(a - b) < 0.002 for a, b in zip(fl, t['flank_conf'])), (k, fl)
        wins.append({'id': 'W-S%02d' % k, 's': s, 'e': e, 'groups': gs,
                     'flank_conf': fl, 'phases': ph})
    # (b) W-47: pairs 146-157; sub-windows starts 146..153 x lengths 3,4,5 (24)
    # v1.1 correction: formula 87 64 96 47 46 sits at 148-152, not 150-154
    assert pairs[148:153] == ['87', '64', '96', '47', '46'], pairs[148:153]
    for st in range(146, 154):
        for ln in (3, 4, 5):
            s, e = st, st + ln - 1
            assert e <= 157
            wins.append({'id': 'W-47-s%d-l%d' % (st, ln), 's': s, 'e': e,
                         'groups': pairs[s:e + 1]})
    # (c) W-62B: 62->94 bigrams, +-3 pairs (v1.1: x8, reconciled with NOTES.md)
    b6294 = [i for i in range(len(pairs) - 1) if pairs[i] == '62' and pairs[i + 1] == '94']
    assert len(b6294) == 8, b6294
    for p in b6294:
        s, e = p - 3, p + 4
        wins.append({'id': 'W-62B-%d' % p, 's': s, 'e': e, 'groups': pairs[s:e + 1]})
    # (d) W-62C: remaining 62 positions, +-3, overlaps merged
    p62 = [i for i, g in enumerate(pairs) if g == '62']
    rest62 = [p for p in p62 if p not in b6294]
    assert len(p62) == 34 and len(rest62) == 26
    wins += merged_windows(pairs, rest62, 3, 'W-62C')
    # (e) W-24: all 52 24-positions, +-3, overlaps merged
    p24 = [i for i, g in enumerate(pairs) if g == '24']
    assert len(p24) == 52, len(p24)
    wins += merged_windows(pairs, p24, 3, 'W-24')
    # (f) W-52: all 27 52-positions, +-3, overlaps merged
    p52 = [i for i, g in enumerate(pairs) if g == '52']
    assert len(p52) == 27, len(p52)
    wins += merged_windows(pairs, p52, 3, 'W-52')
    return wins

def merged_windows(pairs, positions, rad, prefix):
    ivs = []
    for p in sorted(positions):
        s, e = max(0, p - rad), min(len(pairs) - 1, p + rad)
        if ivs and s <= ivs[-1][1] + 1:
            ivs[-1][1] = max(ivs[-1][1], e)
        else:
            ivs.append([s, e])
    return [{'id': '%s-%d' % (prefix, s), 's': s, 'e': e, 'groups': pairs[s:e + 1]}
            for s, e in ivs]

# ---------------- 7. alignment: partition pronounced letters into n blocks
def block_cut(block, units):
    """Score one pair-block against syllable units. 1.0/0.5/0.0 per prereg."""
    s, e = block
    for us, ue in units:
        if us <= s < ue:
            if s == us and e == ue:
                return 1.0
            if e <= ue:
                return 0.5   # SPLIT-PAIR: part of a syllable
            return 0.0       # straddles a syllable boundary
    return 0.0

def compositions(total, parts):
    """Yield all compositions of total into `parts` positive integers."""
    if parts == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - parts + 2):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest

ENUM_CAP = 60000

def align_candidate(pron, units, n, known_slots):
    """known_slots: list of (slot_idx, group). Returns best dict or None.
    best = max cut_fit alignment consistent with all known values."""
    L = len(pron)
    if L < n:
        return None
    # candidate spans per known slot: (a, b, kind) kind in primary/alt/rival
    opts = []
    for slot, g in known_slots:
        cand = []
        for key, kind in (('compat', 'primary'), ('alt', 'alt'), ('rival', 'rival')):
            sets = {'compat': COMPAT.get(g, set()), 'alt': ATT_ALT.get(g, set()),
                    'rival': RIVALS.get(g, set())}[key]
            for a in range(L):
                for b in range(a + 1, min(L, a + 6) + 1):
                    if pron[a:b] in sets:
                        cand.append((a, b, kind))
        if not cand:
            return None
        opts.append((slot, g, cand))
    best = None
    enum = [0]

    def full_cut(spans):
        cuts, idx = [], 0
        for (a, b) in spans:
            cuts.append(block_cut((a, b), units))
            idx += 1
        return sum(cuts) / len(cuts)

    if not opts:
        # unconstrained: enumerate all compositions
        for comp in compositions(L, n):
            enum[0] += 1
            if enum[0] > ENUM_CAP:
                break
            spans, a = [], 0
            for c in comp:
                spans.append((a, a + c))
                a += c
            cf = full_cut(spans)
            if best is None or cf > best['cut_fit']:
                best = {'cut_fit': cf, 'spans': spans, 'kinds': ['free'] * n}
                if cf == 1.0:
                    break
        return best

    # anchored: choose spans for known slots in order, then fill gaps
    slots = sorted(o[0] for o in opts)
    optmap = {o[0]: o for o in opts}

    # iterative enumeration over product of option lists with feasibility pruning
    opt_lists = [optmap[s] for s in slots]  # (slot, g, cand)
    # order slots; feasibility: span for slot s_i must leave >= slots between letters
    best_local = {'best': None}

    def feasible_prefix(chosen):
        # chosen: list of (slot, g, a, b, kind)
        for j, (slot, g, a, b, kind) in enumerate(chosen):
            before = slot  # pairs before this slot
            if a < before:  # need >=1 letter per earlier pair... (each >=1)
                # letters before a must cover `slot` pairs each >=1 -> a >= slot
                return False
            if j > 0:
                ps, pg, pa, pb, pk = chosen[j - 1]
                gap_pairs = slot - ps - 1
                if a - pb < gap_pairs:  # >=1 letter per gap pair
                    return False
        return True

    def rec2(j, chosen):
        if best_local['best'] and best_local['best']['cut_fit'] == 1.0:
            return
        if j == len(opt_lists):
            if not feasible_prefix(chosen):
                return
            # suffix feasibility: last span end b_last; pairs after = n-1-last_slot
            slot_l, g_l, a_l, b_l, k_l = chosen[-1]
            if L - b_l < (n - 1 - slot_l):
                return
            # build full spans: fill gaps with compositions
            segments = []  # (start_letter, n_pairs) gaps to fill
            prev_slot, prev_b = -1, 0
            spans = [None] * n
            kinds = ['free'] * n
            for (slot, g, a, b, kind) in chosen:
                gap_pairs = slot - prev_slot - 1
                gap_letters = a - prev_b
                if gap_pairs:
                    segments.append((prev_b, gap_letters, gap_pairs, prev_slot + 1))
                spans[slot] = (a, b)
                kinds[slot] = kind
                prev_slot, prev_b = slot, b
            tail_pairs = n - 1 - prev_slot
            if tail_pairs:
                segments.append((prev_b, L - prev_b, tail_pairs, prev_slot + 1))
            # enumerate gap fills
            def fill(si):
                if si == len(segments):
                    cf = full_cut(spans)
                    enum[0] += 1
                    if best_local['best'] is None or cf > best_local['best']['cut_fit']:
                        best_local['best'] = {'cut_fit': cf, 'spans': list(spans),
                                              'kinds': list(kinds)}
                    return True
                sb, sletters, spairs, sslot0 = segments[si]
                for comp in compositions(sletters, spairs):
                    a = sb
                    ok = True
                    for t, c in enumerate(comp):
                        spans[sslot0 + t] = (a, a + c)
                        a += c
                    if best_local['best'] and best_local['best']['cut_fit'] == 1.0:
                        return True
                    if enum[0] > ENUM_CAP:
                        return True
                    fill(si + 1)
                    if best_local['best'] and best_local['best']['cut_fit'] == 1.0:
                        return True
                return False
            fill(0)
            return
        slot, g, cand = opt_lists[j]
        for (a, b, kind) in cand:
            # quick feasibility vs previous choice
            if j > 0:
                ps, pg, pa, pb, pk = chosen[j - 1]
                if b <= pb or a < pb:
                    continue
                if a - pb < (slot - ps - 1):
                    continue
            else:
                if a < slot:
                    continue
            if L - b < (n - 1 - slot):
                continue
            chosen.append((slot, g, a, b, kind))
            rec2(j + 1, chosen)
            chosen.pop()
            if best_local['best'] and best_local['best']['cut_fit'] == 1.0:
                return
            if enum[0] > ENUM_CAP:
                return

    rec2(0, [])
    return best_local['best']

# ---------------- 8. candidate inventory (frozen)
FORMULAE = [
    "Par ma dépêche du",
    "En réponse à la dépêche de Votre Excellence du",
    "Agréez, Monsieur, l'assurance de ma haute considération",
    "Je renouvelle à V. Exe. l'assurance de ma considération distinguée",
    "veuillez",
    "je vous prie de",
    "il est à désirer que",
]
COLLOCATIONS = ["ce qui", "parce que", "de ce que", "tout ce qui", "ne pas",
                "ne que", "que je", "je vous", "votre excellence", "monsieur",
                "par ma", "en réponse", "cela", "on ne", "dont", "sans",
                "entre", "contre", "pour", "dans", "comme", "aussi", "très", "plus"]

def multiword_prep(reading):
    words = re.findall(r"[a-z\u00e0\u00e2\u00e4\u00e9\u00e8\u00ea\u00eb\u00ee\u00ef\u00f4\u00f6\u00f9\u00fb\u00fc\u00ff\u00e7\u0153\u00e6']+", reading.lower())
    pron_parts, hds, folds = [], [], []
    att, tot = 0, 0
    for w in words:
        tot += 1
        hit, via_fold = attested(w)
        att += 1 if hit else 0
        folds.append(via_fold)
        p, hd = pronounced(w)
        pron_parts.append(p)
        hds.append(hd)
    pron = ''.join(pron_parts)
    return {'reading': reading, 'words': words, 'pron': pron,
            'units': syllabify(pron), 'lex': att / tot if tot else 0.0,
            'via_fold': any(folds), 'had_double': any(hds),
            'mute_e': is_mute_e_word(words[-1], pron) if words else False,
            'elision': "'" in reading}

def build_multiword():
    out = []
    for r in FORMULAE + COLLOCATIONS:
        if '\u00e7a' in r.lower():
            continue  # 'ça' banned outright
        d = multiword_prep(r)
        d['nunits'] = len(d['units'])
        d['kind'] = 'formula' if r in FORMULAE else 'collocation'
        out.append(d)
    return out

MULTIWORD = build_multiword()

# ---------------- 9. scoring (frozen weights/thresholds)
W_LEX, W_CUT, W_BOUND, W_LEN = 0.30, 0.25, 0.20, 0.25
S_MIN, LEX_MIN, LEN_MIN, BOUND_MIN = 0.60, 0.50, 0.50, 0.30

def score_candidate(pairs, win, cand):
    """cand: dict(reading, pron, units, nunits, lex, kind, ...). Returns record or None."""
    s, e, n = win['s'], win['e'], win['e'] - win['s'] + 1
    groups = win['groups']
    pron, units = cand['pron'], cand['units']
    # len_fit (frozen)
    d = abs(cand['nunits'] - n)
    len_fit = 1.0 if d == 0 else (0.5 if d == 1 else 0.0)
    if len_fit < LEN_MIN:
        return None
    # known slots = pairs carrying a skeleton value with a literal compat set
    known_slots = [(j, g) for j, g in enumerate(groups) if g in COMPAT]
    al = align_candidate(pron, units, n, known_slots)
    if al is None:
        return None
    cut_fit = al['cut_fit']
    bound, binfo = bound_fit(pairs, s, e)
    lex_fit = cand['lex']
    S = W_LEX * lex_fit + W_CUT * cut_fit + W_BOUND * bound + W_LEN * len_fit
    # rules fired (frozen names)
    rules = set()
    if cand.get('mute_e'):
        rules.add('MUTE-E')
    if cand.get('elision'):
        rules.add('ELISION')
    if any(abs(al['spans'][j][1] - al['spans'][j][0] - 1) >= 0 and
           block_cut(al['spans'][j], units) == 0.5 for j in range(n)):
        rules.add('SPLIT-PAIR')
    if cand.get('via_fold'):
        rules.add('ORTH-1835')
    if cand.get('had_double'):
        rules.add('DOUBLE-CONS')
    if '06' in groups and (pron[-2:] in ('er', 'ir', 're') or pron[-3:] == 'oir'):
        rules.add('VERB-STEM')
    nasal_var = False
    for j, (slot, g) in enumerate(known_slots):
        kind = al['kinds'][slot]
        blk = pron[al['spans'][slot][0]:al['spans'][slot][1]]
        if kind == 'rival':
            rules.add('RIVAL-NOTE')
        if blk not in {PRIMARY[g]} and blk in COMPAT[g]:
            nasal_var = True
    if nasal_var:
        rules.add('NASAL-VAR')
    # anchor implications (all UNCONFIRMED)
    impl = []
    for j, g in enumerate(groups):
        blk = pron[al['spans'][j][0]:al['spans'][j][1]]
        if g in COMPAT:
            kind = al['kinds'][j] if (j, g) in known_slots else 'free'
            if kind == 'alt':
                impl.append('UNCONFIRMED polyvalent: %s~%s (attested alternate)' % (g, blk))
            elif kind == 'rival':
                impl.append('UNCONFIRMED rival-required: %s~%s' % (g, blk))
            if g in ('24', '52', '62') and kind == 'primary':
                impl.append('UNCONFIRMED lead-consistent: %s~%s' % (g, blk))
            if g == '64' and blk in ('meme',):
                impl.append('UNCONFIRMED 64=meme rival leg')
        elif g == '06':
            impl.append('UNCONFIRMED 06-class: verb-stem window, reading %s' % blk)
        elif g == '47':
            impl.append('UNCONFIRMED: 47~%s' % blk)
        else:
            impl.append('UNCONFIRMED: %s~%s' % (g, blk))
    rival = 'RIVAL-NOTE' in rules
    passed = (S >= S_MIN and lex_fit >= LEX_MIN and len_fit >= LEN_MIN
              and bound >= BOUND_MIN and not rival)
    return {'window_id': win['id'], 'start_pair': s, 'end_pair': e,
            'groups': groups, 'candidate_reading': cand['reading'],
            'kind': cand.get('kind', 'era-vocab'),
            'score': round(S, 4),
            'lex_fit': round(lex_fit, 4), 'cut_fit': round(cut_fit, 4),
            'bound_fit': round(bound, 4), 'len_fit': round(len_fit, 4),
            'rules_fired': sorted(rules),
            'pass_fail': 'pass' if passed else 'fail',
            'anchor_implications': impl,
            'spans': al['spans']}

def slide(pairs, windows, control_tag):
    out = []
    for w0 in windows:
        # windows are positional; groups come from THIS run's pair stream
        # (in controls the stream is shuffled, so the same positions carry
        # different groups — the control's whole point)
        s, e = w0['s'], w0['e']
        win = {'id': w0['id'], 's': s, 'e': e, 'groups': pairs[s:e + 1]}
        n = e - s + 1
        groups = win['groups']
        known_groups = [g for g in groups if g in COMPAT]
        cands = []
        # ERA-VOCAB pool: frozen inventory = 1-5 syllables; unit count in {n-1,n,n+1}
        # (len_fit>=0.5 acceptance gate), letter budget, known-substring prefilter
        for w, v in VOCAB.items():
            if v['nunits'] < 1 or v['nunits'] > 5:
                continue
            if abs(v['nunits'] - n) > 1:
                continue
            L = len(v['pron'])
            if L < n or L > (4 * n if n < 5 else 3 * n):
                continue
            ok = True
            for g in known_groups:
                pool = COMPAT[g] | ATT_ALT.get(g, set()) | RIVALS.get(g, set())
                if not any(t in v['pron'] for t in pool):
                    ok = False
                    break
            if not ok:
                continue
            cands.append({'reading': w, 'pron': v['pron'], 'units': v['units'],
                          'nunits': v['nunits'], 'lex': 1.0, 'kind': 'era-vocab',
                          'mute_e': v['mute_e'], 'elision': "'" in w,
                          'via_fold': False, 'had_double': v['had_double']})
        # frozen multi-word inventory
        for m in MULTIWORD:
            if abs(m['nunits'] - n) <= 1:
                cands.append(m)
        scored = []
        for c in cands:
            r = score_candidate(pairs, win, c)
            if r is not None and r['score'] >= 0.50:
                r['control_tag'] = control_tag
                scored.append(r)
        scored.sort(key=lambda r: -r['score'])
        out.extend(scored[:5])
    return out

# ---------------- 10. run
def main():
    windows = build_windows(PAIRS)
    by_prefix = Counter(w['id'].split('-')[1] if '-' in w['id'] else w['id'] for w in windows)
    real = slide(PAIRS, windows, 'real')
    real_accepts = sum(1 for r in real if r['pass_fail'] == 'pass')
    ctrl_accepts = []
    ctrl_all = []
    rng = random.Random(1841)
    for k in range(1, 4):
        sh = PAIRS[:]
        rng.shuffle(sh)
        cres = slide(sh, windows, 'ctrl-%d' % k)
        ctrl_all.extend(cres)
        ctrl_accepts.append(sum(1 for r in cres if r['pass_fail'] == 'pass'))
    mean_ctrl = sum(ctrl_accepts) / 3.0
    void = real_accepts < 2 * mean_ctrl
    result = {
        'meta': {
            'prereg': ['prereg_pass1.md',
                       'sha256: 233ff426b04e5163cffde15e9dc25a1f7f2460c2da23b79644be1d84a11861a',
                       'prereg_pass1_v11.md (frame amendment)'],
            'parse': 'lane-canonical load_pairs-identical: 1846 pairs / 96 groups',
            'weights': {'lex': W_LEX, 'cut': W_CUT, 'bound': W_BOUND, 'len': W_LEN},
            'thresholds': {'S': S_MIN, 'lex': LEX_MIN, 'len': LEN_MIN, 'bound': BOUND_MIN},
            'n_windows': len(windows),
            'windows_by_class': dict(by_prefix),
            'n_candidates_emitted_real': len(real),
            'real_accepts': real_accepts,
            'control_accepts': ctrl_accepts,
            'control_mean': round(mean_ctrl, 3),
            'void_condition': 'real < 2x mean(control)',
            'void': bool(void),
            'verdict': 'VOID (null)' if void else 'NOT VOID — accepts stand for red-team review',
            'era_vocab_types_ge3': len(VOCAB),
            'control_seed': 1841,
        },
        'candidates': real + ctrl_all,
    }
    outp = os.path.join(HERE, 'slide_pass1.json')
    json.dump(result, open(outp, 'w'), ensure_ascii=False, indent=1)
    print('windows:', len(windows), dict(by_prefix))
    print('real emitted:', len(real), 'accepts:', real_accepts)
    print('control accepts:', ctrl_accepts, 'mean:', round(mean_ctrl, 3))
    print('VOID:', void)

if __name__ == '__main__':
    main()
