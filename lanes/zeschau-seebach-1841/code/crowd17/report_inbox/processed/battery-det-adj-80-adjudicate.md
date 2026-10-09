# Battery verdict: det-adj-80-adjudicate

- Target: `det-adj-80-adjudicate` (priority 2)
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json`); `canonical.py` not used.

## Bar (verbatim)

"confirm or fence each non-verb parse; if >=1 hard non-verb window stands with the infinitive legs, escalate for polyvalence adjudication (67-sole-polyvalence law)"

## Bar restated as numbered clauses

1. Confirm or fence the @1156 (a6_09) determiner parse of 80.
2. Confirm or fence the @469 (a2_10) adjective parse of 80 (conditional on 06='ent').
3. Confirm or fence the @1090 (a6_05) adjective parse of 80 (gated on 43).
4. If >=1 HARD non-verb window stands alongside the infinitive legs, escalate for
   polyvalence adjudication under the 67-sole-polyvalence law (do not declare a
   second polyvalence at battery level).

## Adverses (from queue)

- 67-sole-polyvalence law: 67 et/veut is the sole true polyvalence; a second
  polyvalence declaration needs red-team approval.
- @469's adjective read is conditional on 06='ent' (battery-promoted, unratified).

## Method

Re-derived all 17 windows of 80 on the repaired stream (offsets @441, @469, @517,
@565, @663, @673, @720, @768, @1011, @1032, @1090, @1156, @1295, @1322, @1596,
@1662, @1808). Tested each named non-verb window against 1841 diplomatic French
grammar with granted values only (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; provisional 59=est,
77=le). Row-offset grades checked against the crowd18 offset-validation report
(a6_09 PROBABLE-WEAK, a2_10 PROBABLE-WEAK, a6_05 PROBABLE, a3_02 UNRESOLVED
not-overturning, a5_00 PROBABLE-WEAK) — no offset requires change; windows stand.

## Window-level evidence

### Clause 1 — @1156 (a6_09): CONFIRMED HARD determiner

Bytes: `66 84 02 00 92 29 [80] 17 77 82 44 83 21`

With grants: `... pour [92]er [80] fois [le] ...` (00=pour, 29=er, 17=fois).

The slot immediately before "fois" (count noun) is determiner-only in French:
"une fois", "deux fois", "la première fois", "plusieurs fois". A verb in that
slot ("pour [inf] [verb] fois") is ungrammatical; a noun object without
preposition ("pour [inf] [noun] fois") is ungrammatical.

Escape attempts, all dead:
- (a) 92-29-80 as one word ("pour [92er80] fois"): the fois slot still lacks a
  determiner. Dead.
- (b) 80-17 as one word: 17=fois is promoted standalone; and the determiner
  gap persists. Dead.
- (c) Clause boundary after 29 ("pour [92]er. [80] fois ..."): 80 still opens
  the new clause in the determiner slot ("[det] fois, le ..."). Determiner
  reading survives re-segmentation.
- (d) 80 as adverb between infinitive and "fois": no French adverb occupies
  that slot. Dead.

80 at @1156 is a HARD non-verb: determiner/quantifier class.

### Clause 2 — @469 (a2_10): CONFIRMED CONDITIONAL adjective

Bytes: `59 42 96 00 33 79 [80] 06 67 46 84 24 37`

With grants: `... [est] [42] par pour [33] tout [80] 06 et/veut que on [24] ...`
(59=est provisional, 96=par, 00=pour, 79=tout, 46=que, 84=on).

Under 06='ent' (battery-promoted, UNRATIFIED) with 80-06 word-internal,
"tout [80]ent" is a grammatical adjective frame ("tout entier", "tout
puissant" shape). The parse is valid IFF 06='ent' is ratified. Fenced points:
(i) the 80|06 word boundary is assumed, not demonstrated; (ii) the right edge
"et que" (67=et per the 67 positional rule, follower 46=que not
infinitive-shaped) is awkward after an adjective and needs a wider-window
re-parse. Conditional-confirmed, not hard.

### Clause 3 — @1090 (a6_05): CONFIRMED CONDITIONAL, gated on 43

Bytes: `02 55 81 00 33 79 [80] 06 43 07 55 81 06`

Same "tout [80] 06" shape as @469: adjective read valid IFF 06='ent' ratified
AND 43 resolves to a value compatible with adjective continuation
(e.g. nominal: "tout [adj] [noun]"). 43's value is open — the gate stands.
Conditional-confirmed, gated.

### The infinitive legs (undisputed)

- @565 (a3_02): `... 43 24 [80] 97 ...` — 24 (finite modal verb, class-level)
  directly governs 80: modal + infinitive slot.
- @673 (a5_00): `... 86 24 [80] 03 ...` — same modal + infinitive frame.
- @441 (a2_09): `... 98 [80] 50 ...` — 98="vient" (battery-promoted, pending
  ratification): "venir" + infinitive complement.
- A8 grants 80 verb-frames. The infinitive legs stand without 77.

### Corroborating non-verb windows (outside the bar, noted)

- @517: `77 [80] 09` — under provisional 77='le', 80 is nominal ("le [80]").
- @1011: `79 [80] 78` — "tout [80]" adjective-shaped.
- @1032: `29 [80] 77` — "[X]er [80] le": 80 as nominal object.
- @1596: `29 [80] 67` — "[X]er [80] et": 80 as nominal object.
The determiner/nominal shape recurs beyond the three bar windows.

## Per-clause pass/fail

1. @1156 determiner: PASS — confirmed HARD.
2. @469 adjective: PASS — confirmed CONDITIONAL (fenced on 06='ent' ratification
   and the "et que" right edge).
3. @1090 adjective: PASS — confirmed CONDITIONAL, gated on 43.
4. Escalation clause: TRIGGERED — one HARD non-verb window (@1156) stands with
   the infinitive legs.

## Adverses answered

- 67-sole-polyvalence law: not ignored — it is the reason for escalation. The
  battery does not declare a second polyvalence; the contradiction is handed to
  the red team.
- @469 conditional on 06='ent': answered — confirmed as conditional-valid with
  stated fence points; no claim made beyond the grant.

## Verdict: NULL — escalate for polyvalence adjudication

Rationale: the battery's bar is satisfied (adjudication performed, escalation
clause triggered), but the outcome contradicts the standing 67-sole-polyvalence
law: 80 is HARD determiner/quantifier at @1156 and infinitive verb at
@565/@673/@441. Per protocol §5.2 the battery marks NULL rather than
overwriting a standing rule, with the contradiction as the headline. The
red-team venue decides among: (a) declaring 80 a second true polyvalence,
(b) a positional-resolution rule for 80 in the style of 67's ("67=veut iff
follower infinitive-shaped"), or (c) re-segmentation dissolving one side.
No standing verdict contradicted or downgraded. R5005, sealed gates, and the
red-team adjudication queue untouched.

## Follow-ups (null regenerates work)

1. `poly-80-docket` (P1, red-team venue): adjudicate 80's verb/determiner split
   — second polyvalence declaration vs positional-resolution rule vs
   re-segmentation. Carries this report's @1156 hard window and the infinitive
   legs as the docket evidence.
2. `det-80-1156-corrob` (P2): close the @1156 frame — identify 92's value (the
   "[92]er" infinitive governing the window); test the 92-29-80 word-internal
   escape byte-exactly; census "X fois" determiner slots to type 80's
   quantifier value.
3. `adj-80-469-ratify` (P2): when 06='ent' is ratified, re-test @469/@1090 as
   hard adjective legs (resolve the "et que" right edge at @469 and the 43 gate
   at @1090); fence or promote the adjective leg for 80.

## Bookkeeping

- Lock `locks/det-adj-80-adjudicate.lock` created on start, deleted on completion.
- `battery-queue.json`: target `det-adj-80-adjudicate` queued → verdict/null,
  own entry only, no downgrade (no prior verdict existed).
