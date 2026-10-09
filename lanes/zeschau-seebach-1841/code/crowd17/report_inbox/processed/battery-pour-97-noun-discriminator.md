# Battery verdict: pour-97-noun-discriminator

Target: `pour-97-noun-discriminator` (priority 3). Parent: `nom-97-526-class` NULL (2026-10-09), follow-up item 1.
Date: 2026-10-09. Worker: battery worker (subagent 0b7149bd).

## Bar (verbatim, pre-registered)

"if 00's bare takes are exclusively verb-frame cells (86/33/92/66/97) with nominal takes article-mediated (00→11×4), the pour-windows stay INF-favoring; a single verified 00→bare-noun take collapses the discriminator and gives NOM-97 four windows"

Numbered clauses (restated before testing; scoping notes are term definitions, not bar changes):

- **C1:** Every bare take of 00 — a 00→F window where F is a governed complement cell and F is not the article — has F in {86, 33, 92, 66, 97}. Complementizer, clitic, letter, pronoun, and polyvalence followers (46=que, 34=i, 64=qui, 67=et/veut, 98=vient-lead) are licensed non-takes, fenced with standing cause; open cells (36, 13, 20, 44) are the kill-search set: any one of them a verified noun fires the kill arm.
- **C2:** Nominal takes of 00 are article-mediated: 00→11 occurs exactly 4× stream-wide and is the only article-directly-after-00 pattern.
- **C3 (kill arm):** A single verified 00→bare-noun window → KILL: the discriminator collapses and NOM-97 gains the four pour-windows (97@2/@288/@588/@1823).

