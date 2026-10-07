"""SEGMENTER round 4 — drag the 25 crib-drag targets (control PASSED).

Per pre-registered protocol in code/crowd4/segmenter_control.md:
  priority @1110-1112 [41 65 38], @81-83 [51 62 16], then STRUCT-score order.
  Each proposed reading needs >=2 INDEPENDENT checks from {G,L,F,X,I}.
  Readings leaning on 62=on stay lead-conditional even with 2 checks.
"""
import collections, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CROWD = os.path.dirname(HERE)
DATA = os.path.join(os.path.dirname(HERE), '..', 'data')
sys.path.insert(0, os.path.join(CROWD, 'crowd'))
sys.path.insert(0, os.path.join(CROWD, 'crowd3'))
from anneal import syllabify_word
from crib_attack import load_pairs

SPLIT_RE = re.compile(r"[\s'\-\xe2\x80\x93\xe2\x80\x94\xc2\xab\xc2\xbb\".,;:!?()\[\]0-9]+")

GT = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er', '40': 'e',
      '46': 'que'}
PROV = {'87': 'ce', '64': 'qui', '96': 'par'}
LEAD = {'62': 'on'}   # STRONG LEAD, promotion candidate (frenchman4_62)

# independent-instrument readings usable for check (I): group -> (syllable, source, strength)
IND = {
    '74': ('te', 'bigram_closer LEAD (2 checks: L1 + self-loop)', 'LEAD'),
    '48': ('les', 'bigram_closer LEAD-weak (2 weak checks)', 'LEAD-weak'),
    '67': ('re', 'bigram_closer LEAD (1 independent leg)', 'LEAD'),
    '16': ('me', 'bigram_closer best, L1=1.001 near-perfect, no anchor legs', 'weak'),
    '98': ('les', 'bigram_closer INCONCLUSIVE w/ reading les (L1=1.08)', 'weak'),
    '94': ('ne', 'round-4 94=ne provisional (frenchman4/syllabary4)', 'provisional'),
}

pairs, odd_lines, off1 = load_pairs()
N = len(pairs)
gfreq = collections.Counter(pairs)
grank = {g: r + 1 for r, (g, _) in enumerate(gfreq.most_common())}

# ---- era corpus: word counts + syllabification cache ----
def tokenize(path):
    # strip Gutenberg boilerplate: keep only between START/END markers
    with open(path, encoding='utf-8', errors='replace') as f:
        text = f.read()
    m1 = re.search(r'\*\*\* START OF.*?\*\*\*', text, re.S)
    m2 = re.search(r'\*\*\* END OF.*?\*\*\*', text, re.S)
    if m1 and m2:
        text = text[m1.end():m2.start()]
    toks = []
    for line in text.splitlines():
        for frag in SPLIT_RE.split(line):
            if frag:
                toks.append(frag.lower())
    return toks

