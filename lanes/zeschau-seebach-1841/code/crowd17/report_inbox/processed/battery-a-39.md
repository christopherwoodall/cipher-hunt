# Battery report: a-39 — 39="a/a"

- Worker session: d1f77c5d-d2d7-439e-ae5a-45de38007150
- Date: 2026-10-08 (UTC 05:51 start)
- Lock: created `code/crowd17/next-token/locks/a-39.lock` on start, deleted on completion.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`).
  `canonical.py` never used. R5005 never touched.

## Bar (verbatim from battery-queue.json)

"promote iff >=2 frames parse cleanly as 'a'/'a' + zero contradictions"

Numbered clauses:

1. At least 2 windows containing 39 parse cleanly with 39 as 'a'/'a'.
2. Zero contradictions: no window forces 39 to a value other than /a/.

## Method

Loaded the repaired stream (1,847 pairs, 96 distinct groups, verified count).
Enumerated all 13 occurrences of 39 (pair indices below are stream positions;
"@N" = pair index N). For each, printed a ±4 window with standing glosses
(banked pencil: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
promoted/granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on,
47=ce; provisional: 59=est, 77=le). Tested each window for a clean French
parse with 39 as the word "a"/"a", as the preposition "a", or as word-internal
letter 'a'. Checked every window for a forced non-/a/ reading.
Frequency-calibrated 39 against the other single-letter pairs.

## Window-level evidence (all 13 occurrences of 39)

| # | pair idx | row | window (39 = [39]) | reading |
|---|----------|-----|--------------------|---------|
| 1 | 37 | a1_01 | 91 [39] 64=qui 41 | "a qui" — CLEAN as "a" (follower 64=qui promoted; "a qui" ungrammatical) |
| 2 | 503 | a3_00 | 56 [39] 68 21 | neutral ("56 a 68", governor unknown) |
| 3 | 600 | a4_00 | 03 [39] 26 96=par | neutral (03 unknown) |
| 4 | 607 | a4_00 | 64=qui [39] 64=qui 02 | "qui ? qui" — FENCED (see adverse A1) |
| 5 | 692 | a5_00 | 03 [39] 74 46=que | neutral (03 unknown) |
| 6 | 764 | a5_03 | 59=est* [39] 88 (locus 761-764: 62 94 59 39) | "est a" — CLEAN as "a" ("est a" ungrammatical); LOAD-BEARING on provisional 59=est |
| 7 | 1068 | a6_04 | 70=pre [39] 11=la 44 | "pre-a-la": consistent with word-internal 'a' in "prealable" (completion unverified); supporting, not a clean word-parse |
| 8 | 1333 | a7_05 | 52 [39] 83 86 | neutral ("52 a 83") |
| 9 | 1491 | a7_10 | 92 [39] 24 00=pour | neutral ("92 a 24") |
| 10 | 1512 | a7_11 | 59=est* [39] 81 88 | "est a" — CLEAN as "a"; LOAD-BEARING on provisional 59=est |
| 11 | 1605 | a8_02 | 70=pre [39] 11=la 92 | "pre-a-la": same as #7 (word-internal 'a' candidate) |
| 12 | 1676 | a8_05 | 03 [39] 74 77=le* | neutral (same 03-39-74 trigram as #5) |
| 13 | 1726 | a8_07 | 98 [39] 88 24 | neutral ("98 a 88") |

Frame-family check against the queued evidence: 64-39 occurs once
(@606, = window #4, "qui ? qui" — does NOT parse as "qui a"; the evidence
label overstates it); 59-39 x2 confirmed (@763, @1511); 03-39 x3 confirmed
(@599, @691, @1675); 70-39-11 x2 confirmed (@1067, @1604); "62 n'est 39"
@762 = pair locus 761-764, load-bearing on provisional 94="ne" AND 59=est —
supports only conditionally, not an independent leg.

Frequency calibration: n(39)=13 sits inside the single-letter-pair band
(40="e" n=21, 82="m" n=39, 34="i" n=11, 70="pre" n=15) — consistent with 39
being the single letter /a/, occurring standalone and word-internally.

## Per-clause results

- Clause 1 (>=2 frames parse cleanly as 'a'/'a'): PASS. Three clean frames:
  #1 "a qui" @37 (fully clean; follower 64=qui promoted), #6 "est a" @764
  and #10 "est a" @1512 (clean modulo provisional 59=est, flagged as
  load-bearing per task instruction). The "pre-a-la" frames (#7, #11) are
  supporting (word-internal 'a') but not counted as clean word-parses.
- Clause 2 (zero contradictions): PASS. 12 of 13 windows are consistent
  with 39=/a/; none forces a non-/a/ value. The one resistant window (#4,
  @607 "qui ? qui") is fenced as adverse A1, not ignored.

## Adverses

- Queue adverses: none listed.
- Discovered adverse A1 (@607, "64=qui 39 64=qui"): neither "qui a qui"
  nor "qui a qui" is French. FENCED with stated cause: word-boundary
  placement at this locus is underdetermined, and 39 has a demonstrated
  word-internal occurrence class (70-39-11 "pre-a-la", consistent with
  "prealable"; frequency band matches the single-letter pairs), so 39 here
  may be word-internal and the locus cannot be forced into a three-word
  "qui a/a qui" parse. Secondary possibility: clause boundary
  ("...qui. A qui..."). Does not force the claim false.

## 'a' vs 'a' per-window test (task requirement)

- Determinate word-parses are ALL "a" (#1, #6, #10). Zero windows parse
  39 as the verb "a" ("has").
- #7/#11 parse as word-internal letter 'a' (neither word).
- Remaining windows are underdetermined between "a"/"a"/word-internal.
- The distinction is NOT cipher-testable: /a/ is one phoneme; the pair
  encodes the sound/letter and "a" vs "a" is resolved by French grammar at
  decode time. Per the lane's allophone-tier doctrine (cf. 47="ce", A4),
  this is ONE value, not polyvalence — promoting 39="a/a" does NOT
  conflict with the standing rule "67 et/veut is the sole true polyvalence".
- No collision with any banked/promoted/granted value.

## Verdict

**promote** — 39="/a/", realized as "a"/"a"/word-internal 'a' (allophone tier).
Both bar clauses pass; the sole discovered adverse is fenced with stated
cause; no standing red-team verdict on 39 is contradicted (none exists;
a/a is allophonic, not a second polyvalence). Caveats fenced into the
verdict: two of three clean frames are load-bearing on provisional 59=est
(lane precedent: promotion with provisional-leaning legs, cf. 77="le" WO2);
the finder's "qui a" 64-39 frame label is corrected to the fenced @607
window; "62 n'est 39" support is conditional on provisional 94="ne"+59=est.

No follow-ups required (verdict is promote, not null). Suggested next
battery if the red team wants it: a rival-value battery for 39 (e.g. 39="o"
or 39 as pure vowel-slot) is not indicated by any window — no window
prefers a rival.
