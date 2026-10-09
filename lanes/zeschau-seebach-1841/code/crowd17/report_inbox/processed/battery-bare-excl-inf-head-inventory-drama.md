# Battery report: bare-excl-inf-head-inventory-drama

- Target: `bare-excl-inf-head-inventory-drama`
- Date: 2026-10-09
- Worker: battery worker (subagent 34f71c0c)
- Stream: not applicable — corpus census against period French drama, per
  target charter and the disloc program precedent. The 1,847-pair repaired
  parse was not used. R5005, sealed gate instances, and the red-team
  adjudication queue were not touched.

Terms (ASD-STE100): "bare exclamatory infinitive" = an infinitive used as an
exclamation with no preposition (de, pour), no "que", no resumptive clitic.
"Head" = the topic before the infinitive. "Demonstrative-headed" = a
demonstrative (cela/ceci/ca/celui...) as fronted topic. "Dialogue" = the
spoken speech of the plays (speaker-header format), not prefaces, cast lists,
or stage directions.

## Parentage

Head-class inventory complement to the disloc-demonstrative program. Does not
duplicate `disloc-demonstrative-drama-dialogue` (demonstrative-only census):
this battery enumerates ALL bare exclamatory infinitives in drama dialogue
and classifies them by head type, to test whether the arm-(a) fence holds
exactly at the demonstrative head or more broadly.

## Bar (verbatim, pre-registered before testing)

"Census of bare exclamatory infinitives in drama dialogue lands with a
head-type table (topic-demonstrative vs other); >=1 demonstrative-headed hit
re-opens arm (a) of ce87-1028-role"

Numbered pass/fail clauses (restated before testing, not modified after):

1. A head-type table of bare exclamatory infinitives in drama dialogue
   exists (topic-demonstrative vs other).
2. At least one GENUINE demonstrative-headed bare exclamatory infinitive is
   found. If yes: arm (a) of ce87-1028-role re-opens (drama register).

## Method

- Corpus: the same 14-file drama corpus as the drama-dialogue battery
  (Dumas x5, Hugo x3, Labiche x2, Musset comedies-proverbes, Scribe x2,
  Vigny Chatterton; 2,939,372 chars). Hetzel 1889 Hernani
  (`hugo-hernani.txt`); `hugo-hernani-1870.txt` excluded per the
  one-edition rule.
- Pass: for each `!`-terminated clause, take the last 160 chars; find an
  infinitive-shaped word within the first 40 chars; exclude if a subject
  pronoun / finite-verb marker / governor / "que" precedes it. Classify the
  head text before the infinitive: DEM_TOPIC (demonstrative fronted topic),
  TONIC (tonic pronoun), NOUN (other nominal), ZERO (infinitive first or
  punctuation-only head), OTHER (residual), DEM_OTHER (demonstrative inside
  head but not as fronted topic).
- Script: `code/crowd17/next-token/bare_excl_inf_head_inventory_drama_census.py`;
  raw results: `code/crowd17/next-token/bare-excl-inf-head-inventory-drama_census.json`.

## Findings

### Head-type table (2,939,372 chars; 1,641 pattern-level candidates)

| Head class | Candidates | Review | Genuine demonstrative-headed |
|---|---|---|---|
| DEM_TOPIC (demonstrative fronted topic) | 4 | all 4 hand-reviewed | **0** |
| DEM_OTHER (demonstrative in head, not topic) | 9 | all 9 hand-reviewed | **0** |
| TONIC (tonic pronoun) | 19 | all 19 hand-reviewed | n/a (see below) |
| ZERO (infinitive first) | 388 | recall control | n/a |
| NOUN | 188 | pattern level | n/a |
| OTHER | 1,033 | pattern level | n/a |

Clause 2: FAIL — 0 genuine demonstrative-headed bare exclamatory infinitives.

### Demonstrative-involving candidates (all 13, with cause)

1. Kean: "Avec cela, notez encore qu'elle loge..." — 'encore' is suffix
   noise (-re ending); cela governed by "avec". FALSE.
2. Kean: "celui-là ; l'autre le trouvait..." — 'autre' suffix noise; no
   infinitive. FALSE.
3. Kean: "et tout cela contre une enfant..." — 'contre' suffix noise (-re);
   "à être brisée" governed. FALSE.
4. Dumas mariage: "cela s'ouvre toujours tout seul." — finite "s'ouvre";
   "!" belongs to "Dam !". FALSE.
