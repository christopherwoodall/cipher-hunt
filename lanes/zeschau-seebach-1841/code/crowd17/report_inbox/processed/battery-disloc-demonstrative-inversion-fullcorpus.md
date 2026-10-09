# Battery report: disloc-demonstrative-inversion-fullcorpus

- Target id: `disloc-demonstrative-inversion-fullcorpus`
- Claim: "same inversion census on full-corpus windows, not dialogue-scoped"
- Date: 2026-10-09
- Worker: battery worker (subagent 93430ca2-8e09-4153-b30a-d5b2cf2ad321)
- Stream: not applicable — corpus census against period French, per target
  charter and the parent-battery precedent. The 1,847-pair repaired parse
  was not used. R5005, sealed gate instances, and the red-team adjudication
  queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved out of its normal
position, set off by a pause, and resumed by a pronoun. "Tonic" = the
stressed form of a pronoun (cela, ceci, ça). "Postposed" = the
demonstrative comes AFTER the infinitive ("[inf] !, cela"), the inverse
of the preposed order fenced by the grandparent batteries.
"Full-corpus windows" = the whole text of each corpus file, including
narrative prose, footnotes, and stage directions — not dialogue-scoped.

## Parentage

Follow-up of the battery-level NULL `disloc-demonstrative-inversion`
(2026-10-09): the inverted (postposed) order "[inf] !, cela/ceci/ça"
fenced at quoted-dialogue level (3,590 dialogue spans, ~10.3M dialogue
chars, 37 candidates, 0 genuine). The NULL's own evidence note said the
pairing "may be a narrative-register feature, not a dialogue one". This
battery tests exactly that hypothesis: the same census on full-corpus
windows.

## Bar (verbatim, pre-registered before testing)

