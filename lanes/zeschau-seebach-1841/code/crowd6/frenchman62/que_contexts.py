#!/usr/bin/env python3
"""Inspect the era 'on que' / 'il que' instances behind P(que|on), P(que|il)."""
import re
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
DATA = LANE / 'data'
def words(path):
    t = open(path, encoding='utf-8', errors='replace').read().lower()
    t = re.sub(r"[']", "'", t)
    t = re.sub(r"\b([a-zàâäéèêëîïôöùûüç]+)'([a-zàâäéèêëîïôöùûüç]+)", r"\1' \2", t)
    return re.findall(r"[a-zàâäéèêëîïôöùûüç]+(?:'[a-zàâäéèêëîïôöùûüç]+)?", t)
toks = words(DATA/'gutenberg-30513-tocqueville-t1.txt') + words(DATA/'gutenberg-30514-tocqueville-t2.txt')
for w in ['on','il','qui']:
    print(f'--- "{w} que" instances ---')
    n=0
    for i in range(len(toks)-1):
        if toks[i]==w and toks[i+1] in ('que','qu'):
            ctx = ' '.join(toks[max(0,i-4):i+5])
            print('  ', ctx); n+=1
            if n>=10: break
    if n==0: print('   (none)')
