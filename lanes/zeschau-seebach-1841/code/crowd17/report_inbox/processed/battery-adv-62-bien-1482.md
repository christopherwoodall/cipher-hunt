# Battery report: adv-62-bien-1482 — test 62='bien' (adverb)

**Target:** `adv-62-bien-1482` (P2)
**Date:** 2026-10-09
**Verdict:** KILL (62='bien' as adverb dies at kill grade)

## Bar (verbatim from queue)

"all 25 parse under adverb-with-'bien', or the 'bien' value dies at kill grade"

## Bar restated as numbered clauses

1. All 25 non-94, non-@46 windows of 62 parse with 62='bien' as an independent adverb under standing values.
2. If any window forces non-'bien' at kill grade, the 'bien' value dies at kill grade.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/adv-62-bien-1482.lock` on start (deleted on completion). Re-derived the full stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (byte-exact tokenizer per `repair_parse.py`); 1,847 pairs confirmed; `canonical.py` never used. n(62)=35 confirmed; 9 follower-94 windows excluded and the @46 window ("30 62 96 00", 0-based @46) excluded per the parent battery's scope → 25 target windows, matching class-62-25's census exactly. R5005, sealed gates, red-team queue untouched.

Value key: pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted/promoted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce, 06=ent, 48=inflectional-'e', 98=finite-verb class, 92=verb class subset-scoped); provisional (59=est, 77=le); battery leads used only where stated (98="vient"). 1841 diplomatic French only.

French "bien" as independent adverb licenses: (a) postverbal manner ("parle bien"); (b) intensifier before a gradable word ("bien grand", "bien des gens"); (c) concessive conjunction "bien que" + subjunctive; (d) fixed preverbal idioms ("bien vouloir", "bien faire"). Preverbal "bien" before an ordinary finite verb is ungrammatical.

## Window-level evidence (0-based @-offsets, repaired stream)

### Kill-grade failures (14 windows — no independent-adverb-'bien' parse exists)

**The five "bien + finite verb" windows — preverbal "bien" ungrammatical (98's finite-verb class is promoted):**
- **@11** (a1_00): `93 62 98` = "93 bien vient". "bien" immediately before finite "vient". No idiom licenses "bien venir"; no "que" for the concessive; intensifier needs a gradable word. **Kill.**
- **@802** (a5_05): `74 62 98` = "74 bien vient". Same. **Kill.**
- **@945** (a5_10): `08 62 98` = "08 bien vient". Same. **Kill.**
- **@1136** (a6_08): `20 62 98` = "20 bien vient". Same. **Kill.**
- **@1324** (a7_04): `08 62 98` = "08 bien vient". Same. **Kill.**

**The six "bien e" windows — "e" (48, promoted inflectional-'e') is not a French word and not gradable:**
- **@360** (a2_06): `11 21 62 48 76` = "la 21-noun bien e 76". Manner needs a verb (21=noun, ratified); intensifier "bien e" impossible; "biene" is not a French word. **Kill.**
- **@425** (a2_09): `47 14 62 48 76` = "ce 14 bien e 76". 14 is determiner/clitic-class; no verb for manner, no gradable word for intensifier. **Kill.**
- **@1315** (a7_04): `36 74 62 48 98` = "36 74 bien e vient". 74≠verb (verb-74 dead by adoption of ne-alone-02-74 KILL); "bien e" impossible. **Kill.**
- **@1349** (a7_05): `73 34 62 48 77` = "73 i bien e le". "i" is the banked letter; no verb, no gradable word. **Kill.**
- **@1464** (a7_09): `01 21 62 48 21` = "01 21-noun bien e 21". Same family. **Kill.**
- **@1569** (a8_01): `24 74 62 48 56` = "24 74 bien e 56". 74≠verb. **Kill.**

**The two "bien ent" windows — "ent" (06, promoted verbal ending) is not a word:**
- **@665** (a4_02): `80 03 62 06 00` = "80 03 bien ent pour". "bienent" is not a French word; manner "bien" cannot split a stem from its ending ("03 bien ent" ≠ "[03-ent] bien"). **Kill.**
- **@1536** (a8_00): `73 41 62 06 21` = "73 41 bien ent 21". Same. **Kill.**

**One more:**
- **@849** (a5_06): `96 40 62 21 67` = "par e bien 21-noun et". Preceding "e" (40, letter) is not a verb; intensifier "bien 21" without "des" before a noun is ungrammatical. **Kill.**

### Passes (2 windows)
- **@1454** (a7_09): `46 92 62 61 21` = "que [92-verb] bien 61 21". Postverbal manner adverb after verb-class 92 (R18 subset-scoped): "que [verb] bien" is grammatical ("qu'il parle bien"). **PASS.**
- **@1482** (a7_10): `16 98 62 46 77 84 24` = "16 vient bien que l'on 24". The concessive rescue parses: "bien que" + "l'on" (77="le" provisional + 84="on" granted A15, elided) + finite 24 (promoted finite-modal). "[16] vient, bien que l'on [24]..." is grammatical 1841 French. **PASS, conditional** on 77="le", 84="on", and 24≠'en' (live red-team docket `24-en-verb-conflict`).

### Fenced (9 windows — open neighbor values, no forcing evidence either way)
- @82: "vient 51 bien 16" (51/16 open). @389: "36-noun bien 91 on" (91 open; manner dead on ratified 36=noun, intensifier conditional). @446: "10 bien 61" (10/61 open). @658: "03 bien 16" (03 conditioned, 16 open). @1065: "par 21-noun bien 18" (18 open). @1141: "vient ver bien 16" (16 open). @1297: "80 04 bien 16" (16 open). @1468: "02 bien 38-verbform" (02 open; preverbal manner ungrammatical, intensifier needs gradable 02). @1539: "ent 21-noun bien 93" (93 open).

## Per-clause pass/fail

1. All 25 parse under adverb-with-'bien': **FAIL** — 14 windows force non-'bien' at kill grade (five "bien + finite verb", six "bien e", two "bien ent", one "par e bien noun").
2. Kill disjunct: **FIRES** — the 'bien' value dies at kill grade.

Adverses: none listed. No standing or red-team verdict contradicted or downgraded — 62's value was open; `redteam-62-conditioned` remains the venue for the conditioned-split hypothesis; `compound-62-vient` (already queued) is the live alternative for the "62 98" family. §7 intact.

## Verdict: KILL

62='bien' (adverb) is killed at kill grade. The concessive rescue at @1482 is real (conditional pass) and @1454 parses as manner adverb, but the bar requires all 25: fourteen windows admit no independent-adverb-'bien' parse under standing values. This kills the VALUE 'bien', not the adverb class in general, and does not touch the conditioned-split / word-internal hypotheses for 62 (red-team venue).

## Caveats (stated, not hidden)

- All rows carry unvalidated upstream offsets (canonicality caveat); verdict holds on the canonical stream per protocol.
- The five "bien vient" kills rest on 98's promoted finite-verb class (not on the "vient" lead): preverbal "bien" before any ordinary finite verb is ungrammatical outside fixed idioms.
- @1482's concessive pass is conditional on provisional 77="le", granted 84="on", and the live `24-en-verb-conflict` docket resolving 24 as finite/modal.
- @46 ("30 62 96 00") was out of scope (parent-bar exclusion, fenced as segmentation-open); not re-litigated.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/adv-62-bien-1482.lock` created 2026-10-09T07:28:05Z, deleted on completion.
- `battery-queue.json`: `adv-62-bien-1482` queued → verdict/kill (temp-file + rename; pre-write assert confirmed no prior verdict; own entry only; JSON re-validated).
- R5005, sealed gates, red-team adjudication queue untouched. `canonical.py` never used.
- Kill verdict — no follow-ups required (nulls regenerate; kills close). Natural next venues already exist: `compound-62-vient` (queued), `redteam-62-conditioned` (red-team docket).
