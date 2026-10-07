# BEDROCK — independent re-derivation of the Seebach lane's standing facts

Date: 2026-10-07. Fleet: two independent verifiers (separate code, no shared logic,
no lane code imported) + red-team adjudicator (third independent derivation).
Primary sources only: `data/upstream-ct_R5005.digits.txt`,
`data/upstream-offsets.json`, `code/side-keyhunt/repaired_offsets.json`,
`data/upstream-NOTES.md` (convention only). Lane files read for claimed values only.

## Verdict: FOUNDATION SOLID, six corrections required (none verdict-flipping)

---

## 1. Transcription & canonical parse — ALL PASS

| Fact | Claimed | Re-derived | Verdict |
|---|---|---|---|
| Digit rows | 70 | 70 | PASS |
| Digit count | 3,764 | 3,764 | PASS |
| Repaired pairs | 1,847 | 1,847 | PASS |
| Distinct groups | 96 | 96 (codes 00–99; absent: 5, 25, 72, 75) | PASS |
| Digit accounting | — | 3,694 paired + 70 dropped (31 by offset + 39 by odd length) | PASS |
| Repair locality | a5_03 flip only | exactly a5_03: 1→0; all other rows byte-identical | PASS |
| Raw crib `117082342940` | twice (raw 1532, 2108) | [1532, 2108] | PASS |
| `11 70 82 34 29 40` positions | pairs 754 + 1034 | [754, 1034], all 12 positions hold claimed groups | PASS |
| Old-parse off-phase read | `71 17 08 23 42 94 02` | confirmed at old 753–759 | PASS |
| a8_05 terminal | ends 46 | 46 at pair 1692 | PASS |
| Stream identity | — | byte-identical to lane's post-repair artifact (all 35 `positions_62` match) | PASS |

Offset convention C1 (per-row independent pairing, skip first `o` digits, drop
trailing leftover) is forced by arithmetic ((3764−2×1847)=70 dropped); the
carry-over alternative gives 1,866 pairs ≠ 1,847.

**Repair premise — epistemic ruling:** VALID given the gloss-over-a5_03 premise
(crib occurs twice raw; the gloss lands exactly on the repaired occurrence).
The premise itself is UNVERIFIABLE from available sources (no manuscript images).
Standing wording should be "conditionally canonical" (REINDEX.md already records
this; elevate to STATE.md standing facts).

## 2. Group frequencies — 6 STALE (confirmed by all three derivations)

| Group | Claimed | Re-derived | Status |
|---|---|---|---|
| n64 | 46 | **47** | STALE — equals old-parse value |
| n00 | 54 | **55** | STALE |
| n11 | 44 | **45** | STALE |
| n82 | 38 | **39** | STALE |
| n34 | 10 | **11** | STALE |
| n29 | 47 | **45** | STALE |
| n62 | 35 | 35 | PASS (updated post-repair) |
| n06 | 44 | 44 | PASS (updated post-repair) |
| n24 | 52 | 52 | PASS |
| n52 | 27 | 27 | PASS |
| n78 | 31 | 31 | PASS |
| n87 | 32 | 32 | PASS |
| n96 | 21 | 21 | PASS |

n77=44, n47=28, n67=38, n43=16, n84=25, n59=27 computed; no explicit unigram
claims exist in NOTES.md for these (N/A — not errors).
The lane updated n62 (34→35) and n06 (46→44) after the F32 repair but missed
these six. All six deltas are confined to row a5_03.

**Blast radius — 13 downstream cites traced, ZERO verdict flips:**
- H3 legs: rank(64) 4→3, predecessors 28→29, P(87|64) 0.109→0.106 — all legs still hold (recomputed from repaired stream).
- Closer battery L4 exclusion *strengthens* at n=47.
- 182×/60× era gaps → ~175×/~62× — still kill-grade.
- "29=er at rank 2" → rank 4 — still top-syllable.
- Small number fixes: "00 leads at 55", rank(64)=3, 11/39=28.2%, 7/45, 2.44%/64×.
- Phase-A rank claims were wrong even under the old parse (no convention pinned) — repaired competition ranks: 11→4, 70→51, 82→9, 34→69, 29→4, 40→34, 46→19.
- Two artifacts are old-parse JSONs needing re-run: `closer64_87_results.json`, `crowd3/morphologist_results.json` (both via old-parse `crib_attack.load_pairs` loader).

