# Morphologist — R4 "-ment" word family (WO1, round 3)

**Claim under test:** 94=ne, 82=m (ground truth ✓), 06=ent — the trigram 94-82-06 reads
"ne-m-ent" as a "-ment"/"-nement" word family (gou-ver-ne-ment / dé-par-te-ment).

All counts recomputed from the pair stream (`crib_attack.load_pairs`, run from `code/`).
Phase profiles recomputed independently — they reproduce the contactor's 29=er signature
(next-B 0.894 vs contactor 0.89; prev-A 0.766 vs 0.77), so the instrument is sound.

## WO correction (instance inventory)

The WO said the extra 94→82 instances are @578/@1181, outside the ×2 repeat @1179/@1350.
Recomputation: **94→82 occurs 4× @ [578, 1181, 1352, 1741]**, and @1181 is *inside*
repeat #1 (77@1179, 78@1180, 94@1181). The true extras are **@578 and @1741** — and @1741
is **94-82-46** (follower 46=que, ground truth), *not* 94-82-06. So the test bed for the
family is: the ×2 repeat (77 78 94 82 06 @1179/@1350, byte-identical ✓) plus **one**
extra trigram @578 ("61 94 82 06 06"). The 94-82-06 trigram occurs **3×** total.

## (a) POSITIONAL — 06 is not word-final; 94 is medial ✓

Contactor phase model (k=12 Jaccard, χ²=181.3): cycle A→C→B→A with **C word-final-ish**
(29=er ∈ C; er→next block B = 0.894, i.e. B = word-initial), A medial, B initial.
(Note: the WO wrote "phase-A onset" — the contactor's word-initial block is **B**,
calibrated by 29=er; I used B.)

| group | block (k=8/12/16) | next-block | prev-block |
|---|---|---|---|
| 29=er | A/**C**/**C** | B=0.894 | A=0.766 |
| 06 | **A**/**A**/**A** | B=**0.196**, C=0.457 | A=0.435, B=0.435 |
| 94 | **A**/**A**/**A** | C=0.389, B=0.361 | B=0.583, A=0.278 |

- 06 sits in A (medial) at all three cuts; only 19.6% of its followers are word-initial
  vs 89.4% for er. **06 does not behave like a word-final syllable.**
- The three trigram-final 06s are followed by **06(A), 06(A), 52(C)** — 0/3 followed by a
  word-initial group. Under the er calibration, P(0/3 B-followers | word-final) ≈ 0.001.
- 94 ∈ A (medial) — compatible with "ne" inside -nement words.

## (b) FREQUENCY — era syllable rates (documented syllabifier)

Syllabification rule (orthographic, formal count): lowercase + strip accents;
nuclei = maximal vowel-letter runs; maximal onset (last consonant goes right) except
valid French liquid onsets {bl,cl,fl,gl,pl,br,cr,dr,fr,gr,pr,tr,vr} and digraphs
{ch,ph,th,gn} stay together; leading/trailing consonants attach; final mute -e is its
own nucleus. Sanity: gouvernement→gou|ver|ne|ment, parlent→par|lent, honneur→hon|neur.
Corpus: Tocqueville t1+t2 (201,057 words → 362,028 syllables). Les Mis not used.

| unit | cipher rate | era rate | ratio |
|---|---|---|---|
| 94 vs "ne" | 0.01950 (36, rank 12) | 0.01902 (n=6886) | **1.025×** |
| 94 vs "en" (rival) | 0.01950 | 0.01089 | 1.79× |
| 94 vs "re" (rival) | 0.01950 | 0.02081 | 1.067× — killed by geometry (82→94 = "m-re" impossible) |
| 06 vs "ent" | 0.02492 (46, rank 4) | 0.00735 – 0.01977* | **over the upper bound** |
| trigram 94-82-06 vs era ne-m-ent | 0.001627 (3/1844) | 0.001544 (563 -nement words) | **1.054×** |

\* "ent" never occurs as a standalone orthographic syllable (always merges: par|lent,
ai|ment) — the encipherer's m|ent split is idiosyncratic (cf. F22's parl|er). Era bounds
under encipherer granularity: lo = -ment words only (each yields m|ent), hi = all
-ent-ending words. Cipher 0.02492 sits 1.26× *above* the generous hi bound.
(Rate legs per WO: uncalibrated band — presented with structural corroboration, not standalone.)

Note: era "ne" count *includes* the standalone negation word (1804×); the 1.025× match
is against the inclusive count. The "ne…pas" frame is untestable until "pas" is
identified (77="pas" is H2-INCONCLUSIVE; 94→77=0 and 94-?-77=0 are currently void, not evidence).

## (c) FOLLOWERS of 06 in the instances — no word boundary

Instance followers of trigram-final 06: **06(A), 06(A), 52(C)** — none word-initial (B).
Global 06 followers: 77×6, 29×5, 00×4, 11×4(la✓), 67×3, 59/21/06/52/65/60×2.
As "ent": 06→77 "…ent pas" ✓ ("parlent pas") and 06→11 "…ent la" ✓ ("prennent la")
are grammatical — but **06→29(er)×5 = "ent|er" is ungrammatical** (no French word splits
ent|er; "entrer"→entr|er would need 06="entr", contradicting R4). 06→06×2 and 06→00×4
are unexplained as "ent".

## (d) PREDECESSORS of 94 — stem frames support "ne"; the 06 tension

