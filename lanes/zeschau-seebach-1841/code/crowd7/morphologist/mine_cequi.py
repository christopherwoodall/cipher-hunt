#!/usr/bin/env python3
"""Round-7 MORPHOLOGIST: mine the period diplomatic corpus (code/side-period/corpus/)
for the "ce qui __ ce que" frame rate (work order 10, leg iii) and the
"ce qui" verb-follower profile (work order 10, leg ii support).

Also re-derives the Tocqueville comparison (F30 era).
"""
import re, glob, os, json
from collections import Counter

CORP = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus')
HERE = os.path.dirname(os.path.abspath(__file__))

def tokenize(text):
    text = text.replace('-\n', '').replace('-\r\n', '')
    text = text.lower()
    # keep French elisions as attached: "l'homme" -> "l'homme"; split "qu'il"? keep as one token
    toks = re.findall(r"[a-zàâäéèêëîïôöùûüçœæ]+(?:'[a-zàâäéèêëîïôöùûüçœæ]+)?", text)
    return toks

def load_corpus():
    toks = []
    files = sorted(glob.glob(os.path.join(CORP, '*.txt')))
    for f in files:
        if os.path.basename(f) in ('PROVENANCE.md', 'harvest-log.txt'):
            continue
        t = open(f, encoding='utf-8', errors='replace').read()
        toks.extend(tokenize(t))
    return toks

print('loading corpus...', flush=True)
T = load_corpus()
NW = len(T)
print('diplomatic tokens:', NW)

out = {'n_tokens': NW}

# 1. "ce qui" + gap(1-3) + "ce que" frames
fillers = Counter()
frame_pos = []
for i in range(NW - 6):
    if T[i] == 'ce' and T[i+1] == 'qui':
        for d in (1, 2, 3):
            if T[i+2+d] == 'ce' and T[i+3+d] == 'que':
                fill = tuple(T[i+2:i+2+d])
                fillers[fill] += 1
                frame_pos.append((i, fill))
                break
out['ce_qui_gap_ce_que'] = {'n': sum(fillers.values()),
                            'fillers': {' '.join(k): v for k, v in fillers.most_common(40)}}
out['ce_qui_gap_ce_que']['rate_per_100k'] = sum(fillers.values()) / NW * 1e5

# 2. "ce qui par ce que" 5-gram and "ce qui parce que" 4-gram
def seq_count(words):
    L = len(words)
    return sum(1 for i in range(NW - L + 1) if T[i:i+L] == list(words))
out['ce_qui_par_ce_que_5gram'] = seq_count(['ce', 'qui', 'par', 'ce', 'que'])
out['ce_qui_parce_que_4gram'] = seq_count(['ce', 'qui', 'parce', 'que'])
out['par_ce_que_3gram'] = seq_count(['par', 'ce', 'que'])
out['n_ce_qui'] = seq_count(['ce', 'qui'])
out['n_ce_que'] = seq_count(['ce', 'que'])

# 3. immediate followers of "ce qui" (top 30) — verb profile for leg (ii)
after = Counter()
for i in range(NW - 2):
    if T[i] == 'ce' and T[i+1] == 'qui':
        after[T[i+2]] += 1
tot = sum(after.values())
out['after_ce_qui'] = {'n': tot, 'top30': after.most_common(30)}

# 4. "qui" + verb-ish: P(word after ce qui is a verb form)? report top verbs among followers
#    crude: followers ending in common verb endings
verb_end = ('er', 'ir', 're', 'ait', 'aient', 'ant', 'é', 'ée', 'és', 'ées', 'u', 'i')
verbish = [(w, c) for w, c in after.most_common(60)
           if w.endswith(verb_end) and len(w) > 3]
out['after_ce_qui']['verbish_top'] = verbish[:20]

# 5. Tocqueville comparison (F30 era) — same measures
import sys
sys.path.insert(0, os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd4'))
import syllabary4 as S
S._era_init()
ERA = S._ERA
EW = len(ERA)
efill = Counter()
for i in range(EW - 6):
    if ERA[i] == 'ce' and ERA[i+1] == 'qui':
        for d in (1, 2, 3):
            if ERA[i+2+d] == 'ce' and ERA[i+3+d] == 'que':
                efill[tuple(ERA[i+2:i+2+d])] += 1
                break
def eseq(words):
    L = len(words)
    return sum(1 for i in range(EW - L + 1) if ERA[i:i+L] == list(words))
eafter = Counter()
for i in range(EW - 2):
    if ERA[i] == 'ce' and ERA[i+1] == 'qui':
        eafter[ERA[i+2]] += 1
out['tocqueville'] = {
    'n_tokens': EW,
    'ce_qui_gap_ce_que': {'n': sum(efill.values()),
                         'fillers': {' '.join(k): v for k, v in efill.most_common(20)},
                         'rate_per_100k': sum(efill.values()) / EW * 1e5},
    'ce_qui_par_ce_que_5gram': eseq(['ce', 'qui', 'par', 'ce', 'que']),
    'ce_qui_parce_que_4gram': eseq(['ce', 'qui', 'parce', 'que']),
    'par_ce_que_3gram': eseq(['par', 'ce', 'que']),
    'n_ce_qui': eseq(['ce', 'qui']),
    'after_ce_qui_top20': eafter.most_common(20),
}

with open(os.path.join(HERE, 'cequi_diplomatic.json'), 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)

print('=== DIPLOMATIC ===')
print('ce qui __ ce que frames:', out['ce_qui_gap_ce_que']['n'],
      'rate/100k:', round(out['ce_qui_gap_ce_que']['rate_per_100k'], 3))
print('fillers:', json.dumps(out['ce_qui_gap_ce_que']['fillers'], ensure_ascii=False)[:2000])
print('ce qui par ce que 5gram:', out['ce_qui_par_ce_que_5gram'])
print('ce qui parce que 4gram:', out['ce_qui_parce_que_4gram'])
print('par ce que 3gram:', out['par_ce_que_3gram'])
print('n ce qui:', out['n_ce_qui'])
print('after ce qui top30:', out['after_ce_qui']['top30'])
print('verbish:', out['after_ce_qui']['verbish_top'])
print()
print('=== TOCQUEVILLE ===')
print('frames:', out['tocqueville']['ce_qui_gap_ce_que'])
print('5gram:', out['tocqueville']['ce_qui_par_ce_que_5gram'],
      '4gram:', out['tocqueville']['ce_qui_parce_que_4gram'],
      'par ce que:', out['tocqueville']['par_ce_que_3gram'])
print('after ce qui:', out['tocqueville']['after_ce_qui_top20'])
print('wrote cequi_diplomatic.json')
