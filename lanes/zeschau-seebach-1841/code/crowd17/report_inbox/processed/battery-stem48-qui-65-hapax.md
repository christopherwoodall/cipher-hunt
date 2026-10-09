# Battery report: stem48-qui-65-hapax — 2026-10-09

Worker: fe79e451-4643-4054-a160-cae41a181aa3. Stream: repaired 1,847-pair parse
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per
code/side-keyhunt/repair_parse.py). Lock: locks/stem48-qui-65-hapax.lock created
on start, deleted on completion. canonical.py never used. R5005, sealed gates,
red-team queue untouched.

## Bar (verbatim, pre-registered BEFORE testing)

"Deliver a licensed parse of @1585-1588 under standing values,"
"or exhaust all re-reads with stated cause. Granted 64='qui' and 70='pre' stay fixed."

## Numbered clauses (restated before testing; bar unmodified)

1. PARSE: @1585–1588 ("36 70 64 65", 0-based) admits a licensed 1841-French
   parse with all four tokens' roles named under standing values
   (64='qui', 70='pre' fixed).
2. EXHAUST: failing (1), every rival re-read is exhausted with stated cause:
   (a) "qui" roles — relative / interrogative / indefinite (+ exclamative,
   "ce qui"-with-elided-"ce"); (b) rival left-attachments for 65;
   (c) segmentation rivals for the 4-gram.

## Method

Re-derived the window byte-by-byte from the repaired stream (never
canonical.py). 0-based @1585–1588 = `36 70 64 65` (row a8_02), preceded by
`44 00` (@1583–1584) and followed by `48 29 47 08` (@1589–1592).
Standing values only: 36 = NOUN-CLASS (class-36-profile PROMOTE, value open),
70 = 'pre' (pencil), 64 = 'qui' (granted), 65 = NOUN-CLASS (battery-prof-65),
00 = 'pour' (A9 leg-1 class-level). Read the parent (stem48-65-value, NULL)
and sibling (stem48-65-governor, PROMOTE: orphan localized to "qui [65]"
@1587–1588, "unclosable qui" as primary defect) first; premises adopted, not
re-litigated. Ran fresh distributional censuses for 70 and the 4-gram's
bigrams (below) — the stranded-"pre" finding is new to this battery.

## Distributional evidence (re-derived, byte-exact)

- n(36)=9, n(70)=15, n(64)=47, n(65)=25 (match lane censuses).
- **"36 70" is a stream hapax** (@1585). 36's other followers: 74 ×2,
  62/29/20/77/67/69 ×1.
- **"70 64" is a stream hapax** (@1586). 70's other followers: 12 ×3
  ("pren-": 70-12-94 = "prenne" is the established "prendre"-family surface),
  82 ×2 ("prem-": "11 70 82 34" = "la première" at @755 and @1035),
  39 ×2, 98/17/91/88/87/37/52 ×1. Every non-hapax follower is open/stem
  material — **no granted word follows 70 anywhere else**.
- 70's left neighbors are boundary-shaped in the anchored windows
  ("la"+"première" ×2, "de"-lead+"pre…" @615, "que"+"prenne" @1547,
  "ne"-lead+"pre…" @1331): 70 is word-initial "pre-" wherever its position
  is determinable. **Zero windows show 70 word-final or medial.**
- "64 65" hapax (@1587); 64's other followers (77/96/29/59/37/98/32/31/79/26/…)
  never include 65.
- 36's left at @1585: "44 00" = "[44] pour" — "pour [36-noun]" matches the
  licensed PP frame (class-36-profile NOUN LEG @740: "pour [36] [20]",
  "pour mémoire"-type diplomatic register).

## Findings

### C1 (licensed parse of the 4-gram): FAIL

No full parse exists. The one clean sub-parse is **"pour [36-noun]"**
(@1584–1585, PP, licensed per class-36-profile). Downstream of it, 70='pre'
is stranded: as a word-initial syllable (15/15 profile) its continuation slot
is occupied by granted word 64='qui', and leftward composition "[36]pre"
would put "pre" word-final — a position with zero support in 70's profile.
"qui [65]" is unclosable (adopted sibling premise). The 4-gram is a syntax
orphan; the breakage refines to the **70|64 boundary** (stranded "pre"),
with "pour [36]" closing cleanly upstream.

This refines — does not contradict — stem48-65-governor's "[36]pre" gloss:
that battery used "[36]pre" as notation, never as a promoted segmentation.
On 70's positional profile the composition is unlicensed; recorded here as a
fenced residual (S1), not a standing value.

### C2 (rival re-reads exhausted)

**"qui" roles @1587:**
- R1 relative (subject relative, antecedent = 36-headed NP): "qui" as subject
  forbids an intervening full NP — "qui [65-noun] [infinitive]" is a double
  subject plus a non-finite predicate. Antecedent variants all die the same
  death: "[36]pre"-as-word (composition fenced, S1), 70's word (stranded
  syllable, not a word), wider "pour [36]" NP (same double-subject kill),
  verb-final close at finite 80 (@1596): French relatives are SVO, never
  verb-final. **KILL at kill grade.**
