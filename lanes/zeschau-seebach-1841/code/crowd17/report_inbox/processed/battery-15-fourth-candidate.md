# Battery `15-fourth-candidate` — verdict: KILL

Worker: 57f85b0d-4b3e-4322-9d01-47ed42973f4a · 2026-10-09T13:29:52Z start
Follow-up #3 of `15-value-id` NULL (2026-10-09). Parent windows and standing
values adopted, re-verified independently below.

## Bar (verbatim, pre-registered)

> "name the fourth candidate iff it fits all three windows with battery-grade evidence."

Restated as numbered pass/fail clauses (before testing):
- C1: corpus census of the "ne [ADV] [V]" slot executed in the 1841 period
  corpus (inventory enumerated empirically, not from grammar alone).
- C2: a fourth candidate beyond {encore, jamais, plus} fits W_A @775
  ("ne [15] [33-INF]") at battery grade.
- C3: the same candidate fits W_B @1730 ("pas [15] [01]") at battery grade.
- C4: the same candidate fits W_C @1017 ("[41] [15] [66-inf]") at battery
  grade.
- Promote (name the fourth candidate) iff C1–C4 all pass. Else kill iff a
  clause fails at kill grade (§4), else null.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs,
96 types; 0-based @-offsets). `canonical.py` never used. Adopted premises
(not re-litigated): 94='ne' (R19-167, sole value), 30='pas' (prom),
33=INF class (R19), 47='ce' (prom), 46='que' (banked — 'que' barred as a
candidate), §7 (67 sole true polyvalence; no adverb/noun split for 15),
battery-15 C1/C2 kills ('encore' dead @775, 'jamais' dead @1730),
battery-15 C3–C5 ('plus' fits W_A only; W_B needs 01's class, W_C needs
41's value — both open). Corpus: `code/side-period/corpus` (77 files,
34,551,456 chars; includes German-language periodicals — French bigram
patterns only, word-boundary matched). R5005, sealed gates, red-team
adjudication queue untouched.

## Window-level evidence (byte-exact, 0-based, re-derived)

**W_A @775** (row a5_04): `@771..779 = 94 07 06 94 | 15 | 33 73 37 08`
→ "ne [15] [33-INF]" (immediate lead 94='ne'; 33 INF cls).

**W_B @1730** (row a8_07): `@1726..1734 = 39 88 24 30 | 15 | 01 56 30 06`
→ "pas [15] [01]" (30='pas' prom; 01 unvalued).

**W_C @1017** (row a6_02): `@1013..1021 = 47 03 24 41 | 15 | 66 91 53 84`
→ "[41] [15] [66]" (47='ce' prom; 41 unvalued; 66 infinitive-shaped).

**15 census: n(15)=10** — [@323, @775, @1017, @1318, @1420, @1495, @1696,
@1730, @1760, @1811]. Matches battery-15.

## Census results: the "ne [ADV] [V]" slot is a closed class

Adjacent `ne <ADV>` bigram counts (34.5M chars) plus windowed
`ne (≤2 words) <ADV>` for clitic-separated forms:

