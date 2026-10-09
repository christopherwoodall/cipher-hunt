# Battery report: frameA-50-value — name 50's value to unlock the "ent…" new-word reading at frame A (NULL — fenced)

**Target:** `frameA-50-value` (P3)
**Worker:** 7390c3bc-b0dd-4cfd-a92a-b64f8f2461a7
**Date:** 2026-10-09
**Parent:** battery-seg-94-82-06-f3 (NULL, 2026-10-09) — follow-up #2

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"unlock the new-word 'ent...' reading at frame A via a licensed French word parsing the window"

Numbered clauses (fixed before data examination):

- **C1:** 50's value is named with byte-exact evidence, consistent across its full window profile (n(50)=11).
- **C2:** "ent"+50 is a licensed French word in 1841 diplomatic French.
- **C3:** The frame-A window (@578–586) parses grammatically with "ent"+50 as a new word.
- **C4 (adverses):** frame C is not re-litigated (blocked by f1's battery-confirmed 59='est' and open 42); the canonical-offset caveat on the doublings is stated.

Verdict rule: **promote** iff C1–C4 pass. **kill** iff a window forces the claim false at kill grade. **null** otherwise, with 1–3 follow-ups.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/frameA-50-value.lock` on start (deleted on completion; no prior/stale lock). Re-derived the repaired 1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (byte-exact tokenizer per `repair_parse.py`; asserts hold: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. Parent f3 and its findings adopted as premises (not re-litigated): the "06-06" doubling occurs exactly 2× (@580 frame A, @1184 frame C); the "ent ent" two-word reading is kill-grade dead; frame C is blocked.

Standing values used as premises: pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9), 84=on (A15), 47=ce (A4); promoted 06=ent (letters tier), 94=ne, 30=pas, 12=n; provisional 59=est, 77=le. Standing kill adopted: 50="ver" dead (dict-45-host-inventory: "50-40" = "vere" non-word at @942).

## Window-level evidence (0-based pair indices)

**Frame A locus** (row a3_02, mid-row): `@578=94 @579=82 @580=06 @581=06 @582=50 @583=10 @584=19 @585=18 @586=14 @587=00 @588=97`, i.e. `ne m ent ent [50] [10] [19] [18] [14] pour [97]`. The full row: `94 59 30 67 11 43 24 80 97 13 76 45 94 52 87 78 45 13 55 61 | 94 82 06 06 50 10 19 18 14 00 97 41` ("n'est pas et…" opens the row).

The new-word reading under test: the second 06 (@581, 'ent') + 50 (@582) compose one new word "ent"+50. The first 06 (@580) then belongs to a preceding word ending in "ent".

**50's full profile** (n=11): @209 (`44 50 88`), @331 (`92 50 45`), @380 (`11 50 82 16`: "pour la [50] m'[16]"), @442 (`80 50 78`), @582 (locus), @662 (`86 50 80`), @696 (`02 50 45`), @942 (`07 50 40`: "[07] [50]e"), @1264 (`11 50 46`: "la [50] que"), @1565 (`71 50 29`: "[71] [50]er"), @1813 (`93 50 42`).

## C1/C2: exhaustive "ent"+X candidate test — FAIL

Enumerated every French word of the shape "ent"+X with X one syllable (X = 50's candidate value), then tested each X against 50's most constraining windows (@380 "la X m'[16]", @1264 "la X que", @1565 "[71] X er", @942 "[07] X e"):

| X | "ent"+X | French? | @380/@1264 "la X" | @1565 "[71] X er" | @942 "[07] X e" |
|---|---|---|---|---|---|
| tre | entre | yes | "latre" non-word — DEAD | "treer" non-word — DEAD | — |
| trée | entrée | yes | "latrée" non-word — DEAD | — | — |
| trer | entrer | yes | "latrer" non-word — DEAD | — | — |
| tier | entier | yes | "latier" non-word — DEAD | — | — |
| tente | entente | yes ("enttente" NO) | "la tente" OK | "[71] tenter" OK | "tentee" non-word — DEAD |
| tend | entend | yes ("enttend" NO) | "latend" non-word — DEAD | — | — |
| tonne | entonne | yes ("enttonne" NO) | "la tonne" OK | "[71] tonner" OK | "tonnee" non-word — DEAD |
| tame | entame | yes | "latame" non-word — DEAD | — | — |
| duire | enduire | yes | "laduire" non-word — DEAD | — | — |
| fler | enfler | yes | "lafler" non-word — DEAD | — | — |
| fouir | enfouir | yes | "lafouir" non-word — DEAD | — | — |
| tendre | entendre | yes | "la tendre" (adj, weak) | "tendreer" non-word — DEAD | — |
| tendu | entendu | yes | "la tendu" agreement clash — DEAD | — | — |

Key result: the X values that make "ent"+X French ('tre', 'tier', 'tendre', …) are incompatible with 50's "la"+X windows; the X values compatible with "la"+X ('tente', 'tonne') give non-French "enttente"/"enttonne" at the locus (and die at @942 on "tentee"/"tonnee"). **The intersection is empty.** No single 50 value (cf. §7: 67 is the sole polyvalence) satisfies both the locus and the profile.

Alternative boundary assumptions at @380/@1264 were also tested (X standalone, X word-initial, "la"+"tre"+"m" = "la trempe" with 16='pe'): X='tre' survives @380 as "pour la trempe" only by valuing open 16='pe', but dies at @1264 ("la tre que" unparseable under every boundary). No rescue.

**C1: FAIL.** 50's value cannot be named at battery grade; no candidate survives the profile.
**C2: FAIL.** No licensed French "ent"+50 exists with a profile-consistent 50.

## C3: parse — MOOT (C1/C2 fail)

Additionally: seven neighbors at the locus are value-open (61, 55, 13, 45 left; 10, 19, 18, 14, 97 right), so no full grammatical parse of the window is statable at battery grade regardless of 50's value. The "ent…" word would also need its left neighbor (@580's "ent") to complete a preceding word and its right neighbors (10, 19, 18, 14) to supply its syntactic frame — all open.

## C4: adverses — PASS

- Frame C (@1184: `94 82 06 06 59 42 …`): not re-litigated; f3's block stands (f1 battery-confirmed 59='est' at @1186; 42 open).
- Canonicality caveat: both doublings sit on unvalidated upstream rows (a3_02, a6_10); the verdict holds on the canonical stream per protocol, offset adoption is a red-team act.
- Standing kill respected: 50="ver" stays dead.

## Rival noted (out of scope, not pursued)

The bytes `94 82 06 06` also admit the one-word rival "ne mentent" (3pl present of *mentir*, "they do not lie"), which would make 50 a standalone one-syllable word rather than part of an "ent…" word. Testing it needs a 3pl subject in `…45 13 55 61` — this is the queued `w580-subject-61` / `second-06-nonent` venue, not this bar. Flagged for the supervisor, not duplicated here.

## Verdict: NULL (fence)

C1 and C2 fail; C3 moot; C4 pass. The new-word "ent…" reading at frame A is **unfalsified but unnameable** at battery grade — no 50 value unlocks it, and 50's value is independently underdetermined. The reading stays locked; 50's value stays open. No standing/red-team verdict contradicted or downgraded; §7 intact.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-50-crosswindow` (P3) — systematic value search for 50 across its 11 windows; the "la"+50 pair (@380/@1264) and "[71] 50 er" (@1565) are the sharpest constraints. Bar: name 50's value iff one value parses all 11 windows with ≤1 unstated assumption.
2. `mentent-580-rival` (P3) — test the "ne mentent" (3pl *mentir*) rival segmentation at frame A (`94 82 06 06` = "ne mentent", 50 = following word). Bar: parse iff a 3pl subject is licensed in `…45 13 55 61` under standing values.
3. `la-50-frames` (P4) — resolve the "la [50]" frames at @380 ("pour la [50] m'[16]") and @1264 ("la [50] que"); naming 50's role there constrains every 50 hypothesis including frame A.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-frameA-50-value.md` (this file).
- `battery-queue.json`: `frameA-50-value` queued → verdict/null via temp-file + rename; pre-write assert confirmed `queued`/verdictless; post-write JSON re-validated; own entry only.
- Lock `locks/frameA-50-value.lock`: created on start, deleted on completion.
- `canonical.py` never used; R5005, sealed gate instances, red-team adjudication queue untouched.
