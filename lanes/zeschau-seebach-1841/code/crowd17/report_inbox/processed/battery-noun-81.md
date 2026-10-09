# Battery verdict: noun-81

## Bar (verbatim, pre-registered)

"promote iff noun frames parse + 'pour [INF]' complement holds"

Restated as numbered clauses:
- **C1:** Noun frames parse — 81 appears in determiner+noun frames that parse grammatically under standing values.
- **C2:** The 'pour [INF]' complement holds — 81 takes "pour" + infinitive complements ("81 00 [INF]") under 00='pour' (A9-granted).
- **Adverse:** 81='prin' KILLED — fresh value needed; the 'prin' value is not re-litigated.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/noun-81.lock` on start (agent id + UTC timestamp). Re-derived the full stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py` (1,847 pairs / 96 types verified). `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched. Offsets below are 1-based (0-based index + 1), matching lane convention.

## Census

81 n=14. Predecessors: 55 x6, 77 x4, 43, 98, 39, 08 (each x1). Followers: 00 x3, 97 x2, 87 x2, 30, 85, 06, 88, 03, 82, 92 (each x1).

All 14 windows (1-based @, row, ±4 context):

| @ | row | context |
|---|---|---|
| 27 | a1_00 | 29 47 33 **55 81 00** 34 24 30 |
| 45 | a1_01 | 01 24 88 **43 81 30** 62 96 00 |
| 94 | a1_02 | 98 19 41 **98 81 97** 46 29 85 |
| 525 | a3_00 | 91 77 06 **55 81 97** 47 44 59 |
| 552 | a3_01 | 24 47 46 **55 81 00 86** 59 34 |
| 746 | a5_02 | 20 30 67 **77 81 85** 28 00 64 |
| 1087 | a6_05 | 89 24 02 **55 81 00 33** 79 80 |
| 1096 | a6_06 | 06 43 07 **55 81 06 29** 67 86 |
| 1242 | a7_01 | 03 40 67 **77 81 87** 11 00 33 |
| 1403 | a7_07 | 48 40 67 **77 81 87** 11 00 11 |
| 1514 | a7_11 | 12 61 59 **39 81 88** 11 31 11 |
| 1594 | a8_02 | 48 29 47 **08 81 03** 29 80 67 |
| 1600 | a8_02 | 29 80 67 **77 81 82** 98 00 44 |
| 1673 | a8_05 | 91 11 78 **55 81 92** 60 03 39 |

## C1: Noun frames — PASS

The trigram "67 77 81" occurs **4x** stream-wide (@746, @1242, @1403, @1600), and "77 81" occurs exactly 4x (all inside the trigram). Under 77='le' (provisional, standing state), these are determiner+noun frames:

- **@1242** (a7_01): "67 77 81 87 11" = "[67] le [81] ce(87) la(11)". "le [81]" + "cela" ("87 11" = "ce"+"la"). Clean nominal: "the [81], that...". ✓
- **@1403** (a7_07): "67 77 81 87 11" = byte-parallel to @1242 ("48 40 67" left vs "03 40 67"). "le [81] cela". Clean nominal. ✓
- **@1600** (a8_02): "67 77 81 82 98" = "[67] le [81] m'(82) [98-verb]". "le [81]" then clause boundary before "me [98]". Clean nominal: "the [81]; [it] [98]s to me...". ✓
- **@746** (a5_02): "67 77 81 85 28" = "[67] le [81] [85-verb-stem] [28]". "le [81]" is clean, but "[85-stem]" (A3-granted verb stem) directly follows with 28 open — no relative "qui", no boundary byte-evidenced. FENCED (see residuals), does not overturn the three clean frames.

Three of four "le [81]" frames parse cleanly as masculine-singular determiner + noun. "le" is masculine; 81 is masculine under this frame. The frame repeats with byte-parallel left context (@1242/@1403 share "40 67"), so this is not a one-window accident.

## C2: 'pour [INF]' complement — PASS

"81 00" occurs **3x** (@27, @552, @1087). 00='pour' is A9-granted. Lane convention (cf. battery-prof-98: "83 86" = "de [86-inf]") treats a bare verb-stem after a preposition as infinitive-shaped.

- **@1087** (a6_05): "55 81 00 33 79 80" = "[55] [81] pour [33-stem] tout(79) [80-verb]". 33 is verb-stem-shaped (stem-class-split census: 33 x5 stem cells; 33+29 = infinitive per A10). "pour [33-inf] tout" = "in order to [33] everything" — grammatical purpose clause ("pour croire tout"-shaped). The infinitive takes "tout" as object, then [80] verb-frame follows. ✓
- **@552** (a3_01): "55 81 00 86 59 34" = "[55] [81] pour [86-stem] est(59) [34]". 86 is verb-stem-shaped (86-29 x4). "pour [86-inf]" = purpose infinitive; "est" (59 provisional) opens a new clause after it. ✓
- **@27** (a1_00): "55 81 00 34 24" = "[55] [81] pour i(34) [24=faire]". 34='i' is a banked letter (GT), not infinitive-shaped. "pour i" does not complete. FENCED (see residuals).

Two of three "81 pour" windows take infinitive-shaped verbal complements. "pour + infinitive" purpose complements are the diagnostic for abstract nouns of the "moyen / ordre / droit / besoin" family (masculine abstract nouns taking purpose clauses). Combined with the masculine "le [81]" frames, the class claim "masculine abstract noun" is supported at class level. No value is named.

## Adverse: 81='prin' — ANSWERED

81="prin" is kill-grade dead per standing state (protocol §7 kills list; cited in battery-adj-groundwork-refollower §7). It is not re-litigated here. No value for 81 is named or proposed; this verdict is class-level only ("masculine abstract noun", value open).

## Fenced residuals (not kill-grade)

- **@1096** (a6_06): "55 81 06 29" — "81 06" reads as stem + "ent" (06='ent' promoted, R17-007) = 3pl verbal ("[81]ent"), followed by 29='er'. No grammatical noun-81 parse available. Counter-readings ("presenter" via 81="s" letter; "[55-81]ent" 3pl verb) require ungranted letter/stem values. FENCED as the strongest anti-noun window; flagged as a §7 polyvalence candidate for the red team (poly-81 question, not declared here per §7).
- **@94** (a1_02): "98 81 97" — under 98='vient' (battery-promoted, lead-level, pending ratification), "vient [81-noun]" is ungrammatical (bare noun after "venir"). FENCED as conditional on 98's value; if 98 is re-valued, this window re-opens.
- **@746** (a5_02): "77 81 85 28" — "le [81]" clean, but "[85-stem] [28]" follows with no relative or boundary. 85 is verb-stem (A3), 28 open. FENCED with cause (open neighbors).
- **@27** right edge (a1_00): "81 00 34" — "pour i" incomplete (34='i' letter). FENCED; the "55 81 00" pour-pattern matches @552/@1087 but the infinitive is absent here.
- **@45** (a1_01): "43 81 30" — 43's value/class open (noun-43 killed; verb-stem lead). Cannot adjudicate "[43] [81-noun] pas". FENCED on open 43.
- **@525** (a3_00): "55 81 97 47" — 55 and 97 open. Neutral; consistent with nominal 81, not probative.
- **@1514** (a7_11): "39 81 88 11" — 39's value open (39=/a/ at @762 per battery-a-39, not globally granted). If 39='à', "à [81-noun]" parses. Neutral.
- **@1594** (a8_02): "08 81 03 29" — 08 open. "[08] [81]" could be determiner+noun; "[03]er" infinitive follows. Neutral.
- **@1673** (a8_05): "55 81 92 60" — 55/92/60 open. Neutral.

The "55 81" collocation (x6: @27, @525, @552, @1087, @1096, @1673) is noted; 55's value is open, so it neither supports nor contradicts the noun reading. It is not double-counted as a noun frame.

## Standing-state check

No red-team verdict on 81's class exists. The 81="prin" kill (§7) is untouched. battery-88-1727-shape, battery-ver-78-rebar, and battery-importe-30-subject-sweep cite 81 only as "value open" — nothing contradicted or downgraded. No polyvalence declared (§7 intact); the @1096 polyvalence candidate is escalated, not declared.

## Verdict: PROMOTE (class-level)

81 = **masculine abstract noun** (class-level; value open; battery grade, needs red-team ratification).

- C1 PASS: "le [81]" x3 clean (@1242, @1403, @1600), inside the repeated "67 77 81" x4 frame; masculine via "le" (77 provisional).
- C2 PASS: "81 pour [INF]" x2 (@552 "pour [86-inf]", @1087 "pour [33-inf]"); the purpose-complement diagnostic for abstract nouns.
- Adverse answered: 81='prin' kill stands, not re-litigated; no value named.
- Residuals fenced with stated cause; @1096 escalated as §7 candidate.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-noun-81.md` (this file).
- Queue: `battery-queue.json` `noun-81` → status `verdict`, result `promote`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated post-write).
- Lock: `locks/noun-81.lock` created on start, deleted on completion.
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched; all counts re-derived on the repaired 1,847-pair stream.
