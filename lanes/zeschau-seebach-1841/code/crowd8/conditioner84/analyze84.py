#!/usr/bin/env python3
"""Round-8 84-CONDITIONER: classify 13 free windows, noun identity, que-84-24."""
import collections, json, os, re, sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'redteam'))
from verify_baseline import load_stream

pairs = load_stream()
N = len(pairs)
assert N == 1847
cf = collections.Counter(pairs)

FREE = [154, 276, 391, 412, 788, 857, 1021, 1151, 1189, 1290, 1378, 1418, 1501]
NOUN = [146, 260, 1058, 1447, 1485, 1620, 1764, 1803]
EN = [167, 310, 473, 1665]

def win(i, w=5):
    lo, hi = max(0, i - w), min(N, i + w + 1)
    return '-'.join('%02d' % pairs[j] for j in range(lo, hi))

print('== wide windows (±5), 84 marked ==')
for i in sorted(FREE + NOUN + EN):
    pre = pairs[i-1]; suc = pairs[i+1]
    cls = 'EN' if i in EN else ('NOUN' if i in NOUN else 'FREE')
    lo, hi = max(0, i-5), min(N, i+6)
    seg = []
    for j in range(lo, hi):
        s = '%02d' % pairs[j]
        seg.append('[%s]' % s if j == i else s)
    print('%-4s @%4d pre=%02d suc=%02d  %s' % (cls, i, pre, suc, '-'.join(seg)))

print()
print('== unigram rates of groups in free windows ==')
groups = set()
for i in FREE:
    groups.add(pairs[i-1]); groups.add(pairs[i+1])
for g in sorted(groups):
    print('  %02d: n=%3d P=%.4f' % (g, cf[g], cf[g]/N))
print('  84: n=%3d P=%.4f' % (cf[84], cf[84]/N))

# predecessor/successor recurrence among free windows
print()
print('== free-window pre recurrence ==')
print(dict(collections.Counter(pairs[i-1] for i in FREE).most_common()))
print('== free-window suc recurrence ==')
print(dict(collections.Counter(pairs[i+1] for i in FREE).most_common()))
# full trigram recurrence
print('== free trigram recurrence ==')
print(dict(collections.Counter(
    (pairs[i-1], pairs[i+1]) for i in FREE).most_common()))

# ============ era corpus ============
def era_words(filepaths):
    words = []
    for fp in filepaths:
        txt = open(fp, encoding='utf-8', errors='replace').read().lower()
        txt = txt.replace('\u2019', "'").replace('\u2018', "'")
        txt = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', txt)
        words += re.findall(r'[a-z\u00e0-\u00ff]+', txt)
    return words

C = os.path.join(LANE, 'code', 'side-period', 'corpus')
def fp(n):
    return n if os.path.isabs(n) else os.path.join(C, n)

primary = [fp('nesselrode-v8.txt'), fp('levant-correspondence-1841-p3.txt')]
alldip = [fp(f) for f in os.listdir(C) if f.endswith('.txt')]

for name, files in [('despatches_primary', primary), ('diplomatic_all', alldip)]:
    words = era_words(files)
    wu = collections.Counter(words)
    n = len(words)
    bi = collections.Counter(zip(words, words[1:]))
    print()
    print('== %s: N=%d == ' % (name, n))
    print('  n("en en") =', bi[('en','en')], ' P=%.6f' % (bi[('en','en')]/max(n-1,1)))
    print('  n("qu en en") trigram =', sum(1 for a,b,c in zip(words,words[1:],words[2:]) if (a,b,c)==('qu','en','en')))
    print('  n("que en en") trigram =', sum(1 for a,b,c in zip(words,words[1:],words[2:]) if (a,b,c)==('que','en','en')))
    print('  n("en") =', wu['en'], ' P=%.5f' % (wu['en']/n))
    # candidate monosyllabic masculine nouns near P84=0.01354
    cands = ['roi','droit','nom','temps','chef','cas','choix','corps','sens',
             'point','cours','lieu','bras','pas','fait','bruit','poids','soin',
             'tour','reste','sujet','objet','effet','projet']
    print('  candidate noun unigrams (P84=%.4f):' % (cf[84]/N))
    for w in cands:
        r = wu[w]/n if n else 0
        if r > 0.001:
            print('    %-8s n=%6d P=%.5f  ratio=%.2fx' % (w, wu[w], r, r/(cf[84]/N)))

# "le X est" / "qui le X est" / "le X en" for top candidates on primary
words = era_words(primary); wu = collections.Counter(words); n = len(words)
print()
print('== despatches_primary contexts for top candidates ==')
for w in ['roi','droit','cas','nom','temps','chef','point','cours','corps']:
    le_w_est = sum(1 for a,b,c in zip(words,words[1:],words[2:]) if (a,b,c)==('le',w,'est'))
    qui_le_w_est = sum(1 for a,b,c,d in zip(words,words[1:],words[2:],words[3:]) if (a,b,c,d)==('qui','le',w,'est'))
    le_w_en = bi = None
    print('  %-8s P=%.5f  "le %s est"=%d  "qui le %s est"=%d' % (
        w, wu[w]/n, w, le_w_est, w, qui_le_w_est))
    # le X en
    cnt = 0; ex = []
    for k in range(n-2):
        if words[k]=='le' and words[k+1]==w and words[k+2]=='en':
            cnt += 1
            if len(ex) < 3: ex.append(' '.join(words[k:k+6]))
    print('           "le %s en"=%d  e.g. %s' % (w, cnt, ex))
