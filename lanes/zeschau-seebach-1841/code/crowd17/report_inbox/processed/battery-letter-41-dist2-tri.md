# Battery report — letter-41-dist2-tri

- Target id: `letter-41-dist2-tri` (priority 3)
- Claim: extend the distance-2 letter-cell leads (@59 "41 08 34", @1048 "41 88 29", @237 "70 98 41") into word-internal readings.
- Date: 2026-10-09
- Worker: subagent letter-41-dist2-tri (session 3f3aacb6-3b87-48fd-9338-fbade677d243)
- Parent evidence: battery-wordinternal-41-census NULL follow-up 2.

## Bar (verbatim, from battery-queue.json)

"pass iff any window yields a kill-grade French word containing the granted letters, else keep 41 outside the letter tier"

## Numbered pass/fail clauses (pre-registered before testing, not modified after)

- **C1:** Window @59 ("41 08 34=i", row a1_01) yields a kill-grade French word containing the granted letters.
- **C2:** Window @1048 ("41 88 29=er", row a6_04) yields a kill-grade French word containing the granted letters.
- **C3:** Window @237 ("70=pre 98 41", row a2_01) yields a kill-grade French word containing the granted letters.

**Kill-grade word reading** (pre-registered standard): the window's cells compose a
complete, grammatical French word containing the granted letters in observed order,
with 41 word-internal, such that the word is UNIQUELY forced — exactly one French
word is consistent with the standing cell values (open-valued letter-tier cells may
take the values the word requires), with no rival word and no rival segmentation.
Cells with standing non-letter values (verb-stem 88, word-valued 98) cannot serve as
letters. Standard follows the val-61-premier locus ("61 40 17" = "première fois",
unique stream-wide).

Verdict rule: **promote** iff any of C1–C3 passes (41's letter-tier arm advances via
that window); else the fence fires (keep 41 outside the letter tier) → **null** with
1–3 follow-ups (val-01-rival-sweep precedent: fence outcome = NULL, evidentiary not
terminal).

## Method

