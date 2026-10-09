# Battery report: mentent-580-rival — test the "ne mentent" (3pl *mentir*) rival segmentation at Frame A

**Target:** `mentent-580-rival` (P3)
**Worker:** 82bda886-d461-4c83-a3c2-718037233919
**Date:** 2026-10-09
**Parent:** battery-frameA-50-value.md NULL 2026-10-09 ("Rival noted" section: the bytes `94 82 06 06`
admit the one-word rival "ne mentent" (3pl present of *mentir*); "Testing it needs a 3pl subject
in `…45 13 55 61`")

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"parse iff a 3pl subject is licensed in \"...45 13 55 61\" under standing values"

Numbered clauses (fixed before data examination):

- **C1:** A 3pl subject is licensed in the "…45 13 55 61" frame (the left context of Frame A)
  under standing values → the "ne mentent" (3pl *mentir*) rival segmentation parses at Frame A.
- **C2:** No 3pl subject is licensed there under standing values → the rival segmentation does
  not parse at battery grade.

Verdict rule: **kill** iff the bar's necessary condition fails at kill grade (the window forces
the 3pl reading false); **null** iff the failure is merely epistemic (fence, with follow-ups).

## Method

Read BATTERY-PROTOCOL.md first; created `locks/mentent-580-rival.lock` on start (deleted on
completion; no prior/stale lock). Re-derived the repaired 1,847-pair / 96-type stream in-session
from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (byte-exact
tokenizer per `code/side-keyhunt/repair_parse.py`; asserts hold: 1,847 pairs, 96 types).
`canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

Standing values adopted as premises (protocol §7 + red-team law, not re-litigated):
pencil 11=la, 82=m, 29=er, 40=e, 46=que; granted/promoted 87=ce, 30=pas, 00=pour, 76=[noun,prom]
(masculine, R19), 43=[noun,cls] (R19-045), 24=R24 (finite/modal — follower is 82/80, not 85),
45=['ce/dict','lead'] (A11 hold), 94=['ne','lead'] (single syllabic "ne" per R19-167, split closed),
78=['ver','lead'] (R16-005, value open); 06='ent' per R17-007 (conditional grant, condition
94="ne" satisfied). Unvalued: 13, 55, 61, 50, 52, 80, 97, 10, 19, 18, 14. Killed: 62='il' (R19,
removed from registry). §3 bars inventing values for unvalued cells.

Grammatical premise: French is non-pro-drop — a 3pl finite verb (*mentent*) requires an overt
3pl subject. (*mentent* is not an imperative form, so no subjectless reading exists.)

## Window-level evidence (0-based pair indices)

"94 82 06 06" census: exactly **x2** stream-wide — @578 (row a3_02, W1) and @1182 (row a6_10,
W2). Byte-exact.

The bar's context string "45 13 55 61" census: exactly **x2** — @574 (W1) and @1165 (W2).
Both Frame A windows share the byte-identical left frame "78 45 13 55 61" immediately before
"94 82 06 06". The bar therefore tests both windows.

**W1** @572–582 (row a3_02): `87 78 45 13 55 61 | 94 82 06 06 | 50`
= "ce(87) ver[78] ce(45) [13] [55] [61] | ne(94) m(82) ent(06) ent(06) | [50]".
Wider left clause @558–577: `94 59 30 67 11 43 24 80 97 13 76 45 94 52`
= "ne(94) est(59,prov) pas(30) et(67, positional: follower 11 not infinitive-shaped)
la(11) [43-noun] [24-finite/modal] [80] [97] [13] [76-noun] ce(45) ne(94) [52]".

**W2** @1164–1186 (rows a6_09/a6_10): `78 45 13 55 61 | 94 82 06 06 | 59`
(same left frame; sibling battery-nementent-W2-subject's wider census adopted as premise:
left "ce [de] [21] [85] [36] [74]" singular ce; "le ver[78]" singular; right "est [42]"
predicative; 84='on' 3sg and non-governing — no 3pl NP anywhere in either clause).

## 3pl-subject audit (both windows)

Every candidate subject position in "…45 13 55 61" and the wider clause, under standing values:

| Candidate | Standing | 3pl? |
|---|---|---|
| 87='ce' (prom) @572 | singular determiner | NO — strictly singular every period |
| 78=['ver','lead'] @573 | value open, ver-family | NO — "ce ver[78]" headed by singular 'ce'; plural "vers" would force determiner-number mismatch ("ce vers"), kill-grade ungrammatical per battery-letter-13-verdicts |
| 45=['ce/dict','lead'] @574 (A11 hold) | singular 'ce' | NO — any NP "ce [X]" is singular regardless of X |
| [13-55-61] @575–577 | unvalued; name-13-55-61 → NULL ("no French word X nameable") | NO — unnameable at battery grade; and embedded under singular 'ce' anyway |
| 76=[noun,prom] masculine @568 | masculine singular noun | NO — and belongs to the earlier 24-clause, not the "mentent" clause |
| 43=[noun,cls] @563 | value open, but under 'la' (pencil, strictly singular) | NO — "la [43]" is singular for any 43 |
| 11='la' @562, 30='pas', 67='et' | determiners/adverb/conjunction | NO — not subject-capable |
| 24=[verb,cls] @564 | finite/modal verb | NO — verb, and already heads "la [43] [24]" |
| 52 @571, 50 @582, 10/19/18/14 | unvalued | NO — §3 bars invention; postposed-subject inversion unlicensed in declarative "ne" clause |
| 84='on' | 3sg pronoun, absent from W1's clause | NO — singular, wrong clause |

**Result: no 3pl subject is licensed in "…45 13 55 61" (narrow frame) or in the wider clause
(broad frame) at either window.** The preverbal subject slot is positively occupied by
singular-licensed determiners (87='ce' promoted, 45='ce' A11 hold); the one open slot
[13-55-61] is unnameable (NULL verdict) and in any case sits under singular 'ce'.

## Per-clause pass/fail

- **C1: FAIL at kill grade.** The bar's necessary condition — a licensed 3pl subject — is not
  met at either Frame A window. The failure is not epistemic: the subject position is
  positively filled by singular determiners, and French grammar (non-pro-drop) makes a
  3pl finite verb without an overt 3pl subject ungrammatical. The window forces the 3pl
  reading false.
- **C2: FIRES.** The "ne mentent" (3pl *mentir*) rival segmentation does not parse at
  battery grade at Frame A.

## Verdict: KILL

The "ne mentent" (3pl of *mentir*, "they do not lie") rival segmentation of "94 82 06 06"
is **forced false at battery grade at both Frame A windows** (@578, @1182): no 3pl subject
is licensed in the "45 13 55 61" frame or the wider clause under standing values, and the
subject slot is positively singular. Per §4, kills regenerate no follow-ups.

## Scope and non-contradiction

- Kills ONLY the rival segmentation/parse (the word-division "ne"+"mentent" as a licensed
  3pl French clause at Frame A). Untouched: 06="ent" (R17-007 conditional value grant stands;
  the condition 94="ne" holds per R19-167), 94="ne" (R19-167/168), 82='m' (pencil),
  50's open value (the parent's standalone-word alternative for 50 is unaffected).
- Consistent with (not duplicating) battery-nementent-W2-subject PROMOTE: that package
  established the systematic subject gap as evidence; this battery draws the parse-level
  consequence its bar required. No standing/red-team verdict contradicted or downgraded;
  §7 intact (67 remains the sole polyvalence).
- Canonical-stream caveat stands (rows a3_02/a6_10 offsets unvalidated).
- Re-open is red-team venue only: a naming act licensing a 3pl subject in the frame
  (e.g., 61/55/13/78 named plural, or the A11 45='ce' hold overturned).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-mentent-580-rival.md` (this file).
- Queue: `mentent-580-rival` → `status: verdict`, `result: kill`, 2026-10-09 (pre-write assert
  passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry
  only; no downgrade).
- Lock created on start (2026-10-09T12:50:39Z), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
