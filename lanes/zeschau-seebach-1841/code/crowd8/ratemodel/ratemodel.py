"""Round-8 WO5 rate-model repair battery (see PREREG.md)."""
import re, json, math, collections, os

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
C = os.path.join(LANE, 'code', 'side-period', 'corpus')

def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

# ---------- cipher side ----------
import sys
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'redteam'))
from verify_baseline import load_stream
seq = ['%02d' % g for g in load_stream()]
N = len(seq)
assert N == 1847, N
o00 = [i for i, g in enumerate(seq) if g == '00']
pre = {i: seq[i-1] if i > 0 else None for i in o00}
pour_class = [i for i in o00 if pre[i] != '96']
print('cipher: N=%d n00=%d pour-class=%d' % (N, len(o00), len(pour_class)))
P00 = len(o00) / N
# clustering: 20 blocks
B = 20
blocks = [0]*B
for i in o00:
    blocks[min(B-1, i*B//N)] += 1
mean = sum(blocks)/B
var = sum((b-mean)**2 for b in blocks)/B
print('00 block counts:', blocks)
print('index of dispersion var/mean = %.2f (1.0=Poisson)' % (var/mean if mean else 0))

# ---------- document splitting ----------
def split_nesselrode():
    txt = open(os.path.join(C, 'nesselrode-v8.txt'), encoding='utf-8', errors='replace').read()
    months = 'janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre'
    pat = re.compile(r'^((?:Saint-Pétersbourg|Berlin|Paris|Londres|Vienne|Varsovie|Constantinople|Munich|Dresde)[ ,.\u00a0]*\d{1,2}\s+(?:%s)\s+184[0-6])\.?,?\s*$' % months, re.M)
    bounds = [m.start() for m in pat.finditer(txt)]
    print('nesselrode-v8 dateline splits:', len(bounds))
    docs = [txt[a:b] for a, b in zip(bounds, bounds[1:]+[len(txt)])]
    return [('nesselrode-v8#%d' % k, d) for k, d in enumerate(docs)]

def split_levant_paras():
    # levant No.-documents are mixed-language (English despatch + French enclosures);
    # document-level vote misclassifies. Use paragraph-level French filtering instead.
    txt = open(os.path.join(C, 'levant-correspondence-1841-p3.txt'), encoding='utf-8', errors='replace').read()
    paras = re.split(r'\n\s*\n', txt)
    fr_paras = []
    for p in paras:
        w = tok(p)
        if len(w) < 25:
            continue
        fr, en = langvote(w)
        if fr > en and fr >= 8:
            fr_paras.append(w)
    print('levant French-majority paragraphs:', len(fr_paras))
    return fr_paras

FR = set('le la les de des du et est que qui pour dans une un son sa ses leur leurs nous vous il elle ils elles ce cette ces mon ma mes ton ta tes au aux en sur par avec sans sous entre vers chez comme plus tout toute tous toutes aussi mais ou donc car ni ne pas bien tres grand faire etre avoir dit monsieur madame votre notre dont lorsque puisque parce afin apres avant depuis pendant contre'.split())
EN = set('the and of to in that was for with from your lordship which have has had are were been being this these those their them they him his her you our not but all any can will shall would should may might must upon between under over after before lord sir honour obedient servant humble majesty government despatch received inclosure house parliament'.split())

def langvote(words):
    c = collections.Counter(words)
    fr = sum(c[w] for w in FR); en = sum(c[w] for w in EN)
    return fr, en

docs = split_nesselrode()
levant_fr_paras = split_levant_paras()
docstats = []
for name, d in docs:
    w = tok(d)
    if len(w) < 40:
        continue
    fr, en = langvote(w)
    lang = 'fr' if fr > en else ('en' if en > fr else 'amb')
    wu = collections.Counter(w)
    npour = wu['pour']
    nq = sum(1 for a, b in zip(w, w[1:]) if a == 'pour' and b == 'que')
    nsyll = sum(1 for x in w if x.startswith('pour'))
    docstats.append(dict(name=name, lang=lang, n=len(w), fr=fr, en=en,
                         npour=npour, nq=nq, nsyll=nsyll))

fr_docs = [d for d in docstats if d['lang'] == 'fr']
en_docs = [d for d in docstats if d['lang'] == 'en']
print('docs: total=%d fr=%d en=%d amb=%d' % (len(docstats), len(fr_docs), len(en_docs),
      len(docstats)-len(fr_docs)-len(en_docs)))

# H-LANG: pooled French rate (nesselrode letters + levant French paragraphs)
def pool(ds):
    n = sum(d['n'] for d in ds); npour = sum(d['npour'] for d in ds)
    nq = sum(d['nq'] for d in ds); nsyll = sum(d['nsyll'] for d in ds)
    return n, npour, nq, nsyll

def pool_paras(paras):
    wu = collections.Counter()
    nq = 0
    for w in paras:
        wu.update(w)
        nq += sum(1 for a, b in zip(w, w[1:]) if a == 'pour' and b == 'que')
    n = sum(wu.values())
    return n, wu['pour'], nq, sum(c for tok_, c in wu.items() if tok_.startswith('pour'))

n, npour, nq, nsyll = pool(fr_docs)
nL, npL, nqL, nsL = pool_paras(levant_fr_paras)
nT, npT, nqT, nsT = n+nL, npour+npL, nq+nqL, nsyll+nsL
P_pour = npT/nT; Pq = nqT/npT if npT else 0
r1 = P00/P_pour; r3 = (4/55)/Pq if Pq else None
print('H-LANG French pool (nesselrode letters + levant FR paras): N=%d n_pour=%d P_pour=%.5f r1=%.2fx | n_pour_que=%d Pque|pour=%.4f r3(4/55)=%s' %
      (nT, npT, P_pour, r1, nqT, Pq, ('%.2fx' % r3) if r3 else 'n/a'))
print('   levant FR paras: N=%d n_pour=%d P_pour=%.5f (vs nesselrode %.5f)' % (nL, npL, npL/nL if nL else 0, npour/n if n else 0))

# ---------- H-SYLL ----------
r1_syll = P00/(nsT/nT)
print('H-SYLL: P(token startswith pour)=%.5f r1_syll=%.2fx' % (nsT/nT, r1_syll))

# ---------- H-CLASS ----------
print('H-CLASS: pour-class 52/1847 vs French P_pour: r1=%.2fx' % ((52/N)/P_pour))

# ---------- beta-binomial helpers ----------
def bb_fit(pairs_nk):
    # method of moments on per-doc rates
    ks = [k for _, k in pairs_nk]; ns = [n for n, _ in pairs_nk]
    K = sum(ks); Nn = sum(ns)
    m = K/Nn
    # weighted sample variance of p_i around m
    wsum = sum(ns)
    s2 = sum(n*((k/n)-m)**2 for n, k in pairs_nk)/wsum
    nbar = wsum/len(pairs_nk)
    # s2 ~= m(1-m)*(rho + (1-rho)/nbar) -> solve rho
    denom = m*(1-m)*(1-1/nbar)
    rho = (s2 - m*(1-m)/nbar)/denom if denom > 0 else 0.0
    rho = min(0.999, max(0.0, rho))
    return m, rho

def bb_sf(k, n, m, rho):
    # P(X >= k) for BetaBinomial(n, a, b); log-space throughout
    from math import lgamma, exp
    if rho <= 0:
        # log-space binomial tail
        tot = 0.0
        lp0 = lgamma(n+1)
        lpm, lq = math.log(m), math.log(1-m)
        for i in range(k, n+1):
            lp = lp0-lgamma(i+1)-lgamma(n-i+1) + i*lpm + (n-i)*lq
            tot += exp(lp)
            if exp(lp) < 1e-300 and i > k+50:
                break
        return tot
    a = m*(1-rho)/rho; b = (1-m)*(1-rho)/rho
    tot = 0.0
    lconst = lgamma(a+b)-lgamma(a)-lgamma(b)
    for i in range(k, n+1):
        lp = (lgamma(n+1)-lgamma(i+1)-lgamma(n-i+1) + lgamma(i+a)+lgamma(n-i+b)-lgamma(n+a+b)
              + lconst)
        tot += exp(lp)
    return tot

# H-DISP-B1
nk1 = [(d['n'], d['npour']) for d in fr_docs if d['n'] >= 40]
m1, rho1 = bb_fit(nk1)
p1 = bb_sf(55, N, m1, rho1)
print('H-DISP-B1: docs=%d m=%.5f rho=%.3f P(X>=55|n=1847)=%.4f %s' %
      (len(nk1), m1, rho1, p1, 'REPAIRED' if p1 >= 0.05 else 'not repaired'))
rates = sorted(d['npour']/d['n'] for d in fr_docs)
print('   per-doc P(pour): max=%.5f p95=%.5f median=%.5f cipher=%.5f pct=%.1f%%' %
      (rates[-1], rates[int(0.95*len(rates))], rates[len(rates)//2], P00,
       100*sum(1 for r in rates if r < P00)/len(rates)))
# H-DISP-B3
nk3 = [(d['npour'], d['nq']) for d in fr_docs if d['npour'] >= 3]
m3, rho3 = bb_fit(nk3)
p3 = bb_sf(4, 55, m3, rho3)
print('H-DISP-B3: docs=%d m=%.4f rho=%.3f P(X>=4|n=55)=%.4f %s' %
      (len(nk3), m3, rho3, p3, 'REPAIRED' if p3 >= 0.05 else 'not repaired'))

out = dict(H_LANG=dict(r1_french=r1, r3_french=r3),
           H_SYLL=dict(r1_syll=r1_syll),
           H_CLASS_52=dict(r1=(52/N)/P_pour),
           H_DISP_B1=dict(m=m1, rho=rho1, p_ge55=p1, repaired=p1 >= 0.05),
           H_DISP_B3=dict(m=m3, rho=rho3, p_ge4=p3, repaired=p3 >= 0.05),
           docs=dict(total=len(docstats), fr=len(fr_docs), en=len(en_docs)),
           cipher_dispersion=var/mean if mean else 0)
json.dump(out, open(os.path.join(LANE, 'code', 'crowd8', 'ratemodel', 'ratemodel_results.json'), 'w'), indent=1)
print('wrote ratemodel_results.json')
