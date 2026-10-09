# Battery `governor-00-inf-locus` — follower-frame-typed census of all 55 00-loci

**Date:** 2026-10-09
**Worker:** battery agent (subagent)

## Bar (verbatim, pre-registered)

> deliver follower-frame-typed census of all 55 00-loci; state whether the pour-governor's actual follower class reproduces the A9 grant or extends it

**Numbered clauses:**
- C1: deliver a follower-frame-typed census covering all 55 00-loci, with stated @-offsets and follower classes.
- C2: state, with battery-grade grounds, whether the pour-governor's actual follower inventory reproduces the A9 grant (`00="pour"`, leg-1 class-level) or forces an extension of it.

## Adverse (pre-registered)

> follower typing against ungranted frames does not license conclusions

**Answer:** adopted. Every follower was typed ONLY against granted/banked frames (ground truth, promoted, provisional, and the A9-class 86 verb-class grant). Followers whose value or class is still open are marked UNTYPED, and no conclusion is drawn from them. The two arms below are stated strictly on the typed windows.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (parsed like `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` was never used. R5005 was never touched. All offsets below are 0-based global pair indices.

## Findings

### C1 — census: n(00) = 55 byte-exact

Follower distribution (sum = 55; every 00 has a follower; none at stream end):

| follower | n | granted frame | typing |
|---|---|---|---|
| 86 | 12 | verb-class (A9 class grant) | TYPED: pour + verb |
| 33 | 8 | open (val-33-verb NULL) | UNTYPED |
| 66 | 7 | open | UNTYPED |
| 92 | 6 | open | UNTYPED |
| 97 | 4 | open (97 INF/NOM tie, red-team venue) | UNTYPED |
| 11 | 4 | GT "la" | TYPED: pour + nominal |
| 46 | 4 | GT "que" | TYPED: pour + que-clause |
| 36 | 3 | open | UNTYPED |
| 34 | 1 | GT "i" (bound letter) | UNTYPED (letter-tier, cannot head a word) |
| 13 | 1 | open | UNTYPED |
| 20 | 1 | open (20~17 split holds) | UNTYPED |
| 64 | 1 | promoted "qui" | TYPED: pour + pronominal |
| 98 | 1 | battery-lead only (not ratified) | UNTYPED per adverse |
| 67 | 1 | et/veut (positional) | UNTYPED per adverse |
| 44 | 1 | open (A1 predicative frame) | UNTYPED |

Window-level table (@-offset, ±2 context, 0-based):

- 00→86 ×12: @552 `55 81 00 86 59` · @660 `62 16 00 86 50` · @727 `64 11 00 86 48` · @866 `47 46 00 86 70` · @888 `03 02 00 86 06` · @961 `67 96 00 86 56` · @1001 `82 33 00 86 56` · @1127 `37 43 00 86 52` · @1374 `67 98 00 86 29` · @1505 `42 33 00 86 56` · @1791 `47 03 00 86 56` · @1824 `00 97 00 86 29`
- 00→33 ×8: @185 `37 06 00 33 16` · @407 `69 26 00 33 01` · @466 `42 96 00 33 79` · @845 `12 16 00 33 96` · @935 `69 26 00 33 21` · @1087 `55 81 00 33 79` · @1244 `87 11 00 33 16` · @1629 `69 26 00 33 21`
- 00→66 ×7: @188 `33 16 00 66 24` · @245 `56 43 00 66 91` · @253 `65 63 00 66 01` · @714 `12 63 00 66 86` · @1108 `65 63 00 66 73` · @1493 `39 24 00 66 15` · @1532 `65 63 00 66 73`
- 00→92 ×6: @48 `62 96 00 92 79` · @329 `01 19 00 92 50` · @592 `41 09 00 92 79` · @682 `09 07 00 92 64` · @977 `08 01 00 92 07` · @1153 `84 02 00 92 29`
- 00→97 ×4: @1 `09 00 97 51` (stream-start, no −2 cell) · @287 `89 28 00 97 09` · @587 `18 14 00 97 41` · @1822 `09 19 00 97 00`
- 00→11 ×4: @76 `87 11 00 11 29` · @378 `82 48 00 11 50` · @1287 `55 68 00 11 17` · @1405 `87 11 00 11 95`
- 00→46 ×4: @106 `45 28 00 46 11` · @545 `42 06 00 46 24` · @1545 `78 43 00 46 70` · @1680 `77 44 00 46 79`
- 00→36 ×3: @739 `82 06 00 36 20` · @1312 `92 44 00 36 74` · @1584 `12 44 00 36 70`
- 00→34 ×1: @27 `55 81 00 34 24`
- 00→13 ×1: @480 `45 93 00 13 52`
- 00→20 ×1: @667 `62 06 00 20 67`
- 00→64 ×1: @748 `85 28 00 64 02`
- 00→98 ×1: @1138 `62 98 00 98 78`
- 00→67 ×1: @1247 `33 16 00 67 46`
- 00→44 ×1: @1602 `82 98 00 44 70`

C1: **PASS** — all 55 loci censused with offsets, context, and frame typing.

### C2 — reproduces or extends the A9 grant?

Typed inventory (21/55 windows): pour + verb (86×12), pour + nominal ("pour la" ×4, "pour qui" ×1), pour + que-clause (46×4). Every typed window reproduces the A9 grant's licensed government of French "pour" — infinitival/verbal, nominal, and "pour que" clausal complements are all standard 1841 French government. No typed window forces a new government class: there is no attested follower class outside pour's standing inventory.

Untyped inventory (34/55 windows): 33, 66, 92, 97, 36, 13, 20, 98, 67, 44 are value/class-open; 34 is letter-tier (bound "i" cannot head a word). Per the adverse, these license no conclusions either way — they neither reproduce nor extend the grant.

Corroboration: the standing `pour-prefix-00-census` KILL closed the syllabic "pour-" composition route under standing values, so 00 reads as a free governing word at every locus — consistent with the typed follower inventory.

C2: **PASS** — the pour-governor's actual follower class **reproduces** the A9 grant; nothing forces an extension.

## Verdict: PROMOTE

All bar clauses pass; the adverse is answered by typing only against granted frames and marking the 34 ungranted/letter-tier windows UNTYPED. This banks the 55-locus census and the reproduction finding at battery grade. No value named, no red-team act requested; §7 intact. No standing/red-team verdict contradicted or downgraded; canonical-stream caveat stands. Per §4 (promote), no follow-ups required.
