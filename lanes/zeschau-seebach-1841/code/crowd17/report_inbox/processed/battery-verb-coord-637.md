# Battery report: verb-coord-637 — "@637 as verb coordination ('que [60-V] et le [89-V]e')"

- Target id: `verb-coord-637`
- Claim: test @637 as verb coordination ('que [60-V] et le [89-V]e')
- Date: 2026-10-09
- Worker: battery worker (subagent cc376c89-ae42-4903-885d-d031cabe2a32)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 types asserted). All @-offsets are 0-based repaired-stream indices.
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/verb-coord-637.lock (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"resolve iff 'que [60-V] et le [89-V]e' @637 parses with 74's class stated and both verbs' subjects identified + zero contradictions; else fence with cause."

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) 'que [60-V] et le [89-V]e' parses grammatically at @636–641 under
   standing values: both conjuncts are verb phrases, i.e. 89 is verb-shaped
   here.
2. (C2) 74's class is stated (it governs the subject slot left of 'que').
3. (C3) Both verbs' subjects are identified.
4. (C4) Zero contradictions with standing values.

## Method

1. Re-derived the repaired parse in-session; asserted 1,847 pairs / 96 types.
   Never used canonical.py. R5005 not touched.
2. Byte-confirmed the locus: @635='74', @636='46', @637='60', @638='67',
   @639='77', @640='89', @641='48', @642='20', all row a4_01 (offset 1,
   upstream, unvalidated — canonicality caveat).
3. Tested against standing values only: 46='que' (banked GT), 67=et/veut
   (sole true polyvalence, positional rule: 'veut' iff follower
   infinitive-shaped — 77 is not, so 'et'), 77='le' (provisional), 48='e'
   (R17 letter-tier grant), 60 verb class (battery-promoted, poly-60-redteam
   venue), 89 fenced split (noun26-89-class PROMOTE: noun at '77 89'
   windows, infinitive at '24 89' windows), 74 class fenced open
   (noun-74-census NULL).

## Window-level evidence

- **@636 = 46 = 'que'** (banked GT).
- **@637 = 60** — verb class adopted as premise at battery grade (bare-60
  verb group, poly-60-redteam the adjudication venue). Not re-litigated;
  the adverse's verb-60 six-window bar is not duplicated.
- **@638 = 67 = 'et'** by the positional rule (follower 77 is not
  infinitive-shaped). So the second conjunct opens with the conjunction,
  not a verb.
- **@639–641 = '77 89 48' = "le [89]e"** — noun-89 arm FORCED at kill grade
  per battery-promoted noun26-89-class: an infinitive after an article is
  ungrammatical in 1841 French; the exact "le [89]e" shape is forced noun at
  @640/@871. Reading '[89-V]e' here is kill-grade dead. Load-bearing on
  provisional 77='le' (stated).
- **Consequence for the coordination claim:** the second conjunct is
  "et le [89]e" = conjunction + noun phrase, not a verb phrase. A verb
  coordination needs two verb phrases; there is one at most. Claim forced
  false at kill grade.
- **@635 = 74** — class fenced open (noun-74-census NULL: the '74 74'
  doubling family caps every whole-word class below the 2/3 bar). C2's
  "74's class stated" cannot be satisfied at battery grade.
- **Subjects:** in the would-be first conjunct "74 que [60-V]", the subject
  would be 74-as-noun (relative antecedent) — class open, not nameable. In
  the would-be second conjunct, no subject slot exists at all ("le" is an
  article/object clitic, never a subject pronoun in this position). C3
  fails: neither verb's subject is identifiable under standing values.
- Left edge @634='63' changes nothing (63 verb class, battery-promoted;
  no licensed subject reading reaches the conjuncts).

## Per-clause pass/fail

1. **C1 FAIL AT KILL GRADE.** 'que [60-V] et le [89-V]e' does not parse:
   89 is forced noun in "le [89]e" (kill grade per noun26-89-class), and
   the second conjunct is an NP ("et le [89]e"), not a VP. The window
   forces the claim false.
2. **C2 FAIL.** 74's class cannot be stated — fenced class-open at battery
   grade (noun-74-census NULL).
3. **C3 FAIL.** No subject identifiable for either verb under standing
   values; the second conjunct has no subject slot.
4. **C4 FAIL.** The parse contradicts the battery-promoted noun-89 arm.

The bar's else-branch ("fence with cause") does not apply: this is not an
unresolved parse, it is a kill-grade contradiction. Verdict is KILL.

## Adverses answered

- "subject gap unresolved" — CONFIRMED and closed as unbridgeable here:
  even adopting 60=V, no subject exists for the coordinated verb pair, and
  the second conjunct is not a verb phrase. Not ignored.
- "coordinate with verb-60 (queued), do not duplicate its six-window bar"
  — 60=V adopted as battery premise only; verb-60's bar untouched, not
  duplicated.

## Verdict: KILL (the verb-coordination hypothesis at @637)

The claim "test @637 as verb coordination" is forced false at kill grade:
'77 89' = "le [89]e" is noun-shaped (forced), so 'et le [89-V]e' cannot be
a verb phrase; 74's class is unstated; neither verb's subject is
identifiable. No cleaner rival demonstrated: the window's standing reading
is the residual "…63 [74] que [60] et le [89]e…" with 74/60 open.

**Scope fence (what did NOT die):** 60's battery-promoted verb class is
untouched; 89's infinitive arm at '24 89' windows (noun26-89-class arm B)
stands; the poly-60 and poly-89 red-team dockets are untouched. §7 intact.

**Re-open conditions (all red-team venue):** the noun-89 arm overturned by
red team, 77≠'le' established, or a licensed verbal parse of "le [89]e"
demonstrated on bytes.

**Caveat:** a4_01's upstream offset is unvalidated; verdict holds on the
canonical stream per protocol.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-verb-coord-637.md
- Queue: `battery-queue.json` → `verb-coord-637` status `verdict`,
  result `kill`, date 2026-10-09 (pre-write assert passed —
  was `queued`/verdictless; temp-file + rename; JSON re-validated; only
  this entry touched).
- Lock created at start, deleted on completion (verified gone).
- No standing or red-team verdict contradicted or downgraded; §7 intact;
  R5005, sealed gates, red-team adjudication queue untouched.
- Kill verdict — no follow-ups required per protocol (re-open conditions
  recorded above).
