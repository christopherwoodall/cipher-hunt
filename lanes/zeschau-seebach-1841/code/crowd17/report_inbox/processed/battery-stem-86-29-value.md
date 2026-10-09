# Battery verdict: stem-86-29-value

- Target id: `stem-86-29-value`
- Claim: "name the -er stem across the four '86 29' windows"
- Date: 2026-10-09
- Worker: battery worker (subagent f7953987-c01e-4c75-9868-6afef048a857)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. @-offsets are 0-based token offsets.
- Lock: `code/crowd17/next-token/locks/stem-86-29-value.lock` created 2026-10-09T19:29:00Z (no stale lock); deleted on completion.

Terms (ASD-STE100): "leg" = one byte-verified window where the named value parses under a licensed frame with zero new assumptions. "Tier" = the level of the unit (whole word vs stem/syllable vs letter). "Discriminator" = a contact or collocation that selects one candidate value over its rivals.

## Bar (verbatim, pre-registered before testing)

"one stem parses all four with a contact discriminator (via the '00 86 56' x4 collocation or the '86 70' @867 -prendre constraint); else fence as unnameable at battery grade"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** one specific -er stem is named that parses all four "86 29" windows AND is selected over rival stems by a contact discriminator (the "00 86 56" x4 collocation or the "86 70" @867 -prendre constraint).
2. **C2 (else-arm):** if no stem meets C1, fence 86's stem value as unnameable at battery grade, with the discriminator failures stated.

Adverses listed: "the 89 slot is licensed infinitive-shaped only, never by a lexical noun (this null's finding 2)" — adopted from val-86-1391, not re-litigated; answered below in Findings §4.

## Method

1. Read BATTERY-PROTOCOL.md first. Created lock on start; no prior/stale lock.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Read the standing 86 record before testing (adopted, never re-litigated):
   - 86 = INF-class, A9 leg-1 class-level; R20-087 re-confirmed "values not named".
   - val-86-1391 NULL (2026-10-09, parent of this target): "[86]er" is a spelled -er infinitive (stem 86 + 'er', battery-grade tier finding); every -er stem parses all four "86 29" windows with zero friction; the "00 86 56" x4 collocation and "86 70" @867 each admit multiple stems.
   - noun-86-dlife-name KILL; ce86-le86-parity PROMOTE (merge, value unnamed); split-86-amended-rule (§7 venue for stem-life vs determiner-life split).
   - Banked: 29='er' (pencil GT), 70='pre' (pencil GT), 00='pour' (A9), 84='on' (A15), 89=noun (LEAD).
4. 1841 diplomatic French throughout.

## Window-level evidence (byte-exact)

### The four "86 29" windows (exactly 4x stream-wide, re-verified)

- @431 (a2_09): `63 77 86 29 82 16 78` — "[77] [86]er m[16]" (77='le' provisional; 82='m' pencil letter)
- @1375 (a7_06): `00 86 29 89 84 92` — "pour [86]er [89] on" (00='pour' A9; 84='on' A15)
- @1391 (a7_07): `67 86 29 89 16` — "[67] [86]er [89] 16" (67 contested et/veut, red-team venue)
- @1825 (a8_11): `00 86 29 82 38` — "pour [86]er m[38]"

Two subfamilies: "86 29 82" x2 (@431, @1825), "86 29 89" x2 (@1375, @1391).

### Discriminator D1: "00 86 56" (exactly 4x; "86 56" never occurs without preceding 00 — re-verified)

- @961: `00 86 56 41` — "pour [86] [56] [41]"
- @1001: `00 86 56 47` — "pour [86] [56] ce"
- @1505: `00 86 56 41` — "pour [86] [56] [41]"
- @1791: `00 86 56 42` — "pour [86] [56] [42-noun]"

56's value and class are open; 56's followers across the four: {41 x2, 47, 42} — heterogeneous, no frame.

### Discriminator D2: "86 70" @867 (1x)

`46 00 86 70 87 77 89` — "que pour [86]pre ce le [89]" (70='pre' pencil GT).

## Findings

### 1. C1 fails: no stem is selected

**Base (adopted from val-86-1391, spot-verified):** the -er infinitive class parses all four windows with zero byte-level friction — "le [S-er]" (nominalized infinitive, @431), "pour [S-er] [N]" (purpose infinitive + nominal object, @1375), "[et/veut] [S-er] [N]" (@1391), "pour [S-er] m[X]" (@1825) — for donner, parler, demander, porter, laisser, trouver, penser, manger alike. The four windows discriminate nothing.

**D1 selects nothing.** "pour [S] [56]" with 56 class-open and value-open is satisfiable for every candidate stem S: 56 can be read as whatever the frame needs (particle, pronoun, adverb, or stem continuation), and its heterogeneous followers (41 x2, 47, 42) supply no frame. A collocation with an open middle term is not a discriminator. For D1 to select, 56's class/value would have to be named first — it is not, at any grade.

