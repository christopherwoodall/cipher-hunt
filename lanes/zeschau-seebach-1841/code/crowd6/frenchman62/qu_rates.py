#!/usr/bin/env python3
"""P(pre='qu' | w) exact, and the H-split adverse computation for 46->62=0/29."""
import re, math, collections
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
DATA = LANE / 'data'
def words(path):
    t = open(path, encoding='utf-8', errors='replace').read().lower()
    t = re.sub(r"[']", "'", t)
    t = re.sub(r"\b([a-zàâäéèêëîïôöùûüç]+)'([a-zàâäéèêëîïôöùûüç]+)", r"\1' \2", t)
    return re.findall(r"[a-zàâäéèêëîïôöùûüç]+(?:'[a-zàâäéèêëîïôöùûüç]+)?", t)
toks = words(DATA/'gutenberg-30513-tocqueville-t1.txt') + words(DATA/'gutenberg-30514-tocqueville-t2.txt')
uni = collections.Counter(toks); bi = collections.Counter(zip(toks, toks[1:]))
for w in ['on','il','qui']:
    for pre in ['qu','que']:
        c = bi[(pre,w)]; nw = uni[w]
        print(f'P(pre="{pre}"|"{w}") = {c}/{nw} = {c/nw:.5f}')
print()
# H-split adverse: under 62="on", E[46->62] = 29 * P("qu"|"on"); obs 0
p_qu_on = bi[('qu','on')]/uni['on']
p_qu_il = bi[('qu','il')]/uni['il']
for label, p in [('on',p_qu_on),('il',p_qu_il)]:
    E = 29*p
    p0 = (1-p)**29
    print(f'62="{label}": E[46->62]=29*{p:.4f}={E:.2f}, P(0|H-split)=({1-p:.4f})^29={p0:.4f}')
# show some qu'on instances for register sanity
print('sample "qu\'on":')
n=0
for i in range(len(toks)-1):
    if toks[i]=='qu' and toks[i+1]=='on':
        print('  ',' '.join(toks[max(0,i-3):i+4])); n+=1
        if n>=6: break
