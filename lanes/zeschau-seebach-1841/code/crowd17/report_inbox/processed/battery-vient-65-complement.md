# Battery report: vient-65-complement (98+[noun-class] complement test)

Date: 2026-10-09. Stream: repaired 1,847-pair parse
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per
code/side-keyhunt/repair_parse.py). canonical.py never used. R5005, sealed gates,
red-team queue untouched. All counts re-derived in-work; no prior counts trusted.
Lock: code/crowd17/next-token/locks/vient-65-complement.lock (created
2026-10-09T02:47:17Z, deleted on completion).
Sibling coordination: vient-98-511-relative (null, 2026-10-08) is the parent
report; ce-le-verb-frame (queued) owns the @515-517 tail. No duplication.

## Bar (verbatim, pre-registered)

"state whether any 98+[noun-class] window admits a grammatical 'venir'
complement (time / locative / purpose with stated frame evidence), or fence
98-65 as a complement-class residual. Decides whether @511's strain touches
98 at all"

Numbered clauses (stated BEFORE testing, unchanged after data):

1. Arm 1: at least one window where 98 is followed by a noun-class group
   admits a grammatical complement of "venir" (time, locative, or purpose),
   with the frame evidence stated.
2. Arm 2 (fallback): if no such window exists, fence 98-65 as a
   complement-class residual and state whether the strain touches 98.

## Method

Fresh byte-exact re-parse of the repaired stream. Full census of 98 (n=40)
followers; cross-checked each follower against class standing (registry +
battery verdicts). Tested every 98+[noun-class] window against the valency
of "venir" in 1841 French: intransitive; licensed complements are
"de" + place/infinitive (recent past), "à" + infinitive, locative/time
adverbs, "pour" + infinitive/noun (purpose). A bare noun is never a licensed
complement of "venir" in any period of French.

## Window-level evidence (@-offsets, repaired stream)

98 follower census (n=40): 83 x5, 82 x3, 80 x3, 98 x3, 00 x3, 56 x2, 20 x2,
then singletons: 76, 51, 19, 81, 41, 92, 65, 53, 96, 48, 12, 78, 86, 55, 15,
62, 24, 60, 39.

Followers with noun-class standing: exactly two.
- 76: masculine noun, PROMOTED (battery noun-76: 'le [76]' x3 determiner+noun
  legs). 98-76 occurs x1 stream-wide, @12 (row a3_00? no — row a1_00):
  @6-18 = "06 77 78 18 93 62 [98] 76 45 91 53 17 64".
- 65: noun-class, battery-PROMOTED (prof-65, six frame legs; value open).
  98-65 occurs x1 stream-wide, @511 (row a3_00):
  @505-517 = "21 67 77 62 94 64 [98] 65 88 56 87 77 80".

All other followers lack noun-class standing: 83 ('de', conditioned), 00
('pour', promoted), 82/12/40/48 (letter/stem values), 86 (INF class),
80 (verb-frame), 78 (word-final 'ver' lead), 96 ('par', ground truth),
20 (split candidate), 60 (verbal polyvalence question), 24 (verb class),
39 ('a/à' lead), 62 (conditioned; 'il' killed as independent word), and
56/41/53/55/15/51/19/81/92 (class open, no noun standing).

98's grammatical complement slots are all filled by NON-noun followers:
- "vient de": 98-83 x5 (origin / recent past).
- "vient pour": 98-00 x3 (purpose).
- "vient" + INF: 98-86 x1 (@1146, 'vient [86=INF]').
No time or locative adverb follower has standing anywhere in the census.

### Per-window tests (Arm 1)

@511 "qui vient [65]":
- Bare-NP complement: ungrammatical. "Venir" licenses no direct noun object.
- Inverted subject ("vient [65-subject]"): impossible — 64='qui' (ground
  truth tier) is already the subject of "vient".
- Time/locative: 65's 25-window profile (relative-head x3, object-relative
  head x1, post-finite-verb direct object x2, post-"-ere" slot x3, post-verb
  x1) contains no temporal or locative frame. Ungranted to posit one.
- Purpose: would need "pour" between 98 and 65; absent.
- Elided preposition ("vient d'[65]", "vient à [65]"): no stream evidence
  for an elision rule; ungranted.
FAIL — no grammatical complement reading.

@12 "…93 62 vient [76]":
- Bare-NP complement: ungrammatical (same valency fact).
- Inverted subject: French inversion requires the determiner ("vient le
  ministre", never "*vient ministre"); 76 is bare here. Additionally 62's
  role at @11 is conditioned/word-medial ('il' killed globally as an
  independent word), so the clause's subject slot is unresolved — but even
  granting a subject gap, the missing determiner kills inversion.
- Time/locative: 76's frames are ordinary count-noun ('le [76]' x3); no
  temporal/adverbial leg anywhere in its n=21 profile.
- Purpose: no "pour" present.
FAIL — no grammatical complement reading.

## Per-clause pass/fail

1. Arm 1 (grammatical venir complement at a 98+[noun-class] window) — FAIL.
   Both noun-class windows (@12, @511) reject every licensed complement
   frame (bare-NP ungrammatical; inversion blocked by missing determiner /
   occupied subject; no time/locative/purpose frame evidence for 76 or 65).
2. Arm 2 (fence 98-65 as complement-class residual) — PASS. 98-65 is a
   stream singleton (x1/1847); 98-76 likewise x1. The contacts are
   distributionally inert. The strain at @511 localizes to the open-value
   complements (65/88/56/87/77/80), not to 98: 98='vient' rests on the
   'vient de' (x5) / 'vient pour' (x3) / 'vient + INF' (x1) frames at other
   windows and is untouched. @511's strain does NOT touch 98.

## Adverse answered

- "'98 65' is a singleton; the contact is distributionally inert" —
  CONFIRMED and absorbed: re-derived 98-65 x1 and 98-76 x1 stream-wide. The
  fence below is local-fit only.
- Prior report's "no 98+[noun] window besides @511" is CORRECTED: @12
  (98-76, masculine noun promoted) is a second 98+[noun-class] window; it
  was tested above and fails the same way. The correction strengthens the
  fence (two independent inert contacts, same outcome).

## Verdict

**NULL** — Arm 1 fails; Arm 2 (fence) succeeds. 98-65 is FENCED as a
complement-class residual: "vient [65]" admits no grammatical complement
reading under current values, and the residual belongs to 65's distribution
(and the @512-517 open-value cluster), not to 98. 98='vient' untouched; no
standing verdict contradicted or downgraded; nothing promoted or killed.

## Null follow-ups (per §4 — work regenerates, never ends)

1. `temp-65-loc-census` (P3): full 25-window census of 65 for any
   temporal/locative/adverbial frame. Bar: >=1 frame leg with a
   time/locative reading under stated period evidence, or 98-65 is fenced
   terminally (this battery's fence becomes permanent and 65's noun-class
   stands unconditioned).
2. `inv-98-76-12` (P3): adjudicate @12's "93 62 98 76". Bar: state 62's role
   at @11 (word-medial unit with 93 vs independent, with byte evidence) and
   give "vient [76]" any grammatical parse (inversion with stated
   determiner facts, or other); else fence 98-76 as the second
   complement-class residual alongside 98-65.

## Provenance

R5005, sealed gate instances, red-team adjudication queue untouched. No
invented data. Lock created on start, deleted on completion.
