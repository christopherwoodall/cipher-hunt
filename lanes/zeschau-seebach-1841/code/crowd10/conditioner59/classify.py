#!/usr/bin/env python3
"""Round-10 59COND: window classification table (locks the census reading).

Classes:
  EST       - 59 = word-"est", proclitic-licensed (pre in {64,94,93})
  ESTE      - 59 = verb-final "-este" syllable (verb-stem completion)
  ESTE_LEAN - ESTE favored but successor/frame has an open wrinkle
  NEUTRAL   - hostile-neutral per standing ruling (I3 @825)
  FENCED    - ambiguous, needs another cell's identity (not counted)
  LEFTOVER  - unclassified (incl. S5-fenced suc=37 x6 - not re-litigated)
"""
import json, os

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
d = json.load(open(os.path.join(LANE, 'code/crowd10/conditioner59/census_results.json')))
wins = {w['pos']: w for w in d['windows']}

CLS = {
    103:  ('EST',   'pre=93 "l\'" LEAD: "on ne l\'est [45]" - era l\'est=6 (Ness v8)'),
    316:  ('EST',   'pre=64 "qui": "qui est [32]" (F52 S2)'),
    1210: ('EST',   'pre=64 "qui": "qui est [32]" (F52 S2)'),
    1777: ('EST',   'pre=64 "qui": "ce qui est [19]" (F52 S2)'),
    559:  ('EST',   'pre=94 "ne": "n\'est [30]" (F52 S3)'),
    763:  ('EST',   'pre=94 "ne": "on n\'est [39]" (F52 S3)'),
    825:  ('NEUTRAL','87-59 "c\'est" candidate: I3 ruled hostile-neutral (RULINGS-ROUND7) - not counted'),
    216:  ('ESTE',  'pre=06 verb-stem-class: "[06-59] que" verb+que-clause; cleft "NP est que" hostile (06 non-nominal, F52-L2)'),
    1186: ('ESTE',  'pre=06 verb-stem-class: "ne me [06-59] [42]" (94=ne prov, 82=m GT); "[stem] est" ungrammatical'),
    1190: ('ESTE',  'pre=84: "[06-84-59] que" 3-syllable -este verb + que-clause; ISLET-1 en-lean ("[V] en est") strained'),
    1448: ('ESTE',  'pre=84: "qui le [84-59] [36]" - ISLET 8 frame; word-"est" era-absent (F65)'),
    1804: ('ESTE',  'pre=84: "[ce] qui le [84-59] [35]" - ISLET 8 frame; word-"est" era-absent (F65)'),
    448:  ('ESTE',  'pre=61: "on [61-59] [32]" (62=on fenced STRONG LEAD); "on [61] est" ungrammatical -> frame-forced'),
    1715: ('ESTE',  'pre=44: "ne [44-59] [30]" (94=ne prov); "ne [44] est" ungrammatical -> frame-forced; [30]=pas?'),
    554:  ('ESTE_LEAN','pre=86 verb-stem-class (F40): "[86-59] i" unit favored; successor 34=i unresolved'),
    1291: ('FENCED','pre=84: "[V-este] [35]" vs "la [17-84] est [35]" - ambiguous; needs 17/84/35'),
    1496: ('FENCED','"[15] est en [89-noun]" vs "[15-59=reste] en [89]" - ambiguous; needs 15'),
    463:  ('LEFTOVER','"la/cela [59]": "la est" era-0/3.96M -> 59!=est here; value open (verb has clitic-order problem)'),
    834:  ('LEFTOVER','"[76] [59] [35]" - 76/35 unknown; no licensed frame'),
    1511: ('LEFTOVER','"[61] [59] [39]": "[61] est [39]" possible (61 noun?) vs "[61-59] [39]"; needs 61/12'),
    1833: ('LEFTOVER','"i [59] [36]" (16="i" LEAD): "y est" would need 16=y - patternist lane; not touched'),
    528:  ('LEFTOVER','S5-fenced (59->37): "ce [44] [59] le qui" resists both - NOT re-litigated'),
    624:  ('LEFTOVER','S5-fenced (59->37) - NOT re-litigated'),
    912:  ('LEFTOVER','S5-fenced (59->37); 37!=le forced ("le par" x) - NOT re-litigated'),
    1178: ('LEFTOVER','S5-fenced (59->37); 37!=le forced ("le le" x) - NOT re-litigated'),
    1443: ('LEFTOVER','S5-fenced (59->37) - NOT re-litigated'),
    1796: ('LEFTOVER','S5-fenced (59->37): "n\'est le" era 10/3.96M (rare, not absent) - fence stands, NOT re-litigated'),
}
assert set(CLS) == set(wins), (set(wins) - set(CLS), set(CLS) - set(wins))

from collections import Counter
counts = Counter(v[0] for v in CLS.values())
print('classification counts:', dict(counts))
print('total:', sum(counts.values()), '(n59 = %d)' % d['n59'])

est  = [p for p, (c, _) in CLS.items() if c == 'EST']
este = [p for p, (c, _) in CLS.items() if c in ('ESTE', 'ESTE_LEAN')]
print('EST arm n=%d: %s' % (len(est), sorted(est)))
print('ESTE arm n=%d (firm %d): %s' % (len(este), sum(1 for p in este if CLS[p][0]=='ESTE'), sorted(este)))

json.dump({str(p): {'class': c, 'note': n} for p, (c, n) in CLS.items()},
          open(os.path.join(LANE, 'code/crowd10/conditioner59/classification.json'), 'w'), indent=1)
print('wrote classification.json')
for p in sorted(CLS):
    w = wins[p]
    print('@%-5d %-10s pre=%02d suc=%02d %s' % (p, CLS[p][0], w['pre'], w['suc'], w['ctx3']))
    print('          %s' % CLS[p][1])
