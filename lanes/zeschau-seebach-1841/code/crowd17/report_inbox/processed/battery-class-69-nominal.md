# Battery report: class-69-nominal

- Target id: `class-69-nominal`
- Claim: "land 69 nominal class beyond the @1836 qui-antecedent leg (12-window census); a landed nominal 69 plus a subject-hood test selects H1 vs H6"
- Date: 2026-10-09
- Worker: battery worker (subagent e173067e-bfeb-4fc5-9fe9-b7e4d4a203a5)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-session, asserts held). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

## Bar (verbatim from battery-queue.json, pre-registered)

"class named with >=2 frame-legs at battery grade"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** At least two independent windows on the repaired stream where 69 fills a licensed nominal slot under standing values (byte-exact offsets).
2. **C2:** No window forces a non-nominal role for 69 under standing values.

Verdict rule: promote iff C1 and C2 pass; kill iff a window forces 69 non-nominal (or a licensed nominal frame is shown impossible); null otherwise.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/class-69-nominal.lock` on start (agent id + 2026-10-09T10:51:00Z); deleted on completion.
2. Re-derived the stream in-session; confirmed n(69)=12 (0-based): @67, @177, @405, @805, @933, @1115, @1259, @1266, @1380, @1413, @1627, @1835.
3. Checked the standing record first (adopted, never re-litigated): `cela-69-11-word` (locus-level PROMOTE: "69 11" @1115-1116 = "cela", one word; global 69 value explicitly left open) and `ce69-global` (PROMOTE finding grade: 69='ce' survives all 12 windows; global promotion is a red-team act). This battery tests CLASS (nominal), not value ('ce') — a strictly weaker claim, consistent with both.

Standing values used: pencil 11=la, 29=er, 46=que, 34=i; granted 64=qui, 84=on; battery-promoted 94=ne (pending ratification); R18 subset-scoped 92=verb. No other values assumed.

## Window-level evidence (0-based @, byte-exact)

Full census (±3 context): @67: `12 94 92 69 13 24 56` · @177: `87 86 21 69 14 24 87` · @405: `88 53 34 69 26 00 33` · @805: `62 98 53 69 24 24 41` · @933: `98 83 56 69 26 00 33` · @1115: `65 38 30 69 11 88 70` · @1259: `61 31 29 69 88 01 09` · @1266: `11 50 46 69 88 24 30` · @1380: `89 84 92 69 13 24 65` · @1413: `42 16 97 69 74 34 52` · @1627: `33 46 56 69 26 00 33` · @1835: `16 59 36 69 64 22 42`.

### Clean nominal frame-legs

**F1 — @1835 (1b@1836), row a8_11:** `59 36 | 69 64 22` = "…[36] [69] qui(64) [22]". 69 is the antecedent of the relative pronoun "qui" (64 granted). A relative pronoun's antecedent is a nominal by grammatical necessity (French has no verbal relative-antecedent). This is the standing qui-antecedent leg named in the claim.

**F2 — @1115 (1b@1116), row a6_07:** `38 30 | 69 11 | 88 …` = "…[38] pas(30) [cela] [88]…". "69 11" parses as the one-word demonstrative pronoun "cela" (locus-level PROMOTE, adopted; 11=la pencil; two-word "ce la" is ungrammatical). A demonstrative pronoun is nominal by definition. This leg is beyond the qui leg.

**F3 — @67 (1b@68), row a1_01:** `94 92 69 13 24` = "ne(94) [92-verb] [69] [13] [24]". 94=ne (battery-promoted), 92=verb (R18 subset-scoped). Post-verbal slot after a finite/modal verb: the direct-object slot, which French reserves for nominals. 69 fills the object-pronoun position ("…[verb] ce [13] [24]…"). Nominal leg, independent window and row from F1/F2.

**F4 — @1380 (1b@1381), row a7_06:** `84 92 69 13 24` = "on(84) [92-verb] [69] [13] [24]". Byte-identical object-pronoun frame to F3 with a different left context ("on" instead of "ne"), independent row. Nominal leg.

**F5 — @1259 (1b@1260), row a7_02:** `31 29 69 88 01` = "[31]er [69] [88] [01]". 29='er' is pencil ground truth, so "31 29" is an infinitive "[31]er". 69 fills the direct-object slot of that infinitive ("…[inf] ce [88]…"); French object slots are nominal-only. A verbal 69 would need licensed government of a bare stem, and 69 is followed by 88 (not 29='er'), so no verbal reading is available. Nominal leg.

### Windows not counted as clean legs (stated cause)

- **@177:** "21-noun [69] en(14)" needs the licensed contraction/dissolution move ("c'en"); not battery-grade clean.
- **@805:** "98 … ce(69) [24]" pronoun-face is conditional on 24=finite/modal; the live red-team docket `24-en-verb-conflict` could re-parse it. Compatible (69 stays nominal under the 24='en' arm too), but not a clean leg.
- **@1413:** "16 97 [69] 74 34" — 74 is class-open; "ce [74]" is nominal-face either way, but 74's class is load-bearing, so the leg is conditional.
- **@405 / @933 / @1627:** "ce [26]" determiner frames — nominal-face, but 26's noun status is lead-grade, not landed; conditional.
- **@1266:** "que(46) ce(69) [88] [24]" — "que ce [verb]" is grammatical, but 88's finiteness at this exact window is unproven; compatible, not a clean leg.

## Per-clause pass/fail

1. **C1: PASS.** Five independent clean nominal frame-legs (F1–F5), four of them beyond the @1836 qui-antecedent leg; the bar needs >=2.
2. **C2: PASS.** No window forces a non-nominal role: @67/@1380 object pronoun; @177/@405/@933/@1627/@1835 nominal-face; @805 nominal under both 24 arms; @1115 one-word pronoun; @1259/@1266 object/subject pronoun; @1413 nominal-face. Zero forced non-nominal windows.

No adverses listed. No standing verdict contradicted or downgraded: consistent with `cela-69-11-word` (locus) and `ce69-global` (value 'ce' implies nominal); §7 intact — no polyvalence declared, and the class claim is strictly weaker than the pending value promote. Canonical-stream caveat stands: rows a1_01/a6_07/a7_02/a7_06/a8_11 offsets unvalidated.

## Verdict: PROMOTE (class-level)

69 is **nominal** at battery grade (5 clean frame-legs, no forced non-nominal window). 69's VALUE stays open — this battery does not promote 69='ce' (that remains the red team's act per `ce69-global`).

## Supervisor observations (not queued targets — promote regenerates none per §4)

- The nominal-69 finding plus a subject-hood test for 69 is the downstream discriminator for the H1/H6 question named in the claim; no new target is proposed here since `val-69...` batteries already exist in the queue.
- The @177 "c'en" dissolution caveat and the @805 24-conditional remain the two windows where 69's nominal face is least clean; a future battery could harden them.

## Bookkeeping

- `battery-queue.json`: `class-69-nominal` queued → verdict/promote (temp-file + rename, own entry only, pre-write assert confirmed no prior verdict, JSON re-validated).
- Lock created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
