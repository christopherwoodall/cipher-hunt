#!/usr/bin/env python3
"""Round-8 84-CONDITIONER part 2: corpus checks + group profiles."""
import collections, json, os, re, sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'redteam'))
from verify_baseline import load_stream

pairs = load_stream()
N = len(pairs)
cf = collections.Counter(pairs)

def occ(g): return [i for i,x in enumerate(pairs) if x==g]
def fol(g): return collections.Counter(pairs[i+1] for i in occ(g) if i+1 < N)
def pre(g): return collections.Counter(pairs[i-1] for i in occ(g) if i > 0)

print('== 66 profile (n=%d) ==' % cf[66])
print('  fol:', dict(fol(66).most_common(8)))
print('  pre:', dict(pre(66).most_common(8)))
print('== 89 profile (n=%d) ==' % cf[89])
print('  fol:', dict(fol(89).most_common(8)))
print('  pre:', dict(pre(89).most_common(8)))
print('== 53 profile (n=%d) ==' % cf[53])
print('  fol:', dict(fol(53).most_common(8)))
print('  pre:', dict(pre(53).most_common(8)))
print('== 26 profile (n=%d) == fol:' % cf[26], dict(fol(26).most_common(6)), ' pre:', dict(pre(26).most_common(6)))
print('== 02 profile (n=%d) == fol:' % cf[2], dict(fol(2).most_common(6)), ' pre:', dict(pre(2).most_common(6)))
print('== 91 profile (n=%d) == fol:' % cf[91], dict(fol(91).most_common(6)), ' pre:', dict(pre(91).most_common(6)))
print('== 92 profile (n=%d) == fol:' % cf[92], dict(fol(92).most_common(6)), ' pre:', dict(pre(92).most_common(6)))
print('== 09 profile (n=%d) == fol:' % cf[9], dict(fol(9).most_common(6)), ' pre:', dict(pre(9).most_common(6)))
print('== 78 profile (n=%d) == fol:' % cf[78], dict(fol(78).most_common(6)), ' pre:', dict(pre(78).most_common(6)))
print('== 24 profile check: 24->37 count ==', sum(1 for i in occ(24) if i+1<N and pairs[i+1]==37))
print('== 37 profile (n=%d) == fol:' % cf[37], dict(fol(37).most_common(6)), ' pre:', dict(pre(37).most_common(6)))

# era corpus
def era_words(filepaths):
    words = []
    for fp in filepaths:
        txt = open(fp, encoding='utf-8', errors='replace').read().lower()
        txt = txt.replace('\u2019', "'").replace('\u2018', "'")
        txt = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', txt)
        words += re.findall(r'[a-z\u00e0-\u00ff]+', txt)
    return words

C = os.path.join(LANE, 'code', 'side-period', 'corpus')
def fp(n): return n if os.path.isabs(n) else os.path.join(C, n)
alldip = [fp(f) for f in os.listdir(C) if f.endswith('.txt')]
words = era_words(alldip); n = len(words)
print()
print('== diplomatic_all N=%d: "qui le X est" 4-grams ==' % n)
c = collections.Counter()
for a,b,cc,d in zip(words, words[1:], words[2:], words[3:]):
    if a=='qui' and b=='le' and d=='est':
        c[cc] += 1
print('  total:', sum(c.values()), ' top X:', c.most_common(15))
print()
print('== "qui le X" (any X) top ==')
c2 = collections.Counter()
for a,b,cc in zip(words, words[1:], words[2:]):
    if a=='qui' and b=='le':
        c2[cc] += 1
print('  total:', sum(c2.values()), ' top:', c2.most_common(15))
print()
print('== sample of the 72 "en en" bigrams ==')
shown = 0
for k in range(n-1):
    if words[k]=='en' and words[k+1]=='en' and shown < 10:
        print('  ...', ' '.join(words[max(0,k-4):k+5]))
        shown += 1
print()
print('== "en le" bigram rate (for 24-37="en le" @310/@473) ==')
nen_le = sum(1 for a,b in zip(words, words[1:]) if a=='en' and b=='le')
print('  n("en le") =', nen_le, ' P=%.7f' % (nen_le/(n-1)))
print('  n("de le") =', sum(1 for a,b in zip(words, words[1:]) if a=='de' and b=='le'))
# "la X" + noun gender check helper: top words after "la"
print()
print('== P84 context: cipher "le"-slot ==')
print('  n(77)=%d P=%.4f  n(11)=%d' % (cf[77], cf[77]/N, cf[11]))
