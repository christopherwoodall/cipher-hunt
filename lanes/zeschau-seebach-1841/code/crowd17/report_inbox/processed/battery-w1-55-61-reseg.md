# Battery report: w1-55-61-reseg

Target: `w1-55-61-reseg`. Claim: re-test W1 under non-detachable
segmentations (13-55-61 or 55-61-94 as one word, e.g. the
"reprenne"/"reprennent" family).
Date: 2026-10-09. Worker: battery worker (subagent 27f06633-26b8-4769-bace-2ce5807bd0b7).
Lock `locks/w1-55-61-reseg.lock` created 2026-10-09T08:39:56Z (no
pre-existing or stale lock for this id); deleted on completion.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff W1 parses under a non-detachable segmentation with byte evidence"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. W1 parses with **13-55-61 as one French word**, with byte evidence for
   the segmentation.
2. W1 parses with **55-61-94 as one French word**, with byte evidence for
   the segmentation.

Adverses (from queue): none listed.

## Method

Read BATTERY-PROTOCOL.md in full first. Re-derived the repaired 1,847-pair
/ 96-type stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (byte-exact stride-2 pairing per row
offset); asserted 1,847 pairs / 96 types before testing. `canonical.py`
never used. R5005, sealed gate instances, and the red-team adjudication
queue untouched. Every number below re-derived in-session; no prior counts
trusted.

Standing values used (protocol section 7): banked GT 11=la, 70=pre, 82=m,
40=e, 46=que, 34=i, 29=er; granted 87=ce, 47="ce" (allophone tier); 94="ne"
STRONG LEAD (R17-001, battery-promoted); 06="ent" (promoted, conditional on
94="ne" per R17-007); leads 78="ver", 45="dict"/"ce" (A11 HOLD). 67 et/veut
sole true polyvalence.

Sibling context read before testing (coordinated, not duplicated):
- `battery-x-55-61-candidate-list.md` (KILL, 2026-10-09): the detachable-slot
  one-word-over-55-61 reading is killed at kill grade; this target is its
  redirect #1.
- `battery-seg-61-94-word-adjudicate.md` (KILL, 2026-10-09): the 55-61-94
  family candidacy CLOSES at kill grade; re-open is red-team-only.
- `battery-seg-55-61-94-word.md` (NULL, superseded by the adjudicate kill):
  its follow-ups F1/F2/F3 are all resolved (seg-55-re-prefix null,
  seg-61-pren-polyvalence kill, seg-55-61-21-stem promote) — nothing to
  duplicate.
- `battery-name-13-55-61.md` (NULL) and
  `battery-unit-13-55-61-contact.md` (NULL): trigram distributionally bound
  (13->55 exclusive to the two windows, Fisher p=0.0455) but not
  French-nameable.
- Queue check: `w1-573-subject` (verdict/null) and `w2-5561-nece-frame`
  (verdict/kill) are both resolved — no duplication.

## Window-level evidence (re-derived)

W1 — 13-55-61 @575-577 (0-based, row a3_02):
`52@571 87@572 78@573 45@574 | 13@575 55@576 61@577 | 94@578 82@579 06@580
06@581`
= "…[52] ce(87, promoted) verdict(78-45, LEAD) [13-55-61] ne(94, STRONG
LEAD) mentent(82-06-06, conditional on 94='ne')".

The 55-61-94 trigram @576-578 is W1's tail — the same window the
adjudicate battery closed (its brief @579 = 1-based 94@578).

## Clause 1: 13-55-61 as one word — FAIL at kill grade

X = one French word of 3 syllables in "…ce verdict X ne mentent".
"mentent" is a 3pl finite verb; the clause needs a grammatical subject or
construction for X. Every word class fails under standing values:

