# Battery report: dict-45-w4-adjudicate — W4 (@1164) under the word-medial rule

- Target id: `dict-45-w4-adjudicate` (priority 2, status queued)
- Claim: decide 45 at W4 (@1164, '21 67 78 45 13 55 61') under the word-medial rule with a stated follower parse
- Worker: b53e0ed1-8fca-4d97-846b-68137b9b83f0
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types re-derived in-session before testing).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/dict-45-w4-adjudicate.lock (no prior lock existed; deleted on completion).

## Bar (verbatim, pre-registered before testing)

"state the follower parse (13-55-61 coordinated from dict-frame-78-45-13-55-61); W1-W3 classified, W4 is the last unclassified 78-45 window"

Numbered pass/fail clauses (frozen before judging):

1. The follower parse (13-55-61) is stated, coordinated from
   dict-frame-78-45-13-55-61 (and its null successor name-13-55-61) — not re-run.
2. W1–W3 are classified per prior adjudications; W4 (@1164) is the last
   unclassified 78-45 window (verified against the stream and the record).
3. W4 is adjudicated under the word-medial rule ("45='dict' iff 78
   word-MEDIAL", R18-026 evidence package, UNADOPTED) — evidence only, no
   positional declaration at battery level (§7).

Adverses: "circle-break left W4 fenced as residual; coordinate with
dict-78-45-wordbound; section 7 -- no positional declaration at battery
level"

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types, byte-exact).
2. Census: 78-45 loci at 0-based 78-positions @313, @573, @982, @1164 (exactly 4, as in
   dict-78-45-wordbound; byte-confirms).
3. W4 window re-derived, not cited from memory (@1156-1173, all row a6_09 except @1173):
   `80 17 77 | 82 44 83 21 67 | 78 45 | 13 55 61 | 94 87 83 21`
   i.e. 0-based 1162=21, 1163=67, 1164=78, 1165=45, 1166-1168=13-55-61, 1169=94, 1170=87.
4. Coordinated (not re-run): verdict45-value (W3 fenced neutral; this target = its follow-up #1),
   dict-frame-78-45-13-55-61 (null: clause 1 FAIL — 13-55-61 unnameable),
   name-13-55-61 (null 2026-10-08: unnameable stands), dict-78-45-wordbound (null:
   boundary holds at W2-W4, W1 two-word exception — escalated, undeclared),
   dict-45-circle-break (null: W4 double-residual within two-token scope),
   battery-rpos-w1-exception / R18-026 (refined rule candidate, W4 UNDETERMINED),
   R18-014 (45="ce" installed at W1 @314).
5. Standing values used: §7 banked (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que)
   and granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47="ce"
   allophone-tier); 78="ver" is LEAD (R16-005), not settled; A11 45="ce" HOLD stands;
   67 et/veut sole true polyvalence with positional rule (67="veut" iff follower
   infinitive-shaped). The word-medial rule ("45='dict' iff 78 word-MEDIAL") is
   UNADOPTED — R18-026 granted it as evidence package + §7-docket candidate only.

## Stated follower parse (13-55-61) — clause 1

Coordinated from dict-frame-78-45-13-55-61, re-verified byte-counts on the stream:

- 13-55-61 occurs exactly 2x stream-wide, at trigram-starts @575 and @1166 —
  i.e. exactly the two post-78-45 positions, nowhere else (global scan zero).
- 13->55 occurs exactly 2x = the two 5-grams (exclusive 45-specific contact).
- 61->94 x2 = the two 5-gram windows (W2 @573, W4 @1164); 61 otherwise scattered (n=18).
- 94-87 bigram: 1/1,847 = this window only (@1169-1170) — stream-unique hapax.
- name-13-55-61 returned null (2026-10-08): no candidate French word survived
  cross-window triangulation; the unit stays unnameable.

**Stated parse:** 13-55-61 is a post-78-45-exclusive positional unit (13->55 only in
the two byte-identical 5-grams), NOT a named French word. It is a syntactic
blank riding the boundary — it cannot lexically rescue any NP containing it.

## W1–W3 classification — clause 2

Verified against the record and the stream census:

- W1 @313: 45="ce" installed by R18-014 (dict-313-w1-adjudicate GRANT); R18-026
  rules the unconditioned R-pos falsified at W1 (78 word-FINAL there). Classified.