toks = (tokenize(os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt')) +
        tokenize(os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')))
wcount = collections.Counter(toks)
SYL = {}
def syls(w):
    if w not in SYL:
        SYL[w] = syllabify_word(w)
    return SYL[w]
for w in wcount:
    syls(w)
# era syllable frequencies (token-weighted)
sfreq = collections.Counter()
for w, c in wcount.items():
    for s in SYL[w]:
        sfreq[s] += c
srank = {s: r + 1 for r, (s, _) in enumerate(sfreq.most_common())}
print(f'era distinct words={len(wcount)} distinct syllables={len(sfreq)}', file=sys.stderr)

targets = json.load(open(os.path.join(CROWD, 'crowd3', 'segmenter_results.json'))
                    )['crib_drag_targets_STRUCT']
for t in targets:  # verify spans against the real stream
    assert pairs[t['start_pair']:t['end_pair'] + 1] == t['groups'], t

# priority: @1110-1112, @81-83, then score order
prio = sorted(targets, key=lambda t: (0 if t['start_pair'] == 1110 else
                                      1 if t['start_pair'] == 81 else 2,
                                      -t['score']))

def candidates_for(t, use_on_lead):
    """Corpus words with syllable count == n_groups (exact; fallback +-1 cut-tolerant)."""
    n = t['n_groups']
    groups = t['groups']
    hard = dict(GT)
    hard.update(PROV)
    if use_on_lead:
        hard.update(LEAD)
    slots = {i: hard[g] for i, g in enumerate(groups) if g in hard}
    out = []
    for w, c in wcount.items():
        s = SYL[w]
        if len(s) != n:
            continue
        if all(s[i] == v for i, v in slots.items()):
            out.append((w, c, s))
    cut_tol = False
    if not out:  # ear-cutting fallback: +-1, marked cut-tolerant
        cut_tol = True
        for w, c in wcount.items():
            s = SYL[w]
            if len(s) not in (n - 1, n + 1):
                continue
            if len(s) >= max(slots, default=-1) + 1 and \
               all(s[i] == v for i, v in slots.items()):
                out.append((w, c, s))
    out.sort(key=lambda x: -x[1])
    return out, slots, cut_tol

def check_G(t):
    f0, f1 = t['flank_conf']
    return f0 >= 0.90 and f1 >= 0.90 and t['max_inner_conf'] < 0.35

def check_F(groups, syl):
    ratios = []
    for g, s in zip(groups, syl):
        rs = srank.get(s)
        if rs is None:
            return False, []
        rg, rs = grank[g], rs
        ratios.append(max(rg, rs) / min(rg, rs))
    return all(r <= 3 for r in ratios), [round(r, 2) for r in ratios]

results = []
proposals = {}   # start_pair -> (word, syl) best proposal, for check X
for t in prio:
    sp = t['start_pair']
    groups = t['groups']
    cands, slots, cut_tol = candidates_for(t, use_on_lead=('62' in groups))
    top = cands[:5]
    entry = {'target': f"@{sp}-{t['end_pair']}", 'groups': groups,
             'phases': t['phases'], 'score': t['score'],
             'flank_conf': t['flank_conf'], 'max_inner_conf': t['max_inner_conf'],
             'n_candidates_exact': len(cands) if not cut_tol else 0,
             'cut_tolerant': cut_tol, 'slots_constrained': slots,
             'top_candidates': [(w, c) for w, c, s in top]}
    if top:
        w, c, s = top[0]
        proposals[sp] = (w, s)
        entry['best'] = {'word': w, 'count': c, 'syllables': s}
        checks = {}
        checks['G'] = check_G(t)
        checks['L'] = c >= 3
        f_ok, ratios = check_F(groups, s)
        checks['F'] = f_ok
        entry['F_ratios'] = ratios
        # (I): independent instrument supports >=1 proposed syllable
        isup = []
        for g, ps in zip(groups, s):
            if g in IND and IND[g][0] == ps:
                isup.append((g, ps, IND[g][1], IND[g][2]))
        checks['I'] = len(isup) > 0
        entry['I_support'] = isup
        entry['checks'] = checks
        entry['lead_conditional'] = ('62' in groups)
    else:
        entry['best'] = None
    results.append(entry)

# ---- check X: cross-target shared-syllable consistency (second pass) ----
# NON-CIRCULAR version: the other target's reading must itself be
# slot-constrained by known values (GT/provisional/lead), otherwise two
# unconstrained top-frequency picks "confirming" each other is vacuous.
for e in results:
    if not e.get('best'):
        e['checks'] = e.get('checks', {})
        e['checks']['X'] = False
        e['X_hits'] = []
        continue
    s = e['best']['syllables']
    groups = e['groups']
    x_hits = []
    for e2 in results:
        if e2 is e or not e2.get('best') or not e2.get('slots_constrained'):
            continue
        s2 = e2['best']['syllables']
        for i, g in enumerate(groups):
            for j, g2 in enumerate(e2['groups']):
                if g == g2 and s[i] == s2[j]:
                    x_hits.append((g, s[i], e2['target'], e2['best']['word']))
    e['X_hits'] = x_hits
    e['checks']['X'] = len(x_hits) > 0

# ---- verdicts ----
# Reading checks are {L, F, X, I}. (G) is span-quality, already baked into
# target selection in round 3 — counting it again as a reading check would
# be double-counting, and it does not discriminate between readings.
# KILL only on ground-truth contradiction (polyvalence is lane-evidenced:
# bigram_closer 'me' x3 groups, so one group = two syllables is allowed).
for e in results:
    if not e.get('best'):
        e['verdict'] = 'LEAD-held (no candidates)'
        e['n_checks'] = 0
        continue
    reading_checks = {k: v for k, v in e['checks'].items() if k in 'LFXI'}
    n = sum(1 for v in reading_checks.values() if v)
    e['n_checks'] = n
    e['reading_checks_passed'] = [k for k, v in reading_checks.items() if v]
    if n >= 2:
        e['verdict'] = ('PROPOSED-LEAD-CONDITIONAL' if e['lead_conditional']
                        else 'PROPOSED')
    else:
        e['verdict'] = 'LEAD-held'

with open(os.path.join(HERE, 'drag25_results.json'), 'w') as f:
    json.dump({'values': {'ground_truth': GT, 'provisional': PROV,
                          'lead': LEAD},
               'independent_instruments': {k: list(v) for k, v in IND.items()},
               'targets': results}, f)

for e in results:
    b = e.get('best')
    ck = e.get('reading_checks_passed', [])
    print(f"{e['target']} [{' '.join(e['groups'])}] {e['verdict']}"
          + (f" '{b['word']}' x{b['count']} {b['syllables']}" if b else '')
          + f" reading_checks={ck} n_cand={e['n_candidates_exact']}"
          + (' CUT-TOL' if e['cut_tolerant'] else '')
          + (' LEAD-COND' if e.get('lead_conditional') else ''))
