# Battery report: redteam-94-v2-input

- Target id: `redteam-94-v2-input`
- Claim: Gather-only: package the seg-94-60-12 fence + the @841 twin + ne-ce-1169 + @1705 "94 88 26 12" as consolidated input to the red-team 94 venue.
- Date: 2026-10-09
- Worker: battery worker (subagent 13342902-e1c3-4a0e-b1d4-f02665300da6)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- @i = 0-based pair index.

## Bar (verbatim, pre-registered)

"deliver the package; gather only, no adjudication. 94='ne' STRONG LEAD adjudication is red-team venue"

Numbered clauses (restated before testing, not modified after):

1. **C1:** the package is delivered with all four inputs byte-verified in-session on the repaired stream.
2. **C2:** no adjudication is made — no value named, no split declared, §7 intact.

Adverses: 94='ne' STRONG LEAD (R17-001) must not be overturned at battery grade; §7 bars any second 94 value at battery grade.

## Package contents

All four loci re-derived byte-exact in-session on the repaired stream.

### 1. seg-94-60-12 fence (V2 @699–702)

- Locus: `@698=28 @699=94 @700=60 @701=12 @702=98`, row a5_01. Wider: `46 02 50 45 28 94 60 12 98 20 12 66` = "que [02] [50] ce [28] ne [60] n [12] [98] [20]…"
- Verdict NULL (fence). All three resegmentation arms fail:
  - (i) 94 leftward ("[28]ne" one word): right edge "12 98" unparseable — "n'"-elision needs vowel-initial 98 (open; "n'vient" not French), "n[98]" as word needs unlicensed 98 values.
  - (ii) 94='ni' + 12+98='ni': barred by the 94='ne' STRONG LEAD adverse (§7, red-team venue) and 98's openness.
  - (iii) clause boundary between 60 and 12: left side needs licensed expletive-ne governor (02/50/28 all open); right side needs vowel-initial 98 (unlicensed).
- Binding constraint: 98's open value — every arm's right edge dies on it.
- Scope: fence only, not kill. V2 is byte-secure (no phase anomaly) but unparseable under licensed values — a future 98 value or red-team 94 ruling re-opens it.
- Report: `code/crowd17/report_inbox/processed/battery-seg-94-60-12.md`

### 2. The @841 twin

- Locus: `@839=20 @840=62 @841=94 @842=26 @843=12` (byte-confirmed in-session).
- Shape: "94 26 12" = "ne [26-noun-LEAD] n[12]" — likewise ungrammatical as segmented (adopted from seg-94-60-12: the 94-family segmentation problem is not a V2 one-off).
- The twin corroborates the pattern without resolving it: 94 sits in an unparseable position, flanked by a noun-class cell and the letter 'n'.

### 3. ne-ce-1169 residual

- Locus: `@1164=78 @1165=45 @1166=13 @1167=55 @1168=61 @1169=94 @1170=87 @1171=83 @1172=21 @1173=85`, row a6_09 (byte-confirmed in-session).
- Verdict NULL (fence). Rescue inventory exhausted at battery grade:
  - Rescue (1) — leftward "...ne" word ("prenne" family): kill-grade dead (seg-61-pren-polyvalence; seg-61-94-word-adjudicate KILL; frame-restricted rescue = §7).
  - Rescue (2) — word-initial "néce-" (nécessaire family): killed (nece-94-87-initial KILL, 2026-10-08, adopted not re-litigated).
- @1169 is a pure segmentation residual — 94-87 unresolvable at battery grade pending 61's value or red-team §7 action. R17-001 untouched.
- Report: `code/crowd17/report_inbox/processed/battery-nece-1169-revisit.md`

### 4. @1705 "94 88 26 12"

- Locus: `@1703=20 @1704=62 @1705=94 @1706=88 @1707=26 @1708=12 @1709=06` (byte-confirmed in-session).
- Shape: "94 88 26 12" = "ne [88-gov] [26] n[12]". 88=governor class (registry), 26=noun LEAD, 12='n' PROMOTE.
- Third instance of the family pattern: 94 followed by a governor/class-only cell, a noun-class cell, and letter 'n' — ungrammatical as a standalone "ne" particle with no licensed parse at battery grade.

## The 94-family pattern (for the red team)

Four independent windows share one structure:

| Locus | Shape | 94's neighbors | Status |
|---|---|---|---|
| @699 (V2) | `28 94 60 12 98` | open 28, open 60, 'n', open 98 | segmentation residual |
| @841 | `94 26 12` | noun-26, 'n' | segmentation residual |
| @1169 | `61 94 87` | open 61, 'ce'-87 | segmentation residual |
| @1705 | `94 88 26 12` | gov-88, noun-26, 'n' | unparseable at battery grade |

In every case 94='ne' (STRONG LEAD, R17-001) cannot parse as a standalone particle, and every resegmentation arm dies on an open neighbor value (98, 61, 60, 28) or a §7 block (second 94 value, conditioned composition). The battery cannot resolve any of them: the blockers are unvalued cells and red-team-venue decisions, not missing diligence.

Standing red-team material this feeds: `redteam-94-functional-split` (P1, queued) — the §7 venue for 94's functional split. The nece-1169-residual gather-only package (proposed follow-up of nece-1169-revisit) is a natural companion; not queued by this worker (gather-only precedent: no follow-ups proposed here).

## Verdict: NULL (gather-only package delivered)

C1 PASS (package delivered, all four loci byte-verified in-session). C2 PASS (no adjudication: no value named, no split declared, §7 intact). No standing/red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands.

## Scope

Package only. 94='ne' STRONG LEAD (R17-001) adopted as premise throughout; the four windows' residual status unchanged; seg-94-60-12's NULL, nece-1169-revisit's NULL, and all standing grants/kills adopted, none re-litigated.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-redteam-94-v2-input.md` (this file).
- Queue: `redteam-94-v2-input` queued → `verdict`/`null` 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.redteam-94-v2-input.tmp` + atomic rename; disk re-validated; own entry only; no downgrade).
- Lock `locks/redteam-94-v2-input.lock`: created on start (2026-10-09T20:02:00Z, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
