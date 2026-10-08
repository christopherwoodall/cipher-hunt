#!/usr/bin/env python3
"""VALUE-52 hunter battery — Seebach lane round 14, WO5.

Task: battery 52's non-est value.
  T1: census all 52 windows (re-derived from the repaired stream), per-window
      predecessor/successor + est-frame test.
  T2: "la 52" x3 — corpus-driven candidacy for what follows "la".
  T3: positional-allophone test — 52 vs 59 complementary distribution.
  T4: F106 P1c prior respected — no est-class promotion for 52 without
      >=2 independent legs that address the fence.

Stream: repaired 1,847-pair parse, built here from
code/side-keyhunt/repaired_offsets.json (NOT canonical.py, NOT upstream
offsets). Corpus: clean-diplo pool verbatim
(code/crowd12/estetie/estetie.py FRENCH_CLEAN + lane tokenizer).
"""
import json, os, re, unicodedata
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
OUTDIR = os.path.join(LANE, 'code', 'crowd14', 'value52')

# ---------------- 1. repaired stream (own implementation) ----------------
def load_stream():
    offsets = json.load(open(os.path.join(LANE, 'code', 'side-keyhunt', 'repaired_offsets.json')))
    pairs = []
    for line in open(os.path.join(LANE, 'data', 'upstream-ct_R5005.txt')):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        digits = re.sub(r'\D', '', digits)
        off = offsets.get(lid, 0)
        d = digits[off:]
        for i in range(0, len(d) - 1, 2):
            pairs.append(int(d[i:i + 2]))
    assert len(pairs) == 1847, len(pairs)
    assert len(set(pairs)) == 96, len(set(pairs))
    assert pairs[754:760] == [11, 70, 82, 34, 29, 40]
    assert pairs[1034:1040] == [11, 70, 82, 34, 29, 40]
    return pairs

# ---------------- 2. era corpus (lane tokenizer verbatim) ----------------
FRENCH_CLEAN = ['guizot-memoires-t1-gutenberg.txt', 'guizot-memoires-t2-gutenberg.txt',
                'guizot-memoires-t3-gutenberg.txt', 'guizot-memoires-t5-t6.txt',
                'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
                'pozzo-di-borgo-correspondance-v1.txt',
                'levant-correspondence-1841-p3.txt', 'talleyrand-memoires-v1.txt',
                'revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
                'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt']
WORD = re.compile(r"[a-z\xe0\xe2\xe4\xe9\xe8\xea\xeb\xee\xef\xf4\xf6\xf9\xfb\xfc\xff\xe7\u0153\xe6]+(?:'[a-z\xe0\xe2\xe4\xe9\xe8\xea\xeb\xee\xef\xf4\xf6\xf9\xfb\xfc\xff\xe7\u0153\xe6]+)*")

