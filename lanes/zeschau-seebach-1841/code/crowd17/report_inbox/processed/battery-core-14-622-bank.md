# Battery report: core-14-622-bank

**Target:** `core-14-622-bank` (P2)
**Date:** 2026-10-09
**Verdict:** PROMOTE (finding grade — battery-grade; needs red-team ratification before banked use)

## Bar (verbatim from queue)

"promote iff core parses with zero new assumptions AND >=1 independent 'en'-frame corroborates (the @896 `82 14` leg or the `79 14` gerundive x2)."

## Bar restated as numbered clauses

1. The @622–626 core (`76 82 14 59 37`) parses as "[76-noun] m'en est [37-pred]" with **zero new assumptions** — i.e. using only pencil ground truth, red-team grants, provisional values, battery-promoted premises, and the hypothesis 14='en' itself.
2. **≥1 independent 'en'-frame corroborates**: either the @896 `82 14` leg or the `79 14` gerundive ×2 yields a natural 'en'-frame under 14='en' with no contradiction.

Indexing: all @-offsets below are **1-based** repaired-stream pair indices (matching the bar's convention; the bar's @622–626 = 0-based @621–625). Row a4_01.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/core-14-622-bank.lock` on start (deleted on completion). Re-derived the repaired 1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (byte-exact tokenizer per `repair_parse.py`; count asserts 1847). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. Prior batteries consulted as prior work, every byte claim re-derived independently: `battery-clitic-14-623-steelman.md` (NULL — full-window parse blocked; this target is its follow-up #3), `battery-en14-three-window.md` (PROMOTE — 14='en' arm kept).

## Window-level evidence

### C1 — the core @622–626 = `76 82 14 59 37` (row a4_01), stream-unique 5-gram

Byte context (1-based): `619:29 620:88 621:37 | 622:76 623:82 624:14 625:59 626:37 | 627:33 628:29 629:87`.

Parse under standing values only:

| @ | pair | standing value | role |
|---|------|----------------|------|
| 622 | 76 | noun (battery-promoted 2026-10-08) | subject noun |
| 623 | 82 | 'm' (pencil GT, banked letter) | proclitic `m'` |
| 624 | 14 | 'en' (the hypothesis) | clitic `en` → `m'en` |
| 625 | 59 | 'est' (provisional, standing) | copula |
| 626 | 37 | predicative (A1 granted frame) | predicative complement |

Reading: **"[76-noun] m'en est [37-pred]"** — subject + m' + en + est + predicative. This is the literary `il m'en est resté / garant` pattern (cf. "le souvenir m'en est resté"): grammatical 1841 French. Letter-strictness holds: 82='m' is a banked letter ('me' would need 82+48='e'), so `82 14` reads `m'` + vowel-initial clitic only; `m'y est` is dead per the steelman brief's 'être'-takes-no-'y' argument (adopted, not re-litigated); 14='le' is killed globally (le-14-kill-1121); 14's verb class is fenced lane-wide; 14's determiner arm is licensable only at @117 (det-14-census) — so **'en' is the unique surviving reading of 14 here**.

Assumption audit (C1's "zero new assumptions"):
- 76=noun: battery-promoted 2026-10-08 — pre-existing lane premise, not new.
- 82='m': pencil GT. 59='est': provisional standing. 37 predicative: A1 grant.
- 14='en': the hypothesis itself (not an "assumption" — it is the claim).
- Left boundary before @622: **forced, not assumed.** Left context @621=37 (A1 predicative): "37-pred 76-noun" ("*est resté souvenir") is ungrammatical, and "88 37 76" gives the noun no role — so 76 must head a new clause. The left clause's own incompleteness (@620=88 open) is fenced as `prof-88`'s business (already queued by the steelman battery), not assumed away.
- Right edge: fenced per the claim — the 1-based @626–627 `37 33` bigram is a stream-wide hapax (verified: exactly 1/1847 windows) and is fenced as a red-team residual joint with `frame-37-reexam`. The core's 37-pred is complete without it.

**No rival parse of the core is statable** under standing values (all 14 arms except 'en' are killed/fenced at this window; the clitic order m'-en-est is correct).

### C2 — corroboration

**Option A: the @896 `82 14` leg — does NOT corroborate.** 1-based @896–897 = `82 14` inside `894:01 895:98 896:82 897:14 898:98 899:83 900:86` (row a5_08). Under 14='en': "98-fin m'en 98-fin" — 98's finite-verb class is battery-promoted, so two finite verbs strand the clitic ("vient m'en vient"); proclitic `m'en` before an imperative is ungrammatical and no subject licenses the second finite verb. Re-derived independently; agrees with en14-three-window W2. The failure is **value-independent** (forced by 98's promoted class, not by 14's value): it neither corroborates 'en' nor contradicts it. Option A fails as a corroborator.

