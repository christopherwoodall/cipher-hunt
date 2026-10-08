# Round-16 battery: pre (70) — value promotions adjudicated

Finder report: `code/crowd16/report_inbox/next-token-findings-pre.md` (ingested 2026-10-07).
Status entering: 70="pre" BANKED (pencil GT). 94, 12, 48, 39 all OPEN
(94's value unnamed; 48="ne" KILLED, 48="de" unconditioned KILLED,
48="est" KILLED, {48,94} homophone-set KILLED — none of which is 94="ne"
or 48="e"-letter).

---

## PRE-REGISTRATION (locked before formal tests)

**Promotion bar (values):** ≥2 INDEPENDENT clean legs. "Independent" =
different frames, not the same window family; "clean" = grammatical on
banked/promoted values without straining. Conditional legs (on leads or
provisionals) count toward LEAD, not promotion.

**Bar R1 (94="ne" PROMOTE):** frames — 62-94 ×9 (conditional on 62="on"
STRONG lead), 94-59 ×3 "n'est" (conditional on 59="est" provisional),
94-82 ×4 "ne m'" (82="m" banked GT — independent, but continuations
examined), 70-12-94 ×2 "prenne" (conditional on 12="n" lead). PROMOTE iff
≥2 independent clean legs; else STRONG LEAD.

**Bar R2a (12="n" PROMOTE):** frames — 12-48 (count CHECKED, not taken on
trust), 40-12 "en" @64 (word-internal alternative examined), 12-34 "ni"
@1740, 70-12 "prenne/prennent" (compositional — conditional, cannot
self-promote). PROMOTE iff ≥2 independent GT-anchored legs.

**Bar R2b (48="e" PROMOTE):** 48="e"-letter must have INDEPENDENT legs, not
just a re-reading of A7's granted "me [48-verb]" frame — and the re-reading
must parse ≥ as well as the granted frame at all 4 windows. Otherwise
DECLINE (the A7 frame stands; no re-litigation without new evidence).

**Bar R4 (39="a/à" value):** frames — 64-39 "qui a" (count CHECKED),
70-39-11 ×2, 59-39 ×2 (frame labels CHECKED against classification),
03-39 ×3. ≥2 independent legs for LEAD-or-better.

---

## TESTS

