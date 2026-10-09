# Battery report: val-21-reopen — re-run the 21 value search with 'suite' killed

- Target id: `val-21-reopen`
- Claim: "Re-run the 21 value search with 'suite' killed — the rival shootout's idiom controls ('donner X', 'par X', 'de X') remain anchored frames for a new candidate."
- Date: 2026-10-09
- Worker: battery worker (subagent 9d3a7330-0fee-4469-a85a-7df20de1554b)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
  1,847 pairs / 96 types asserted in-work). `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched. All @-offsets
  are 0-based repaired-stream pair indices.
- Lock: code/crowd17/next-token/locks/val-21-reopen.lock (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"name a value with >=2 anchored frames and zero kill-grade contradictions, or
close the battery-grade value search. Do not duplicate queued
suite-21-residuals."

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) A value is NAMED iff it parses >=2 anchored frames with zero
   kill-grade contradictions anywhere in 21's 30 windows. Anchored frames
   (re-derived in-work, matching rival-21-feminine's F1–F5):
   F1 "donne X" @171 (`84 53 12 48 21 60`), F2 "par X" @231/@1064/@1787
   (`96 21` x3), F3 "la X" @109/@359 (`11 21` x2), F4 "de X" @1162/@1841
   (`83 21` x2), F5 "X veut" @1422/@1456 (`21 67` x2, 67="veut" by §7 rule).
2. (C2) If no value satisfies C1, the battery-grade value search is CLOSED
   with stated cause (the bar's second arm).
3. (C3) suite-21-residuals' owned residuals (@176, @1207) are not duplicated.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 types; n(21)=30
   confirmed; all 30 windows enumerated with ±8 context).
2. Re-verified the five anchored frame-types on the repaired stream
   (F1–F5 match rival-21-feminine's census; F1's 53-12-48 "donne" composition
   is half-pass pending 12/48 ratification — stated wherever leaned on).
3. Tested the candidate space by CLASS, not just by rival list:
   (a) feminine nouns — adopted rival-21-feminine's shootout (10 rivals,
   cited not duplicated); (b) masculine nouns — fresh spot-check of the 5
   best idiom-fit candidates against F1/F2/F4 plus the F3 kill; (c) non-noun
   classes — checked against the promoted class verdict.
4. Re-tested @134 ("qui 21 65") for value-INDEPENDENCE: does the kill hold
   for every noun value, not just "suite"?
5. Phase-checked the killing loci (rival-offset re-parses of a1_04, a1_03,
   a2_06, a8_00) and recorded the canonical-offset caveats.

## Standing premises (adopted, not re-litigated)

- 21 = NOUN class: battery-promoted (de-frame-21-class). Battery cannot
  downgrade it; non-noun values require red-team re-tiering.
- 21 = "suite" (value): kill-grade dead (suite-21-qui-que), cited as premise.
- 65 = noun: battery-promoted (prof-65, 2026-10-08, pending ratification).
- 63 = verb class: battery-promoted (verb-63-frames, 2026-10-09).
- 11 = "la": banked ground truth. 64 = "qui": banked ground truth.
  96 = "par": promoted. 67 et/veut §7 positional rule: sole true polyvalence.

## Window-level evidence

### The universal kill: @134 "qui 21 65" (a1_04, repaired offset 1)

Context (re-derived): `... 96(par) 56 64(qui) 21 65 23 91 65 13 66 ...`
= "par [56] qui [21] [65] [23] [91] [65] ...".

For ANY noun value N at 21, with 65 noun-class (battery-promoted):
- (a) relative "qui" + NP ("qui N 65"): ungrammatical — subject relative
  "qui" must be immediately followed by its verb. KILL.
- (b) "qui" + interrogative/exclamative reading: still needs a verb.
  None present. KILL.
- (c) 65 as finite verb ("qui N [65-V]"): contradicts the battery-promoted
  65=noun — battery cannot downgrade; closed at battery grade.
- (d) 21 as the verb ("qui [21-V] [65]"): contradicts battery-promoted
  21=noun — closed at battery grade.
- (e) clause boundary ("...qui. N 65..."): interrogative "qui" still
  requires a verb; none follows. Forced, not a parse. KILL.
- (f) 21-65 as a unit verb: requires a second polyvalence per §7 —
  red-team venue (already escalated by suite-21-qui-que), never declared
  here.
- (g) a later finite verb rescuing "qui" (23? 91?): "qui" must be
  IMMEDIATELY followed by its verb; the intervening nouns 21/65 break
  the construction regardless of 23/91's class. KILL.

Result: @134 kills EVERY noun value at kill grade, value-independently.
The old 65=verb conditional rescue is gone (65=noun battery-promoted).

### The gender lock: @109 / @359 "la 21" (a1_03 / a2_06)

@109: `... 00(pour) 46(que) 11(la) 21 67 93 ...` (a1_03, offset 0, row-internal).
@359: `... 47(ce) 11(la) 21 62 ...` (a2_06, offset 0, row-internal).
11="la" is banked ground truth: any uniform value must be feminine-singular
at these windows. Every masculine noun is kill-grade dead here
("la" + masculine noun is ungrammatical in every register).

### @1529 "que 21 65 63 pour 66" (a8_00, repaired offset 1)

Value-NEUTRAL under the new battery state: "que [21] [65] [63-verb]
pour [66-inf]" = "que" + NP + finite verb + purpose clause, where the
"21 65" subject composition costs one stated assumption (A12 unit
precedent, per verb-63-frames). It parses for ANY noun value — neither a
kill nor a confirmation for any candidate. Noted, not leaned on.

### @176 "[86-INF] 21" and @1207 "21 65 qui est"

Value-independent residuals (name-21-obj / suite-21-residuals): bare noun
after an infinitive (@176) and the "21 65" NP (@1207) fail or parse for
every bare noun alike — they do not discriminate between values.
suite-21-residuals owns their resolution; not duplicated here (C3).

## Candidate-space sweep

**Feminine nouns — exhausted (cited, not duplicated).** rival-21-feminine
(2026-10-09, NULL) tested 10 rivals (chose, peur, force, raison, vérité,
forme, audience, naissance, satisfaction, + mémoire/mégarde) against the
three idiom controls: none beats "suite" (the unique triple-winner), and
every rival inherits @134's value-independent kill plus the class-level
residuals. No feminine noun satisfies C1.

**Masculine nouns — fresh spot-check, all dead.** Tested the 5 best
idiom-fit masculine candidates against F1/F2/F4 and the F3 kill:

| candidate | donner X (F1) | par X (F2) | de X (F4) | la X (F3) |
|---|---|---|---|---|
| droit | ✓ "donner droit à" | ✗ "par droit" unattested | ✓ "de droit" | ✗ KILL ("la droit") |
| ordre | ~ "donner ordre à" (bare, thin) | ✓ "par ordre" | ✗ "d'ordre" weak | ✗ KILL ("la ordre") |
| parti | ✗ "donner parti" | ✗ "par parti" | ✗ | ✗ KILL |
| point | ✗ "donner point" | ✗ | ✗ | ✗ KILL |
| moyen | ✗ "donner moyen" (bare) | ✗ "par moyen" (bare) | ✗ | ✗ KILL |

Every masculine candidate fails ≥1 idiom control AND dies at kill grade
at F3. No masculine noun satisfies C1. (F3's "la" is banked GT; a1_03's
offset-0 is likelihood-favored — see phase caveats.)

**Non-noun classes — barred.** Adjective/pronoun/verb/adverb values
contradict the battery-promoted 21=noun class; battery cannot downgrade a
verdict and declares no polyvalence (§7). They are re-openable only by
red-team re-tiering. Numbers ("la deux") and infinitives-as-nouns
("qui manger 65") die at kill grade at F3/@134 respectively.

## Per-clause pass/fail

1. (C1) Name a value with >=2 anchored frames and zero kill-grade
   contradictions: **FAIL.** Feminine space exhausted (cited); masculine
   space killed at F3 + idiom controls; non-noun space barred by the
   promoted class. @134 kills every noun value value-independently.
2. (C2) Close the battery-grade value search: **FIRES.** The nameable space
   is empty at battery grade: every noun dies at @134, every masculine noun
   dies at @109, non-nouns contradict the promoted class.
3. (C3) No duplication of suite-21-residuals: **PASS** — @176/@1207 treated
   as value-independent residuals, not re-parsed.

## Adverses

- "The 'suite' kill stands (cited as premise, not re-litigated)":
  ANSWERED — adopted; @134's universality extends the kill to all noun
  values without re-litigating "suite" specifically.

## Verdict: KILL

The proposition "a battery-grade value for 21 exists" fails at kill grade:
@134 forces every noun value false, @109/@359 force every masculine value
false, and non-noun values contradict the battery-promoted noun class.
**The battery-grade value search for 21 is closed.** This is a search
closure, not a class downgrade: 21=noun (de-frame-21-class) stands
untouched.

### Re-open conditions (red-team venue only)

1. Red-team overturns prof-65's 65=noun promote → @134's kill re-opens
   (65=verb rescue).
2. Red-team grants the §7 21-65 unit-verb rescue (already escalated) →
   @134 re-opens.
3. Red-team re-tiers 21's class → non-noun values become nameable.

## Phase caveats (stated, not hidden)

- @134's "64 21 65" trigram DISSOLVES under a1_04's rival offset-0
  (re-parses to "56 42 16 52 39 ..."). a1_04's repaired offset-1 is
  likelihood-favored (not among the 20 rival-favoring rows), so the kill
  holds per protocol on the canonical stream — but it is a canonical-offset
  object (same mechanism class as a1_01/a7_10/a2_05).
- @109's "11 21" bigram dissolves under a1_03's rival offset-1;
  a1_03's offset-0 is likelihood-favored. Holds per protocol.
- @359's "11 21" dissolves under a2_06's rival offset-1; a2_06 is weakly
  rival-favoring (-0.26 nats, near-tie) — the feminine constraint rests on
  @109, not @359.
- F1's "donne" composition (53-12-48) is half-pass pending 12/48
  ratification; the F3 kill and @134 kill do not lean on it.

## Follow-ups (kills regenerate work too)

1. **reopen-21-65-ratified** (P3): re-open 21's value search iff the red team
   (a) ratifies 65=noun AND (b) rules on the §7 21-65 unit-verb rescue.
   Bar: name a value with >=2 anchored frames and zero kill-grade
   contradictions under the ratified state.
2. **phase-a1_04-134** (P4): constraint sweep of a1_04 under offset-0; if a
   rival phase is ever adopted, @134's kill dissolves and the value search
   re-opens on new soil.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-val-21-reopen.md
- Queue: battery-queue.json → `val-21-reopen` status `verdict`, result
  `kill`, date 2026-10-09 (pre-write assert passed — was `queued`,
  verdictless; temp-file + rename; JSON re-validated; only this entry
  touched; no downgrade).
- Lock created on start, deleted on completion. `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched. No standing or
  red-team verdict contradicted or downgraded; §7 intact.
