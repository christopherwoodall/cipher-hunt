# Battery `15-value-id` — verdict: NULL (fence)

Worker: 1c6698bd-373b-47fa-aa2c-8e7672d51ab9 · 2026-10-09T12:55:43Z start
Follow-up #1 of `15-noun-verify` NULL (2026-10-09). Parent discriminators adopted as bar constraints; re-verified independently below.

## Bar (verbatim, pre-registered)

> "name 15's value among adverb candidates fitting all three windows: 'ne [15] [33=dire]' @775, 'pas [15] [01]' @1730, '[41] [15] [66-inf]' @1017; constraints: 'encore' fails @775, 'jamais' fails @1730, 'plus' fits both ('ne plus dire'; 'pas plus [01]' iff 01 adjectival - test 01's class); fence or pursue the pronoun rival ('en'/'y', via R1 @1495)"

Restated as numbered pass/fail clauses (before testing):
- C1: 'encore' fails @775 (*"ne encore [33]") at kill grade.
- C2: 'jamais' fails @1730 (*"pas jamais [01]") at kill grade.
- C3: 'plus' fits @775 ("ne plus [33]") under standing values.
- C4: 'plus' fits @1730 ("pas plus [01]" iff 01 adjectival — 01's class tested).
- C5: 'plus' fits @1017 ("[41] plus [66]") under standing values.
- C6: pronoun rival ('en'/'y') fenced or pursued (via R1 @1495).
- C7 (adverse): §7 sole-polyvalence — no adverb/noun split; @1696 noun stays fenced if 15 is adverb-valued.

Promote (name 15='plus') iff C1–C5 pass and C6/C7 answered. Else null with follow-ups.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs,
96 types; 0-based @-offsets). `canonical.py` never used. Adopted premises
(not re-litigated): 94='ne' (R19-167, single value, split closed), 30='pas'
(prom), 33=INF class (R19), 47='ce' (prom), 59='est' (prov), R24
(24='en' iff follower=85, else finite/modal), 15-noun-verify NULL (15 is
adverb-class, possibly pronoun-adjacent; noun fenced; §7 blocks the split),
§7 (67 sole true polyvalence). Corpus: `code/side-period/corpus`
(63 files, 31,664,431 chars) for the kill-grade grammaticality checks.
R5005, sealed gates, red-team adjudication queue untouched.

## Window-level evidence (byte-exact, 0-based)

**W_A @775** (row a5_04): `@771..779 = 94 07 06 94 | 15 | 33 73 37 08`
→ "ne [15] [33-INF]" (94='ne' lead; 33 INF cls).

**W_B @1730** (row a8_07): `@1726..1734 = 39 88 24 30 | 15 | 01 56 30 06`
→ "pas [15] [01]" (30='pas' prom; 01 unvalued).

**W_C @1017** (row a6_02): `@1013..1021 = 47 03 24 41 | 15 | 66 91 53 84`
→ "[41] [15] [66]" (47='ce' prom; 03's R19 verb-stem grant is conditioned to
"03 29"×3 and does not apply here — successor is 24; 24=finite/modal per R24
since follower 41≠85; 41 unvalued; 66 unvalued but infinitive-shaped,
pre=00='pour' ×7).

**15 census: n(15)=10** — [@323, @775, @1017, @1318, @1420, @1495, @1696,
@1730, @1760, @1811]. Predecessors {60, 94, 41×2, 98, 79, 66, 58, 30, 61};
successors {63, 33×2, 66, 24, 59, 23, 01, 93×2}.

## Per-clause results

- **C1: PASS (kill grade).** *"ne encore [33]"* is ungrammatical French in
  every period — "ne" cannot pair with "encore" without "pas" ("ne pas
  encore"). Corpus: 0 occurrences of negator-"ne + encore + V" in
  31,664,431 chars (the 3 raw "ne encore" hits are substrings of "règne",
  "jeune", "me répugne"). 'encore' is eliminated as 15's value.
- **C2: PASS (kill grade).** *"pas jamais [01]"* is ungrammatical French in
  every period — "jamais" is a negative-polarity item requiring "ne";
  "pas jamais" is not a French collocation. Corpus: 0 occurrences in
  31,664,431 chars. 'jamais' is eliminated as 15's value. (It also fails
  W_C independently: no "ne" licenses it there.)
