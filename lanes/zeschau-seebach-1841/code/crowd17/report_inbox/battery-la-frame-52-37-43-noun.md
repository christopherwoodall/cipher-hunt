# Battery verdict: la-frame-52-37-43-noun

- Target: `la-frame-52-37-43-noun`
- Claim: the byte-identical "11-52-37-43" tail shared by @1123 and @1721 is one noun phrase
- Worker: battery worker la-frame-52-37-43-noun (a8457e8d-95d0-438e-8fb2-68a89fcb67da)
- Date: 2026-10-09
- Verdict: **NULL** (43's nominality is red-team-gated; the structural parse is real but not battery-promotable)

## 1. Bar (verbatim from battery-queue.json)

"name the 52-37-43 phrase iff it parses as a single noun phrase under 'la' identically in both windows with one stated segmentation; stems inherit shape constraints; else fence tail as formulaic"

Numbered clauses (pre-registered before testing):
- **C1:** PASS iff one naming of "52 37 43" parses as a single noun phrase under 'la' (=11, banked GT), identically at both windows, with one stated segmentation.
- **C2:** PASS iff the naming respects ("inherits") the standing shape constraints on 52, 37, 43.
- **C3 (else):** if C1 fails, fence the tail as formulaic.

## 2. Method

- Read BATTERY-PROTOCOL.md first. Lock `locks/la-frame-52-37-43-noun.lock` created on start, deleted on completion.
- Stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: **1,847 pairs / 96 types verified**. `canonical.py` never touched.
- 0-based @-offsets throughout (queue convention). The claim's "@1123"/"@1721" are the 0-based indices of the "11".
- Adopted as premises (not re-litigated): battery-la-523743-adjective's Type-A structural parse (2026-10-08); battery-unit-52-37-name's 52~52 split candidacy (2026-10-08); battery-dite-52-37-anaphora's "dite" kill (2026-10-08/09); battery-noun-43's closure (NULL, 2026-10-09); battery-cond-mesure-43full's empty survivor set (NULL, 2026-10-09); battery-at21-82-43-29-adjudicate's @21 word-internal confirmation (NULL, 2026-10-09); battery-ent14ent-residual-adjudicate's head-residual fence (KILL, 2026-10-09); battery-ne52inf-adverb's 52 adjective-arm finding (NULL, 2026-10-09).
- R5005, sealed gate instances, and the red-team adjudication queue untouched.

## 3. Window-level evidence (all byte-traced)

- "52 37 43" occurs **exactly 2x** stream-wide: 0-based @1124 (row a6_07) and @1722 (row a8_07). Both are preceded by 11 → the "11 52 37 43" tails sit at @1123 and @1721, byte-identical, both fully mid-row.
- **W1 @1123 (a6_07):** `14 06 | 11 52 37 43 | 00 86 52` = "[residual head] la [52-37] [43] pour [86] [52]..."
- **W2 @1721 (a8_07):** `68 06 | 11 52 37 43 | 98 39 88` = "[68]ent la [52-37] [43] [98-finite] [39] [88-verb]..."
- Control: the third "11 52" window @1006 (a6_02) is "11 52 35 18 79 80" — a different frame; 52's shape undetermined there (per la-523743-adjective).
- "52 37" occurs 4x: @1124, @1129 ("52 37 86" — 86-follower, not 43), @1356 ("52 37 64"), @1722. The trigram is 2/4 of "52 37" windows.

## 4. Per-clause pass/fail

- **C1 — CONDITIONAL PASS.** Stated segmentation: `11 | 52-37 | 43`. Naming: **"la [52-37-prenominal-adjective-unit] [43-head-noun]"** (the Type-A parse). Both windows admit it identically with zero new assumptions beyond standing premises: W1 "la même/seule [43] pour [86]" (NP + pour-complement — clean); W2 "la même/seule [43] [98-finite]" (subject NP + finite verb — clean). No finite-verb parse is available in the slot (la-battery L2). The rival segmentation "la [52-adj] [37-noun] | 43" strands 43 as a bare post-object NP (ungrammatical per la-523743-adjective); the compound-noun rescue "la [52-adj] [37-43-noun]" has no positive evidence. The structural parse is unique. **However**, the naming's 43-leg cannot be battery-confirmed (see C2) — the pass is structural only.
- **C2 — FAIL.** Inherited shape constraints:
  - 52: adjective-shaped in the prenominal slot ✓ (no finite-verb parse available; adjective arm live at "la [52]" x3 / "52 37" x4 per ne52inf-adverb; unit candidates {même, seule} after dite's kill).
  - 37: unit-internal, not head noun ✓ (la-523743-adjective clause 2); sub-lexical value fenced to S5 (37="le" MEDIUM standing fence; venue s5-foundation) — not decided here.
  - 43: ✗ **contradictory at battery grade.** (i) Verb stem CONFIRMED at @21: "43-29 = [43]er" word-internal (at21-82-43-29-adjudicate; noun-43: "@21 independently kills every monovalent noun at kill grade"). (ii) Noun values {suite, manière, condition, mesure} ALL kill-grade dead — survivor set EMPTY (noun-43, cond-mesure-43full). (iii) "The noun-43 line is closed at battery level pending red-team act" (noun-43 headline). Naming 43 as head noun here while @21's verb-stem stands is an implicit polyvalence claim — the redteam-43-polyvalence venue, a red-team act. Battery cannot satisfy C2.
- **C3 — FIRES in modified form.** The bar's "fence tail as formulaic" is inaccurate: the structural NP parse is real and unique, not a mere collocation. The accurate fence: **the Type-A NP reading is FENCED AS RED-TEAM-GATED** — it stands as the unique structural parse of the tail but cannot be battery-promoted until redteam-43-polyvalence adjudicates 43's nominality (or the par43-adverbial-attestation corpus defense re-opens the noun premise).

## 5. Adverses answered

- **"52/37/43 values open"** — ANSWERED: no values named; the naming is structural/class-level only. The 52-37 unit's {même, seule} tie stays open (owned by queued `adj-52-37-value-rerun`, not duplicated); 37's sub-lexical value stays S5-fenced; 43's value stays open (survivor set empty).
- **"@1121's head is a segmentation residual"** — ANSWERED, now CONFIRMED: battery-ent14ent-residual-adjudicate (KILL, 2026-10-09) proved "06-14-06" @1118–1123 exhaustively unresolvable at battery grade. The tail's NP parse is head-independent — it is identical at W2, whose head is "68 06" (nominal-leaning per stem-68-id), not residual. The residual does not disturb the tail.

## 6. Verdict: NULL

The tail IS one noun phrase structurally ("la [52-37-adj-unit] [43-head-noun]", identical at both windows, one stated segmentation), but the naming's 43-leg requires 43-nominal, which is now red-team-gated: @21's confirmed verb-stem reading kills monovalent-noun at kill grade, the noun-value survivor set is empty, and the noun-43 line is closed at battery level. Promoting the naming would implicitly declare 43 polyvalent — a red-team act under §7. No standing verdict contradicted or downgraded (la-523743-adjective's structural parse adopted; noun-43's closure honored; no red-team ruling on 43 exists yet). §7 intact. R5005, sealed gates, red-team queue untouched.

**Headline for the red team:** the 43 crisis now gates a previously-firm structural parse. "la [52-37] [43]" is the second casualty site of the @21 verb-stem confirmation (after the noun values): the NP is real, but its head noun's nominality is the redteam-43-polyvalence question.

## 7. Follow-up targets (null regenerates work)

1. **`tail-523743-rerun-43poly`** (P2) — re-run this bar once redteam-43-polyvalence adjudicates 43's nominality; the Type-A naming promotes cleanly iff 43-nominal is granted (via polyvalence declaration or the par43-adverbial-attestation corpus defense). Verified absent from queue.
2. **`la-1006-52-frame`** (P4) — control: test 52's adjective shape at the third "la 52" window (@1006, "11 52 35 18 79 80"); sharpens whether the adjective arm is tail-specific. Verified absent from queue.
- Coordination note: queued `adj-52-37-value-rerun` owns the {même, seule} tie-break; not duplicated here.
