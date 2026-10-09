# Battery verdict: stem-62-7994-residual

- Target: `stem-62-7994-residual` (battery-queue.json, priority 3, status queued)
- Claim: "Narrow bar on the unparsed 62-94-79 twins (@1362/@1686)."
- Bar (verbatim, pre-registered): "Resolve iff the twins parse under one stated lexeme choice with <=1 ungranted assumption; else confirm as hard residual with stated cause."
- Numbered clauses: C1 — the twins parse under ONE stated lexeme choice for 62 with ≤1 ungranted assumption → resolve (PROMOTE-equivalent). C2 — else confirm as hard residual with stated cause → NULL.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`;
asserts held). `canonical.py` never used. Adopted as premises (not re-litigated):
scope-62-verb-noun NULL (twins = hard residual, unparsed under {règn-, trôn-}
and the 'il' rival); gerund-60-1688 PROMOTE ("tout en [60]" = licensed
gérondif at both windows); 94='ne' STRONG LEAD (R17-001); 79='tout' granted
(A5); 62='il' killed at kill grade (R19-106, confirmed R20-125); 92/93 verb
class granted. R5005, sealed gates, red-team queue untouched.

## Window evidence (byte-exact)

- **@1362** (a7_06): `35(noun) 13 92(verb) [62] 94(ne) 79(tout) 14 60 03(verb-stem) 30(pas) 82(m) 16 91 67`
- **@1686** (a8_05): `65(noun) 13 93(verb) [62] 94(ne) 79(tout) 14 60 27 46(que) 24(verb) 85 58`

Both twins share the core `[13] [92/93-verb] [62] ne tout en [60-gérondif]`.
The "79 14 60" tail is settled (gerund-60-1688 PROMOTE). The live question is
62's role and, structurally prior, the placement of "ne".

The full 62-94 family (n=9: @100/@508/@761/@840/@1329/@1362/@1686/@1704/@1772)
was re-derived for control. The twins are the ONLY "62 94 79" windows: in all
seven other windows "ne" is followed by {verb, qui, est, noun, pre, gov} —
only the twins have "ne" followed by "tout".

## C1: lexeme-choice tests (each = one stated lexeme choice for 62, tested at BOTH twins)

1. **62 = noun.** "[92/93-verb] [N] ne tout en [60]". A bare noun between a
   finite verb and "ne" is ungrammatical; additionally the productive
   bare-singular-nominal-direct-object frame is killed at grammaticality grade
   (30.8M-char corpus census). FAIL.
2. **62 = finite verb.** "[V] [V-fin] ne..." — two adjacent finite verbs,
   ungrammatical. FAIL.
3. **62 = infinitive.** "[V] [INF] ne tout en [60]" — non-modal verb +
   bare infinitive is ungrammatical; 92/93 as modals is an ungranted
   assumption, and "ne" remains dangling. ≥1 ungranted + "ne" unparsed. FAIL.
4. **62 = adverb.** "[V] [adv] ne tout en [60]" — "ne" has no verb to negate.
   FAIL.
5. **62 = subject pronoun.** 'il' killed at kill grade; any other pronoun is
   an ungranted value, and "ne" as expletive needs an ungranted licenser
   (92/93 = fear/doubt verb unattested). ≥2 ungranted assumptions. FAIL.
6. **62 = letter/syllable, word-internal** ("92/93+62" or "62+ne" as one
   word). "62ne" fusion contradicts 94='ne' STRONG LEAD (a standing verdict;
   per §5.2 the battery cannot overwrite it). "92/93+62" leaves "ne" dangling
   before "tout". FAIL.

**The blocker is 62-independent and structural.** In every segmentation,
94='ne' (STRONG LEAD negator) lacks a verb in negating position:
- "ne" is POST-verbal to 92/93/62 in every parse ("ne [verb]" order violated).
- "ne tout en [60-gérondif]" is ungrammatical — no "ne"-adverbial-gérondif
  frame exists in French.
- The expletive-'ne' reading needs a licenser (fear verb, "avant",
  comparative) before "ne"; none is attested at either window (92/93 values
  open; assuming one is ungranted).
- Long-distance "ne...pas": W1 has 30='pas' at @1368, but the span
  "ne tout en [60] [03] pas" puts an adverbial + gérondif + stem between
  "ne" and "pas" with no finite verb in the "ne [verb]" slot. Ungrammatical.
- W2's 24 (verb class, finite per R17-009) sits at @1693, five cells after
  "ne" with "tout en [60] 27 que" intervening — "ne" cannot reach it.

No lexeme choice for 62 changes the "ne" placement. C1 FAILS.

## C2: hard residual confirmed — stated cause

The 62-94-79 twins (@1362/@1686) are a **hard residual**. Stated cause: the
negator "ne" (94, STRONG LEAD) is unlicensable at both windows — post-verbal
in every segmentation, followed by "tout" (a configuration unique to these
two windows in the 9-window 62-94 family), with no expletive licenser and no
reachable finite verb. The failure is structural and 62-independent: no
single lexeme choice for 62 parses either twin within ≤1 ungranted
assumption. This confirms and hardens scope-62-verb-noun's residual (which
predates the 'il' kill and the gerund-60-1688 promote); neither intervening
verdict re-opens the windows.

## Verdict: NULL

Not PROMOTE: C1 fails — no resolving lexeme choice. Not KILL: no positive
claim is falsified; the residual is confirmed, not a value killed. §7 intact;
no standing/red-team verdict contradicted, downgraded, or re-litigated.
Canonical-stream caveat stands (rows a7_06/a8_05 offsets unvalidated).

## Follow-ups proposed (§4; all verified ABSENT from battery-queue.json)

1. `ne-tout-62-corpus` (P4) — corpus test: does negator-"ne" immediately
   followed by "tout" (no intervening verb/"pas") EVER occur grammatically in
   1841 French? A confirmed zero hardens this residual to grammaticality
   grade.
2. `val-13-1361-1685` (P4) — name 13's class at @1361/@1685 (shared left
   context "13 [92/93-verb] 62"); a named 13 (e.g. relative pronoun) could
   restructure the left edge of both twins.
3. `seg-62-94-word` (P4, gather-only) — package the "62+94" word-fusion
   hypothesis against 94='ne' STRONG LEAD as red-team input; fusion would
   need red-team adjudication to override standing, so no battery claim is
   made here.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-stem-62-7994-residual.md` (this file).
- Queue: `stem-62-7994-residual` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique temp
  file `battery-queue.json.stem-62-7994-residual.tmp` + atomic rename, no
  leftover; disk re-validated; own entry only; no downgrade).
- Lock `locks/stem-62-7994-residual.lock`: created on start
  (agent a59dc541-ff89-4d9d-bf62-40f74cbb8904, 2026-10-09T19:55:40Z, no stale
  lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
