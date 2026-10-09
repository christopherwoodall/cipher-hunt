# Battery report: inventory-doubling-contrast

Target: `inventory-doubling-contrast` (P3, RED-TEAM INPUT). Claim: package the
"prenne"-doubled vs "prenent"/"pasent"-single contrast for the red team. Date:
2026-10-09. Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types
re-derived in-session, asserts held). `canonical.py` never used. R5005, sealed
gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

"standing falsification of any general single-consonant habit; venue for the
compositional (group-inventory) account; evidence only, no class named"

Numbered clauses (before testing):

1. C1 — standing falsification of any general single-consonant habit: byte-exact
   evidence that a general "clerk writes single where standard French doubles"
   rule is falsified at the lane's byte standard.
2. C2 — venue for the compositional (group-inventory) account: the
   doubled-vs-single contrast is explained by which group follows 12='n'
   (94='ne' contributes its own n; 06='ent' contributes no consonant), with a
   full inventory census to back the claim.
3. C3 — evidence only, no class named: the package declares no value, class,
   split, or polyvalence; red-team venue is honored.

Offset convention: 0-based token indices; rows from `repaired_offsets.json`.

## Standing values used (registry, unchanged)

- 70='pre' (gt), 12='n' (prom), 94='ne' (lead), 06='ent' (prom),
  30='pas' (prom), 29='er' (gt).
- R19-167 (adopted, not re-litigated): 94's value is the single syllabic
  spelling "ne"; the 94 split is CLOSED. This is the premise on which the
  compositional account rests.

## Method

Re-derived the repaired stream in-session; census-verified every window below
byte-exact. Adopted (not re-tested): `spell-single-consonant` NULL (2026-10-09)
and its window-level findings; `enne-family-12-94` PROMOTE (12+94 as letters
inside one word).

## C1 — falsification of the general single-consonant habit

The general rule ("the clerk writes a single consonant where standard 1841
French orthography doubles it", e.g. nn->n, ss->s) predicts that a clerk
writing "prenne" would write "prene". The cipher writes the doubled n in
full, twice:

- **W-A** "prenne": 70-12-94, 0-based @347-349 (row a2_05), ctx
  `43 87 01 06 [70 12 94] 74 67 78 40`.
- **W-B** "prenne": 70-12-94, 0-based @1547-1549 (row a8_00), ctx
  `78 43 00 46 [70 12 94] 92 45 23 99`.
- **W-C** (corroborating, non-70 context): 12-94 at 0-based @64-65
  (row a1_01), ctx `08 34 29 [40 12 94] 92 69 13` — 'e'+'n'+'ne' = "enne"-shaped;
  the doubled n is written in full outside the "prenne" trigrams too.

12-94 census: exactly 3x stream-wide (@64, @348, @1548); all three carry the
doubled n. The general rule's prediction ("prene"/"ene") fails at all three
windows — direct contradiction at the lane's byte standard. C1 PASS: any
general single-consonant habit is falsified.

## C2 — venue for the compositional (group-inventory) account

The single-n windows, all byte-confirmed:

- "prenent": 70-12-06, x1 stream-wide, 0-based @1118 (row a6_07), ctx
  `30 69 11 88 [70 12 06] 14 06 11 52`.
- "pasent": 30-06, x4 stream-wide, 0-based @1251 (a7_02), @1327 (a7_04),
  @1561 (a8_01), @1733 (a8_07).
- 12-06 census: exactly 2x (@1119, @1708) — @1708 (row a8_06, `26 [12 06]`)
  is single-n without any 70 involvement; the single-n outcome generalizes
  to the bigram, not just the trigram.
- 70-12 census: exactly 3x (@347, @1118, @1547) — exhausted by the two
  "prenne" and the one "prenent" windows.

Compositional mechanism (evidence packaged, not adjudicated):

1. 94='ne' begins with n. 12='n' + 94='ne' -> "n"+"ne" -> doubled n
   ("prenne", "enne") — the doubling is composed by the group inventory
   itself.
2. 06='ent' begins with a vowel. 12='n' + 06='ent' -> "n"+"ent" -> single n
   ("prenent"); 30='pas' + 06='ent' -> "pas"+"ent" -> single s ("pasent").
3. No 'ss' or 'nent' group exists in the 96-type inventory (checked via the
   successor census of 12: {'06': 2, '16': 3, '33': 1, '34': 1, '41': 2,
   '44': 2, '48': 5, '61': 1, '63': 1, '66': 1, '94': 3, '98': 1} — none
   contributes an initial double-consonant).

Therefore the "missing" consonant in "prenent"/"pasent" is an inventory fact
(no group supplies the extra letter), not a scribal habit; and the
"present" doubled n in "prenne" is likewise an inventory fact (94 supplies
its own n). The same clerk writes both shapes — no habit needed. C2 PASS:
the compositional account is packaged as venue.

## C3 — evidence only, no class named

No value, class, split, or polyvalence is declared in this package. The
compositional account is offered as venue for the red team (§7 honored; 67
remains the sole polyvalence). C3 PASS.

## Adverses

- **red-team venue — gather only.** Honored: this is an evidence-only
  package. No adjudication, no class naming, no red-team docket items
  touched. Nothing here upgrades any standing verdict.

## Standing state

No standing or red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands (rows a1_01/a2_05/a6_07/a7_02/a7_04/a8_00/
a8_01/a8_06/a8_07 offsets unvalidated).

## Verdict: PROMOTE

All three bar clauses pass and the adverse is honored. Package delivered for
the red team. Per §4, promotes require no follow-ups; none proposed (the
red-team input queue is the destination for this material).

## Bookkeeping

- Report: this file.
- Queue: `inventory-doubling-contrast` -> status `verdict`, result `promote`,
  date 2026-10-09 (temp-file + rename; own entry only; no downgrade).
- Lock `locks/inventory-doubling-contrast.lock`: created on start, deleted on
  completion.
