# Battery `noun-86-878-fois` — verdict: NULL (fence executed)

## Bar (verbatim, pre-registered)

"name 78's class iff the @879 frame licenses it at battery grade with stated values; else fence the locus"

Numbered clauses:
- C1: name 78's class — the @879 frame ("le [86] 78 fois") licenses a class for 78 at battery grade with stated values.
- C2: else — fence the locus with stated cause.

Result: C1 FAIL / C2 FIRES.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `repair_parse.py`); asserts held (1,847 pairs, 96 types).
`code/side-keyhunt/canonical.py` never used. Offsets are 1-based as in the
queue; locus row is a5_08 (canonicality caveat stands: 68 of 70 upstream row
offsets unvalidated).

Stated values used (registry, `code/table-grid/table-registry.json`):
- 77 = 'le' (provisional), 86 = INF (class-level), 17 = 'fois' (promoted).
- 78 = 'ver' is LEAD and R20-DEFERRED — NOT a stated value; not used to name.
  (R20-284 carry-forward; R16-005 LEAD stands; R19-194 re-arm queued, unfired.)

## Locus (1-based @876–@883, byte-verified)

```
876:49 877:16 878:77 879:86 880:78 881:17 882:08 883:31
```

Frame: `le(77,prov) [86-INF,cls] [78-open] fois(17,prom)`.
The bigram `86 78` is a stream hapax; the 4-gram `77 86 78 17` is unique.
n(78) = 31 (distributional profile below).

## Findings

### C1: no class for 78 is licensed by the frame

Exhaustion over candidate classes for 78 at @880, with stated values:

1. **Adjective/participle modifying 86** — "le [INF] [ADJ] fois":
   no grammatical French continuation. The only adjective idiom before
   "fois" is "même", and it dies on gender: "fois" is feminine, so
   "le(77, masc.) même fois" is ungrammatical (requires "la même fois").
   The parent's favored hypothesis (valued 78 = participle/adjective
   constraining noun-86) fails at the locus even under the open
   masculine-noun-86 candidacy: "le [N] [part/adj] fois" leaves "fois"
   unattached — there is no licensed "[N] [ADJ] fois" frame.
2. **Noun** — "le [86] [N] fois": ungrammatical stacking; nothing licenses
   a second bare noun between a determined head and "fois".
3. **Adverb** — "le [86] [adv] fois": ungrammatical.
4. **Quantifier/ordinal** (licensing "[Q] fois") — excluded by 78's standing
   shape: the LEAD value 'ver' is a syllable, not a number word, and 78's
   distributional profile is determiner-nominal ("le 78" x7, "ce 78" x5,
   "la 78" x2), never quantificational.
5. **Word-internal "86+78"** — 86's licensed completions are 29='er' (the
   four "86 29" infinitive windows); "86 78" occurs nowhere else, and no
   French word "[86]ver" before "fois" is constructible under standing
   values (86's value open; 78's value deferred).
6. **Preposition ("vers")** — "le [86] vers fois": ungrammatical.

The R20-033 flagship legs ("le ver ne mentent" @1181, "le ver ne ment"
@1352) do not transfer: there "le" determines 78 directly; here "le"
determines 86, and 78 sits between 86 and "fois" — a different frame.

### 78's global nominal profile does not name the locus class

78's predecessors (77 x7, 47 x5, 37 x4, 67 x4, 11 x2, 87 x2, …) show a
determiner-nominal profile, but (a) the bar is locus-level, and (b) 78's
class/value is exactly what R20 deferred to the red team (DEFER with
cause; settle conditions unmet). Naming 78's class from the global
profile would pre-empt the red-team venue. Not done.

### Adverse answered

"78's value must not be invented" — satisfied: no value was assumed or
named; the 'ver' LEAD was treated as deferred, not as a stated value.

## Verdict: NULL — locus fenced

The frame "le [86] [78] fois" at @878–881 admits no class for 78 at
battery grade under stated values. The fence is locus-level only: 86's
INF class, 78's 'ver' LEAD (deferred), 17='fois' promoted, and all
standing/red-team verdicts are untouched. §7 intact. No contradiction
with any standing verdict (the parent's masc-noun-86-name NULL left 86's
noun candidacy open, not granted).

## Follow-ups proposed (all verified ABSENT from queue, left for supervisor)

1. `le86-x-fois-corpus` (P4) — corpus census of "le [N/INF] [X] fois" in
   1841 French; a genuine attestation re-opens the locus, zero hardens
   the fence to grammaticality grade.
2. `noun-86-879-frame` (P4) — name 86's class at @879 ("le [86]"
   substantivized infinitive vs noun); the locus cannot be fully read
   until 86's class is fixed.
3. `seg-86-78-word` (P4, gather-only) — test "86+78" word-internal fusion
   ("[86]ver") against 78='ver' LEAD and 86's INF class; package for the
   red-team 78 venue. No battery claim.

## Scope

Fences only the @879 locus class-naming. Untouched: 86's INF class and
its four "86 29" infinitive windows, the @867 prefix-tier finding,
78's 'ver' LEAD and its R20 deferral, the ver78-gate-wordbound re-arm
(trigger unfired), §7, R5005, sealed gate instances, the red-team
adjudication queue.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/noun-86-878-fois.lock` created
  2026-10-09T20:12:35Z (agent id + timestamp; no stale lock), deleted on
  completion (verified gone).
- Queue `noun-86-878-fois`: pre-write assert passed (was queued,
  verdictless); updated to `status: verdict`, `verdict: {result: null,
  report: code/crowd17/report_inbox/battery-noun-86-878-fois.md,
  date: 2026-10-09}` via target-id-unique tmp
  `battery-queue.json.noun-86-878-fois.tmp` + atomic rename; disk
  re-validated; own entry only; no downgrade; no tmp leftover.