- W2 @573: 45='dict' conditional — R18-026 classification "consistent, conditional"
  on unsettled 78='ver' LEAD (R16-005); one-word 78-45 boundary promoted by
  verdict-w2-574-gate. Classified (conditional).
- W3 @982: fenced NEUTRAL under the w3-ceci circularity (verdict45-value);
  R18-026: UNDETERMINED. Classified as fenced-residual.
- W4 @1164: UNDETERMINED per battery-rpos-w1-exception ("double-residual ...
  residual, pending red-team polyvalence decision") and R18-026. No other
  78-45 window exists in the 1,847-pair stream. W4 is the last unclassified one.

## W4 under the word-medial rule — clause 3 (evidence only)

### Antecedent: is 78 word-medial at W4?

The rule's antecedent ("78 is word-MEDIAL" = 78–45 word-internal, 78 not
word-final) is the one-word 78-45 boundary at W4. dict-78-45-wordbound held the
boundary at W2-W4 — but returned NULL and escalated the boundary to the red
team (value arm + positional declaration both need red-team action). At battery
level the mediality of 78@1164 is therefore UNDECLARED. The antecedent is
conditionally available only: IF the red team declares the W2-W4 one-word
boundary, 78@1164 is word-medial (word-internal, not word-final) and the rule
fires toward 45='dict'.

### Consequent: what does 45='dict' compose at W4?

Under the rule (conditional on the undeclared boundary + unsettled 78='ver' LEAD):

