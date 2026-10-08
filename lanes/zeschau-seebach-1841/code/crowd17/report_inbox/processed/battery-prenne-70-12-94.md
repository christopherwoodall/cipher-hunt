# Battery verdict: prenne-70-12-94

Target: `prenne-70-12-94` — "prenne" composition: 70-12-94 x2 as "pre"+"n"+"ne".
Worker: 9d83fa78-d8ad-40fd-b858-2602b2adfb89. Date: 2026-10-08.
Lock: created 2026-10-08T06:37:43Z, no prior lock (no stale-lock note needed).

## Bar (verbatim, pre-registered before testing)

> resolve iff 'prenne' parses with subject-search at 92 (@1548) and 74 (@348) before either battery promotes; else fence for red team

Numbered clauses:
1. 'prenne' = 70-12-94 parses compositionally as "pre"+"n"+"ne" at both windows (70='pre' banked pencil GT; 12='n' and 94='ne' both battery-promoted pending ratification).
2. Subject search at 92 (@1548 window, row a8_00): a visible, grammatical subject of 'prenne' is found — in the slot between 'que'(46) and the verb, or as a licensed post-verbal / elliptical subject.
3. Subject search at 74 (@348 window, row a2_05): a visible, grammatical subject of 'prenne' is found.
4. Joint 12/94 duality co-test: 12='n' (letter) and 94='ne' (syllable) hold simultaneously in the composition; per the joint constraint neither side may promote at battery level while the duality is unresolved.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). Never `canonical.py`. No invented data. Offsets below are 0-indexed pair positions; the battery's anchor convention points at the 12-cell, so @348 = trigram @347-349 and @1548 = trigram @1547-1549. 70-12-94 occurs exactly 2x stream-wide (closed set).

## Window-level evidence

### Window B — @1547-1549 (row a8_00)

`@1545 00 | @1546 46 | @1547 70 @1548 12 @1549 94 | @1550 92 @1551 45 ...`
= "pour que pre-n-ne 92 45 ..."
Left context: `@1536 62 @1537 06 @1538 21 @1539 62 @1540 93 @1541 88 @1542 77 @1543 78 @1544 43`.

- 00='pour' (A9 class-level grant) + 46='que' (banked pencil) = 'pour que'. The subject slot between 'que'(@1546) and 'prenne'(@1547) is EMPTY (pairs adjacent).
- 92 profile (n=22): predecessors {00 x6, 11 x3, 94 x2, 84 x2, ...}; followers {79/69/60/64/62 x2 each, ...}. 'la 92' x3 (11='la' banked) and '92 qui' x2 (64='qui' banked; 92 heads a relative clause) → 92 is NOMINAL (feminine noun-shaped), not subject-shaped. 'pour 92' x6 and 'on 92' x2 noted but do not make 92 a subject here.
- A postposed subject after 'pour que' is ungrammatical in French ('pour que' requires normal S-V order; inversion is not licensed). Subject ellipsis across 'pour que' is not licensed either, and no impersonal 'il' pair is present.
- Sibling control: the other 'pour que' window @1680 fills the subject slot ('pour que tout [65]', 79='tout' granted) — @1545 leaves it empty, anomalous by comparison.

Subject search at 92: **FAIL**. (Confirms the pre-registered adverse: "92 follows @1548, unresolvable" — now with cause: 92 is nominal, and no grammatical subject position exists.)

### Window A — @347-349 (row a2_05)

`@346 06 | @347 70 @348 12 @349 94 | @350 74 @351 67 ...`
= "[06] pre-n-ne 74 et/veut ..."
Left context: `@343 43 @344 87 @345 01` ("43 ce [01] [06]").

