# Battery report: ce-qui-left-closure

**Target:** `ce-qui-left-closure` (priority 3)
**Verdict:** NULL (fence executed)
**Date:** 2026-10-09
**Parent:** battery-ce-qui-87-subject (null, 2026-10-09) — follow-up #3

## Bar (verbatim, pre-registered)

> Bar: all five lefts close with zero new assumptions, or fence the outlier windows.

Restated as numbered clauses before testing:

- **C1:** W1 @148 — left ("67 64 77 84 29") closes as a complete unit with zero new assumptions.
- **C2:** W2 @180 — left ("69 14 24") closes as a complete unit with zero new assumptions.
- **C3:** W3 @1767 — left ("84 09 24") closes as a complete unit with zero new assumptions.
- **C4:** W4 @1775 — left ("62 94 24") closes as a complete unit with zero new assumptions.
- **C5:** W5 @1800 — left ("94 59 37 91 79") closes as a complete unit with zero new assumptions.
- **C6:** Any window failing C1–C5 is fenced with stated cause (per the bar's else-arm), not killed.

Verdict rule: C1–C5 all pass → promote (uniformity established). Else C6 fires → null (fence).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005 never
touched. Confirmed the five "87 64" adjacencies byte-exact at 0-based offsets
148, 180, 1767, 1775, 1800 (matches parent census). Graded each window's left
context for a complete grammatical unit under standing values only.

Adopted premises (all standing or battery-grade, none invented):
banked GT 29=er, 46=que, 11=la, 70=pre, 82=m, 34=i, 40=e;
promoted/granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9),
84=on (A15), 47=ce (A4);
battery-grade 94='ne' (lead), 62='il' (lead, il-62 PROMOTE), 24 finite/modal
verb class (R17-009, red-team), 69 nominal class (class-69-nominal PROMOTE,
battery);
provisional 59='est', 77='le';
frames 37/32/42 predicative (A1), 78 nominal class (R18);
67 et/veut positional rule (sole polyvalence).
14, 09, 91, 23, 26, 66: no standing value or class.

"Closes" = the left context forms a complete grammatical clause/phrase under
the adopted premises with zero new assumptions, such that 87 heads a new unit.

Lock: no fresh lock existed. Lockfile created at start, deleted at end.

## Window-level evidence

**W1 @148 (a1_04):** `... 66 14 74 | 67 64 77 84 29 | 87 64 | 96 ...`
Left: "67 64 77 84 29" = "et" (67; follower 64=qui not infinitive-shaped, so
positional rule gives "et") + "qui" (64, granted) + "l'on" (77=le* + 84=on)
+ "er" (29, banked).
- "qui" needs a finite predicate: none present (29=er is not finite; no 24 in
  the window). The relative clause is incomplete.
- "29=er" needs a verb stem: none ("on"+"er" is not a French word; 84 is a
  promoted word, and §7 bars a word-internal re-reading).
- "l'on" + bare infinitive is ungrammatical in 1841 French (infinitives take
  no overt "l'on" subject).
- Wider left (@133–142: "64 21 65 23 91 65 13 66 14 74") is verbless — no
  rescue from further left.
The parent's passing remark ("an 'on …er' infinitive closes cleanly") does
not survive testing: there is no licensed "l'on + infinitive" construction
and no stem for "er".
**Result: C1 FAIL → fence W1.** Re-open: a licensed stem/governor for the
"29"-infinitive, or a complete-unit re-segmentation of @143–147.

**W2 @180 (a1_05):** `... 87 86 21 | 69 14 24 | 87 64 | 23 ...`
Left: "69 14 24". 69 nominal class (battery PROMOTE, adopted as subject);
24 finite/modal (R17-009); 14 has no standing value or class.
- "[69] [14] [24-fin]" = subject + verb, but 14 needs a role
  (en-pronoun → "[69] en [24]", cf. "il en veut"; adverb; object pronoun).
  Every role is a new assumption (14="en" is pending red team, not granted).
- No longer complete unit avoids 14 (it sits between subject and verb).
**Result: C2 FAIL → fence W2.** Re-open: 14's class/value granted
(e.g., 14="en" ratified → "69 en [24]" closes).

**W3 @1767 (a8_08):** `... 93 06 77 | 84 09 24 | 87 64 | 26 ...`
Left: "84 09 24". 84=on (A15); 24 finite/modal (R17-009); 09 has no standing
value or class ("-ère" value killed; 09~92 split holds, no class granted).
- "on [09] [24-fin]" = subject + verb, but 09 needs a role (adverb, object
  pronoun, particle). No standing role; any role is a new assumption.
