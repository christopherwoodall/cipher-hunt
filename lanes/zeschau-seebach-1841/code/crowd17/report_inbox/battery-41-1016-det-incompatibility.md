# Battery `41-1016-det-incompatibility` — verdict: PROMOTE (red-team input package)

Worker: 85432fab-1377-4206-806f-b442d079277f · 2026-10-09 start
Follow-up #2 of `val-41-1016` NULL (2026-10-09). RED-TEAM INPUT for the
`split-41-redteam` docket: per-value determiner incompatibility at @1016.

## Bar (verbatim, pre-registered)

> "deliver the per-value incompatibility evidence to the split-41-redteam docket at battery grade."

Restated as numbered pass/fail clauses (before testing):
- C1: each unforced determiner value (une / chaque / deux / plusieurs)
  tested against the @1016 frame "[24-fin] [det] [15-adv] [66-inf]"
  with byte evidence and corpus counts.
- C2: clause-boundary rescue tested — a word/clause boundary placed
  inside @1015..1017 that licenses one of the four values, or a
  stated reason none can.
- C3: per-value pass/fail delivered at battery grade; either all four
  fail (split-forced evidence) or the rescued value is named.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1847
pairs, 96 types; 0-based @-offsets). `canonical.py` never used. Adopted
premises (not re-litigated): 24 finite/modal at @1015 (R24: follower is
41, not 85); 15 adverb-class (noun-15 killed, `15-noun-verify`); 66
infinitive-shaped; `val-41-det-windows` PROMOTE (the determiner arm at
D1 @237, values une/chaque/deux/plusieurs unforced); §7 (67 sole true
polyvalence — no class, split, or polyvalence declared here). Corpus:
`code/side-period/corpus`, 76 .txt files, 34,526,989 characters;
denormalized, hyphen-joined, letter-boundary search (accents stripped,
case folded). R5005, sealed gates, red-team adjudication queue
untouched.

## Window-level evidence (byte-exact, 0-based)

**W0 @1016** (row a6_02; row a6_03 begins @1020=53):

```
@1012..1023 = 78 47 03 24 | 41 | 15 66 91 53 | 84 92 64
                    a6_02                | a6_03
```

→ "[78] [47=ce] 03 [24-fin] [41] [15-adv] [66-inf] 91 53 | [84=on]…"

The frame under test: finite/modal verb (24) → determiner (41) →
adverb "plus" (15) → infinitive (66). A determiner in this slot needs
a nominal; the only nominal it could govern is "plus [66]" — but
15-as-noun is killed (`15-noun-verify`), so the determiner stands with
no nominal under the single-value reading.

## Corpus counts (34.53M chars, letter-boundary)

**Pattern A — "DET plus" bigram, following-word shape:**
| det | hits | follows | +INF |
|-----|------|---------|------|
| une | 78 | all comparative adjectives (grande 22, longue 7, large 7, haute 3, forte 2, digne 2, …) | 0 |
| chaque | 0 | — | 0 |
| deux | 10 | all comparative adjective + noun ("deux plus grands pays", "deux plus belles années", …) | 0 |
| plusieurs | 0 | — | 0 |

**Pattern B — "[V-fin] DET plus"** (28 finite/modal verbs × 4
determiners: veut/veulent, doit/doivent, peut/peuvent, faut, va/vont,
voulait/voulaient, devait/devaient, pouvait/pouvaient, voudrait/,
devrait/, pourrait/, sait/savent, dit/disent, allait/allaient):
**0 hits in 34,526,989 characters.**

Every attested "DET plus" in the corpus is the comparative frame
"DET plus [ADJ]" — grammatical, but it needs an adjective where our
frame has an infinitive (66). "chaque plus" and "plusieurs plus" are
unattested entirely. No finite verb is ever followed by "DET plus".

## Per-value verdicts (C1)

- **une: FAIL.** *"veut une plus [inf]"* — the only licensed "une plus"
  shape is "une plus [ADJ]" (78/78); 66 is infinitive-shaped, not
  adjectival. 0/34.5M "[V-fin] une plus".
- **chaque: FAIL.** "chaque plus" unattested anywhere (0/34.5M);
  *"[V-fin] chaque plus [inf]"* ungrammatical in 1841 French with no
  licensed rescue.
- **deux: FAIL.** *"veut deux plus [inf]"* — "deux plus" licenses only
  "deux plus [ADJ] [N]" (10/10); 0/34.5M "[V-fin] deux plus".
- **plusieurs: FAIL.** "plusieurs plus" unattested anywhere (0/34.5M).

All four fail. No unforced determiner value licenses the W0 frame.

## Clause-boundary rescue audit (C2)

Only two boundary placements exist inside @1015..1017:
- **B1 at 24|41:** "[78] [47=ce] 03 [24-fin]. [41=det] [15-adv]
  [66-inf]…" — the second clause is "DET plus [inf]" with no nominal
  after the determiner; corpus: "DET plus [INF]" = 0/88. Fails.
- **B2 at 41|15:** "[24-fin] [41=det]. [15-adv] [66-inf]…" —
  clause-final determiner with no nominal after a finite verb
  (*"veut deux." / *"veut une.") — ungrammatical. Fails.

Neither placement licenses any of the four values. The only further
segmentation would make 41 word-internal to 15's word (a letter cell),
which contradicts the determiner-arm premise being tested — out of
scope of this battery, not a rescue of the premise.

## Per-clause results

- **C1: PASS** — all four values tested with byte evidence and corpus
  counts; all four fail.
- **C2: PASS** — both possible boundary placements tested; neither
  rescues any value.
- **C3: PASS** — all four fail → split-forced evidence delivered below
  at battery grade.

## Evidence package for the `split-41-redteam` docket (C3)

1. **Under §7's single-value rule, the promoted determiner arm at
   D1 (@237) and the @1016 window are jointly unsatisfiable**: every
   unforced det value (une/chaque/deux/plusieurs) fails the W0 frame
   "[24-fin] [det] [15-adv] [66-inf]" — corpus zeros 0/34.5M
   (Pattern B) and 0/88 "DET plus [INF]" (Pattern A).
2. **No clause-boundary placement inside @1015..1017 rescues any
   value** (B1, B2 both fail — stated cause above).
3. This evidence is consistent with `val-41-1016`'s own C1 FAIL and
   does not re-litigate it; it is the per-value elaboration the
   docket asked for. Nothing here names a class, value, or split.

## Adverses

- A1 (`val-41-det-windows` PROMOTE): carried, not answered — per the
  brief. The determiner arm stands at D1; this battery only records
  its per-value incompatibility at @1016.
- §7 sole-polyvalence: honored — evidence only; no class, split, or
  polyvalence declared or named by this battery.

## Verdict: PROMOTE (red-team input package delivered)

No follow-ups required per §4 (promote). Re-open conditions are
red-team venue only: a `split-41-redteam` grant (per-window naming
re-opens, per `val-41-1016`'s own evidence note), or a naming act
for 15/24/66/91 that reframes W0.

## Scope

Per-value determiner incompatibility at @1016 only. Untouched: §7
standings, `val-41-det-windows` PROMOTE, `val-41-1016` NULL/fence,
`split-41-redteam` (queued), R5005, sealed gates, red-team
adjudication queue. No standing or red-team verdict contradicted or
downgraded. Canonicality caveat stands (row a6_02 offset unvalidated).
