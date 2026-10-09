# Battery verdict: val-61-premier

**Verdict: PROMOTE (locus-level)** — "61 40 17" @1556 reads **"première fois"**.
61 = "premier" (single-group spelling of 70-82-34-29) at this locus. 61's GLOBAL
value stays fenced — val-61-contact's KILL of any global 61 value stands and is
not re-litigated here (follows the cela-69-11-word locus-promote precedent).

## Target

- id: `val-61-premier` (priority 2)
- claim: narrow ordinal bar: "61 40 17" @1556 = "première fois"
- evidence: battery-val-61-contact.md null/kill follow-up #1
- adverses: none stated

## Bar (verbatim from battery-queue.json)

61 substitutes "70 82 34 29" in crib-grade structural parallel to the flagship
"la premiere fois"; fence @223/@1510/@367 out of scope

## Numbered pass/fail clauses (pre-registered before testing — bar not modified after data)

1. **Clause 1 (substitution):** PASS iff 61 at @1556 substitutes the four-group
   "70 82 34 29" ("pre"+"m"+"i"+"er") with byte-exact spelling "61"+"40"+"17" =
   "première"+"fois", in structural parallel to the flagship crib
   "11 70 82 34 29 40 17".
2. **Clause 2 (fence @223):** PASS iff @223 is fenced out of scope with stated cause.
3. **Clause 3 (fence @1510):** PASS iff @1510 is fenced out of scope with stated cause.
4. **Clause 4 (fence @367):** PASS iff @367 is fenced out of scope with stated cause.

Verdict rule: **promote** iff clauses 1–4 pass. **kill** iff @1556 forces the
reading false on standing values. **null** otherwise, with 1–3 follow-ups.

## Method

Read BATTERY-PROTOCOL.md §1–§8 in full before testing. Created
`code/crowd17/next-token/locks/val-61-premier.lock` on start (agent id +
2026-10-09T03:1x UTC); no stale lock present. Parsed the repaired 1,847-pair
stream from `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt` with the upstream byte-exact tokenization
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]`, same as
`code/side-keyhunt/repair_parse.py`). Verified 1,847 pairs / 96 types.
`canonical.py` never touched. R5005, sealed gates, and the red-team adjudication
queue untouched. Standing values held fixed per §7 (11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que pencil; 17=fois promoted).

## Window-level evidence (all byte-verified on the repaired stream)

### The locus — @1556 (row a8_01)

`... [1550]92 [1551]45 [1552]23 [1553]99 [1554]13 [1555]93 [1556]61 [1557]40(e)
[1558]17(fois) [1559]11(la) [1560]26 [1561]30 ...`

- Spelling: 61 + 40("e", pencil GT) + 17("fois", promoted) = "premiere fois".
  In 1841 orthography, "première fois".
- The flagship crib (manuscript-gloss-anchored, row a5_03 repair): "11 70 82 34 29
  40 17" = "la" + "pre"+"m"+"i"+"er"+"e" + "fois". 61 substitutes exactly the
  four groups 70-82-34-29 ("premier") — one group vs four groups, same letter
  sequence. This is the lane's analytic-vs-syllabic duality (cf. 94="ne" vs
  12-48="n"+"e").
- **Clause 1: PASS.** Distributional facts:
  - "61 40" bigram occurs exactly **once** stream-wide: @1556. The "premier"+"e"
    composition is unique to this window.
  - "40 17" ("e"+"fois") occurs exactly **twice** stream-wide: @1039 (flagship)
    and @1556. The right edge is byte-identical to the flagship.
  - The full analytic "70 82 34 29 40 17" occurs exactly once: @1035 (flagship).
  - No standing value contradicts the locus: 40="e" and 17="fois" are the only
    valued neighbors, and both compose. Left neighbor 93 is unvalued (no
    contradiction possible); right context "11 26 30" ("la [26] pas") is an
    independent clause edge, not part of the locus.
- Row context: "43 00 46 70 12 94" closes row a8_00; a8_01 opens "92 45 23 99 13
  93" then the locus. The locus sits clause-medially; "première fois" reads as
  the temporal NP. The missing "la" (vs flagship "la première fois") is noted
  but not kill-grade: the bar tests the substitution parallel, and bare
  "première fois" is not forced ungrammatical by any standing value.

### Fenced windows (stated cause each)

- **@223 ("89 61 96 87 46") — fenced.** val-61-contact's Frame B showed this
  window needs 89's class to parse 61 at all (verb vs object-noun arms); 89's
  class is unresolved. The locus claim makes no assertion here. **Clause 2: PASS
  (fenced).**
- **@1510 ("12 61 59 39") — fenced.** val-61-contact's Frame C forces any GLOBAL
  61 value into the clitic/adverb class ("n' __ est"); that KILL stands and this
  battery does not re-litigate it. Boundary note: "41 12" (@1509–1510) may
  complete "en", making "n" word-internal — the window's segmentation is
  independently open. **Clause 3: PASS (fenced).**
- **@367 ("49 61 70 17") — fenced.** "premier"+"pre"+"fois" is ungrammatical as
  a word sequence under the standing values (70="pre" GT, 17="fois" promoted);
  the 49/61/70 boundary is unresolved, so this window is a genuine residual
  against any 61="premier" extension — left as residual, out of scope for the
  locus claim. **Clause 4: PASS (fenced).**

## Per-clause results

1. Substitution at @1556: **PASS** (byte-exact, unique "61 40", flagship-identical
   "40 17" right edge, no standing-value contradiction).
2. @223 fenced with cause: **PASS**.
3. @1510 fenced with cause: **PASS**.
4. @367 fenced with cause: **PASS**.

**Verdict: PROMOTE (locus-level).** "61 40 17" @1556 = "première fois".
Explicitly NOT promoted: 61="premier" as a global value (val-61-contact KILL
stands); 93's value; the "11 26 30" right-edge parse.

## Follow-ups proposed (for supervisor queuing)

1. `duality-61-7034-pattern` (P2) — 61 vs 70-82-34-29 is the lane's second
   documented one-group-vs-many analytic/syllabic duality (after 94 vs 12-48
   "ne"). Census whether other 61 windows (esp. 61-94 @577/@1168) show
   conditioned one-group behavior; escalate the duality pattern to the red team.
2. `reseg-367-4961-bound` (P3) — resolve the 49/61/70 boundary at @367; the
   "premier pre fois" residual is the sharpest anti-leg against any 61 extension.

## Bookkeeping

- `battery-queue.json`: `val-61-premier` queued → verdict/promote (temp-file +
  rename, own entry only, pre-write assert confirmed no prior verdict, JSON
  re-validated).
- Lock created on start, deleted on completion. No standing verdict contradicted
  or downgraded. R5005, sealed gates, red-team queue untouched.
