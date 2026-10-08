# Battery report: stem-44-nominal — "44 as nominal STEM vs whole word"

- Worker: battery worker stem-44-nominal, agent ac20a3d1-1b84-4545-bf5f-cdf7d983d587
- Date: 2026-10-08 (lock created 2026-10-08T23:15:00Z, no stale lock found)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). canonical.py NOT used. R5005 untouched. Red-team adjudication queue untouched.
- Regeneration #2 of the noun-44 kill (2026-10-08), which STANDS and is NOT re-litigated here. The noun-44 kill targeted the VALUE claim "44 is a noun"; this battery tests the SEGMENTATION claim (stem-level vs whole-word). Whole-word status is not a noun value (cf. @1714's clitic forcing).

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff 44's stem-vs-whole status is decided across the stem windows ('44ere' @540, 'm[44]' @1160) and the whole-word frames with <=10% orphan; else fence the split for red team"

Numbered clauses (frozen before testing):
1. The stem windows are adjudicated: @540 ('12 44 29', "44ere"-shaped) and @1160 ('82 44', "m[44]"-shaped) — each classified as forced stem-level composition vs admittable whole-word parse.
2. The whole-word frames are adjudicated: 'le 44' x2 (@208, @1679), 'la 44' @1070, 'ce 44 est 37' @527, '44 pour' x3 (@1311, @1583, @1679), subject-44 (@249, @527), plus all remaining windows (@797, @800, @1603, @1618, @1714, @1839).
3. Resolution test: ONE status (all-stem or all-whole) covers all 15 windows with <=10% orphan (<=1 window). If met, the stem-vs-whole status is decided.
4. Fence branch: if clause 3 fails, fence the split for the red team with stated cause — which windows need stem-level, which need whole-word, the A10 (33/86) stem/whole HOLD precedent cited, and the polyvalence/second-value declaration reserved to the red team per protocol §7 (67 is the sole true polyvalence).

## Method

Enumerated all 15 windows of 44 on the repaired stream (n(44)=15 re-derived; indices [208, 249, 527, 540, 797, 800, 1070, 1160, 1311, 1583, 1603, 1618, 1679, 1714, 1839] — byte-identical to the noun-44 battery's re-parse). Key bigram counts re-derived from the stream, not copied: '77 44' x2 (@207, @1678), '44 00' x3 (@1311, @1583, @1679), '11 44' x1 (@1069), '42 44' x2 (@1617, @1838), '82 44' x1 (@1159), '12 44' x2 (@539, @1582), '47 44' x1 (@526), '94 44' x1 (@1713), '44 29' x1 (@540), '00 44' x1 (@1602), '37 44' x1 (@796), '86 44' x1 (@799), '44 83' x2 (@1160, @1839).

Standing values used (protocol §7): pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); battery-promoted/queue-standing (94=ne, 12=n + 48=e, 30=pas, 06=ent); provisional (59=est, 77=le). Per §7, declaring a second polyvalence is a red-team act; one cipher number carries one phonological form at battery level.

## Window-level evidence (stem-level vs whole-word)

**Forced stem-level (word-internal composition): 2 windows.**

