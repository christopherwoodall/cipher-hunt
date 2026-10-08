# Battery report: noun-89-1377-adjudicate

- Target id: `noun-89-1377-adjudicate`
- Claim: "adjudicate @1376 ('pour [86-inf] [89-noun/adv], on...') against the infinitive-slot legs"
- Date: 2026-10-08
- Worker: subagent 27596e34-7e12-460e-a5d8-8d4a55d26d5b
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`).
  1,847 pairs / 96 distinct groups re-derived. Never used `canonical.py`.
  R5005 untouched. No invented data.
- Lock: `code/crowd17/next-token/locks/noun-89-1377-adjudicate.lock` created
  2026-10-08T23:09:55Z; no prior/stale lock existed; deleted on completion.

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"either produce a verb-89 parse of @1376 (killing the noun/adverb reading) or
confirm the class conflict and escalate for polyvalence adjudication; feed
@1376 + @221/@985 into queued val-89-mirror; do not duplicate its bar"

Numbered pass/fail clauses (restated, not modified):

1. Produce a grammatical verb-89 parse of @1376, under standing values only,
   that makes the noun/adverb reading of 89 ungrammatical (kills it).
2. Else, confirm the class conflict — the infinitive-slot legs @221/@985
   stand AND @1376 forces a non-verb 89 — and escalate for polyvalence
   adjudication. Battery declares nothing (protocol §7: 67 is the sole true
   polyvalence).
3. Feed @1376 + @221/@985 into val-89-mirror's docket without duplicating
   its bar ("name 89's class (noun vs infinitive) with all three windows
   parsing").

## Method

1. Replicated the repaired parse in Python (offsets + upstream text, same
   tokenization as `repair_parse.py`). Asserted 1,847 pairs.
2. Indexing: @-offsets are 0-indexed pair indices into the 1,847-pair parse,
   citing the FIRST pair of the named frame (matches prior reports).
3. Values used (standing only): banked GT 11=la, 70=pre, 82=m, 34=i, 29=er,
   40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour
   (A9), 84=on (A15, unconditioned per collision-62-84), 47=ce;
   battery-promoted 24=modal (ne-24-profile, 2026-10-08, unratified),
   06='ent' (ent-06), 48='e' (letter), 94='ne' (ne-94), 30='pas' (pas-30);
   provisional 59=est; 86 INF-class (A9 class-level grant, value open);
   67 et/veut positional rule (sole polyvalence, §7). 77 held unfixed
   throughout (not needed by any window below).
4. Re-derived every count below from the stream. Census: 89 n=14 at
   0-indexed [113,222,275,285,303,640,781,871,986,1082,1377,1393,1498,1752];
   00->86 x12, 86->29 x4, 24->89 x3 (@221/@985/@1497), 29->89 x5
   (@112/@274/@780/@1392/@1376), 89->84 x2 (@274/@1376), 89->48 x3.
   All match the frames-80-89-indep re-derivation; no correction needed.

## Window-level evidence

### @1376 — the adjudication window (89 at 1377)

Re-derived context (pairs 1371–1385):
`91 67 98 | 00 86 29 | 89 | 84 92 69 13 | 24 65 68 52`
= "[91] [67] [98] pour [86]er [89] on [92] [69] [13] [24] [65] [68] [52]".

Slot analysis: 00='pour' (A9 grant) + 86 (INF-class, A9 class-level;
00->86 x12, 86->29 x4) + 29='er' (pencil GT) = "pour [infinitive]".
89 sits in the post-infinitive slot, followed by 84='on' (A15 grant,
holds unconditioned per collision-62-84 kill).

Verb-89 candidates, each tested under standing values:

1. **89 = finite verb.** "pour [86]er [89-finite] on" — an infinitive
   followed at once by a finite verb with no subject is ungrammatical.
   FAIL.
2. **89 = infinitive.** "pour [86]er [89] on" — two bare infinitives in a
   row. Ungrammatical UNLESS 86 is a causative/perception verb taking a
   bare-infinitive complement ("pour faire [89-inf]"). 86's value is OPEN
   (stem-86 queued); val-89-mirror (2026-10-08, null) independently tested
   this at the same window and found no causative/perception evidence for
   86 — kill-grade exclusion of infinitive-89 here. Under standing values:
   FAIL. FENCED conditional: activates only if 86 names a causative
   'faire'-shaped value (see follow-up 1). Even then it would coexist with,
   not kill, the noun/adverb reading.
3. **89 = imperative.** An imperative must head its own clause; 89 sits
   inside the pour-phrase between the infinitive and "on [92]…", with no
   clause boundary and no vocative context. FAIL (strained beyond grammar).
4. **89 = participle.** Past participle needs an auxiliary ("pour avoir
   [pp]"); present participle needs "en". Neither is present. FAIL.
5. **89 = finite verb with postposed subject "on".** Declarative French
   does not allow bare "V on" word order (inversion "V-on" is
   question/parenthetical only). FAIL.
6. **89-84 as one word "[89]on".** 84='on' holds unconditioned (A15;
   collision-62-84 kill-grade resolution) — word-internal 84 is excluded.
   As one word "[89]on" would be nominal (-on suffix), still non-verb-89.
   FAIL as a verb parse.
7. **Re-segmentation "00 86" or "86 29".** 00='pour' granted (A9);
   29='er' banked pencil GT; 86->29 x4 is the class-level INF leg. No
   standing rival segmentation. FAIL.

Noun/adverb readings (the rival to kill): "pour [86]er [89-noun], on…"
(direct object of the infinitive: "pour faire le pain, on…") and
"pour [86]er [89-adv], on…" (manner adverb: "pour parler bien, on…")
are both grammatical French under standing values. Neither can be killed:
86's transitivity is unknown (value open), and adverbs are positionally
permissive. Clause 1's kill requirement is not met by any candidate.

### @221 and @985 — the infinitive-slot legs (re-derived, not re-litigated)

- @221 (89 at 222): `29 42 16 24 89 61 96 87 46`
  = "[29] [42] [16] [24-modal] [89-infinitive] [61] par ce que".
  24=modal (ne-24-profile battery-promote, 2026-10-08, unratified) takes
  infinitive complements; 89 sits in the infinitive slot. 77 absent.
  LEG, 77-independent.
- @985 (89 at 986): `45 01 24 89 48 01 76`
  = "[45] [01] [24-modal] [89-infinitive] [48] [01] [76]".
  Same modal+infinitive core; the 48-junction is fenced rightward
  ("e[01]", 01 open) under 48='e' (letter battery) — "[89]e" would unmake
  the infinitive under the modal. LEG with fenced follower, 77-independent.
- (@1497 `15 59 24 89 41…` is the known weak third leg — "59 24"
  junction broken under provisional 59='est'; fenced, not needed here.)

Both legs survive with 77 unfixed and need no 77 assumption. They put 89
in verb-class (infinitive slot); @1376 puts 89 in noun/adverb-class.
Same cell, two classes: the conflict is confirmed on the repaired stream.

### Coordination

- **val-89-mirror** (bar: "name 89's class (noun vs infinitive) with all
  three windows parsing"): already verdict NULL (2026-10-08), report at
  `code/crowd17/report_inbox/processed/battery-val-89-mirror.md`. Its
  docket ALREADY contains the @1376 + @221/@985 inputs (adopted from
  frames-80-89-indep's feed) and independently reached the same
  kill-grade infinitive exclusion at @1375. Feed for clause 3 is therefore
  recorded here as confirmed-delivered, not re-run; its bar is not
  duplicated. Its follow-ups (class-89-adjudicate, tail-89-16,
  laisser-89-impact) are already queued/verdicted — see below.
- **class-89-adjudicate**: already verdict PROMOTE (2026-10-08, packaging
  verdict — window table 11/14 noun-clean + 3 infinitive-slot legs,
  no class named, no polyvalence declared). The red-team escalation this
  battery's clause 2 calls for is therefore already packaged and promoted;
  this battery's confirmation feeds that docket rather than opening a new
  escalation. No standing verdict is contradicted: A8's conditional grant,
  A9, A15, ne-24-profile, and the 67-sole-polyvalence law are all untouched.

## Adverses answered

"class conflict implicates the 67-sole-polyvalence law — battery may only
gather/escalate, not declare": ANSWERED by gathering, not declaring. The
conflict (verb-class @221/@985 vs noun/adverb-class @1376) is confirmed
with window-level derivations above; the escalation artifact already
exists (class-89-adjudicate, promoted 2026-10-08, packaging only — no
class named, no polyvalence declared). This battery declares nothing and
retracts nothing.

## Per-clause pass/fail

1. Verb-89 parse of @1376 killing the noun/adverb reading: **FAIL**.
   Seven candidates tested under standing values; all fail (finite,
   infinitive, imperative, participle, postposed-subject, "[89]on"
   compounding, re-segmentation). The sole verb-shaped parse
   (causative-complement infinitive) is conditional on ungranted
   86='faire'-shaped, was independently found evidenceless by
   val-89-mirror, and would not kill the noun/adverb reading anyway.
2. Confirm the class conflict and escalate: **PASS**. Infinitive-slot
   legs @221/@985 re-derived standing; @1376 forces non-verb 89;
   conflict confirmed. Escalation lands on the already-promoted
   class-89-adjudicate packaging — no new escalation opened, none needed.
3. Feed @1376 + @221/@985 into val-89-mirror without duplicating its bar:
   **PASS**. Feed confirmed already present in its docket (adopted via
   frames-80-89-indep; independently re-derived there); bar not re-run.

## Verdict: NULL

Headline: no verb-89 parse of @1376 kills the noun/adverb reading —
"pour [86]er [89-noun/adv], on…" stands as a hard non-verb window —
while the infinitive-slot verb-class legs @221/@985 stand unrefuted on
the same stream. The class conflict is genuine and confirmed, and under
the §7 67-sole-polyvalence law its resolution belongs to the red team,
whose packaging (class-89-adjudicate) is already promoted. Battery level
cannot declare a second polyvalence and does not.

## Follow-up targets (null regenerates work)

1. **faire-86-causative-test.** Test 86 for causative 'faire'-shape
   (bare-infinitive-complement valency in its contact profile across its
   32 windows). Bar: iff 86 names a causative value taking bare-infinitive
   complements, @1376's fenced conditional verb-89 parse
   ("pour faire [89-inf], on…") activates and the conflict picture changes;
   else fence the conditional permanently. Coordinates with queued
   stem-86 (narrower valency test, not a duplicate of its all-windows bar).
2. **adv-89-1376.** Discriminate noun vs adverb for 89 at @1376 (the
   bar's rival was "noun/adverb", never split). Bar: decide noun-vs-adverb
   iff 89's determiner-contact or adverb-positional profile discriminates
   across its 14 windows; else record the ambiguity as the residual for
   the red-team docket.
3. **tail-1376-on92.** Resolve the "84 92 69 13" tail ('on [92] [69] [13]')
   at @1376 under standing values. Bar: iff the tail parses as a complete
   clause with 84='on' as subject, the clause-boundary reading hardens
   (89 closes the pour-phrase, blocking verb-89); else fence the tail with
   stated cause.
