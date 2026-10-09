# Battery verdict: o79-adjudicate

**Target:** `o79-adjudicate` (priority 3)
**Date:** 2026-10-09
**Stream:** repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`), re-derived in-session: 1,847 pairs / 96 types confirmed. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. 1841 diplomatic French throughout.

## Bar (verbatim from battery-queue.json)

> As neighbor values resolve, classify the 5 O-windows into W/S: S-growth strengthens the 79 homophone split, W-growth weakens it.

Numbered clauses:
- C1: classify @496 (`94 02 [79] 88 47`, a2_11) into W/S/O with stated cause.
- C2: classify @883 (`08 31 [79] 68 37`, a5_08) into W/S/O with stated cause.
- C3: classify @1010 (`35 18 [79] 80 78`, a6_02) into W/S/O with stated cause.
- C4: classify @1364 (`62 94 [79] 14 60`, a7_06) into W/S/O with stated cause.
- C5: classify @1688 (`62 94 [79] 14 60`, a8_05) into W/S/O with stated cause.

Adverses: none listed.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/o79-adjudicate.lock` on start. Adopted the homophone-79-split report's partition (W=9 / S=4 / O=5) as the baseline; this battery adjudicates only the 5 O-windows. W = grammatical as independent word 'tout' (conditional-W allowed per the split report's own precedent: @50/@594/@1682 were conditional). S = ungrammatical as word-'tout' in every available function, requiring the syllabic life. O = undecidable under standing values, with the gate stated.

Standing values used (all adopted, none re-litigated): 94="ne" single value (R19-167/168); 47="ce" (A4); 29="er", 40="e", 11="la" (GT); 68="noun" CLASS tier (R19-107, ratified); 35="noun" CLASS tier (R19-050); 88=verb-class (battery promote, RATIFIED R19-156); 80/89 verb-frames (A8); 78="ver" LEAD, word-final (R16-005; inf-37-78-475); 62="il" KILLED at kill grade, no standing value (R19-106); 02 verbal reading KILLED at distributional grade (ne-alone-02-74); 08 letter-tier signature (08-letter-geometry promote); 18 adjective-stem ONLY at the @737 locus, class elsewhere explicitly underdetermined (adv-18-ment).

## Window-level evidence

### @496: `67 78 42 94 02 [79] 88 47 11 29 40` (a2_11) — O-remains (gated)

Byte-confirmed. The available word-'tout' shape is "tout [88-verb]" = object pronoun + verb ("tout dire"-shaped), licensed in principle by ratified 88=verb-class. But the left edge "42 ne [02]" is independently broken: 94="ne" is single-valued, 02's verbal reading was killed (ne-alone-02-74), no 'pas' (30) downstream in the clause, and bare-'ne' is unjustified — so "ne [02]" strands no matter what 79 does. Word order "ne [02-noun] tout [88]" cannot be rescued as word-'tout' (subject/object between ne and verb must be clitic; 02 is not licensed as one), and no positive word-internal evidence forces the S-life either (88's value open; "tout[88]" composition speculative). The window's fate rides on the queued `subj-42-ne-frame` (P2) / 02-class batteries. **O-remains, gated — not a W, not an S.**

### @883: `86 78 17 08 31 [79] 68 37 03 02 00` (a5_08) — W (conditional)

Byte-confirmed. "tout [68-noun]" reads as determiner 'tout' + masculine noun ("tout homme"-shaped) — grammatical as independent word-'tout' under the ratified 68=nominal CLASS grant. The predecessor "[08-letter] [31]" (08 letter-tier per 08-letter-geometry; 31-08 host open) does not block the determiner head reading. **Condition (stated): 68 must be masculine** — determiner 'tout' before a feminine noun would need 'toute'; 68's gender is open. No S-forcing clash exists (unlike @53 "la tout"). **W-conditional: W-growth.**

### @1010: `91 11 52 35 18 [79] 80 78 47 03 24` (a6_02) — W (conditional)