- @540 ('91 12 44 29 48 42', a3_01): "91 n [44]er e 42". With 12='n' (battery), 29='er' (banked GT), 48='e' (battery), the only grammatical parse is word-internal '44'+'ere' ("[X]ère"/"[X]ere"-shaped feminine stem, as fenced in noun-44 clause 4). A whole-word 44 here would strand "ere" as a standalone word — "ere" is not a French word ('erre' needs a double r; only one 29 present). No whole-word parse is nameable. FORCED STEM-LEVEL.
- @1160 ('77 82 44 83 21', a6_09): "77 m [44] de [21]". Two candidate parses: (a) word-internal "m[44]" (82='m' letter, pencil GT); (b) clitic "m' [44]" (elision before vowel-initial 44). Parse (b) is EXCLUDED: @1070 gives unelided 'la 44' with 11='la' banked as the article — French elision is mandatory before vowels ('l'amie', never 'la amie'), so 44 is consonant-initial; 'le 44' x2 (@208, @1679) unelided confirms. Under §7's sole-polyvalence rule (67), 44 carries one phonological form across windows, so the "m'" elision at @1160 is inadmissible. FORCED STEM-LEVEL ("m[44]" one word).

**Whole-word-needing: 13 windows.**

- @208 ('06 77 44 50'): "le [44] [50]" — article frame (77='le' provisional).
- @249 ('91 32 44 94 65'): "[32] [44] ne [65]" — subject-44 slot (value killed as noun, but segmentation whole-word; 44 precedes 'ne' as a standalone token).
- @527 ('47 44 59 37 64'): "ce [44] est [37] qui" — demonstrative frame (47='ce' granted A4; word-internal "ce44" would overturn a granted value — unavailable at battery level).
- @797 ('37 44 77'): "[37] [44] le" — whole-word (no nameable word-internal parse).
- @800 ('86 44 74'): "[86] [44] [74]" — whole-word (no nameable word-internal parse).
- @1070 ('70 39 11 44 74'): "pre [a/à] la [44] [74]" — article frame (11='la' banked).
- @1311 ('92 44 00 36'): "[92] [44] pour [36]" — '44 pour' complement frame.
- @1583 ('53 12 44 00 36'): "n [44] pour [36]" — '44 pour' complement frame (left edge fenced in noun-44, non-discriminating for the bigram).
- @1603 ('00 44 70'): "pour [44] pre" — 'pour' + whole-word 44.
- @1618 ('42 44 11 84'): "[42] [44] la on" — 44 whole-word (right-edge 'la on' fenced as an anomaly independent of 44 per noun-44; 44's own segmentation unaffected).
- @1679 ('74 77 44 00 46'): "74 le [44] pour que" — article + 'pour que' complement frame.
- @1714 ('65 94 44 59 30'): "ne [44] est pas" — whole-word in the clitic slot (noun-44 kill; segmentation is ROBUST to the pending 94='ne' / 59='est' ratifications — "[94] [44] [59]" is a whole-word token whatever the values).
- @1839 ('42 44 83 21'): "[42] [44] de [21]" — whole-word frame. The 5-gram's 44-status question belongs to queued stem-44-1839 (bar: red-team decision target); NOT duplicated here — this battery records only the window-level segmentation.

## Per-clause verdicts

1. Stem windows adjudicated: PASS. @540 forced stem-level ('44ere' word-internal; "ere" not a word). @1160 forced stem-level ("m[44]" word-internal; "m'" elision excluded by unelided 'la 44' @1070 under §7 sole-polyvalence).
2. Whole-word frames adjudicated: PASS. 13 windows need whole-word segmentation; none admits a nameable word-internal parse without overturning banked/granted values.
3. Resolution test: FAIL. Whole-only orphans 2/15 = 13.3% > 10% bar (@540, @1160 forced stem). Stem-only orphans 13/15 = 86.7% — and is unavailable anyway (would overturn granted 47='ce' at @527 and banked 11='la' at @1070). Neither status covers the stream within the bar's orphan budget.
4. Fence branch: EXECUTED. The split is genuine and is fenced for the red team below.

## Verdict: NULL

The stem-vs-whole status of 44 is undecided at battery level: 2 windows force stem-level composition, 13 force whole-word segmentation, and neither uniform status meets the <=10% orphan bar. This is the A10 (33/86) stem/whole HOLD precedent in parallel — a standing split, not a forced answer. Per §7, declaring a second polyvalence for 44 (stem-level nominal item vs whole-word item) or ruling the stem windows re-parseable is a red-team act; this battery does not declare it.

No standing verdict is contradicted or downgraded: the noun-44 KILL (value claim) stands untouched — whole-word segmentation is not a noun value, and @1714's clitic forcing is preserved. The A10 HOLD is coordinated (parallel split), not re-litigated. stem-44-1839's @1839 5-gram question is not duplicated.

## Follow-ups (null regenerates work; the supervisor queues these)

1. **phon-44-elision**: systematic elision census for 44 — re-derive the consonant-initial evidence ('la 44' @1070 unelided, 'le 44' x2 unelided, zero elided 'l'44' forms stream-wide) and test whether ANY 44 window admits a vowel-initial reading. Gates the @1160 "m'"-clitic alternative and hardens the stem-forcing there; if a vowel-initial window is found, the §7 one-form assumption breaks and the split re-opens.
2. **stem-44-value**: name a French nominal stem value for 44 that yields real words in BOTH stem windows — '44ere' ("[X]ère"/"[X]ere"-shaped, @540) and 'm[44]' (@1160). If one value fits both, the split becomes a value-level question (is the whole-word 44 the same word?); if no value fits both, the split hardens toward polyvalence and feeds the red-team docket.
3. **poly-44-docket** (red-team decision): the standing split — 2/15 windows stem-level (@540, @1160) vs 13/15 whole-word; whole-only orphans 13.3% > 10% bar. Red team to decide: (a) declare a second polyvalence for 44 (stem-level nominal item vs whole-word item); (b) rule the stem windows re-parseable under one value; or (c) rule the n-e-12-48 analytic/syllabic-duality precedent applicable (one item, two segmentation levels). Battery cannot declare per §7.

## Provenance

Every number above traces to the repaired 1,847-pair stream (re-parse verified in-work: n(44)=15; all 14 bigram counts re-derived from the stream). No invented data. canonical.py not used. R5005, sealed gates, and the red-team adjudication queue untouched. Adverses answered (A10 precedent coordinated; stem-44-1839 not duplicated).
