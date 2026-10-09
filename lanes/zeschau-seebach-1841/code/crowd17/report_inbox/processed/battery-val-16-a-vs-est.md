# Battery report — val-16-a-vs-est (discriminate 16='a' vs 16='est')

Worker: battery-worker-val-16-a-vs-est. Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/val-16-a-vs-est.lock` created 2026-10-09T04:56:41Z;
no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(replicated in-worker, not `canonical.py`). R5005 not touched. Every count
below re-derived from the stream in this run. No observed values redacted.

## Bar (pre-registered verbatim, from battery-queue.json)

`resolve iff one of {16='a', 16='est'} covers the non-doubled windows with zero forced contradiction; else fence`

Adverses (queue): none.

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. 16='a' covers all 26 non-doubled 16-windows with zero forced contradiction.
2. 16='est' covers all 26 non-doubled 16-windows with zero forced contradiction.
3. If neither clause 1 nor clause 2 passes, fence (neither value resolved).

"Forced contradiction" = the candidate yields an ungrammatical parse under
standing values with no rescue available without contradicting a standing
verdict. Windows whose strain is shared by both candidates, or depends on
open/provisional values, are marked STRAINED/CONDITIONAL, not forced.

Standing values used: GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce;
provisional 59=est, 77=le; battery-promoted 12=n, 48=e, 94=ne (R17),
98=finite verb class-level (prof-98), 06=ent (R17-007), 24=finite verb
modal-shaped class-level (ne-24-profile); lead-only 62=on.

## Method

Re-derived the repaired stream (assert 1,847 pairs; assert 96 types;
n(16)=28 confirmed, byte-identical to frame-82-16's census). Excluded the two
doubled-frame windows (1-based @1196, @1199 — universal killer per
frame-82-16, not re-litigated). Tested 16='a' (avoir 3sg) and 16='est'
(être 3sg) at each of the remaining 26 windows with ±4 context. Adopted
frame-82-16's eliminations ("même"/"mais"/noun/infinitive killed) and its
fenced residuals (@1142 universal, @876/@1832 provisional-tier) as prior
evidence, not re-litigated. 1841 diplomatic French only.

## Window-level evidence (26 non-doubled windows, 1-based @)

Predecessor census: 82 x9, 62 x4, 12 x3, 33 x2, 42 x2, 65/32/49/86/67/89 x1.
(Doubled-frame 82 x2 excluded.)

- @84 "62 16 14": "on/il a/est [14]". 14 open. Both CONDITIONAL. No force.
- @188 "33 16 00": "[33] a/est pour [66]". "a pour"/"est pour" both grammatical;
  33 open. Both CONDITIONAL (shared strain on 33's left edge).
- @221 "42 16 24": "[42] a/est [24-finite-modal]". "a"+"[finite]" and
  "est"+"[finite]" both strained; 24's class standing but the window's
  left edge (42 predicative) leaves the construction underdetermined.
  Both STRAINED (shared, not candidate-specific). Follows parent's
  "open/neutral" assessment; not counted as forced for either.
- @243 "12 16 56": "n'a/n'est [56]". Both CONDITIONAL (56 open).
- @295 "65 16 01": "[65-noun] a/est [01]". Both CONDITIONAL (01 open).
- @383 "82 16 52": "m'a/m'est [52]". Both CONDITIONAL (52 open).
- @435 "82 16 78": "m'a/m'est [78]". Both CONDITIONAL (78 open).
- @534 "32 16 08": "[32] a/est [08]". Both CONDITIONAL (32/08 open).
- @538 "82 16 91": "m'a/m'est [91]". 91 open. "a"+"[pp]" (passé composé) vs
  "est"+"[adj]" both live. Both CONDITIONAL. **Key future discriminator:
  91's class decides this window.**
- @660 "62 16 00": "on/il a/est pour [86]". Both CLEAN ("a pour"/"est pour"
  grammatical). No force.
- @845 "12 16 00": "n'a/n'est pour [33]". Both CLEAN. No force.
- @877 "49 16 77": "[49] a/est le [86]". Under 'est': "est le" grammatical.
  Under 'a': "a le" ungrammatical in French ("avoir"+"le" contracts to
  "l'a") — CONDITIONAL contradiction of 'a', gated on provisional 77='le'
  and 49 as subject. **Weak signal toward 'est'.** Already fenced by parent
  as provisional-tier residual; not counted as forced.
- @901 "86 16 92": "[86] a/est [92]". Both CONDITIONAL (86/92 open).
- @904 "67 16 88": "et a/est [88-verb]" (67="et": 16 not infinitive-shaped,
  positional rule). Both STRAINED (shared).
- @1143 "62 16 29": "on/il a/est er [42]". "a"+"er" ("aer" not French),
  "est"+"er" ("ester" not French); 29='er' GT bound morpheme. **FORCED for
  both.** Already fenced by parent as universal residual ("ungrammatical
  under every class"); not candidate-discriminating.
- @1247 "33 16 00": same as @188. Both CONDITIONAL.
- @1299 "62 16 02": "on/il a/est [02]". Both CONDITIONAL (02 open).
- @1371 "82 16 91": "m'a/m'est [91]". Same as @538. Both CONDITIONAL.
  **91's class is the key.**
- @1388 "82 16 06": "m'a/m'est [06=ent]". "ent" is a bound ending, not a
  word. Both STRAINED (shared).
- @1395 "89 16 76": "[89] a/est [76-noun]". Both STRAINED (shared;
  determiner missing under either).
- @1412 "42 16 97": "[42] a/est [97]". Both CONDITIONAL (97 open).
- @1432 "12 16 76": "n'a/n'est [76-noun]". Both STRAINED (shared bare-'ne'
  strain; no 30='pas' downstream at any of the three 12-16 windows).
- @1438 "82 16 24": "m'a/m'est [24-finite-modal]". Same as @221.
  Both STRAINED (shared, per parent's neutral assessment).
- @1481 "82 16 98": "m'a/m'est [98-finite-verb]". "m'a"+"[finite]" and
  "m'est"+"[finite]" are both ungrammatical in French at any period
  ("m'a"/"m'est" license only participle/adjective complements; 98 is
  finite verb per standing battery verdict prof-98, §5-forbidden to
  overwrite). Rescues attempted: clause boundary after "m'a" (no byte
  evidence, "[98] [62] que" unparseable); 16+98 one word ("avient"/
  "estvient" not French); 82+16 as "ma" possessive ("ma"+"[finite]"
  ungrammatical). **FORCED for both.** (Confirms laisser-gate-16 C3.)
- @1653 "82 16 01": "m'a/m'est [01]". Both CONDITIONAL (01 open).
- @1833 "82 16 59": "m'a/m'est [59=est-provisional]". Both ungrammatical
  ("m'a est"/"m'est est"); already fenced by parent as provisional-tier
  residual. Not candidate-discriminating.

## Per-clause pass/fail

1. 16='a' with zero forced contradiction: **FAIL**. Forced at @1143
   ("a er") and @1481 ("m'a"+"[finite verb]").
2. 16='est' with zero forced contradiction: **FAIL**. Forced at @1143
   ("est er") and @1481 ("m'est"+"[finite verb]").
3. Fence: **TAKEN**. Neither value resolves.

## Discrimination signals (not forced, recorded for the red team)

- @877 weakly favors 'est' ("est le" clean vs "a le" needing "l'a"),
  conditional on provisional 77='le'.
- 16-91 x2 (@538/@1371): 91's class is the cleanest remaining discriminator
  ("m'a"+"[past participle]" → 'a'; "m'est"+"[adjective]" → 'est').
- 16-00 x4: "a pour"/"est pour" both grammatical — not discriminating.
- @1481 is a forced contradiction of the finite-verb CLASS itself, not just
  'a'/'est': frame-82-16's "fits 24/28" overcounts (it did not flag @1481;
  laisser-gate-16 C3 did). The class lead needs re-tiering at red team.

## Standing-verdict check

No standing verdict contradicted or downgraded. gate-satisfiability-16-85
(16=infinitive, promote) still stands un-overwritten per §5; the
finite-verb lead (frame-82-16, laisser-gate-16) remains a lead, not a
naming. prof-98 (98=finite verb) used as standing, not re-litigated.
No polyvalence declared (§7 intact). R5005, sealed gates, red-team queue
untouched. `canonical.py` never used.

## Verdict: NULL (fence executed)

Neither 16='a' nor 16='est' covers the 26 non-doubled windows with zero
forced contradiction. Both are forced-false at @1143 ("a/est er") and
@1481 ("m'a/m'est"+"[finite verb]"). The 'a'/'est' refinement does not
close; the finite-verb class lead itself carries @1481 as an unresolved
forced contradiction (red-team territory).

## Follow-ups proposed (for supervisor queuing)

1. `val-91-pp-adj` (P2): name 91's class at the 16-91 x2 windows (@538/@1371).
   Past participle selects 'a' ("m'a [pp]" passé composé); adjective selects
   'est' ("m'est [adj]"). Cleanest remaining 'a'/'est' discriminator.
2. `reseg-1481-98` (P2): @1481 forces the finite-verb class itself. Seek a
   byte-evidenced clause boundary or re-segmentation of "82 16 98 62";
   if none, escalate to red team — the "24/28 fit" claim overcounts.
3. `est-16-877-confirm` (P3): re-test @877 once 77's value is decided. If
   77='le' holds, "[49] a le" becomes a forced contradiction of 16='a'
   (currently conditional on the provisional tier).
