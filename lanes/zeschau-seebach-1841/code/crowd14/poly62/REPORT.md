# 62-POLYVALENCE BATTERY — Round 14 (2026-10-07)

**Objective:** test whether 62 = syllable-"on" in the six "62-48" windows, which would
dissolve the Path A ("on-48") fence against 48's hypotheses.
**Scope:** `code/crowd14/poly62/`; stream rebuilt from `code/side-keyhunt/repaired_offsets.json`
(never `canonical.py`). Corpus: `code/side-period/corpus/` French files; primary-diplomatic
= nesselrode-v8 + levant-correspondence-1841-p3 (372,751 tokens); elision-split tokenizer.
v8 OCR word-split caveat noted (F77); bigram hits below hand-checked for genuineness.

## 1. Window re-derivation (repaired 1,847-pair stream, 0-based)

62→48 bigrams at **360, 425, 1315, 1349, 1464, 1569** = cited @361/@426/@1316/@1350/@1465/@1570
(1-based). Six windows confirmed; n62=35 total.

| # (1-based) | −3 −2 −1 [62] [48] +1 +2 +3 |
|---|---|
| @361 | 47(ce) 11(la) 21(me·lead) [62] [48] 76(ver) 47(ce) 78 |
| @426 | 29(er) 47(ce) 14(?) [62] [48] 76(ver) 42(?) 63(?) |
| @1316 | 00(pour) 36(?) 74(te·lead) [62] [48] 98(?) 15(?) 24(en) |
| @1350 | 66(?) 73(?) 34(i·crib) [62] [48] 77(le) 78 94(ne) |
| @1465 | 17(fois·weak) 01(?) 21(me·lead) [62] [48] 21(me·lead) 02(?) 62 |
| @1570 | 29(er) 24(en) 74(te·lead) [62] [48] 56(plus·med) 32(?) 28(?) |

## 2. Per-window readings

**Corpus pre-context check (pronoun-"on"):** adjacent-word bigrams, genuineness hand-checked —
"me on": 21 raw hits ALL English ("and me on the same subject", levant file) or OCR garbage;
"te on": 1 (OCR "^te on ne peut"); "en on": 1 (OCR garbage); "ce on": 1 (OCR "ce on dirait"
for "ce qu'on"/"comme on"). **Genuine "me on" / "te on" / "en on" / "ce on" = 0.**
Controls behave: "qu' on"=4051, "si on"=303, "comme on"=362, "et on"=337 (ALL corpus).

**Corpus post-context (Path A frame):** "on de"=2 (both non-genuine per F83 D2a — not re-litigated);
"on a"=76 (3.48%, grammatical); "on ne"=100; "on en"=17; "on est"=21. Path A's A1 0/10
(F83) is window-level (with successors), not bigram-level — consistent.

| window | pronoun-"on" | syllable-"on" | verdict |
|---|---|---|---|
| @361 | pre "me on"=0 genuine → **pre-adverse** (cond. on 21="me" lead); post fenced (Path A) | "me"+"on" not a word; no composition | CONTESTED — neither reading clean |
| @426 | pre=14 unknown → undetermined; post fenced | 14+"on" unverifiable | OPEN — both undetermined |
| @1316 | pre "te on"=0 genuine → **pre-adverse** (cond. on 74="te" lead); post fenced | "te"+"on" not a word; "pan-thé-on" via 36 unverified | CONTESTED |
| @1350 | pre=34 ("i" crib): "i on" ungrammatical as words; as word-final syllable needs 73-completion | **best near-miss:** 73-34-62 = "t"+"i"+"on" = "-tion" IF 73="t" (unverified); then 66+"tion" = question/mention/nation-… (66 unverified) | LEAN-SYLLABLE (weak; 2 unverified values) |
| @1465 | pre "me on"=0 genuine → **pre-adverse** (cond. on 21="me"); post fenced | "me"+"on" not a word | CONTESTED |
| @1570 | pre "te on"=0 genuine → **pre-adverse** (cond. on 74="te"); post fenced | "te"+"on"/"er-te-on" not words | CONTESTED |

Note: the pre-context adverse also hits 4 REST windows (@101/@1066/@1540 pre=21; @803 pre=74) —
it is a general 21/74-value tension, not specific to the six (supports uniformity; see §4).

## 3. Dissolution verdict: NOT DISSOLVED — HOLD

The conditional is logically valid: Path A's fence ("on de"=0 genuine ×6; A1 0/10, F83) rests on
the premise "62 = pronoun 'on'" in these windows; a syllable reading is a different claim and the
fence would not apply. **But the premise is not established at the window level:** no window yields
an era-attested word with 62 as syllable-"on" under standing values (@1350's "-tion" needs two
unverified values). The adverse therefore STANDS. F83's flag ("tension points at the premises,
62='on' ear-only is the load-bearing weak link") remains the live pointer.

## 4. Legs

