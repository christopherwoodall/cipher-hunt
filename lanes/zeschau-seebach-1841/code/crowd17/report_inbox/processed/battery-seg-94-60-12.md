# Battery report: seg-94-60-12

- Target id: `seg-94-60-12`
- Claim: Re-segment V2's "94 60 12 98" (@699-702); V2 admits no grammatical French parse as segmented.
- Date: 2026-10-09
- Worker: battery worker (subagent f4de01b8-deb4-489e-b3f3-a7bd29a4c927)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- @i = 0-based pair index.

Terms (ASD-STE100): "re-segment" = change word boundaries without changing the pair order. "Segmentation residual" = a window that stays unparsed after all licensed re-segmentations are tried; it is kept as an open problem, not a claim. "Battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"produce one grammatical parse of @699-702 under standing values with stated word boundaries — testing (i) 94 leftward ('[28]ne'), (ii) 94='ni' with 12+98='ni', (iii) a clause boundary between 60 and 12 — using only banked/granted/promoted values; else fence V2 as a segmentation residual with stated cause"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** one grammatical parse of @699-702 exists under standing (banked/granted/promoted) values with stated word boundaries, via arm (i), (ii), or (iii).
2. **C2 (else-arm):** if no such parse exists, fence V2 as a segmentation residual with stated cause → NULL.