Adverses: none listed.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py`. Asserts held (1,847 pairs,
96 types, crib "11 70 82 34 29 40" pair-aligned at 754/1034). `canonical.py`
never used. R5005, sealed gate instances, and the red-team adjudication queue
untouched.

Standing premises adopted (not re-litigated): 00="pour" (A9); 86 INF-class
(A9); 33 que-valency (A10); 46=que; 47="ce" (A4); 64="qui"; 11=la (pencil);
34=i (pencil); 67=sole true polyvalence et/veut (§7); 17="fois" (promote);
36=NOUN class-level (battery PROMOTE, `class-36-profile`, 2026-10-08);
noun-44 KILLED; 97 infinitive-class (battery PROMOTE, `frame-97-profile`),
finite-verb KILL (`val-97-verb-test`), INF/NOM tie NULL.

## Window-level evidence (byte-exact, 0-based @-offsets of the 00 cell)

Full 00-follower census, n(00)=55 (matches `battery-pour-prefix-00-census.md` exactly):

| follower | n | windows |
|---|---|---|
| 86 | 12 | @552 @660 @727 @866 @888 @961 @1001 @1127 @1374 @1505 @1791 @1824 |
| 33 | 8 | @185 @407 @466 @845 @935 @1087 @1244 @1629 |
| 66 | 7 | @188 @245 @253 @714 @1108 @1493 @1532 |
| 92 | 6 | @48 @329 @592 @682 @977 @1153 |
| 97 | 4 | @1 @287 @587 @1822 |
| 11 | 4 | @76 @378 @1287 @1405 |
| 46 | 4 | @106 @545 @1545 @1680 |
| 36 | 3 | @739 @1312 @1584 |
| 34 | 1 | @27 |
| 64 | 1 | @748 |
| 67 | 1 | @1247 |
| 98 | 1 | @1138 |
| 13 | 1 | @480 |
| 20 | 1 | @667 |
| 44 | 1 | @1602 |

**The three 00→36 windows** (±3 context):

- **@739** (a5_02): `18 82 06 | 00 | 36 20 30` — "pour [36] [20]".
- **@1312** (a7_04): `30 92 44 | 00 | 36 74 62` — "pour [36] [74]".
- **@1584** (a8_02): `53 12 44 | 00 | 36 70 64` — "pour [36] [70-pre]".

36's standing class verdict: `class-36-profile` PROMOTE (2026-10-09 queue
status: verdict/promote) — 36=NOUN at class level on 9 windows, zero hard
contradictions; infinitive and adjective excluded with hard ungrammatical
windows. Its legs L2/L3/L4 are exactly these three windows, scored as
"pour [36-noun]" — grammatical in the formal register ("pour memoire" /
"pour information" pattern). The noun assignment does not depend on the
pour-frames alone (solid ce-contact leg @1215 "par ce [36]"; restricted
est-frames @1449/@1834; infinitive dead at @1449/@1834/@1215; adjective dead
at all three pour-frames + @1215). No circularity: the class is independently
grounded, and "pour" (A9) must govern a complement — no boundary rescue
strands 00 grammatically.

**The four 00→11 windows** (C2): @76 `00 11 29` ("pour la [29]"),
@378 `00 11 50`, @1287 `00 11 17` ("pour la fois" — 17="fois" promoted,
genuine article-mediated nominal), @1405 `00 11 95`. 11 is the only
determiner-class cell that ever directly follows 00 (47/77 never do).

**Fenced non-take followers** (standing cause, not noun takes):

- 46=que ×4: "pour que" A9-granted (bar (a) met via @1545/@1680). Clausal complementizer, not a noun take.
- 34=i ×1 (@27): pencil ground-truth letter. Not a noun.
- 64=qui ×1 (@748): granted relative pronoun; "pour qui" grammatical. Not a noun.
- 67=et/veut ×1 (@1247): the §7 sole true polyvalence; the A9-noted "pour et/veut que" residual. Not a noun.
- 98="vient" ×1 (@1138): battery-grade verb lead. Not a noun (the window is hard for 00="pour" generally, but outside this discriminator's noun scope).

**Open-cell followers — kill-search set, all negative:**

- 13 ×1 (@480): no noun verdict anywhere (13: letter KILL, "les"-pronoun KILL, reseg-13-armA PROMOTE = nominal-closer, not a noun value; val-13-567 queued). Not verified.
- 20 ×1 (@667): noun-20-value NULL; 20-as-noun is the queued `poly-20-docket` RED-TEAM venue. Not verified at battery grade.
- 44 ×1 (@1602): `noun-44` KILLED at battery grade. Not a noun.

## Per-clause pass/fail

1. **C1 (bare takes exclusively verb-frame cells): FAIL — kill grade.** Three
   windows force the claim false: @739, @1312, @1584 are 00→36 with 36 a
   battery-promoted NOUN (class level, standing). These are bare takes
   (no article between 00 and 36) of a verified noun. The parent's in-session
   check ("zero 00→bare-noun windows") counted only 41 of 55 followers
   (37 verb-frame + 4 article) and missed 36×3 among the 14 uncounted windows.
2. **C2 (nominal takes article-mediated, 00→11×4): PASS.** Exactly four
   00→11 windows byte-exact; 11 the only determiner-class direct follower;
   @1287 shows genuine article-mediated nominal ("pour la fois").
3. **C3 (kill arm): FIRES.** A verified 00→bare-noun take exists — three of
   them (@739/@1312/@1584, 00→36, 36=NOUN promoted). The discriminator
   collapses. Consequence per the bar: NOM-97 gains the four pour-windows
   (97@2/@288/@588/@1823, the 00→97 windows): "pour [97-noun]" is now
   grammatically licensed by the 00→36 precedent, joining NOM's four clean
   windows (@525/@94/@566/@1413).

## Verdict: KILL

The article discriminator is dead at kill grade: 00 governs bare nouns
stream-wide (three verified windows), so the pour-windows cannot be held
INF-favoring on distributional grounds.

Scope and non-contradictions (explicit):

- NOT re-litigated: 36=NOUN (adopted as premise); 00="pour" (A9); the four
  pour-windows' INF legs still exist as legs — only the discriminator's
  distributional argument against NOM is removed.
- NOT promoted: noun-97. The class question stays red-team venue
  (`redteam-97-tie-adjudication` package stands). `frame-97-profile`'s
  class-level INF promote is untouched — never downgraded; this kill removes
  an anti-NOM argument, it does not overturn a verdict.
- No standing or red-team verdict contradicted (red-team report carries no
  36 or bare-noun-government ruling; grep-verified). §7 intact; no new
  polyvalence declared; canonical-stream caveat stands.
- Per §4, kills regenerate no follow-ups.

Note for the red team: the INF/NOM-97 tie tally changes shape — the
discriminator that disfavored NOM at the four pour-windows is gone, so the
tie is now 6 INF legs vs 8 NOM-available windows (4 clean + 4 pour) pending
adjudication. The `redteam-97-tie-adjudication` package should be refreshed
with this kill.

## Bookkeeping

- Stream: repaired 1,847-pair parse, asserts held; `canonical.py` never used.
- Queue: `pour-97-noun-discriminator` → status verdict, result kill, 2026-10-09 (update follows; pre-write assert: was queued/verdictless; temp-file + rename; own entry only; no downgrade).
- Lock `locks/pour-97-noun-discriminator.lock` created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
