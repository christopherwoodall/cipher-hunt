# Battery `laisser-85-15window` — verdict: NULL

## Bar (verbatim, pre-registered)
"kill iff any window forces 85 non--er-stem; promote iff all 15 parse with zero kill-grade contradictions"

Numbered clauses (derived before testing, not modified after):
- C1: KILL iff any of the 15 windows forces 85 to be non--er-stem at kill grade.
- C2: PROMOTE iff all 15 windows parse as 85='laisser' with zero kill-grade contradictions.
- C3: else NULL with 1–3 follow-ups per §4.

Adverses: none listed. Adopted premises: 85 = verb-stem frame grant only (A3, value open);
'29 85' never composes as a word (battery-er85-word-census PROMOTE); 29='er' banked;
79='tout' granted (A5); 48='e' promoted letter; 08='t' battery-grade (unratified, used
only where noted — no finding depends on it).

## Method
Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(same parse as `repair_parse.py`; asserts held: 1,847 pairs, 96 types).
`canonical.py` never used. n(85)=15, loci byte-confirmed:
@54, @97, @375, @595, @733, @746, @956, @1047, @1173, @1234, @1278, @1439,
@1694, @1699, @1755. Scored 'laisser' (causative/permissive -er verb:
"laisser + inf", "laisser + noun", finite "laisse" + object) at each window
using standing values only.

## Findings

| @ | window (±2, standing values) | 'laisser' parse |
|---|---|---|
| 54 | tout [85] [58-nominal] | PARSE — "tout laisser [N]" |
| 97 | [97]er laisser [08] | FAIL — "[97]er" infinitive + "laisser" adjacent; '29 85' does not compose (census), 29 attaches left |
| 375 | [63]er laisser m'e | FAIL — same "[X]er laisser" adjacency |
| 595 | tout [85] [01] | PARSE — "tout laisser [01]"; "01 29" = "[01]er" would give causative "tout laisser [inf]" |
| 733 | [24-verb] laisser [93-verb] | PARSE (cond: 93 infinitive-shaped) — "[V] laisser [inf]" |
| 746 | [81] laisser [28] | PARSE (cond: 28 inf/noun; both open) |
| 956 | [24-verb] laisser [04] | PARSE (cond) |
| 1047 | [76-noun] laisser [41] | PARSE — finite "laisse": "[N] laisse [41-inf]" |
| 1173 | [21-noun] laisser [36-noun] | PARSE — finite "laisse" + noun object: "[N] laisse [N]" |
| 1234 | ce [33]er laisser [56] | FAIL — same "[X]er laisser" adjacency |
| 1278 | [56] laisser e(48) | UNCERTAIN — "85 48" is a stream hapax; no licensed letter-composition frame (the 40='e' model does not transfer to 48); "laisser e" does not parse as two words |
| 1439 | [24-verb] laisser [01] | PARSE (cond) |
| 1694 | [24-verb] laisser [58-nominal] | PARSE — "laisser [N]" |
| 1699 | [91] laisser [33-INF] | PARSE — "85 33" bigram (hapax): causative "laisser [inf]"; strongest leg |
| 1755 | [24-verb] laisser [58-nominal] | PARSE — "laisser [N]" |

- **C1 (kill) FAIL.** No window forces 85 non--er-stem. The three "[X]er laisser"
  failures are 'laisser'-specific adjacency contradictions, not tier-forcing:
  85 could still be a different -er stem at @97/@375/@1234. The @1278
  uncertainty likewise does not force a non-verb tier.
- **C2 (promote) FAIL.** 11/15 parse (several conditional on open neighbors),
  3 fail (@97/@375/@1234, shared "[X]er laisser" shape), 1 uncertain (@1278).
  Not all 15 parse.
- The three failures share one shape: an 'er'-final infinitive immediately
  left of 85 ("[97]er", "[63]er", "[33]er"). 'Laisser' cannot follow a bare
  infinitive in French. This is a 'laisser'-killing pattern at those windows,
  not an 85-killing pattern.

## Scope
'Laisser' is not killed as 85's value (11 windows parse, strongest @1699
"laisser [33-INF]"), and not promoted (3 windows reject it). 85 stays
verb-stem frame, value open (A3). No standing/red-team verdict contradicted,
downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands
(a1_02/a2_06/a7_01 offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)
1. `er85-adjacency-reseg` (P3) — the "[X]er laisser" ×3 (@97/@375/@1234):
   re-segmentation audit or rival -er-stem test; if 'laisser' is excluded
   here but viable at the other 11, package as conditioned-split/red-team input.
2. `unit-85-48-1278` (P4) — test "85 48" = "laisse" composition at @1278
   under a licensed letter-composition frame; name-or-fence.
3. `rival-85-stems` (P4) — score the surviving rival -er stems
   (contredire et al., per battery-contredire-85-33-vehicle) against the
   11 parsing windows; narrow the candidate set or fence.

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-laisser-85-15window.md`
- Queue: `laisser-85-15window` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique temp
  file `battery-queue.json.laisser-85-15window.tmp` + atomic rename;
  disk re-validated; own entry only; no downgrade).
- Lock `locks/laisser-85-15window.lock`: created 2026-10-09T19:19:00Z
  (agent ea787683), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