- 67@1163 = 'et': §7 positional rule fires — 78 is noun-shaped (re-derived:
  77x7/47x5/37x4/11x2/87x2 determiner-predecessors, 21/31; 67->78 x4
  stream-wide @351/@491/@1163/@1842), not infinitive-shaped, so 67='veut' is
  excluded. (Dict-frame clause-3 fence coordinated: left-context blocker is
  21's open value, not 67.)
- 78-45 = "verdict" (one word, conditional on LEAD + boundary).
- Result: "...21 et(67) verdict(78-45) [13-55-61] ne(94) ce(87) [83]..."

Composition fails at battery level on three independent grounds:

1. **Determiner gap (kill-grade within scope).** "et verdict" = bare singular
   countable noun in argument position with no determiner — ungrammatical French.
   Verified on the window: no determiner-shaped token adjacent left of 78
   (nearest: 77='le' provisional at @1158, separated by 82-44-83-21-67, cannot
   govern 78). Row a6_09 is mid-row, mid-clause — the zero-determiner
   headline/fixed-expression rescue does not apply (coordinated with
   dict-45-circle-break's fencing).
2. **Follower unnameable.** The stated parse (above): 13-55-61 is a positional
   blank, not a word — it cannot complete or rescue the NP.
3. **Right-edge hapax.** @1169-1170 = "94 87" = "ne ce" under 94='ne' STRONG LEAD
   (R17-001) + 87='ce' granted — ungrammatical; 1/1,847 stream-wide. Owned by
   ne-ce-1169 (null); flagged here, not re-litigated.

The reverse arm (rule doesn't fire → 78 word-final → 45='ce') also fails at
battery level: two-word "et [78] ce [13-55-61]" needs a battery-level noun/verb
value for 78 (none — 78='ver' is LEAD-only) or the 'vers ce' reading (2 ungranted
assumptions: 78='vers' + 13-55-61 nounhood — over the <=1 budget per
dict-45-ce-rival-1165, coordinated).

### Falsification audit of the rule

The rule is NOT falsified at W4: the composition failure runs through an
unfired conditional (undeclared boundary + unsettled 78='ver' LEAD) — per the
fork-78-45-adjudication precedent, an unfired conditional is null, not kill.
The rule is also NOT confirmed: its W4 consequent does not compose under
standing values. R18-026's falsification audit ("no window contradicts it")
survives this battery. The W4 datapoint is handed to the red team as stated
evidence for the §7 decision: the rule's W4 prediction is unparseable under
standing values, which the red team can read as (a) the boundary not holding
at W4, (b) the follower blank bearing structure, or (c) a genuine residual —
all red-team territory.

## Per-clause pass/fail

1. Follower parse stated: PASS — 13-55-61 = post-78-45-exclusive positional unit,
   unnameable (name-13-55-61 null 2026-10-08); 13->55 x2 = the two 5-grams;
   94-87 hapax 1/1,847 at @1169.
2. W1–W3 classified / W4 last unclassified: PASS — W1=45='ce' (R18-014),
   W2=45='dict' conditional (R18-026/R16-005), W3=fenced neutral (verdict45-value),
   W4=UNDETERMINED (rpos/R18-026); stream census confirms exactly four 78-45 loci.
3. W4 adjudicated under the word-medial rule: FAIL at battery level — the
   antecedent (78 word-medial at W4) requires the escalated, undeclared
   boundary; the consequent (45='dict') yields an ungrammatical composition
   (determiner gap kill-grade in scope; follower positional-only; "ne ce"
   hapax). No decision possible at battery level; §7 respected, nothing declared.

Adverses:
- "circle-break left W4 fenced as residual": coordinated — consistent with
  dict-45-circle-break (null) and dict-45-ce-rival-1165; W4 stays fenced residual.
- "coordinate with dict-78-45-wordbound": done — the W2-W4 boundary is the
  rule's load-bearing antecedent; its null verdict + escalation is respected,
  not re-run.
- "§7 — no positional declaration": respected — no value declared for 45 or 78
  at W4; no polyvalence declared; the word-medial rule remains a candidate.

## Verdict: NULL

Headline: W4 cannot be decided at battery level. The word-medial rule's
antecedent at W4 is conditional on the red-team-escalated one-word boundary
(dict-78-45-wordbound null), and its consequent — "et verdict [13-55-61]"
— fails to compose under standing values (determiner gap kill-grade in scope,
unnameable follower, "ne ce" hapax). The rule is neither falsified nor
confirmed here (unfired conditional → null per fork precedent); W4 stays
fenced as the last unclassified 78-45 window, pending (a) the red-team §7
boundary declaration and (b) ver-78's resolution. No standing red-team verdict
is contradicted: R18-026 classified W4 UNDETERMINED — this battery agrees.

## Follow-ups (null regenerates work; all verified ABSENT from battery-queue.json 2026-10-09)

1. **w4-det-gap-census** (priority 2). Claim: the W4 determiner-gap is lane-law,
   not a one-window assertion. Bars: (a) census all 67='et' loci on the repaired
   stream (67->X); state which X are noun-valued under granted values; (b) the
   gap is law-grade iff zero bare-countable-noun-after-'et' compositions occur
   among decidable loci; (c) use only granted/banked values for the noun call.
   Evidence: this report (W4 @1162-1165). Adverses: 67->78 x4 (noun-shaped 78);
   21's open value (left edge).
2. **w4-left-edge-21-83** (priority 3). Claim: the W4 left edge @1158-1163
   ("77 82 44 83 21 67") decides whether 'et' coordinates an antecedent NP.
   Bars: (a) parse the 6-gram under standing values with 21 and 83 named or
   fenced with stated cause; (b) if 'et' coordinates a named antecedent NP,
   state whether the coordination rescues or deepens the W4 residual; (c)
   coordinate with dict-frame clause-3's fence (21's value = the blocker).
   Evidence: this report. Adverses: 83='de' lead (R17); 77='le' provisional.
3. **w4-78-mediality-gate** (priority 3). Claim: re-test the rule's antecedent
   at W4 once the red team adjudicates the W2-W4 one-word 78-45 boundary
   (dict-78-45-wordbound escalation). Bars: (a) if the boundary is declared
   word-level at W4, re-run the W4 decision under the word-medial rule with
   this report's determiner-gap finding as input; (b) if the boundary is
   rejected at W4, record 45@1165 under the two-word parse per the declared
   segmentation; (c) declare nothing — report the recomposition to the red
   team. Evidence: this report (antecedent analysis, determiner-gap kill-grade
   finding). Adverses: ver-78 still LEAD (gate is boundary-only, not value).

## Reproducibility

Stream: `code/side-keyhunt/repair_parse.py` (`load_rows()` + `parse(rows,
repaired_offsets.json)`), run in-session 2026-10-09: 1,847 pairs / 96 types;
78-45 loci (0-based 78-positions) [313, 573, 982, 1164]; 13-55-61 trigram starts
[575, 1166]; 13->55 x2; 94-87 x1 (@1169); 67->78 x4 (@351/@491/@1163/@1842);
78 predecessors {77:7, 47:5, 37:4, 67:4, 11:2, 87:2, 16:1, 50:1, 86:1, 80:1,
98:1, 84:1, 17:1} (n=31). No writes outside this report, the queue edit (own
entry only, temp-file + rename, re-read before write), and the lockfile (deleted).