- NO subjunctive trigger in the clause: the nearest 46='que' is @309 ('20 17 46 84 24'), 38 pairs back across multiple finite verbs ('est'@316, provisional) — it cannot govern 'prenne' @347.
- Pre-verbal 06: 'ent'/'-ment' lead (ent-06: '[X]-ent la [NOUN]' x3, 'prennent' = 70-12-06) — a verb ending / adverb, not subject-shaped.
- 74 profile (n=34): predecessors {74 x6 (self-doubled), 49 x5, 94 x3, ...}; followers {74 x6, 45 x3, 46 x3, 62 x3, 67 x2, 77 x2, ...}. '74 le' x2 (@212 '74 77 78', @1677 '74 77 44'; 77='le' provisional) and '74 que' x3 (@418, @635, @693) → 74 is VERB-shaped (takes 'le' objects and 'que' clauses), not subject-shaped. 'prenne 74' as V+V is ungrammatical.
- The 'prennent' re-parse (70-12-94-74 = pre-n-ne-nt, 74='nt') is unpromoted speculation: 74's contact profile ('74 le', '74 que', self-doubling x6) does not support a verb-ending reading, and no value for 74 is granted.

Subject search at 74: **FAIL** — no trigger, no subject-shaped candidate (06 is an ending/adverb, 74 is verb-shaped).

## Per-clause verdicts

1. Composition "pre"+"n"+"ne": **PASS** — both trigrams spell 'prenne' cleanly under standing values (70='pre' GT, 12='n', 94='ne'); neither window forces the composition false; no cleaner rival demonstrated on these frames.
2. Subject search at 92 (@1548): **FAIL** — slot empty, 92 nominal, no licensed post-verbal/elliptical subject.
3. Subject search at 74 (@348): **FAIL** — no trigger, no subject-shaped candidate.
4. 12/94 duality co-test: **UNRESOLVED** — the composition spells correctly but cannot be clausally integrated at either window; per the joint constraint neither 12='n' nor 94='ne' may advance on this evidence.

## Adverses

- "'que/pour prenne' needs a visible subject (92 follows @1548, unresolvable)" — CONFIRMED and fenced with cause (92 nominal: 'la 92' x3, '92 qui' x2; §-level grammar blocks postposed/elliptical readings). Not ignored.
- "battery flagged the same 12/94 duality for red-team adjudication" — the duality is NOT resolved at battery level; fenced for the red team per the joint constraint. Neither the ne-94 battery promote nor the n-e-12-48 battery promote is downgraded by this verdict (both stay "promote, pending ratification"); this null is scoped to the joint composition + subject bar only.

## Verdict: NULL — fence for red team (headline)

The bar's resolve condition failed at both windows (clauses 2 and 3), and the bar routes that outcome to fencing, not killing: no window forces the composition false (clause 1 passes), so kill grade is not met. The 12/94 duality cannot be co-tested to resolution at battery level — escalated to the red-team adjudication queue. This worker does not touch that queue; the supervisor routes the fence.

## Follow-ups (null regenerates work)

1. **prenne-92-noun** (priority 2): name 92's value/class. Evidence: 'la 92' x3 + '92 qui' x2 → feminine-noun lead; reconcile 'on 92' x2 and 'pour 92' x6. Bar: name 92 iff one class covers >=80% of its 22 windows. (If 92 = noun, @1545 reads 'pour que [S] prenne 92' = V + direct object with S still open — narrows the search to S.)
2. **prenne-subject-S1545** (priority 1): find the subject of 'pour que … prenne' @1545, or demonstrate the clause is genuinely subjectless. Re-examine @1536-1546 ('62 93 88 77 78 43') for any grammatical (even non-canonical) subject parse. Bar: resolve iff a subject parse is found under standing values with zero contradiction, else confirm subjectless with stated cause (strengthens the fence).
3. **prenne-trigger-348** (priority 2): locate the subjunctive trigger for @347-349 via full clause-boundary analysis @300-347; test the '74 = verb' reading's consequence ('prenne 74' ungrammatical → forces re-parse of the trigram's right edge). Bar: resolve iff a trigger+subject parse is found, else confirm triggerless with stated cause.