def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('\u2019', "'").replace('\u2018', "'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p:
                continue
            toks.append(p + "'" if i < len(parts) - 1 else p)
    return toks

# ---------------- 3. census ----------------
def windows_of(s, g, r=3):
    out = []
    for i, v in enumerate(s):
        if v == g:
            pre = s[i - 1] if i > 0 else None
            suc = s[i + 1] if i < len(s) - 1 else None
            win = s[max(0, i - r):min(len(s), i + r + 1)]
            out.append({'pos': i, 'pre': pre, 'suc': suc, 'window': win})
    return out

GLOSS = {11: 'la', 70: 'pre', 82: 'm', 34: 'i', 29: 'er', 40: 'e', 46: 'que',
         87: 'ce?', 64: 'qui?', 96: 'par?', 59: 'est?', 77: 'le?', 94: 'ne?',
         52: '52?', 62: 'on?', 6: 'Vstem?', 86: 'Vstem2?', 78: 'ver/er?',
         0: 'pour/le?', 33: 'inf?', 93: 'l\'?', 1: 'est?'}

def gl(w):
    return [('%d%s' % (g, '=%s' % GLOSS[g] if g in GLOSS else '')) for g in w]

def main():
    s = load_stream()
    w52 = windows_of(s, 52)
    w59 = windows_of(s, 59)
    res = {}
    res['n52'] = len(w52); res['n59'] = len(w59)
    res['pos52'] = [w['pos'] for w in w52]
    res['pos59'] = [w['pos'] for w in w59]

    # --- re-derivation check vs round-13 baseline ---
    r13 = json.load(open(os.path.join(LANE, 'code', 'crowd13', 'homophone-cd', 'homophone_cd_results.json')))
    base52 = [w['pos'] for w in r13['set_52_59']['windows52']]
    res['rederive_52_match_round13'] = (res['pos52'] == base52)

    # --- T1: per-window table ---
    tab = []
    for w in w52:
        tab.append({'pos': w['pos'], 'pre': w['pre'], 'suc': w['suc'],
                    'win': ' '.join(gl(w['window']))})
    res['t1_windows'] = tab
    res['pre_dist_52'] = dict(Counter(w['pre'] for w in w52))
    res['suc_dist_52'] = dict(Counter(w['suc'] for w in w52))
    res['pre_dist_59'] = dict(Counter(w['pre'] for w in w59))
    res['suc_dist_59'] = dict(Counter(w['suc'] for w in w59))

    # --- T3: allophone / complementary-distribution tests ---
    frames52 = Counter((w['pre'], w['suc']) for w in w52)
    frames59 = Counter((w['pre'], w['suc']) for w in w59)
    shared_frames = sorted(set(frames52) & set(frames59))
    res['t3_shared_pre_suc_frames'] = [{'pre': p, 'suc': q,
                                       'n52': frames52[(p, q)], 'n59': frames59[(p, q)]}
                                      for (p, q) in shared_frames]
    pre52set, pre59set = set(frames52 and [f[0] for f in frames52]), set(f[0] for f in frames59)
    suc52set, suc59set = set(f[1] for f in frames52), set(f[1] for f in frames59)
    res['t3_shared_predecessors'] = sorted(pre52set & pre59set)
    res['t3_shared_successors'] = sorted(suc52set & suc59set)
    # adjacency: 52 and 59 in the same +-3 window?
    adj = [i for i in range(len(s)) if s[i] == 52 and
           any(s[j] == 59 for j in range(max(0, i - 3), min(len(s), i + 4)))]
    res['t3_52_with_59_within_3'] = adj
    adj2 = [i for i in range(len(s)) if s[i] == 59 and
            any(s[j] == 52 for j in range(max(0, i - 3), min(len(s), i + 4)))]
    res['t3_59_with_52_within_3'] = adj2
    # -este arm exclusivity re-derive
    res['t3_pre84_52'] = sum(1 for w in w52 if w['pre'] == 84)
    res['t3_pre84_59'] = sum(1 for w in w59 if w['pre'] == 84)
    res['t3_pre84_59_pos'] = [w['pos'] for w in w59 if w['pre'] == 84]
    # est-arm (ISLET-10) overlap detail
    res['t3_52_estarm_pos'] = [w['pos'] for w in w52 if w['pre'] in (64, 94, 93)]
    res['t3_59_estarm_pos'] = [w['pos'] for w in w59 if w['pre'] in (64, 94, 93)]

    # --- era corpus ---
    toks = []
    for f in FRENCH_CLEAN:
        toks += tokenize(open(os.path.join(LANE, 'code', 'side-period', 'corpus', f),
                              encoding='utf-8', errors='replace').read())
    res['era_N'] = len(toks)
    la_next = Counter()
    n_la = 0
    for i, t in enumerate(toks):
        if t == 'la':
            n_la += 1
            if i + 1 < len(toks):
                la_next[toks[i + 1]] += 1
    res['era_n_la'] = n_la
    res['era_top_la_followers'] = la_next.most_common(40)
    res['era_P52_given_la_cipher'] = 3 / 45  # cipher: 3 la-52 of 45 la
    # "la est" check
    res['era_la_est'] = la_next.get('est', 0)
    # "est" bigram sanity for per-window test
    est_next = Counter(); est_prev = Counter()
    n_est = 0
    for i, t in enumerate(toks):
        if t == 'est':
            n_est += 1
            if i + 1 < len(toks):
                est_next[toks[i + 1]] += 1
            if i > 0:
                est_prev[toks[i - 1]] += 1
    res['era_n_est'] = n_est
    res['era_top_est_successors'] = est_next.most_common(25)
    res['era_top_est_predecessors'] = est_prev.most_common(25)

    json.dump(res, open(os.path.join(OUTDIR, 'value52_results.json'), 'w'),
              indent=1, ensure_ascii=False)
    print('n52', res['n52'], 'n59', res['n59'])
    print('rederive matches round-13:', res['rederive_52_match_round13'])
    print('shared (pre,suc) frames:', res['t3_shared_pre_suc_frames'])
    print('shared predecessors:', res['t3_shared_predecessors'])
    print('shared successors:', res['t3_shared_successors'])
    print('52-with-59-within-3:', adj)
    print('pre84: 52 ->', res['t3_pre84_52'], '; 59 ->', res['t3_pre84_59'], res['t3_pre84_59_pos'])
    print('era N:', res['era_N'], 'n(la):', n_la, 'n(est):', n_est, '"la est":', res['era_la_est'])
    print('top la-followers:', res['era_top_la_followers'])

main()
