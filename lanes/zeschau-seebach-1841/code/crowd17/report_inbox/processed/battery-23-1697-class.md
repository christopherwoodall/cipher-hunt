# Battery report — 23-1697-class

Worker: 361966ec-f73f-442c-915e-c6a71a9acac6 (2026-10-09T18:17Z).
Target: `23-1697-class`. Follow-up #3 of `15-noun-verify` NULL (2026-10-09).

## Bar (verbatim, pre-registered)

"name 23's class at @1697 (n=8; pre {65 x3, 45 x3, 64 x1, 15 x1}, suc {91 x2, 37, 09, 77, 99, 08}); decides the '[15] [23] 91' tail parse and tests whether 'ce [23]' (45-pre x3) mirrors a nominal frame; 23~26 SPLIT granted so no homophone rescue via 23"

## Numbered clauses

- **C1:** Name 23's class with ≥2 independent legs at battery grade.
- **C2:** The '[15] [23] 91' tail parse at @1697 is decided by the class naming.
- **C3:** The 'ce [23]' nominal-frame test (45-pre ×3) is resolved.
- **C4:** Adverse answered — 23~26 SPLIT respected; no homophone rescue via 23/26.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session (asserts held:
1,847 pairs, 96 types). `canonical.py` never used. All @-offsets 0-based.
Censused all 8 windows of 23 with ±2 context; cross-checked against the
`qui-fol-23-26-value` NULL (2026-10-09) leg inventory (adopted, not re-litigated).

Stream census (matches the bar's distribution exactly):
n(23)=8; pre {65×3 (@136/@1609/@1782), 45×3 (@679/@1056/@1552), 64×1 (@182),
15×1 (@1697)}; suc {91×2 (@136/@1697), 37 (@182), 09 (@679), 77 (@1056),
99 (@1552), 08 (@1609)}.

## Window-level evidence

| @ | window (±2) | class leg |
|---|-------------|-----------|
| 136 | `21 65 [23] 91 65` | VERB — 65 noun-class (R20-047 grant) subject; "[N] [V] [91]" |
| 182 | `87 64 [23] 37 06` | VERB, kill grade — 64="qui" promoted (["qui","prom"]) forces a finite verb; 37 A1 predicative → copula slot |
| 679 | `77 45 [23] 09 07` | VERB (copula) — 45="ce" (A11 hold); "c'est"-frame; nominal rival "ce [N]" leaves a verbless fragment |
| 1056 | `74 45 [23] 77 84` | VERB — "ce [23] [77]"; "ce [N] le" ungrammatical (determiner after bare noun); verbal frame forced |
| 1552 | `92 45 [23] 99 13` | VERB (copula) — "ce [23] [99]"; "c'est [99]" complete clause vs verbless nominal fragment |
| 1609 | `92 65 [23] 08 55` | VERB, battery grade — 65 noun-class subject + 23 + 08="t" (battery-grade letter); "[N] [V]t" finite frame |
| 1697 | `58 15 [23] 91 85` | VERB — "[15] [V] [91]"; 15's class open (15-noun-verify NULL) so 15's role unnamed, but 23's verbal slot decided |
| 1782 | `74 65 [23] 98 83` | VERB — "[65-N] [23]"; 98="vient" is LEAD-only so 23's finiteness here is open, but verb CLASS holds (non-finite or finite) |

## Per-clause pass/fail

- **C1 — PASS.** Six independent verb-class legs at battery grade or better:
  @182 (kill-grade, qui-forced finite), @679/@1056/@1552 (three independent
  "ce [23]" copula frames), @1609 (noun-subject finite), @136 (noun-subject).
  Zero noun-class legs anywhere on the stream.
- **C2 — PASS.** With 23=VERB, the @1697 tail parses as "[15] [23-V] [91]".
  The nominal-tail rival (23 as nominal head/modifier) is excluded. 15's own
  class stays open per 15-noun-verify NULL — not claimed here.
- **C3 — PASS (nominal frame rejected).** The three "ce [23]" windows do NOT
  mirror a nominal frame: "ce [N]" + follower ("[09]"/"[77]"/"[99]") yields
  verbless fragments in all three, while the "c'est" copula reading yields
  complete clauses. The nominal hypothesis is excluded at all three loci.
- **C4 — PASS.** All legs are 23's own windows; 26's legs not used. No
  homophone claim made. The 23~26 SPLIT (granted) is respected. Naming the
  CLASS "verb" does not name a value and creates no §7 polyvalence issue
  (cf. qui-fol-23-26-value, where only the VALUE "est" was §7-blocked).

## Verdict: PROMOTE — 23 = VERB class

23 is uniformly verb-class across all 8 windows (finite and copula
realizations; copula is a verb subclass). No window forces or admits a
non-verb class; the noun hypothesis is kill-grade excluded by the
"ce [23]" test. This is a class-level promote only — no value named
(value "est" remains §7-blocked per qui-fol-23-26-value).

## Scope

Class-level only. Does not name 23's value. Does not touch 26 (split
respected), 15 (class open), 91 (open), or any standing red-team verdict.
23 was previously unregistered; this promote is a candidate for red-team
ratification. §7 intact (sole polyvalence 67 et/veut untouched).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-23-1697-class.md`
- Queue: `23-1697-class` → `status: verdict`, `result: promote` (pre-write
  assert passed — was queued/verdictless; temp-file + rename; own entry
  only; no downgrade)
- Lock created on start (2026-10-09T18:17:00Z), deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
- No follow-ups required (promote). Optional red-team venue: ratify
  23=["verb","cls"] registry entry.
