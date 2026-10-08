# PREREG — Battery 81="prin" (crowd14/prin81)

**Date:** 2026-10-07 | **Battery:** PRIN-81 | **Lane:** zeschau-seebach-1841

## Objective
Adjudicate the F108 systematic-drag docket item "le prince"×2 (@1240/@1401,
mapping 77-81-87 → "le"-"prin"-"ce") against:
1. the "la pour" post-context adverse (post-context groups read 11="la" (GT) + 00="pour" (strong lead));
2. the F107 "cela"×2 segmentation ambiguity (87-11-87-11 "ce la ce la" vs 77-81-87 "le prin ce");
3. the F-C@1088 anchor frame ("00 33 79 80 06" @467/@1088; 81 flanks F-C@1088 at @1086/@1095).

## Bar (pre-registered, frozen before run)
81="prin" promotion to LEAD-grade requires **≥2 independent legs**:
- **Leg A (positional):** both windows @1240 and @1401 are byte-exact
  77-81-87 in the repaired 1,847-pair stream (stream built from
  `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
  never canonical.py), and 77="le" (lead) and 87="ce" (provisional) are
  unbroken in pre-context.
- **Leg B (corpus grammaticality):** the full window frame
  [pre-context] + 77-81-87 + [post-context] maps to a construction
  attested in the era corpus `code/side-period/corpus/` (clean pool;
  v8 phrase-zeros VOID per WO3) at era-rate ≥ 2 independent sources,
  OR a single era-source attestation PLUS one independent structural leg.
- **Leg C (structural):** either (i) 81="prin" strengthens the F-C@1088
  anchor frame, or (ii) adjudication of "cela"×2 comes down decisively
  against the "ce la ce la" reading at both windows.

## Adverse bar (pre-registered)
The "la pour" post-context adverse is RESOLVED only if:
- post-context groups at both windows are extracted byte-exact, and
- "la pour" (11="la" GT + 00="pour" strong lead) is grammatical in that
  post-context per 1840s diplomatic French, with corpus attestation
  (pre-registered: ≥2 independent era attestations of the exact
  [X "la pour"] construction, or ≥1 plus structural explanation), OR
- the post-context groups do NOT parse as 11-00 (adverse evaporates), OR
- it conflicts: then REPORT as conflict — **do not regrade 11="la" (GT)
  or 00="pour" (strong lead) unilaterally.** The adverse is then
  escalated, not adjudicated by this battery.

## "cela" ambiguity adjudication rule
"le prince" (77-81-87) vs "cela"×2 (87-11-87-11 "ce la ce la") can coexist
only if both segmentations are anchored on their own evidence; if the
byte-exact stream cannot support one reading, it is dead at that window.
A reading that survives at both windows but lacks a second leg stays LEAD-weak.

## Verdict options
- **PROMOTE-to-LEAD:** ≥2 independent legs AND adverse resolved cleanly AND
  ambiguity adjudicated.
- **HOLD:** one leg only, or adverse unresolved but no conflict.
- **KILL:** conflict with 11="la"/00="pour" that cannot be reported upward
  cleanly, or byte-exact re-derivation FAILS (window not 77-81-87), or
  corpus test returns era-0 with no structural leg.

## Status constraints
- Do NOT disturb 11="la" (GT) or 00="pour" (strong lead) without
  red-team-grade evidence; conflicts get REPORTED, not regraded.
- No re-litigation of: 48="ne" kill, H_verb kill, 86=que-family refutation,
  unconditioned 84s, three mergers, refuge concretizations, retired WO-6 bar.
- 68 unvalidated offsets: conditional-canonical caveat recorded; if any
  window falls in the unvalidated offset region, flag explicitly.
