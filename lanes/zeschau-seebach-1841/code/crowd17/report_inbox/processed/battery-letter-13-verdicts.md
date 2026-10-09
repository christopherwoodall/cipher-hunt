# Battery verdict: letter-13-verdicts

Target: `letter-13-verdicts`. Claim: test 13 as word-final letter at the two
"78-45-13" windows (@576/@1167, 1-based positions of 13) under the
45='dict'-iff-78-medial lead.
Date: 2026-10-09. Worker: c0e78df6-ea45-4334-8081-ca46aba535d2 (battery worker).
Lock `locks/letter-13-verdicts.lock` created 2026-10-09T12:39:38Z (no stale lock;
locks dir held only NOTE.md plus other workers' live locks); deleted on completion.

## Bar (verbatim, pre-registered from battery-queue.json)

"Kill test is the determiner-number mismatch ("ce verdicts"); else the
sub-lexical 13 reading survives."

Restated as numbered clauses (frozen before testing):
- **C1 (kill arm):** the "ce verdicts" determiner-number mismatch is demonstrated
  at a window under the sub-lexical word-final-13 hypothesis -> the sub-lexical
  13 reading is KILLED.
- **C2 (survival arm):** if C1 does not fire, the sub-lexical 13 reading survives
  (licensed, not killed).

No adverses listed on the queue target.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair / 96-type
stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py`
(stride-2 pairing per row offset). Asserts held: 1,847 pairs, 96 types.
`canonical.py` never used. R5005, sealed gates, red-team adjudication queue
untouched. Offset convention: @n = 0-based pair index; 1-based equivalents given.

Standing values used (protocol §7 + post-R19): banked GT 11=la, 82=m, 29=er,
40=e, 46=que; granted 87=ce, 64=qui, 96=par, 47="ce" (A4 allophone tier);
leads: 78="ver" (ver-78 LEAD, red-team R16-005 venue), 45="ce/dict" (A11 HOLD +
R16-004 lead); 78-45 one-word boundary = "verdict" PROMOTED
(verdict-w2-574-gate); 67 et/veut sole true polyvalence (R24 declared R19-191
for 24, not touched here).

## Window-level evidence (byte-verified in-session)

The 5-gram "78 45 13 55 61" occurs exactly 2x stream-wide (0-based @573, @1164).

**Window A** — 0-based @573-577 (1-based @574-578), row a3_02:
`@569:45 @570:94 @571:52 | @572:87 | @573:78 @574:45 @575:13 @576:55 @577:61 | @578:94 @579:82 @580:06 @581:06`
-> "[52] ce(87) verdict(78-45) [13] [55-61] ne(94) m'(82) ..."

**Window B** — 0-based @1164-1168 (1-based @1165-1169), row a6_09:
`@1160:44 @1161:83 @1162:21 @1163:67 | @1164:78 @1165:45 @1166:13 @1167:55 @1168:61 | @1169:94 @1170:87 @1171:83`
-> "[21] et/veut(67) verdict(78-45) [13] [55-61] ne(94) ce(87) ..."

n(13)=12, confirmed (matches battery-value-13-third-arm census).

## The sub-lexical hypothesis, pinned down

Under the 45='dict'-iff-78-medial lead, 78-45 = "ver"+"dict" = "verdict"
(complete word; boundary promoted). For 13 to be a WORD-FINAL letter, the word
must be "verdict"+[13]. French lexicon check: "verdict" is noun-only; the sole
French word of shape "verdict"+letter is "verdicts" (plural). No verb
"verdictir", no other derivation. Therefore the sub-lexical word-final
hypothesis is exactly: **13 = "s", completing plural "verdicts"**.

## Per-clause pass/fail

**C1: FIRES (kill).** At Window A, the hypothesis forces "ce(87) verdicts":
- 87='ce' is granted and is forced determiner of the NP: "ce" as COD pronoun is
  impossible French ("ce" is never a direct-object pronoun); "ce" as subject
  pronoun requires "etre" ("c'est/ce sont"), absent here; "ce" cannot be a
  dislocated tonic topic (tonic form is "ca"/"cela"). The cells 87-78-45-13 are
  contiguous with 78-45 one word, so "ce [verdicts]" is one NP.
- "ce" (demonstrative adjective) is masculine singular in every period of
  French; plural is "ces". "verdicts" is plural. The number mismatch is
  ungrammatical, with no period/register rescue.
- No alternative letter: only "s" completes a French word after "verdict".
- 78-45="verdict" is promoted; not re-litigated at battery grade (and the
  target's claim explicitly operates under the dict lead).

Window B ("21 67 verdicts") does not force the mismatch (67='et' takes a bare
plural conjunct; 67='veut' takes a bare plural object), but the hypothesis under
test is the uniform word-final reading across the two byte-identical windows,
and Window A falsifies it. The kill test fires.

**C2: moot** (antecedent false — C1 fired).

## Verdict: KILL

The sub-lexical word-final-13 reading (13 = plural "s" of "verdicts") is killed
at kill grade by the forced "ce verdicts" determiner-number mismatch at Window A
(@573-577, row a3_02). All four rescue routes fail (87 forced determiner; "s"
sole letter candidate; "verdict" boundary promoted; "ce" strictly singular).

## Scope of the kill (narrow)

Killed: 13 as a word-FINAL letter (the "s" of "verdicts") at the two 78-45-13
windows. NOT killed and still live:
1. 13 as word-internal letter/syllable (e.g. inside a longer 13-55-61... word;
   the 13-55-61 one-word unit was left unresolved by dict-frame-78-45-13-55-61
   NULL).
2. 13 as word-initial letter.
3. §7 split (13 with different values at different windows) — battery cannot
   declare polyvalence; already escalated to the red team by
   battery-value-13-third-arm.

No standing/red-team verdict contradicted or downgraded (87=ce, 78="ver" lead,
45="ce/dict" lead, 78-45 "verdict" promote, A11 HOLD on its remaining 21 windows,
R19-191 R24 all adopted as premises). §7 intact. Canonical-stream caveat stands
(rows a3_02/a6_09 offsets unvalidated). Per §4, kills regenerate no follow-ups.

## Bookkeeping

- Queue: `letter-13-verdicts` -> `status: verdict`, `result: kill`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON
  re-validated post-write; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone). R5005, sealed
  gates, red-team adjudication queue untouched.
