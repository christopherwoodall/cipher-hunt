"""1248-RE-RUN (round 12, WO6): pool-registered P-C re-run + double-pour license hunt.

Implements code/crowd12/rerun1248/PREREG.md. Writes rerun1248_raw.json
(all hit contexts for constituency reading); adjudication is a separate step.

PC-1: exhaustive "X peu que" census in Guizot-DIP (guizot-memoires-t5-t6.txt).
DP-1: strict "pour W1 W2 pour peu que" / "pour W1 W2 pour INF que" across the
      era-French pool, plus a descriptive k!=2 secondary scan.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORP = os.path.abspath(os.path.join(HERE, '..', '..', 'side-period', 'corpus'))

def load(p):
    return open(os.path.join(CORP, p), encoding='utf-8', errors='replace').read()

# ---------- lane tokenizer verbatim (round-10/11 arm1248) ----------
def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

def is_inf(w):
    return w.endswith(('er', 'ir', 're')) and len(w) > 3

def ctx(t, i, half=20):
    lo, hi = max(0, i - half), min(len(t), i + half + 1)
    return ' '.join(t[lo:hi])

# ---------- corpora ----------
# PC-1: Guizot-DIP only
guizot_dip = load('guizot-memoires-t5-t6.txt')
g_tok = tok(guizot_dip)

# DP-1 primary tier (era French): RDM-1841, Guizot-DIP, nesselrode v7/v9/v10,
# pozzo-di-borgo v1. v8 is scanned but reported separately (OCR-void constraint).
primary = {}
for q in ['q1', 'q2', 'q3', 'q4']:
    primary['RDM-1841-%s' % q] = load('revue-deux-mondes-1841-%s.txt' % q)
primary['Guizot-DIP'] = guizot_dip
for v in ['v7', 'v9', 'v10']:
    primary['nesselrode-%s' % v] = load('nesselrode-%s.txt' % v)
primary['pozzo-di-borgo-v1'] = load('pozzo-di-borgo-correspondance-v1.txt')
v8_raw = load('nesselrode-v8.txt')

# DP-1 secondary tier: guizot t1-t3 gutenberg (era French, memoir register)
secondary = {}
for n in ['t1', 't2', 't3']:
    secondary['guizot-%s-gutenberg' % n] = load('guizot-memoires-%s-gutenberg.txt' % n)

primary_tok = {k: tok(v) for k, v in primary.items()}
v8_tok = tok(v8_raw)
secondary_tok = {k: tok(v) for k, v in secondary.items()}

raw = {'pc1_peu_que_hits': [], 'dp_strict_peu': [], 'dp_strict_inf': [],
       'dp_kdepth_peu': [], 'dp_kdepth_inf': [],
       'corpus_bytes': {}, 'v8_strict_peu': [], 'v8_strict_inf': []}
for name, text in list(primary.items()) + [('nesselrode-v8', v8_raw)] + list(secondary.items()):
    raw['corpus_bytes'][name] = len(text)

# ---------- PC-1: "X peu que" census in Guizot-DIP ----------
for i in range(1, len(g_tok) - 1):
    if g_tok[i] == 'peu' and g_tok[i + 1] == 'que':
        raw['pc1_peu_que_hits'].append({
            'tokpos': i, 'x': g_tok[i - 1],
            'context': ctx(g_tok, i, 20)})

# ---------- DP-1 strict patterns ----------
def scan_strict(t, name, out_peu, out_inf):
    hits_peu, hits_inf = [], []
    for i in range(len(t) - 5):
        if t[i] == 'pour' and t[i + 3] == 'pour':
            if t[i + 4] == 'peu' and t[i + 5] == 'que':
                hits_peu.append({'corpus': name, 'tokpos': i,
                                 'w1': t[i + 1], 'w2': t[i + 2],
                                 'context': ctx(t, i, 20)})
            elif is_inf(t[i + 4]) and t[i + 5] == 'que':
                hits_inf.append({'corpus': name, 'tokpos': i,
                                 'w1': t[i + 1], 'w2': t[i + 2],
                                 'inf': t[i + 4],
                                 'context': ctx(t, i, 20)})
    return hits_peu, hits_inf

for name, t in primary_tok.items():
    hp, hi = scan_strict(t, name, None, None)
    raw['dp_strict_peu'].extend(hp)
    raw['dp_strict_inf'].extend(hi)
for name, t in secondary_tok.items():
    hp, hi = scan_strict(t, name, None, None)
    raw['dp_strict_peu'].extend(hp)
    raw['dp_strict_inf'].extend(hi)
hp, hi = scan_strict(v8_tok, 'nesselrode-v8', None, None)
raw['v8_strict_peu'] = hp
raw['v8_strict_inf'] = hi

# ---------- DP-1 secondary scan: k != 2 stack depths (descriptive) ----------
def scan_kdepth(t, name, out_peu, out_inf):
    for k in (1, 3, 4, 5):
        for i in range(len(t) - (k + 3)):
            if t[i] == 'pour' and t[i + k + 1] == 'pour':
                if t[i + k + 2] == 'peu' and t[i + k + 3] == 'que':
                    out_peu.append({'corpus': name, 'tokpos': i, 'k': k,
                                    'mid': t[i + 1:i + k + 1],
                                    'context': ctx(t, i, 20)})
                elif is_inf(t[i + k + 2]) and t[i + k + 3] == 'que':
                    out_inf.append({'corpus': name, 'tokpos': i, 'k': k,
                                    'mid': t[i + 1:i + k + 1],
                                    'inf': t[i + k + 2],
                                    'context': ctx(t, i, 20)})

for name, t in list(primary_tok.items()) + list(secondary_tok.items()):
    scan_kdepth(t, name, raw['dp_kdepth_peu'], raw['dp_kdepth_inf'])
scan_kdepth(v8_tok, 'nesselrode-v8', raw['dp_kdepth_peu'], raw['dp_kdepth_inf'])

# ---------- summary ----------
raw['summary'] = {
    'pc1_n_hits': len(raw['pc1_peu_que_hits']),
    'dp_strict_peu_n': len(raw['dp_strict_peu']),
    'dp_strict_inf_n': len(raw['dp_strict_inf']),
    'dp_kdepth_peu_n': len(raw['dp_kdepth_peu']),
    'dp_kdepth_inf_n': len(raw['dp_kdepth_inf']),
    'v8_strict_peu_n': len(raw['v8_strict_peu']),
    'v8_strict_inf_n': len(raw['v8_strict_inf']),
    'guizot_dip_tokens': len(g_tok),
    'primary_tokens': sum(len(t) for t in primary_tok.values()),
    'secondary_tokens': sum(len(t) for t in secondary_tok.values()),
}

outp = os.path.join(HERE, 'rerun1248_raw.json')
json.dump(raw, open(outp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(raw['summary'], indent=1))
print('wrote', outp)
