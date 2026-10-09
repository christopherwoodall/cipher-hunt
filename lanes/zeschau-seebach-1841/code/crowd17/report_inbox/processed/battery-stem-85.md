# Battery verdict: stem-85

- Target: `stem-85` (battery-queue.json, priority 3, status queued)
- Claim: 85 verb-stem value
- Worker: c7110be1-b93c-4cf6-b164-ccf88ea9d44b. Date: 2026-10-08.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; assert 1,847 pairs, 96 groups). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- All @-offsets are pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/stem-85.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"promote iff value named with >=2 independent verb-stem frames"

Numbered clauses (frozen before testing):
1. A specific French verb-stem VALUE for 85 is named (a value, not a class).
2. At least 2 independent verb-stem frames (distinct positions, non-overlapping windows) parse cleanly with 85 carrying that named value.
3. Every listed adverse is answered (re-parsed cleanly, fenced with stated cause, or shown to be a misread — not ignored).

Standing values used: pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional 59=est; battery-lead 94='ne' (ratification pending, used as lead only); §7 sole polyvalence (67 et/veut). NOT assumed: any value for 85, 24 beyond 'en' (A3 GT), 01, 58, 33 (dire/croire tied).

## Method

Re-parsed the repaired stream from bytes. Re-derived all 15 windows of 85 with ±4 context, the full 85 predecessor/successor census, and every 46-29 and 46-85 bigram in the stream. Re-tested each of the A3 frame legs individually against 1841 diplomatic French with only granted values.

## Window-level evidence

### Clause 1+2: the frame legs, re-derived

