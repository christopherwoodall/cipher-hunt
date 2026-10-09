# Battery verdict: val-52-55-class

- Target: `val-52-55-class` (battery-queue.json, priority 3, status queued)
- Claim: name the classes of 52 and 55 to license the rightward-13 attachment at @481/@575/@1166.
- Worker: 8439805b-730e-4581-bacc-63a4f4437a7a. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/val-52-55-class.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"name 52/55 classes iff they parse with standing values and zero new assumptions; else fence"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (55):** name 55's class at @576/@1167 with standing values and zero new assumptions; if unnameable, fence it.
2. **C2 (52):** name 52's class at @482 with standing values and zero new assumptions; if unnameable, fence it.

Standing values used (per protocol §7): pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour A9, 84=on A15, 47=ce A4; 45=ce A11); provisional (59=est, 77=le); 94='ne' STRONG LEAD (R17-001); granted word-unit "55+61=prend" (R19-077 GRANT, confirmed at @576/@1167 by seg-55-61-94-letters PROMOTE 2026-10-09); R19-079 GRANT (55's class named verb at the @1205 "prend" window). Kills: 62='il' (R19-106, R20-125). 52, 55, 13 all UNIDENTIFIED in registry (R20-027).

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed all loci and row labels.
3. Adopted (not re-litigated): R19-077 ("55+61=prend" bare finite stem; letter-level tension fenced as §7), R19-079 (55's class=verb at @1205; 11-vs-1 segmentation tension red-team venue), seg-55-61-94-letters (2026-10-09 PROMOTE: 55+61="prend" word, 94='ne' particle at @576/@1167; internal "prend" split residual scoped), unif-52a-1334-orphan (2026-10-09 PROMOTE: 52="a" x26, @1332 fenced as syllable; §7 split escalated), reseg-13-rightward (parent NULL: rightward-13 fenced; leftward killed by reseg-13-armB).

## Window-level evidence (byte-confirmed, in-session)

- **@575 (row a3_02):** `[573]78 [574]45 [575]13 [576]55 [577]61 [578]94 [579]82` = "...[78] ce [13] [55] [61] ne [82]...". 55 at @576, followed by 61.
- **@1166 (row a6_09):** `[1164]78 [1165]45 [1166]13 [1167]55 [1168]61 [1169]94 [1170]87` = "...[78] ce [13] [55] [61] ne [87]...". 55 at @1167, followed by 61.
- **@481 (row a2_11):** `[479]93 [480]00 [481]13 [482]52 [483]30 [484]01` = "...[93] pour [13] [52] [30] [01]...". 52 at @482, preceded by 13, followed by 30.

## Clause results

### C1: PASS — 55's class = VERB at @576/@1167

- The "55 61" bigram at @576/@1167 is the word "prend" (bare finite stem), red-team GRANTed (R19-077) and confirmed at exactly these two windows by seg-55-61-94-letters (PROMOTE, 2026-10-09): "55+61 is the word 'prend', 94='ne' particle".
- Precedent: R19-079 GRANT named "55's class = verb" at the @1205 "55 61"='prend' window ("58 47 43 55 61 21 65"). Same structure at @576/@1167 → same class, by granted precedent.
- Nominal excluded at battery grade: 55 is word-internal to the finite verb "prend"; a nominal reading of the cell is incoherent.
- Stem excluded: the stem of "prendre" is "pren-/prend-"; the live internal-split residual (55='pre'/'pr' + 61='nd'/'end', per seg-55-61-94-letters) makes 55 a syllable/prefix, not a stem; 61='pren' is killed globally (seg-61-pren-polyvalence).
- The lane's class convention (R19-079) names the word's class for the composing cell: VERB (55 is descriptively sub-lexical, but its class is the verb word's).
- Zero new assumptions: no value named for 55; no new grammatical rule; only standing values + granted findings + granted precedent.
- **Consequence for the parent (reseg-13-rightward):** the "granted nominal-55" route to its C1 is CLOSED at battery grade. A nominal "13-55" word-unit would break the granted "prend" word-unit → kill-grade dead at @575/@1166. The only surviving rightward arm there is "13"+"prend" as a larger unit, which needs 13's letter content (val-13-letter, queued).

### C2: FENCE (else-arm fires) — 52's class at @482 unnameable

- **Finite-verb class KILLED at kill grade:** 00='pour' (A9 preposition) cannot govern a finite clause ("pour" + finite verb is ungrammatical in French, value-independent of 13). So 52 is not a finite verb ('a' or otherwise) at @482.
- Letter-tier ('a' composing leftward with 13 or rightward with 30): possible, but 13's content is open (val-13-letter queued) and 30's content is open → not nameable with zero new assumptions.
- Preposition 'à': "pour [13] à [30] [01]" needs 13/30/01 values (all open) and has no standing frame → not nameable.
- Nominal: "pour [13] [52-noun]" needs 13 nominal (open); zero positive legs → not nameable.
- Stem: needs a completion neighbor; followers are 30, 01 (29='er' absent); zero positive legs → not nameable.
- 52 is UNIDENTIFIED in the registry (R20-027); the battery-grade 52="a" (x26, unif-52a) is verb-or-letter per the escalated §7 split, and neither arm is licensable at this window.
- → 52's class at @482 is FENCED with stated cause (finite-verb arm killed; all other arms need open neighbor values).

## Verdict: PROMOTE

C1 passes (55=VERB named at battery grade, zero new assumptions). C2's else-arm fires as the bar specifies (52's class fenced with stated cause; finite-verb arm killed at kill grade). No adverses listed; none ignored. No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands.

Net for the parent docket: the nominal-52/55 route to reseg-13-rightward C1 is closed (55=VERB, not nominal; 52's class fenced). The rightward-13 attachment remains unlicensed; val-13-letter (queued) is the remaining key, and even a named letter-13 would still need 52's class (fenced at @481) to complete the @481 arm.

## Scope

- Names 55's class (VERB) at @576/@1167 only. Does not name 55's value; does not touch the "55 81" x6 population, the "55 83" x2 / "55 68" x1 windows, the internal "prend" letter-split residual (§7), or the 11-vs-1 segmentation tension (red-team venue, R19-079).
- Fences 52's class at @482 only. Does not touch 52="a" x26, the @1332 syllable locus, or the escalated redteam-52a-syllable-split (§7).
- Does not change reseg-13-rightward's verdict (NULL/fence stands); supplies the class input its follow-up requested.

## Bookkeeping

- `battery-queue.json`: `val-52-55-class` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-52-55-class.tmp` + atomic rename; disk re-validated; own entry only; no downgrade).
- Lock `locks/val-52-55-class.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
