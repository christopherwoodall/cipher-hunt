#!/usr/bin/env python3
"""Round-7 CONDITIONER: 84 conflict + 00 conflict (bars in PREREG.md)."""
import collections, json, os, re, sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'redteam'))
from verify_baseline import load_stream

pairs = load_stream()
N = len(pairs)
assert N == 1847
cf = collections.Counter(pairs)
cbi = collections.Counter(zip(pairs, pairs[1:]))

def occ(g):
    return [i for i, x in enumerate(pairs) if x == g]

def win(i, w=3):
    lo, hi = max(0, i - w), min(N, i + w + 1)
    return [(j, pairs[j]) for j in range(lo, hi)]

R = {}

# ================= 84 =================
A = {}
o84 = occ(84)
A['n84'] = len(o84)
tbl = []
for i in o84:
    pre = pairs[i-1] if i > 0 else None
    suc = pairs[i+1] if i + 1 < N else None
    tbl.append({'pos': i, 'pre': pre, 'suc': suc})
A['table84'] = tbl
covered = {'en': [t for t in tbl if t['pre'] in (46, 94, 82)],
           'noun': [t for t in tbl if t['pre'] in (77, 11)]}
free = [t for t in tbl if t['pre'] not in (46, 94, 82, 77, 11)]
A['en_class'] = [t['pos'] for t in covered['en']]
A['noun_class'] = [t['pos'] for t in covered['noun']]
A['free_cases'] = free
A['B1_coverage'] = len(free) == 0
A['en_windows'] = {t['pos']: win(t['pos']) for t in covered['en']}
A['noun_windows'] = {t['pos']: win(t['pos']) for t in covered['noun']}
A['suc_of_en_class'] = collections.Counter(t['suc'] for t in covered['en'])
A['suc_of_noun_class'] = collections.Counter(t['suc'] for t in covered['noun'])
A['pre_of_en_class'] = collections.Counter(t['pre'] for t in covered['en'])
A['pre_of_noun_class'] = collections.Counter(t['pre'] for t in covered['noun'])
# byte-identity among noun-class windows (n_eff)
A['noun_class_trigrams'] = collections.Counter(
    '-'.join('%02d' % g for g in pairs[t['pos']-1:t['pos']+2]) for t in covered['noun'])
A['en_class_trigrams'] = collections.Counter(
    '-'.join('%02d' % g for g in pairs[t['pos']-1:t['pos']+2]) for t in covered['en'])
R['84'] = A

# ================= 00 =================
B = {}
o00 = occ(0)
B['n00'] = len(o00)
tbl0 = []
for i in o00:
    pre = pairs[i-1] if i > 0 else None
    suc = pairs[i+1] if i + 1 < N else None
    tbl0.append({'pos': i, 'pre': pre, 'suc': suc})
B['table00'] = tbl0
le_class = [t for t in tbl0 if t['pre'] == 96]
pour_class = [t for t in tbl0 if t['pre'] != 96]
B['le_class_pos'] = [t['pos'] for t in le_class]
B['le_class_suc'] = [t['suc'] for t in le_class]
B['le_class_windows'] = {t['pos']: win(t['pos']) for t in le_class}
B['le_class_free'] = [t for t in tbl0 if t['pre'] == 96 and (t['pos'] - 1) not in
                      [i for i in range(N-1) if pairs[i] == 96 and pairs[i+1] == 0]]
B['C3_zero_free'] = len(B['le_class_free']) == 0
# C4: battery after removing pre=96 windows
B['C4_00_86'] = sum(1 for t in pour_class if t['suc'] == 86)
B['C4_00_06'] = sum(1 for t in pour_class if t['suc'] == 6)
B['C4_00_46'] = sum(1 for t in pour_class if t['suc'] == 46)
B['C4_00_11'] = sum(1 for t in pour_class if t['suc'] == 11)
B['C4_06_00'] = cbi[(6, 0)]  # 06->00 unaffected by pre=96 removal
B['C4_96_00_86'] = sum(1 for t in le_class if t['suc'] == 86)
B['P00'] = B['n00'] / N
B['P46g00'] = sum(1 for t in tbl0 if t['suc'] == 46) / B['n00']
B['pred00_full'] = dict(collections.Counter(t['pre'] for t in tbl0).most_common())
R['00'] = B

# ================= era: elision-split word model =================
def era_model(filepaths):
    words = []
    for fp in filepaths:
        txt = open(fp, encoding='utf-8', errors='replace').read().lower()
        txt = txt.replace('\u2019', "'").replace('\u2018', "'")
        txt = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', txt)
        words += re.findall(r'[a-z\u00e0-\u00ff]+', txt)
    wu = collections.Counter(words)
    we = collections.defaultdict(collections.Counter)
    for a, b in zip(words, words[1:]):
        we[a][b] += 1
    return words, wu, we

