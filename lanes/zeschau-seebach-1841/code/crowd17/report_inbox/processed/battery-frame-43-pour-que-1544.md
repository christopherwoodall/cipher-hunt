# Battery verdict: frame-43-pour-que-1544

Target: `frame-43-pour-que-1544` — "78-43-pour-que-pre-n-ne (@1544-1549) is the pour que discriminator for noun-43: name 43 or kill the queued candidates".
Worker: 06af1cea-7de1-459b-aeb1-35440702cbf9. Date: 2026-10-09.
Lock: created `code/crowd17/next-token/locks/frame-43-pour-que-1544.lock` on start (no prior lock, no stale-lock note needed).

## Bar (verbatim from battery-queue.json, pre-registered before testing)

> "resolve iff (a) 43 is named (from {suite, condition, maniere, mesure} or new) with X pour que [subjunctive] parsing; (b) 78's slot is stated (verb like faire? determiner?); (c) the parse is consistent with the prenne battery's finding (subject slot empty, 92 nominal - battery-prenne-70-12-94, null)"

Numbered clauses:
1. (a) 43 is named — from {suite, condition, maniere, mesure} or a new value — with a grammatical "X pour que [subjunctive]" parse in 1841 diplomatic French.
2. (b) 78's slot at @1543 is stated: verb-shaped (like "faire X pour que") or determiner-headed.
3. (c) The parse is consistent with the prenne battery's finding: subject slot empty, 92 nominal (battery-prenne-70-12-94, null).

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`; 1,847 pairs / 96 types re-verified in-session). Never `canonical.py`. R5005, sealed gates, red-team adjudication queue untouched. No data invented. @-offsets are 0-based pair positions (this battery family's convention).

**Anchor correction (noted before testing):** the claim's "@1544-1549" is off by one at both ends. On the repaired stream the 7-cell is:

`@1543 78 | @1544 43 | @1545 00 | @1546 46 | @1547 70 | @1548 12 | @1549 94 | @1550 92 (a8_00)`

i.e. "78-43-pour-que-pre-n-ne" spans **@1543..1549**, with 43=@1544 (not 78). All @-references below use this corrected anchor.

## Window-level evidence

### The target window — @1543-1550 (row a8_00)

`62 06 21 62 93 88 [77 78 43] 00 46 70 12 94 92 45 23` (@1536-1552)
= "... il ?ent 21 il [93] 88 [le] [78] [43] pour que pre-n-ne [92] ce [23] ..."
- 00='pour' (A9 grant) + 46='que' (banked pencil GT) = "pour que"; 70+12+94 = "prenne" (subjunctive, compositional on 12='n'/94='ne', battery-promoted).
- Subject slot between 'que'(@1546) and the verb(@1547): EMPTY (adjacent positions; 70 word-internal).
- The frame is the ONLY "43 pour que" window stream-wide: "43->00" occurs x3 (@244, @1126, @1544) but only @1544 continues with 46='que' (others: @244 '43 00 66 91...', @1126 '43 00 86 52...'). Closed-set verified.

### The four "pour que" (00-46) windows stream-wide

| window | row | left context | slot after 46 |
|---|---|---|---|
| @106 | a1_03 | `... 59 45 28` (28 unknown) | 11='la' -> overt nominal subject |
| @545 | a3_01 | `... 48 42 06` (06 'ent' lead) | 24 (class open, slot occupied) |
| @1545 | a8_00 | `... 77 78 43` (THE TARGET) | 70 word-internal -> EMPTY, anomalous |
| @1680 | a8_05 | `... 74 77 44` (44 unknown) | 79='tout' -> overt subject |

Independently matches the prenne-subject-S1545 census (2 clean overt subjects; @106 'pour que la [21]', @1680 'pour que tout [65]'). **No "pour que" window stream-wide is noun-governed**: all three sibling windows have non-nominal left contexts (unknown 28, verb-ending 06, unknown 44).

### 78's slot (clause b) — full census, n=31

- Predecessors: {77: 7, 47: 5, 37: 4, 67: 4, 11: 2, 87: 2, others x1}. 19/31 (61%) are determiner-shaped (77 x7, 47 x5, 11 x2, 87 x2).
- "77-78" x7, followers in that frame: {18, 06, 52, 64, 94 x2, 43} — including @1181/@1352 "77 78 94 82 06" ('le [78] ne m/ent...'), i.e. 78 subject-capable before 94='ne'.
- At @1543: "77 78 43" = [le] [78] [43] — a determiner-headed nominal slot.
- ver-78 verdict (2026-10-08, NULL, red-team R16-005): 78='ver' graded LEAD (correctly, not settled); 3/7 positive ver-word reads in "ce [78]" x7, zero verb-shaped readings ever recorded for 78.
- A "faire"-like verb reading would require an infinitive in this slot, but 78 is ver-shaped by shape and never verb-shaped in contact; "faire" is also incompatible with the ver-78 LEAD. Excluded.

### Adopted (not re-litigated, protocol §5 — never downgrade an existing verdict)

- battery-noun-43-discriminator (KILL, 2026-10-08): 43='suite' and 43='manière' KILLED; discriminator positive set = {condition, mesure}.
- battery-cond-mesure-43full (NULL, survivor set EMPTY, 2026-10-09): 'condition' and 'mesure' both fail par-43 x2 (0-based @343, @1027: byte-identical "45 64 96 [43] 87 01" = "ce qui par [43] ce [01]") and @21 (word-internal segmentation, battery-43-29-segment PROMOTE) at kill grade.
- battery-par43-adverbial-attestation (PROMOTE on negative arm, 2026-10-09): bare "par mesure"/"par condition" unattested as 1841 adverbials (Littré + TLF dictionary bar); par-43 kill terminal pending only the @21 polyvalence ruling (red-team docket).
- battery-noun-43 (NULL, 2026-10-09): discriminator positive set exhausted at the lexical level; extended candidates (façon, raison, fin, cause, intention, précaution, disposition) all die on independent windows; @21 kills every monovalent noun at kill grade.
- battery-prenne-70-12-94 (NULL, 2026-10-08): subject slot empty at @1547-1549, 92 nominal ('la 92' x3, '92 qui' x2); 12/94 duality fenced for red team.
- battery-prenne-subject-S1545 (PROMOTE, 2026-10-08): the "pour que ... prenne" clause @1545 CONFIRMED genuinely subjectless with stated cause; controls show the slot is normally filled (@106, @1680), so the emptiness is a genuine anomaly, not a cipher convention.
- pour-que-lexicon-close: already queued (P3) — not duplicated.

## Per-clause verdicts

1. **Clause (a) — 43 named: FAIL.** The discriminator's positive set within French feminine nouns is {condition, mesure} (noun-43 §4: façon/manière/raison/fin/cause/intention/précaution/disposition all fail the "N pour que [subj]" government or independent windows). Both members are dead at battery level: kill-grade on par-43 x2 + @21 (cond-mesure-43full), terminal corpus closure (par43-adverbial-attestation). The remaining candidates (suite, manière) were killed earlier. No value — old or new — can be named with "X pour que [subjunctive]" parsing at battery grade.
2. **Clause (b) — 78's slot: ANSWERED (determiner-headed, not verb-like).** "77 78 43" = determiner + [78] + [43]; 19/31 of 78's predecessors are determiner-shaped; ver-78 LEAD bounds 78 to ver-words (never a verb); "faire"-like reading excluded by shape. 78's slot is nominal.
3. **Clause (c) — consistent with prenne battery: CONSISTENT.** Subject slot empty + 92 nominal confirmed (prenne battery; strengthened by prenne-subject-S1545's PROMOTE on the subjectless reading). Under the government reading, "X pour que ∅ prenne" is ungrammatical 1840s French regardless of 43's value — consistent with, not contradictory to, the fenced null.

## Adverses

1. **"pour que after a bare noun is unidiomatic for all four queued candidates"** — CONFIRMED and sharpened. It is not merely unidiomatic for the four candidates: the discriminator's full positive set is {condition, mesure}, and both are dead at kill grade on independent windows (par-43 x2 @343/@1027, @21). The sibling "pour que" census strengthens this: no "pour que" window stream-wide is noun-governed (@106 left=28, @545 left=06, @1680 left=44 — never a bare noun). The government reading has zero constructional support stream-wide.
2. **"prenne battery found no licensable subject"** — CONFIRMED and strengthened. battery-prenne-subject-S1545 (PROMOTE) confirmed the clause genuinely subjectless with stated cause; the sibling controls (@106 'pour que la [21]', @1680 'pour que tout [65]') show the subject slot is normally filled, making @1545's emptiness a genuine anomaly. Not ignored.
3. **"78's value open (ver-78 queued)"** — ANSWERED with status. ver-78 returned NULL (2026-10-08), graded LEAD under red-team R16-005 (not granted, not settled); 78's value remains open but is bounded to ver-words. The slot answer in clause (b) does not depend on the value: determiner-headed nominal holds under any ver-shaped value, and the "verb like faire" reading is excluded by shape.

## Verdict: NULL — the frame is a dead discriminator at battery level

**Headline:** @1543-1549 cannot serve as the "pour que" discriminator for noun-43 — the discriminator's positive set is exhausted ({condition, mesure}), both members dead at battery grade on independent windows, and no new value can be named. The claim's "kill the queued candidates" arm is already satisfied by sibling batteries (suite/manière killed; condition/mesure killed at kill grade + terminal attestation closure), so the window has nothing left to discriminate.

Not kill-grade per protocol §4: the failure is candidate exhaustion, not a window forcing the frame false — the only reopen paths are red-team acts (the @21 polyvalence ruling; the red-team adjudication of the confirmed-subjectless "pour que prenne" fence), exactly the reservation that kept the sibling noun-43 battery at NULL. No standing red-team verdict is contradicted or overwritten (no A-series verdict covers 43's value or "43 pour que"; A9 00='pour' and GT 46='que' stand).

Note for the supervisor: this verdict makes `pour-que-lexicon-close` (already queued) the terminal bookkeeping for the discriminator itself; `frame-43-pred-37-32` (queued) remains the live 43 leg. The boundary alternative ("…78 43 ‖ pour que…" — 43 ending the matrix clause, the frame non-discriminating) is NOT decided here; it is proposed as follow-up 1 below.

## Follow-ups (null regenerates work; none duplicate queued targets)

1. **frame-43-00-boundary** (P3): adjudicate the boundary alternative at @1544. Test the parse "…77 78 43 ‖ 00=pour 46=que…" with 43 closing the matrix clause (@1536-1544 '62 06 21 62 93 88 77 78 43' must parse complete under standing values) and the subjectless "pour que prenne" reading (already confirmed: prenne-subject-S1545 PROMOTE) as the subordinate clause. Bar: resolve iff the matrix clause parses complete AND no government reading of "43 pour que" survives the noun-43 exhaustion; else fence for red team. If the boundary holds, @1544 is definitively non-discriminating and the red team can close it.
2. **pour-que-leftclass-4win** (P4): left-class census of all four "pour que" windows (@106, @545, @1545, @1680) — name the left context's class in each (verb/ending/unknown/noun) under standing values, and test the distributional hypothesis "pour que is never noun-governed stream-wide" as construction-level kill-grade evidence against any government reading. Bar: resolve iff all four left-contexts are classified with <=1 open; else fence.
3. **frame-77-78-43-slot** (P4): name the "77 78 43" nominal frame at @1542-1544 (the only 78-43 contact stream-wide): decide whether 78 heads the NP (43 appositive/adjectival) or 78 is appositive to 43, under the 77-78 x7 census and the ver-78 LEAD. Bar: resolve iff one structure parses with zero contradiction under standing values; else fence. Feeds the noun-43 red-team docket and the 78-value question.

## Bookkeeping

- Lock created on start (`frame-43-pour-que-1544.lock`), deleted on completion.
- battery-queue.json: `frame-43-pour-que-1544` -> status "verdict", verdict {"result": "null", "report": "code/crowd17/report_inbox/battery-frame-43-pour-que-1544.md", "date": "2026-10-09"} (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated post-write).
- No downgrade of any standing verdict. No standing red-team verdict contradicted. R5005, sealed gates, red-team queue untouched. No numbers invented — every count traces to the repaired 1,847-pair stream.