## 3. Windows / bigrams / trigrams — ALL PASS

| Claim | Re-derived | Verdict |
|---|---|---|
| 62→94 ×9 | exact 9 positions | PASS |
| 24→87→64 ×3 @[179,1766,1774] | confirmed | PASS |
| `64 96 43 87 01` ×2 @[341,1025] | confirmed | PASS |
| 06→29 ×4 | confirmed | PASS |
| 00→86 ×12 vs 00→06 ×0 | confirmed | PASS |
| 77→86 ×5 @[430,798,877,950,1133] | confirmed (new-indexing; old-parse: [430,797,876,949,1132]) | PASS |
| 77→78 ×7 | confirmed | PASS |
| 94→82 ×4 @[578,1182,1353,1742] | confirmed | PASS |
| `87 64 77 84` @1800 | confirmed | PASS |
| "la veut" `11 67` @1044, unique | confirmed | PASS |

## 4. Rotation — STRUCTURE CONFIRMED, two wording corrections

- chi²=366.3 **reproduced to the decimal** (df=4 explicitly, p≈5e-78, n=1,514 transitions) under the lane's A/B/C labels.
- Independent Hellinger-geometry k-means (k=3, 40 restarts) finds the 3-cycle independently: chi²=555.4 on 4df; cosine variant 561.3. Agreement with claimed phase map: 0.75 on non-R groups.
- **Cycle direction — labeling artifact, not a contradiction.** F11's "A→C→B→A" describes the old parse; under repaired labels the dominant direction reads A→B→C→A, and an independent cosine geometry flips it. Direction must NOT be cited as intrinsic. Robust: 3 phases, suppressed self-transitions, dominant directed 3-cycle (181.3 old / 366.3 repaired / 555+ independent). Adopt REPORT.md's already-revised F11 wording.
- **Lag-3 — significance stands, decimals unconfirmed.** Claimed z=+5.6 (0.4219/0.3530); independent: z≈+4.6–4.77, p~1e-6–1e-8. Soften the decimals. Lag-2 z=−3.18 was checked by neither verifier — flagged, not refuted.
- Methodological note: plain Euclidean k-means on contact profiles degenerates ([2,22,72], no structure) — wrong geometry for distributions; Hellinger/cosine required. Documented pitfall.

## 5. Anchor inventory — POSITIONS VERIFIED, values rest on manuscript

- All 11 anchor groups (7 pencil GT: 11, 70, 82, 34, 29, 40, 46; provisional 87, 64, 96; provisional-conditioned 77) exist with plausible counts; `11 70 82 34 29 40` @754 and @1034 confirmed pair-by-pair.
- 87→64=5/32 matches claimed P(64|87)=0.1562.
- **Distinction:** digit statistics verify existence and position only. The VALUE assignments (11=la, 87=ce, 77=le…) rest on the erased pencil manuscript / lane inference and are not independently verifiable from the digit stream.

## 6. Required corrections (before building further — none block cracking work)

1. Update six stale counts+ranks in NOTES.md/STATE.md (n64=47, n00=55, n11=45, n82=39, n34=11, n29=45; ranks as above).
2. Adopt corrected F11 cycle-direction wording (direction is labeling-relative).
3. Soften lag-3 decimals to z≈+5; flag lag-2 z=−3.18 as unchecked.
4. Re-run `closer64_87_results.json` and `crowd3/morphologist_results.json` on the repaired parse.
5. Elevate "conditionally canonical" repair wording to STATE.md standing facts.
6. Apply small number fixes ("00 leads at 55", rank(64)=3, 11/39=28.2%, 7/45, 2.44%/64×).

## Artifacts
- `code/bedrock/verifier_a.py`, `verifier_a_results.json`, `verifier_a_ledger.md`
- `code/bedrock/verifier_b.py`, `verifier_b_results.json`, `verifier_b_ledger.md`
- `code/bedrock/redteam_adjudication.md`
- `code/bedrock/report_inbox/bedrock-redteam.md` (REPORTING.md-shaped, for the 2h sweeper)

Verifier independence CONFIRMED: A and B agree on 100% of overlapping facts with
zero disagreements — no derivation ambiguity; all mismatches are lane staleness.