C = os.path.join(LANE, 'code', 'side-period', 'corpus')
fr_files = {
    'guizot-mem-t1': 'guizot-memoires-t1-gutenberg.txt',
    'guizot-mem-t2': 'guizot-memoires-t2-gutenberg.txt',
    'guizot-mem-t3': 'guizot-memoires-t3-gutenberg.txt',
    'guizot-mem-t5t6': 'guizot-memoires-t5-t6.txt',
    'nesselrode-v7': 'nesselrode-v7.txt',
    'nesselrode-v8': 'nesselrode-v8.txt',
    'nesselrode-v9': 'nesselrode-v9.txt',
    'nesselrode-v10': 'nesselrode-v10.txt',
    'pozzo-di-borgo': 'pozzo-di-borgo-correspondance-v1.txt',
    'talleyrand-mem': 'talleyrand-memoires-v1.txt',
    'metternich-v4': 'metternich-papiere-v4.txt',
    'metternich-v6': 'metternich-papiere-v6.txt',
    'levant-1841-p3': 'levant-correspondence-1841-p3.txt',
    'revue-q1': 'revue-deux-mondes-1841-q1.txt',
    'revue-q2': 'revue-deux-mondes-1841-q2.txt',
    'revue-q3': 'revue-deux-mondes-1841-q3.txt',
    'revue-q4': 'revue-deux-mondes-1841-q4.txt',
    'tocq-t1': os.path.join(LANE, 'data', 'gutenberg-30513-tocqueville-t1.txt'),
    'tocq-t2': os.path.join(LANE, 'data', 'gutenberg-30514-tocqueville-t2.txt'),
}
D = {}
for name, fn in fr_files.items():
    fp = fn if os.path.isabs(fn) else os.path.join(C, fn)
    if not os.path.exists(fp):
        D[name] = {'missing': True}
        continue
    words, wu, we = era_model([fp])
    n = len(words)
    npour = wu['pour']
    pq = we['pour'].get('que', 0)
    D[name] = {'N': n, 'n_pour': npour, 'P_pour': npour / n if n else 0,
               'n_pour_que': pq, 'Pque_given_pour': pq / npour if npour else 0,
               'r1': (B['P00'] / (npour / n)) if n and npour else None,
               'r3': (B['P46g00'] / (pq / npour)) if npour and pq else None}
# despatches-primary subset and full-French-diplomatic subset
subsets = {
    'despatches_primary': ['nesselrode-v8', 'levant-1841-p3'],
    'diplomatic_all': ['guizot-mem-t1', 'guizot-mem-t2', 'guizot-mem-t3',
                       'guizot-mem-t5t6', 'nesselrode-v7', 'nesselrode-v8',
                       'nesselrode-v9', 'nesselrode-v10', 'pozzo-di-borgo',
                       'talleyrand-mem', 'metternich-v4', 'metternich-v6',
                       'levant-1841-p3', 'revue-q1', 'revue-q2', 'revue-q3',
                       'revue-q4'],
    'tocqueville_parity': ['tocq-t1', 'tocq-t2'],
}
for sname, members in subsets.items():
    words, wu, we = era_model([
        fr_files[m] if os.path.isabs(fr_files[m])
        else os.path.join(C, fr_files[m]) for m in members
        if not D[m].get('missing')])
    n = len(words)
    npour = wu['pour']
    pq = we['pour'].get('que', 0)
    D[sname] = {'N': n, 'n_pour': npour, 'P_pour': npour / n if n else 0,
                'n_pour_que': pq, 'Pque_given_pour': pq / npour if npour else 0,
                'r1': B['P00'] / (npour / n),
                'r3': B['P46g00'] / (pq / npour)}
R['diplomatic'] = D

with open(os.path.join(LANE, 'code', 'crowd7', 'conditioner',
                       'conditioner_results.json'), 'w') as f:
    json.dump(R, f, indent=1, ensure_ascii=False)

print('== 84 ==')
print('n84 =', A['n84'])
for t in tbl:
    print('  pos=%4d pre=%s suc=%s' % (t['pos'],
          ('%02d' % t['pre']) if t['pre'] is not None else '--',
          ('%02d' % t['suc']) if t['suc'] is not None else '--'))
print('en-class pos:', A['en_class'])
print('noun-class pos:', A['noun_class'])
print('B1 coverage (zero free cases):', A['B1_coverage'], '| free:', A['free_cases'])
print('en-class pre/suc:', dict(A['pre_of_en_class']), dict(A['suc_of_en_class']))
print('noun-class pre/suc:', dict(A['pre_of_noun_class']), dict(A['suc_of_noun_class']))
print('en-class trigram n_eff:', dict(A['en_class_trigrams']))
print('noun-class trigram n_eff:', dict(A['noun_class_trigrams']))
print()
print('== 00 ==')
print('le-class (pre=96) pos/suc:', list(zip(B['le_class_pos'], B['le_class_suc'])))
print('C3 zero free:', B['C3_zero_free'])
print('C4 battery post-removal: 00->86=%d 00->06=%d 00->46=%d 00->11=%d 06->00=%d le->86=%d'
      % (B['C4_00_86'], B['C4_00_06'], B['C4_00_46'], B['C4_00_11'],
         B['C4_06_00'], B['C4_96_00_86']))
print()
print('== diplomatic rates ==')
for name in ['tocqueville_parity', 'despatches_primary', 'diplomatic_all'] + \
        [k for k in fr_files if k in D and not k.startswith('tocq')]:
    d = D[name]
    if d.get('missing'):
        print('  %-20s MISSING' % name); continue
    print('  %-20s N=%8d n_pour=%6d P_pour=%.5f n_pour_que=%5d Pque|pour=%.4f r1=%5.2fx r3=%5.2fx'
          % (name, d['N'], d['n_pour'], d['P_pour'], d['n_pour_que'],
             d['Pque_given_pour'], d['r1'], d['r3']))
print('wrote conditioner_results.json')