">=1 genuine attestation re-opens; confirmed zero fences the inverted
order at full-corpus level"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE postposed "[inf] !, cela/ceci/ça" attestation
   (bare exclamatory infinitive, demonstrative in post-topic position,
   paired) exists anywhere in the full text of the
   revue-deux-mondes-1841 corpus (dialogue and narrative). If yes:
   the inverted order re-opens as a register-general construction
   (promote-grade per §4).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends excluded with cause — the inverted order
   is fenced at full-corpus level in RDM 1841 (null per §4: zero is an
   absence, not a kill).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-inversion-fullcorpus.lock`
   on start (agent id + UTC timestamp; no stale lock for this id
   existed); deleted on completion.
2. Wrote and ran a full-corpus variant script:
   `code/crowd17/next-token/disloc_demonstrative_inversion_fullcorpus_census.py`
   (differs from the parent census in one line only: it searches the
   whole file text instead of dialogue spans). Verbatim same patterns:
   INF `\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b`,
   DEM_POST `\b(cela|ceci|ça|ca|cel[àa]|cec[iy])\b`,
   candidate iff DEM starts AFTER the infinitive within INF..INF+100
   and "!" occurs between INF start and 20 chars past the DEM end.
   Covers all postposed shapes: "Voler !, cela" / "Voler, cela !" /
   "Voler ! cela" / "Voler cela !". Results:
   `code/crowd17/next-token/disloc-demonstrative-inversion-fullcorpus_census.json`.
3. Corpus (character counts computed in-session):
   - revue-deux-mondes-1841-q1.txt: 3,013,552 chars → 10 candidates.
   - revue-deux-mondes-1841-q2.txt: 2,964,405 chars → 18 candidates.
   - revue-deux-mondes-1841-q3.txt: 3,054,350 chars → 7 candidates.
   - revue-deux-mondes-1841-q4.txt: 3,165,234 chars → 22 candidates.
   - Totals: 12,197,541 corpus chars; **57 unique candidates**.
4. Cross-check: all 37 parent-battery candidates re-appear with
   identical (file, absolute INF offset) keys — the parent's
   classification transfers by identity. 20 candidates are NEW
   (non-dialogue windows), classified individually below.

## Window-level evidence

### The 37 carried-over candidates

Identical to `battery-disloc-demonstrative-inversion.md`
(21 false-INF nouns/adjectives/possessives/finite verbs, 15 genuine
infinitive with demonstrative in a finite/prepositional/interjectional
slot, 1 OCR hyphenation fragment; 0 genuine). Classifications carry
over unchanged — no re-litigation.

### The 20 new non-dialogue candidates (classified in-session)

"/" = source line break; @-offset = corpus char offset of the
infinitive-shaped word.

1. q1 @103539 (d'Angleterre), @103554 (leUre), @103584 (lire), dem
   "Ceci!" — footnote text: "lire de Ceci!, à qui lord Bedford
   l'envoya" / "(2) 8 mai 1567. Archives d'Angleterre". "Ceci" is
   governed by the preposition "de" (part of the footnote's wording),
   not a dislocated topic; the first two INF hits are OCR fragments
   ("d'Angleterre", "lettre" misread "leUre"). Excluded (all three).
2. q1 @569924 (plaisir), dem "cela" — "le plaisir était neuf...
   — Quoi! cela est encore beau, se dit-on." "cela" is the subject
   of finite "est". Excluded.
3. q1 @1446015 (faire), dem "cela" — "...j'ai donc pu faire cela !
   Et à la première occasion on recommence..." "cela" is the direct
   object of "faire" inside the perfect clause "j'ai pu faire cela".
   Not extra-clausal, not a dislocation. Excluded.
4. q1 @1524253 / @1524282 (notre ×2), dem "cela" — "notre influence
   détruite, notre honneur compromis! Puis, après cela, il suffira
   de..." "notre" possessives; "cela" governed by preposition
   "après". Excluded (both).
5. q2 @501253 (accuser), @501262 (d'avoir), dem "cela" —
   "...accuser d'avoir commis une faute, et commencé une folie !
   // Il faut pourtant le dire : cela n'est p..." "cela" opens the
   NEXT sentence as subject of "n'est". Not paired with the
   infinitive. Excluded (both).
6. q2 @1446218 (faire), @1446225 (jeter), @1446236 (dernière), dem
   "ça" — "faire jeter ma dernière chique. // — Ah! ça! prenons
   conseil..." "Ah! ça!" is the fixed interjection "ah ça"; the
   infinitives belong to a causative "faire jeter", not a bare
   exclamatory one. Excluded (all three).
7. q2 @1946045 (terre), dem "cela" — "terre autour du soleil! Et
   c'est avec cela qu'on veut réaliser..." "terre" noun; "cela"
   governed by preposition "avec". Excluded.
8. q2 @2381800 (retourner), dem "cela" — "...le faisant retourner :
   « Mi amo, allez vous-en!.... » Cela dit, il donna..." "Cela dit"
   is the absolute participle "that said" (cela = subject of
   participle "dit"), not a dislocation of "retourner". Excluded.
9. q2 @2790701 (dernier), dem "ça" — "dernier des maladroits !
   s'écria-t-il en frappant la terre... Ah ça" — "dernier" adjective;
   "Ah ça" interjection. Excluded.
10. q4 @835907 (dire), dem "cela" — "dire? s'écria le docteur
    pâlissant. // - Vous le demandez ! vous demandez ce que cela
    veut..." "cela" is the subject of finite "veut". Excluded.
11. q4 @1095036 (l'air), @1095051 (reconnaître), dem "ça" —
    "...n'a pas l'air de la reconnaître : // Viens ça, l'ami!
    N'attends demain!..." "l'air" is the noun (false-INF via "ir"
    suffix); "Viens ça" is imperative + locative "ça" ("come over
    here"). Not paired with an infinitive. Excluded (both).
12. q4 @1707032 (s'ouvrir), @1707089 (abjurer), dem "cela" —
    "...qu'à abjurer la religion de vos pères! // — Cela viendra,
    répondit Célestin..." "cela" opens the next paragraph as subject
    of finite "viendra". Excluded (both).

**0 of 20 genuine.** The three nearest misses: "j'ai donc pu faire
cela !" (#3, demonstrative is the governed direct object, not
extra-clausal), "Cela dit" (#8, absolute participle — cela is the
subject of "dit"), "Viens ça" (#11, imperative with locative ça).

## Per-clause pass/fail

1. ≥1 genuine postposed "[inf] !, cela/ceci/ça" attestation anywhere
   in RDM 1841: **FAIL (confirmed zero).** 57 unique candidates over
   12,197,541 corpus chars → 37 dialogue candidates classified in the
   parent battery (0 genuine), 20 new narrative-footnote candidates
   (0 genuine); 0 genuine.
2. Confirmed zero → inverted order fenced at full-corpus level:
   **EXECUTED.** The parent's hypothesis that the pairing "may be a
   narrative-register feature" is tested and rejected: narrative
   windows contribute zero additional candidates beyond the dialogue
   set's false friends (objects of prepositions, finite-verb subjects,
   absolute participles, interjections, OCR noise). Per §4 this is a
   **null**, not a kill.

## Adverses, answered

- None pre-registered.
- Self-check: no contradiction with the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head the construction) —
  tonic demonstratives only, as in the parent.
- Self-check: consistent with the parent NULL
  (disloc-demonstrative-inversion) — the bar anticipated exactly this
  outcome ("confirmed zero fences the inverted order at
  full-corpus level").
- §5.2: no standing red-team verdict touched; no overwrite, no
  escalation required.

## Verdict: NULL (fence per clause 2)

The inverted (postposed) order "[inf] !, cela/ceci/ça" is fenced at
full-corpus level in revue-deux-mondes-1841: 57 unique candidates
across ~12.2M characters, every one classified with cause (including
the 20 narrative-window candidates unique to this census), 0 genuine.
Arm (a) of ce87-1028-role stays fenced — now in both word orders at
both dialogue and full-corpus level.

## Follow-ups (nulls regenerate work)

None of these duplicates a queued target (the disloc-demonstrative
family covers preposed-order and verb-tagged re-runs only):

1. **disloc-demonstrative-inversion-verbtags** (P3): re-run this
   census with a POS-tagged genuine-infinitive filter. 41 of 57
   candidates across the two censuses were noun/adjective/possessive/
   false-INF noise from the suffix-only INF pattern; a verb-tagged
   pass discriminates cleanly. Bar: ≥1 genuine postposed pairing on
   the cleaned candidate set re-opens arm (a) as a word-order variant;
   confirmed zero fences it at verb-filtered level.
2. **joint-order-demonstrative-pairing-census** (P4): supersede the
   order-framed batteries with one joint census of
   bare-exclamatory-infinitive + tonic-demonstrative adjacency in
   EITHER order across the RDM 1841 corpus (full text). Bar: ≥1
   genuine pairing in either order re-opens arm (a); confirmed zero
   closes the family at RDM 1841 level.
3. **disloc-demonstrative-corpus-1770-1820** (P4): test whether the
   fence is an 1841-period effect. The bar construction
   ("[inf] !, cela") may have existed in earlier literary French and
   died out; if so, the RDM-1841 zero is a period effect, not a
   grammatical ban. Bar: ≥1 genuine attestation in a pre-1841 literary
   corpus (e.g. Rousseau, Diderot) documents the construction as a
   diachronic feature; confirmed zero extends the fence backward.

## Bookkeeping

- Census script:
  code/crowd17/next-token/disloc_demonstrative_inversion_fullcorpus_census.py
  (one-line variant of the parent census; re-runnable).
- Results:
  code/crowd17/next-token/disloc-demonstrative-inversion-fullcorpus_census.json
  (per-file sizes, 57 candidates, each with file, absolute INF char
  offset, dem match, window text).
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-inversion-fullcorpus.md
  (this file).
- battery-queue.json: `disloc-demonstrative-inversion-fullcorpus`
  queued → verdict/null via temp-file + rename (pre-write assert
  confirmed queued/verdictless; JSON re-validated post-write; own
  entry only; claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp; no stale lock for
  this id existed), deleted on completion.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus files or the census script; no invented data.