- **C3: PASS.** "ne plus [33-INF]" = "ne plus dire"-shaped, fully
  grammatical; positive control "ne plus en parler" / "ne plus me laisser"
  attested in the period corpus. All premises standing (94, 33).
- **C4: FAIL (cannot establish at battery grade).** "pas plus [01]"
  requires 01 ∈ {gradable adjective, adverb} ("pas plus grand",
  "pas plus souvent"). 01's class is open (registry null; n(01)=28).
  "37 01" ×3 (predicative frame) admits adjective OR noun; "ce [01]"
  @345/@984 leans nominal. No battery-grade frame establishes 01 as
  adjectival. 'plus' therefore does not fit W_B without an ungranted
  assumption. (Not killed: if 01 proves adjectival, the fit revives.)
- **C5: FAIL (cannot establish at battery grade).** "[41] plus [66]":
  41 unvalued, 66 unvalued. "plus"="no more" needs 41='ne' — contradicted
  (94 is the sole 'ne', R19-167). "plus"="more" needs a licensed
  "[41] plus [66]" frame; the only grammatical candidate ("sans plus
  [inf]") requires inventing 41='sans', barred by §3. No parse exists
  under standing values alone. (Not killed: naming 41's value re-opens it.)
- **C6: ANSWERED (fence).** The pronoun rival ('en'/'y') is KILLED as 15's
  global value: W_A "ne [15] [33]" would force "ne en"/"ne y", violating
  French clitic order (must elide: "n'en"/"n'y") — kill grade, independent
  of corpus. The @1495 residual ("[66] [15] [59='est']", pronoun-shaped
  per 15-noun-verify R1) is a separate window-level question, fenced;
  §7 bars promoting it into a second 15 value.
- **C7: ANSWERED.** No split is declared or needed. If a future battery
  names 15='plus', the @1696 noun reading stays fenced per 15-noun-verify
  NULL; the adverse is consistent with the verdict.

## Verdict: NULL (fence)

'encore' and 'jamais' are dead at kill grade (C1, C2). 'plus' is the sole
surviving candidate — it fits W_A cleanly (C3) — but it cannot be NAMED:
W_B needs 01's class (C4) and W_C needs 41's value (C5), neither available
at battery grade. The pronoun rival is fenced as a global value (C6).
No standing/red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands (rows a5_04/a8_07/a6_02 offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json 2026-10-09)

1. `val-01-class` (P3) — name 01's class at battery grade (n=28; "37 01"×3
   predicative frames vs "ce [01]" @345/@984 nominal lean). Adjectival-01
   revives 'plus' at W_B; nominal-01 kills it there. Bar: class named with
   ≥2 independent frame-legs, else fence.
2. `val-41-1016` (P3) — name 41's class/value at @1016. A named 41 decides
   whether "[41] plus [66]" parses (e.g. 41='sans' → "sans plus [inf]").
   Bar: 41's value named with battery-grade evidence; else fence W_C for
   'plus' permanently.
3. `15-fourth-candidate` (P3) — corpus census of the "ne [ADV] [V]" slot in
   1841 diplomatic French; if an adverb beyond {encore, jamais, plus}
   (e.g. 'guère', 'rien', 'point') fits W_A, test it against W_B and W_C.
   Bar: name the fourth candidate iff it fits all three windows with
   battery-grade evidence.

## Bookkeeping

- Queue: `15-value-id` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated from disk; own entry only; no downgrade).
- Lock created on start (2026-10-09T12:55:43Z), deleted on completion
  (verified gone). R5005, sealed gates, red-team adjudication queue
  untouched.
