# Battery report: pasent-subject-26-56

Target: `pasent-subject-26-56`. Claim: decide 26/56 as 3pl subjects at the four
30-06 windows (@1251/@1327/@1561/@1733 0-based). Date: 2026-10-09. Stream:
repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`;
1,847 pairs re-verified). Never used `canonical.py`. R5005, sealed gates,
red-team queue untouched.

Adverse ("coordinate with spell-single-consonant; do not duplicate") —
answered: this battery adopts the spell battery's window inventory (W1–W5),
its W4 exclusion ("la [26] passent" ungrammatical), its per-window subject
requirement (W2 needs 26, W3/W5 need 56), and its compositional letter
account ("pas"+"ent" as letter groups, no clerk habit). The spelling argument
is not re-derived. This battery decides ONLY the subject-class question.

## Bar (verbatim, pre-registered)

"if neither can be 3pl, the 'passent' reading dies grammatically and 30-06
must re-segment"

Numbered clauses (fixed before testing, not modified after):

1. C1 — 26 admits a 3pl-subject reading at @1251: "46 26 30 06" parses as
   "que [26-3pl-subject] passent …" with no standing-value contradiction.
2. C2 — 56 admits a 3pl-subject reading at @1327 and @1733: "98 56 30 06"
   and "01 56 30 06" parse as "[56-3pl-subject] passent …" with no
   standing-value contradiction.
3. C3 — control: @1561 ("11 26 30 06" = "la [26] passent") is excluded as a
   'passent' window under any subject assignment (spell-battery finding,
   confirmed byte-exact, not re-litigated).
4. C4 — conditional: if C1 and C2 both fail, the 'passent' reading dies
   grammatically at all four windows and 30-06 must re-segment.

## Method

Full census of 26 (n=17) and 56 (n=23) on the repaired stream. Subject test:
a 3pl subject must be a plural pronoun or plural nominal (French does not
pro-drop; bare singular nouns cannot be 3pl subjects). Each live class
hypothesis for 26/56 was tested against its byte-exact windows. A pronoun
reading is a new value: under §7 (67 et/veut is the sole true polyvalence)
declaring it at battery level is barred — only the red team can declare a
second polyvalence. Standing values used: 11='la', 46='que', 64='qui',
84='on', 87/47='ce', 94='ne' (battery-promoted), 12='n', 06='ent' (promoted),
30='pas' (promoted, conditional), 17='fois', 00='pour', 23~26 SPLIT (A2).

## Window-level evidence

Target windows (byte-confirmed on the repaired stream):

- W2 @1251 (a7_02): `16 00 67 46 | 26 | 30 06 | 65 46 01 61 31 29`.
  "46 26" is the ONLY "que 26" bigram stream-wide. Subject of "passent"
  must be 26 (only token between "que" and the verb).
- W3 @1327 (a7_04): `80 08 62 98 | 56 | 30 06 | 62 94 70 52 39 83`.
  Byte check: @1327=30, @1328=06, @1329=62, @1330=94, @1331=70.
  Subject of "passent" must be 56 (or 98 — see adverse A1 below).
- W4 @1561 (a8_01): `61 40 17 11 | 26 | 30 06 | 60 71 50 29 24 74`.
  "la [26] passent" — excluded (C3).
- W5 @1733 (a8_07): `24 30 15 01 | 56 | 30 06 | 60 12 48 52 86 12`.
  "01 56" @1731-1732. Subject of "passent" must be 56 (01 is
  adverb/participle-shaped — 'ci'/'faisant' candidates, ci-01-value battery;
  not subject-shaped).

26's class evidence (n=17):

- Noun legs: "11 26" = "la [26]" x2 @239 (a1_03: "41 17 11 26 12 16 56")
  and @1559 (a8_01: "40 17 11 26 30 06 60"). Banked 11='la' + 26 =
  feminine singular nominal. The noun-26 battery reads "fois la [26]" as
  the absolute "une fois la [N]" (2 legs). A feminine singular noun cannot
  be a 3pl subject — number clash.
- Verb legs: "64 26" = "qui [26]" x2 @530 (a3_01: "59 37 64 26 32 16 08")
  and @1768 (a8_08: "24 87 64 26 37 78 62") — 26 in the finite-verb slot
  after relative "qui". "94 26" @842 (a5_06: "20 62 94 26 12 16 00") —
  26 directly after promoted 94='ne'; "ne" is followed by the finite verb.
  "84 26" @154 (a1_04: "46 66 84 26 35 58 35") — 26 directly after promoted
  84='on' (3sg subject pronoun); a second subject there is ungrammatical,
  so 26 is verb/adverb/complement — non-subject. A verb cannot be a
  subject — category clash.
- "46 26" @1249: the W2 window only. No other que-clause subject test.
- Residual: "26 24" @1753 (a8_08: "07 28 89 26 24 85 58") — the ONLY 26
  window with 26 directly before a verb (24, verb per ne-24-profile).
  24's top predecessors stream-wide are 11/01/13/84/46 — never 26
  elsewhere. Adverb reading ("[26-adv] [24-verb]") is fully available;
  not a clean subject leg. Fenced as follow-up `subj-26-1753`.

56's class evidence (n=23):

- Noun leg: "56 64" @132 (a1_03: "26 32 96 56 64 21 65") — 56 as
  antecedent of "qui"-relative: "[96] [56-noun] qui [21]". Nominal,
  non-pronominal.
- Verb leg: "64 56" @794 (a5_04: "46 07 64 56 37 44 77") — "qui [56]",
  verb slot, mirroring 26's verb legs.
- Pre-"ce" x4: "56 87" @70, @514; "56 47" @193, @1003 — 56 directly
  before "ce" (87/47, promoted). Non-subject slots (verb/adverb/noun).
- Quantifier/adjective slots: "56 17" @836 (a5_06: "76 59 35 56 17 98 20")
  = "[56] fois" — quantifier position ("N fois"). "48 56 32" @1282 and
  @1571, "01 56 37" @1654, "86 56 42" @1793 — 56 before predicative
  adjectives 32/37/42.
- Que-clause slots: "46 56" @1625 (a8_03: "67 33 46 56 69 26 00 33 21")
  = "que [56] [69] [26] pour [33]" — if 56 were the subject, "[69] [26]"
  must supply verb+complement; 69's class is open, 26 is verb/noun —
  does not parse cleanly. "46 56" @1744 (a8_08: "94 82 46 56 40 06 65")
  = "ne me que [56] e ent [65]" — no clean finite verb follows 56.
  Zero clean subject legs in 23 windows.

Adverses fenced (not ignored):

- A1 (W3 subject alternative): 98 precedes 56 @1325 ("62 98 56 30 06").
  98 is verb-shaped in its flagship frame (98-83-82-96-21 "vient"-shaped
  formula, frame-vient-parvenir battery) and promiscuous elsewhere
  (n=40, no clean subject leg); "62 98 56" stacks subjects under the
  demonstrated 62='il' rival. 98-as-subject is not a live alternative.
- A2 (W3 right context): "30 06 62 94" — 62-94 is 'il'-rival + promoted
  'ne'. "passent il ne [70=pre]" is ungrammatical under 62='il'
  (demonstrated rival, not promoted — noted, not asserted). Independent
  block on the 'passent' reading at W3 regardless of 56's class.
- A3 (W2 left knot): "00 67 46" = "pour [et/veut] que" — "pour et que" /
  "pour veut que" do not parse under standing values. The que-clause's
  left edge is itself ungrammatical; fenced for the re-segmentation
  follow-up, not decided here.

## Per-clause results

- **C1 — FAIL (kill grade).** 26 cannot be a 3pl subject at @1251. Every
  live class hypothesis excludes it: (a) feminine-singular noun legs
  ("la [26]" x2, byte-exact) — number clash with 3pl, forced; (b)
  verb-slot legs ("qui [26]" x2, "ne [26]", "on [26]") — category clash,
  a verb cannot be a subject, forced; (c) a 3pl-pronoun value would be a
  second polyvalence — barred to this battery by §7 (red-team act only).
  The single "26 [24]" @1753 window is adverb-compatible, not a subject
  leg. No clean "26 as subject" window exists in n=17.
- **C2 — FAIL (kill grade).** 56 cannot be a 3pl subject at @1327/@1733.
  Attested classes: noun-antecedent ("56 qui" @132), verb-slot
  ("qui 56" @794), pre-"ce" x4, quantifier ("56 fois" @836),
  pre-predicative-adjective x4 — none is subject-shaped, and zero of 23
  windows give a clean subject leg ("que [56]" @1625/@1744 do not parse
  cleanly). A pronoun value is §7-barred at battery level. At W5, 01 is
  not subject-shaped, so 56 is the only candidate — and it fails. At W3,
  the 98 alternative fails (A1) and the right context independently
  blocks "passent" (A2).
- **C3 — PASS (control holds).** @1561 "11 26 30 06" byte-confirmed;
  "la [26] passent" remains excluded — stranded determiner, French does
  not pro-drop a 3pl subject. Not re-litigated.
- **C4 — FIRES.** C1 and C2 both fail at kill grade: neither 26 nor 56
  can be 3pl subjects under standing values and §7. Per the
  pre-registered bar, the 'passent' reading dies grammatically at all
  four windows and 30-06 must re-segment.

## Verdict

**KILL** — the 3pl-subject hypothesis for 26/56 is killed, and per the
pre-registered bar the 'passent' word-reading of 30-06 dies
grammatically at @1251/@1327/@1561/@1733. What survives: the letter
strings "pas"+"ent" (30='pas' promoted-conditional, 06='ent' promoted,
12='n' letter account from spell-single-consonant) — only the WORD
"passent", which needs a 3pl subject, is dead. No standing verdict is
contradicted or downgraded: noun-26 NULL (26's class stays open — this
battery decides only non-subject-hood), 23~26 SPLIT, 62='il' rival
status, and all §7 constraints are untouched. No polyvalence declared.

## Follow-ups proposed (the bar's consequent: 30-06 must re-segment)

1. `reseg-3006-w2` (P2) — re-segment W2 @1251 "00 67 46 26 30 06 65":
   test "que [26-verb] pas | [06…]" (26 finite verb per "qui/ne/on [26]"
   legs, "pas" adverb, 06 opens the next word) and word-internal
   "[26]pas" arms; must also resolve the fenced "00 67 46"
   ('pour et/veut que') left knot. Bar: one grammatical full-row parse
   or fence with stated cause.
2. `reseg-3006-w35` (P2) — re-segment W3 @1327 "98 56 30 06 62 94" and
   W5 @1733 "01 56 30 06 60": test the "pas | [06…]" boundary shift
   (06='ent' as next word's onset vs previous word's ending) with 56 in
   its adverb/noun arms from this battery's census; W3 must reconcile
   "62 94", W5 must place 56 and 01. Bar: per-window grammatical parse
   or fence with stated cause.
3. `subj-26-1753` (P3) — discriminate the single "26 [24]" @1753 window:
   adverb vs subject reading of 26 via 24's subject profile (24 takes
   84='on'/46='que'/94='ne' subjects; 26 never precedes 24 elsewhere).
   If a subject reading holds, this battery's category-clash arm
   re-opens; if not, the kill hardens.

## Bookkeeping

- Report: this file.
- battery-queue.json: `pasent-subject-26-56` → status `verdict`, result
  `kill`, date 2026-10-09 (temp-file + rename, own entry only; pre-write
  re-read; JSON re-validated post-write).
- Lock `locks/pasent-subject-26-56.lock`: created on start, deleted on
  completion. No pre-existing lock was present.
