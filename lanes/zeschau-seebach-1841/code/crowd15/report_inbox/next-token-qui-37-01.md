# Battery A12 — "qui 37-01" ×2 (@938, @1632)

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder P8 (next-token-findings-qui.md).
Windows: @938 `21-64-37-01-07` and @1632 `21-64-37-01-74`
(64@938/@1632 "qui"; 37@939/@1633; 01@940/@1634).
Shared pre: 21-64 ("[21] qui") ×2.

## Pre-registered bar (written BEFORE touching data)

- **Bigram-unit test:** is 37-01 a recurring unit? 37-01 count globally;
  if ≥3, it's a word/collocation candidate independent of "qui".
- **Link to A1:** A1 promoted 37's predicative frame ("est 37" ×6). Here
  37 is FIRST after "qui" (different slot — the finder said don't merge).
  Test whether "qui 37-01" constrains 37's value: does any "qui 37-01"
  window contradict the predicative frame, or refine it (e.g. 37 as a
  verb here vs adjective in A1 — the "cern" interlock from A1)?
- **PROMOTE** a 37-01 unit reading iff: the bigram recurs ≥3× AND ≥2
  windows parse it as one word/collocation with no contradiction.
- **HOLD** if it's exactly 2× (the anchor pair) with no third leg.
- Do not merge this slot with A1's "est 37" slot (different position).

## Data

### 37-01 bigram (re-derived): 3×

| pos | window |
|---|---|
| @939 | 33-21-64-**37-01**-07-50 ("[21] qui [37-01] [07]") |
| @1633 | 33-21-64-**37-01**-74-87 ("[21] qui [37-01] [74]") |
| @1817 | 42-06-29-**37-01**-02-09 ("er [37-01] [02]") |

The "21-64-37-01" 4-gram recurs byte-identical ×2 (@937–940, @1631–1634).
Third leg @1817 lacks "qui" (pre=29 "er") — the bigram travels.

### A1-link audit

A1 promoted 37's predicative frame ("est 37" ×6) and flagged the "cer/cern"
syllable interlock ("certain" × adj-frame, "concerne(nt)" × verb-frame @179).
Here 37 sits FIRST after "qui" (different slot — no merge per the finder).
"qui [37-01]": if 37="cer", 37-01 = "cer-[01]" — "certain" is cer-tain!
"qui certain [07/74]"? = "[X] qui [est] certain"? — missing "est", but
"qui certain" as "[noun] certain" (adjective postposed: "un fait certain")?
Hmm: "[21] qui certain" doesn't parse as noun+adj either ("qui" intrudes).
Value-level: unknown. The "cer" hypothesis is COMPATIBLE (37-01="cer-tain"
is phonotactically clean) but this window doesn't prove it — the "qui"
slot is new.

## Verdict: PROMOTE (unit, not value)

**37-01 is a recurring collocation/word-unit (3×, twice in the identical
"21-qui-37-01" 4-gram).** Bar met (≥3× + twice identical frame, no
contradiction). Value NOT promoted. A1-link: the unit is compatible with
A1's "cer/cern" syllable lead (37-01 = "cer-[01]", "certain"-shaped) —
recorded as supporting L1 of A1, not independent proof. The "qui"-slot
vs "est"-slot distinction holds: no merge of the two 37 frames.
