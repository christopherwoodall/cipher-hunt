# Battery `88-1727-shape` — verdict: PROMOTE (locus-level)

**Claim:** 88's shape at @1727 specifically decides whether continuation B is live.

## Bar (verbatim, pre-registered)

> decide 88's shape at @1727 via the '39 88' x3 set (@765 'est à [88]', @1514 'à [81] [88]', @1727 'vient à [88]') with 88's local followers; infinitive-shaped keeps B live for both survivors, otherwise B is fenced for both

Numbered clauses:
- **C1.** The '39 88' x3 set is as stated on the repaired stream.
- **C2.** 88's shape at @1727 is decided (infinitive-shaped vs otherwise) on grammatical and distributional grounds.
- **C3.** Infinitive-shaped → continuation B live for both survivors (condition, mesure); otherwise B fenced for both.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/88-1727-shape.lock` on start.
Re-derived the full stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (1,847 pairs / 96 types verified;
`canonical.py` never touched; R5005, sealed gates, red-team queue untouched).
@-offsets below are 1-based (matching the bar); 0-based equivalents noted.
Continuation B (adopted from 43-1126-1725-joint via cond-mesure-43full):
@1724 (row a8_07) "la [52] [37] condition/mesure vient à [88]" —
`... 06 11 52 37 43 98 39 88 24 30 ...` (0b@1721–1729).

## Findings

**C1 — PASS.** Exhaustive census on the repaired stream: '39 88' direct x2
(1-based @765 = 0b@764; 1-based @1727 = 0b@1726) and '39 81 88' x1
(1-based @1514 = 0b@1513). No other '39 ? 88' pattern exists (39: n=13).
- @765: `11 70 82 34 29 40 20 62 94 59 39 88 66 98 80` → "la première … [62] ne est à [88] [66] vient …" (rows a5_03/a5_04).
- @1514: `33 00 86 56 41 12 61 59 39 81 88 11 31 11 91` → "… est à [81] [88] la [31] …" (row a7_11).
- @1727: `30 64 47 68 06 11 52 37 43 98 39 88 24 30 15` → "… la [52] [37] [43] vient à [88] [24] pas …" (rows a8_06/a8_07).

**C2 — infinitive-shaped.** Decided on four converging legs:
1. **The "à" + 88 contact.** In both direct windows 88 immediately follows 39
   ("à"-class; 39="/a/" lead R17-005). After "à", French licenses an infinitive
   ("vient à mourir", "est à faire"), not a bare noun ("vient à [noun]" needs an
   article — "vient à la maison") and not a preposition. Adverb/pronoun shapes
   are distributionally excluded for 88 (n=23, verb/governor-class standing,
   takes "er" — see leg 3).
2. **Idiomatic frames.** "vient à + inf" is idiomatic 1841 French
   ("venir à" + infinitive = come to / happen to; cf. Littré art. "venir").
   "est à + inf" is the standard passive-infinitive construction
   ("est à faire", "est à craindre") — exactly the @765 frame.
3. **Infinitive morphology on 88.** @1050 (0b@1049):
   `40 17 77 82 63 11 67 76 85 41 88 29 40 29` → "… [41] [88]er e er …"
   (40="e" GT, 29="er" GT). 88 directly carries the -er infinitive ending.
4. **Local follower at @1727 is clean.** 88→24 (verb-class); no postposed
   article at this window, so no conflict with the infinitive shape here.

**Rival shapes at @1727 — killed:**
- *Noun:* bare noun after "à" is ungrammatical in 1841 French (fixed locutions
  like "à Paris"/"à cheval" excepted); 88 (n=23, takes "er") is not a proper
  noun. Kill-grade at this window.
- *Preposition/governor:* "à" + preposition is ungrammatical ("*vient à pour").
- *Adverb:* "vient à [adv]" is unidiomatic and 88's profile excludes it.

**Residuals (fenced, not vetoes):**
- @1514's "88 11" ("la" after 88): parsed via clause boundary —
  "… est à [81] [88]. La [31] la [91] …" (new clause after the infinitive is
  grammatical). 81's value is open and 81 intervenes, so this window does not
  bear on @1727's shape.
- 88→77 x3 / 88→11 x2 at other windows: out of scope for this locus decision;
  88 is NOT named globally here.

**C3 — B stays live for both survivors.** With 88 infinitive-shaped at @1727,
"la [52] [37] condition vient à [88-inf]" and "la [52] [37] mesure vient à
[88-inf]" are both grammatical ("venir à + inf"), symmetric strain as adopted.

## Adverses

- **No polyvalence declared at battery level (§7):** honored — shape decided
  at @1727 only; no second value declared for 88 anywhere.
- **Do not name 88 globally:** honored — no global value named; the "88 29"
  leg is used only as morphological evidence for the locus shape.

## Verdict

**PROMOTE (locus-level):** 88 is infinitive-shaped at @1727. Continuation B
("la [52] [37] condition/mesure vient à [88-inf]") stays live for both
survivors, condition and mesure. No standing verdict contradicted or
downgraded.

## Bookkeeping

- Lock `locks/88-1727-shape.lock` created on start, deleted on completion.
- `battery-queue.json`: `88-1727-shape` → status `verdict`, result `promote`
  (temp-file + rename, own entry only, pre-write assert confirmed no prior
  verdict, JSON re-validated).
- No follow-ups required (promote verdict). Optional red-team note: the
  88→77 x3 / 88→11 x2 article-follower windows remain the standing tension
  against any future global infinitive naming of 88.