- R2 interrogative: French "qui" interrogatives require "qui"+finite verb,
  "qui est-ce qui/que", or "à/de"+"qui". "qui [65] [STEM]er…" has no finite
  verb adjacent (nearest finite-capable token 80 is +9 and not in
  interrogative position); "qui [NP] [infinitive]" is not a French
  interrogative frame. **KILL at kill grade** (converges with the parent's
  candidate-3 kill; not re-litigated).
- R3 indefinite ("whoever"-role; the "quiconque" *value* rival is excluded
  by the claim and stays in noun-65-value): indefinite "qui" requires a
  finite verb ("qui dort dîne"); only an infinitive follows. **KILL at kill
  grade.**
- R4 "ce qui" with elided "ce": left neighbor is 70='pre', which cannot
  supply "ce". **KILL.**
- R5 exclamative "qui": no such French construction exists. **KILL.**

**Rival left-attachments for 65 @1588:**
- L1 subject of the infinitive: no perception/causation governor; "pour"
  governs 36, not 65 (adopted parent kill, candidates 1–2).
- L2 fronted direct object of the infinitive: French non-clitic objects do
  not front (adopted parent kill, candidate 6).
- L3 vocative: vocative after relative "qui" is unlicensed; orphans the
  infinitive leg (adopted parent kill, candidate 7).
- L4 appositive to 36/"[36]pre": apposition cannot span the intervening
  "qui". **KILL.**
- L5 65 as antecedent with "qui" postposed: relative pronouns follow their
  antecedents; impossible word order. **KILL.**
- L6 subject of finite 80 (@1596): verb-final clause + "qui" double-subject.
  **KILL.**
- L7 "64 65" one word: contradicts granted 64='qui' (§7 sole polyvalence);
  barred — red-team venue only, not adopted.
- L8 65 governed by "pre" (70): no "pre"+NP construction exists in French.
  **KILL.**

**Segmentation rivals:**
- S1 "36 70" = "[36]pre" one word: "36 70" hapax; 70's 15-window profile
  gives zero support for word-final "pre"; 36's value is open so no word is
  nameable without invention. **FENCED as residual** (re-opens iff 36's value
  names a "[val]pre" word — follow-up 1).
- S2 "70 64" one word: non-word ("prequi*") + contradicts granted 64='qui'.
  **KILL.**
- S3 "64 65" one word: contradicts the grant; barred per claim.
- S4 70 as standalone word "pre": no French word. **KILL.**
- S5 "pour [36]" closes, 70 stranded: the surviving partial parse —
  **licensed sub-parse, adopted** (see C1).

No standing or red-team verdict is contradicted; §7 intact. Adverses: none
listed on the target.

### Caveats
- Canonical-stream verdict: row a8_02's upstream offset is one of the 68
  unvalidated (protocol §7). Under a rival a8_02 phase the @1586 successor
  could differ — the fence is phase-conditional (follow-up 3).
- "pour [36-noun]" rests on 00='pour' (A9 leg-1 class-level) and 36's
  battery-promoted noun class (value open).

## Verdict: NULL (fence executed)

HEADLINE: every rival "qui"-role (relative / interrogative / indefinite /
exclamative / "ce qui") dies at kill grade, every rival 65-attachment dies or
is grant-barred, and the 4-gram has no licensed full parse — but the orphan
is now sharper than the sibling left it: "pour [36-noun]" closes cleanly, so
the breakage localizes to the stranded "pre" (70) at the 70|64 boundary.
70 is word-initial in all 15 windows of its profile and its only
granted-word follower in the stream is "qui" at @1587; "[36]pre" composition
is unlicensed on that profile. The "qui [65]" unclosability (sibling
premise) stands as the secondary defect.

## Follow-ups proposed (all verified absent from battery-queue.json)

1. **val-36-noun** (P3): name 36's noun value across its 9 windows
   (@388/@421/@740/@1174/@1215/@1313/@1449/@1585/@1834). Bar: re-opens the
   S1 "[36]pre" residual iff "[36-val]pre" is a licensed French word; kills
   the stranded-"pre" fence iff 36's value cannot compose with "pre".
2. **pre70-positional-profile** (P3): full positional census of 70's 15
   windows with left-boundary evidence per window. Bar: revises the
   "70 always word-initial" premise iff any window shows medial/final "pre"
   (cf. "après"/"reprendre"-type medial); hardens the stranded-"pre" fence
   iff all 15 confirm initial position.
3. **a802-phase-rival-1586** (P4): re-test @1585–1588 under admissible rival
   row-phases for a8_02 (canonicality caveat). Bar: the fence stands iff no
   rival phase gives 70 a licensed host or "qui" a finite verb; else the
   orphan is declared phase-conditional with the licensing phase named.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-stem48-qui-65-hapax.md (this file)
- Queue: `stem48-qui-65-hapax` → status `verdict`, result `null`, date
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; JSON re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion.
