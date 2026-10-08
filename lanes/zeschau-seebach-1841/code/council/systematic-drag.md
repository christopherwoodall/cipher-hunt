# THE SYSTEMATIC DRAG — attack plan

**Status:** plan only (pre-registration). No drag has been run.
**Author:** the Crib Dragger, 2026-10-07.
**Lane:** `~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/`
**Target:** R5005 — 1841 French diplomatic nomenclator, repaired parse
(1,847 pairs → 1,847 group tokens, 96 group types 00–95).

## 0. Why this hasn't been done, and why now

The lane drags cribs one by one ("Méhémet-Ali" @8, "parmi" @1196,
"par ce que" ×3, "la première fois" @1034). Each drag is bespoke:
a human picks a phrase, syllabifies it by ear, and checks one window.
That finds what we already suspect. It cannot find what we don't.

The systematic drag inverts this: take every high-frequency
diplomatic phrase of 1840–41 and test it at every position, scored
against the board. The compute is trivial (Section 4). The only reason
it hasn't been run is that nobody specified the inventory, the
scoring, and the null. This document is that specification.

## 1. Phrase-inventory spec

### 1.1 Sources (all under `code/side-period/corpus/`, public domain)

| Tier | Files | Role |
|---|---|---|
| DIPLOMATIC CORE | nesselrode-v7/v8/v9/v10, guizot-memoires-t5-t6 (his 1840–42 despatches), levant-correspondence-1841-p3 | primary: French diplomatic register, 1840–42 |
| PRESS | revue-deux-mondes-1841-q1..q4, allgemeine-zeitung-1841-01-*.txt (French excerpts only) | secondary: topical collocations |
| MEMOIR | guizot t1–t3, metternich v4/v6, talleyrand v1, pozzo-di-borgo v1 | tertiary: formulaic background |

**CAUTION (standing):** Nesselrode v8 contains archive.org OCR
word-splits ("ment" tokens etc.). v8 is VOID for phrase queries —
use it for unigram/bigram rates only. Phrase extraction uses the
clean pool: Guizot t5–t6 + Levant + RdM + Metternich + Talleyrand
(~3.9M tokens after filtering).

### 1.2 Extraction

1. Tokenize with the lane's `tok_elision` tokenizer **verbatim**
   (elisions preserved: "l'", "d'", "qu'", "n'").
2. Lowercase; strip accents for matching (the cipher is accent-blind
   per the by-ear convention) but KEEP the accented form for the
   human-readable inventory.
3. Count word 2-grams, 3-grams, 4-grams over the clean pool.
4. Keep an n-gram iff:
   - it occurs ≥ 5× in the DIPLOMATIC CORE, **or** ≥ 25× in the full
     clean pool; **and**
   - it is not subsumed: if bigram B ⊂ trigram T and
     freq(B) < 1.5 × freq(T), keep T only (kills "de la" in favor
     of "de la Porte" when the longer form dominates).
5. Seed the inventory with the lane's known items regardless of
   frequency: the formulae miner's inventory
   (`code/french-blitz/formulae-inventory.md`), all live cribs
   ("Méhémet-Ali", "parmi", "même", "par ce que",
   "la première fois", "ne ment pas"), and the 117 adjudicated
   crib cards (`code/side-period/cribs-adjudicated.md`).
6. Target **500 phrases**; cap at **2,000** (compute still trivial,
   Section 4). Rank by `freq × log(1 + diplomatic_core_freq)`.

### 1.3 By-ear syllabification

Each phrase → one or more syllable sequences using the lane's
**frozen** by-ear syllabifier (pin the exact script + commit in the
run log; do NOT use `canonical.py` — it still loads the obsolete
1,846-pair parse per the 59-mapper's finding).

Generate **licensed variants** per phrase for the cipher's
over-splitting (Frenchman H-split: the clerk writes /k/ as 46="que"
before vowels, splits "m'en", etc.). Variant rules (lane by-ear
conventions, documented per variant):
- V0: plain by-ear syllabification.
- V1: consonant-onset splits licensed by GT precedent
  (e.g. "que" → "k"+"e" where the cipher does so).
- V2: elision-joined forms ("l'est", "c'est", "n'est" as units).

Cap at 3 variants per phrase; record which variant hit.

## 2. Scoring function

### 2.1 The board oracle

Build ONCE, freeze as JSON (`board_oracle.json`):

```
oracle[(group, predecessor)] -> value | None
```

Sources, in precedence order:
1. **7 pencil GT** (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que) —
   unconditioned, infallible for scoring.
2. **5 provisional** (87=ce, 64=qui, 96=par, 59=est, 77="le"
   prov-conditioned) — applicable per their standing conditions.
3. **Restructured registry** (`code/crowd14/registry/REGISTRY.md` —
   round-14 rewrite per red-team R-IA1–R-IA7; supersedes the 10-islet
   registry). Word rules: W-est1 (93-59 «l'est»), W-est2 (94-59 «n'est»),
   W-este2 ([stem]-59 -este verb), F-qui-est (64-59 «qui est»),
   F-qui-le (64-77 «qui le») + W-este1 (84-59 «[X]este»),
   W-m'en (82-84 «m'en»), F-en («[noun] en [V]» arms), W-par-le
   (96-00 «par le»), W-ment (82-06 «ment»). Sole true polyvalence: the
   67 et/veut fork (SUPPORTED). Class tier: 66 / 89 (values NULL). Old
   example conditioning (e.g. 84="en" iff pre∈{82,66,89}) is retired as a
   cell rule — use the word/frame forms. Banked falsifiers and fences
   carry; splits {52,59}, {76,78}, {33,86}, {48,94} are constraints.

