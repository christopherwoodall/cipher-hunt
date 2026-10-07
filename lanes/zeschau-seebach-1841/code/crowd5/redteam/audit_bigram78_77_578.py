#!/usr/bin/env python3
"""RED TEAM audit of Bigram Closer's round-5 WO1/WO2/WO3 (78, 77=le, @578)."""
import json, re, unicodedata, collections
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]
import sys
sys.path.insert(0, str(LANE / 'code' / 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
seq = [int(g) for g in pairs]; n = len(seq)
assert n == 1847
big = collections.Counter(zip(seq[:-1], seq[1:]))
cf = collections.Counter(seq)

def find(pat):
    L = len(pat)
    return [i for i in range(n - L + 1) if seq[i:i+L] == pat]

print('=== position audit ===')
print('n78 =', cf[78], '| n77 =', cf[77])
print('77->78 @', find([77,78]))
print('78->94 @', find([78,94]))
print('77-78-94-82-06 @', find([77,78,94,82,6]), '(F14 banked @1179/@1350)')
print('94-82-06 @', find([94,82,6]))
print('78-45-13-55-61-94 @', find([78,45,13,55,61,94]))
print('61->94 @', find([61,94]))
print('87->77 @', find([87,77]))
print('77->86 @', find([77,86]))
print('86->29 @', find([86,29]))
print('11->78 n =', big[(11,78)], '| 47->78 n =', big[(47,78)], '| 87->78 n =', big[(87,78)])
print('78->40 n =', big[(78,40)], '| 67->78 n =', big[(67,78)])
print('64->77 n =', big[(64,77)], '| 67->77 n =', big[(67,77)], '| 06->77 n =', big[(6,77)])
print('67-77-81 @', find([67,77,81]))

# era models (independent re-implementation)
def words_elision(path):
    txt = open(path, encoding='utf-8').read().lower().replace('’', "'").replace('‘', "'")
    txt = re.sub(r"([a-zà-ÿ])'([a-zà-ÿ])", r'\1 \2', txt)
    return re.findall(r'[a-zà-ÿ]+', txt)

DATA = LANE / 'data'
words = words_elision(DATA/'gutenberg-30513-tocqueville-t1.txt') + words_elision(DATA/'gutenberg-30514-tocqueville-t2.txt')
wu = collections.Counter(words); wb = collections.Counter(zip(words, words[1:])); wN = len(words)
print('\n=== era word-space ===')
print('wN =', wN)
p_me = wu['me']/wN
print(f'P(me) word = {p_me:.6f} -> L1w = {cf[78]/n/p_me:.2f}x (claim 22.76x)')
print('("la","me") =', wb[('la','me')], '| ("ce","me") =', wb[('ce','me')], '| ("me","ne") =', wb[('me','ne')], '| ("le","me") =', wb[('le','me')], '| ("ce","le") =', wb[('ce','le')])
# Leg A era: P(inf|le)
NONV = {'mer','fer','ver','hier','enfer','amer'}
def is_inf(w):
    return len(w) > 3 and w not in NONV and bool(re.search(r'(er|ir|oir|yer)$', w))
n_inf = sum(c for (a,b),c in wb.items() if a=='le' and is_inf(b))
print(f'P(inf|le) = {n_inf}/{wu["le"]} = {n_inf/wu["le"]:.4f} (claim 507/4570=0.1109)')
print(f'Leg A: P(86|77)={big[(77,86)]}/{cf[77]}={big[(77,86)]/cf[77]:.4f} ratio={(big[(77,86)]/cf[77])/(n_inf/wu["le"]):.3f}x (claim 1.024x)')
print(f'Leg C: P(77)={cf[77]/n:.5f} vs P(le)={wu["le"]/wN:.6f} ratio={(cf[77]/n)/(wu["le"]/wN):.3f}x (claim 1.152x)')
# vernement / verrement
n_vernement = sum(c for w,c in wu.items() if 'vernement' in w)
n_verrement = sum(c for w,c in wu.items() if 'verrement' in w)
n_nement = sum(c for w,c in wu.items() if 'nement' in w)
n_rement = sum(c for w,c in wu.items() if 'rement' in w and 'nement' not in w)
print(f'vernement={n_vernement} (claim 554) | verrement={n_verrement} (claim 0) | nement={n_nement} (claim 641) | rement={n_rement} (claim 282)')

# syllabifier (battery4 recipe) for L1s
def strip_acc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
VOW = set('aeiouy'); LIQ = {'bl','cl','fl','gl','pl','br','cr','dr','fr','gr','pr','tr','vr'}; DIG = {'ch','ph','th','gn'}
def syllabify(word):
    w = strip_acc(word.lower())
    if not w: return []
    toks=[]; i,nn=0,len(w)
    while i<nn:
        if w[i] in VOW:
            j=i
            while j<nn and w[j] in VOW: j+=1
            toks.append(('V',w[i:j])); i=j
        else:
            j=i
            while j<nn and w[j] not in VOW: j+=1
            toks.append(('C',w[i:j])); i=j
    syls,cur,idx=[], '',0
    if toks and toks[0][0]=='C': cur,idx=toks[0][1],1
    while idx<len(toks):
        typ,val=toks[idx]
        if typ!='V': cur+=val; idx+=1; continue
        if idx+1<len(toks) and toks[idx+1][0]=='C':
            cc=toks[idx+1][1]
            if idx+2<len(toks) and toks[idx+2][0]=='V':
                onset=cc[-1]
                if len(cc)>=2 and (cc[-2:] in LIQ or cc[-2:] in DIG): onset=cc[-2:]
                cur+=val+cc[:-len(onset)]; syls.append(cur); cur=onset; idx+=2
            else: cur+=val+cc; idx+=2
        else: cur+=val; idx+=1; syls.append(cur); cur=''
    if cur: syls.append(cur)
    return [s for s in syls if s]
stream=[]
for w in words: stream.extend(syllabify(w))
eu=collections.Counter(stream); eN=len(stream)
p_me_syl = eu['me']/eN
print(f'\n=== era syllable-space ===')
print(f'P(me) syll = {p_me_syl:.6f} -> L1s = {cf[78]/n/p_me_syl:.3f}x (claim 1.131x)')
print('top me-hosts:', [w for w,c in wu.most_common(40000) if 'me' in w][:0])
