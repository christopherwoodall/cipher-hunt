# Battery report: gov-excl-inf-drama-recall

- Target id: `gov-excl-inf-drama-recall`
- Claim: "close gov-excl-inf-register-drama's recall gaps:
  '?'-terminated exclamatory infinitives, preposition-to-infinitive
  spans longer than two short tokens, dash/colon pause marks"
- Date: 2026-10-09
- Worker: battery worker (subagent 2b2ab915-298c-4e21-a0b5-f1eb7ef7ddba)
- Stream: not applicable — corpus census against period French drama,
  per target charter (same taxonomy as the prose recall battery
  `battery-gov-excl-inf-recall`). The 1,847-pair repaired parse was
  not used. R5005, sealed gate instances, and the red-team
  adjudication queue were not touched.

Terms (ASD-STE100): "governed exclamatory infinitive" = an infinitive
governed by a preposition (pour / à / de) used as an exclamation in
its own right ("pour rire !" = the infinitive phrase IS the exclaimed
element, with or without a dislocated topic). "Genuine attestation" =
the "!" terminates the governed infinitive phrase itself; the
infinitive is not embedded in a finite matrix clause whose "!"
belongs to the matrix, and not embedded in an exclaimed noun phrase.
"Register" = the ingested drama corpus (14 distinct plays, the
byte-identical set of the parent drama battery).

## Parentage

Follow-up #2 of the PROMOTE `battery-gov-excl-inf-register-drama`
(2026-10-09). That battery found 1 genuine governed exclamatory
infinitive in the drama corpus (scribe-bertrand-et-raton:
"Pour conspirer !") but fenced three recall gaps its design never
searched: "?"-terminated windows, preposition-to-infinitive spans
longer than two short tokens, and exclamations adjacent to
dash/colon pause marks. THIS battery searches exactly those three
window classes in the drama corpus, and nothing else. It mirrors the
prose recall battery `battery-gov-excl-inf-recall` (1,874 candidates,
0 genuine, NULL) structurally.

## Bar (verbatim, pre-registered before testing)

"Close this battery's recall gaps ('?'-terminated exclamatory
infinitives, preposition-to-infinitive spans longer than two short
tokens, dash/colon pause marks) - same fenced gaps as the prose
battery; >=1 genuine re-opens"

Numbered pass/fail clauses (restated before testing, not modified
after):

1. If >=1 genuine attestation is found in the widened gap searches,
   the register question is re-opened (the parent's register-boundary
   evidence strengthens / the gap search adds new evidence).
