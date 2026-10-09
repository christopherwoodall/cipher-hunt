#!/usr/bin/env python3
"""Verse-vs-dialogue census: reinforced-head + bare exclamatory infinitive in the
comedy corpus (18 files), split by sung-verse (AIR-marked couplets) vs spoken dialogue.

Verse region: from a line matching ^(AIR|Air)\\b until the next ALL-CAPS speaker
header (ending '.'), a 'Scène N.' line, or EOF. Method limitation: tails of long
vaudeville songs may bleed a few dialogue lines; every candidate is hand-checked.
"""
import re, json, os

CORPUS = os.path.expanduser(
    '~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus')
OUT = os.path.expanduser(
    '~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd17/next-token')

def is_caps(s):
    letters = [c for c in s if c.isalpha()]
    return len(letters) >= 2 and all(not c.islower() for c in letters)

def is_speaker(line):
    l = line.strip()
    if not l.endswith('.'):
        return False
    return is_caps(l[:-1])

AIR = re.compile(r'^\s*(AIR|Air)\b')
SCENE = re.compile(r'^\s*Sc[eè]ne\b')
DEM_REINF = re.compile(
    r'\b(celui-là|celle-là|ceux-là|celles-là|celui-ci|celle-ci|ceux-ci|celles-ci)\b',
    re.IGNORECASE)
SEP = re.compile(r'[,;:\u2014\u2013\-()]')
INF = re.compile(r"\b[a-zàâäéèêëîïôöùûüÿç]{3,}(er|ir|re|oir)\b", re.IGNORECASE)

files = sorted(f for f in os.listdir(CORPUS) if f.endswith('.txt')
               and (f.startswith('labiche-') or f.startswith('scribe-')))

stats = {'files': files, 'n_files': len(files)}
candidates = []
heads_total = 0

for fname in files:
    text = open(os.path.join(CORPUS, fname), encoding='utf-8').read()
    lines = text.split('\n')
    # build partition: mark verse spans as (start_char, end_char)
    spans = []
    in_verse = False
    pos = 0
    vstart = 0
    line_start = []
    for ln in lines:
        line_start.append(pos)
        pos += len(ln) + 1
    n = len(lines)
    for i, ln in enumerate(lines):
        if AIR.match(ln):
            if in_verse:
                spans.append((vstart, line_start[i]))
            in_verse = True
            vstart = line_start[i]
            continue
        if in_verse and (is_speaker(ln) or SCENE.match(ln)):
            in_verse = False
            spans.append((vstart, line_start[i]))
    if in_verse:
        spans.append((vstart, len(text)))

    def in_verse_off(off):
        return any(a <= off < b for a, b in spans)

    for m in DEM_REINF.finditer(text):
        heads_total += 1
        tail = text[m.start():m.start() + 400]
        sepm = SEP.search(tail[len(m.group(0)):])
        if not sepm:
            continue
        seppos = m.start() + len(m.group(0)) + sepm.start()
        win = text[m.start():m.start() + 400]
        if '!' not in win:
            continue
        if not INF.search(win):
            continue
        candidates.append({
            'file': fname,
            'offset': m.start(),
            'head': m.group(0),
            'sep': sepm.group(0),
            'partition': 'verse' if in_verse_off(m.start()) else 'dialogue',
            'window': win[:400],
        })

stats['heads_total'] = heads_total
stats['n_candidates'] = len(candidates)
stats['verse_candidates'] = sum(1 for c in candidates if c['partition'] == 'verse')
stats['dialogue_candidates'] = sum(1 for c in candidates if c['partition'] == 'dialogue')

json.dump({'stats': stats, 'candidates': candidates},
          open(os.path.join(OUT, 'disloc-reinforced-verse-vs-prose-comedy_census.json'),
               'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(stats, indent=1))
for c in candidates:
    print('=====', c['file'], c['offset'], c['partition'], repr(c['head']), 'sep=', repr(c['sep']))
    print(c['window'].replace('\n', ' / ')[:300])
