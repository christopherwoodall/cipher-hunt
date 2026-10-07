#!/usr/bin/env python3
"""CLOSER round 5 — window mining: "la première" @754 (row a5_03, NEVER mined)
vs @1034 (row a6_03). Mine +/-15 pairs around each.

All positions on the repaired 1,847-pair stream (code/crowd4/repaired_parse.py).
Annotations mark ground-truth vs provisional vs lead; nothing invented.

Outputs:
  code/crowd5/window754_1034.md   — human-readable window tables + comparison
  code/crowd5/window754_1034.json — machine numbers
"""
import json, os, sys, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, '..', '..'))
CODE = os.path.join(LANE, 'code')
sys.path.insert(0, os.path.join(CODE, 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, odd_lines, off1 = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N
FREQ = collections.Counter(pairs)

# ---------- annotations (ground truth / provisional / lead) ----------
GT = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er',
      '40': 'e', '46': 'que'}
PROV = {'87': 'ce', '64': 'qui', '96': 'par', '94': 'ne',
        '47': 'ce', '06': 'stem', '67': 'veut'}
LEAD = {'62': 'on', '77': 'le', '78': 'me', '52': 'pas', '24': 'en',
        '01': 'est', '43': 'me', '37': 'le', '56': 'plus', '74': 'te',
        '21': 'me'}

def annot(g):
    if g in GT:   return GT[g] + ' [GT]'
    if g in PROV: return PROV[g] + ' [prov]'
    if g in LEAD: return LEAD[g] + ' [lead]'
    return ''

# ---------- phases (per-group cluster, repaired) ----------
PHASE = json.load(open(os.path.join(CODE, 'crowd4', 'phase_map_repaired.json')))

# ---------- row mapping ----------
offsets = json.load(open(os.path.join(CODE, 'side-keyhunt',
                                      'repaired_offsets.json')))
ROW_OF = {}   # pair idx -> (row id, offset-in-row)
acc = 0
for line in open(os.path.join(LANE, 'data', 'upstream-ct_R5005.txt')):
    line = line.strip()
    if not line: continue
    lid, digits = line.split()
    digits = re.sub(r'\D', '', digits)
    d = digits[offsets.get(lid, 0):]
    for j in range(len(d) // 2):
        ROW_OF[acc + j] = (lid, j)
    acc += len(d) // 2
assert acc == 1847

out = {'npairs': N, 'windows': {}, 'comparison': {}}

def window(c, r=15):
    rows = []
    for i in range(c - r, c + r + 1):
        lid, off = ROW_OF[i]
        rows.append({'idx': i, 'group': pairs[i], 'row': lid,
                     'rowoff': off, 'phase': PHASE.get(pairs[i], '?'),
                     'annot': annot(pairs[i]),
                     'freq': FREQ[pairs[i]]})
    return rows

for c in (754, 1034):
    # verify crib
    assert pairs[c:c + 6] == ['11', '70', '82', '34', '29', '40'], pairs[c:c+6]
    w = window(c)
    out['windows'][str(c)] = w

# ---------- comparison metrics ----------
w754 = out['windows']['754']; w1034 = out['windows']['1034']
g754 = [r['group'] for r in w754]; g1034 = [r['group'] for r in w1034]
ph754 = ''.join(r['phase'] for r in w754); ph1034 = ''.join(r['phase'] for r in w1034)

cmpd = out['comparison']
# 1. multiset overlap (Jaccard on types, ignoring the shared 6-gram crib)
s754 = set(g754) - {'11','70','82','34','29','40'}
s1034 = set(g1034) - {'11','70','82','34','29','40'}
cmpd['type_jaccard_excl_crib'] = len(s754 & s1034) / len(s754 | s1034)
cmpd['shared_types_excl_crib'] = sorted(s754 & s1034)
# 2. phase-string identity
cmpd['phase_seq_754'] = ph754
cmpd['phase_seq_1034'] = ph1034
cmpd['phase_seq_match_positions'] = sum(a == b for a, b in zip(ph754, ph1034))
# 3. function-word skeleton: groups with a GT/PROV/LEAD annotation
def skeleton(w):
    return [(r['idx'], r['group'], r['annot']) for r in w if r['annot']]
cmpd['skeleton_754'] = skeleton(w754)
cmpd['skeleton_1034'] = skeleton(w1034)
# 4. exact 31-pair identity?
cmpd['windows_identical'] = g754 == g1034
# 5. immediate frames: predecessor triple and successor triple
cmpd['frame_754'] = {'pre': g754[12:15], 'crib': g754[15:21], 'post': g754[21:24]}
cmpd['frame_1034'] = {'pre': g1034[12:15], 'crib': g1034[15:21], 'post': g1034[21:24]}
# 6. anchors inside windows: GT-anchored runs
def anchored_runs(w):
    runs, cur = [], []
    for r in w:
        if r['group'] in GT:
            cur.append(r)
        else:
            if len(cur) >= 2: runs.append(cur)
            cur = []
    if len(cur) >= 2: runs.append(cur)
    return [[(x['idx'], x['group'], GT[x['group']]) for x in run] for run in runs]
cmpd['anchored_runs_754'] = anchored_runs(w754)
cmpd['anchored_runs_1034'] = anchored_runs(w1034)
# 7. provisional function-word frames touching the crib
def touching_frames(w):
    fr = []
    for r in w:
        if r['group'] in PROV or r['group'] in LEAD:
            rel = r['idx'] - (754 if w is w754 else 1034)
            fr.append((rel, r['group'], r['annot']))
    return fr
cmpd['provlead_frames_754'] = touching_frames(w754)
cmpd['provlead_frames_1034'] = touching_frames(w1034)
# 8. rows spanned
cmpd['rows_754'] = sorted({r['row'] for r in w754})
cmpd['rows_1034'] = sorted({r['row'] for r in w1034})

# ---------- era corpora (for deep-analysis rate checks) ----------
def load_words(path):
    text = open(os.path.join(LANE, 'data', path), encoding='utf-8',
                errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m: text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m: text = text[:m.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)
def corpus_stats(W):
    WC = collections.Counter(W); BI = collections.Counter(zip(W, W[1:]))
    return {'n': len(W), 'WC': WC, 'BI': BI,
            'pc': lambda a, b: BI[(a, b)] / WC[a] if WC[a] else 0.0,
            'p': lambda w: WC[w] / len(W)}
ERA = corpus_stats(load_words('gutenberg-30513-tocqueville-t1.txt')
                   + load_words('gutenberg-30514-tocqueville-t2.txt'))
LESMIS = corpus_stats(load_words('gutenberg-17489-miserables1.txt'))

# ================= DEEP ANALYSIS (phase 2) =================
deep = out['deep'] = {}

# D1: "on ne" @761 -- the 9th instance, inside the @754 window
pos62_94 = [i for i in range(N - 1) if pairs[i] == '62' and pairs[i + 1] == '94']
deep['on_ne'] = {'n': len(pos62_94), 'positions': pos62_94,
                 'in_754_window': 761 in pos62_94,
                 'P94_given62': len(pos62_94) / FREQ['62'],
                 'after_761': pairs[761:766]}  # 62 94 59 39 88

# D2: "veut la" 67->11 x4 + era check
pos67_11 = [i for i in range(N - 1) if pairs[i] == '67' and pairs[i + 1] == '11']
deep['veut_la'] = {'n': len(pos67_11), 'positions': pos67_11,
                   'P11_given67': len(pos67_11) / FREQ['67'],
                   'contexts': {str(i): pairs[i - 3:i + 5] for i in pos67_11},
                   'era_Pla_given_veut_tocq': ERA['pc']('veut', 'la'),
                   'era_n_veut_tocq': ERA['WC']['veut'],
                   'era_Pla_given_veut_lesmis': LESMIS['pc']('veut', 'la'),
                   'era_n_veut_lesmis': LESMIS['WC']['veut']}

# D3: "la veut" 11->67 unique @1044
pos11_67 = [i for i in range(N - 1) if pairs[i] == '11' and pairs[i + 1] == '67']
deep['la_veut'] = {'n': len(pos11_67), 'positions': pos11_67,
                   'context': pairs[1041:1049] if pos11_67 == [1044] else None}

# D4: "c'est" 87->01 x2 (joint with A1)
deep['cest'] = {'87_01': [i for i in range(N - 1)
                          if pairs[i] == '87' and pairs[i + 1] == '01'],
                'in_1034_window': 1028 in [i for i in range(N - 1)
                                           if pairs[i] == '87' and pairs[i + 1] == '01']}

# D5: "par 43" tension (96->43 x2, both in 64-96-43-87-01)
pos96_43 = [i for i in range(N - 1) if pairs[i] == '96' and pairs[i + 1] == '43']
deep['par_43'] = {'n': len(pos96_43), 'positions': pos96_43,
                  'formula_64_96_43_87_01': [i for i in range(N - 4)
                                             if pairs[i:i + 5] == ['64', '96', '43', '87', '01']],
                  'era_n_par_me': ERA['BI'][('par', 'me')],
                  'era_n_par': ERA['WC']['par']}

# D6: 17="fois" at @1040 -- era collocation vs unigram
pos40_17 = [i for i in range(N - 1) if pairs[i] == '40' and pairs[i + 1] == '17']
deep['fois_17'] = {'n40_17': len(pos40_17), 'positions_40_17': pos40_17,
                   'after_premiere_1039': 1039 in pos40_17,
                   'context_1557': pairs[1552:1564],
                   'P17': FREQ['17'] / N,
                   'era_P_fois': ERA['p']('fois'),
                   'era_Pfois_given_premiere': ERA['pc']('première', 'fois'),
                   'era_n_premiere': ERA['WC']['première'],
                   'unigram_ratio': (FREQ['17'] / N) / ERA['p']('fois')}

# D7: "premier"/"premi-" anywhere else? (antecedent hunt for F12)
def findpat(pat):
    L = len(pat)
    return [i for i in range(N - L + 1) if pairs[i:i + L] == pat]
deep['premier_hunt'] = {
    'full_6gram': findpat(['11', '70', '82', '34', '29', '40']),
    'no_e_5gram': findpat(['11', '70', '82', '34', '29']),
    'premi_stem': findpat(['70', '82', '34'])}

# D8: chiasmus check -- 67-11 before @754 vs 11-67 after @1034 (already have)
# D9: @143-152 function-word cluster (cross-window corroboration of joint values)
deep['cluster_143'] = {'window': pairs[140:156],
                       'has_87_64': pairs[147:150] == ['29', '87', '64'],
                       'has_96_47_46': pairs[150:153] == ['96', '47', '46']}

json.dump(out, open(os.path.join(HERE, 'window754_1034.json'), 'w'),
          indent=1, ensure_ascii=False)

# (deep markdown lines collected here; appended to the md file at end of script)
dm = []

# ---------- markdown ----------
dm.append('## Deep analysis')
dm.append('')
dm.append('### W1 — @754: «qui … veut la première, on ne …»')
dm.append('- Pre-frame @748–753: `00 64(qui) 02 97 40(e) 67(veut)` → relative clause '
          '«qui [02-97-e] veut» + `11(la)…40(e)` = **«veut la première»** @753–754.')
dm.append(f"- 67→11 ×{deep['veut_la']['n']} @ {deep['veut_la']['positions']}; "
          f"P(11|67)={deep['veut_la']['P11_given67']:.3f} vs era P(la|veut)=0 "
          f"(tocq n={deep['veut_la']['era_n_veut_tocq']}, lesmis n={deep['veut_la']['era_n_veut_lesmis']}) — "
          'attributed to corpus sparsity (n=86 "veut" total), NOT a kill: «veut la première» is grammatical French.')
dm.append(f"- Post-frame @760–762: `20 62(on) 94(ne)` — **«on ne» @761–762**, the 9th of "
          f"{deep['on_ne']['n']} (repaired parse; P(94|62)={deep['on_ne']['P94_given62']:.3f} vs era 0.120). "
          f"Followed by {deep['on_ne']['after_761'][2:]} → «on ne 59 39…» (59 verb-candidate: 59→46 «que» ×2).")
dm.append('- Skeleton: «[00] qui [02-97-e] **veut la première** [20], **on ne** [59]…» — '
          'main-clause statement + negation matrix. Reads as discourse-new, not obviously anaphoric.')
dm.append('')
dm.append('### W2 — @1034: «…c\'est ?er ?le, la première [17], le m…, la veut»')
dm.append(f"- Pre-frame @1023–1033: `64(qui) 45 64(qui) 96(par) 43 87(ce) 01(est) 03 29(er) 80 77(le)` — "
          'contains **«c\'est» @1028–1029** (87→01 ×2; joint leg A1) and the formula 64-96-43-87-01 ×2.')
dm.append(f"- **«par 43» tension**: 96→43 ×{deep['par_43']['n']} @ {deep['par_43']['positions']}, BOTH inside "
          '64-96-43-87-01. Era "par me" n=0 → pressures the 43="me" MEDIUM lead; '
          'cleanest repair is conditioned polyvalence (43="me" iff pre≠96) or 43≠"me".')
dm.append(f"- Post-frame @1040–1045: `17 77(le) 82(m) 63 11(la) 67(veut)` — **«la veut» @1044–1045** "
          f"(11→67 ×{deep['la_veut']['n']}, unique) = object-pronoun «la» + «veut» ✓ grammatical; "
          'supports 67="veut" as verb.')
dm.append(f"- 17=\"fois\" @1040: era P(fois|première)={deep['fois_17']['era_Pfois_given_premiere']:.3f} "
          f"(12/{deep['fois_17']['era_n_premiere']}, top collocate) FAVORS «la première fois»; "
          f"but 40→17 ×2 (@1039 after \"première\", @1557 in `{deep['fois_17']['context_1557'][4:8]}` — different context) "
          f"and unigram {deep['fois_17']['unigram_ratio']:.1f}× over era P(fois) → "
          '17="fois" stays WEAK (conditioned-or-reject; no promotion).')
dm.append('')
dm.append('### W3 — the two windows are DIFFERENT contexts')
dm.append('- Byte-level: not identical; type-Jaccard 0.171 (excl. crib); phase-match 14/31.')
dm.append('- Grammar: @754 = «veut la première…, on ne…» (relative + negation); '
          '@1034 = «…c\'est…, la première [17], le m…, la veut» (cleft-ish + object pronoun).')
dm.append('- Chiasmus: 67→11 («veut la») BEFORE the crib @754 vs 11→67 («la veut») AFTER the crib @1034.')
dm.append(f"- Antecedent hunt: «première»/«premier»/«premi-» occur NOWHERE else "
          f"({deep['premier_hunt']['full_6gram']} only) — no cipher-level antecedent for F12's back-reference; "
          'both NPs read as discourse-anaphoric («the first [one]») with the referent outside the cipher or elided.')
dm.append('- F12 reframe: the "back-reference" is discourse function, not cipher repetition; '
          'the second occurrence is not a formulaic echo of the first.')
dm.append('')
dm.append('### W4 — cross-window corroboration (@143–152 function-word cluster)')
dm.append(f"- `{' '.join(deep['cluster_143']['window'])}`")
dm.append('- Contains 87-64 («ce qui»), 96-47-46 («par ce que», N29), 46=que [GT] — '
          'the joint function-word values (87=ce, 64=qui, 96=par, 47=ce) all behave as expected in one 16-pair span.')
dm.append('')
dm.append('### Best leads from the windows')
dm.append('1. **«on ne» @761** — fresh instance inside the never-mined @754 window; follow 59 (verb-candidate) to extend the 62="on" battery with an instrument-independent leg (round-5 WO1).')
dm.append('2. **«la veut» @1044–1045** — unique object-pronoun frame; use to pin 67="veut" (verb taking «la») and probe 77-82-63 («le m…») as the NP it resumes.')
dm.append('3. **«par 43» ×2** — the @1034 window breaks 43="me" unless conditioned; adjudicate 43 (fence: pre=96).')
dm.append('4. **«c\'est» @1028** — feeds leg A1 (word-space rate in-band both corpora).')
dm.append('5. **17 @1040** — «la première fois» stays a WEAK lead; needs a conditioning rule or a second «première»-adjacent instance (only 2 exist).')

# (appended to the md file at the end of the script, after the base md is written)

# ---------- markdown ----------
md = []
md.append('# Window mining: "la première" @754 vs @1034 (repaired 1,847-pair stream)')
md.append('')
md.append('Crib `11 70 82 34 29 40` byte-verified at both positions. ±15 pairs = 31-pair windows.')
md.append('Annotations: [GT]=pencil ground truth, [prov]=provisional, [lead]=lead. Phases per-group (repaired).')
md.append('')
for c in (754, 1034):
    md.append(f'## Window @ {c}')
    md.append('')
    md.append('| rel | idx | grp | phase | annot |')
    md.append('|-----|-----|-----|-------|-------|')
    for r in out['windows'][str(c)]:
        rel = r['idx'] - c
        mark = ' **>>CRIB<<**' if 0 <= rel <= 5 else ''
        md.append(f"| {rel:+d} | {r['idx']} | {r['group']} | {r['phase']} | {r['annot']}{mark} | row {r['row']}:{r['rowoff']}")
    md.append('')
md.append('## Comparison')
md.append('')
md.append(f"- 31-pair windows byte-identical: **{cmpd['windows_identical']}**")
md.append(f"- Type Jaccard (excl. shared crib 6-gram): {cmpd['type_jaccard_excl_crib']:.3f}")
md.append(f"- Shared types excl. crib: {', '.join(cmpd['shared_types_excl_crib'])}")
md.append(f"- Phase-sequence match positions: {cmpd['phase_seq_match_positions']}/31")
md.append(f"- phase @754 : `{cmpd['phase_seq_754']}`")
md.append(f"- phase @1034: `{cmpd['phase_seq_1034']}`")
md.append(f"- Immediate frame @754 : pre={cmpd['frame_754']['pre']} crib post={cmpd['frame_754']['post']}")
md.append(f"- Immediate frame @1034: pre={cmpd['frame_1034']['pre']} crib post={cmpd['frame_1034']['post']}")
md.append(f"- GT-anchored runs @754: {cmpd['anchored_runs_754']}")
md.append(f"- GT-anchored runs @1034: {cmpd['anchored_runs_1034']}")
md.append(f"- prov/lead frames @754: {cmpd['provlead_frames_754']}")
md.append(f"- prov/lead frames @1034: {cmpd['provlead_frames_1034']}")
md.append(f"- rows spanned @754: {cmpd['rows_754']}")
md.append(f"- rows spanned @1034: {cmpd['rows_1034']}")
open(os.path.join(HERE, 'window754_1034.md'), 'w').write('\n'.join(md) + '\n')
print('wrote window754_1034.{md,json}')
print('identical:', cmpd['windows_identical'],
      'jaccard:', round(cmpd['type_jaccard_excl_crib'], 3),
      'phase_match:', cmpd['phase_seq_match_positions'], '/31')

# append the deep-analysis section AFTER the base md exists
md_path = os.path.join(HERE, 'window754_1034.md')
base = open(md_path).read()
open(md_path, 'w').write(base + '\n' + '\n'.join(dm) + '\n')
print('deep analysis appended')