Adverses listed: 94='ne' STRONG LEAD R17-001 (do not overturn without red-team declaration — fence, don't declare); 28 hapax predecessor.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/seg-94-60-12.lock` on start (agent id + 2026-10-09T18:53:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Adopted (not re-litigated): 94='ne' STRONG LEAD (R17-001); 12='n' PROMOTE; 46='que', 45='ce' standing; 98 open (98='vient' is LEAD only, not a licensed value for parsing); 60/28/02/50 open.
4. Grammar tests in 1841 diplomatic French throughout.

## Window-level evidence (byte-exact)

Locus, 0-based: `@698=28 @699=94 @700=60 @701=12 @702=98`, all on row a5_01.
Wider frame @694–705: `46 02 50 45 28 94 60 12 98 20 12 66` =
"que[46] [02] [50] ce[45] [28] ne[94] [60] n[12] [98] [20]…".

Stream censuses (re-derived):
- "94 60" = 1x stream-wide (@699 only); "94 60 12 98" = 1x (hapax window).
- "28 94" = 1x (@698; 28's only 94 contact, n(28)=6).
- "60 12" = 2x (@700, @1735); "12 98" = 1x (@701 only).
- No 30 ('pas') within ±15 of @699 — no "ne…pas" completion anywhere near.
- Twin anomaly @841: "94 26[noun-lead] 12" = "ne [26] n[12]" — likewise ungrammatical as segmented (verb-60-bare).

## Per-clause testing

### Arm (i): 94 leftward → "[28]ne" one word

Parse shape: "…ce[45] [28]ne [60] [12] [98]…". The "ne" particle is consumed,
so the double-"ne" blocker of verb-60-bare's arm (b) is gone — but the right
edge still fails:

- "12 98" must parse as "n'"-elision ("n'[98]") or a word "n[98]".
  12='n' is PROMOTE. "n'"-elision requires a vowel-initial host; 98's value
  is open (98='vient' is LEAD only, and 'vient' is consonant-initial anyway —
  "n'vient" is not French). No licensed vowel-initial value for 98 exists.
- "n[98]" as a word ("non"/"nous"/"notre"/"nul") needs 98='on'/'ous'/'otre'/'ul'
  — all unlicensed; 84='on' is a different group (§7).
- "60 12" as "[60]n" word-final: verb-final bare -n is impossible (adopted
  from verb-60-bare's exhaustion); as a noun ("rien"-shaped) it needs 60='rie'
  — unlicensed.
- "ce [28]ne" as subject NP ("ce personne"-shaped) is ungrammatical
  (45='ce' hold A11; "personne" needs "cette").
- 28's value is open, so no specific "[28]ne" word ("donne"/"prenne"/
  "personne") can be licensed at battery grade.

**Arm (i) fails:** no complete grammatical parse with licensed values only.
The right edge "12 98" is unparseable without a licensed 98 value.

### Arm (ii): 94='ni' with 12+98='ni'

Parse shape: "…[28] ni[94] [60] ni[12+98] [20]…" = "ni [60] ni…" correlative.

Two independent kill-grade blocks:

1. **Adverse block (jurisdictional):** 94='ne' is STRONG LEAD (R17-001).
   Naming 94='ni' at this window is a second 94 value — §7 territory,
   red-team venue only. The bar's own adverse forbids overturning it here
   ("fence, don't declare"). Battery grade cannot act on this arm.
2. **Value block:** "12+98"='ni' needs 98='i' — unlicensed. 12='n' is
   PROMOTE, but the 'i' half has no lane record.

**Arm (ii) fails:** barred by the adverse and by 98's openness.

### Arm (iii): clause boundary between 60 and 12

Parse shape: "…ne[94] [60-verb] | n'[12][98] [20]…".

- Left clause "ne [60]": no "pas" within ±15; expletive-"ne" needs a licensed
  governor among @694–698 (02/50/28 — all open, no values). Unlicensed.
- Right clause "n'[98] [20]…": needs vowel-initial 98 — unlicensed (as in
  arm (i)). 20's relative-adverb reading is licensed only after "n'importe",
  which needs 98='importe' — unlicensed. Noted as the strongest near-miss
  (see follow-up 1).

**Arm (iii) fails:** neither side licenses with standing values only.

### C1 — FAIL. C2 — FIRES.

No arm produces a grammatical parse of @699–702 under banked/granted/
promoted values. The binding constraint is 98's open value: every arm's
right edge ("12 98") dies on it, and 60/28/02/50 are likewise open, so no
arm can be completed at battery grade. Arm (ii) is additionally barred by
the 94='ne' STRONG LEAD adverse.

## Scope (stated, not hidden)

- **Fence only.** V2 (@699–702) is fenced as a segmentation residual: the
  pair order is byte-secure (row a5_01, offset 1, no phase anomaly), but no
  licensed segmentation yields a grammatical parse. This is a fence, not a
  kill — a future 98 value (or red-team 94 ruling) can re-open it.
- The parent's V1/V3/V4 -dre coherence and V2 impossibility proof stand
  untouched; verb-60-dre / verb-60-er remain the live naming tracks with
  V2 excluded.
- The "12 48"='ne' letter-tier composition seen at @1735–1737 ("60 12 48")
  does not apply at @699 (follower is 98, not 48).
- 94='ne' STRONG LEAD intact; 98='vient' LEAD untouched (not used as a
  licensed value); §7 intact. No standing or red-team verdict contradicted
  or downgraded.

## Verdict: NULL (fence executed)

V2 fenced as a segmentation residual with stated cause: all three licensed
re-segmentation arms fail — (i) and (iii) die on 98's open value at the
right edge, (ii) is barred by the 94='ne' STRONG LEAD adverse plus 98's
openness. The twin anomaly @841 ("94 26 12") corroborates the 94-family
segmentation problem without resolving it.

## Follow-ups (§4; all ids verified ABSENT from battery-queue.json)

1. `val-98-702-importe` (P3) — test 98='importe' at @702: "n'[98]" →
   "n'importe" with 20's battery relative-adverb reading at @703. Bar: name
   98='importe' with ≥2 independent legs or fence. (Strongest near-miss of
   arm (iii).)
2. `ne-expletive-699` (P3) — test expletive-"ne" at @699: needs a licensed
   governor among @694–698 (02/50/28 all open). Bar: name the governor with
   stated values or fence the expletive arm.
3. `redteam-94-v2-input` (P2, gather-only) — package this fence + the @841
   twin + ne-ce-1169 + @1705 "94 88 26 12" as consolidated input to the
   red-team 94 venue (94='ne' STRONG LEAD adjudication).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-94-60-12.md` (this file).
- Queue: `seg-94-60-12` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/seg-94-60-12.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