Byte-confirmed. "tout [80]" with 80 under the granted A8 verb-frame reads as object pronoun + verb ("tout dire"-shaped) — grammatical as word-'tout'. 78="ver" word-final sits after 80; the "80 78" bigram is a stream hapax (1×, this window), so no recurrent-word claim is made — the reading needs only 80's verbal frame, which stands. **Condition (stated): 80 must be non-finite (infinitive-shaped) at this window** — object-pronoun "tout" is pre-verbal only before infinitives ("*il tout dit" is ungrammatical in finite clauses); the subject-pronoun alternative ("tout périt"-shaped) would need finite-80, which no grant supplies. 18's class at this window is explicitly underdetermined (adv-18-ment) and does not block. **W-conditional: W-growth.**

### @1364: `35 13 92 62 94 [79] 14 60 03 30 82` (a7_06) — S

Byte-confirmed. "94 79" = "ne tout": with 94="ne" single-valued (R19-167/168), "ne tout" is ungrammatical as word-'tout' in every function: (1) subject pronoun impossible — subject precedes "ne" ("il ne vient"); (2) object pronoun impossible — "tout" as direct object of a finite verb is post-verbal ("je vois tout", "*je ne tout vois"); (3) adverb impossible — 'tout' never modifies a verb directly (the @1419 "on tout [15]" S-precedent); (4) determiner impossible — "ne" admits no "ne tout [noun]" frame. No rescue via 14 (unvalued; 'à'-shaped "tout à fait" rescue unlicensed and "ne tout à fait" is not standard French anyway). **S: S-growth.**

### @1688: `65 13 93 62 94 [79] 14 60 27 46 24` (a8_05) — S

Byte-confirmed. Same "ne tout" failure as @1364, same cause. Distributional note: "94 79" is exactly 2× stream-wide (@1363/@1687, i.e. these two 79s), and "62 94 79 14 60" is exactly 2× (@1362/@1686) — the "ne tout" S-shape is systematic, not a hapax. **S: S-growth.**

## Per-clause results

- **C1 (@496): O-remains** — gated on the 42-94-02 frame (`subj-42-ne-frame` P2 queued); neither W nor S decidable at battery grade.
- **C2 (@883): W** — conditional on 68 masculine (determiner "tout [68-noun]").
- **C3 (@1010): W** — conditional on 80 non-finite/infinitive-shaped ("tout [80]" = "tout dire"-shaped).
- **C4 (@1364): S** — "ne tout" ungrammatical in all word-'tout' functions.
- **C5 (@1688): S** — same, systematic 2-window shape.

## Verdict: PROMOTE (adjudication delivered)

The 5 O-windows adjudicate as **2 W-conditional / 2 S / 1 O-remains**. Net for the split hypothesis: S-growth ×2 (a new systematic "ne tout" S-marker, 2/2 of "94 79" windows) strengthens it; W-growth ×2 (both conditional — on 68's gender and 80's finiteness) weakens it. The O-family shrinks 5 → 1. Combined with the baseline partition, 79's 18 windows now read: W=11 (9 + 2 conditional), S=6 (4 + 2), O=1 (@496). The split hypothesis SURVIVES and gains a second systematic S-shape ("ne tout" alongside "tout fois"), but monovalent word-'tout' still covers 11/18 — **no battery-level declaration is made or warranted; the split stays red-team venue per §7** (67 et/veut sole polyvalence untouched; 79's "tout" A5 grant uncontradicted for the W-family).

Recommended continuations (not required by a promote; noted for the supervisor): `val-68-gender` (firms or kills the @883 W); `fin-80-1010` (firms or kills the @1010 W); `subj-42-ne-frame` (already queued, P2 — unblocks @496).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/o79-adjudicate.lock` created on start (2026-10-09T13:41:54Z), deleted on completion.
- `battery-queue.json`: `o79-adjudicate` → status `verdict`, result `promote`, date 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched. No standing/red-team verdict contradicted or downgraded; canonical-stream caveat stands.
