# Battery report: conj-02-306

Target: `conj-02-306` — test 02 as conjunction at @305 and @858 jointly.
Date: 2026-10-09. Worker: battery subagent.

## Bar (verbatim)

"name a French conjunction fitting "[88] [02] [88]" while surviving "on [02] faire"; fence if none parses"

## Bar restated as numbered pass/fail clauses

- C1: Name a French conjunction that fits "88 [02] 88" at @305 (0-based).
- C2: The same conjunction survives "on [02] faire" at @858 (0-based).
- C3 (else-branch): If no conjunction parses at both windows, fence the conjunction claim.

## Method

BATTERY-PROTOCOL.md read first. Lock `locks/conj-02-306.lock` created on start,
deleted on completion. Repaired stream re-derived in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(1,847 pairs / 96 types verified). `canonical.py` never touched. All offsets
0-based. R5005, sealed gate instances, red-team adjudication queue untouched.

Premises adopted as premises (not re-litigated): 84="on" (A15 grant),
64="qui" (GT), 46="que" (GT), 29="er" (GT), 80/89 verb-frames (A8),
88=verb class (battery-grade, prof-88), 24="faire" verb (ne-24-profile
battery promote; the 24-en-verb-conflict is noted but the C2 result is
independent of it — see below).

## Window evidence

- @305 (row a2_04, mid-row — no row edge within ±10): `... 89 88 | 02 | 88 20 17 ...`
  (0-based @302–307 = 18, 89, 88, 02, 88, 20, 17).
- @858 (row a5_07, mid-row — no row edge within ±8): `... 48 84 | 02 | 24 49 74 ...`
  (0-based @856–861 = 48, 84, 02, 24, 49, 74).

## Per-clause results

- **C1: PASS (in isolation).** At @305, "88 [02] 88" is coordination of
  like-with-like: 89 is a granted verb-frame (A8), 88 is verb-class
  (battery-grade). The French conjunctions "et", "ou", "ni", "mais" all fit:
  "[V] et/ou/ni/mais [V]" is grammatical VP coordination. The class is
  conjunction-shaped at this window regardless of 88's final value.

- **C2: FAIL at kill grade for the uniform value.** At @858, "on [02] faire"
  admits no French conjunction:
  - Coordinating: "on et/ou/ni/mais/car/donc faire" — ungrammatical. No
    conjunction can stand between a subject pronoun and its verb.
  - Subordinating: "on que faire" — 46="que" is the que-cell, and "on que
    faire" is ungrammatical in any case.
  - The 24-conflict does not rescue it: under 24="en" (en85-gerund-reaudit
    A3), "on [02] en" = "on et/ou en" — dead identically. The conjunction
    reading is independent of 24's value.
  - Boundary rescues all strand "on" verbless (mid-row a5_07, no byte
    boundary):
    - boundary before 02 → "…[32]e on. | [02] faire…" — left context is
      "32 48" = "[32]e" (verb lexeme 32, feminine past participle per
      R17-008); it cannot govern a following verbless "on";
    - boundary after 02 → "on [02]. | [24]…" — "on et/ou." is dead;
    - boundary before 24 → "on [02] | faire" — "on et" as a unit is dead.

- **C3: FIRES.** No French conjunction parses at both windows; the
  conjunction claim for 02 is fenced at battery grade.

## Adverses

None listed. Note: 02's class inventory per 02-class-609's NULL (verb-selecting
"qui [02]" @609/@750 vs anti-verb @305/@858) is the standing frame; this
battery fences the conjunction arm specifically and does not re-litigate the
§7 split candidacy.

## Verdict

**NULL — fence the conjunction claim.** The claim "02 is a conjunction" is
not kill-grade dead in every window (@305 genuinely fits "et"/"ou"
coordination), but the bar's uniform requirement (one conjunction surviving
both @305 and @858) cannot be met: @858 is conjunction-hostile under every
reading without inventing unevidenced boundaries that strand "on" verbless.
02's class stays open with the 02-class-609 §7 split candidacy.

## Follow-ups proposed (for supervisor queuing)

1. `adv-02-858` (P3) — test 02 as adverb/modal at @858: "on [02] faire" =
   "on [02-modal] faire" shape (cf. "on peut/veut/doit faire"); name a modal
   or fence.
2. `qui-02-750-parse` (P3) — deep parse of the second "qui [02]" window
   (@750); if the relative-"qui" verb requirement dissolves there, the
   anti-verb side of 02 wins outright (proposed by 02-class-609, verified
   absent from the queue).
3. `sub02-wordinternal` (P3) — sub-lexical 02 composing with right neighbor
   (compositional account dissolves the class question; proposed by
   02-class-609, verified absent from the queue).

## Standing-state check

No red-team verdict on 02 exists; nothing contradicted or downgraded. §7
intact. The standing kills (09/92 "-ère" value, {48,94} homophone-set, etc.)
and holds (45="ce" A11, 67 sole polyvalence) are untouched.
