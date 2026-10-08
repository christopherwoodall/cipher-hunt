# Battery A7 — trigram 79-82-48 ×2 ("qui tout m …")

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder P6 (next-token-findings-qui.md); fenced residual in A5.
Standing: 79="tout" PROMOTED (A5) — "qui tout m…" is poor French, so the
trigram must be re-read (word-boundary or clitic parse).
Windows: @395–399 and @1226–1230 (64@395/@1226 "qui"; 79@396/@1227).

## Pre-registered bar (written BEFORE touching data)

Three leads, tested against each other:
- **L1 "m'est avis"**: 82="me"/"m'", 48="est"-homophone, then "avis"-shaped.
  Requires 48="est" — which needs the homophone standard vs 59 (joint
  frames + distribution test). If 48="est" fails the standard, L1 dies.
- **L2 "me"+verb**: 82="me" clitic, 48=verb (must be vowel-initial per
  H_stem — check 48's successor/predecessor phonotactics used in the 48
  syntax battery, or re-derive vowel-initiality here).
- **L3 one word**: 79-82-48 as a single word's syllables (79="tou/tout"
  syllable inside a longer word, 82="m" spelling cell — cf. H_stem's
  "French lacks mC-onsets" used FOR cell-internal m). Test: does 82's
  contact profile support word-internal "m" (predecessor = vowel cell)?

- **PROMOTE** a lead iff ≥2 independent legs (the two windows count as
  ONE leg — they're byte-identical; the second leg must come from 82/48
  contact profiles or an independent window) AND the rival leads are
  excluded with cause.
- **HOLD** if no lead reaches 2 legs.
- **KILL** a lead if its requirement fails (e.g. 48="est" fails homophone
  standard → L1 dead; 82 never word-internal → L3 dead).
- Note: the two trigram windows are byte-identical — n_eff=1 for the
  frame itself. Say so explicitly.

## Data

### The windows (n_eff=1 for the frame — byte-identical trigram)

- @395–399: `67-64-79-82-48-06-11` = "[67] qui | tout me [48] [06] la"
- @1226–1230: `57-64-79-82-48-29-47` = "[57] qui | tout me [48] er ce"

79-82 occurs **only** in this trigram (2/2); 82-48 occurs ×4 (@125, @376,
@397, @1228).

### Lead L1 "m'est avis": KILLED

Requires 48="est". Distribution test vs 59="est": 59's successors
concentrate on predicative slots (37×6, 32×3, 35×3, 46×2, 42×2…);
48's are flat/diverse (21, 52, 76, 20, 47, 77, 96, 29 ×2 each) with
**48→{37,32,35} = 0/38** vs 59's 12/27. An "est"-homophone would show the
predicative concentration. Clean distributional kill. ("Avis" additionally
has no slot: tails are 06-11 and 29-47.)

### Lead L2 "tout me [48-verb]": 3 legs

- **Corpus leg:** "tout me/m' + verb" is register-real ×4: "tout me sourit",
  "tout me ramène", "tout me porte", "tout me frappa"
  (code/side-period/corpus/). The finder's "poor French" adverse note is
  refuted — "tout me [verb]" ("everything [verb]s me") is good French.
- **"me [48]" leg:** 82-48 ×4 (@125 "[98] me [48] la", @376 "[85] me [48]
  [00]", @397, @1228) — "me"+verb slot recurring independently of the
  trigram.
- **48's verb profile:** successors flat/diverse (verb-like complement
  spread); predecessors 62×6, 12×5, 82×4, 32×4, 89×3 (subject/clitic slots).
- **Parse:** "tout me [48]" as clause-initial ("…qui [X]. Tout me
  [48-verb]…" = "…which [X]. Everything [verb]s me…") — no comma-strain;
  "qui" closes the previous clause.

### Lead L3 (one word "79-82-48"): EXCLUDED

No French "tou-m-[vowel]" word fits ("toum[V]" unattested in corpus);
79-82's trigram-exclusivity is neutral, not a leg. Zero legs.

### Residual strains (named, not hidden)

- R1: @1229's tail "48-29-47" = "[48]er ce" recurs independently @1589
  ("70-64-65-48-29-47-08", no trigram) — "[48]er ce" ×2. If 48 is a verb
  stem, 48-29 = stem+"er" infinitive + 47="ce" object ("[to-48] this") —
  consistent at @1589, strained after "me" at @1229. The "48-29" shape is
  real (2×); its integration with "me" is unresolved.
- R2: 48-06 @398 is a singleton — 06's role after 48 unknown.

## Verdict

- **L1 KILLED** (48="est" distributionally dead).
- **L3 EXCLUDED** (zero legs).
- **L2 PROMOTED** as the trigram reading: "…qui [X]. Tout me [48-verb]…"
  (3 legs; rivals excluded with cause). This is a frame promotion, not a
  value: **48 becomes a verb-stem candidate** (4 "me [48]" legs + verb
  profile + "[48]er ce" ×2) queued for the verb battery. 48's value is NOT
  promoted; R1/R2 stay open.
