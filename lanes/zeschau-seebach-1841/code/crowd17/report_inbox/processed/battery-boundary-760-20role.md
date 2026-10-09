# Battery `boundary-760-20role` — verdict: KILL (forced-after-20 claim is dead)

## Target

- id: `boundary-760-20role` (P3)
- claim: test 20 as clause-initial at the @760 locus directly (relative-adverb
  subclass "où/quand/comment" per reladv-20-1703's surviving arm, plus any
  other clause-initial role).
- Parent: `battery-adv-20-760-boundary` NULL (2026-10-09) — follow-up 3 of 3.
- adverses: none listed.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

> Bar: test 20 as clause-initial at @761 directly (relative-adverb subclass
> "où/quand/comment" per reladv-20-1703's surviving arm, plus any other
> clause-initial role). Bar: every clause-initial role killed → the boundary
> must fall after 20 (boundary forced, given a complete right clause); any
> role live → the forced claim is dead.

Numbered pass/fail clauses (restated, not modified after data):

- **C1.** Every clause-initial role for 20 at the locus is killed → the
  boundary must fall after 20 (boundary forced, given a complete right clause).
- **C2.** Any clause-initial role for 20 at the locus is live → the forced
  claim is dead.

Note on offsets: the queue brief says "@761" but the locus is 20 at 0-based
@760 (15-window census; parent battery). The right clause "62 94 59 39 88 66"
opens at @761. Same window, same test.

## Method

Read BATTERY-PROTOCOL.md first. Created
`code/crowd17/next-token/locks/boundary-760-20role.lock` on start (agent id +
UTC timestamp); no fresh lock present. Re-derived the repaired stream
in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed like
`code/side-keyhunt/repair_parse.py`: **1,847 pairs / 96 types**, asserts held;
20 census n=15 at @280 @307 @490 @642 @668 @703 @741 @760 @839 @873 @958 @1135
@1224 @1270 @1703. `canonical.py` never used. R5005, sealed gate instances,
red-team adjudication queue untouched.

Adopted, never re-litigated (all processed 2026-10-09):
`particle-20-760-839` NULL (particle face confirmed at battery grade, 'mais'
named and routed to `poly-20-docket`); `adverb-20-wide` NULL (clause-adverb
fenced, compatible at @760); `conj-prep-20-wide` NULL (conj/prep fenced);
`importe-1702-singleton` PROMOTE ('n'importe' confined @1700-1702);
§7 standing values (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; 87=ce,
64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; 59=est, 77=le
provisional; 62='il', 94='ne' leads; 67 et/veut sole polyvalence; 20="fois"
killed; 20~17 split holds).

## Window evidence (byte-exact, 0-based)

Locus, row a5_03 (@748–773, full row):

```
748: 00  749: 64  750: 02  751: 97  752: 40  753: 67 |
754: 11  755: 70  756: 82  757: 34  758: 29  759: 40 |   "la première"
760: 20 |
761: 62  762: 94  763: 59  764: 39  765: 88  766: 66 |
767: 98  768: 80  769: 10  770: 22  771: 94  772: 07  773: 06
```

"20 62 94" trigram occurs x3 stream-wide: @760, @839, @1703.
"20 62" bigram x4: @760, @839, @1135, @1703.

@1703 window (row a8_06): `... 85 33 94 30 | 20 62 94 88 26 12 06` —
"n'importe [20] il(62) ne(94) [88] [26]". The 'n'importe' frame confines
@1700-1702 (adopted PROMOTE). "n'importe où/quand il ne [88]" is the standard
French concessive relative clause. This is direct in-stream proof that 20 can
head a "62 94" ("il ne") clause as a relative adverb.

@839 window (row a5_06): `... 17 98 | 20 62 94 26 12 16 00 ...` — the particle
battery found the clause-initial particle slot effectively forced here (no
noun/det-adj/verbal reading grammatical for a free 20 between a closed clause
and "il ne").

## Clause-initial role tests at @760

1. **Particle ('mais' face): LIVE.** `particle-20-760-839` c1 PASSED at battery
   grade: "…et la première ; mais il(62) ne(94) est(59) à(39) [88] [66]…"
   parses as grammatical French, with the "la première" nominalization
   ellipsis stated. At @839 the same face's slot is effectively forced. A
   clause-initial role for 20 at the locus is confirmed, not merely
   compatible.
2. **Relative adverb 'où'/'quand': LIVE.** At @1703 the identical "20 62 94"
   frame carries the concessive "n'importe où/quand il ne [88]" reading —
   grammatical precedent that 20 heads an "il ne" clause as a relative
   adverb. At @760: "la première [fois] où/quand il n'est à [88] [66]"
   ("the first [time] when/where there is nothing to be [88]-ed [66]") with
   the stated nominalization ellipsis. Compatible, unfalsified, precedented.
3. **Clause adverb (ainsi/donc/cependant): LIVE at fence grade.**
   `adverb-20-wide` found it compatible at @760 ("la première, ainsi il
   n'est à…") with equally-live rivals — fenced, not killed. A fenced route
   is a live route.
4. **Relative/interrogative 'comment': KILLED at this window.** No manner
   antecedent ("la première" is not manner); relative "comment" is
   unlicensed here.
5. **Preposition: KILLED at this window.** A preposition needs an NP
   complement; 20 is followed by the finite clause "il ne est…". Ungrammatical.
6. **Subject: KILLED at this window.** 20 as subject + "il" = double subject.
   Ungrammatical.
7. **Coordinating 'et': KILLED at battery grade.** Naming 20="et" needs a
   homophone ruling against 67="et" (adopted particle-battery bound); §7
   declares no new polyvalence.
8. **Subordinating 'que': KILLED at this window.** No matrix verb governs a
   "que"-complement after the bare NP "la première", and as a relative
   pronoun "que" finds no gap ("il" fills the subject; no object gap).

## Per-clause results

- **C1: FAIL.** Three clause-initial roles are live at the locus: the particle
  face (confirmed at battery grade), the relative-adverb 'où'/'quand' face
  (in-stream grammatical precedent at @1703), and the clause-adverb face
  (fenced-compatible). Not every role is killed.
- **C2: FIRES.** A clause-initial role for 20 at the locus is live — twice
  over at battery grade. The forced-after-20 claim is dead.

## Verdict: KILL

**Headline:** the boundary-after-20 forced claim is dead. 20 heads the right
clause at @760 under two battery-grade clause-initial roles: the particle
face ('mais', confirmed by `particle-20-760-839`) and the relative-adverb
face ('où'/'quand', precedented by the @1703 "n'importe où/quand il ne [88]"
concessive). The boundary cannot be forced to fall after 20.

## Scope

This kills only the forced-after-20 claim. It does not promote a
boundary-before-20 reading and does not name 20's value — the value question
('mais' vs 'où' vs adverb rivals) is already routed to `poly-20-docket`.
No standing or red-team verdict contradicted or downgraded: the parent's
NULL fence on @760's boundary stays intact (fence narrows, it does not
break); §7 intact (no polyvalence declared — per-window role findings only).
Canonical-stream caveat stands (68/70 row offsets unvalidated).

No follow-ups proposed: the bar's decision rule is satisfied outright (kill,
not null), and the surviving value question already lives in
`poly-20-docket`. No new queue writes by this worker.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-boundary-760-20role.md` (this file).
- Queue: `boundary-760-20role` queued → `verdict`/`kill`, 2026-10-09
  (pre-write assert: status queued, no prior verdict; temp-file + rename;
  JSON re-validated post-write; own entry only; no downgrade).
- Lock `boundary-760-20role.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