**D2 selects nothing — and actively resists a uniform stem.** For a uniform -er stem S, the @867 frame reads "pour S+pre ce le [89]". S+"pre" is not a French word for any -er stem S (exhaustive over the plausible inventory: "compre"/"apre"/"repre"/"surpre"/"entrepre" are non-words; "propre" would need S="pro", not a verb stem; "pré"/"près" readings — "pour [S] pré", "pour [S] près" — are ungrammatical). The only French-plausible reading is a -prendre compound (comprendre/apprendre/surprendre/reprendre/entreprendre — five candidates, none forced, per the parent), and that reading requires 86 to be a PREFIX syllable — which contradicts the battery-grade stem tier ("[86]er" = stem + 'er') at the four windows. So D2 does not discriminate among stems; it creates tier tension: a uniform 86 cannot be stem-tier at the four windows and prefix-tier at @867 simultaneously. Resolving that tension (tier-split vs re-parse) is §7 red-team venue under split-86-amended-rule, not a battery discriminator.

**C1: FAIL.** Neither contact selects one stem over its rivals.

### 2. C2 passes: fence 86's stem value as unnameable at battery grade

The naming arm is structurally unmeetable on current bytes: the four windows admit the whole -er class identically, D1's middle term is open, and D2's only French-plausible reading contradicts the stem tier. No future battery work on the current bytes can name the stem; naming any one candidate would be arbitrary. **Fence cause:** underdetermination at the lane's naming standard (zero-new-assumptions leg required; none exists).

### 3. Tier tension at @867 recorded (not resolved)

Uniform-86 readings at @867:
- (i) stem-tier ("pour [S]pre..."): ungrammatical for every -er stem S.
- (ii) prefix-tier (-prendre compound): five candidates, none forced; contradicts the stem tier at the four windows.
- (iii) 86 as a complete word ("pour [86-word] pre..."): no licensed complete-word tier for 86 on current bytes.
Battery cannot choose; the split question belongs to the red team (§7). The stem-life arm at the four '86 29' windows is unaffected.

### 4. Adverse answered

"The 89 slot is licensed infinitive-shaped only, never by a lexical noun": at @1375/@1391, "[86]er [89-noun]" parses as infinitive + nominal direct object ("pour prendre le train" shape) for every candidate stem — consistent with the adverse (89 is the infinitive's object, licensed by the infinitive's shape, not a standalone nominal licensor). The adverse constrains the frame, not the stem choice; it selects nothing among stems. Answered as consistent, non-selecting.

## Per-clause results

- **C1: FAIL.** No stem is selected by either contact discriminator.
- **C2: PASS (fence arm fires).** 86's -er stem value is fenced as unnameable at battery grade; cause stated in Finding 2.

## Verdict: NULL

86's stem value across the four "86 29" windows remains unnamed. The two pre-registered discriminators fail to select: "00 86 56" x4 has an open middle term (56 unvalued, heterogeneous followers), and "86 70" @867 admits no uniform -er stem (its only French-plausible reading is a -prendre compound requiring prefix-tier 86, in tension with the battery-grade stem tier — §7 venue). No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands (rows a2_09/a7_06/a7_07/a8_11 offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json; supervisor to queue)

1. `tier-86-867-prefix` (P3) — name 86's tier at @867: prefix of a -prendre compound (comprendre/apprendre/surprendre/reprendre/entreprendre — test which prefix parses "pour [prefix]pre ce le [89]") vs stem-tier. If prefix-tier is confirmed against the stem-tier at the four "86 29" windows, package the tier-split for red-team §7 adjudication.
2. `val-56-contact-86` (P4) — name 56's class/value at the "00 86 56" x4 windows (@961/@1001/@1505/@1791). A named 56 converts the collocation from an open-middle-term into a live stem discriminator.
3. `sel-89-86inf` (P4) — at the "86 29 89" x2 windows (@1375/@1391), test 89 as direct object of "[86]er": once 89's noun value resolves, object-selectional fit discriminates among -er stems (only some infinitives take that object). Conditional on 89's value being named.

## Scope

Value-fence only, scoped to the four "86 29" windows. Untouched: the battery-grade tier finding ("[86]er" = stem + 'er'), 86's INF class (A9 leg-1), ce86-le86-parity merge, noun-86-dlife KILL, split-86-amended-rule (§7 venue), queued `x-er-89-frame` and `det-86-29-431`, the 67 @1390 et/veut conflict (red-team venue). No new polyvalence declared.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-stem-86-29-value.md` (this file).
- Queue: `stem-86-29-value` queued -> `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.stem-86-29-value.tmp` + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/stem-86-29-value.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
