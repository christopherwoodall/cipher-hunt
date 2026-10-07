#!/usr/bin/env python3
"""Round-10 59COND: era batteries on Nesselrode v8 (closer's tokenizer)."""
import json, re, unicodedata
from pathlib import Path
from collections import Counter

LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
CORP = LANE / 'code' / 'side-period' / 'corpus'
WORD = re.compile(r"[a-zàâäéèêëîïôöùûüÿçœæ]+(?:'[a-zàâäéèêëîïôöùûüÿçœæ]+)*")

def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('’', "'").replace('‘', "'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p:
                continue
            toks.append(p + "'" if i < len(parts) - 1 else p)
    return toks

toks = tokenize((CORP / 'nesselrode-v8.txt').read_text(encoding='utf-8', errors='replace'))
N = len(toks)
uni = Counter(toks)
bi = Counter(zip(toks[:-1], toks[1:]))
tri = Counter(zip(toks[:-1], toks[1:], toks[2:]))
OUT = {'N': N}

def P2(a, b):
    return bi.get((a, b), 0) / uni[a] if uni[a] else 0.0

print('N =', N)
# --- -este verb inventory ---
este = sorted([(w, c) for w, c in uni.items()
               if re.fullmatch(r'[a-zàâäéèêëîïôöùûüç]{3,}este', w or '')],
              key=lambda kv: -kv[1])
OUT['este_inventory'] = este
print('--- -este inventory (nesselrode v8) ---')
for w, c in este:
    print('  %-14s %d' % (w, c))

# frame counts per candidate
frames = {}
for w, c in este:
    frames[w] = {
        'n': c,
        'qui_le_V': tri.get(('qui', 'le', w), 0),
        'V_que': bi.get((w, 'que'), 0),
        'la_V': bi.get(('la', w), 0),
        'V_le': bi.get((w, 'le'), 0),
        'ne_V_pas': sum(1 for i in range(N - 3)
                        if toks[i] in ("ne", "n'") and toks[i+1] == w and toks[i+2] == 'pas'),
    }
OUT['este_frames'] = frames
print('--- candidate frames ---')
for w, c in este:
    f = frames[w]
    print('  %-14s n=%4d qui_le=%d V_que=%d la_V=%d V_le=%d ne_V_pas=%d'
          % (w, c, f['qui_le_V'], f['V_que'], f['la_V'], f['V_le'], f['ne_V_pas']))

# --- misc frames ---
OUT['misc'] = {
    'l_est': bi.get(("l'", 'est'), 0),
    'c_est': bi.get(("c'", 'est'), 0),
    'en_est_que': sum(1 for i in range(N - 3)
                      if toks[i] == 'en' and toks[i+1] == 'est' and toks[i+2] == 'que'),
    'P_le_given_est': P2('est', 'le'),
    'n_est_le': bi.get(('est', 'le'), 0),
    'n_est': uni['est'],
    'n_est_le_pat': sum(1 for i in range(N - 2)
                        if toks[i] in ("n'", 'ne') and toks[i+1] == 'est' and toks[i+2] == 'le'),
    'la_est': bi.get(('la', 'est'), 0),
    'P_est_given_qui': P2('qui', 'est'),
    'P_est_given_np': P2("n'", 'est'),
}
for k, v in OUT['misc'].items():
    print('%-16s %s' % (k, v))

json.dump(OUT, open(LANE / 'code/crowd10/conditioner59/era_battery.json', 'w'), indent=1)
print('wrote era_battery.json')