| adverb | ne+ADV (adj) | ne..ADV (≤2w) | pas+ADV (adj) | W_A fit | W_B fit |
|---|---|---|---|---|---|
| pas | 1298 | — | — | n/a (30) | n/a |
| point | 223 | — | 0 | PASS (period-attested, verb followers) | FAIL kill |
| rien | 117 | — | 0 | PASS ("ne rien dire" ×5, "ne rien faire" ×11) | FAIL kill |
| plus | 116 | — | 405 | PASS (battery-15 C3) | open (01's class) |
| jamais | 83 | — | 0 | killed (battery-15 C2) | killed |
| guère | 1* | 362 | 0 | PASS ("ne guère espérer" — infinitive follower, period-attested) | FAIL kill |
| nullement | 0 | 65 | 0 | PASS ("ne convient nullement" ×65, period-attested) | FAIL kill |
| aucunement | 0 | 2 | 0 | PASS (period-attested) | FAIL kill |
| encore | 0 | — | 588 | killed (battery-15 C1) | n/a |
| que | 1 | — | 671† | barred (46='que' banked) | n/a |

\* Single adjacent "ne guere" hit is OCR-degraded ("J'avoue ne guere
esperer" — accent dropped); the form is period-attested.
† "pas que" samples are all complementizer-"que" ("il ne faut pas que
je…"), not an adverb candidate; barred independently by 46='que'.

No other member of the French "ne [ADV] [V]" inventory exists: "aucun",
"nul", "personne" require a nominal host and cannot sit pre-infinitivally
in the 15 slot (0 "ne aucun"/"ne nul"/"ne personne" hits); "à peine",
"quasiment", "sans" never pair with "ne". The inventory above is
exhaustive.

## Per-clause results

- **C1: PASS.** Census executed over 77 files / 34,551,456 chars. The
  "ne [ADV] [V]" slot admits exactly {pas, point, rien, plus, jamais,
  guère, nullement, aucunement} (plus clitic-separated variants), each
  period-attested in the ne-slot.
- **C2: PASS.** Fourth candidates fitting W_A "ne [15] [33-INF]" at
  battery grade: 'guère', 'rien', 'point', 'nullement', 'aucunement' —
  each period-attested in the adjacent or clitic-separated "ne [ADV]
  [V]" slot with verb/infinitive followers ("ne rien dire" ×5;
  "ne guère espérer"; "ne point" ×223 with verb followers;
  "ne … nullement" ×65; "ne … aucunement" ×2).
- **C3: FAIL at kill grade — for every C2 survivor.** W_B is
  "pas [15] [01]". 'guère', 'rien', 'point', 'nullement', 'aucunement'
  are negative-polarity adverbs: they require the "ne" licensor and
  cannot pair with "pas". Corpus: 0 attestations of "pas guère",
  "pas rien", "pas point", "pas nullement", "pas aucunement" in
  34,551,456 chars (same kill standard battery-15 used for
  "pas jamais" @1730). *"pas rien [01]" / *"pas guère [01]" are
  ungrammatical French in every period. W_B structurally forces every
  fourth candidate false. This is not a data gap — it is a polarity
  constraint.
- **C4: FAIL at battery grade — for every C2 survivor.** W_C
  "[41] [15] [66]" has no "ne" licensor; licensing a polarity adverb
  there would require 41='ne', contradicted (94 is the sole 'ne',
  R19-167, split closed). No parse exists under standing values alone.

## Verdict: KILL

The hypothesis "an adverb beyond {encore, jamais, plus} fits all three
windows" is forced false at kill grade: the "ne [ADV] [V]" inventory is
exhaustively enumerated from the period corpus (C1), five fourth
candidates fit W_A (C2), and W_B kills every one of them at kill grade
(C3) — a negative-polarity adverb cannot sit in the "pas [15] [01]"
slot, 0/34.5M chars, ungrammatical in every period. W_C independently
fails for all of them (C4). No standing verdict contradicted;
battery-15's NULL stands (its 'plus' path is untouched — 'plus' is the
sole polarity-compatible survivor and its W_B/W_C fate belongs to the
already-queued siblings below). §7 intact; no split declared or needed.

## Follow-ups

None proposed. A kill is terminal for this hypothesis; there is no
residual narrower bar — the inventory is closed and W_B's polarity
constraint is structural, not frame-dependent. The live 'plus' path
remains covered by already-queued siblings `val-01-census` (01's class
for W_B) and `val-41-1016` (41's value for W_C); verified queued
2026-10-09, not re-proposed.

## Bookkeeping

- Queue: `15-fourth-candidate` → `status: verdict`, `result: kill`,
  2026-10-09 (pre-write assert passed — was queued/verdictless;
  temp-file + rename; JSON re-validated from disk; own entry only;
  no downgrade).
- Lock created on start (2026-10-09T13:29:52Z), deleted on completion
  (verified gone). R5005, sealed gates, red-team adjudication queue
  untouched.
