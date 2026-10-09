# Battery verdict: ver78-76-47-78-48-legfamily

- Target: `ver78-76-47-78-48-legfamily` (battery-queue.json, priority 3, status queued)
- Claim: '76-47-78-48' x2 leg family (@364, @1397) as its own positive-leg target
- Worker: d7d6f712-eb1a-477e-a2bc-5d9841e9b891
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types re-derived in-session, asserts held).
  `canonical.py` never used. R5005, sealed gate instances, red-team
  adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/ver78-76-47-78-48-legfamily.lock`
  (created 2026-10-09T20:22:51Z, no stale lock; deleted on completion).

## Bar (verbatim, pre-registered before testing)

"promote the leg family iff '76-47-78-48' x2 parses as an NP frame
('76 ce verre') under 47='ce' + 48='e' with zero contradictions; gated:
fires only after red team ratifies 48='e' (battery n-e-12-48 promotion)"

Adverse (from the queue entry, verbatim): "do not promote 78='ver' globally
(R16-005 LEAD grading stands); ratification is a red-team act, not battery"

## Bar as numbered pass/fail clauses (frozen before testing)

- **C0 (gate):** the red team has ratified 48='e' (letter tier) at
  promote/grant level. The bar fires only then.
- **C1:** the 4-gram '76-47-78-48' occurs exactly 2x stream-wide,
  byte-identical, at the claimed windows.
- **C2:** the 4-gram parses as an NP frame ('76 ce verre') under 47='ce'
  (A4) + 48='e' (letter tier) — i.e. [76] + [ce verre NP], the lane's
  "X licenses a following-NP frame" jargon (cf. det-91-11-frame).
- **C3:** zero contradictions at either window.
- **C4 (adverse):** no global 78='ver' promotion; R16-005 LEAD grading
  stands; leg-family only.

## Method

1. Read BATTERY-PROTOCOL.md first. Created lock on start, deleted on
   completion.
2. Re-derived the repaired stream in-session: 1,847 pairs, 96 types.
   `canonical.py` never used.
3. Census of the '76-47-78-48' 4-gram and the '47-78-48' trigram
   stream-wide; byte-confirmed both windows with full row contexts.
4. Gate check against the R20 red-team round report (48='e' standing).
5. Contradiction scan: left/right neighbors of both windows against the
   "[76] + [ce verre]" frame; 45-presence scan of both rows.
6. Standing values used (adopted, not re-litigated): 47='ce' (A4 allophone
   tier, granted); 48='e' (letter tier); 76=noun masculine (R19-111 GRANT
   PROMOTE); 78='ver' (R16-005 LEAD, value under test — NOT promoted here);
   40='e' / 11='la' / 29='er' / 70='pre' / 17='fois' banked pencil GT;
   86 INF-class, 89 noun-lead, 92 verb-cls, 77='le' provisional.

## Window-level evidence (0-based pair indices)

### W1 — 0-based @362–365 (claim's "@364" = the 78 position), row a2_06

`92 98 92 47 11 21 62 48 | 76 47 78 48 | 49 61 70 17 06 21`

- @362=76 (noun, masc), @363=47 ('ce'), @364=78 ('ver' under test),
  @365=48 ('e' letter).
- "47 78 48" = "ce" + "ver" + "e" = "ce verre" — demonstrative + noun
  "verre" (glass): a grammatical French NP. Adopted from R20-035 GRANT
  (ver78-non45-positive-leg), not re-litigated.
- Left neighbor of the frame: @361=48 ('e' letter), @360=62 (open).
  Nothing forces 76 into a role incompatible with a following NP
  (clause-boundary and apposition readings live; neither contradicted).
- Right neighbor: @366=49 (open) — no contradiction.
- Row a2_06 (25 pairs) contains NO 45 token: the 78<->45 mutual
  conditionality is broken from the 78 side at this window.

### W2 — 0-based @1395–1398 (claim's "@1397" = the 78 position), row a7_07

`16 06 29 67 86 29 89 16 | 76 47 78 48 | 40 67 77 81 87 11`

- @1395=76, @1396=47, @1397=78, @1398=48 — byte-identical to W1.
- Same "ce verre" NP parse under the identical standing set.
- Left: @1394=16 (open), @1393=89 (noun-lead) — no contradiction.
- Right: @1399=40 ('e' letter), @1400=67 — the 'e' is a separate token;
  no composition with "verre" is licensed or needed; no contradiction
  with the NP.
- Row a7_07 (28 pairs) contains NO 45 token.

### Census

- '76-47-78-48' 4-gram: exactly **2x** stream-wide (@362, @1395).
- '47-78-48' trigram: exactly **2x** (@363, @1396) — both inside the
  4-grams; no free-standing '47 78 48' elsewhere.

## Per-clause pass/fail

- **C0 (gate): PASS / FIRES.** R20-008: n-e-12-48 — DUPLICATE
  (R17-002 + R17-003 GRANT PROMOTE, letter tier): 12="n", 48="e" letter
  tier. The red team has ratified 48='e' at grant level; the bar's gate
  condition is satisfied.
- **C1: PASS.** Exactly 2x, byte-identical, at the claimed windows
  (0-based 78 positions @364/@1397).
- **C2: PASS.** Under 47='ce' + 48='e', "47 78 48" = "ce verre" is a
  grammatical French NP (R20-035 GRANT, adopted); 76 = masculine noun
  (R19-111 GRANT PROMOTE) sits as the frame's left element with zero
  forced incompatibility — the 4-gram parses as [76] + [ce verre NP].
- **C3: PASS.** Zero contradictions: no neighbor at either window forces
  76, 47, 78, or 48 into a value/role against the frame; no 45 in
  either window or row.
- **C4 (adverse): answered by compliance.** This report promotes ONLY
  the leg family. 78='ver' is NOT promoted globally; R16-005 LEAD
  grading stands unchanged; no registry change.

## Verdict: PROMOTE (leg family only)

All bar clauses pass and the adverse is answered. The '76-47-78-48' x2
leg family is promoted as a positive-leg family for 78='ver' at
battery grade, with the 48='e' dependency now satisfied at red-team
level (R20-008). Ratification of what the legs imply for 78 is a
red-team act.

## Scope

- Promotes only the leg family. No value named globally, no class
  granted, no registry change, no §7 declaration.
- Untouched: R16-005 (78='ver' LEAD), R19-111 (76=noun), R20-035 (legs),
  R20-008 (48='e'), the ver78 re-arm (trigger unfired), §7.
- Canonical-stream caveat stands (row a2_06/a7_07 offsets unvalidated).
- No follow-ups (promote, not null).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ver78-76-47-78-48-legfamily.md`
- Queue: `ver78-76-47-78-48-legfamily` queued -> `verdict`/`promote`,
  2026-10-09 (pre-write assert passed — was queued/verdictless;
  target-id-unique tmp
  `battery-queue.json.ver78-76-47-78-48-legfamily.tmp` + atomic rename;
  disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/ver78-76-47-78-48-legfamily.lock`: created on start,
  deleted on completion (verified gone). R5005, sealed gates, red-team
  adjudication queue untouched.
