## LE FRANÇAIS (round 4): 62 = « on » — troisième jambe, verdict PROMOTE

- Context: work order 1 — find the THIRD independent leg for 62="on", the round's
  first promotion candidate. Two legs exist: (1) the round-3 ear lock F31
  (« on ne prend pas » @1328, « on ne [V] » ×5, « pers|on|ne » @508), (2) 62→94
  « on ne » ×8 at 1.97× in-band (red-team-3b recomputation). I dumped all 34
  62-windows (`code/crowd4/frenchman4_62_results.json`, pairs via
  `code/crib_attack.py::load_pairs`, 1,846 pairs) and read the 26 fresh ones —
  every window NOT in the ×8 and NOT ear-locked — aloud as « on », hunting a leg
  that touches neither leg-1's windows nor leg-2's bigram.

- Decision: **PROMOTE 62="on" → promotion-candidate (pending red-team
  adjudication; kill authority acknowledged).** Third leg = fresh-window
  subject-triangulation, crown window @848.

- Why: the third leg is grammatical, word-space, F30-legal, and discriminating.
  `@848: 00 33 [par] e >>62<< 21 67 91 51` → « …33 par e, **on me** 67 … » —
  « …par écrit, on me [dit]… » (« in writing, one tells me… »), a coherent
  despatch clause in the lane's established register. The object pronoun
  21=« me » (bigram_closer LEAD, 3 checks, established WITHOUT 62 — no
  circularity) FORCES a subject before it: only the pronoun « on » survives
  without breaking anchors. The alternatives die clean: « …éon me [V] »
  (noun-subject) requires breaking provisional-strengthened 96=« par » (4/4 on
  repaired leg F28); word-internal « …eon » + « me » leaves the clause
  subjectless. Supporting fresh-window instances, same subject-frame family:
  @1140 « …78, **on a** er… » (« …me, on a [nom]… », 16=« a » lead; the
  « …meon » alternative is no French word); @665/@1535 « …, on 06 … »
  (« on » + verb-stem 06, provisional — compatible, ambiguous with
  word-final-« on »-of-subject-noun, so corroboration only); @46
  « …, **on parle** 00… » (96=« par » word-internal — the polyvalence the
  round-3 enlightenment predicts); @1348 « …i|on … » (« …ion » word-internal,
  second polyvalence sighting after « personne » @508, consistent with L1 4.27×).
  Sweep result: **34/34 windows compatible with 62=« on », zero counterexamples**;
  /ɔ̃/-rivals (« son/mon/nom/ont ») die in the fresh subject-frames, and « te »
  stays dead. Leg-2 re-derived independently: 8/34=0.2353 vs era P(ne|on)=0.1182
  (my Tocqueville tokenization; lane's 0.1194) → 1.99× ≈ the recorded 1.97×,
  in-band — verification, not double-counting.

- Enlightenment: the ear stopped being a garnish the moment the grammar started
  doing casework — @848 isn't « more on-ne windows », it's a different
  construction (« on me » vs « on ne ») with a different anchor (21 vs 94),
  and the OBJECT PRONOUN is what forces the subject: French word order did the
  discriminating, not frequency. Second surprise, from the sanity check: the
  by-ear model makes a PREDICTION — « qu'on » is one spoken syllable /kɔ̃/, so
  the encipherer should write it as ONE group, and indeed 46=que→62 = ×0
  (era P(on|qu')=24.8%, naive expectation 29×0.0798≈2.3, observed 0). The
  absence is predicted, not anomalous. And the phonetic-variant question
  answers itself: no window in 34 needs « ont » or any rescue — « on »
  suffices everywhere, so the variant hypothesis is unnecessary (Occam).

- For the report: belongs in the 62=« on » promotion case, as leg 3 of 3.
  Numbers that matter: f(62)=34/1846; fresh windows 26/26 read clean, 0
  counterexamples; @848 « on me » lock (21=« me » LEAD, 96=« par »
  provisional-strengthened, both pre-existing); leg-2 re-derivation 1.99×
  in-band (matches 1.97×); 46→62 ×0 vs 2.3 expected (by-ear prediction,
  p≈0.10 — consistent, not probative alone). Files:
  `code/crowd4/frenchman4_62.py`, `code/crowd4/frenchman4_62_results.json`.

- Caveats: (1) Legs 1 and 3 share the ear instrument — independence here is
  window/formula/anchor-based per the work order, NOT instrument-based; the
  red-team may weigh that differently. Flagged, not hidden. (2) Leg-3 instances
  lean on provisional reads (21=« me » LEAD with a standing « par me »
  contradiction; 06=verb-stem; 96=« par »; 16=« a » lead) — marked throughout.
  (3) NULL, first-class: the STRUCT boundary-confidence leg FAILED —
  `code/crowd4/frenchman4_62_struct.py`/`.json`: 62 both-sides->0.5 = 0.188 vs
  GT control 46=« que » 0.207 vs random pairs 0.25 — the instrument doesn't
  discriminate standalone words (the GT control fails its own signature), so it
  was discarded, not used. (4) « 21 on » ×4 (@360/@1064/@1463/@1538) and
  « 74 on » ×2 (@801/@1314) stay ambiguous (word-final-« on »-of-unknown-word
  parses live) — they don't threaten « on » (polyvalence covers both parses)
  but they don't confirm the pronoun either. (5) No GitHub push; R5005 only;
  every number above traces to the two JSONs or the cited lane files.