2. If the widened search confirms zero genuine attestations, the
   recall gap is closed (the parent's n=1 stands with recall
   due-diligence complete).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/gov-excl-inf-drama-recall.lock`
   on start (agent id + UTC timestamp 2026-10-09T12:10Z); deleted on
   completion. No stale lock for this target existed.
2. Ran a reproducible census script:
   `code/crowd17/next-token/gov_excl_inf_drama_recall_census.py`
   (gap designs verbatim from `gov_excl_inf_recall_census.py`).
   Raw results in
   `code/crowd17/next-token/gov-excl-inf-drama-recall_census.json`
   (per-gap yields, per-file sizes, all 1,232 candidate windows with
   prep/infinitive/dist/terminator-offset fields) and
   `code/crowd17/next-token/gov-excl-inf-drama-recall_windows.json`
   (full windows for hand reading).
3. Corpus, byte-identical to the parent drama battery (file set
   pinned by name from `gov-excl-inf-register-drama_census.json`;
   total asserted in-session): 14 files, 2,969,582 characters,
   13,212 "!" (same files as the parent: dumas-antony,
   dumas-henri-iii, dumas-kean, dumas-mariage-louis-xv-1841,
   dumas-tour-de-nesle, hugo-burgraves, hugo-hernani-1870,
   hugo-ruy-blas, labiche-chapeau-de-paille,
   labiche-martin-poudre-aux-yeux, musset-comedies-proverbes-1850,
   scribe-bertrand-et-raton, scribe-verre-d-eau,
   vigny-chatterton-1835).
4. The three gap searches (exact patterns in the script); each
   targets windows the parent's design could not produce:
   - G1 ('?'-terminated): parent keyed ONLY on "!". For every "?"
     in the corpus: 120-char lookback, the parent's GOV_INF
     pattern verbatim (prep + 0-2 short tokens + infinitive-shaped
     word), closest match to "?", no [.;] between match end and
     "?" (same sentence-internal rule as the parent). ALL G1
     candidates are novel by construction. 872 candidates (629
     tight, dist<=40).
   - G2 (long spans): parent's GOV_INF allowed at most 2 short
     tokens between prep and infinitive. For every "!": 300-char
     lookback, LONG_INF = prep + 3-6 short tokens (each <=8 chars)
     + infinitive-shaped word, closest match to "!", same
     no-[.;]-tail rule. Novelty is structural: the {3,6}-token
     floor vs the parent's {0,2} ceiling makes the spans disjoint.
     248 candidates (99 tight).
   - G3 (dash/colon-adjacent): parent kept only the CLOSEST match
     per "!" (its candidates() keeps max g.end()). For every "!":
     120-char lookback, ALL GOV_INF matches; keep the non-closest
     ones where a dash (em/en/hyphen) or colon lies between the
     match end and the "!" (no [.;] between match end and the pause
     mark). 24 candidates (1 tight).
   - Dist = chars from infinitive-shaped word end to terminator.
     Tight band dist<=40 is the discriminating band (the exclaimed
     element is the infinitive phrase itself).
5. Classification. Tight band (748 candidates) fully classified by
   hand, in two passes. Pass 1 (automatic): 197 candidates whose
   infinitive-shaped word is on the NEVER_INF denylist (verbatim
   from the prose recall battery) — excluded as cause A, the
   parent's cause-A class. Pass 2 (manual): the remaining 551
   tight candidates read window by window and classified A-hand
   (drama-specific never-infinitives recorded below), B
   (finite-matrix embedding), C (exclaimed-NP embedding), D
   (terminator belongs to a following quotation/interjection), E
   (interrogative matrix, '?' windows), or GENUINE. Wide band (484
   candidates) scanned in full, parent battery's "scanned"
   treatment. The 88 G3-diag candidates (non-closest matches with
   NO dash/colon — untested by the parent but outside this
   battery's three named gaps) were scanned as due diligence: 19
   tight classified, 69 wide scanned, 0 genuine (all B/A/D).
   Classification record in
   `code/crowd17/next-token/gov-excl-inf-drama-recall_classification.json`.

## Window-level evidence

### Census yields

- G1 '?'-windows: 872 candidates (629 tight). Tight: 427 E, 197
  auto-A + 34 hand-A (nouns/names/OCR/finite forms), 1 C-adjacent
  (bare exclamation "De la voir! Où?" — '?' belongs to "Où?").
- G2 long spans: 248 candidates (99 tight). Tight: 1 GENUINE,
  54 B, 15 hand-A (chevalier, sentier, soir, m'entoure finite,
  rare, bassompierre, martyre, gaultier, tager=OCR "partager",
  meurtrier), 2 C, 1 D.
- G3 dash/colon: 24 candidates (1 tight: 1 auto-A). 23 wide
  scanned (B/C/D/A).
- G3-diag (diagnostic): 88 candidates (19 tight: 17 B, 2 hand-A
  [peintre, palefrenier nouns]; 69 wide scanned, 0 genuine).
- **1 of 1,232 gap candidates is genuine.**

### The genuine attestation (G2, tight band, dist 1)

- (labiche-martin-poudre-aux-yeux.txt, pour/montrer, dist 1, 3
  intervening tokens "ne pas la") — the full exchange verbatim:
  - MADAME MALINGEAR: "Elle était si petite… si petite… que tu
    en avais honte… Tu la cachais sous ton gilet."
  - MALINGEAR: "Pour ne pas la perdre."
  - MADAME MALINGEAR: "Oh ! non… pour ne pas la montrer !…
    Nous l'avons remplacée par une autre…"
  - Mme Malingear's turn is a corrective elliptical retort: the
    "!" terminates the pour-infinitive phrase itself. No finite
    matrix verb governs the phrase in her turn ("Oh ! non" is an
    interjection, not a finite clause; the continuation "Nous
    l'avons remplacée par une autre…" is a separate declarative
    with no exclamatory terminator). The governed infinitive
    phrase is the exclaimed element — exactly the "Pour
    conspirer !" shape (also an elliptical corrective retort in
    dialogue), with a non-demonstrative (zero) topic.
  - The 3 intervening tokens ("ne pas la") place it beyond the
    parent drama battery's 2-short-token ceiling: the parent's
    GOV_INF could never match this window. It is novel by
    construction, not a recount of the parent's find.

### Exclusion causes (tight band, 1,232 candidates)

**E — interrogative matrix, "?" belongs to a question** (427; all
G1): e.g. (dumas-mariage-louis-xv-1841 @26683) "Monsieur le comte
a-t-il des ordres à donner ?"; (musset @164836) "Pourquoi
refusez-vous de le dire ?"; (hugo-hernani-1870 @33189)
"Messieurs ! avons-nous fait cela pour rire ?" — '?' belongs to
the matrix "avons-nous fait cela pour rire ?", "pour rire" is its
purpose adjunct. The "Lui, pour rire ?" incredulity shape never
materializes in 872 "?" candidates.

**A — infinitive-shaped word is not an infinitive** (197 auto +
51 hand): nouns/adjectives/determiners ("votre", "soir",
"fenêtre", "peintre", "palefrenier", "sentier", "rare",
"martyre", "meurtrier"...), names ("chevalier", "bassompierre",
"gaultier", "Tenfer"), finite verb forms ("m'enivre", "vergeter",
"m'entoure"), OCR garbage ("llkure"=l'heure, "yotre"=votre,
"tager"=partager split).

**B — governed infinitive embedded in a finite matrix clause**
whose "!" belongs to the matrix (69): e.g. (scribe-verre-d-eau
@37974) "il m'a été facile de deviner que cela me concernait…
moi !"; (hugo-burgraves @145560) "Je suis même content qu'elle
te soit venue / Pour pouvoir à jamais l'arracher de ton cœur !";
(vigny-chatterton @100194) "Ouvrir son cœur pour le mettre en
étalage sur un comptoir !" — the bare-infinitive positive
control re-observed: the exclaimed element is the bare "Ouvrir",
the pour-phrase is its adjunct; (hugo-ruy-blas @182977) "Mais
c'est à se briser le front contre le mur !" — finite copular
matrix "c'est" owns the "!" (B under the strict taxonomy).

**C — infinitive embedded in an exclaimed noun/adjective phrase**
(2): (vigny-chatterton @99204, G2 wide-leaning) "Il ne s'agit
plus / de sourire et d'être bon ! de saluer et de serrer /
la main !" — matrix "il ne s'agit plus" (B/C boundary);
(hugo-hernani-1870 @173916) "Le temps de respirer et de voir
seulement !" — the exclaimed element is the NP "le temps de",
not the governed phrase.

**D — terminator belongs to a following interjection** (1):
(dumas-henri-iii @120331) "n'auras-tu de courage que pour
meurtrir le bras d'une femme… Ah !".

### Wide-band scan (484 candidates, "scanned" treatment)

- G1 wide (243): "?" with dist>40 — the infinitive phrase cannot
  be the exclaimed element; all interrogative matrices.
- G2/G3 wide with real infinitive-shaped words (123 read):
  all B/C/D/A by the same taxonomy. Notable recurrences:
  (hugo-burgraves @143387) "A fait aux pieds de Dieu murmurer
  le tonnerre !" (B); (dumas-henri-iii @124014) "je te maudis
  pour ton amour qui me fait entrevoir le ciel et mourir…
  mourir !" (B); (musset @709493) "de m'expliquer ce que cela
  signifie" (B).
- G3-diag wide (69): 0 genuine.

### Positive controls (the widened census detects the shapes)

The bare exclamatory infinitive re-attests inside the widened
windows (vigny "Ouvrir son cœur…!", "Il ne s'agit plus de
sourire…!"), proving the zero in G1/G3 is not a detection
failure: the widened patterns fire on exclamatory infinitives
when they exist — they find the BARE variant and exactly one
governed one (G2), never a "?"-terminated or dash/colon-adjacent
governed one.

## Per-clause pass/fail

1. >=1 genuine attestation in the widened search re-opens:
   **PASS.** 1 genuine of 1,232 candidates: (labiche,
   Martin Poudre-aux-yeux) "Oh ! non… pour ne pas la montrer !"
   — governed exclamatory infinitive, elliptical corrective
   retort, 3-token prep→infinitive span, no finite matrix. The
   register question is re-opened: the construction now counts
   n=2 in the drama corpus (Scribe's "Pour conspirer !" +
   Labiche's "pour ne pas la montrer !"), and the G2 long-span
   gap — closed by design — is where the second attestation was
   hiding. Two playwrights now attest it, which weakens the
   Scribe-idiolect fence and feeds the sibling battery
   gov-excl-inf-drama-n2 directly.
2. Confirmed zero closes the recall gap: **ANTECEDENT FALSE.**
   The zero does not hold in G2; it holds in G1 (872/872
   excluded) and G3 (24/24 excluded), so those two gaps close
   with a confirmed zero.

## Verdict: PROMOTE

One genuine governed exclamatory infinitive in the widened
drama-census searches (Labiche, Martin Poudre-aux-yeux:
"Oh ! non… pour ne pas la montrer !") — a long-span
prep→infinitive window the parent drama battery's 2-token
ceiling could never see. The register question re-opens:
governed exclamatory infinitives now count n=2 in drama
(Scribe + Labiche), both dialogue-elliptical corrective
retorts. G1 ("?") and G3 (dash/colon) gaps close with confirmed
zeros; G2 closes with a genuine attestation.

### Caveats (stated, not hidden)

- n=2 genuine total across the drama corpus (839 parent + 1,232
  gap candidates, 2 genuine). The register-boundary claim stays
  thin but meets the pre-registered ">=1 genuine" bar.
- Both drama attestations are dialogue-anaphoric corrective
  fragments, not fully conventionalized standalones like "pour
  rire !". The construction's drama habitat is elliptical
  retort; its status as a conventionalized exclamation remains
  unestablished.
- The new attestation carries a leading interjection
  ("Oh ! non"); the '!' terminating the governed phrase is the
  operative terminator, and no finite matrix verb stands between
  them — graded genuine under the parent battery's strict
  taxonomy, recorded for red-team grading.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this promote contradict the standing prose
  NULL (battery-gov-excl-inf-register, prose recall gap closed
  with 0 genuine)? No — different register; the prose zero
  stands. This promote strengthens the parent drama battery's
  PROMOTE rather than contradicting anything.
- Self-check: does this contradict any standing red-team
  verdict? No — no red-team verdict covers governed infinitives.
- Self-check: novelty — is "pour ne pas la montrer !" really
  untested by the parent drama battery? Yes: 3 intervening
  tokens exceed the parent GOV_INF's {0,2} ceiling, so no
  parent-census match could span it; verified byte-exact that
  the parent's regex cannot produce this candidate.

## Follow-ups (promote; optional, not mandatory)

1. **gov-excl-inf-drama-n2**: the sibling battery (already
   queued) now has two attestations from two playwrights to
   widen from — the Scribe-idiolect question is materially
   easier to test.
2. **gov-excl-inf-drama-long-n3** (P4): widen the drama corpus
   and rerun LONG_INF at 3-6 token spans only (G1/G3 closed) to
   raise the genuine count above n=2.

## Bookkeeping

- Census script:
  code/crowd17/next-token/gov_excl_inf_drama_recall_census.py
  (re-runnable; gap designs verbatim from the prose recall
  battery; outputs gov-excl-inf-drama-recall_census.json and
  gov-excl-inf-drama-recall_windows.json).
- Classification harness:
  code/crowd17/next-token/gov_excl_inf_drama_recall_classify.py;
  decisions in
  code/crowd17/next-token/gov-excl-inf-drama-recall_classification.json
  (E 427, B 69, A-hand 51 + auto 197, C 2, D 1, GENUINE 1).
- Report: code/crowd17/report_inbox/battery-gov-excl-inf-drama-recall.md
  (this file).
- battery-queue.json: `gov-excl-inf-drama-recall` queued ->
  verdict/promote via temp-file + rename (pre-write assert
  confirmed queued/verdictless; JSON re-validated post-write;
  own entry only; claim/bars/adverses preserved).
- Lock created on start (agent id + UTC timestamp
  2026-10-09T12:10Z), deleted on completion. No stale lock for
  this target existed.
- R5005, sealed gates, red-team queue untouched. Every number
  traces to the named corpus files or the census script; no
  invented data.
