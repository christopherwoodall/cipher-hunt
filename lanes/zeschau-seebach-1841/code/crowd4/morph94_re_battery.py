"""Round 4, WO3 (morphologist): symmetric F30-legal battery for 94="re" vs 94="ne".

F30: rigid syllabification DEAD — no era-syllable-conditional legs on fragments.
All legs here are word-space (whole-word strings / word bigrams) or compositional
frames on ground-truth/provisional anchors. The "-nement"/"-rement" question is
tested at the letter-string level: under the recovered ear-cutting (upstream-syll*.py
inventory + round-3 evidence), ANY word containing "nement" is a legal host for a
...94-82-06 segmentation, likewise "rement" for ...94-82-06 under 94="re".

Ground truth: 11=la 70=pre 82=m 34=i 29=er 40=e 46=que
Provisional: 87=ce 64=qui 96=par 62=on(ear-lock) 52=pas(inconclusive)
"""
import json, os, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(LANE, 'data')

# ---------- cipher load (same alignment as upstream: offsets.json + ct_R5005.txt) ----------
def load_pairs():
    off = json.load(open(os.path.join(DATA, 'upstream-offsets.json')))
    pairs = []
    for line in open(os.path.join(DATA, 'upstream-ct_R5005.txt')):
        k, s = line.split()
        o = off[k]
        d = s[o:]
        pairs += [d[i:i + 2] for i in range(0, len(d) - 1, 2)]
    return pairs

pairs = load_pairs()
N = len(pairs)
print(f'pairs={N} distinct={len(set(pairs))}')
assert N == 1846, N

pos94 = [i for i, p in enumerate(pairs) if p == '94']
print(f'n94={len(pos94)} P94={len(pos94)/N:.5f}')

def window(i, r=7):
    lo, hi = max(0, i - r), min(N, i + r + 1)
    return ' '.join(pairs[lo:hi]), lo

# full adjacency
pre = collections.Counter(pairs[i - 1] for i in pos94 if i > 0)
suc = collections.Counter(pairs[i + 1] for i in pos94 if i + 1 < N)
print('94 predecessors:', dict(pre.most_common()))
print('94 successors:  ', dict(suc.most_common()))

# bigram / trigram families with positions
def find_pat(pat):
    L = len(pat)
    return [i for i in range(N - L + 1) if pairs[i:i + L] == pat]

fam_94_82 = find_pat(['94', '82'])
tri_94_82_06 = find_pat(['94', '82', '06'])
print('94-82 @', fam_94_82)
print('94-82-06 @', tri_94_82_06)
print('94-52-80 @', find_pat(['94', '52', '80']))
print('62-94-70-52 @', find_pat(['62', '94', '70', '52']))
print('82-94 @', find_pat(['82', '94']))
print('94-87 @', find_pat(['94', '87']))
print('77-78-94-82-06 @', find_pat(['77', '78', '94', '82', '06']))

for i in fam_94_82:
    w, lo = window(i, 6)
    print(f'--- 94-82 @{i}: [{lo}]', w)
for i in pos94:
    if pairs[i + 1] != '82':
        w, lo = window(i, 5)
        print(f'--- 94 @{i} ->{pairs[i+1]} (pre={pairs[i-1] if i>0 else "-"}): [{lo}]', w)

# ---------- era corpus: word-space ----------
def load_era():
    words = []
    for fn in ['gutenberg-30513-tocqueville-t1.txt', 'gutenberg-30514-tocqueville-t2.txt']:
        txt = open(os.path.join(DATA, fn), encoding='utf-8').read().lower()
        txt = txt.replace('\u2019', "'").replace('\u2018', "'")
        # split elisions: l'homme -> l' homme ; m'en -> m' en
        txt = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', txt)
        words += re.findall(r"[a-z\u00e0-\u00ff]+", txt)
    return words

words = load_era()
W = len(words)
print(f'era words={W}')
wc = collections.Counter(words)
n_nement = sum(c for w, c in wc.items() if 'nement' in w)
n_rement = sum(c for w, c in wc.items() if 'rement' in w)
both = sum(c for w, c in wc.items() if 'nement' in w and 'rement' in w)
print(f"words w/ 'nement': {n_nement}  ({n_nement/W:.6f})")
print(f"words w/ 'rement': {n_rement}  ({n_rement/W:.6f})")
print(f'both: {both}')
print('top nement hosts:', wc.most_common() and [ (w,c) for w,c in wc.most_common(4000) if 'nement' in w][:12])
print('top rement hosts:', [(w,c) for w,c in wc.most_common(4000) if 'rement' in w][:12])
print("word 'ne':", wc.get('ne',0), wc.get('ne',0)/W)
print("word 'en':", wc.get('en',0), wc.get('en',0)/W)
# word bigrams
bi = collections.Counter(zip(words, words[1:]))
def p_bigram(a,b):
    return bi.get((a,b),0), bi.get((a,b),0)/max(1,wc.get(a,0))
for a,b in [('on','ne'),('ne','pas'),('en','ce'),('ne','que'),('que','ne'),('on','en'),('en','pas')]:
    n, p = p_bigram(a,b)
    print(f'era P({b}|{a}) = {n}/{wc.get(a,0)} = {p:.4f}')
# cipher-side analogs (group bigrams)
def cp(a,b):
    n = sum(1 for i in range(N-1) if pairs[i]==a and pairs[i+1]==b)
    d = pairs.count(a)
    return n, n/max(1,d)
for a,b in [('62','94'),('94','52'),('94','87'),('94','82'),('82','94'),('94','70')]:
    n,p = cp(a,b)
    print(f'cipher P({b}|{a}) = {n}/{pairs.count(a)} = {p:.4f}')

res = {
  'pairs': N, 'n94': len(pos94), 'P94': len(pos94)/N,
  'pre': dict(pre), 'suc': dict(suc),
  'fam_94_82': fam_94_82, 'tri_94_82_06': tri_94_82_06,
  'era_words': W, 'nement_hosts': n_nement, 'rement_hosts': n_rement,
  'nement_rate': n_nement/W, 'rement_rate': n_rement/W,
  'host_odds_ne_vs_re': n_nement/max(1,n_rement),
}
json.dump(res, open(os.path.join(HERE,'morph94_re_battery.json'),'w'), indent=1)
print('wrote morph94_re_battery.json')
