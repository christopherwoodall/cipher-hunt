# Round-16 battery: i (34) — compositional frames, new adverses

Finder report: `code/crowd16/report_inbox/next-token-findings-i.md` (ingested 2026-10-07).
Status entering: 34="i" BANKED (pencil GT). 64="qui" PROMOTED. 79="tout"
BANKED. 00="pour" BANKED.

---

## PRE-REGISTRATION (locked before formal tests)

**Bar I1 (P1 "la première" ×2):** CONFIRM iff 11-70-82-34-29-40 re-derives
byte-identical ×2 (@754/@1034). The 20-constraint (feminine singular noun
after "la première") feeds the 20 battery; 82-34 exclusivity and the
zero masculine-"premier" are checked.

**Bar I2 (P2 "-quière" ×2):** LEAD-grade iff 9-64-29-40 @291 and 92-64-29-40
@685 re-derive exact (64="qui" word-internal, two independent stems). The
"pour"+subjunctive left-context is CONFRONTED, not buried: if 00 precedes
in both windows, they are new adverses for 00="pour" (fenced, handed to the
pour/split battery).

**Bar I3 (P3 "tout entière"):** supports 79="tout" (adverbial) iff the
window re-derives; stem 85-1="enti" is single-leg LEAD.

**Bar I5 (73="lu"):** LEAD iff 73-34 ×2 re-derive exact in "lui"-shaped
frames.

**Bar I6 (nulls):** held as stated; @1415's 32 left-context fed to the
adjective battery.

---

## TESTS

`t = code/crowd16/next-token/test_i.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | n34 = 11; starts = [28,61,393,404,555,757,1037,1348,1415,1741,1749] | |
| 2 | 11-70-82-34-29-40 ×2 @754/@1034 byte-identical | |
| 3 | 82-34 = [756,1036] (only ×2) | |
| 4 | 70-82-34-29 = [755,1035]; no 70-82-34-29 without 40 | |
| 5 | @291: P[287:297] = [0,97,9,64,29,40,65,16,1,11] | |
| 6 | @685: P[681:691] = [7,0,92,64,29,40,65,94,29,60] | |
| 7 | @595: P[591:600] = [9,0,92,79,85,1,29,40,3] | |
| 8 | @61: P[59:66] = [41,8,34,29,40,12,94] | |
| 9 | 73-34 = [393,1348]; @393 P[391:398]; @1348 P[1346:1353] | |
| 10 | 29-40 = 9; stems {34:3,64:2,11:1,1:1,88:1,6:1} | |
| 11 | @28: P[24:34]; @555: P[553:560]; @1415: P[1413:1420] | |
| 12 | @307: P[305:312] = [2,88,20,17,46] ("[20] fois") | |

---

## VERDICT

**I1 "la première" ×2 — CONFIRM.** 11-70-82-34-29-40 byte-identical @754/
@1034 re-derived; tails 20 (@760) / 17="fois" (@1040) confirmed. 82-34
("mi") occurs ONLY in these two windows ([756,1036]); 70-82-34-29 without
40 ("premier" masc.) occurs 0×. Two-leg "première" is now a fixed anchor.
**20-constraint:** "la première [20]" forces 20 = feminine singular noun
(or noun-phrase head) — any 20-value ungrammatical there dies. Fed to the
20 battery (with the pour beat's @667 "pour [20]" leg — the feminine-noun
side now has 3 legs: @667, @760, and the la-beat's P7-adjacent @667... no:
@667, @760, plus formula-tails T4's @760 — two distinct: @667 and @760).

**I2 "-quière" ×2 — LEAD, plus 2 NEW adverses for 00="pour".**
9-64-29-40 @291 ("acquière"-shaped) and 92-64-29-40 @685 ("requière"-shaped)
re-derived exact — 64="qui" compositional inside the verb, two independent
stems, same subjunctive frame. LEAD (not a value claim for 64 — already
promoted; the lead is the "-quière" frame for the verb battery).
**The flagged adverse is REAL and fenced:** @291 = [0,97,9,64,29,40,…]
("pour [97] acquière") and @685 = [7,0,92,64,29,40,…] ("pour [92]
requière") — "pour"+subjunctive is ungrammatical under 00="pour" in both
windows. These are **2 new fenced adverses for 00="pour"** (docket now:
@1247 strong, @864 fenced, @291/@685 fenced, rate moderate). Handed to the
pour/split battery. They do not kill 00 (50/55 clean) but the pattern —
"pour" before subjunctive-shaped verbs — is now 3 windows (@291/@685 plus
the @106 fork-conditional).

**I3 "tout entière" @595 — supports 79="tout".** [9,0,92,79,85,1,29,40,3] =
"pour [92], tout entière [3]…" — adverbial "tout" (invariable) + "entière",
grammatical and natural. New compositional leg for banked 79="tout"
(5th leg family). Stem 85-1="enti": 85-1 ×2 (@595/@1439) — LEAD for the
stem; the word isn't doubled. [3] after "tout entière" queued ("à"/"dans"-
shaped?).

**I5 73="lu" — LEAD.** 73-34 ×2 @392/@1347 (bigram starts; 34-cells
@393/@1348): "[84] lui [67] qui tout" and "[66] lui [62] le" — "lui" ×2,
both before verb-ish groups, best French fit for standalone [X]i. The
finder's self-correction (@404 = 53-34, not 73-34) verified and kept.

**I6 nulls — held.** @28 "[0]i en" ("bien"/"rien"-shaped vs 00="pour?" —
boundary "0|34" or 00-hit; null, flagged). @555 "est-i-fois" unparsed
(explicit null, not forced). @1415 "[74]i [52] 32" — 32's THIRD
left-context ([52], joining "qui est 32" and "qui 32") fed to the adjective
battery. @1741/@1749 orphans held.

**20's paradox — now one-sided (CONFIRM).** The feminine-noun window (@760)
is rock-solid (3rd leg via @667 "pour [20]"); the "[20] fois" window (@309:
[20,17]="…[20] fois") is the side needing re-examination — "20=fois" is
killed, so "[20] fois" must be "[noun] fois" or a mis-segmentation, not
"fois fois".

**Queued:** 20-as-feminine-noun filter; 9/92 stem battery + subjunctive-
trigger sweep (@291/@685 left context); 85/1 "enti" battery + [3]
identification; 8-stem battery ("[8]ière" @61); 73 "lu" battery; 32 third
left-context to the adjective battery.