| # | X class | Parse | Result |
|---|---|---|---|
| 1 | plural noun (bare 3pl subject) | "…verdict [noun-pl] ne mentent" | KILLED — French prose requires a determiner for count-noun subjects ("*Témoins ne mentent" ungrammatical). The detachable reading's noun survival (x-55-61) depended on 13 as a SEPARATE determiner slot ("les X ne mentent"); non-detachable segmentation removes that slot. |
| 2 | singular noun | agreement with 3pl "mentent" fails | KILLED |
| 3 | finite verb (3pl, e.g. "reprennent"-shaped) | "verdict [V] ne mentent" — two finite verbs, no conjunction | KILLED |
| 4 | finite verb (3sg) | double finite verb + agreement fail | KILLED |
| 5 | infinitive | no licensed role in this frame | KILLED |
| 6 | adjective | nothing to modify; no copula | KILLED |
| 7 | adverb | no license in this position | KILLED |
| 8 | determiner / pronoun / preposition / conjunction / interjection | no 3-syllable French subject pronoun exists (inventing one = inventing data); all others leave "ne mentent" subjectless or the frame ungrammatical | KILLED |
| 9 | plural proper noun (bare) | same determiner-licensing failure as #1 | KILLED |

Rescue attempts, all dead:
- Expletive-"ne" reading of 94: no trigger present (no comparative, no
  "avant que"); 94="ne" STRONG LEAD stands undisturbed.
- Elided-"qui" relative ("verdict [X] [qui] ne mentent"): "qui"-elision is
  ungrammatical French.
- Redefining 94: forbidden — §7 bars a second 94 value without red-team
  declaration; R17-001 STRONG LEAD holds.

The failure does not depend on the unsettled 78="ver"/45="dict" leads:
even with 78-45 unread, "[X] ne mentent" admits no word class for X. The
load-bearing assumptions are 94="ne" (STRONG LEAD), 82-06-06="mentent"
(promoted, conditional on 94="ne"), and 87="ce" (promoted) — all standing.

Byte evidence: the distributional binding (13->55 exclusive to the two
5-gram windows, Fisher p=0.0455 per unit-13-55-61-contact) is real but is
evidence of COLLOCATION, not wordhood — and that battery already showed
the trigram is not French-nameable. The bar's conjunction (parse AND byte
evidence) fails on the parse conjunct.

## Clause 2: 55-61-94 as one word — NOT TESTED, closed by standing verdict

`seg-61-94-word-adjudicate` (verdict/kill, 2026-10-09) closed the 55-61-94
family candidacy at kill grade: the only named sub-claim (61="pren") is
forced false at two banked windows, and the bar's else arm is terminal
("closes"). Its re-open condition is red-team-only ("the red team fences
@1556 and @367 with stated cause, or the red team ratifies a named French
word with 61-94 as syllables at both windows"). Re-testing the closed arm
at battery level would contradict a standing verdict; per §5 it is fenced
with cause here, not re-litigated.

## Per-clause pass/fail

1. **FAIL (kill grade).** W1 forces the 13-55-61-as-one-word claim false:
   no French word class yields a grammatical parse under standing values.
2. **FENCED (not tested).** 55-61-94 arm closed at kill grade by standing
   verdict seg-61-94-word-adjudicate; red-team-only re-open.

## Adverses answered

None listed in the queue entry.

## Verdict: KILL

Both non-detachable arms are dead: 55-61-94 is closed by standing
kill-grade verdict (red-team-only re-open); 13-55-61 is forced false at
W1 at kill grade — every word class for the 3-syllable word X fails
grammaticality under standing values, and the byte evidence (collocation
binding) does not satisfy the bar's parse conjunct. Together with
x-55-61-candidate-list's kill of the detachable reading, W1's 13-55-61
span is now exhaustively unparseable at battery level under standing
values. No standing or red-team verdict contradicted or downgraded (§5
escalation not triggered).

## Follow-ups

None required (§4: kills do not regenerate work). The live redirect ends
are all resolved: `w1-573-subject` (verdict/null — W1's "ne mentent"
subject stays unidentified), `w2-5561-nece-frame` (verdict/kill),
seg-55-61-94-word F1/F2/F3 (null/kill/promote). The distributional
13-55-61 binding (unit-13-55-61-contact null) keeps its own queued
follow-ups; nothing here duplicates them. Re-open condition (battery may
not call it): the red team declares a determiner-less plural-subject
license for this register, or ratifies a named 61-94-syllable word per
the adjudicate's re-open terms.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-w1-55-61-reseg.md (this file).
- Queue: `w1-55-61-reseg` queued -> verdict/kill via temp-file + rename
  (pre-write assert confirmed queued/verdictless; JSON re-validated
  post-write; own entry only; no downgrade).
- Lock created on start (2026-10-09T08:39:56Z), deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication
  queue untouched.
