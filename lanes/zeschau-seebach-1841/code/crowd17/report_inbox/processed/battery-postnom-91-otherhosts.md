# Battery report — postnom-91-otherhosts

Date: 2026-10-09
Target: `postnom-91-otherhosts` (P3)
Verdict: **NULL** (fence executed — no attributive-91 geometry at any of the five DET-proximate windows)
Parent: `battery-detframe-43-hunt.md` (NULL, follow-up #2)

## Bar (verbatim from battery-queue.json)

"test @15/@723/@1005/@1428/@1518 for licensed attributive-91 geometry with named hosts; fence if no host licenses it there either"

Restated as numbered clauses:
- C1: test @15/@723/@1005/@1428/@1518 for licensed attributive-91 geometry with named hosts (byte evidence at battery grade).
- C2: fence if no host licenses it there either, with stated cause.

## Method

Re-derived the repaired stream in-session (1,847 pairs / 96 types, all asserts held;
`canonical.py` never used). All five offsets are 0-based pair indices; 91 confirmed
at each (n(91)=21 stream-wide, byte-exact). Determiner tier from standing values only:
11='la' (GT), 47='ce' (promoted), 77='le' (provisional), 87='ce' (promoted demonstrative),
45='ce' (A11 hold). Named noun-class hosts with standing status:
76 (masculine noun, R19-promoted), 43 (noun, R19-045 class tier),
58 (nominal class), 81 (masculine-abstract-noun class grant).

## Findings — the five windows (±3, 0-based)

| @ | context | DET geometry | host status |
|---|---------|--------------|-------------|
| 15 | `98 76 45 [91] 53 17` (a1_00) | 45='ce' directly before 91 ("ce [91]") | none — 91 itself occupies the noun slot |
| 723 | `80 77 03 [91] 65 64` (a5_02) | 77='le' two back; 03 intervenes ("le [03] [91]") | 03 is verb-stem (R19 "er" infinitive class), not a noun host |
| 1005 | `86 56 47 [91] 11 52` (a6_02) | 47='ce' directly before 91 ("ce [91]") | none — 91 itself occupies the noun slot |
| 1428 | `29 87 63 [91] 61 12` (a7_08) | 87='ce' two back; 63 intervenes ("ce [63] [91]") | 63's value open (finite-shaped, unvalued), not a named host |
| 1518 | `11 31 11 [91] 67 08` (a7_11) | 11='la' directly before 91 ("la [91]") | none — 91 itself occupies the noun slot |

Completeness check: scanned all 21 91-windows for any determiner within 3 positions
left — only these five qualify (@15, @723, @1005, @1428, @1518). The parent's
five-window list is byte-exact complete.

Distributional facts:
- **No "DET [named-noun] 91" geometry exists at any of the five windows.** At
  @15/@1005/@1518 the determiner is immediately adjacent to 91 ("ce 91" ×2,
  "la 91" ×1) — 91 sits in the noun slot, not postnominal-adjective position.
- **No standing noun-class cell (76/43/58/81) directly precedes 91** at any of
  the five windows.
- The only cell between any DET and 91 is 03 (verb-stem, barred as host),
  63 (unvalued, barred as host by §3 — naming it would invent a value), or 31/11
  (unvalued), which cannot license a host under standing values.

## Per-clause results

- **C1 PASS:** all five windows tested for licensed attributive-91 geometry with
  named hosts, using standing values only.
- **C2 FIRES:** fence executed — no host licenses attributive-91 at any of the
  five windows, with cause stated above. Fence, not kill: this is not a global
  falsification of "91 is an adjective" (91 could still be an adjective at
  windows without DET proximity); it only fences the DET-proximate attributive
  frame across these five windows.

## Adverses

"the only '43 91' window sits in the predicative-37 frame" — answered. The five
windows are a disjoint population: none involves 43 (re-confirmed "43 91" as a
stream hapax at @386/387 with pre=38 37 43, the predicative frame, in the
21-window scan). Nothing here bears on @386's predicative frame; the fence is
window-scoped to the five DET-proximate windows. No standing/red-team verdict
contradicted or downgraded; §7 intact; canonical-stream caveat stands.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `noun-91-det-frames` (P3) — test 91 as a NOUN in the three direct "DET 91"
   windows (@15 "ce 91", @1005 "ce 91", @1518 "la 91"); name nominal-91 iff
   ≥2 windows parse with zero kill-grade contradictions, else fence.
2. `inf-03-91-complement` (P3) — test 91 as the complement/object of the
   infinitive-shaped 03 at @723 ("le [03] [91]"); needs 03's verb-stem value
   plus 91's class; else fence the verb-complement arm there.
3. `ce63-91-host-gate` (P4) — re-test @1428's "ce [63] [91]" geometry once 63's
   value is named; gated on the 63 naming act.
