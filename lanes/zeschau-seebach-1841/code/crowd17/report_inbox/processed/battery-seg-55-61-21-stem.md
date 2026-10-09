# Battery verdict: seg-55-61-21-stem

**Verdict: PROMOTE** (discriminator success — the window is decided as bare stem; promotes no value, kills no value).

## Bar (verbatim from battery-queue.json)

"(a) full-row parse of a7_00 around @1205: `58 47 43 55 61 21 65` = \"[58] ce [43] [55-61] NOUN [65]\"; (b) decide whether 55-61 is a bare stem (\"prend\" + noun object) or 94's absence breaks the unit — one grammatical parse either way; (c) keep 21=NOUN class promoted"

## Numbered clauses (pre-registered before testing)

1. (a) Produce ONE grammatical parse of the 7-gram `58 47 43 55 61 21 65` with 47=ce, 21=NOUN class, 65 as slotted.
2. (b) Decide: 55-61 is a bare finite stem ("prend" + noun object), OR 94's absence breaks the 55-61-94 word unit. Account for the missing 94 either way.
3. (c) 21=NOUN class retained (registry `21 -> ["noun","cls"]` untouched).

## Method

Read BATTERY-PROTOCOL.md first; created `locks/seg-55-61-21-stem.lock`
(agent b2c667e1…, 2026-10-09T04:00:51Z) on start — no stale lock existed.
Re-derived the repaired 1,847-pair / 96-type stream from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed per `code/side-keyhunt/repair_parse.py`: byte-exact
`[s[i:i+2] for i in range(o, len(s)-1, 2)]`). `canonical.py` never touched.
R5005, sealed gates, red-team queue untouched. Every count re-derived;
no prior counts trusted.

**Offset convention:** the target brief's "@1205" is the 0-based stream index
of the 55 token (matches battery-seg-55-61-94-word's table). 1-based
equivalents: 58=@1203, 47=@1204, 43=@1205, 55=@1206, 61=@1207, 21=@1208,
65=@1209, all on row a7_00 (0-based row start 1191).

## Window-level evidence

### Row a7_00 (0-based 1191–1218), byte-verified

`46 07 24 82 16 96 82 16 64 29 45 | 58 47 43 55 61 21 65 | 64 59 32 48 96 45 36 77 83 92`

Target 7-gram (0-based 1202–1208): `58 47 43 55 61 21 65`.

### Census facts (re-derived)

- `55 61` bigram: exactly **3x** stream-wide — @577/0-based-576 (a3_02,
  `…13 55 61 94 82…`), @1168/0-based-1167 (a6_09, `…13 55 61 94 87…`),
  @1206/0-based-1205 (a7_00, `…43 55 61 21 65…`). Two carry 94, one does not.
- `61 21` bigram: **2x** — this window and @1456 (a7_09,
  `33 46 92 62 61 21 67 86 66`; 61 WITHOUT 55 there).
- `21 65` bigram: **4x** — @135 (a1_04, after 64=qui), @372 (a2_06, after
  06=ent), @1208 (this window), @1530 (a8_00, after 87=ce, 46=que).
  Heterogeneous frames: no fixed compound; two adjacent nouns.
- 61's followers: 96 x2, 59 x2, 94 x2, 21 x2, 20, 42, 70, 88 (n=18).
  The only two 94-followers are the two formula windows.
- 55's followers: 81 x6, 61 x3, 83 x2, 68 x1 (n=12).

### Standing values used

47="ce" (A4 granted), 64="qui" (promoted), 96="par" (promoted),
59="est" (provisional), 77="le" (provisional), 21=NOUN class and
65=NOUN class (table-registry.json `["noun","cls"]`), 32 predicative
frame (A1), 36=NOUN class (round-18).

## Clause 1 (a): PASS — one grammatical parse

`[58] ce(47) [43] prend(55-61) [21] . [65] qui(64) est(59) [32]e(48) par(96) [36] …`

- **"ce [43]"** — subject NP: 47="ce" determiner + 43 as head noun.
  43's battery profile is noun-shaped in 15/16 windows ("par [43]" x2,
  "43 pour" x3, "43 00" x3); the single word-internal window (@22,
  "43 29" = "[43]er" infinitive) is the fenced conditioned-split residual
  (venue: red-team 43 docket). Noun-class at this window is the working
  profile; value stays open.
