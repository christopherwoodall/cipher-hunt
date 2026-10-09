# Battery report: syll-39-de-host — verdict: KILL

- Target id: `syll-39-de-host` (priority 3)
- Claim: "name 39's syllable at @1334 as the penultimate of a French '-de'-final verb"
- Date: 2026-10-09
- Worker: 1b1e3ff2-0a3d-4e69-bc5d-f45b30f61cd5
- Verdict: **KILL** — the @1334 '-de'-final-verb leg is dead at kill grade
- Lock: created `code/crowd17/next-token/locks/syll-39-de-host.lock` 2026-10-09T17:32:02Z, deleted on completion. No stale lock encountered.

## Bar (verbatim, pre-registered)

"host verb named and @1334 parsed under standing values, or the @1334 leg fenced (39's value decides; phase-fragility noted)"

## Bar restated as numbered pass/fail clauses

1. C1: A specific French verb is named with 39 as its penultimate syllable and 83 as its final '-de' syllable, and @1334 parses under standing values. → FAIL at kill grade.
2. C2: The @1334 leg is fenced with stated cause. → FENCED (kill-grade cause stated below).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`;
asserted 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed
gates, red-team adjudication queue untouched. All @-offsets 0-based.

Standing values used (all from §7 / cited batteries, not re-litigated):
94='ne' (promoted), 70='pre' (banked pencil GT), 39=/a/ (promoted, allophone
tier: 'a'/'à'/word-internal 'a', battery-a-39), 86=INF-class (granted),
64='qui' (granted). 52, 62, 06, 71, 60 open. 62='il' kill-grade dead
(R19-106/R20-125).

Locus byte-confirmed (row a7_05 spans @1332–@1358; 70 is the last pair of
row a7_04 — stream treated as continuous per parent-battery convention):

```
@1327=30 @1328=06 @1329=62 @1330=94('ne') @1331=70('pre') @1332=52
@1333=39('a') @1334=83 @1335=86(INF) @1336=71 @1337=64('qui')
```

So the window reads: `... ne pre[52]a-de [INF] ...` under the hypothesis
that 83 is the syllable '-de' final to a verb with 39='a' penultimate.

## Window-level evidence

**The verb is forced to match /^pre.*ade$/.**
94='ne' is the preverbal negation particle; it must be followed by a verb
(modulo clitics — 70='pre' is not a clitic, not a pronoun, not a verb, so
it cannot standalone after "ne": "ne pre" is ungrammatical). The verb must
therefore span 70. With 39='a' as penultimate syllable and 83 as final
'-de', the verb's shape is fixed: it starts with 70='pre' (banked), ends
with 39-83 = "a"+"de", and contains 52 medially — i.e. the verb matches
/^pre.*ade$/ with 52 supplying the middle.

**Corpus check: zero French words match /^pre.*ade$/.**
Searched 29,489,376 chars of 1841-register French (period corpus,
German files excluded per lane method): the set of words matching
`pre*ade` is EMPTY — not just no verbs, no words at all. ("ade"-final
words exist — persuade, parade, dégrade, saccade, malade, promenade —
none begins with "pre".) A host verb therefore cannot be named under
standing values. This is not an epistemic gap; the French lexicon has no
slot for it.

**The "strand 70" rescue is ungrammatical.**
Excluding 70 from the verb would require "pre"/"pré" to parse as a
standalone word after "ne" — it does not ("ne pré" is not French), and no
clitic reading exists. Attaching 70 leftward (62-70 as "[62]pre", e.g.
"propre" via 62='pro') would invent 62's value and still leaves "ne [adj]"
ungrammatical. Dead.

**52's open value cannot rescue the leg.**
52 is an adverb candidate ('plus'/'jamais', tie fenced at battery grade by
plus-jamais-tiebreak 2026-10-09); even as a fully open unit, no value of
52 can create a French word matching /^pre.*ade$/ (corpus-empty set), so
naming 52 as a verb-stem piece would be invention on top of impossibility.

**39's value decides — and it is decided.**
39=/a/ is promoted (battery-a-39). Under 39='a', "[39]de" as a standalone
is "ade" (not a word, per parent syll-83-de); as a verb tail it demands a
host verb that does not exist. The a-39 battery additionally found zero
windows parsing 39 as the verb "a" ("il a"), so the "a de" two-word rescue
("avoir de") is unavailable — and was independently killed by
de-83-residuals ("'a'/'à' + 'de' never adjacent").

**Phase-fragility verified and noted (secondary).**
Parent claim re-verified in-session: row a7_05 has 55 digits (odd), so
offset 0 → `52 39 83 86 ...` while offset 1 → `23 98 38 67 16 46 00 86
56 45 23 84 78 66 ...` (byte-exact match to the parent's cited rival
parse). Upstream EM chose 0; the repair (a5_03 1→0) did not touch a7_05.
Under the standing offset-0 parse the kill above holds; under offset 1 the
39-83 bigram dissolves entirely — consistent with the kill, not a rescue.

## Per-clause results

- C1 (name the host verb): FAIL at kill grade — the window forces the
  claim false. No French verb matches the forced shape /^pre.*ade$/;
  corpus-exhaustive zero in 29.5M chars; grammatical rescues dead.
- C2 (fence with cause): FENCED — cause is the kill-grade linguistic
  impossibility above, plus the verified phase-fragility note.

## Verdict: KILL

The @1334 leg — "39's syllable as penultimate of a '-de'-final verb" — is
dead. Under standing values the locus cannot host such a verb.

## Scope

- KILLS: the @1334-specific verb-host instantiation of the syllabic-83
  fork. 39 cannot be penultimate to a '-de'-final verb here.
- Does NOT kill: the word-level 83='de' reading at @1334
  ("[pre[52]a] de [86-INF]", de-83-residuals PROMOTE — untouched and now
  the default fork); the syllabic '-de' fork at @614/@1171 (different
  left context, owned by frame-87-83-cede / syll-83-de); 39='a';
  70='pre'; 94='ne'.
- No standing or red-team verdict contradicted. §7 intact
  (67 et/veut remains the sole true polyvalence). No cleaner rival value
  needed — the claim dies on the lexicon, not on a rival.
- The sibling target syll-83-de-1829 (@1829 "38-83" fork) is unaffected:
  different locus, different left context, fenced to its own target.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-syll-39-de-host.md`
- Queue: `syll-39-de-host` → `status: verdict`, `verdict: kill`,
  2026-10-09 (pre-write assert passed — was queued/verdictless;
  temp-file + rename; disk re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion. R5005, sealed gates,
  red-team adjudication queue untouched.