Instance predecessors of 94: **61(A), 78(C), 78(C), 34(A)=i**. Globally 94's predecessors
are B-block (word-initial) dominated: 62×8, 42×4, 12×3, 82×3 — i.e. "pre|nez",
"te|nez", "do|nne"-type frames (B→A initial→medial ✓). This is a natural "ne" profile.

**The 06 tension (R4 "ent" vs F21 verb stem), scored:**

| frame | 06=verb stem (F21) | 06="ent" (R4) |
|---|---|---|
| 06→77×6 | "X pas" ✓✓ | "…ent pas" ✓ ("parlent pas") |
| 06→29×5 | "X-er" infinitive ✓✓ | "ent\|er" ✗✗ ungrammatical |
| 06→11×4 (la✓) | "X la" verb+object ✓ | "…ent la" ✓ ("prennent la") |
| 30 distinct preds | subjects ✓ | — |
| phase: 06∈A medial, next-B 0.196 | ✓ stem-like | ✗ must be final |
| 94-82-06 ×3 | ✗ ("ne-m-[stem]" fails) | ✓✓✓ |
| 06→06×2 | ✗ ("stem stem") | ✗ ("ent ent") — but reads as "…ent [stem]" under polyvalence |
| count of explained frames | 43/46 | 3/46 |

Neither single reading covers everything. **F21 (verb stem) is the better general reading
(43/46); R4's "ent" survives only as a restricted claim on the 3 -ment instances.**
The 06→06×2 instances ("61-ne-m-ent 06", "gouvernement 06") actively favor *polyvalence*
("…ent [verb-stem]": "…nement décide…") over single-reading "ent" ("…ent ent…" ✗).
Polyvalence is an added, uncorroborated mechanism — flagged, not assumed.

## (e) CONTEXT — the ×2 repeat parses in its surround, weakly inside

- @1175: `32 48 59 37 |77 78 94 82=m 06| 06 59 42 06 84` → "…37 gouvernement **[verb]** 59…"
  parses *iff* 37="le" (37∈B ✓ word-initial), 77="gou", 78="ver", and 06 polyvalent.
- @1346: `73 34=i 62 48 |77 78 94 82=m 06| 52 37 64=qui? 35 13` → "…48 gouvernement
  52 37 qui…" — a "qui" relative after a noun phrase is grammatical ✓.
- The surround is compatible; the internal weak links are 77="gou" (77∈C, but "gou"
  should be initial) and 78="ver" (78∈C with next-B=0.484; medial "ver" should be A).
  77/78 resolution is out of this WO's scope — flagged for the 77-lane.

## Refutation attempts (strongest counter-evidence found)

1. **06's phase kills "ent" generally**: A-block at all cuts, next-B 0.196 vs 0.894
   er-calibrated; 0/3 instance-final 06s followed by word-initial (p≈0.001).
2. **06→29(er)×5**: "ent|er" is ungrammatical — 5 instances where 06≠"ent".
3. **@1741**: "34=i 94 82=m 46=que" — "i-ne-m-que" does not parse; 1 of 4 94→82
   instances lacks the 06 (25% of the bigram family unexplained).
4. **Rival 94="en"**: explains 82→94×3 beautifully as "m'en" ("52 m'en 76/74" —
   cf. "je m'en"), but is *killed* for the trigram instances ("en-m-ent" is no French
   word; all -nement words need "ne") and loses on rate (1.79× vs 1.025×).
5. **Rival 94="re"**: rate 1.067× but killed by bigram geometry (82→94 = "m-re" impossible).
6. 06="ent" rate sits 1.26× above even the generous era upper bound.

## Verdicts

- **94 = "ne": CONFIRMED.** Three legs, two independent instruments: (1) syllable rate
  1.025× (era corpus); (2) trigram 94-82-06 ×3 at 1.054× era -nement rate with the
  ground-truth 82=m anchor centered and a ×2 byte-identical repeat (cipher structure);
  (3) phase medial (A, stable) + B→A "pre|nez"-type predecessor profile. Anomalies
  (@1741, the "m'en" triple) are unexplained, not fatal.
- **06 = "ent" (general reading): REFUTED** — phase, 06→29×5, rate over-bound.
  Survives only as a **PLAUSIBLE restricted claim** on the 3 -ment instances
  (trigram rate + composition for; phase anomaly against; polyvalence uncorroborated).
- **Family 94-82-06 = "ne-m-ent": PLAUSIBLE, not CONFIRMED** — blocked by 06's phase
  anomaly and the cost of the polyvalence mechanism.
- **06 tension: no forced kill.** F21 verb-stem stands as the working *general* reading;
  R4's "ent" stays live *only* for the 3 -ment trigrams. The honest state is coexistence
  under test, not a single winner.

## Best next step

1. **Polyvalence test (direct):** examine @737 "…76 18 82 06 00…" — the only other
   "m|ent" split (18→82 ×1). If 18 proves to be a -ment stem syllable, 06="ent" gains
   its first out-of-trigram leg; if not, the trigram stays isolated.
2. **Resolve 77/78** (77-lane): the repeat's "gouvernement" parse needs 77="gou"/78="ver",
   both phase-weak (C-block). If 77/78 fall, the family's ×2 anchor falls with them.
3. **The "m'en" anomaly** (82→94×3, round 4): test whether 94 is conditioned ne/en by
   neighbor (polyvalent) or whether "52-m-ne" is an "mne"-word ("automne"/"emmené"-type).
4. **Identify "pas"** to test 94's negation-frame absence (currently void, not evidence).
