# Battery verdict: regne-trone-tiebreak

**Verdict: NULL** — the tie is not broken at battery grade. Headline
(§5 escalation): the one frame where "règne" and "trône" make different
predictions favors **règne**, which contradicts the standing
battery-grade @508 "trône" locus promote. A battery worker cannot
downgrade that verdict; the tiebreak package goes to the red team.

## Bar (verbatim, pre-registered)

> 1. "Produce a frame where 'règne' and 'trône' make different
> grammaticality/collocation predictions, or fence as lexically tied
> pending neighbor resolution."
> 2. "Do not re-litigate the fenced C1/C2 scope findings; this is
> lexeme discrimination only."

Restated as numbered clauses (before testing):

- **C1**: Produce a frame where "règne" and "trône" make different
  grammaticality/collocation predictions — via (a) 1841 diplomatic
  French corpus collocational data for the attested frames
  ("le [62]ne qui", "[62]e [76]", "[62]ent"), or (b) a landed neighbor
  value (76, 98, 65, 93, 21) creating selectional pressure admitting
  one but not the other; OR fence as lexically tied pending neighbor
  resolution.
- **C2**: Lexeme discrimination only; the parent battery's fenced
  C1/C2 scope findings (val-62-ne-noun) are adopted, not re-litigated.

## Method

Read BATTERY-PROTOCOL.md first. Created
`locks/regne-trone-tiebreak.lock` on start (agent id + UTC timestamp).
Re-derived the repaired stream in-session from
`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt` (parsed per `repair_parse.py`):
**1,847 pairs / 96 types verified**. `canonical.py` never touched.
R5005, sealed gates, red-team adjudication queue untouched.

Locus windows byte-confirmed independently (0-based):
- @507–512 (row a3_00): `77 62 94 64 98 65`
  = "le [62]ne qui vient [65]"
- 62-06 windows: @665 (`80 03 62 06 00 20`, a4_02),
  @1536 (`73 41 62 06 21 62`, a8_00) — matches parent census
- 62-48 windows: 360, 425, 1315, 1349, 1464, 1569 — matches parent
- n(62) = 35 confirmed

Standing values adopted as premises (never re-litigated): 62 = "règn-"
/ "trôn-" stem (parent C1/C2); 98='vient' battery-promoted (pending
red-team ratification); 65 = noun class (R18, value open); 76 = noun
class (F104 battery lead, value open); 93="l'"-alone rate-KILLED;
21 = NOUN class (value search kill-closed); 77="le" provisional;
94 = particle-'ne' letter tier (R17-003); 06 = "-ent" with the
ent-06-host-census decision rule.

## C2 first: scope honored

No scope finding re-litigated. The parent's {règne, trône} narrowing,
the C1 parse test, the C2 six-window compatibility, the @508 head
re-test, and the §7 no-polyvalence posture are all adopted as given.
This battery tests lexeme discrimination only.

## C1: the discrimination hunt

### Avenue (b): landed-neighbor selectional pressure — NEGATIVE

None of the named neighbors has a landed value that admits one lexeme
but not the other:

- **98='vient'** (battery-promoted, pending ratification): at @508,
  "le [62]ne qui vient" admits both "le règne qui vient" and
  "le trône qui vient" grammatically. No pressure.
- **65** = noun class (R18), value open: "[62]ne qui vient [65]"
  admits any noun in 65's slot. No pressure.
- **76** = noun class (F104 battery lead), value open: "[62]e [76]"
  admits any noun in 76's slot. No pressure.
- **93**: "l'"-alone rate-KILLED — no value, no pressure.
- **21**: NOUN class, value search kill-closed — no pressure.

The keyhole is 65's value at @508 (see follow-up 1): a landed 65
value would create the selectional pressure this battery lacks.

### Avenue (a): corpus collocational data — DIFFERENTIAL FRAME FOUND

Corpus: `code/side-period/corpus/`, 62 files, **31,662,737 chars** of
1841-register French (prose, drama, newspapers, correspondence),
censused in-session.

**Frame "[62]ent" (3pl verb, @665/@1536): no discrimination.**
Both forms are real and both attested: "règnent" ×4, "trônent" ×1.

**Frame "[62]e [76]" (62-48 windows): no discrimination possible.**
76's value is open; no collocation can be tested.

**Frame "le [62]ne qui vient" (@508): DIFFERENTIAL.**

Selectional asymmetry (1841 French):
- "règne" is a temporal period. Temporal periods license "venir" in
  the onset sense — parallel to the attested "l'année qui vient" /
  "the coming year" class. "Le règne qui vient" = "the reign that is
  coming" is selectionally licensed.
