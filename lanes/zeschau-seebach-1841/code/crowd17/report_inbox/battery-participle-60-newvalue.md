# Battery report: participle-60-newvalue

Worker: battery subagent (session 20006ee2-5e88-49f6-aa59-ce2406d15dc6).
Date: 2026-10-09.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`), parsed per
`code/side-keyhunt/repair_parse.py` (re-implemented inline; n=1847 asserted,
96 groups asserted). `canonical.py` never used. R5005, sealed gate instances,
and the red-team adjudication queue untouched. @i = 0-based pair index.
Lock: `code/crowd17/next-token/locks/participle-60-newvalue.lock` created at
start with agent id + UTC timestamp, deleted on completion.
No standing verdict overwritten or downgraded.

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"name the value iff it parses @454 ('77 60 [noun]') and survives all 17 other
60 windows with zero hard contradictions"

Numbered clauses (fixed before data examination):

1. (C1) The proposed past-participle value parses @454 ("77 60 [noun]")
   with <=1 unstated assumption.
2. (C2) The value survives all 17 other 60 windows with zero hard
   contradictions.
3. (C3) Adverses answered: @690 hostile; @1338 forces finite 60.

## Method

Fresh parse of the repaired stream (n(60)=18 confirmed; windows
[119, 172, 197, 232, 322, 454, 637, 690, 700, 995, 1338, 1366, 1474, 1563,
1644, 1674, 1690, 1735]). Read the parent evidence (ledit-60-corrob NULL)
and the dit-60-syncretic kill first; nothing re-litigated. Since the parent
established 60="dit" as the only participial value parsing @454 and it is
kill-grade dead, I enumerated the remaining French past-participle space for
a value fitting "le [PP] [65-noun]" at @454, then tested the single honest
survivor against all 17 other windows.

## Findings

### C1 — candidate found: 60 = "nommé"

@454 (row a2_10, byte-verified): `79 17 77 60 65 13` = "tout fois le [60]
[65-N]". With 60="nommé": "…tout fois, le nommé [65]…" — the legal/
administrative 1841 formula "le nommé X". Attested in the lane's period
corpus: "le nomme Landry", "le nomme conseiller", "le nomme ministre"
(`code/side-period/corpus/`, 4 hits for "le nomm[ée] ").

Assumption count: the value itself is the only new assumption. 77="le" is
provisional (standing); 65 is R18-ratified noun-class (value unnamed, but
the slot "65=N" parses). **C1 PASS.**

(Discarded candidates with cause: "dénommé/prénommé/surnommé/susnommé/
susdit" — same frame family, longer and less likely as a single cipher
group than "nommé"; monosyllabic PPs "lu/vu/su/eu/fait/mis/pris" — "le
lu/vu/su X" are not licensed NP shapes in 1841 French ("le dit X" was the
fixed legal formula, now dead). "nommé" is the strongest honest candidate;
all share the same C2 fate.)

### C2 — kill-grade failure

A uniform 60="nommé" (past participle) must parse every 60 window as a
participle. Three independent windows force it false:

- **Leg A — @197 (battery-promoted verb slot).** `47 01 21 60 08 67 76`
  = "ce [01] [21-N] [60] [08] et [76-N]" (row a2_00). slot-60-at-197
  (2026-10-09, battery PROMOTE) resolved this as a finite-verb slot:
  "[21-N] [60-V] [08]". A bare past participle "nommé" with no auxiliary
  is ungrammatical here — kill-grade contradiction.
- **Leg B — @1338 (adverse confirmed).** `86 71 64 60 08 65 64` =
  "[86] [71] qui [60] [08] [65] qui". 64="qui" is a standing grant; "qui"
  requires a finite verb — "qui nommé" is ungrammatical. The adverse's
  "forces finite 60" holds; "nommé" dies here at kill grade.
- **Leg C — @1644.** `12 33 98 60 03` = "[12] [33] vient [60]". The
  boundary-98-839 PROMOTE hardens 98="vient" as clause-terminal with an
  infinitive-selecting complement inventory; "vient nommé" (finite-form PP
  after a complement-selecting finite verb, no auxiliary) is
  ungrammatical.

Under §7 (67 et/veut is the sole true polyvalence), a battery cannot hold
60 as verb at @197 and participle at @454 — that is a conditioned split,
red-team venue only. The uniform past-participle value is forced false.

**C2 FAIL at kill grade.**

### C3 — adverses answered

- @690 hostile: `65 94 29 60 03` = "[65-N] ne [29]er [60] [03]". Banked
  pencil GT 29="er" directly abuts 60; "er nommé" admits no grammatical
  parse (this is the same hostile environment that killed 60="dit" in
  dit-60-syncretic). Confirmed, folded into the C2 kill.
- @1338 forces finite 60: confirmed (Leg B above). Folded into the C2
  kill.

No adverse ignored.

## Verdict: KILL

The claim "propose one new past-participle value for 60" is killed at kill
grade: the best honest candidate (60="nommé", the only new PP parsing @454
within the assumption budget) dies at three independent windows (@197
battery-promoted verb slot, @1338 "qui"-forced finite, @1644
"vient"-governed). The past-participle avenue for 60 is closed at battery
grade — joining "dit" (dit-60-syncretic), present-participle (@1338, per
participle-60 V1 via the parent), and finite "-dre" stem (@700, per
participle-60 V2 via the parent).

Scope: kills only the PP avenue. verb-60's battery PROMOTE is consistent
with this verdict (not downgraded, not contradicted). The red-team
poly-60-redteam docket remains the venue for any conditioned verb/PP split
(§7). No standing or red-team verdict contradicted or downgraded; §7
intact. Canonical-stream caveat stands (68 of 70 upstream row offsets
unvalidated).

No follow-ups mandated (kill, not null; per protocol §4 only nulls must
regenerate). Supervisor note: the 60 PP question is now fully closed at
battery level; remaining 60 work is verb-side (verb-60's six windows) and
the red-team poly-60 docket.
