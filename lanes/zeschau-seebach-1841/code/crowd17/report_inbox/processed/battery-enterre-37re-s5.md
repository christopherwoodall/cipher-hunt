# Battery report: enterre-37re-s5

**Target:** `enterre-37re-s5` (P2)
**Date:** 2026-10-09
**Verdict:** KILL (uniform 37='re' as a candidate value; conditional — re-open iff 77≠'le')

## Bar (verbatim from parent brief; queue `bars` field is null)

Parent brief: "BARS: derive numbered bars from the claim before testing: (1) all cited windows parse under 37='re' with zero kill-grade contradictions; (2) @1815 reads as "enterre" or is fenced; (3) any contradiction of 're' is stated at kill grade."

## Bar restated as numbered clauses

1. All cited windows (@1815 "enterre", "59 37" ×6, "64 37" ×3, "37 78" ×4) parse under 37='re' with zero kill-grade contradictions.
2. @1815 reads as "enterre" or is fenced with stated cause.
3. Any contradiction of 're' is stated at kill grade.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/enterre-37re-s5.lock`
(2026-10-09T07:28:00Z; deleted on completion). Re-derived the repaired
1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs).
`canonical.py` never used. R5005, sealed gates, red-team adjudication queue
untouched. Standing values per §7: 11=la / 70=pre / 82=m / 34=i / 29=er /
40=e / 46=que (pencil); 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
84=on, 47=ce (granted/promoted); 59=est, 77="le" (provisional).
Offsets below are 0-based stream indices (lane convention); the claim's
"@1815" = 1-based @1816 = 0-based @1815 (the 06 of "06 29 37").

## Window-level evidence

**Cited-set completeness check.** n(37)=28. Cited: "59 37" ×6 at
0-based 528/624/912/1178/1443/1796 (37 at +1) ✓; "64 37" ×3 at
675/938/1632 (37 at +1) ✓; "37 78" ×4 at 312/414/475/1770 ✓;
@1815-window: 0-based 1815:06, 1816:29, 1817:37, 1818:01 ✓.

### @1815 "enterre" window — PASS (conditional)

Row a8_10: `1814:42 [1815:06] [1816:29] [1817:37] 1818:01`.
Under 37='re': 06('ent')+29('er')+37('re') = **"enterre"**, byte-exact
spelling of *enterrer* 3sg. Parse: "…[42-noun] enterre [01]…" —
grammatical (subject + 3sg verb + complement slot). Conditional on 42's
noun value and 01's object role (both open, unforced). No contradiction.

### "59 37" ×6 — six STRAINED FENCES, no kill-grade contradiction

59='est' is provisional. Under 37='re', "59 37" = "estre" (archaic
spelling of *être*, attested in classical French, anomalous in 1841
diplomatic prose) or "est" + "re-" prefix needing an open-valued
follower. Per window:

- @528 (`47 59 37 64`): "ce [44] est re qui [26]" — "estre qui"
  archaic; "est re-qui" impossible. FENCED (strained).
- @624 (`82 14 59 37 33 29`): "…[14] est re [33] er…" — conditional
  pass IFF 33 is a re- compatible participle tail ("est re[33]" =
  *être* + past participle, e.g. "est revenu"-shaped); 33's class is
  open. FENCED-CONDITIONAL.
- @912 (`64 83 59 37 96`): "qui [83] est re par" — no parse beyond
  archaic "estre". FENCED (strained).
- @1178 (`48 59 37 77`): "…[48] est re le [78]" — no parse beyond
  archaic "estre". FENCED (strained).
- @1443 (`68 59 37 64`): "…[68] est re qui" — no parse beyond archaic
  "estre". FENCED (strained).
- @1796 (`94 59 37 91`): "ne est re [91]" — no parse beyond archaic
  "estre". FENCED (strained).

None forces 37≠'re': the archaic "estre" is real French, and
conditional parses exist via open neighbors. Weak flank, not a kill.

### "64 37" ×3 — ONE KILL-GRADE CONTRADICTION (@676)

64='qui' is granted: "qui" must be followed by a verb.

- @676 (`674:03 [675:64] [676:37] 677:77 678:45`): "…[03] qui re le ce".
  Under 37='re': "re" is not a verb; "re"+"le" is not a verb;
  "re"+"le"+"ce" is not a French word; leftward "[03]quire" is not a
  French word; 64≠'qui' is unavailable (granted). The ONLY grammatical
  rescue is 77≠'le' (provisional) with 77 as a re- verb tail
  ("qui re[77-finite] ce" — e.g. 77='fait'/'çoit'/'dit' gives
  "qui refait/reçoit/redit ce", all grammatical). So @676 forces
  (37='re' ∧ 77='le') false. Per §7 both are standing constraints, but
  77='le' is the standing value and 37='re' is the candidate under
  test: the candidate loses the tie. **Uniform 37='re' is killed at
  @676, conditional on provisional 77='le' holding.**
- @938 (`937:21 [938:64] [939:37] 940:01`): "…[21] qui re [01]…" —
  conditional pass IFF 01 is a re- compatible verb stem
  ("qui repose/revient"-shaped); 01's value is open. No contradiction.
- @1632 (`1631:21 [1632:64] [1633:37] 1634:01`): same shape as @938 —
  conditional pass on open 01. No contradiction.

### "37 78" ×4 — conditional passes, one value tension flagged

- @312 (W1) and @475: F130 (battery-w1-314-rebar, PROMOTE) establishes
  37-78 word-internal as the COMPLETE infinitive complement of
  modal-24, 78 word-final. Under 37='re' the infinitive must be exactly
  "re"+78 — parses IFF 78 is a compatible re-infinitive tail
  ('dre'→rendre, 'ter'→rester, 'voir'→revoir, 'faire'→refaire).
  Conditional pass. **Tension flagged for S5:** 78's R16-005 lead is
  'ver', but "re"+"ver" = "rever" is not a French word ("rêver" has a
  circumflex). The 're' candidate and the 78='ver' lead are mutually
  exclusive at these two windows; 78's value is open, so no
  kill-grade contradiction — but S5 cannot hold both.
- @414 (`413:51 [414:37] [415:78] 416:49`): no modal-24 governor;
  conditional pass IFF "51-37-78" composes one word with internal "re"
  (51/78 open) or a governor is found. Fenced with cause.
- @1770 (`1769:26 [1770:37] [1771:78] 1772:62`): conditional pass IFF
  "37-78" composes with open neighbors (26/62 open). Fenced with cause.

## Per-clause pass/fail

1. **FAIL at kill grade.** @676 ("64 37 77" = "qui re le ce") forces
   (37='re' ∧ 77='le') false; the provisional standing value 77='le'
   wins the tie, so uniform 37='re' is killed. All other 13 cited
   windows parse (conditionally) or fence without kill-grade
   contradiction — the kill is single-window but sufficient.
2. **PASS.** @1815 reads "…[42] enterre [01]…" cleanly under 37='re'
   (conditional on open 42/01).
3. **PASS.** The @676 contradiction is stated at kill grade above,
   with its exact condition.

## Adverses

- "Coordinate with S5; 37's value is S5/red-team's to decide":
  ANSWERED. This battery kills only the 're' CANDIDATE (a parent-battery
  lead, never a standing verdict); it does not name 37's value and does
  not touch S5's fence (37="le" MEDIUM, round-7, already contradicted by
  other batteries and awaiting red-team). Packaged below for S5/red-team.

## Verdict: KILL

Uniform 37='re' is **killed** as a candidate value: @676 ("qui re le
ce") admits no grammatical parse under 37='re' + standing values, and
the sole rescue requires overturning provisional 77='le'.

**Explicit re-open conditions (all red-team/S5 venue):**
- 77≠'le' established at @677 (provisional overturn), which revives
  "qui re[77-verb] ce" parses; or
- red-team positional conditioning of 37 (note: @1815 needs 37='re'
  word-final, @312/@475 need it word-initial — simple
  initial/final conditioning does not separate them; "except after 64"
  conditioning would be ad hoc).

**For S5's docket:** the 're' candidate is eliminated, but the
@1815 "enterre" lead and the "37 78" re-infinitive frames remain live
phenomena needing a value for 37 — S5's open question is unchanged,
its candidate set is narrowed by one.

## Notes for the supervisor

- Kill verdict: no follow-ups required by protocol. Re-open conditions
  above are red-team-gated, not battery work.
- Scope limit: uncited 37 windows (e.g. @51 "79 37 11", @183, @385)
  were census-listed but not adjudicated — S5 owns the global question.
- Canonicality caveat: all cited rows carry unvalidated upstream
  offsets; verdict holds on the canonical stream per protocol.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/enterre-37re-s5.lock` created
  2026-10-09T07:28:00Z, deleted on completion.
- `battery-queue.json`: `enterre-37re-s5` queued → verdict/kill
  (temp-file + rename; pre-write assert confirmed no prior verdict;
  JSON re-validated; only this entry touched).
- R5005, sealed gates, red-team adjudication queue untouched.
  `canonical.py` never used. §7 intact.
