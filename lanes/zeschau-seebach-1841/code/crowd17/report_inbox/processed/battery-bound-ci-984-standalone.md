# Battery report: bound-ci-984-standalone

- Target id: `bound-ci-984-standalone`
- Claim: narrow the bound-ci claim to the single clean locus @984
- Date: 2026-10-08
- Worker: battery worker (session 9f9e6ab6-5bc6-4f35-9bd1-b95edbe71bf5)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  All @-offsets are 0-based repaired-stream indices. canonical.py never used.
  R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/bound-ci-984-standalone.lock (created at
  start, deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"promote-restricted iff @983-986 parses as ceci [24-modal] [89-inf] with the
A11 dependency stated and zero contradictions in +-10; the @195 leg stays
fenced per this battery"

Numbered pass/fail clauses (restated before testing, not modified after):

1. @983-986 parses as "ceci [24-modal] [89-inf]": 45='ce' (A11 HOLD),
   01=bound '-ci' (hypothesis under test), 24=finite modal verb
   (ne-24-profile PROMOTE, class-level), 89=infinitive verb-frame (A8 grant).
2. The A11 dependency is stated: the reading is explicitly conditional on
   45='ce' (A11 HOLD); 45's 'dict' rival is a lead (NULL batteries), not
   a promoted value.
3. Zero contradictions in ±10 (@974-994): no window in ±10 forces a reading
   incompatible with the ceci parse at @983-986.
4. The @195 leg stays fenced per this battery: not re-litigated; remains
   fenced per feeder-ceci-47-45 (resist with stated cause at [21]/[60]).

## Method

1. Re-derived the repaired parse in-session: 1,847 pairs, 96 unique groups
   confirmed. Window contents verified byte-level in-stream (not cited from
   memory): @973-996 =
   `51 45 08 01 00 92 07 76 47 78 45 01 24 89 48 01 76 49 24 26 30 03 60 67`,
   all within row a6_01 (row a6_02 starts at index 996 — no row boundary
   inside the locus or its ±10).
2. Re-derived the key censuses: 45-01 bigram is stream-unique at @983
   (count 1); 24-89 contacts x3 (@221, @985, @1497) — @985 is one of the
   three modal+infinitive-frame contacts.
3. Tested the locus parse and swept ±10 (@974-994) for contradictions,
   relying only on standing verdicts: 45='ce' (A11 HOLD), 47='ce' (A4
   granted), 24=finite modal verb class-level (ne-24-profile PROMOTE),
   89 verb-frame (A8 grant), 30='pas' (promoted), 00='pour' (A9 promoted),
   48='e' / 11='la' (ground truth), 77='le' (provisional), 78='ver'
   (NULL — fork-78-45 antecedent false), 45='dict' (NULL lead, not promoted).

## Window-level evidence

### Clause 1 — the locus @983-986: `45 01 24 89`

- 45 = 'ce' under the A11 HOLD (dependency stated, not hidden).
- 01 = bound '-ci' in the ce-context (the hypothesis under test; 01
  valueless elsewhere per ci-bound-01, which stands).
- 24 = finite verb, modal-shaped (ne-24-profile PROMOTE, class-level;
  value unnamed). At @985 it takes the infinitive-frame complement 89 —
  one of exactly three 24->89 contacts on the repaired stream
  (@221/@985/@1497), the modal+infinitive shape.
- 89 = verb-frame (A8 frames grant; value open) — infinitive-shaped
  complement.

Parse: "ceci(45-01) [24-modal] [89-inf]" = "ceci peut [inf]"-shaped.
Clean, grammatical, full coverage of the locus window.

Result: PASS.

### Clause 2 — A11 dependency stated

The parse is explicitly conditional on 45='ce' (A11 HOLD). 45's rival
'dict' is a battery-level lead (dict-45 batteries NULL; dict-313-w1-adjudicate
just promoted 'ce qui' at @313 under the same HOLD). No stronger claim
is made for 45 at this locus. Result: PASS.

### Clause 3 — ±10 contradiction sweep (@974-994)

Checked every group in `45 08 01 00 92 07 76 47 78 45 01 24 89 48 01 76
49 24 26 30 03` for a forced reading incompatible with the locus parse:

- @974=45 ('ce', A11 HOLD): consistent with the locus's own A11
  dependency. No contradiction.
- @975=08, @976=01: 08's class open (stem-08 queued); 01 valueless
  outside ce-contexts. Unparsed residue, not a forced rival. No
  contradiction.
- @977=00 ('pour' promoted): "…ce [08] [01] pour…" grammatical opener.
  No contradiction.
- @978=92, @979=07: open. @980=76 ('le' provisional): "…pour [92]
  [07] le…" unparsed but unforced. No contradiction.
- @981=47 ('ce' granted A4), @982=78 (open; 'ver' NULL): "ce [78]
  ceci…" — 78-45 at @982-983 is NOT forced word-internal: the two-token
  "verdict" reading was killed at kill grade (dict-45-ce-rival-1165);
  the 5-gram unit reading belongs to a different window
  (dict-frame-78-45-13-55-61, fenced as outside scope). 78 stands
  unparsed; it does not force a rival parse of 45 at @983. No
  contradiction.
- @987=48 ('e' ground truth): 48 is a single letter; no standing
  verdict forces 89-48 word-internal. "…[89-inf] e…" is an open
  boundary, not a contradiction.
- @988=01: non-ce-context 01 (48-01), valueless per ci-bound-01. Fenced,
  not a contradiction of the ce-context locus.
- @989=76, @990=49, @991=24, @992=26, @993=30 ('pas' promoted),
  @994=03: downstream clause "…[01] le(77) [49] [24] [26] pas [03]".
  Open and unparsed, but nothing in it forces the @983-986 window to a
  non-ceci reading. No contradiction.

Result: PASS — zero contradictions in ±10.

### Clause 4 — @195 leg fenced

Per the bar, the @195 leg is not re-tested here. It remains fenced per
feeder-ceci-47-45: 47-01 at @194-195 resists with a stated cause (21 =
NOUN promoted, cannot take the verb slot; 60's slot undeterminable at
battery grade). The fence is downstream of the 47-01 bigram and does not
touch the @984 locus. Result: PASS (fence preserved, not re-litigated).

## Per-clause pass/fail

1. @983-986 parses as "ceci [24-modal] [89-inf]": PASS.
2. A11 dependency stated: PASS.
3. Zero contradictions in ±10: PASS.
4. @195 leg stays fenced: PASS.

## Adverses

1. "A11 HOLD": ANSWERED. The dependency is stated as a condition of the
   restricted promotion, not promoted beyond HOLD. 45='dict' remains a
   NULL lead; if a future battery promotes it, this restricted result is
   conditional, not contradicted — the condition was explicit.
2. "fork-78-45 watch item (vacuous while ver-78 NULL)": ANSWERED.
   78='ver' is NULL (dict-45-w3-ceci NULL), so the fork's antecedent is
   false and the item is vacuous, exactly as the adverse states. The
   78-45 contact at @982-983 is additionally cleared: the two-token
   "verdict" reading is kill-grade dead (dict-45-ce-rival-1165) and the
   5-gram unit escape belongs to another window.

## Verdict: PROMOTE (restricted)

All bar clauses pass and both adverses are answered. Scope of this
promotion is restricted, exactly as the bar names it:

- RESTRICTED TO THE LOCUS: only @983-986 (`45 01 24 89`) is promoted as
  "ceci [24-modal] [89-inf]". This is not a promotion of the general
  bound-ci claim (01='-ci' elsewhere), of 01's value, or of 45's value.
- CONDITIONAL ON A11: the promotion holds only under 45='ce' (A11 HOLD).
  45's value is not promoted here.
- The @195 leg remains fenced per feeder-ceci-47-45; nothing in this
  battery changes its status.

No standing verdict is contradicted or downgraded: A4 (47='ce'), A11
(45='ce' HOLD), A8 (89 verb-frame), ne-24-profile (24 modal class),
the 21-noun promote, the 60-adjective kill, ci-bound-01 (01 valueless
elsewhere), the ver-78/fork-78-45 NULLs, and the dict-45 NULLs are all
relied on, not challenged. No red-team escalation needed — the A11
condition and the @195 fence are both stated, not hidden.

## Follow-ups

None required: this battery's verdict is promote-restricted, not null.
(The @195 fence already generated its follow-ups in feeder-ceci-47-45:
ceci-195-nounslot, slot-60-at-197.)
