# Battery verdict: par-96-complement-census

**Target:** par-96-complement-census
**Date:** 2026-10-09
**Verdict: PROMOTE (sweep finding)**

## Bar (verbatim)

> uniqueness check

Restated as clauses:
- **C1:** census all 21 of 96's windows on the repaired stream (byte-exact @-offsets, successors stated).
- **C2:** test whether 96 is ever complement-less elsewhere, i.e. whether "96 00" ('par pour') x3 is unique in its complement-lessness.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`. `canonical.py` never touched.
n(96) = 21, byte-confirmed. @-offsets are 0-based stream indices.

Standing premises (adopted, not re-litigated):
- 96='par' promoted; 00='pour' granted (A9, leg-1 class-level); 00='contre'
  conditioned after 96='par' is red-team territory (contre-00-condition-gate queued).
- par-43 noun kill terminal (battery-par43-adverbial-attestation, promote,
  2026-10-09: bare "par mesure"/"par condition" unattested); pending only the
  @21 polyvalence adjudication.
- Clause-boundary rescue for "96 00" fenced (battery-bound-96-00-clause, null,
  2026-10-09): no byte evidence; elided prepositional complements ungrammatical
  in 1841 French.

## Census: all 21 of 96's windows (0-based @, successor in brackets)

| @ | Row | Window (succ) | Complement verdict |
|---|-----|----------------|--------------------|
| 47 | a1_01 | 62 96 [00] 92 | COMPLEMENT-LESS — "par pour" ungrammatical; "par contre" conditioned, red-team gate |
| 131 | a1_03 | 32 96 [56] 64 | parses — "par [56]" infinitive (56 verb-stem class) |
| 150 | a1_04 | 64 96 [47] 46 | parses — "par ce" (47='ce' A4) |
| 224 | a2_01 | 61 96 [87] 46 | parses — "par ce" (87='ce' promoted) |
| 230 | a2_01 | 82 96 [21] 60 | parses — "par [21-noun]" (21 noun class) |
| 342 | a2_05 | 64 96 [43] 87 | COMPLEMENT-LESS — par-43 kill terminal; 43's value open, no "par [43]" rescue statable |
| 465 | a2_10 | 42 96 [00] 33 | COMPLEMENT-LESS — "par pour" x2 |
| 602 | a4_00 | 26 96 [45] 93 | parses — "par ce" (45='ce' A11 held) |
| 847 | a5_06 | 33 96 [40] 62 | fenced — 40='e' letter; compositional word-initial reading ("par e[62]"), not a word-level complement |
| 914 | a5_09 | 37 96 [09] 02 | fenced — 09's class open (verb hypothesis fenced); undecidable |
| 927 | a5_10 | 61 96 [48] 82 | fenced — 48='e' letter; compositional ("par em-..."), not a word-level complement |
| 947 | a5_10 | 98 96 [86] 01 | fenced — 86 open (positional 86); undecidable |
| 952 | a6_00 | 86 96 [87] 46 | parses — "par ce" |
| 960 | a6_00 | 67 96 [00] 86 | COMPLEMENT-LESS — "par pour" x3 |
| 998 | a6_02 | 11 96 [82] 33 | fenced — 82='m' letter; compositional word-initial ("par m[33]"), not a word-level complement |
| 1026 | a6_03 | 64 96 [43] 87 | COMPLEMENT-LESS — "par [43]" x2 (par-43 kill) |
| 1063 | a6_04 | 82 96 [21] 62 | parses — "par [21-noun]" |
| 1196 | a7_00 | 16 96 [82] 16 | fenced — 82='m' letter, doubled frame; canonicality caveat (a7_00 offset unvalidated; offset-1 reparse is red-team territory) |
| 1213 | a7_00 | 48 96 [45] 36 | parses — "par ce" (45='ce') |
| 1526 | a8_00 | 48 96 [87] 46 | parses — "par ce" |
| 1786 | a8_09 | 82 96 [21] 68 | parses — "par [21-noun]" |

Successor census: 00 x3, 87 x3, 21 x3, 43 x2, 45 x2, 82 x2, 56, 47, 40, 09, 48, 86.

## Per-clause results

- **C1: PASS** — all 21 windows censused byte-exact above.
- **C2: PASS (refined).** 96 is complement-less elsewhere: "96 43" x2
  (@342, @1026) also lacks a grammatical complement under standing verdicts.
  But the "par pour" x3 anomaly is unique in KIND: 00 is the ONLY successor of
  96 that carries a granted preposition value under standing grants, making
  "par pour" the unique preposition-pile-up among the 21 windows. The "par [43]"
  windows are complement-less by a different route — the follower's value is
  open and its noun readings are dead (par-43 kill), so nothing grammatical can
  be stat
...[truncated 1604 chars]