**Result: C3 FAIL → fence W3.** Re-open: 09's class granted.

**W4 @1775 (a8_09):** `... 87 64 26 37 78 | 62 94 24 | 87 64 | 59 ...`
Left: "62 94 24". 62='il' (battery PROMOTE il-62, lead in registry — adopted,
flagged as battery-grade, not banked); 94='ne' (battery-promoted, lead);
24 finite/modal (R17-009).
- "il ne [24-fin]" = subject + literary negation ("ne" alone, fully
  grammatical in 1841 French) + finite verb = complete clause. Zero new
  assumptions (all premises adopted).
- Caveats (noted, not blocking): (i) 24's complement valency is
  value-dependent — if 24 is modal-shaped like "veut" it may want an
  infinitive complement; at the class level ("finite verb") the clause shape
  is complete. (ii) Without the battery-grade 62='il' premise the left would
  be subjectless "94 24" and would fence; the closure depends on it.
  (iii) Rival: 24 could govern rightward ("il ne [dit] ce qui…"), but that
  needs 24's value (new assumption), so it does not block the zero-assumption
  closure.
**Result: C4 PASS.** W4's left closes.

**W5 @1800 (a8_10):** `... 86 56 42 | 94 59 37 91 79 | 87 64 | 77 ...`
Left: "94 59 37 91 79". 94='ne'; 59='est*' (provisional); 37 predicative
frame (A1); 91 no standing value/class; 79='tout' (A5).
- "n'est [37] [91] tout": subjectless ("n'est" with no subject); 91 has no
  role; "tout" in final position cannot be adverb (postposed), cannot be
  object of "est", and naturally attaches rightward — "79 87 64" =
  "tout ce qui", the parent's own reading ("'tout ce qui' opens cleanly").
- Extending left ("86 56 42 94 59 37 91 79"): 42 nominal (battery) gives
  "[42] n'est [37]", but "[91] tout" remains stranded.
The "79-tout" does not close the left; it opens the rightward unit.
**Result: C5 FAIL → fence W5.** (Structural: no zero-assumption re-open
visible; "tout" belongs with "ce qui".)

## Per-clause result

- **C1 FAIL** → W1 fenced (no licensed "l'on + infinitive"; "qui" verbless, "er" stemless).
- **C2 FAIL** → W2 fenced (14's role open; one assumption away via 14="en").
- **C3 FAIL** → W3 fenced (09's role open).
- **C4 PASS** → W4 closes ("il ne [24-fin]", zero new assumptions under adopted premises).
- **C5 FAIL** → W5 fenced ("tout" opens rightward; left subjectless with stranded 91).
- **C6 FIRES** → outliers fenced with stated causes.

Left-closure uniformity is NOT established: 1 of 5 windows closes at zero
new assumptions. The parent's "24-verb x3" characterization was loose — W2
and W3 each need one ungranted assumption (14's / 09's role), and only W4's
"62 94 24" is complete under adopted premises.

No standing/red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands (68/70 row offsets unvalidated).

## Verdict: NULL (fence executed)

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `close-14-180-rerun` (P3) — Re-test W2's left ("69 14 24" @177–179) once
   14's class/value is granted. Bar: "69 [14] [24]" closes with zero new
   assumptions iff 14's granted role composes (e.g., 14="en" → "69 en [24]",
   cf. "il en veut"); else fence W2 permanently.
2. `close-09-1767-rerun` (P3) — Re-test W3's left ("84 09 24" @1764–1766)
   once 09's class is granted. Bar: "on [09] [24]" closes with zero new
   assumptions iff 09's granted role composes (adverb / object pronoun);
   else fence W3 permanently.
3. `left-148-reseg` (P3) — Exhaust re-segmentations of W1's left
   ("67 64 77 84 29" @143–147) for a complete-unit parse under standing
   values (word-internal 29, alternative 67 reading, "qui"-scope variants).
   Bar: a complete parse with zero new assumptions, or fence W1 permanently.

## Bookkeeping

- Queue: `ce-qui-left-closure` → status `verdict`, result `null`, 2026-10-09
  (pre-write assert passed — was `queued`/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock `locks/ce-qui-left-closure.lock` created on start, deleted on
  completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