A group with no applicable value → `None` (NEUTRAL — absence of
evidence, scores 0, never a contradiction).

**Value comparison** is by-ear normalized: strip accents, lowercase,
apply the lane's equivalence classes (e.g. "é"/"e"). A syllable
"matches" a board value iff normalized strings are equal.

### 2.2 Per-alignment score (pseudocode)

```
def score(phrase_syllables, pos):
    # phrase_syllables: list of k normalized syllables, k >= 3
    # pos: 0-based start in the 1,847-group stream
    matches = 0      # syllable == oracle[(G[pos+i], G[pos+i-1])]
    anchored = False # at least one match on GT or provisional
    contra  = 0      # syllable != oracle value (oracle non-None)
    for i, syl in enumerate(phrase_syllables):
        g = stream[pos+i]
        v = oracle.get((g, stream[pos+i-1] if pos+i>0 else None))
        if v is None:
            continue            # neutral: unknown group
        if v == syl:
            matches += 1
            if board_status(g) in (GT, PROVISIONAL):
                anchored = True
        else:
            contra += 1
    return matches, anchored, contra
```

### 2.3 Pre-registered hit bar

A (phrase, variant, position) is a **HIT** iff ALL of:

- **H1** `k ≥ 3` — syllable count at least 3 (1–2 syllable phrases
  false-positive constantly; they are excluded from the inventory,
  not merely down-ranked).
- **H2** `contra == 0` — zero contradictions (primary run).
- **H3** `matches ≥ max(2, ceil(0.5 × k))` — at least two, and at
  least half, of the syllables land on known board values.
- **H4** `anchored == True` — at least one match on a GT or
  provisional value (registry-only matches don't anchor).
- **H5** the phrase's corpus frequency rank is in the inventory
  (no post-hoc phrase invention).

**Ranking** among hits: `matches × log(1 + corpus_freq)`, tie-broken
by longer k.

**Sensitivity variant (pre-registered):** re-run with H2 relaxed to
`contra × 5 ≤ matches` (penalty instead of veto). Rationale: a
wrong provisional (77="le" is provisional-*conditioned*) would
veto true phrases under the hard veto. Any hit that appears ONLY
in the relaxed run is flagged `VETO-SENSITIVE` and does not
promote — it diagnoses board risk instead.

### 2.4 Worked example (what a hit looks like)

"par ce que" (k=3: par|ce|que) @224:
groups [96, 87, 46] → par (96 provisional) ✓, ce (87 provisional) ✓,
que (46 GT) ✓. matches=3, contra=0, anchored=True (GT).
**HIT**, and in fact the formulae miner already confirmed it —
the drag must reproduce this as a sanity check (if the drag
does NOT hit "par ce que" @224/@952/@1526, the implementation
is broken — pre-registered positive control).

## 3. Null design and false-positive rate

### 3.1 Shuffled-stream null (primary)

For `S = 20` replicates: randomly permute the 1,847 group tokens
(preserving unigram frequencies — this keeps the board-match base
rates honest), re-run the full drag with identical inventory and
bar. Count hits per replicate: `h_1 … h_20`.

- **FDR estimate:** `mean(h_s) / max(1, h_real)`.
- **Per-hit p-value:** fraction of replicates with ≥ as many hits
  at ≥ the hit's rank-score.
- Pre-registered interpretation: the drag "works" iff
  `h_real > max(h_s)` (real beats all 20 shuffles).

### 3.2 Decoy-inventory null (secondary)

Drag an inventory of ~100 **anachronistic** phrases (post-1841
coinages, 20th-century diplomatic formulae — e.g. "guerre froide",
"société des nations") against the REAL stream at the same bar.
Expectation: ~0 hits. Any hit is a pure false positive and
calibrates the bar's looseness directly. (If decoys hit, the bar
is too loose — tighten H3 before believing real hits.)

