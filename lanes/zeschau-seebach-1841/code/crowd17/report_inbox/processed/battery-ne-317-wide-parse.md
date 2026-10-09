# Battery report: ne-317-wide-parse — full @314-325 clause re-parse

Target: `ne-317-wide-parse`. Claim: full @314-325 clause parses under standing values with alternate word boundaries.
Date: 2026-10-08. Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`),
parsed like `code/side-keyhunt/repair_parse.py` (re-implemented inline; parse
asserted n=1847). Never used `canonical.py`. R5005, sealed gates, red-team
adjudication queue untouched. No data invented.
Lock: `code/crowd17/next-token/locks/ne-317-wide-parse.lock` created
2026-10-09T01:41:13Z; no prior lockfile (no stale-lock note needed).

## Bar (verbatim, pre-registered from battery-queue.json, BEFORE testing)

"one grammatical parse with <=1 new-value assumption; else confirm the fence"

Numbered clauses:

1. Produce ONE grammatical parse of @314-325 ("45-64-59-32-94-06-11-92-60-15-63-71")
   under standing values with alternate word boundaries, using at most ONE
   new-value assumption.
2. Failing that, CONFIRM the fence: show the 94-06 residual stands fenced at
   the wide-clause level, with stated cause for each rejected boundary.

## Method

Re-derived the @314-325 window and the 94/06 censuses from the repaired
stream. Enumerated every binary word-boundary placement across 32-94-06-11
and tested each against standing values: banked GT (11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois,
79=tout, 00=pour, 84=on, 47=ce, 45=ce A11); provisional (59=est, 77=le);
battery promotes (94=ne STRONG LEAD R17-001, 06=ent, 12=n, 48=e, 30=pas,
32=verb lexeme with past-participle forms per verb-32 PROMOTE,
92=verb subset-scoped per verb-92-subset PROMOTE). One-assumption
candidates tested in §"Single-assumption sweep". 1841 diplomatic French only.

## Window-level evidence (@-offsets)

- **@314-325** (re-derived): `45 64 59 32 94 06 11 92 60 15 63 71`
  = "ce(45,A11) qui(64) est(59,prov) [32] ne(94) ent(06) la(11) [92] [60]
  [15] [63] [71]". Wider: @310-313 "84-24-37-78" = "on(84) [24] [37-78]"
  (w1-314-rebar: infinitive complement, word-internal ending at 78);
  @326-332 "10-01-19-00-92-50-45" = "[10][01][19] pour(00) [92] [50] ce(45)".
- **94 census (n=37, re-derived)**: followers 82x4, 74x3, 59x3, 52x3,
  92x2, 24x2, rest singles. **94-06 occurs exactly once (@318): hapax
  confirmed (1 of 37).**
- **32-94 x1, 32-94-06 x1** on the stream (both = this @317-319 window).
- **Standing left edge (fresh, not re-litigated)**:
  dict-313-w1-adjudicate PROMOTE (2026-10-08): @313 parses 'ce qui',
  45@314='ce' (A11 two-word exception); 'verdict qui' reading dead.
  verb-32 PROMOTE (2026-10-08): 32 = one verb lexeme; @317 is a
  past-participle window, "est [32](e)", clause 2 fencing @317's 'ne 06'
  with stated cause. So @314-317 = "ce qui est [32-participle]" parses
  cleanly — the clause's LEFT half is settled; the residual is @318-325.
- **Standing right side**: 92 noun VALUE killed (prenne-92-noun KILL, noun
  arm only; 92=verb subset lead stands); 60 masculine-noun KILLED,
  masculine-adjective KILLED, {60,68} homophone KILLED (verb-60 NULL leaves
  verbal open); 63 verb-shaped lead-level ("63 00" x4).

### Boundary enumeration across 32-94-06-11 (all fail)

1. **32 | 94 | 06 | 11** ("[32] ne ent la"): gate-killed at kill grade —
   "ne ent" = negator + bare ending, no stem (ne-06-317-gate readings a/b/c
   all FAIL).
2. **32-94 | 06 | 11** ("[32]ne" + "ent la"): "[32]ne" is a viable word
   shape (-ne final, cf. 70-12-94="prenne" fence), but "ent la" is not
   French — 06="ent" cannot stand before 11="la" as a word ("entla" void;
   ent-06 battery fenced @318-320, "stem slot filled by non-stem").
3. **32 | 94-06 | 11** ("[32]" + "neent" + "la"): "neent" is not a French
   word (gate reading b: "n'ent" void; unelided "neent" void).
4. **32 | 94 | 06-11** ("[32]" + "ne" + "entla"): "entla" void.
5. **32-94-06 | 11** ("[32]nent" + "la"): "[32]nent" is a viable 3pl-verb
   shape ("[stem]nent", cf. 70-12-94-06="prennent"), BUT @317 is promoted
   as "est [32-participle]" (verb-32, strong) — re-reading 32-94-06 as a
   3pl verb contradicts that promote (never-downgrade), and "est" + 3pl
   verb is ungrammatical regardless.
6. **32 | 94-06-11** ("nentla"): void. **06-11-92** ("entla[92]"): void.
   No French word spans these boundaries under banked letters.

### Single-assumption sweep (each candidate costs the one allowed assumption)

- **45="ceux"** ("ceux qui [32-94-06=3pl] la…"): contradicts
  dict-313-w1-adjudicate's fresh PROMOTE (45@314='ce', 'ce qui') —
  not available without red-team re-adjudication. REJECTED.
- **92=noun** ("la [92-noun]…"): contradicts prenne-92-noun KILL (noun
  value arm). REJECTED.
- **32=3pl stem** ("[32]nent"): contradicts verb-32 PROMOTE (@317 =
  "est [32](e)" participle, strong). REJECTED (never-downgrade).
- **60=verb** (verb-60's open arm): "la [92] [60-verb]" still
  ungrammatical — "la [92]" has no parse under the standing 92=verb lead,
  and this assumption does not touch the 94-06 blocker. INSUFFICIENT.
- **15="de/à"** ("[60] de [63-inf]"): 15-33 x2 / 15-63 suggest
  preposition-before-infinitive shape, but the 94-06 blocker is upstream
  of it — the clause still has no grammatical spine. INSUFFICIENT.
- **63=verb** (lead-level): same — does not repair 94-06. INSUFFICIENT.
- **94 positional split** (negator vs word-final syllable): red-team venue
  only (§7; ne-ce-1169's redteam-94-functional-split follow-up). NOT
  AVAILABLE at battery level.
- **59≠"est"**: 59="est" is provisional but budgeted into the fresh
  dict-313 promote ("ce qui est [32]" with 59 provisional); no evidence
  for a rival 59 value on this window. REJECTED as unmotivated.

No single assumption within battery authority yields a grammatical parse.
Every escape route either contradicts a standing verdict/kill/promote or
leaves the 94-06 hapax unparsed.

## Per-clause pass/fail

1. One grammatical parse with ≤1 new-value assumption: **FAIL** — no
   parse exists within the budget (boundary enumeration § + assumption
   sweep §; the 94-06 hapax is the load-bearing blocker and every repair
   contradicts standing verdicts or is red-team-gated).
2. Confirm the fence: **PASS** — the 94-06 residual stands fenced at the
   wide-clause level. Cause: hapax (1/37 94-followers, re-derived); all
   three local readings kill-grade dead (ne-06-317-gate); all alternate
   boundaries lexically void under banked letters (enumerated above);
   the only structural repairs (45="ceux", 92=noun, 32=3pl-stem, 94 split)
   are barred by standing promotes/kills or §7. The clause parses cleanly
   through @317 ("ce qui est [32-participle]", promoted) and the fence
   begins exactly at @318.

## Adverses (from queue; answered, none ignored)

- "94-06 is 1 of 37 94-followers": CONFIRMED on the repaired stream
  (94 n=37 re-derived; 94-06 x1 @318; 32-94 x1; 32-94-06 x1).
- "word-boundary hypotheses constrained by banked letters": HONORED —
  every boundary placement tested against banked GT values only
  (11=la, 45=ce, 64=qui, 94=ne, 06=ent); no boundary requires an
  unbanked letter string.

## Verdict

**kill** — the claim is falsified at the wide-clause level: no grammatical
parse of @314-325 exists under standing values with ≤1 new-value
assumption, and the fence is confirmed with stated cause per boundary.
@314-317 ("ce qui est [32-participle]") stands as promoted; the fenced
residual is exactly @318-325, load-bearing on the 94-06 hapax. This does
not downgrade dict-313-w1-adjudicate, verb-32, verb-92-subset, or
prenne-92-noun — it is consistent with all four.

## Follow-ups (kills close; none queued by this worker)

- NOTE for supervisor: ne-06-317-gate proposed gated follow-up
  **hapax-94-06-rerun** ("re-test @317 if verb-32 or a 32-value promotion
  lands"). Its trigger has now fired (verb-32 PROMOTE landed 2026-10-08),
  but its bar is NOT met: verb-32 clause 2 FENCED @317's 'ne 06' with
  stated cause rather than un-fencing it — the new 32 value does not change
  the parse of "94-06-11" vs the current fence. Recommend the supervisor
  mark hapax-94-06-rerun's gate condition evaluated-and-closed, not
  re-queued, unless the red team re-opens 94's positional split.

## Standing constraints observed

Did not touch R5005, sealed gates, or the red-team adjudication queue. Did
not use `canonical.py`. No numbers invented: n=1847 asserted; 94 n=37,
94-06 x1, 32-94 x1, 32-94-06 x1 all re-derived. No standing verdict
downgraded or overwritten. No polyvalence declared. 1841 diplomatic French
throughout.
