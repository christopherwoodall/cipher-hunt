# Battery report: ceci-984-195-pair

- Target id: `ceci-984-195-pair`
- Claim: "bound '-ci' holds at the two surviving loci @984 and @195"
- Date: 2026-10-08
- Worker: battery worker (session 6cd55bfb-de82-4b72-8515-cb8525de601f)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  All @-offsets are 0-based repaired-stream indices of the 01 token.
  canonical.py never used. R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/ceci-984-195-pair.lock (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"@984 AND @195 both parse as 'ceci' in full context once [21]'s class resolves at @195; promote the restricted reading ('-ci bound, ce-contexts only, confirmed at 2 loci') iff both parse; kill the narrowed claim iff @195 forces 'ceci' false once [21] resolves"

Numbered pass/fail clauses (restated before testing, not modified after):

1. @984 parses as 'ceci' in full context.
2. @195 parses as 'ceci' in full context with [21]'s resolved class applied
   (21 = NOUN, class-level, F122 battery-promote via de-frame-21-class).
3. Promote the restricted reading ('-ci bound, ce-contexts only, confirmed
   at 2 loci') iff clause 1 AND clause 2 pass.
4. Kill the narrowed claim iff @195 forces 'ceci' false once [21] resolves
   (i.e., a grammatical full-context parse exists in which 47-01 is NOT
   'ceci' and is cleaner than the ceci reading).
5. Adverses answered: (a) A11 dependency at @984 (45='ce' HOLD) stated, not
   hidden; (b) fork-78-45 watch item checked (ver-78 status determines
   whether the @984 leg is threatened).

## Method

1. Re-derived the repaired parse in-session (1,847 pairs confirmed).
   Window bytes verified in-stream, not cited from memory:
   @983-986 = `45 01 24 89` (row a6_01); @194-198 = `47 01 21 60 08`
   (row a2_00). Both match ci-bound-01 and feeder-ceci-47-45 exactly.
2. Applied standing verdicts only: 21=NOUN class (F122, de-frame-21-class
   PROMOTE 2026-10-08, battery-level, value unnamed); 45='ce' A11 HOLD;
   47='ce' A4 granted; 24=finite modal verb (ne-24-profile PROMOTE,
   class-level); 89=verb-frame (A8); 06='ent' (round-17 promote);
   76=noun lead; 67 et/veut sole polyvalence with positional rule
   (67='veut' iff follower infinitive-shaped); 60 adjective single-value
   KILLED (adj-60), verb arm NULL (verb-60, verb-60-ent — value unnamed);
   08 class open (stem-08 queued); 01 valueless outside ce-contexts
   (ci-bound-01 clause 2).
3. Tested each locus for a grammatical full-context parse under the bound
   '-ci' reading; enumerated rival parses for the kill clause.
4. Checked for contradictions with standing red-team verdicts (A11, A4,
   §7 polyvalence law, round-17 adjudication).

## Window-level evidence

### Clause 1 — @984 (row a6_01): `45 01 24 89`

Bytes @976-992: `01 00 92 07 76 47 78 45 01 24 89 48 01 76 49 24 26`.
Parse: "…ce(47) [78] ceci(45-01) [24-modal] [89-inf]…" =
"ceci [modal] [infinitive]…" ("ceci peut [inf]"-shaped). Clean and
grammatical — the one clean ceci+verb window, as in ci-bound-01 W1 and
feeder clause 2.

- Adverse (a): depends on 45='ce', the A11 HOLD (allophone tier), not a
  promotion. Stated explicitly. Corroboration since ci-bound-01:
  dict-313-w1-adjudicate (2026-10-08, PROMOTE) adjudicated @313 for
  'ce qui' with 45@314='ce' under the same A11 HOLD — the hold is
  strengthened, not weakened.
- Adverse (b): fork-78-45 clause (a) says IF 78='ver' promotes, 45='dict'
  applies at the 78-45 windows including @982-983. ver-78 is a LEAD
  (promote rejected, round-17); dict-45 is NULL. Antecedent false; A11
  stands here. If ver-78 ever promotes, this leg must be re-examined.

Result: PASS (conditional on the A11 HOLD, as in both parent batteries).

### Clause 2 — @195 (row a2_00): `47 01 21 60 08`

Bytes @187-203: `16 00 66 24 87 98 56 47 01 21 60 08 67 76 87 11 92`.
With standing values: "…[24-modal] ce(87) [98] [56] ceci(47-01) [21-N]
[60] [08] et/veut(67) [76-N] ce(87) la(11) [92]…".

21's resolved class is NOUN (F122). 21 therefore cannot fill a verb
slot — the provisional "[21] in the verb slot" reading that ci-bound-01's
W2 left open is dead under the promotion (as feeder-ceci-47-45 already
recorded; re-verified here against the current queue state — no
intervening verdict has overturned F122; name-21-obj went NULL on naming
a value, which does not touch the class).

Candidate full-context parses of "ceci [21-N] [60] [08] …":

- (i) 60 as finite verb: "ceci [noun] [verb]" — wrong word order for a
  plain clause. Ungrammatical.
- (ii) 60 as adjective: "ceci [21-N] [60-adj]" is a verbless NP fragment.
  The dislocation rescue ("ceci, [21] [60-adj] [08] veut [76]") needs
  (a) 60 adjectival — single-value adjective KILLED (adj-60), and any
  adjective/verb polyvalence is a red-team-only declaration per §7;
  (b) 08 as object — 08's class open (stem-08 queued); (c) 67='veut' —
  fails the §7 positional rule here since @200=76 is noun-shaped (76=noun
  lead), so 67='et'; (d) unresumed dislocation of "ceci". Four unstated
  assumptions plus a red-team act: not battery grade.
- (iii) 60 as infinitive: "ceci [noun] [inf]" — no governing verb; the
  exclamatory-infinitive reading needs "[inf] ceci" order. Ungrammatical.
- (iv) Dislocation with 60 as verb: "Ceci, [21-N], [60-V] [08] et [76]" —
  needs 60 verb-class (verb-60 and verb-60-ent both NULL, value unnamed;
  class not granted) + 08 as complement (open) + unresumed dislocation.
  ≥2 ungranted assumptions: not battery grade for a promote.

The "21-60" bigram's other windows (@118, @171, @231) offer no rescue:
@171's "12-48 21 60" ("ne [21] [60]") is itself fenced to
frame-87-83-cede by de-frame-21-class and does not parse under 21=NOUN
either.

Result: RESIST with stated cause. 21=NOUN kills the only clause shape
("ceci [21-verb]") under which the bigram's downstream context parsed;
60's slot cannot be stated at battery grade (adjective killed
single-value, verbal unnamed, polyvalence red-team-only); 08 open.
Per the brief's NOTE, the class-level resolution is insufficient for the
@195 subject slot — fenced here with stated cause rather than
over-claimed. The resistance is localized to [21]/[60], downstream of
the 47-01 bigram; it does not force "ceci" false at the bigram itself.

### Clause 4 — kill check: does @195 force 'ceci' false?

A kill needs a grammatical rival parse with 47-01 ≠ 'ceci'. Candidates:

- 01='faisant' ("ce faisant [21]"): killed generally by
  battery-ci-01-value. Dead.
- 01 as independent token value: ci-bound-01 clause 2 swept all 24
  non-ce windows — 01 is valueless elsewhere; no window forces a token
  value on 01. No rival value exists to deploy here.
- 47 ≠ 'ce': 47='ce' is A4-granted (allophone tier). No rival.

No grammatical full-context parse of @190-205 exists under ANY reading
of 47-01 (the window is a residual, like @345/@1029 in ci-bound-01) —
so a fortiori none exists that forces 47-01 ≠ 'ceci'. The narrowed claim
is under-evidenced at @195, not refuted.

Result: no kill. (Precedent: ci-bound-01's kill standard — "kill iff a
window forces the claim false" — is not met.)

## Per-clause pass/fail

1. @984 parses as 'ceci' in full context: PASS (conditional on A11 HOLD;
   fork-78-45 vacuous while ver-78 stays a lead).
2. @195 parses as 'ceci' in full context with 21=NOUN: RESIST (stated
   cause: 21 cannot take the verb slot; 60's slot unstated at battery
   grade; 08 open; no candidate parse survives at battery grade).
3. Promote restricted reading iff 1+2: NOT MET — no promote.
4. Kill iff @195 forces 'ceci' false: NOT MET — no rival parse; no kill.
5. Adverses: (a) ANSWERED — A11 dependency stated with the
   dict-313-w1-adjudicate corroboration; (b) ANSWERED — fork-78-45
   checked, antecedent false (ver-78 = lead, promote rejected).

## Verdict: NULL

The restricted bound-'-ci' reading survives cleanly at @984 ("ceci
[modal] [inf]", A11-conditional) and remains bigram-compatible at @195,
but @195 does not parse in full context once 21's NOUN class is applied —
and @195 does not force 'ceci' false either. Under-evidenced, not
refuted. This independently re-derives feeder-ceci-47-45's verdict on
the current queue state (no intervening verdict changes the analysis:
verb-60/verb-60-ent went NULL, 76=noun lead is new, stem-08 still
queued).

No standing red-team verdict is contradicted or downgraded: A11 relied
on, not challenged; F122 (21=NOUN) used as granted at battery level;
§7 polyvalence law respected (no second polyvalence declared).

Dependencies: @984's leg is load-bearing on the A11 HOLD and on ver-78
staying unpromoted (fork-78-45 clause a). The @195 leg is load-bearing
on 60's and 08's classes (verb-60 NULL, stem-08 queued) — re-test when
either resolves.

## Follow-up targets (nulls regenerate work)

1. **slot-60-08-at-195** (priority 2): name 60's class at @197 and 08's
   class at @198 with the left edge "ceci [21-N]" fixed. Bar: produce a
   grammatical full-context parse of @190-205 with ≤1 ungranted
   assumption; promote the @195 ceci leg iff it parses; kill the @195
   leg (not the bigram) iff the named classes still leave no parse.
   Adverses: verb-60 NULL (value unnamed), stem-08 queued, §7
   polyvalence law (60 adjective/verb needs red-team act).
2. **disloc-ceci-corpus** (priority 3): is unresumed dislocated "ceci,"
   ("Ceci, [NP], [VP]") attested in 1841 diplomatic French? Bar: cite
   period corpus evidence for or against; if unattested, the
   dislocation rescue for @195 is dead and the @195 leg stays fenced
   as a neighbor-driven residual with stated cause. Adverses: none at
   battery level — red-team eyes welcome.
3. **rival-195-killpath** (priority 3): attempt ANY grammatical
   full-context parse of @190-205 with 47-01 ≠ 'ceci' (rival 01
   reading, re-segmentation, or 47 rival). Bar: produce the parse with
   byte-level windows; if one is found and is cleaner than the ceci
   reading, escalate to the red team as a kill-path for the narrowed
   claim; else record the attempt as a second negative leg for the
   kill clause. Adverses: 01='faisant' killed; 01 valueless elsewhere;
   47='ce' A4-granted.
