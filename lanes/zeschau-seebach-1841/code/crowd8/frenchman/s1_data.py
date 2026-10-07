#!/usr/bin/env python3
"""Round-8 FRENCHMAN step 1: data — 93 windows, 77/78/5-mer windows,
diplo l' rate + following-vowel distribution (elision-split tokenizer)."""
import json, re, glob, os, collections
from pathlib import Path
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import util
from util import PAIRS, N, UNI, GT, followers, predecessors, window, positions

CORP = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus')

def tokenize_elision(text):
    text = text.replace('-\n', '').replace('-\r\n', '')
    text = text.lower()
    text = re.sub(r"[’‘`]", "'", text)
    text = re.sub(r"\b([a-zàâäéèêëîïôöùûüçœæ]+)'([a-zàâäéèêëîïôöùûüçœæ]+)", r"\1' \2", text)
    return re.findall(r"[a-zàâäéèêëîïôöùûüçœæ]+'?|[a-zàâäéèêëîïôöùûüçœæ]+", text)

def load_diplo():
    toks = []
    for f in sorted(glob.glob(os.path.join(CORP, '*.txt'))):
        if os.path.basename(f) in ('PROVENANCE.md', 'harvest-log.txt'):
            continue
        t = open(f, encoding='utf-8', errors='replace').read()
        toks.extend(tokenize_elision(t))
    return toks

print('loading diplo...', flush=True)
D = load_diplo()
ND = len(D)
DU = collections.Counter(D)
DB = collections.Counter(zip(D, D[1:]))
print('diplo tokens:', ND)

def lstats(toks, name):
    eu = collections.Counter(toks); n = len(toks)
    nl = eu["l'"]
    # following-vowel-class distribution
    vcls = collections.Counter()
    hosts = collections.Counter()
    pres = collections.Counter()
    for i, t in enumerate(toks):
        if t == "l'" and i + 1 < n:
            h = toks[i+1]
            hosts[h] += 1
            v = h[0] if h else '?'
            # normalize accented
            v = {'é':'e','è':'e','ê':'e','ë':'e','à':'a','â':'a','î':'i','ï':'i',
                 'ô':'o','ö':'o','ù':'u','û':'u','ü':'u','ç':'c'}.get(v, v)
            vcls['front' if v in 'ie' else ('back' if v in 'aouy' else 'other')] += 1
        if t == "l'" and i > 0:
            pres[toks[i-1]] += 1
    print(f'\n=== {name}: n(l\')={nl} P={nl/n:.5f} E[n93|H0]={nl/n*N:.1f}')
    print('  vowel class of host:', dict(vcls))
    print('  top hosts:', hosts.most_common(12))
    print('  top predecessors:', pres.most_common(12))
    return eu, nl, vcls, hosts, pres

eu_d, nl_d, vcls_d, hosts_d, pres_d = lstats(D, 'DIPLO')
T = util.toks()
eu_t, nl_t, vcls_t, hosts_t, pres_t = lstats(T, 'TOCQUEVILLE')

# qu'on / l'on / qu'il rates in diplo
def bigram_rate(toks, eu, a, b):
    return sum(1 for i in range(len(toks)-2) if toks[i]==a and toks[i+1]==b)
print('\ndiplo: qu\'on =', bigram_rate(D, DU, "qu'", 'on'),
      '| l\'on =', bigram_rate(D, DU, "l'", 'on'),
      '| qu\'il =', bigram_rate(D, DU, "qu'", 'il'),
      '| si l\'on =', sum(1 for i in range(ND-3) if D[i]=='si' and D[i+1]=="l'" and D[i+2]=='on'))
print('diplo: n(on)=', DU['on'], 'n(il)=', DU['il'], 'n(que)=', DU['que'], 'n(ne)=', DU['ne'], "n(n')=", DU["n'"])

# ---------- cipher: 93 windows ----------
print('\n=== 93 windows (n=%d) ===' % UNI[93])
for i in positions(93):
    print(' @%4d pre=%3d fol=%3d : %s' % (i, PAIRS[i-1] if i>0 else -1,
          PAIRS[i+1] if i+1<N else -1, window(i, 3)))
print('93 followers:', dict(followers(93)))
print('93 predecessors:', dict(predecessors(93)))
print('93->62:', sum(1 for i in positions(93) if i+1<N and PAIRS[i+1]==62))

# ---------- cipher: 77/78/5-mer ----------
print('\n=== 5-mer 77-78-94-82-06 positions ===')
mer = [i for i in range(N-4) if PAIRS[i:i+5]==[77,78,94,82,6]]
print(mer)
for i in mer:
    print(' @%4d: %s' % (i, window(i, 5)))
print('\n=== all 77->78 windows ===')
for i in range(N-1):
    if PAIRS[i]==77 and PAIRS[i+1]==78:
        print(' @%4d: %s' % (i, window(i, 4)))
print('\n=== 78->94 windows ===')
for i in range(N-1):
    if PAIRS[i]==78 and PAIRS[i+1]==94:
        print(' @%4d: %s' % (i, window(i, 4)))
print('\n=== 77 not followed by 78 (n=%d) — sample ===' % sum(1 for i in range(N-1) if PAIRS[i]==77 and PAIRS[i+1]!=78))
c=0
for i in range(N-1):
    if PAIRS[i]==77 and PAIRS[i+1]!=78:
        if c<25: print(' @%4d: %s' % (i, window(i,3)))
        c+=1
print('UNI[77]=',UNI[77],'UNI[78]=',UNI[78],'UNI[93]=',UNI[93],'UNI[8]=',UNI[8],'UNI[14]=',UNI[14])
