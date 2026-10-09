#!/usr/bin/env python3
"""cequi-par-corpus-widen: expanded prose census for the verbless
'ce qui par [N], ceci' correlative frame. Replicates the parent
ceci-correlative-corpus methodology on the widened French corpus."""
import os, re, json, glob

CORPUS = 'code/side-period/corpus'
GERMAN = set([os.path.basename(f) for f in glob.glob(os.path.join(CORPUS,'allgemeine-zeitung-*.txt'))]
             + ['adb-zeschau-heinrich-anton-von.txt',])
SKIP = {'PROVENANCE.md','PROVENANCE-delavigne-tragedies.txt','harvest-log.txt'}

files = sorted(f for f in glob.glob(os.path.join(CORPUS,'*.txt'))
               if os.path.basename(f) not in GERMAN and os.path.basename(f) not in SKIP)

def norm(t):
    return re.sub(r'\s+',' ',t)

exact_hits, gen_hits = [], []
total_chars = 0
for fp in files:
    raw = open(fp, encoding='utf-8', errors='replace').read()
    total_chars += len(raw)
    t = norm(raw)
    for m in re.finditer(r'ce\s+qui\s+par\b', t, re.I):
        s = max(0, m.start()-400); e = min(len(t), m.end()+400)
        exact_hits.append({'file': os.path.basename(fp), 'offset': m.start(),
                           'context': t[s:e]})
    for m in re.finditer(r'qui\s+par\b', t, re.I):
        window = t[m.start():m.start()+600]
        if re.search(r'\bceci\b', window, re.I):
            s = max(0, m.start()-200); e = min(len(t), m.start()+600)
            gen_hits.append({'file': os.path.basename(fp), 'offset': m.start(),
                             'context': t[s:e]})

out = {'nfiles': len(files), 'total_chars': total_chars,
       'nhits_exact': len(exact_hits), 'exact_hits': exact_hits,
       'nhits_generosity': len(gen_hits), 'generosity_hits': gen_hits,
       'files': [os.path.basename(f) for f in files]}
json.dump(out, open('code/crowd17/next-token/cequi-par-widen_census.json','w'), ensure_ascii=False, indent=1)
print('files:', len(files), 'chars:', total_chars)
print('exact hits:', len(exact_hits))
for h in exact_hits: print(' -', h['file'], h['offset'])
print('generosity hits:', len(gen_hits))
for h in gen_hits: print(' -', h['file'], h['offset'])
