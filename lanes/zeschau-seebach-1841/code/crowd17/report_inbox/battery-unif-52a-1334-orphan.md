# Battery verdict: unif-52a-1334-orphan

- Target: `unif-52a-1334-orphan` (battery-queue.json, priority 3, status queued)
- Claim: A10-orphan test: apply the stem-56-whole nameability standard to 52="a" at @1334 ("preaa" non-word; "a de [INF]" ungrammatical per de83-39-1334). Bar: orphan confirmed iff the status strands a non-word under standing values; then fence the uniformity extension of 52="a" to @1334 (escalate the 52="a"-vs-syllable tension to the red team if the global orphan rate otherwise holds).

## Bar (verbatim, numbered)

C1. Orphan confirmed iff the 52="a" status strands a non-word under standing values at the @1334 window.
C2. Fence the uniformity extension of 52="a" to @1334.
C3. Escalate the 52="a"-vs-syllable tension to the red team iff the global orphan rate otherwise holds.

Note: the queue entry's claim/bars text embeds two further numbered items (`ne-1330-bare-corpus`, `subj-62-1329-agree`). These are separate targets, not this bar: `ne-1330-bare-corpus` already holds verdict/promote; `subj-62-1329-agree` is queued. Both out of scope here.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/unif-52a-1334-orphan.lock` on start (agent 6d157938-99e9-4d2d-b0b4-d7668b508e19, 2026-10-09T19:45:00Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types. `canonical.py` never used.
3. Byte-confirmed the locus: 0-based @1331=70, @1332=52, @1333=39, @1334=83, @1335=86 (rows a7_04/a7_05; the target's "@1334" names the 83 position per the de83-39-1334 convention; 52 sits at 0-based @1332). "70-52" and "52-39" each exactly 1x stream-wide (hapaxes).
4. Adopted (not re-litigated): 70="pre" (pencil GT); 39=/a/ (`a-39` PROMOTE — word "a"/"à" or word-internal 'a'); 83="de" (lead); de83-39-1334 PROMOTE (conditional collision matrix: "a de [INF]"/"à de [INF]" ungrammatical iff 39='a/à' AND 83='de' ratify); seg-528294-word PROMOTE (52="a" in the "amne..." word-unit — explicitly scoped "word-unit only", conditional on the fenced red-team 94 ruling); stem-56-whole PROMOTE (nameability standard); profile-52-host-word NULL (three-way syllable tie 'scri'/'ser'/'voi' at this locus, unbreakable stream-wide); syll-52-locus-1334 NULL (recorded the 52="a"-uniformity-vs-locus-parse tension — this battery is its venue).

## Findings

### C1 — orphan confirmed: PASS

Under the 52="a" status, the window 0-based @1331–@1335 = `70("pre") 52 39(/a/) 83("de"-lead) 86(INF)` strands a non-word in every composition arm:

- Arm 1 (all word-internal): "pre"+"a"+"a" = "preaa" — not a French word. Dead.
- Arm 2 (39 as separate word): "prea" + "a"/"à" + "de" + INF. "prea" is not a French word; and the "a de [INF]"/"à de [INF]" tail is ungrammatical per de83-39-1334's own matrix (premises currently battery-grade: a-39 PROMOTE + 83="de" lead; the matrix's ratification condition is unmet, so this arm is fenced-conditional, not kill-grade — but Arm 1 already suffices). Dead.
- Arm 3 (leftward composition): left neighbor @1330=94 ("ne", STRONG LEAD) cannot compose with "pre". Dead.
- No re-segmentation rescues: 52="à" (preposition) gives "pre à de" — worse; 39 word-final gives "prea" — non-word.

The orphan is confirmed at battery grade: the 52="a" status strands a non-word at this window under standing values.

### Global orphan rate (C3 condition)

Rendered all 27 windows of 52 with 52="a" and standing values substituted (±2 context). The @1332 window is the ONLY one with the "pre _ a" stranding shape (`94=ne 70=pre 52=a 39=a/à 83=de`). At the other 26 windows 52="a" sits in licensable positions ("ne a", "qui a", "la a", "a de [INF]"-free contexts, etc.) with no stranded non-word — consistent with seg-528294-word C2's zero-forced-contradiction compatibility result across all 27 windows (adopted).

Global orphan rate: 1/27. The 52="a" status otherwise holds → the C3 escalation condition fires.

### C2 — fence the uniformity extension: PASS

The uniformity hypothesis (52="a" at all 27 windows) fails at @1332. The extension of 52="a" to this window is FENCED. The locus keeps its live syllable reading ('scri'/'ser'/'voi' per the adopted three-way tie — each yields a clean French word where "a" orphans). This does not overturn seg-528294-word PROMOTE (explicitly word-unit-scoped and conditional); it refines it.

### C3 — escalate: RECORDED

The 52="a"-vs-syllable tension is a classic §7 conditioned-split shape (uniform "a" ×26 vs syllable ×1 at @1332). Battery cannot declare it. Escalated to the red team — proposed venue target below.

## Verdict: PROMOTE

All bar clauses pass; no adverses listed. The orphan is confirmed, the uniformity extension of 52="a" to @1334 is fenced, and the §7 tension is escalated.

## Scope

- Fences only the uniform extension of 52="a" to the @1332 window. 52="a" stands (scoped, conditional) at the other 26 windows per seg-528294-word.
- Untouched: a-39 PROMOTE, de83-39-1334's conditional matrix, the 'scri'/'ser'/'voi' tie, 94="ne" STRONG LEAD, 67 sole polyvalence, §7 (no split declared — red-team venue).
- No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a7_04/a7_05 boundary offsets unvalidated).

## Follow-ups (for supervisor queuing)

1. `redteam-52a-syllable-split` (P2, red-team venue) — §7 adjudication: uniform 52="a" ×26 vs conditioned syllable at @1332 ('scri'/'ser'/'voi' tie). Package: this report + seg-528294-word + syll-52-locus-1334 + profile-52-host-word + de83-39-1334.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-unif-52a-1334-orphan.md`
- Queue: `unif-52a-1334-orphan` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.unif-52a-1334-orphan.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/unif-52a-1334-orphan.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