1. Read BATTERY-PROTOCOL.md in full before testing. Created
   `code/crowd17/next-token/locks/letter-41-dist2-tri.lock` on start
   (agent id + 2026-10-09T17:20:28Z); no stale lock for this target existed.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`
   (`[s[i:i+2] for i in range(o, len(s)-1, 2)]`, offsets from
   `code/side-keyhunt/repaired_offsets.json`, rows from `data/upstream-ct_R5005.txt`).
   Asserts held: 1,847 pairs, 96 types, n(41)=19. `canonical.py` never used. R5005,
   sealed gate instances, and the red-team adjudication queue untouched.
3. Adopted, never re-litigated: protocol §7 standings; 08 letter-tier value-open
   (stem-08-letter-probe PROMOTE, 2026-10-09); 98='vient' (vient-98-name PROMOTE,
   2026-10-08, battery grade, explicitly covering @236); 88 verb-stem (A3 frame;
   lane usage: verb-88 / infinitive-88 hypothesis / "[88-V]").
4. The claim's "@237 '70 98 41'" trigram sits at pair indices 235–237
   (70@235, 98@236, 41@237) — the 41 is at 237; window addressed as @235–237.

## Window-level evidence (all @-offsets 0-based pair indices, byte-verified)

Granted letter cells in play: 34=i, 29=er, 40=e, 12=n (banked GT + letter-tier n).

### W1 — @59, row a1_01: `85 58 35 53 12 41 08 34 29 40 12 94 92 69` (@54–67)

Letter-capable run @58–64: `12=n 41 08 34=i 29=er 40=e 12=n`. Complete-word
candidates containing the granted letters (i, er):
- @59–62 `41 08 i er` = ??ier (5 letters): **acier, osier, trier, crier, prier,
  scier** — 6 rivals; 41 unforged (a/o/t/c/p/s).
- @59–63 `41 08 i er e` = ??ière (6 letters): **prière** (p,r — unique common
  word) vs **brière** (proper noun, La Brière).
- @59–64 `41 08 i er e n` = ??ièren: no French word. @58–63 `n ??ière`: none.
- Segmentation @59–62 vs @59–63 is underdetermined: no boundary evidence at
  @58|59, @62|63, or @63|64 (neighbors 12=n both sides are boundary-compatible
  either way). The two viable segmentations assign 41 different values.

Strongest lead: "prière" (41=p, 08=r) — unique common word in its segmentation,
but the segmentation itself is not forced. **Not kill-grade.**

### W2 — @1048, row a6_04: `63 11 67 76 85 41 88 29 40 29 74 74 45 23` (@1043–1056)

Fencing cause (class): 88 stands as **verb-stem (A3 frame)** per lane usage
(verb-88, infinitive-88 hypothesis, "[88-V]" readings). A word-internal letter
reading `41 88 29=er 40=e` requires 88 to be a single letter — class-incompatible
with the standing A3 verb-stem frame. Arm fenced with stated cause.
Belt-and-suspenders (hypothetical, 88-as-letter): @1048–1051 `41 88 er e` = ??ère
(5 letters): **frère, bière, fière, opère, avère, acère** — 6 rivals;
@1048–1050 `41 88 er` = ??er: **fier, hier, lier, amer, suer, tuer, muer,
nuer** — 8 rivals; @1048–1052 `41 88 er e er` = ??erere: none.
**Not kill-grade** (fenced by class; underdetermined even hypothetically).

### W3 — @235–237, row a2_01: `96 21 60 71 51 70 98 41 17 11 26 12 16 56` (@230–243)

Fencing cause (standing battery verdict): vient-98-name PROMOTE (2026-10-08,
battery grade) explicitly covers @236 — "`70 98` with 70='pre' (banked) reads
'pré-vient' = 'prévient' (prévenir, 3sg)". Under the adopted reading the window is
**"prévient [41]"**: 98 is a word, 41 is word-external. The word-internal letter
reading ("pre"+letter+letter) contradicts the standing promote and is not
re-litigated here. Note: the parent census (2026-10-09) listed this lead without
flagging 98='vient' (promoted 2026-10-08) — recorded here as a discovered tension,
adopted per lane convention.
Belt-and-suspenders (hypothetical, 98-as-letter): `70=pre 98 41` = pre?? 
(5 letters): **prend, preux, prêts, préau, prêta** — 5 rivals.
**Not kill-grade** (fenced by standing verdict; underdetermined even hypothetically).

## Per-clause pass/fail

- **C1 (@59): FAIL** — no kill-grade word. Best reading "prière" (41=p, 08=r) is
  the unique common word only within the @59–63 segmentation, which is not forced
  (@59–62 yields 6 rivals: acier/osier/trier/crier/prier/scier).
- **C2 (@1048): FAIL** — fenced: 88 is verb-stem (A3), class-incompatible with a
  letter reading; 6+8 rivals even hypothetically (frère/bière/fière/opère/avère/
  acère; fier/hier/lier/amer/suer/tuer/muer/nuer).
- **C3 (@235–237): FAIL** — fenced: standing 98='vient' battery promote reads the
  window as "prévient [41]" (41 word-external); 5 rivals even hypothetically
  (prend/preux/prêts/préau/prêta).

No window yields a kill-grade French word containing the granted letters. The bar's
pass condition is determinately false (not inconclusive): the fence fires.

## Verdict

**NULL** — fence outcome per pre-registered bar (val-01-rival-sweep precedent):
**keep 41 outside the letter tier.** The fence is evidentiary, not terminal —
re-openable when the middle cells' values bank (08 value-open; 88/98 class- or
word-valued by standing verdicts).

## Follow-ups (per §4; all verified ABSENT from battery-queue.json — for the supervisor to queue)

1. `letter-41-08-rerun` (P3) — Re-test W1 (@59) once 08's letter value is banked.
   Bar: "pass iff the banked 08 value admits exactly one French word over
   41,08,i,er(,e) with a forced segmentation, else keep 41 outside the letter
   tier." Rationale: "prière" (41=p) is the unique common-word @59–63 reading iff
   08=r; currently 08 value-open and the @59–62 vs @59–63 segmentation is
   underdetermined (6 rivals in the shorter: acier/osier/trier/crier/prier/scier).
2. `letter-41-88-classcheck` (P3) — W2's letter arm requires 88 as a letter, but 88
   stands as verb-stem (A3 frame). Bar: "pass iff 88's verb-stem frame is
   scoped/downgraded away from @1049 AND exactly one of {frère, bière, fière,
   opère, avère, acère} survives, else keep the W2 arm fenced."
3. `wordbound-41-59-seg` (P3) — Boundary evidence at W1 to force the segmentation.
   Bar: "pass iff neighbor-class boundary rules select exactly one segmentation
   (@59–62 vs @59–63) over @58–64, else fence the segmentation as
   underdetermined." Decides whether "prière" (41=p) is even segmentally viable.

## Scope

Repaired stream only (1,847 pairs, 96 types, n(41)=19). Standing values per
protocol §7 plus adopted battery verdicts (stem-08-letter-probe, vient-98-name —
neither re-litigated, none contradicted or downgraded). No red-team docket item
touched. No invented numbers: every @-offset re-derived in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`.

## Bookkeeping

- Lock created: `code/crowd17/next-token/locks/letter-41-dist2-tri.lock`
  (agent id + 2026-10-09T17:20:28Z); no stale lock present. Deleted on completion.
- Report: `code/crowd17/report_inbox/battery-letter-41-dist2-tri.md` (this file).
- Queue: target `letter-41-dist2-tri` set to status `verdict` (NULL) — own-entry-only
  temp-file+rename write, pre-write assert queued/verdictless, JSON re-validated.