- "trône" is a concrete object (the seat) / the institution-as-seat.
  As subject of lexical "venir" (arrive/come), it is selectionally
  anomalous: thrones are ascended to ("monter sur le trône",
  "venir au trône"), they do not themselves arrive. "Le trône qui
  vient" = "the throne that comes" is strained — exactly the strain
  the standing @508 "trône" promote itself recorded
  ("the phrase is semantically strained").

Corpus check (consistent with the asymmetry, not decisive on its own):
- "règne" as subject of "venir": 1 attestation —
  "regne vient de commencer en france" ("the reign has just begun";
  note: "venir de" onset construction).
- "trône" as subject of lexical "venir" (arrive/come): **0
  attestations in 31.66M chars**. The sole "trône"+"venir"
  collocation is "trônes qui viennent d'être abandonnés" —
  "venir de" recent-past auxiliary + passive participle, a different
  construction (the throne is not arriving; it is being abandoned).
- Exact frame "le [62]ne qui vient": 0 attestations for either arm
  ("règne qui" ×2, "trône qui" ×1 in the corpus, none with "vient").

Honest grading of this evidence: the frame makes different
predictions for the two lexemes (licensed + weakly attested vs
strained + unattested), but the corpus support is n=1 (and itself a
"venir de" construction) vs n=0 — below battery-grade confidence for
naming or killing either arm. Per the lane's own "zero is an absence"
principle, the trône arm cannot be killed on this.

### Why the verdict is NULL and not PROMOTE of the fence

The bar's primary clause is satisfied in form (a differential frame
was produced), but:

1. The differential evidence is below battery-grade naming
   confidence (corpus n=1 vs n=0; the asymmetry is selectional, not
   kill-grade grammaticality).
2. Naming "règne" would contradict the standing battery-grade @508
   "trône" locus promote (syll-94-508-verify's conditional promote,
   recorded in the lane summary as "locus-level word promoted as
   trône"). Per §5, a battery worker never downgrades an existing
   verdict — the contradiction is the headline and goes to the red
   team.
3. No landed neighbor value creates selectional pressure; the
   "[62]ent" frame admits both; the "[62]e [76]" frame is untestable
   with 76's value open.

So: the tie is **not** broken at battery grade. The evidence package
(frame + selectional asymmetry + corpus census) is a red-team input:
the red team can either (i) downgrade the @508 "trône" promote and
ratify "règne", or (ii) keep the tie fenced pending neighbor
resolution (65's value at @508 is the keyhole).

Note: the queued `re-prefix-03-665` target (03 as "re-" prefix at
Window A) is lexeme-neutral — "reprègnent"/"retrônent" are equally
non-French — and does not affect this verdict either way.

## Follow-ups proposed (for supervisor queuing)

1. `val-65-at-508` (P3) — Name 65's value at the @508 locus
   ("le [62]ne qui vient [65]"). A landed 65 value creates the
   selectional pressure this battery lacks: a temporal noun favors
   "règne", a concrete/institutional noun re-opens "trône".
   Bar: name 65 iff the value parses at @508 with zero new
   assumptions; the named value decides the règne/trône frame.
2. `trone-vient-register` (P3) — Wider 19th-century French search
   (beyond the lane corpus) for "trône" as subject of lexical
   "venir" (arrive/come, excluding "venir de" + infinitive and
   passive auxiliaries). Bar: ≥1 genuine attestation closes the
   selectional asymmetry (tie stands); confirmed zero across a
   larger base hardens the règne lean.
3. `redteam-508-reread` (P2) — Red-team adjudication of @508:
   the standing battery-grade "trône" locus promote rests on a
   semantically strained reading ("the phrase is semantically
   strained", per its own report); this battery's differential
   frame + corpus census is the input. The battery cannot
   downgrade the standing promote — red-team venue.

## Adverses

None listed on the queue target. The @508 "trône" promote is a
standing battery verdict, not an adverse on this target; it is
handled via the §5 escalation above, not re-litigated.

## Standing state

No standing verdict contradicted or downgraded. §7 intact (no
polyvalence declared). Canonical-stream caveat stands (row a3_00's
upstream offset unvalidated). The redteam-62-conditioned venue and
the parent val-62-ne-noun NULL are untouched.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-regne-trone-tiebreak.md`
  (this file)
- Queue: `battery-queue.json` `regne-trone-tiebreak` → status
  `verdict`, result `null`, date 2026-10-09 (pre-write assert
  passed — was queued/verdictless; temp-file + rename; JSON
  re-validated post-write; own entry only)
- Lock: `locks/regne-trone-tiebreak.lock` created on start, deleted
  on completion