- **L1 — rate (NEW, strong, independent):** n62=35. Primary-diplomatic expectation for monovalent
  pronoun-"on": 2184/372751×1847 ≈ **10.8** → observed is **3.2× over** (no single extra word closes
  the 24.2 gap: "ont"→+1.8, "mon"→+1.8). "on"-nucleus syllable-cell model (syllabify.py,
  F30 finer-cut caveat): 14183/617002×1847 ≈ **42.5** expected vs 35 observed (0.82× — in range).
  → 62 behaves like an "on"-syllable cell, not a monovalent pronoun. Internal-"on" share 0.846 →
  ~29.6 of 35 expected word-internal; the six 62→48 windows are candidates for that share.
  CUT-DEPENDENCE (honest): the 0.82× assumes groups≈standard syllables; the encipherer cuts finer
  (pre|m|i|er, F30), so 1847 groups may represent only ~900–1200 standard syllables → syllable-model
  expectation drops to ~21–28 (35 = 1.3–1.7× over: needs mild register pleading or "on"-nuclei kept
  whole while other syllables split fine). The pronoun-only model degrades FASTER under finer cuts
  (1847 groups ≈ ~1000 words → expected ≈ 5.9, observed 5.9× over). Qualitative leg — 62 covers far
  more than the pronoun — is robust either way; the quantitative fit is cut-dependent.
- **L2 — pre-context anti-pronoun (conditional):** "me on"/"te on"=0 genuine → 4/6 windows'
  pronoun reading ungrammatical under lead values 21="me"/74="te". Conditional on non-standing
  leads; also present in REST → general tension, not six-specific.
- **Uniformity (1690 law — necessary, insufficient):** pre-62 distribution SIX {21×2,74×2,14,34}
  vs REST: Fisher p=0.195 (21), p=0.070 (74); collapsed χ²(4df)=9.12, p≈0.058 — does NOT reject
  homogeneity at bar (n=6, low power). Necessary condition SATISFIED, not violated. 67-model
  "zero BOTH" cleanliness not met (no window cleanly admits either reading) — the six are
  over-constrained under current values, a signal the local value assignments (21/74/48/62)
  contain an error, not just 62's reading.
- **Constraint check:** 62→94 "on ne" ×9/29 all in REST — the STRONG LEAD legs survive the
  conditioning untouched. 62="il" not re-litigated. No global regrade attempted.

## 5. Status: HOLD (not CONFIRMED-conditional, not KILLED)

**Pre-registered bar:**
- CONFIRM-conditional (≥2 legs): L1 banked + one of — (i) compositional hit (era-attested word
  spanning a 62-window with 62 as "on"-syllable under standing values — NOT FOUND); (ii) independent
  instrument (e.g., H_stem battery independently composing 48 after "on" in ≥2 of the six —
  NOT RUN); (iii) distributional separation at bar (n=6 underpowered). → NOT MET.
- KILL: (i) a window forcing pronoun-"on" (48 promotes to pronoun-requiring value, or pre-62
  promotes to a licensor — NOT MET); (ii) rate leg overturned (despatch 3×+ "on"-heavy — no
  evidence); (iii) monovalent explanation for n62=35 (none). → NOT MET.

## 6. What this means for 48's hypotheses

1. The six "on de"=0 data points REMAIN IN FORCE. F110's kill of unconditioned 48="de" used 11
   windows; the six are a subset — even full dissolution would not resurrect it ("de pour/en/est/par"
   ×5 stand independently). No 48 hypothesis changes status on this battery alone.
2. The live follow-up is now precise: **test H_stem (48 = vowel-initial verb-stem syllable) specifically
   in the six windows** — i.e., "[X]on" + 48-stem compositions. If that battery independently composes
   48 after "on" in ≥2 of the six, it retro-supplies the missing second leg and triggers the
   dissolution. (@1570's "on a plus…" via 48="a"/56="plus"·MEDIUM is a thread, not a leg.)
3. New adverse exported: the "me on"/"te on"=0 finding constrains 21="me"/74="te" leads — the
   21/74 batteries should book @361/@1316/@1465/@1570 (plus REST @101/@1066/@1540/@803) as adverses.
4. 62="on" STRONG LEAD is untouched; what L1 licenses is the *framing* the WO already ordered:
   62 as "on"-syllable cell with pronoun-"on" as the conditioned standalone use — to be confirmed
   or killed by the follow-ups above, not by this battery.

## Evidence
Scripts: `build_stream.py` (repaired parse, asserts 1847 pairs), `windows.py`, `fulltable.py`,
`profile62.py`, `uniformity.py`, `corpus62.py`, `genuine.py`, `syrate.py`, `syrate2.py`, `onX.py`.
Corpus pool: `code/side-period/corpus/` (French files; primary-diplomatic nesselrode-v8 +
levant-correspondence-1841-p3). All counts re-derived this battery.
