# Battery A10 — 33's que-valency + the 33+29 composition

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder Q4 (next-token-findings-que-ce.md) + finder §6
(next-token-findings-parle-and-rest.md).
Standing: 33=INF class (precedes 29 ×5, pre=00 ×8 "pour", suc=29 ×5);
A9 confirmed 00="pour" and 86's INF-class by the 33-parallel.

## Pre-registered bar (written BEFORE touching data)

**Q4 — que-valency:**
- **CONFIRM** the valency constraint iff: (a) both 33-46 windows (@1452,
  @1625) parse as "[33-infinitive] que [clause]" with zero contradiction
  (check the "67" predecessor — the et/veut fork — and 46's "que"-clause
  continuation); (b) 33→46 occurs globally at a rate consistent with a
  que-taking infinitive (not a one-off: ≥2 windows, which (a) already
  gives, plus no anti-que-valency frame).
- This NARROWS 33's candidate set to {dire, penser, croire, savoir,
  vouloir, falloir…} — it does not name the verb. Do not promote a value.

**§6 — 33+29 = stem+ending:**
- **CONFIRM** the composition iff: (a) all 33-29 windows audit as
  stem+"er"-ending with no contradiction; (b) 33-alone windows vs 33-29
  windows show the expected split (33-alone = whole infinitive or
  stem+other-ending; 33-29 = stem+"er") — OR state that the audit cannot
  distinguish and HOLD.
- **Tension to resolve:** "pour 33" ×8 has 33 WITHOUT 29 — if 33 is a
  STEM, "pour [stem]" without ending is ungrammatical; if 33 is the whole
  infinitive, 33-29's 29 is unexplained. The audit must pick: stem or
  whole-infinitive, with cause. Do not leave both live silently.

## Data

### Q4 — 33-46 ×2 (re-derived)

- @1451–1456: `36-67-33-46-92-62` = "[36] [67] [33] que [92]…" 
- @1624–1629: `66-67-33-46-56-69` = "[66] [67] [33] que [56]…"
Identical "67-33-46" trigram ×2, different tails. Both parse as
"[67] [33-infinitive] que [clause]" with zero contradiction (the 67
et/veut fork doesn't block: "et [33] que" / "[veut→?] [33] que" both
leave 33+que intact; the valency is 33's, not 67's).
33→46 globally: exactly these 2 (2/25) — consistent with a que-taking
infinitive (que-clauses are infrequent by nature), no anti-que frame.
**Candidate set narrowed to que-taking infinitives:**
{dire, penser, croire, savoir, vouloir, falloir, voir…}. No value promoted.

### §6 — 33-29 ×5 audit

| pos | window | stem+"er" read |
|---|---|---|
| @273 | 67-33-29-89-84 | "[67] [33]er [89]" ✓ infinitive-shaped |
| @626 | 37-33-29-87-78 | "[37-adj] [33]er ce [78]" ✓ ("[33]er ce" — see below) |
| @1232 | 47-33-29-85-56 | "ce [33]er [85]" ✓ ("ce"+"[inf]" — cf. A4's 47→33) |
| @1424 | 67-33-29-87-63 | "[67] [33]er ce [63]" ✓ ("[33]er ce" ×2 with @626) |
| @1477 | 67-33-29-82-16 | "[67] [33]er m[16]" ✓ |

All five audit as stem+"er" infinitives. "[33]er ce" ×2 (@626, @1424) is
a recurring sub-frame.

### The tension: stem vs whole-infinitive

- **For whole-infinitive (1-syllable: dire/croire/voir):** "pour 33" ×8
  grammatical ("pour dire"); que-valency ×2 fits {dire, croire, voir};
  33-alone successors diverse (21×3, 16×2, 42×2, 79×2, 00×2, 46×2…).
  Explains 10/25 windows cleanly.
- **For stem:** 33-29 ×5 ("[33]er"); 33→29 is a top successor (5/25).
- **Against whole:** 33-29's 29 unexplained (20% of windows).
- **Against stem:** "pour 33" ×8 unexplained (32%; "pour"+bare stem is
  ungrammatical).
- The "dire"-shaped hypothesis (33="dire"): explains "pour dire"×8 +
  "dire que"×2 but dies on 33-29×5 ("dire"+"er" is nothing). Not promoted;
  recorded as the leading partial.

## Verdicts

- **Q4 que-valency: CONFIRM.** Both windows parse; 33→46 ×2 with no
  anti-que frame. 33's candidate set is now que-taking infinitives only.
  (Value NOT named — "dire" is the leading partial, unpromoted.)
- **§6 composition: HOLD.** Stem vs whole-infinitive is genuinely
  unresolved: 8 windows need 33=whole ("pour 33"), 5 need 33=stem
  ("[33]er"). Forcing either reading orphans 20–32% of the windows.
  The 29-after-33 ("[33]er ce" ×2) goes to a dedicated battery —
  do not re-litigate here.
- **A9 cross-feed:** 00="pour" + 33=INF is now double-confirmed
  ("pour [33]" ×8); 86's INF-class (A9) stands on the 33-parallel.