`t = code/crowd16/next-token/test_pre.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | 62-94 = 9 | |
| 2 | 94-59 = [558,762,1795] | |
| 3 | 94-82 = [578,1182,1353,1742]; followers P[579+2],P[1183+2],P[1354+2],P[1743+2] | |
| 4 | 70-12-94 = [347,1547]; windows P[345:353], P[1545:1553] | |
| 5 | 12-48 count = 5 ([169,709,809,1075,1736]) — finder claimed ×7 | |
| 6 | 40-12 @64: P[62:67] = [29,40,12,94,92] | |
| 7 | 12-34 = [1740] | |
| 8 | 70-12-06 = [1118] | |
| 9 | 64-39 = [606] (×1 — finder implied a frame) | |
| 10 | 70-39-11 = [1067,1604] | |
| 11 | 59-39 = [763,1511]; @763 window P[761:766] | |
| 12 | 70-98-41 = [235]; 98-41 global = 1 | |
| 13 | 70-91-77 = [519]; 91-11 = 2 | |
| 14 | 70-88-10 = [615] | |
| 15 | @1067: P[1065:1072] = [62,18,70,39,11,44,74] | |
| 16 | 82-48 followers: P[126],P[377],P[398],P[1229] = [11,0,6,29] | |

---

## VERDICT

**R1 94="ne" — STRONG LEAD, not promotion.** All frames re-derived, but none
is both fully independent and clean:
- 62-94 ×9 "on ne": strong, but CONDITIONAL on 62="on" (STRONG lead, not banked).
- 94-59 ×3 "n'est" @558/@762/@1795: clean elision, but CONDITIONAL on
  59="est" (provisional).
- 94-82 ×4 "ne m'": 82="m" banked GT (independent), but continuations
  strained — @578/@1182 → 06-06 (doubled 06 resists "en"), @1353 → 06-52,
  @1742 → 46 ("ne me que", verbless).
- 70-12-94 ×2 "prenne": CONDITIONAL on 12="n" (lead, see R2a).
- 12-48 dual-spelling: ×5 not ×7 (corrected), conditional on 12="n".

Zero fully-independent clean legs; three conditional legs converging on one
value + one independent-but-strained leg. The convergence is real and
valuable — 94="ne" is the strongest open value on the board — but promotion
needs an independent clean leg (e.g., 62="on" promoting, which upgrades the
×9 leg, or a "ne"+banked-verb window). The finder's PROMOTE is declined;
STRONG LEAD granted.

**R2a 12="n" — LEAD, not promotion.**
- 12-48 = **×5, not ×7** (re-derived thrice: [169,709,809,1075,1736]) —
  finder count error, material: it weakens the "high frequency n=23"
  argument's key exhibit.
- 40-12 "en" @64: P[62:67]=[29,40,12,94,92] — "…er-en-94-92"; word-internal
  "…eren…" not excluded; single ambiguous leg.
- 12-34 "ni" @1740: clean (34="i" GT) but n=1.
- 70-12 "prenne/prennent": compositional — conditional, cannot self-promote.
LEAD. The "prenne"/"prennent" compositional + "ni" keep it alive; the count
error and @64 ambiguity keep it below promotion.

**R2b 48="e"-letter — DECLINED.** No independent legs: the entire case is a
re-reading of A7's 4 granted "me [48]" windows, and it parses WORSE:
@125 "me la [02]…" (needs a verb after — possible), @376 "me pour la"
(broken — 00="pour" banked), @397 "me [06] la" (broken), @1228 "me er ce"
(broken). 1/4 possible, 3/4 broken vs the granted frame's 4/4 verb-slot
recurrence. Revisiting the granted A7 L2 frame on this basis is
re-litigation without new evidence — declined. 48's value stays open
(verb-stem candidate stands); 48="e" is not banked, not lead-grade.

**R3 "prenne"/"prennent" — compositional LEAD.** @1547 [0,46,70,12,94,92]
("pour que prenne [92]" — 00/46 banked, beautiful) and @347 [1,6,70,12,94,74]
and @1118 "prennent" all re-derived. Conditional on the 12="n" + 94="ne"
leads — they SUPPORT the leads, cannot promote them. Recorded as the best
compositional exhibit for both leads.

**R4 39="a/à" — LEAD.**
- 64-39 "qui a": **×1 @606** (finder implied a frame; it's a singleton —
  corrected).
- 70-39-11 ×2 @1067/@1604: word-internal "pré-a-la" (compatible with P8's
  "préalable" @1067: 70-39-11-44 = "pré-a-la-ble" — the readings compose,
  not compete).
- 59-39 ×2: @763 = [94,59,39] = **"n'est [39]"** (finder mislabeled "est à"
  — corrected); @1511 LEFTOVER.
- 03-39 ×3: 03 unknown, weak.
Two word-internal legs + one "qui a" singleton = LEAD. Promotion needs a
standalone "a"/"à" window ("[il] a [verb]", "[noun] à [inf]").

**P5–P11 (leads/nulls, as finder stated):**
- P5: "première fois" @235 = word-LEAD ("pre-?-?-fois" admits one French
  word); 98-41 hapax bigram → 98="mi"/41="ère" stay SINGLE-LEG (not
  lead-grade for the cells). The analytic/syllabic dual-spelling
  observation ("première" two ways) is a genuine architectural finding —
  recorded.
- P6: 91="va" LEAD ("prévalent" @519 + "va la" ×2).
- P7: 88="s"/10="s" LEAD ("presser" @615; "présenter" alternative live;
  88's plural/article boundaries support letter-"s").
- P8: 44="ble" LEAD ("préalable" @1067 only; @1604's 92 divergent — the
  finder's honest fencing stands).
- P9/P10/P11: nulls held (@368 anomaly, @1586 boundary, @1300/@1331 singletons).

**Queued:** 94="ne" promotion battery (needs 62="on" or a clean "ne"+verb);
12="n" second-leg hunt ("ni"/"en" disambiguation); 39 standalone-"a" hunt;
88 "presser/présenter" discriminator.
