# Battery report: prof-35 — 35 = noun (class-level)

Worker: battery worker (prof-35). Date: 2026-10-09.

## Bar (verbatim from battery-queue.json)

"resolve iff 35's class is stated with the @707-711 subject slot parsing; else fence 35 as the blocker, not the leg"

## Bar as numbered clauses (pre-registered before testing)

1. 35's class is stated (a single class covering all 10 windows of 35 on the
   repaired stream).
2. The @707-711 subject slot parses with 35 in the subject role under standing
   values: 1-based @707-711 = `21 35 53 12 48` ("21 35 donne"), continuing
   @712 = 71 ("35 donne 71").

Adverses (from queue): "35's class open; 'donne' agreement conditional on
singularity".

## Method

Read BATTERY-PROTOCOL.md first; created `locks/prof-35.lock` on start.
Re-derived the full stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (1,847 pairs / 96 types verified;
`canonical.py` never touched). Every @-offset below is 1-based pair index on
the repaired stream. R5005, sealed gates, and the red-team adjudication queue
untouched. §7 obeyed: no new polyvalence declared.

Standing values used: 11=la (GT), 87=ce (promoted), 64=qui (promoted),
79="tout" (A5), 84="on" (A15), 96=par (promoted), 17=fois (promoted),
12="n"/48="e" (promoted letters), 59="est" (provisional), 77="le"
(provisional). 53="don" is lead-level (compositional, from
battery-donne-168-708-leg), used only where stated.

## Window-level evidence: 35 census (n=10, all windows)

| @ (1-based) | row   | frame (35 bold)                                   |
|-------------|-------|---------------------------------------------------|
| 57          | a1_01 | 11 79 85 58 **35** 53 12 41 08                    |
| 157         | a1_04 | 46 66 84 26 **35** 58 35 93 52 94 24              |
| 159         | a1_04 | 84 26 35 58 **35** 93 52 94 24                    |
| 708         | a5_01 | 20 12 66 21 **35** 53 12 48 71                    |
| 836         | a5_06 | 11 77 76 59 **35** 56 17 98 20                    |
| 1009        | a6_02 | 47 91 11 52 **35** 18 79 80 78                    |
| 1293        | a7_03 | 11 17 84 59 **35** 94 52 80 04                    |
| 1360        | a7_06 | 06 52 37 64 **35** 13 92 62 94                    |
| 1640        | a8_04 | 74 87 74 74 **35** 56 12 33 98                    |
| 1806        | a8_10 | 64 77 84 59 **35** 94 52 80 04                    |

Contact summary. Predecessors: 58, 26, 58, 21, 59, 52, 59, 64, 74, 59.
Successors: 53, 58, 93, 53, 56, 18, 94, 13, 56, 94.

Decisive frames (under standing values):
- "est 35" x3 (@836, @1293, @1806) — 59="est" (provisional) + 35 in
  predicate-nominal position. @1293 and @1806 share the tail
  "84 59 35 94 52 80 04" = "on est 35 ne [52] [80] [04]".
- "qui 35" @1360 — 64="qui" (promoted) + 35 as the relative's subject slot.
- "35 donne" @708 — 35 as subject of the finite 3sg "donne"
  (53-12-48 compositional, lead-level).
- "35 don-[41]" @57 — 35 as subject of the 53-12-41 donne-family word.

## Class elimination (all 10 windows)

- **Verb: DEAD.** "est 35" (être + finite verb ungrammatical), "qui 35"
  (relative subject cannot be a finite verb), @57/@708 would be verb+verb.
- **Adjective: DEAD.** "qui 35" (no adjective can be a "qui"-relative
  subject), "35 donne" (an adjective cannot be the subject of a finite verb).
- **Adverb: DEAD.** "qui 35" and "35 donne" both ungrammatical for adverbs;
  "est 35" is at best strained.
- **Pronoun: DEAD.** "est 35" (être + bare pronoun needs "ce": "c'est moi"),
  "qui 35" ungrammatical.
- **Preposition: DEAD.** "est 35", "35 donne", "qui 35" all fail.
- **Noun: SURVIVES all 10.** Predicate-nominal after "est" x3, relative
  subject after "qui", subject of "donne"/"don-[41]" x2, neutral elsewhere
  (@1009, @1640, doubled @157/159).

Noun is the unique surviving class. No window forces a non-nominal 35 under
any standing value.

## Per-clause pass/fail

1. **35's class stated: PASS.** 35 = **noun** (class-level; value open).
   Stated at class level only — no value is attached, no number is decided.
2. **@707-711 subject slot parses: PASS (conditional).** Under the
   lead-augmented standing set (12="n"/48="e" promoted, 53="don"
   compositional per the donne leg), `21 35 53 12 48` reads
   "21 [35-NP] donne" with 35 as the singular noun subject and 71 (@712) as
   the direct object. Nothing at the window or in 35's census contradicts
   this parse.

Adverses answered:
- "35's class open": ANSWERED — noun, by unique-class elimination across
  all 10 windows.
- "'donne' agreement conditional on singularity": ANSWERED as a condition,
  not a kill. 35's number is undetermined from bytes (no agreement evidence
  anywhere in the census); plurality is NOT proven, so the leg-grade kill
  path ("if 35 proves plural") does not fire. The singular-subject reading
  of "donne" stands conditionally, as before.

## Standing-state check

- No red-team verdict on 35 exists; 35 has no registry cell. Nothing
  contradicted or downgraded.
- battery-donne-168-708-leg (verdict/null) stands untouched: its naming
  clauses (21/71 named) still fail — this battery names neither 21 nor 71.
- battery-prof-53 (verdict/null) stands untouched.
- No polyvalence declared (§7 intact).

## Verdict: PROMOTE (class-level)

35 = **noun**. Value open; number undetermined. Battery grade; needs
red-team ratification like every battery promote.