5. Hernani: "Cela vaut la lumière et le bruit." — finite "vaut";
   'lumière' suffix noise. FALSE.
6. Musset: "après tout cela, avoir peuplé un palais d'ouvrages
   magnifiques... à Florence !" — NEAREST NEAR-MISS. "avoir" is a genuine
   bare exclamatory infinitive, but the head "après tout cela" is a
   preposition-governed adjunct, NOT a dislocated demonstrative topic.
   Same window as the drama-dialogue battery's near-miss #21; classified
   OTHER (preposition-governed adjunct head).
7. Musset: "Ouvrez celle fenêtre..." — 'celle' is a determiner; "fenêtre"
   is a noun (suffix noise). FALSE.
8. Musset: "tout cela coûte très-cher..." — finite "coûte". FALSE.
9. Musset: "Celle clef ouvre ma chambre" — finite "ouvre". FALSE.
10. Musset: "dans celle fraîche aurore de jeunesse..." — cela governed by
    "dans"; 'aurore' is a noun (suffix noise). FALSE.
11. Musset: "sur celle misère couronnée..." — cela governed by "sur";
    'misère' is a noun (suffix noise). FALSE.
12. Scribe Bertrand: "cela ne pouvait pas durer !" — finite "pouvait". FALSE.
13. Scribe verre-d'eau: "celui-là, j'en suis sûre…" — finite; "!" belongs
    to "parlons plus". FALSE.

### Positive-space contrast (why the zero is a fence, not blindness)

The census does find genuine bare exclamatory infinitives with other heads:

- **Tonic-pronoun heads (5 genuine):** "moi, fuir devant le duc de Guise !"
  (henri-iii); "moi, céder la place à Kemble et à Macready..."
  (kean); "… Eux rire… mille démons !" (antony); "… moi, épouser une
  autre femme !" (chapeau-de-paille); "Moi, déprécier le commerce !"
  (bertrand-et-raton). The other 14 TONIC candidates are false friends
  (imperatives like "Laisse-moi fuir !", governed shapes, wrong-"!").
- **Zero-topic heads:** recall control "— Gouverner tout cela !" (hernani)
  caught; plus "Fuir, et comment !", "… Fuir !" (henri-iii), "Sortir… tous
  les yeux se fixeront sur moi…" (antony) — 95 infinitive-first
  zero-topic candidates.

**Result:** tonic pronouns license bare exclamatory infinitives in drama
("Moi, déprécier le commerce !"); demonstratives never do (0 genuine of
13 demonstrative-involving candidates). The arm-(a) fence holds exactly at
the demonstrative head.

### Recall limitations (stated, not hidden)

- Head window capped at 40 chars from clause start; infinitive beyond
  that is missed (the disloc program's separator-recall batteries cover
  the long-pause risk independently).
- Suffix-pattern false positives handled by hand review of the
  discriminating classes; the big OTHER/NOUN/ZERO classes are
  pattern-level counts, not hand-verified.

## Verdict: NULL

Clause 1 PASS (the table lands). Clause 2 FAIL (0 genuine
demonstrative-headed hits). Per §4, zero is an absence: arm (a) of
ce87-1028-role stays fenced at the demonstrative head, now with
positive-space contrast (tonic-pronoun and zero-topic heads license the
shape). No standing or red-team verdict contradicted; §7 intact.

## Follow-ups proposed (verified absent from queue)

1. `tonic-vs-demonstrative-topic-census` (P4) — tighter-pattern census
   quantifying the tonic-topic vs demonstrative-topic licensing contrast
   as a grammar fact of the drama register.
2. `ceci-dem-head-dialogue-recall` (P4) — recall-gap closure: allow up to
   3 intervening words between demonstrative and infinitive
   ("Cela, mes amis, partir !").
3. `bare-excl-inf-head-inventory-prose` (already queued) — same head
   inventory on the 27.66M-char prose corpus; adopt its head table rather
   than duplicating this work.

## Bookkeeping

- Report: this file
  (`code/crowd17/report_inbox/battery-bare-excl-inf-head-inventory-drama.md`).
- Census script:
  `code/crowd17/next-token/bare_excl_inf_head_inventory_drama_census.py`;
  raw JSON:
  `code/crowd17/next-token/bare-excl-inf-head-inventory-drama_census.json`.
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched.
