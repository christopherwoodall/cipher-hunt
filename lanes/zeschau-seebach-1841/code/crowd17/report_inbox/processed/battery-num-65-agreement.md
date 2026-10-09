# Battery verdict: num-65-agreement

- Target: `num-65-agreement` (battery-queue.json, priority 3, status queued)
- Claim: "Census number agreement across all 25 windows of 65 (singular vs plural verb/adjective/determiner agreement)"
- Stream: repaired 1,847-pair / 96-type parse, re-derived in-session; asserts held. `canonical.py` never used.

## Bar (verbatim, pre-registered)

"Produce the full 25-window number-agreement table; fence 65 as number-variable iff both singular and plural agreement are attested at battery grade, else name the fixed number"

Numbered clauses:
- C1: Produce the full 25-window number-agreement table.
- C2: Fence 65 as number-variable iff both singular AND plural agreement are attested at battery grade.
- C3: Else (not both attested), name the fixed number.

## Method

Byte-exact census of all 25 windows of 65 on the repaired stream (n(65)=25 confirmed).
For each window, tested number-forcing configurations: (a) 65 as subject of a
number-fixed verb (3sg "est"/"vient" vs 3pl "-ent" 06), (b) 65 preceded by a
number-fixed determiner ("la" pencil, "le" provisional, "tout" A5-granted),
(c) 65 as antecedent of a "qui" relative with number-fixed verb,
(d) 65 directly followed by 06 ("65 + ent-verb" subject frame).

## Findings — the 25-window number-agreement table

| @ | window (65 centered) | agreement evidence |
|---|---|---|
| 135 | 56 64-qui 21 65 23 | none — neighbors unvalued |
| 138 | 21 65 23 91 65 | none |
| 251 | 94-ne 65 63-verb | none — 63 number open |
| 293 | 64-qui 29 40-e 65 16 | none |
| 372 | 06-ent 21 65 63 29 | none — 06 precedes, not agreeing with 65 |
| 455 | 77-le 60 65 13 | none — "le" separated by 60, head ambiguous |
| 512 | 98 65 88 | none — 65 is object of "vient" |
| 687 | 64-qui 29 40-e 65 94 | none |
| 724 | 77-le 03 91 65 64-qui | none — "le" at -3 |
| 787 | 74 65 84-on 06-ent | none — "on ent" is the 84 tension, not 65 |
| 812 | 24-verb 65 14 29 | none |
| 923 | 40-e 08 65 71 | none |
| 1106 | 47-ce 78 65 63-verb | none |
| 1112 | 41 65 38-verb 30-pas | none — 38 number open |
| 1208 | 21 65 64-qui 59-est | **SINGULAR** — "qui est" 3sg; antecedent NP "21 65" forced singular |
| 1253 | 06-ent 65 46-que | none — 06 precedes 65 |
| 1340 | 64-qui 60-08 65 64-qui | none — 65 follows "vient", not its subject |
| 1383 | 24-verb 65 68 | none |
| 1530 | 87-ce 46-que 21 65 63 | none |
| 1588 | 64-qui 65 48-e 29-er | none |
| 1608 | 39 11-la 92 65 23 | none — "la" governs 92, not 65 |
| 1683 | 46-que 79-tout 65 13 | **SINGULAR** — "tout" (ms, A5-granted) + noun-class 65 |
| 1712 | 40-e 65 94-ne 44 59-est | none — "est" governs 44, not 65 |
| 1748 | 40-e 06-ent 65 34-i | none — 06 precedes 65 |
| 1781 | 59-est 19 48-e 74 65 | none — "est" far left, no government of 65 |

Singular legs (battery grade):
- **L1 @1208** `43 55 61 [21-noun] [65-noun] [64-qui] [59-est] [32-verb] 48`: "qui est"
  is 3sg (64="qui" granted; 59="est" provisional). The relative's antecedent is
  the immediately preceding NP "21 65"; singular "est" forces the antecedent
  singular, and a plural member noun would force "qui sont" — so 65 is singular.
- **L2 @1683** `44 00-pour 46-que [79-tout] [65] 13 [93-verb]`: 79="tout" is
  A5-granted in the masculine-singular form. 65 is registry noun-class, which
  kills the adverbial-"tout" reading; the remaining parse is determiner "tout"
  + noun = "every [65]" → 65 singular (masculine at this window).

Plural legs: **zero**. Exhaustive negative:
- 65 is never directly followed by 06 (no "65 + ent-verb" subject frame exists
  stream-wide).
- No plural determiner ever precedes 65 (predecessor inventory: 21×4, 40×3,
  91×2, 74×2, 24×2, 08×2, 06×2, 94, 60, 98, 78, 41, 64, 92, 79 — none plural).
- The two 06-adjacent windows (@1253, @1748) have 06 *preceding* 65; the @787
  "on ent" is the 84-agreement tension, not a 65 frame.

## Per-clause pass/fail

- C1 (full table) PASS — all 25 windows tabled above.
- C2 (fence variable iff both attested) — condition NOT met: singular attested
  (2 legs), plural unattested (0 legs). Fence arm does not fire.
- C3 (else name the fixed number) PASS — **65's number is singular**.

## Verdict: PROMOTE (number named: singular)

65 is number-fixed singular. Two battery-grade singular legs (@1208 relative-
clause agreement, @1683 determiner agreement); zero plural configurations
stream-wide.

## Scope

Names number only. Gender not named (masculine suggested at @1683 alone — one
window, left open). Value still open. Animacy owned by the parallel
`anim-65-select` target — untouched. No standing/red-team verdict contradicted
or downgraded; §7 intact. Canonical-stream caveat stands.

No follow-ups required (promote, not null).

## Bookkeeping

- Lock `locks/num-65-agreement.lock`: created on start (agent 384361e8,
  2026-10-09T19:19:00Z, no stale lock), deleted on completion (verified gone).
- Queue: `num-65-agreement` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless;
  target-id-unique tmp `battery-queue.json.num-65-agreement.tmp` + atomic rename;
  disk re-validated; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
