# Battery report: `doublet-589-97-role` — verdict PROMOTE (97 = VERB class)

## Bar tested (verbatim, pre-registered)

"pass iff >=2 independent legs name one class (verb/noun/other) with zero kill-grade contradictions; fence iff unclassifiable"

Numbered clauses:
- **C1** (≥2 independent legs name one class): PASS — 4 clean "pour"-infinitive verb legs at independent loci (@2, @288, @588, @1823), plus 3 verb-consistent supporting legs (@94, @525, @1412).
- **C2** (zero kill-grade contradictions): PASS — no window forces 97 non-verbal. @751 is letter-tier ("97e" forced), a positional split at a different locus, precedent-legitimate per the 88/52 split treatment; @299/@566 are ambiguous, not forced-false.
- **C3** (fence iff unclassifiable): does not fire.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. Censused all 10 windows of 97 byte-exact with ±5 context (0-based @-offsets). Standing values per §7: 00="pour" granted word (A9), 46="que"/40="e" pencil GT letters, 47="ce" granted (A4), 69 noun-class red-team grant (R19-109).

## Findings — window-level evidence

**Clean verb legs (4, independent loci, "pour"-infinitive frame):**
- **@2** (a1_00): `09 | 00=pour [97] 51 | 47=ce 41` — "pour" is a granted word, boundary forced; 97 word-tier per adverses; bare word directly after "pour" must be infinitive (noun would need a determiner). VERB.
- **@288** (a2_03): `89 28 | 00=pour [97] 09 | 64=qui 29` — same frame, distinct locus. VERB.
- **@588** (a3_02): `18 14 | 00=pour [97] 41 41 | 09` — same frame, distinct locus; this is the doublet locus. VERB.
- **@1823** (a8_11): `09 19 | 00=pour [97] 00=pour | 86 29` — same frame, distinct locus. VERB.

**Verb-consistent supporting legs (3, boundary-undecided but verb-plausible):**
- **@94** (a1_02): `41 98 81 [97] 46=que 29 85` — "[97] que" finite-verb + subordinate-clause frame (46=que pencil GT). "81|97" boundary undecided (81 open), so supporting only.
- **@525** (a3_00): `91 77 06 55 81 [97] 47=ce 44 59` — "[97] ce" transitive-verb + object frame (47=ce granted). "81|97" boundary undecided, supporting only.
- **@1412** (a7_07): `95 46 52 42 16 [97] 69-N 74 34` — "[97] [69-noun]" verb + nominal-object frame (69 noun-class grant). "16|97" boundary undecided, supporting only.

**Split / ambiguous windows:**
- **@751** (a5_03): `85 28 00 64 02 [97] 40=e 67 11 70 82` — 40="e" is a letter cell and cannot stand alone; right-attachment "e"+"et/veut" composes no word, so 40 attaches left: "[97]e" is one word. **97 is letter-tier (word-internal syllable) here — forced by bytes + lexicon.** Positional split, not a contradiction of the verb loci.
- **@299** (a2_04): `16 01 11 78 40=e [97] 86 91 18` — 40 must be word-internal; "78e" (78 open) vs "e97" both geometrically possible. Ambiguous.
- **@566** (a3_02): `67 11 43 24 80 [97] 13 76 45` — 80 verb-frame open; noun-object reading available but not forced. Ambiguous.

**Rival arms:**
- Noun: zero legs — no determiner (11/77/47/87) precedes 97 in any of the 10 windows. Unsupported, fenced by absence.
- Uniform word-tier verb: contradicted at @751 only → resolved as positional split (see below), not a global kill.

**Adverses answered:** the standing adverse ("'00 97 X' slot is word-tier in all 4 frames") is adopted and consistent — all 4 "pour" legs are word-tier verbs, confirming it.

## Scope

- Promotes **97 = VERB class** (4 clean + 3 supporting legs, zero kill-grade contradictions).
- **Positional split recorded:** 97 is verb-word at the verb loci but letter-tier (syllable) at @751 ("97e" forced), ambiguous at @299. This mirrors the established 88 and 52 non-uniformity; any formal split declaration is red-team venue (suggested docket: split-97).
- **Doublet feed:** at the doublet locus @588, the parse is now "pour [97-VERB] 41 41 09" — 97's verb class constrains the doublet resolution (companion targets doublet-589-09-role / doublet-589-97-role).
- No standing or red-team verdict contradicted; §7 intact (class split is positional, not a second value declaration).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-doublet-589-97-role.md`
- Queue: `doublet-589-97-role` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; own entry only; no downgrade)
- Lock: created on start (agent d02e1e72-7559-4833-9ac5-e9ea97c01dea, 2026-10-09T17:58Z), deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
