# Battery report: frame-76-94-trigram — verdict: NULL (fence)

Date: 2026-10-09. Worker: agent 390a7735-fea4-446a-9f7f-8c9c99dcaf30.

## Bar (queue verbatim)

"census 74 (n=34) vs 76 to test whether 'm ne [X]' is a real frame with unknown head class"

Numbered clauses (frozen before testing):
- (C1) Census all 74 and 76 windows on the repaired stream; record full left/right contact profiles.
- (C2) Enumerate every "m ne [X]" (= "82 94 [X]", X in {74, 76}) window with byte offsets.
- (C3) Resolve iff the 74-vs-76 contact profiles decide whether "m ne [X]" is a real frame; fence with stated cause if not.

Claim under test: "m ne [X]" is a real frame whose head X has an unknown class.

## Method

- Read `code/crowd17/next-token/BATTERY-PROTOCOL.md` first; created `locks/frame-76-94-trigram.lock` on start.
- Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parses like `repair_parse.py`): asserts held (1,847 pairs, 96 types). `canonical.py` never used.
- R5005, sealed gate instances, and the red-team adjudication queue untouched.
- Standing values used as granted per §7: 82='m' (banked), 94='ne' (STRONG LEAD, pending ratification), 47='ce' (A4), 64='qui', 96='par'.

## Findings (all byte-verified; @-offsets 1-based lane convention)

### C1 — contact profiles

**74 (n=34):** left: 74 x6, 49 x5, 94 x3, 39 x2, 44 x2, 36 x2, rest singletons. Right: 74 x6, 45 x3, 46 x3, 62 x3, 67 x2, 77 x2, 65 x2, 47 x2, rest singletons.

**76 (n=21):** left: 77 x3, 67 x2, 48 x2, 94 x2, 16 x2, rest singletons. Right: 47 x4, 42 x3, 49 x3, 45 x2, 87 x2, 01 x2, rest singletons.

Shared contacts: 94 precedes both (74: x3 @350/@786/@1103; 76: x2 @652/@1577); both followed by 47, 45, 48.
Distinctive: 74 has the 74-74 self-bigram x6 (17.6% of its tokens; 76 never self-bigrams); 74's right includes 46('que') x3, 62 x3, 77 x2, 65 x2 — 76 has none of these; 76's right is dominated by 'ce'-contacts 47 x4 / 87 x2 plus 42 x3 / 49 x3 — 74 lacks 87 entirely and has 42/49 only as singletons.

### C2 — the "m ne [X]" token set

Exactly three "82 94 [X]" windows, with a byte-identical left trigram "52 82 94" in all three:
- @651 (row a4_02): `... 77 78 | 52 82 94 76 49 | 24 26 ...`
- @1102 (row a6_06): `... 67 86 | 52 82 94 74 47 | 78 65 ...`
- @1576 (row a8_01): `... 32 28 | 52 82 94 76 47 | 98 24`

"82 94" occurs exactly 3x stream-wide (these windows). "52 82" occurs 5x: followers 94 x3 (the frame) and 16 x2 (@1386: `52 82 16 06 29`; @1436: `52 82 16 24 85`).

### C3 — does the profile comparison decide the frame question?

No. The frame claim is not decidable at battery grade, for three independent reasons:

1. **Frozen, not productive.** A "real frame" requires a productive head slot. The token set is n=3 with zero left-context variation (identical "52 82 94" trigram) and X in {74, 76} only, with followers 49 x1 / 47 x2. This is formula-grade, not frame-grade. Per §4, the absence of productivity is not a refutation — but it is also not a frame.
2. **The particle reading is ungrammatical under standing values.** 82='m' is banked and 94='ne' is the STRONG LEAD; "m ne" ("me ne") is not a French construction. The only rescues are word-internal composition ("[52]mne..."; 52's class/value is open — untestable at battery level) or a non-negator 94 at these windows (a §7 polyvalence question = red-team venue). The parent battery `ne-94-right-context` (PROMOTE) deliberately left "m ne 76" x2 as unfenced residuals; killing the frame on the grammatical leg would overreach its fence. No contradiction with it is declared.
3. **Profiles deny a unified homophone head, but cannot decide the head class.** 74 and 76 do not support a single homophone head class at battery grade (the 74-74 x6 bigram vs none; disjoint 'ce'/verb contact sets). But "unknown head class" does not require homophony, and the shared contacts (94-left, 47/45/48-right) are too thin to decide either head's class. The comparison therefore decides neither "real frame" nor "not a real frame".

**Verdict: NULL — fence executed.** @651/@1102/@1576 stay fenced as formula residues ("52 82 94" + head X in {74,76}, follower 47 shared once); the head class stays open; the "m ne" particle reading is ungrammatical under standing values but adjudicating 94 at these windows is red-team/parent-battery venue.

No standing or red-team verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands (68 of 70 upstream row offsets unvalidated).

## Follow-ups proposed (all verified absent from battery-queue.json)

1. `mne-52-16-branch` (P3) — the "52 82 16" x2 windows (@1386, @1436) share the "52 82" head with the frame but take infinitive-16; test whether "52 82" is a compositional unit ("[52] me...") licensing both branches. If "52 82 16" parses cleanly, 94 becomes the sole defect and the fence isolates to 94.
2. `seg-528294-word` (P3) — test "52 82 94" as word-internal composition ("[52]mne..."): enumerate French "mne"-medial words compatible with 52's other windows; kill the word-unit iff none fits.
3. `homophone-74-76` (P4) — full 74-vs-76 homophony test under the lane's distributional standard (1690 frequency uniformity necessary but insufficient): kill the homophone hypothesis iff the contact profiles reject at the stated standard.
