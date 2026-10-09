# Battery verdict: reseg-553-retry

- Target id: `reseg-553-retry`
- Claim: "@553 residual '59 34' ('est-i') with 86='voi' ('pour voir est-i fois')"
- Date: 2026-10-09
- Worker: battery worker (subagent aeaef377-6fee-4c7c-a6bc-6a6101196faa)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`). `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/reseg-553-retry.lock`
  (created 2026-10-09T07:00:23Z, no prior lock; deleted on completion).

## Bar (verbatim, pre-registered BEFORE testing)

"demonstrate a parse of '59 34' as 'est'+'i'/'est'+'y' with grammatical
continuation, or fence '59 34 17' as a genuine residual with stated cause"

Restated as numbered clauses (fixed before testing, not modified after):

1. (C1) A parse of '59 34' as 'est'+'i' or 'est'+'y' is demonstrated AND
   its grammatical continuation parses in-window. PASS -> the residual
   resolves (promote-feed).
2. (C2) Else, '59 34 17' is fenced as a genuine residual with stated
   cause. PASS -> NULL (fence executed; the existential claim is not
   established but not kill-grade, since 59='est' is provisional and
   no window forces the parse false under all values).

## Method

1. Re-derived the repaired stream in-session: 1,847 pairs, 96 types
   asserted. Located the locus byte-exact.
2. Tested every 'est'+'i'/'est'+'y' candidate form against 1841 French
   with only standing values (banked GT 34='i'; provisional 59='est';
   promoted 17='fois'; 86's wordhood at @553 adopted from
   reseg-86-553-889, not re-litigated).
3. Checked the row's phase status against battery-phase-likelihood-row-sweep.
4. Did not re-litigate 86's wordhood (brief: orthogonal).

## Window (re-derived, 0-based @-offsets)

@546-562: `46 24 47 46 55 81 00 86 59 34 17 86 | 94 59 30 67 11`
(row a3_01 through @557; a3_01/a3_02 boundary between @557 and @558).

Target trigram: @554-556 = `59 34 17` ("est"-"i"-"fois").
Gloss under standing values:
"...que(46) [24] ce(47) que(46) [55] [81] pour(00) [86] est(59) i(34)
fois(17) [86] | ne(94) est(59) pas(30) et(67) la(11)..."

Distributional facts (re-derived): '59 34' is hapax stream-wide (1x);
'86 59' is hapax (@553 only); n(59)=27, n(34)=11, n(17)=15.

## Per-candidate results (prong A)

**(a) "est-il" (interrogative inversion).** FAIL. Inversion spells
e-s-t-i-l; the 'l' is absent. French elision/inversion is written in
this cipher via 82='m' (lane precedent, lere-296-rival); no 82 appears
at the locus, so no elision mark licenses a dropped 'l'. 17='fois'
(promoted) cannot supply the 'l'.

**(b) "est-y" (adverbial 'y').** FAIL at two levels. 34='i' is banked
pencil GT, so re-valuing 34 to 'y' is out of battery scope; and "est-y"
is not a French verb form in any register ("il y est" is the form).

**(c) Letter composition "esti-" into a host word.** FAIL. Candidate
hosts "estival" / "estime" find no continuation: following tokens are
promoted 17='fois' and 86 — no 'v'/'a'/'l' or 'm' available.

**(d) 34 as word-initial 'i'.** FAIL. '34 17' = "i"+"fois" = "ifois" —
not a French word.

**(e) Continuation check (independent kill of prong A).** Even granting
"est-il", the continuation '17'='fois' kills the parse: "est-il fois"
is ungrammatical in 1841 French (inversion needs a predicate), and
"fois" stands bare here — bare "fois" never occurs (needs
det/quant/num; class-71-adjective). So no 'est'+'i'/'est'+'y' reading
can achieve a grammatical continuation.

C1: FAIL (no clause passes).

## Fence (prong B)

'59 34 17' is fenced as a genuine residual. Stated cause:

1. '59 34' admits no licensed French parse under standing values:
   "est-il" needs the absent 'l' with no elision mark; 34 is banked
   'i' so no 'y'; letter-composition finds no host word.
2. The continuation independently fails: bare '17'='fois' (no
   det/quant/num) + "est-il fois" ungrammatical in any register.
3. Hapax contacts ('59 34' x1, '86 59' x1) give no second instance to
   triangulate.
4. Defect localizes to '59 34', not to 86's wordhood at @553
   (reseg-86-553-889; not re-litigated per the brief).
5. Phase: a3_01 is NOT among the 20 rival-phase-favoring rows in
   battery-phase-likelihood-row-sweep — phase-solid at battery grade.
   The fence holds on the canonical stream per protocol.

Caveat (load-bearing, stated not hidden): 59='est' is provisional.
If 59's value ever changes, the fence re-opens — the residual's
unparseability is conditioned on the provisional gloss.

C2: PASS (fence executed with stated cause).

## Verdict: NULL

The bar's parse-demonstration prong fails at every candidate; the
fence prong fires. NULL per protocol §4 (inconclusive: no window
forces the existential claim false under all possible 59 values, and
59 is provisional). No standing red-team verdict contradicted or
downgraded; §7 intact. No polyvalence declared.

## Follow-up targets (nulls regenerate work)

1. **reseg-553-59value** (P3): re-test '59 34 17' iff 59's value
   changes from provisional 'est'. The fence is load-bearing on the
   59='est' gloss; a new 59 value re-opens the trigram. Bar: the new
   59 value parses '59 34' with grammatical continuation, or the
   fence re-executes.
2. **reseg-553-offset1** (P4): offset-1 constraint sweep of row a3_01.
   a3_01 is phase-solid by likelihood but the sweep is statistical;
   a constraint sweep hardens or dissolves the residual. Bar:
   constraint-clean across the row under offset-1, or the residual
   re-fences on the canonical stream.
3. **estil-corpus-1841** (P4): 1841 diplomatic-French corpus check for
   any attested "est-i[l]" truncation or poetic inversion form.
   Closes the elision objection conclusively. Bar: >=1 attested form
   with citation, or certified none.