85 census (n=15), ±3 context (matches contredire-85-33-vehicle's independent census):

| @ | row | pre → 85 → suc |
|---|-----|---------------|
| 54 | a1_01 | 37 11 79 **85** 58 35 53 |
| 95–97 | a1_02 | 97 46 29 **85** 08 21 62 |
| 375 | a2_06 | 65 63 29 **85** 82 48 00 |
| 595 | a4_00 | 00 92 79 **85** 01 29 40 |
| 733 | a5_02 | 48 88 11 24 **85** 93 76 18 |
| 746 | a5_02 | 67 77 81 **85** 28 00 64 |
| 956 | a6_00 | 96 87 46 24 **85** 04 20 67 |
| 1047 | a6_04 | 11 67 76 **85** 41 88 29 |
| 1173 | a6_10 | 87 83 21 **85** 36 74 32 |
| 1234 | a7_01 | 47 33 29 **85** 56 10 03 |
| 1278 | a7_03 | 76 48 56 **85** 48 53 61 |
| 1439 | a7_08 | 52 82 16 24 **85** 01 52 68 |
| 1694 | a8_06 | 60 27 46 24 **85** 58 15 23 |
| 1699 | a8_06 | 15 23 91 **85** 33 94 30 |
| 1755 | a8_08 | 28 89 26 24 **85** 58 17 78 |

Predecessor census: 24 ×5, 29 ×3, 79 ×2, 81/76/21/56/91 ×1. Successor census: 58 ×3, 01 ×2, 10 others ×1.

**FINDING 1 — "que [85]er"×2 does not re-derive; it is ×1.** The A3 evidence claims '"en [85]"×5 + "que [85]er"×2' (7 frame-legs). The "que [85]er" legs trace to Q2 (crowd15 `next-token-findings-que-ce.md`): "29='er' (verb ending) immediately after 'que', two different stems (85, 42)". On the repaired stream there are exactly two 46-29 bigrams in the whole cipher: @95–97 `46-29-85` (a1_02) and @217 `46-29-42` (a2_01). The second leg belongs to **42, not 85**. There is no 46-85 bigram anywhere in the stream. The A3 leg count for 85 corrects **7 → 6**. (The a5_03 repair cannot explain this: a1_02/a2_01 precede a5_03, so their pair sequences are identical in both parses.)

**FINDING 2 — the "que [85]er" frame is order-inconsistent as a clean infinitive parse.** Byte order is 46-29-85 = "que er [85]". The cipher's own stem+er spelling puts the ending LAST (33-29, A9's 86-29 ×4, A10's 33+29 composition). A "que + [85-stem] + er" infinitive reading would need 85 before 29; no 85-29 bigram exists. The leg survives only as a verb-stem PROFILE leg (85 sits immediately post-"er" inside a que-clause, a verb-selecting environment) — fenced with stated cause, not a clean infinitive frame.

**FINDING 3 — of the five "en [85]" legs, 3 are clean gerunds; @733 admits a forced rival parse.**
- @956 (a6_00): `96-87-46-24-85` = "par-ce-qu'en [85]" — the A3-confirmed frame itself. Clean. ✓
- @1694 (a8_06): `46-24-85-58` = "qu'en [85] [58]" — clean elision. ✓
- @1755 (a8_08): `26-24-85-58` = "[26-noun] en [85] [58]" — gerund adjunct. Clean. ✓
- @733 (a5_02): `88-11-24-85-93` = "[88] la en [85] [93]". 11='la' (pencil) + 24='en' (A3 GT) forces the surface elision **"l'en"** — a grammatical pronoun cluster ("la"+"en", cf. "il l'en informa"). Two parses use only granted values: (a) gerund adjunct — "[88-verb] la, en [85-ing] [93]"; (b) pronoun cluster + FINITE 85 — "[88] l'en [85-finite] [93]". Both grammatical in 1841 French. Parse (b) makes 85 finite, not a stem — a class-level rival inside the frame evidence itself. Genuinely ambiguous; fenced.
- @1439 (a7_08): `82-16-24-85-01-52` = "m' [16] en [85] [01] [52]" (82='m' pencil). Murky: the gerund reading needs "m'[16]" to close before the adjunct (16 open), and no clean pronoun-cluster rival exists (16 intervenes). Not adjudicated here; flagged for the re-audit follow-up.

Net: the A3 frame grant's SPIRIT (85 = verb-stem candidate) survives on 3 clean gerund legs + 1 profile leg, but the headline "7 frame-legs" is overstated at 6, with 2 of the 5 gerund legs carrying stated ambiguity.

**FINDING 4 — no value is nameable from bytes.** Every frame above is value-open: 85's distinctive neighbors (58 ×3, 01 ×2, 93/04/08/82/28/41/36/56/48/33/36) are all unvalued except 82='m' and 48='e'. No French verb stem is determined by any ≥1 frame, let alone 2 independent ones. The 'laisser' lead is gated on 33's tied value (dire/croire); the 'contre' lead is a hapax bigram conditional on two open values (contredire-85-33-vehicle, 2026-10-08). Clause 1 FAILS, so clause 2 fails by consequence. This is a data limit, not a testing failure: the bar demands a NAMED value and the stream does not supply one.

### Clause 3: adverses

**Adverse 1 — "85→01→29 ('er') once — verbal signal vs nominal frames" (@595–598: `79-85-01-29-40`).** Shown to be a MISREAD as a forced verbal signal. The "verbal" reading needs 85-01 to be a verb stem taking -er (ungranted; 85-01 occurs ×2 and its wordhood is open). The window admits a fully nominal parse conditional only on 01='ci' (A12-unit-adjacent; cf. dict-45-w3-ceci's "verdict-ci", tested 2026-10-08): "pour [92] tout [85]-ci [29-40]" = "pour [92] tout [85]-ci …" — demonstrative-postfix "X-ci", exactly parallel to the granted 37-01 unit shape. Under that parse the window is CONSISTENT with the nominal frames, not against them. Neither parse is forced (01='ci' ungranted); the "verbal signal" is not established. Fenced with stated cause.

**Adverse 2 — "79→85 ×2 forces adjective/noun IF 79='tout'" (@54, @595).** CONFIRMED as a standing, granted-frame consequence, not a hypothesis: 79='tout' is PROMOTED (A5). "tout [85]" ×2 therefore forces a nominal (adjective/noun) function F2 for 85 — in direct tension with the verb-stem frames F1 under the §7 sole-polyvalence law (67 et/veut only). This tension was already recorded by x-33-laisser-test (null, 2026-10-08) and contredire-85-33-vehicle's F2; I re-confirm it stands on the repaired stream. It independently blocks any clean verb-stem-value promote: naming a verb value for 85 without red-team polyvalence adjudication would contradict a PROMOTED value's frame. Escalation venue: red team (already in flight; no new escalation opened by this battery).

## Per-clause results

1. Value named: **FAIL** — no French verb-stem value is determined by any frame; all distinctive neighbors are value-open (Finding 4).
2. ≥2 independent verb-stem frames with the named value: **FAIL** — consequence of (1). (Frame evidence itself also corrects 7→6 legs per Finding 1, with 2 of 5 gerund legs ambiguous per Finding 3.)
3. Adverses answered: **PASS** — Adverse 1 shown to be a misread (nominal "tout [85]-ci" parse available; verbal reading unforced); Adverse 2 confirmed as a standing granted-frame tension, re-recorded for the red team rather than decided.

## Verdict: NULL

The bar is not met (no value nameable), and no kill-grade evidence was found (no window forces 85 non-verbal; the frame grant's core — 3 clean gerund legs — stands). The headline correction for the supervisor and red team: **the A3 leg count "7 frame-legs" does not re-derive on the repaired stream — it is 6** ("en [85]"×5 + "que [85]er"×1; the second "que" leg is a 42 window, @217 `46-29-42`), and 2 of the 5 gerund legs carry stated ambiguity (@733 "l'en"+finite rival; @1439 murky). This refines the A3 evidence; it does not overturn the red-team CONFIRM of 85 as a verb-stem candidate (frame-level), which rests on the 3 clean legs.

## Follow-up targets (null regenerates work)

1. **en85-gerund-reaudit** (priority 2): battery-level re-audit of the five 24-85 gerund legs individually. Bars: (a) adjudicate @733's "l'en"+finite-85 rival parse vs the gerund parse with banked values only; (b) adjudicate @1439's "m'[16] en [85]" shape; (c) confirm or correct the A3 "en [85]"×5 count on record. Verdict promote iff ≥4 of 5 legs confirm as gerund frames; null with corrected count otherwise.
2. **ant-58-ending** (priority 3): 58 follows 85 ×3 (@54/@1694/@1755) — test 58='ant' (present-participle ending), which would close the gerund frames as "en [85]-ant" and is the most direct path to naming 85's stem. Full 58-census required. Bars: promote 58='ant' iff ≥3 windows parse as participle endings with independent frames; kill iff any window forces 58 non-verbal.
3. **unit-85-01** (priority 3): 85-01 ×2 (@595/@1439) — test two-group word/unit. Bars: promote unit iff ONE French word-formation reading (e.g. "[stem]-ci" demonstrative postfix, parallel to the A12 37-01 unit) covers both windows with stated boundary evidence; kill iff the two windows force different segmentations. (Resolves Adverse 1's frame either way.)

Note for the supervisor: croire-33-compound85, stem-85-then-1700, and laisser-gate-85 remain correctly GATED on stem-85 naming a value — this null does not unblock them. The red-team polyvalence question for 85 (F1 verb-stem vs F2 nominal under 79='tout' PROMOTED) is already in flight via x-33-laisser-test; not re-escalated.
