# INVENTORIST pattern re-drive — report (crowd6, 2026-10-07)

## Context
Re-drove the word-pattern matcher on the F44 crib-learned 24-unit alphabet
(round-5 inventorist delivery), replacing the standard-French syllabification
that killed the old instrument (N32). Reused the fleet's 11,870-word lexicon
and the polyvalence-expansion method under red-team restrictions R1–R8
(R1 strengthened, R3 demoted, R8 satisfied by construction — the by-ear
alphabet is orth-based). Did NOT reuse the 26 killed proposals (12 unique
words blocklisted) or the tester's §6 K≥3 numbers. All numbers on the
canonical 1,847-pair repaired stream (F32).

## Decision
**CONTROL PASSES — the alphabet is repaired.** The ground-truth control that
killed the old version now works:
- **C1** (full "première" [70,82,34,29,40], 5 GT anchors): "première" top-1
  (2 candidates: première, premières). PASS.
- **C2** (tail [82,34,29,40] = m|i|er|e, 4 GT anchors — the old zero):
  **"première" top-1** (5 candidates: première, lumières, premières,
  lumière, chaumière). PASS. The old instrument's zero is repaired.
- **C3** (specificity: contradictory GT anchor [11,34,29,40]): 0 candidates,
  "première" correctly excluded. PASS — the instrument is anchor-driven.

**Proposals (2):**
1. **"parmi" @1196–1198 [96,82,16]** — NEW. 4 checks: (a) unique T3 survivor
   (only by-ear [par,m,?] in 11,870 words); (b) era freq 174; (c) whole-word
   by-ear match [par,m,i] (top-1 tiling, score 9.0); (d) 1 GT anchor (82=m)
   + 1 PROV-STRONG (96=par, CONFIRMED 4/4). **Implication flagged:** 16 is
   unanchored; the reading entails **16="i"** (n=1, new claim — 34=i is GT,
   so this would be a second 'i' group). 16="i" needs its own battery;
   supporting datum: 82→16 ×11 (29% of 82's followers) reads m|i, and 16's
   top predecessor is 82=m. Not established.
2. **"cela" @269–270 and @357–358 [47,11]** — 3 checks: (a) era freq 47;
   (b) repeats ×2 at independent positions (47→11 is ×3 corpus-wide:
   @269/@357/@498); (c) whole-word [ce,la]. Anchors 47=ce (LEAD) + 11=la
   (GT). This is a **47="ce" corroboration**, not a new crib (the lane
   already banks 47→11 "cela").

**Leads (not proposed — <2 solid checks, fragments, or weak filters):**
"seulement" @1041 [77,82,63] / @1158 [77,82,44] (freq 136, ×2, BUT fragment
"lement", 108 T3 candidates, and two DIFFERENT third groups 63/44 both
implying "ent" — opportunistic le|m anchor drive); "donner" @1362/@1686
[62,94,79] / @1704 [62,94,88] (freq 82, ×3, BUT 0 GT anchors, fragment
"onner", 113 candidates); "acquière" @290/@684 [64,29,40] (2 GT anchors +
unique, BUT freq 1 hapax + fragment "quiere" — old Class-B shape);
"ensemble", "général", "comparer", "confédération", "nationale",
"circonstances", "établissements", "semble", "raison", "cinquième",
"acquièrent" (all fragments and/or 0–1 GT anchors and/or weak T3 filters).

**Recommended KILL (register pollution / hapax accidents):** "meeting" ×2
(@352/@819, English word, freq 2 — the "susquehanna" shape); "maryland"
(@376, US state, freq 11, 2 GT anchors but Americana); "chancelantes" ×2
(@200/@1242, freq 2; @1242 is the Ruling-4 cela+X non-evidence spot).

## Why (instrument)
- **By-ear tiler** (`byear.py`): tiles each lexicon word into 1–4-letter
  cells, scored for inventory-unit matches (20 F44 strings), single letters
  (R1), onset clusters; top-8 tilings kept (R2: the SET of cuts).
  Calibration (disclosed, on ground truth): "première"→[pre,m,i,er,e] top-1;
  "cela"→[ce,la] top-1; "lumière"→[lu,m,i,er,e] rank 3. Limitation: the
  20-string inventory cannot recover unattested multi-letter cells — the
  attested "personne" cuts (per|so|nne, pers|on|ne) are not generated
  ('per'/'pers' unknown). Honest boundary; anchor-relevant cells ('so','on',
  'ne') ARE generated, and subsequence matching aligns them.
- **Subsequence pattern index** (`build_index.py`): (n,pattern) over ALL
  contiguous cell subsequences — this implements R7's "tolerate n-mismatch"
  with an explicit mechanism, and is REQUIRED for the control (no 4-cell
  French word is "miere"; whole-word lookup on the tail is unpassable by
  construction). 846,748 subsequences, 7,297 keys.
- **Smart polyvalence expansion only** (R1/R2): each subsequence filed under
  its exact reachable cipher patterns given the by-ear islets (94:ne|en,
  52:pas|so|se, 59:se, 78:me|ver, 47/87:ce, 06:ent-restricted). 3,451 extra
  filings (vs 202×–2318× for naive). Old 06=/mɑ̃/ model dead per N17 — not
  transferred. R4 enforced in the anchor filter (polyvalent groups allow
  only their reading sets); R5: proposals touching 06/94/52/78/47 flagged.
- **Anchor tiers** updated to round-5 statuses (77="le" now PROV per F37;
  87=ce prov-strengthened; 94="ne" prov-strong; 96="par" CONFIRMED-inheriting).
  06 not an anchor (verb-stem-class, no string).
- **Sweep**: 434 anchor-bearing viterbi words (re-indexed; 15 dropped in the
  repaired 748–772 region) → 27 generator proposals → 2 survive the ≥2-check
  bar as whole-word matches.

## Enlightenment
What the alphabet changed vs round 5: round 5 DELIVERED the inventory; this
re-drive OPERATIONALIZED it. The binding change is not just the 20 strings —
it is the **unit SHAPES** (single letters legal, onset clusters atomic,
mute-e written) plus **subsequence matching**. The old instrument failed on
a single unit ('m'); the new one passes because the tiler EMITS 'm' and the
index TOLERATES the segmenter's mis-cut. The cost: fragment matches
("onner", "lement") — controlled by the whole-word/fragment distinction and
the ≥2-check bar. The 16="i" implication is the sharpest new lead: if
"parmi" holds, the lane gains a second 'i' group (34/16 allophony, parallel
to 87/47 for "ce"), and the 82→16 ×11 bigram (F5's strongest anchor-adjacent
pattern) becomes m|i cuts. That battery is round-6 work.

## Files
- `code/crowd6/inventorist/byear.py` — by-ear tiler + calibration
- `code/crowd6/inventorist/build_index.py` — subsequence pattern index with
  smart polyvalence expansion
- `code/crowd6/inventorist/byear_index.json` — the rebuilt index (29 MB)
- `code/crowd6/inventorist/matcher.py` — matcher + C1/C2/C3 controls
- `code/crowd6/inventorist/control.json` — control verdicts
- `code/crowd6/inventorist/sweep.py` + `sweep_results.json` — full sweep

## For red team
Adjudicate: (1) the "parmi" proposal (esp. the 16="i" entailment — single
observation, needs a battery); (2) the "cela" corroboration; (3) the three
recommended kills; (4) the subsequence-matching design (fragment risk).
Nothing here is promoted — all await ruling.