- **"prend" = 55-61** — finite 3sg present of *prendre*, agreeing with
  singular "ce [43]". No 94 because the verb is INDICATIVE, not
  subjunctive: the left context (`58 47 43`) carries no subjunctive
  trigger (no "que", no "pour que"), so "prenne" would be ungrammatical
  here and "prend" is the expected form.
- **"[21]"** — direct object, noun class per registry. "prendre + DO" ✓.
- **Unmarked clause boundary** after 21 (the cipher carries no punctuation
  anywhere; unmarked boundaries are the norm, not a cost).
- **"[65] qui est [32]e par [36]"** — 65 (noun class) as antecedent of the
  relative "qui(64) est(59) [32]e(48)", with passive agent "par(96)
  [36-noun]". Fully grammatical 1841 French.
- **58** left as the bar's own "[58]" slot: left-edge residual, fenced with
  cause (belongs to the prior clause or an interjection/vocative slot;
  58's class is open — pre 85 x3, fol 47 x2 — and deciding it is outside
  this bar).

English gloss: "this [43] takes [21]. [65], which is [32]ed by [36] …"

Rival parses killed at this window:
- 55-61 as subjunctive "prenne" (no trigger → ungrammatical).
- 55-61 as infinitive "prendre" (no finite verb in the clause →
  ungrammatical).
- 55-61 as noun/adjective ("ce [43] [55-61] [21]" = two head nouns →
  ungrammatical; no determiner for a second NP).

## Clause 2 (b): PASS — bare stem; 94's absence is EXPLAINED, the unit is not broken

**Decision: 55-61 is the bare finite stem "prend" + noun object.**

94's absence does not break the 55-61-94 word unit. The two 94-carrying
windows (@576, @1167) sit in the `78-45-13-55-61-94` formula with
"prenne"-compatible (subjunctive-frame) readings; this window has no
subjunctive trigger, so the finite "prend" appears. Indicative/subjunctive
alternation (*prend* / *prenne*) is the ordinary morphology of *prendre* —
the missing 94 is the expected finite form, not a hole in the unit.

**Residual flagged (not decided):** the letter-level segmentation is now
tensed. The word battery framed 55="re" + 61="pren" + 94="ne"
("reprenne"); the "prend" reading wants 55="pre" + 61="nd" (or 55="pr" +
61="end"). Both segmentations cannot hold at once — a §7/red-team
segmentation question, not a battery-grade contradiction (no standing
verdict fixes 61's letters; 61's locus-level "premier" @1556 is a separate
window). The UNIT (55-61-94 as a "prenne"-family word where 94 occurs)
survives this window; its internal letters do not.

Supporting note: @1456 shows `62 61 21` — 61 followed by 21 WITHOUT 55 —
so 61 carries verbal force outside the 55-61 pair too. Consistent with,
not required by, the bare-stem decision.

## Clause 3 (c): PASS — 21=NOUN class kept

21 is used as the direct-object noun ("prend [21]"); the registry cell
`21 -> ["noun","cls"]` is untouched. Nothing downgraded.

## Adverses answered

- **43 unknown:** noun-class profile supports the "ce [43]" subject;
  value open, fenced with cause (red-team 43 docket owns it).
- **58 unknown:** left-edge slot per the bar's own skeleton; fenced with
  cause (prior-clause/interjection residual).
- **65 unknown:** noun-class supports the relative antecedent; value
  open, fenced with cause.
- **55-61-94 word claim undemonstrated:** acknowledged — this battery
  neither demonstrates nor breaks it. The claim stands exactly where
  battery-seg-55-61-94-word left it (NULL, three follow-ups).

## Verdict: PROMOTE (discriminator success)

All three clauses pass; every listed adverse is answered (parsed cleanly
or fenced with stated cause — none ignored). No standing verdict is
contradicted or downgraded; no polyvalence declared (§7 intact);
no value promoted.

---
*Worker: battery agent b2c667e1 (supervisor dispatch). Lock created
2026-10-09T04:00:51Z, deleted on completion. Stream: repaired 1,847-pair
parse (repaired_offsets.json + upstream-ct_R5005.txt). canonical.py
untouched; R5005 and sealed gates untouched.*
