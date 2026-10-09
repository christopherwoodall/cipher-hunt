# Battery `tout-88-frame` — verdict: PROMOTE

## Bar tested (verbatim)
The queue entry's `bars` field is `None` (no bars registered). Per §2 I do not
silently rewrite: the numbered clauses below are derived directly from the
claim text, stated here explicitly.

Claim (verbatim): Characterize the "tout [88]" frame at @496-497 — under
granted 79="tout", enumerate the classes 88 can take there (noun/adjective/
adverb) and kill the ones the 23-window profile excludes. Constrains all
future 88 value claims.

- C1: Enumerate, from 1841-French grammar, the classes 88 can take at
  @496-497 under granted 79="tout" (A5), with standing neighbors.
- C2: Kill any of noun/adjective/adverb that the 23-window profile of 88
  excludes at battery grade.
- C3: State the resulting constraint on future 88 value claims.

## Method
Repaired 1,847-pair / 96-type stream re-derived in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts: 1,847 pairs, 96
types — held). `canonical.py` never used. Full 23-window census of 88 with
±2 context; every number below traces to the stream.

## Findings

### Locus
Row a2_11, 0-based: `@494=94 @495=02 @496=79 @497=88 @498=47 @499=11 @500=29`.
Standing: 79="tout" granted (A5), 47="ce" granted (A4), 11="la" pencil GT,
29="er" pencil GT, 94="ne" STRONG LEAD (R17-001). "47 11" reads "cela"
(demonstrative pronoun; "la" cannot be a noun here).

### C1 — class enumeration at @496-497 ("tout [88] cela er…")
1841-French grammar admits after "tout":
- **Noun** — "tout homme", "tout le monde". Admissible.
- **Adjective** — "tout petit", "tout nouveau" (tout as adverb + adjective).
  Admissible.
- **Adverb** — "tout près", "tout à fait" (tout as adverb + adverb).
  Admissible.
- **Past participle** — "tout compris" (tout as adverb + pp); adjective-class
  arm, folds into the adjective enumeration.
- **Finite verb** — KILLED at this locus: "tout" + finite verb is
  ungrammatical ("*tout veut"); no clause boundary is licensable between
  79 and 88 on standing values.
- **Bare infinitive** — KILLED at this locus: "tout" + infinitive needs
  "pour" ("pour tout dire"); the left neighbor is 02 (unvalued, and 00 — not
  02 — is the granted "pour", A9). No standing license.

C1 PASS.

### C2 — the 23-window profile excludes none of the three
n(88)=23, byte-exact. Predecessors: 21 distinct cells; followers: 19
distinct cells. Key profile legs:
- **Verb-forcing windows (battery grade):** @730 (88 forced finite,
  pron730-clause-wide PROMOTE), @1049 ("[88]ere" one-word finite shape,
  seg-88er-1049 PROMOTE), and "88 77" ×3 (@86, @646, @1541) — with 77="le"
  provisional, "88 le" parses only as verb + clitic object ("veut le");
  noun/adjective/adverb + "le" is ungrammatical.
- **Noun-compatible windows:** @42 ("01 24 88 43 81" — [V-fin] + 88 as
  object noun), @1267 and @1727 ("…69 88 24 30…" / "…39 88 24 30…" —
  "que ce [88-N] [24-V] [30]" reads grammatical with noun-88 under R24's
  finite/modal 24 and the conditioned 30="pas").
- **None of noun / adjective / adverb is excluded by the profile at battery
  grade.** The profile is non-uniform: 88 is verb-forced at some windows and
  noun-compatible at others. No window forces 88 non-nominal in a way that
  transfers to @496-497, and the tout-geometry admits all three classes.

C2 PASS (vacuous — nothing to kill; all three survive).

### C3 — constraint on future 88 value claims
Any future claim of a **uniform verb-88 value** must either (a) declare a
split at @496-497 (polyvalence is red-team venue, not battery), or
(b) re-parse the "tout [88]" frame — because finite verb and bare
infinitive are dead at this locus by tout-geometry while verb-88 is forced
elsewhere (@730, @1049, "88 77" ×3). A uniform 88 value covering @496-497
can only be nominal/adjectival/adverbial.

C3 PASS.

## Scope
Locus-level characterization only. No value named for 88, no class granted,
no split declared, no polyvalence claimed (red-team venue). The non-uniformity
observation is distributional, not a class claim. Untouched: 78='ver'
(deferred, R16-005 LEAD stands), 93's value, 02's value, the "94 02" frame.
No standing/red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands. No follow-ups per §4 (promote).

## Adverses
None listed.

## Bookkeeping
- Stream re-derived in-session; asserts held (1,847 pairs, 96 types).
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue
  untouched.
- Lock created on start, deleted on completion.