### 3.3 Expected false-positive intuition

With ~12 anchored groups out of 96 and typical group unigram
~1–3%, a random 3-syllable window has P(≥2 anchored matches,
0 contra) ≈ small but nonzero; over 923k phrase-positions the
shuffle null — not closed-form math — is the honest estimator.
This is WHY the null is empirical. Do not hand-wave it.

## 4. Compute architecture

### 4.1 Scale

| Step | Work | Estimate (this VM: 2 CPU, 7 GB) |
|---|---|---|
| Inventory build | n-gram count over ~3.9M tokens | 5–10 min, single Python pass |
| Syllabify | ≤2,000 phrases × ≤3 variants | seconds |
| **Drag** | 2,000 × 1,847 ≈ 3.7M alignments × ~4 syllable lookups ≈ 15M dict ops | **2–6 min single-threaded** |
| Null (20 shuffles) | 20 × drag | 40–120 min single-threaded; **embarrassingly parallel → 20–60 min on 2 CPUs** |
| Decoy null | 100 × 1,847 ≈ 185k alignments | ~30 s |

**Verdict: TRACTABLE.** End to end under ~2 hours on this VM,
dominated by the shuffle null. No GPU, no cluster, no new
infra needed. Memory footprint < 200 MB.

### 4.2 Implementation notes

- Build the stream ONCE from `repaired_offsets.json` +
  `data/upstream-ct_R5005.digits.txt` (re-derive the 1,847 group
  sequence in the drag script; do NOT import `canonical.py`).
- Optional pruning (not required at this scale): inverted index
  group → positions; skip (phrase, pos) where no syllable can
  match a known group. Implement only if scaling past 2,000 phrases.
- Determinism: seed every shuffle (`seed = 1000 + s`); log seeds,
  inventory hash, oracle hash, syllabifier version. The whole run
  must be re-derivable byte-identical.
- Output: `drag_hits.json` — every hit with phrase, variant,
  position, per-syllable alignment table, matches/contra,
  rank-score, and `veto_sensitive` flag.

### 4.3 What the output feeds

- Hits → red-team docket (each hit is LEAD-grade max; promotion
  needs the standing ≥2-leg rule — a drag hit is ONE leg).
- `VETO-SENSITIVE` hits → board-risk review (they mark where a
  provisional may be vetoing truth).
- Null results (a clean drag with FDR ≈ 1) → evidence that the
  remaining plaintext avoids the top-500 formulaic phrases, which
  itself constrains register/topic.

## 5. Standing caveats

1. The drag inherits the by-ear segmentation model (see weakest
   assumption, below). Licensed variants (V1/V2) cover the KNOWN
   over-splits; unknown clerk habits are not covered.
2. The registry's predecessor-conditioned rules are consulted with
   predecessor context only; the registry's successor-conditioned rules
   (if any are added) require a two-sided oracle — spec it then.
3. The DIPLOMATIC CORE is ~4M tokens but skewed (RdM is press,
   not despatches). Weight accordingly; the Guizot-despatch slice
   is the highest-register subset — consider a core-only run as
   a pre-registered variant.

---

## 6. The paradigm's weakest load-bearing assumption

**The by-ear segmentation model — the assumption that we know how
the clerk cut French into the group stream — is the load-bearing
assumption everything else stands on, and it is the least
proven.** Every crib drag in lane history, including this plan,
aligns phrase-syllables to groups 1:1 under a syllabifier built
from *spoken* French plus a handful of licensed over-splits. But
the Frenchman's H-split finding proved the clerk does not segment
like a speaker: 46="que" writes a bare /k/ before vowels, "m'en"
splits where speech doesn't, and the over-splitting has no
published rule — we have examples, not a grammar. If the clerk's
segmentation inserts or merges cells unsystematically (a habit,
not a rule), then a true phrase can sit in the stream and be
*unalignable* under our syllabifier: the drag returns null not
because the phrase is absent but because the ruler is wrong, and
worse, every "kill" of a phrase ("gouvernement" @1180,
"Méhémet-Ali" via 62='a') is contingent on the ruler being
right. The licensed variants (V1/V2) patch the known cases; the
unknown cases are unpatched and unpatchable until the clerk's
segmentation grammar is itself inferred — which is circular with
key recovery. Runner-up: provisional-board circularity (the
contradiction veto assumes 77="le" and friends are correct; the
sensitivity variant in §2.3 is the hedge). Mitigation for both is
built into the plan, but the assumption itself remains the
deepest unproven premise in the lane.