**Option B: the `79 14` gerundive ×2 — CORROBORATES (battery grade).** Exactly two `79 14` bigrams stream-wide (verified by scan):
- 1-based @1365: `…1363:62 1364:94 1365:79 1366:14 1367:60…` (row a7_06)
- 1-based @1690: `…1688:94 1689:79 1690:14 1691:60…` (row a8_05)

Both present the identical immediate frame **`79 14 60` = "tout en [60-V]"** (79="tout", A5 granted; 60=verb class, battery grade). Two natural French readings, both 'en'-frames:
- (R1) Gerundive: "tout en" (adverbial) + [60 as present participle] — "tout en marchant"-shaped.
- (R2) Pronominal: "tout" (neuter pronoun subject, "all") + "en" (clitic) + [60 as finite verb] — "tout en dépend"-shaped.

At both windows 14's only live arm is 'en' (determiner fenced to @117; verb class fenced lane-wide; 'le' killed globally), and neither reading contradicts any standing value. **Stated caveat (not hidden):** 60's exact inflection (participle vs finite) is open — 60's battery profile names verb class only. The corroboration is frame-compatibility at battery grade: two independent rows, same 'en'-shaped trigram, zero contradictions, 'en' the forced reading. This satisfies the bar's "corroborates" at the grade the bar was written for (the core alone carries the zero-assumption standard).

Independence: core is row a4_01; corroborators are rows a7_06 and a8_05 — disjoint windows, no shared cells.

## Per-clause pass/fail

1. **PASS.** Core @622–626 parses as "[76-noun] m'en est [37-pred]" with zero new assumptions (audit above; boundary forced; right edge fenced per claim).
2. **PASS.** The `79 14` ×2 corroborates via the "tout en [60]" 'en'-frame on two independent rows. The @896 leg is recorded as non-corroborating (98-driven, value-independent failure) — it does not contradict 14='en' either.

Adverses: none listed. No standing or red-team verdict contradicted or downgraded; §7 intact (no polyvalence declared; 14='en' is a single value claim).

## Verdict: PROMOTE

The @622–626 core is banked **at battery grade** as a confirmed 'en'-clitic frame for 14: "[76-noun] m'en est [37-pred]", zero new assumptions, independently corroborated by the `79 14` ×2 "tout en [60]" frames.

**Explicitly fenced (NOT promoted):**
- 14='en' GLOBALLY. This banks one frame, not the value — global 14='en' needs the red-team docket (and must survive the `24-en-verb-conflict` ruling where 14's other windows interact with 24).
- The 1-based @626–627 `37 33` hapax (red-team residual joint with `frame-37-reexam`).
- 60's inflection in the corroborating frames (participle vs finite open).
- 76's noun value (class-level lead only); 59='est' stays provisional.

## Load-bearing caveats

- Canonicality: row a4_01's upstream offset (0) is unvalidated; the core is a canonical-offset object. Offset adoption is a red-team act.
- If provisional 59='est' falls, the core needs re-audit (adverse carried forward from the steelman battery).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-core-14-622-bank.md`
- Queue: `core-14-622-bank` → status `verdict`, result `promote`, date 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; 768 targets intact)
- Lock `code/crowd17/next-token/locks/core-14-622-bank.lock` created 2026-10-09T07:28:05Z, deleted on completion (verified gone)
- `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched
