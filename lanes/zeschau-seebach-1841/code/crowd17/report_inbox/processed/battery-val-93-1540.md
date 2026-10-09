# Battery report: val-93-1540

- Target id: `val-93-1540`
- Claim: "Name 93's value at @1540; a named governor constrains 88's infinitive semantic class at @1541."
- Date: 2026-10-09
- Worker: battery worker (subagent 2f7f7f92-fd68-4c07-9a01-6bf443efbdae)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched. @i = 0-based pair index.

Terms (ASD-STE100): "name" = assign a specific French value at battery grade. "Ungranted assumption" = any premise not banked, granted, promoted, or battery-grade in the lane record. "Fence" = the question is closed at battery grade with a stated cause; it is not decided.

## Bar (verbatim, pre-registered before testing)

"Value named with zero ungranted assumptions; else fence."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 93's value is named at @1540 with zero ungranted assumptions → PROMOTE.
2. **C2 (else-arm):** if no value can be named under that standard, fence with stated cause → NULL (fence executed).

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-93-1540.lock` on start (agent id + 2026-10-09T19:09:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Adopted (not re-litigated): 93 = verb class (R19-166 class grant; R20 defers the value with cause). Standing values used: 06=ent promoted, 11=la GT, 21=noun class-level, 29=er GT, 40=e GT, 46=que GT, 47=ce A4, 59=est provisional, 64=qui granted, 67=et/veut sole polyvalence, 77=le provisional, 78=ver LEAD, 82=m GT, 84=on conditional, 88=governor class-level, 94=ne STRONG LEAD. 1841 diplomatic French throughout.

## Window-level evidence

### @1540 locus, byte-confirmed

Row context (0-based): `@1534=73 @1535=41 @1536=62 @1537=06 @1538=21 @1539=62 @1540=93 @1541=88 @1542=77 @1543=78 @1544=43 @1545=00 @1546=46`

Under standing values: `[73] [41] [62] ent [21-N] [62] [93-V] [88-gov] le ver [43-N] pour que`

93 sits in the governor slot before 88 (governor-class, infinitive-complement government). The slot is a French "verb + [infinitive]" frame, but it admits the entire open governor class: vouloir, pouvoir, devoir, savoir, aller, venir, commencer, essayer, oublier, cesser, daigner, and dozens more.

### Full 93 census (n=14), all windows byte-exact on the repaired stream

| @ | -3..-1 | 93 | +1..+3 | follower |
|---|--------|-----|--------|----------|
| 10 | 77 78 18 | 93 | 62 98 76 | 62 |
| 102 | 21 62 94 | 93 | 59 45 28 | 59=est |
| 111 | 11 21 67 | 93 | 29 89 68 | 29=er |
| 159 | 35 58 35 | 93 | 52 94 24 | 52 |
| 263 | 84 74 45 | 93 | 52 33 42 | 52 |
| 479 | 78 74 45 | 93 | 00 13 52 | 00=pour |
| 604 | 26 96 45 | 93 | 54 64 39 | 54 |
| 734 | 11 24 85 | 93 | 76 18 82 | 76=noun |
| 1540 | 06 21 62 | 93 | 88 77 78 | 88=gov |
| 1555 | 23 99 13 | 93 | 61 40 17 | 61=premier |
| 1685 | 79 65 13 | 93 | 62 94 79 | 62 |
| 1761 | 78 41 15 | 93 | 06 77 84 | 06=ent |
| 1812 | 04 61 15 | 93 | 50 42 06 | 50 |
| 1846 | 78 49 74 | 93 | (stream end) | — |

Follower inventory (11 distinct): {62×2, 59, 29, 52×2, 00, 54, 76, 88, 61, 06, 50}. Predecessor inventory (10 distinct): {18, 94, 67, 35, 45×3, 85, 62, 13×2, 15×2, 74}. The distribution is heterogeneous at both edges — no recurring frame pins a value.

### Why no window names a value with zero ungranted assumptions

- **@1540:** the governor slot is discriminator-free. The left neighbor 62 is value-open; the right context "88 le ver [43-N] pour que" is compatible with every semi-auxiliary governor. Naming any one verb requires ≥1 ungranted assumption (a guess about 62, or a semantic preference with no byte leg).
- **@111** ("11 21 67 [93] 29 89"): "et [93]er [89-N]" is suggestive of an infinitive complement, but 93 is verb-class (not stem-class); reading "[93]er" as one word contradicts the class grant unless 29 attaches rightward — an ungranted segmentation assumption. Not nameable.
- **@479** ("ce [93] pour [13]"): needs a 93 value that takes "ce" as subject — any intransitive modal; no discriminator.
- **@604** ("par ce [93] 54 qui 39"): three open neighbors; no discriminator.
- All other windows likewise: every candidate value needs at least one assumption about an open neighbor (62, 52, 54, 61, 50, 13, 15, 73, 41) or an unlicensed segmentation.

The bar's "zero ungranted assumptions" standard is not met by any window. C1 fails.

## Per-clause pass/fail

- **C1: FAIL.** No 93 value can be named with zero ungranted assumptions — the full 14-window census shows heterogeneous frames and every candidate needs ≥1 assumption about an open neighbor.
- **C2: FIRES.** Fence executed with stated cause (below).

## Verdict: NULL (fence executed)

**Fence:** 93's value is unnameable at battery grade. All 14 windows were censused byte-exact; the @1540 governor slot (`[62] [93] [88-gov]`) admits the full open class of French semi-auxiliary/modal governors with no discriminator; no other window supplies a discriminating frame without an ungranted assumption. 93 stays verb-class (R19-166 grant stands; R20 value-defer stands). The claim's hoped-for consequence — a named governor constraining 88's infinitive semantic class at @1541 — does not fire.

No standing or red-team verdict is contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands (row offsets unvalidated, 68/70).

## Follow-ups (nulls regenerate work; all ids verified ABSENT from battery-queue.json)

1. **gov-93-88-frame** (P3): census whether 93's followers across all 14 windows are consistently infinitive-shaped; if yes, 93 = semi-auxiliary governor *class* candidate (class-level, not value); else fence the governor-class reading.
2. **val-93-111-inf** (P4): test @111 "67 [93] 29" as "et [93]er" — a licensed -er infinitive reading of 93 narrows the governor class at battery grade; else fence the infinitive arm.
3. **val-62-1539-discrim** (P4): name 62's value at @1539; 62 is the only byte-internal discriminator adjacent to the @1540 governor slot, and its value gates any future 93-naming attempt there.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-93-1540.md` (this file).
- Queue: `val-93-1540` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; same-directory temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-93-1540.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
