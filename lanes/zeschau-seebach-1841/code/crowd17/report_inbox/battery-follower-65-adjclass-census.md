# Battery report: follower-65-adjclass-census

**Target:** `follower-65-adjclass-census` (priority 3)
**Date:** 2026-10-09
**Worker:** a4988920-1c4d-45a2-acf1-1bf947f205e0
**Verdict:** NULL (follower route fenced per the bar's else-branch)

## Bar (verbatim from queue)

"class each of {23, 88, 16, 68} with >=2 windows at battery grade; if any is a gendered adjective, test agreement with 65 at the contact window (@135/@1608/@1781, @512, @293, @1383); if none is gendered, fence the follower route with stated cause."

## Bar restated as numbered clauses (frozen before testing)

- (C1) Each of {23, 88, 16, 68} is classed with ≥2 windows at battery grade.
- (C2a) If any is a gendered adjective, agreement with 65 is tested at the contact window.
- (C2b) If none is gendered, the follower route is fenced with stated cause.

Lane @ = 0-based stream index (matching the bar); 1-based equivalents noted. The bar's contacts are 0-based: 23 → 135/1608/1781, 88 → 512, 16 → 293, 68 → 1383.

## Method

Read `BATTERY-PROTOCOL.md` first; created `locks/follower-65-adjclass-census.lock` on start (deleted on completion). Re-derived the repaired 1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` parsed per `repair_parse.py` (asserts: 1,847 pairs, 96 types — held). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Prior battery verdicts used as premises (cited, not re-litigated per adverses): `class-23-qui-adjective` (NULL), `prof-88` (PROMOTE), `w2-16-class` (NULL; 16=infinitive standing promote), `fem32e-subject-gender` (PROMOTE). The adverses' fenced items (34=i letter; '65 14' @812 unlicensed; verb-63-frames, reseg-13-armA, stem48-65-value, class-71-adjective) are not re-litigated.

## Findings

### Stream facts (byte-exact)

n(65) = 25. The four target followers:
- 65→23: 0b135 (a1_04), 0b1608 (a8_02), 0b1781 (a8_09) — 3×
- 65→88: 0b512 (a3_00) — 1×
- 65→16: 0b293 (a2_03) — 1×
- 65→68: 0b1383 (a7_06) — 1×

Gender-mark composition check: `X 48` (48='e', R17 letter-tier grant, the cipher's feminine mark) occurs **0×** for every X in {23, 88, 16, 68}. No gendered value is named for any of the four.

### 23 (n=8) — verb; 0/8 adjective windows

- 0b182 (a1_05): `87 64 [23] 37` — "ce qui [23] [37]": the post-qui slot forces a finite verb (qui-2326-prefix/encequi-triple PROMOTEs adopted as premise). Kill-grade against any adjective reading here.
- 0b679, 0b1056, 0b1552: `45 [23]` ×3 — "ce [23]" with granted 45='ce', consistent with finite verb, ungrammatical as adjective ("ce" + bare adjective with no noun).
- Contact windows: 0b135 `21 65 [23] 91`, 0b1608 `92 65 [23] 08`, 0b1781 `74 65 [23] 98` (the W8 orphan from class-23-qui-adjective; verb arm still the only live class there).
- C1 for 23: PASS (verb, ≥2 windows).

### 88 (n=23) — verb stem / verb-governor (prof-88 PROMOTE); 0/23 adjective windows

Legs verified byte-exact (0-based, matching prof-88's numbering):
- 0b1049: `[88] 29` = "[88]er" infinitive (1b@1050).
- 0b1706: `94 [88] 26` = "ne [88-verb]" (1b@1707).
- 0b402: `45 [88] 53` = "ce [88-verb]" (1b@403).
- 0b646/0b1541: `[88] 77` = "[88] le [78]" transitive-governor trigram (1b@647/@1542).
- Contact window 0b512 (1b@513): `98 65 [88] 56` — "vient [65-N] [88-V]": 88 in the verb slot.
- C1 for 88: PASS (verb, ≥2 windows).

### 16 (n=28) — infinitive (standing battery promote, gate-satisfiability-16-85); 0/28 adjective windows

- `82 [16]` ×11 — "m'[16-inf]" clitic + infinitive.
- `[16] 00` ×4 — "16 pour [inf]" purpose chain (0b187, 0b659, 0b844, 0b1246).
- Contact window 0b293 (1b@294): `40 65 [16] 01` — 16 directly after 65-noun; infinitive, not adjective (no "pour"/"à" governor, but the class is the infinitive per the standing promote).
- C1 for 16: PASS (infinitive, ≥2 windows).

### 68 (n=8) — class OPEN (split; red-team venue)

- Adjective arms: 0b1383 `65 [68] 52` (post-nominal after 65-noun — the contact window); 0b1442 `52 [68] 59` (post-nominal before provisional 59='est'); 0b1788 `21 [68] 47` (nominal phrase).
- Noun arms: 0b1719 `47 [68] 06` ("ce [68]" — determiner + noun slot; an adjective here would need a following noun, and 06='ent' standalone is not one); 0b1286 `55 [68] 00` (verb 55's object); 0b884 `79 [68] 37` ("tout [68]" + A1 predicative frame).
- A single value cannot be both noun and adjective under §7 (67 is the sole true polyvalence); the split is red-team venue, not decidable at battery level.
- Crucially for this bar: **68 carries no gender mark anywhere** — 68→48 never occurs, and no gendered value is named. Even on the adjective arm, 68 is not a *gendered* adjective at battery grade.
- C1 for 68: FAIL (class open — reported honestly, not forced).

### C2a — no gendered adjective exists

None of {23, 88, 16, 68} is a gendered adjective at battery grade:
- 23/88/16 are verb-shaped (finite verb / verb stem-governor / infinitive); gender morphology is inapplicable to all three, with 0 adjective windows across 8/23/28 windows respectively.
- 68's adjective arm is live but unmarked: no 68→48 composition, no gendered value. An unmarked adjective cannot supply a gender-agreement window.
- Independently, 65's own gender is unmarked (fem32e-subject-gender PROMOTE: 65 @1208 UNMARKED), so no agreement target exists to test against even if a gendered adjective were found.

C2a does not fire. C2b fires.

## Per-clause results

- (C1): PARTIAL — 23/88/16 classed with ≥2 windows each at battery grade; 68's class is honestly open (noun/adjective split, red-team venue).
- (C2a): does not fire — no gendered adjective among the four.
- (C2b): EXECUTED — the follower route is fenced (see below).

## Verdict rationale: NULL, follower route fenced

**Stated cause for the fence.** The parent route — using one of 65's adjective-position followers (23 ×3, 88, 16, 68) to supply a second gender-agreement window for 65 — is fenced because:

1. Three of the four followers are verb-shaped at battery grade (23 finite verb, 88 verb stem/governor, 16 infinitive) with zero adjective windows; a gendered-adjective reading is excluded for each.
2. The fourth (68) is class-open with a live adjective arm, but carries no gender mark (no 68→48 composition anywhere; no gendered value named) — an unmarked adjective cannot agree.
3. 65's own gender is unmarked (fem32e-subject-gender), so the agreement test has no target.
4. The adverses' fenced followers (34=i letter; '65 14' @812 unlicensed) remain fenced.

No standing or red-team verdict contradicted or downgraded; §7 intact. Adverses answered (none re-litigated). Canonical-stream caveat stands (unvalidated upstream offsets).

## Follow-ups (for supervisor queuing; all verified absent from battery-queue.json)

1. `val-68-noun-sweep` (P3) — census 68's 8 windows for a noun value; if 68 resolves nominal, the adjective arm closes and this fence hardens to a kill.
2. `adj-68-postnominal` (P3) — test 68 as post-nominal adjective at 0b1383/0b1442/0b1788 with a stated adjective value; a gendered naming (feminine -e or masculine form) re-opens the agreement test at the contact window.
3. `gender-65-independent` (P4) — independent gender probe for 65 (other followers, predicative frames) so a future gendered adjective has an agreement target.

## Bookkeeping

- Queue: `follower-65-adjclass-census` → status `verdict`, result `null`, date 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; 958 targets intact; no downgrade).
- Lock `locks/follower-65-adjclass-census.lock` created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched.
