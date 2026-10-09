# Battery `41-05-class` — verdict: PROMOTE

Worker: 4343a469-30d6-4696-b10f-eb90145e39e9 · 2026-10-09T16:58:03Z start
Discriminates 41's class at @5 (`47=ce 41 06 77=le`): adjective vs noun.
Follow-up #3 of `battery-val-41-word-census` NULL.

## Bar (verbatim, pre-registered before the discriminating corpus test)

> "name 41's class at @5 (adjective vs noun) iff >=2 independent legs
> decide the class with zero kill-grade contradictions"

Restated as numbered pass/fail clauses (before testing):
- C1: @5's window re-derived byte-exact from the repaired stream
  (0-based @-offsets; pre/suc context with standing values).
- C2: >=2 independent legs both name the same class (adjective or
  noun), with zero kill-grade contradictions against §7 standings or
  other windows' forcings.
- C3: the rival class is fenced at @5 with stated cause (no surviving
  grammatical parse), not merely outscored.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like
`code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs, 96
types; 0-based @-offsets). `canonical.py` never used. R5005, sealed
gates, red-team queue untouched.

Adopted premises (not re-litigated):
- §7 standings: 47='ce' (granted A4), 06='ent' verb ending (battery
  PROMOTE 2026-10-08; bound morpheme; "82+06='ment'" compositional;
  doubled-06 "ne mentent" x2), 77='le' (PROVISIONAL — battery null
  2026-10-07), 78='ver' (R16-005 LEAD, R20-032-038 deferred — not
  settled), 67 sole true polyvalence, 39="a/à" accent-indifferent
  allophone tier.
- `val-41-word-census` NULL: @5's window and n(41)=19 adopted; D3
  (det/num/adv killed at @5) adopted. Its "STANDALONE forced" judgment
  at @5 is CORRECTED below (fenced with cause — the census never
  tested 06's wordhood).
- `split-41-redteam` queued: this battery names 41's class AT @5 ONLY.
  It does not adjudicate the split and does not touch @39
  (finite-verb forcing) or @237 (determiner arm, battery PROMOTE).

The corpus leg ran AFTER bar pre-registration, against
`code/side-period/corpus/` (~27.7 MB period French, provenance in
`code/crossfleet/memo2-period-corpus.md`).

## Window-level evidence (byte-exact, 0-based)

@1..9 = `00 97 51 47 41 06 77 78 18` (row a1_00):
@4=47='ce' (granted) | @5=41 | @6=06='ent' (promoted) |
@7=77='le' (provisional) | @8=78 ('ver'-lead).

### Leg 1 — 06 must compose leftward with 41 (stream)

- 06='ent' is a bound ending (promoted battery; adverses answered).
  There is no French word "ent"; 06 never stands alone.
- The word-initial-06 alternative is real in-stream but conditional:
  "30 06"+Y x4 (@1251/@1327/@1561/@1733; 30='pas' promoted) =
  "pas [ent…]" with valid continuations (Y=65/62/60/60:
  "entendu/entier/entr…"‑shaped). A word-initial 06 REQUIRES a valid
  continuation.
- At @5 the continuation would be 77: "ent"+"le" = "entle" — no French
  word begins "entle", and 77='le' (provisional) is a standalone word,
  not a continuation. Rightward composition ("entle") impossible;
  standalone "ent" impossible.
- Therefore 06 composes leftward: the word is "41+06" = "Xent",
  and @5 reads "ce [41+ent] le [78]".
- CORRECTION (headline): `val-41-word-census` judged @5 "STANDALONE
  forced". That forcing is vacated: a standalone 41 would leave 06
  wordless, which no standing permits. 41 is word-INTERNAL with 06 at
  @5 (stem of an "Xent" word). Fenced with cause above; the census's
  NULL verdict itself is untouched.

### Leg 2 — class enumeration of "41+ent" (grammar, @5-local)

Candidate classes for the "Xent" word after "ce":
- verb (3pl "-ent"): "ce [V-3pl]" — singular demonstrative subject of
  a 3rd-plural verb: number clash, ungrammatical. DEAD.
- adjective: "ce [adj-ent] le [78]" — dead on EVERY 78-class: as
  subject of "le [V]" adjectives cannot head an object-clitic frame;
  "ce [adj-ent] le [N]" (*"ce présent le verre") ungrammatical;
  "ce [adj-ent]" bare is ungrammatical (demonstrative needs its noun).
  DEAD.
- determiner/numeral/adverb/pronoun: dead per adopted D3 + the "ce
  [X]" nominal requirement. DEAD.
- noun: "ce [N-ent] le [V-ver…]" — "ce moment le verra"-shaped:
  subject noun + object clitic + "ver-" verb. PARSES.
  Load-bearing: provisional 77='le' and 'ver'-lead 78 verb-shaped
  (caveat C-a below).

Exactly one class survives: NOUN (41 = noun-stem of the "Xent" word).

### Leg 3 — period-corpus counts (discriminating test, post-registration)

- "ce [Xent] le [Y]" (X any -ent word): 5/5 hits have X="moment"
  (noun). ZERO adjectives. ("en ce moment le sceptre / le plus voisin
  / le nommer / le théâtre / le plateau" — dumas-kean, guizot-t3,
  hugo-hernani, scribe x2.)
- "cet [Xent] le [Y]": 0 hits.
- "ce [Xent]-là": "moment-là" x3, "régiment-là" x1 — all nouns, zero
  adjectives. "cet [Xent]-là": "accident-là" x1 — noun.
- Control "ce/cet [Xent]" (no "le"): 755 hits / 130 distinct; top-30
  all nouns except "excellent" (25x, always with its head noun after
  — never in the "le"-frame). The "le"-restriction is exactly what
  kills the adjective arm, empirically 0/5 vs noun 5/5.

### Leg 4 — frame family "47 X 06" (stream)

- "47 X 06" ("ce [Xent]") recurs 3x: @4 X=41, @269 X=11, @1718 X=68.
- @1718: `59=est 30=pas 64=qui | 47=ce 68 06 11=la 52 37 …` →
  "ce [68+ent]-là [52]": reading 11 as the "-là" suffix (accent-tier,
  cf. 39="a/à" precedent) gives "ce [Xent]-là". An adjective cannot
  host "-là" (*"ce grand-là" — the suffix needs its noun), so the
  adjective arm is independently dead at the sibling window; the
  family's clean parses are noun-headed ("ce moment-là"-shaped).
- @269: `47 11 06 67` = "cela [06] et/veut": 06@271 is UNATTACHED
  under current standings (1 of 44 "X 06" bigrams). FENCED with cause
  as an unresolved residual for the 06-frame program — out of scope
  here. It does NOT license dangling at @5: @5 has a fully clean
  composed parse (Legs 1–2), and a clean parse dominates a dangle.

## Per-clause results

- **C1: PASS.** @1..9 = `00 97 51 47 41 06 77 78 18` re-derived
  byte-exact; standings attached per window.
- **C2: PASS.** Four legs; Legs 1+2 are @5-local and independent
  (attachment vs class-enumeration), Legs 3+4 independent corroboration
  (period corpus, frame family). All name NOUN. Zero kill-grade
  contradictions: no §7 standing contradicted; @39 verb-forcing and
  @237 determiner arm are different windows (split-41-redteam venue,
  queued, untouched); the parent census's "STANDALONE forced" is a
  same-day worker judgment, corrected with cause (not a standing).
- **C3: PASS.** Adjective fenced at @5 with stated cause (Leg 2:
  "ce [adj-ent] le [78]" ungrammatical on every 78-class) and at the
  sibling window (Leg 4: *"ce grand-là").

## Adverses

- A1 (@269 "cela [06]" residual): fenced with cause, out of scope —
  flagged for the 06-frame program. Answered, not ignored.
- A2 (load-bearing): provisional 77='le' + 'ver'-lead 78 verb-shaped.
  If 78 is ever shown non-verb-shaped, parse (h) dies and @5 has no
  clean parse — escalation path: the 78 venue (R16-005/R20), not this
  battery.
- A3 (parent-census correction): headline-noted above; the census's
  NULL verdict stands, only its @5 forcing judgment is vacated.
- No pre-registered adverses (bars/adverses were null).

## Verdict: PROMOTE

41 is noun-class at @5: 41 is the noun-stem of the composed word
"41+ent" in "ce [41+ent] le [78]" ("ce [N-ent] le [V-ver…]"-shaped).
Class-at-@5 only — delivered to the split-41-redteam docket as the
noun arm's @5 leg. Per §4, promotes propose no follow-ups.

## Caveats

- C-a: load-bearing on provisional 77='le' (battery null 2026-10-07)
  and 'ver'-lead 78 verb-shaped (R16-005 LEAD; R20-032-038 deferred).
- C-b: names 41's class at @5 only. @39 (finite verb) and @237
  (determiner) are separate windows under the queued split-41-redteam;
  §7 sole-polyvalence rule respected (no global two-class claim).
- C-c: canonicality caveat stands (68 of 70 upstream row offsets
  unvalidated); row a1_00's pairing adopted as-is.

## Flags for supervisor discretion (not §4-mandated follow-ups)

- F1: @205 `42 06 77 44` ("[Xent] le [44]") is @5's shape-twin for 42's
  predicative frame — adjudicating 44's class would decide 42's @205
  arm the same way. Out of scope (42, not 41).
- F2: 06@271 (@269, "cela [06] et/veut") — open residual for the
  06-frame program.

## Scope

Decides 41's class at @5 only. Untouched: all §7 standings,
`val-41-word-census` NULL, `val-41-det-windows` PROMOTE,
`val-41-1016` NULL + W_C fence, `41-doubling-audit` PROMOTE,
`split-41-redteam` (queued), `41-808-role` (queued), `41-verb-arm-package`
(queued), R5005, sealed gates, red-team adjudication queue.
