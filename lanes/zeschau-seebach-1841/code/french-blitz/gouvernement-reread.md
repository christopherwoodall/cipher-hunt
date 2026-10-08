# GOUVERNEMENT RE-READ — French-syntax verdicts on all 77/78/06 windows

**Agent:** GOUVERNEMENT RE-READER (direct French-work, no coordinator)
**Date:** 2026-10-07
**Parse:** repaired 1,847-pair, positions 0-based per `code/side-keyhunt/repaired_offsets.json`
**Board used:** 7 GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que) + provisional
  87=ce, 64=qui, 96=par, 59=est, 77="le" (prov-conditioned) + leads 78={ver,er} fork,
  06="ent" iff pre=82 (ISLET 3), 52="pas" (STRONG), 94="ne" (prov-strong, negation)

## Method

Every 77–78 adjacency in the stream was extracted (±8 pairs). The "gouvernement"
5-mer (77-78-94-82-06) exists at exactly TWO positions: @1180 and @1351.
@1351 was resolved (round 10) to R-c «le [78] ne ment pas»; the gouvernement
reading is DEAD there. This re-read covers the remaining six 77–78 windows,
the 77–06 window, and the six 06–77 windows, with @1180 as the deciding window.

**Corpus grounding:** phrase queries over `code/side-period/corpus/` —
nesselrode-v7/v8/v9/v10, guizot-memoires-t5-t6 (his 1840–42 despatches),
levant-correspondence-1841-p3, revue-deux-mondes-1841-q1/q2.
CAUTION honored: Nesselrode v8 OCR word-splits make bare "ment" tokens VOID;
«ne ment pas» attestation below is from RdM (clean), not v8.

## Corpus facts established (all counts word-boundaried, case-folded)

| Phrase | Hits | Source | Status |
|---|---|---|---|
| «il ne ment pas» | 1 | RdM 1841-Q2: «il sait se taire; il ne ment pas.» | ATTESTED (verb mentir + ne…pas, era-good) |
| «ment pas» | 3 | guizot-t5t6, nesselrode-v7, nesselrode-v9 | ALL adverbial "-ment" («probablement/sûrement/vraiment pas») — NOT the verb |
| «gouvernement est» (bare, no determiner) | 0/10 | 10 hits all carry «votre/mon/leur/ce/le» or «de gouvernement» | VOID as bare subject |
| «le gouvernement est» | 4 | guizot-t5t6 ×2, RdM-Q1 ×1, nesselrode-v9 ×1 | ATTESTED (with determiner) |
| «gouvernement pas» | 0 | all files | ERA-0 (ungrammatical) |
| «ne gouverne pas» | 2 | RdM-Q1 ×1, nesselrode-v7 ×1 | ATTESTED (verb, not noun) |
| «le gouvernement» | 436 | all files | ATTESTED (noun, needs determiner) |

**Standing French rule (corpus-backed):** «gouvernement» as a subject requires a
determiner — 0/10 bare «gouvernement est» in ~7MB of 1840s diplomatic/literary
French. Every instance carries «le/votre/mon/leur/ce» or sits in a
«de»-construction.

---

## Per-window verdicts

### W1 @7 — pairs[2:13] = `97 51 47 41 06 77 78 18 93 62 98`
Sequence at focus: **06 77 78** (06@6, 77@7, 78@8), followers 18-93-62.
- R-gouv (77=gou, 78=ver): needs 94-82-06 after 78 for "gouvernement". Followers
  are 18-93-62. **5-mer ABSENT → GOUVERNEMENT IMPOSSIBLE. KILL (structural).**
- R-le (77="le"): «le [78] [18]…». 78={ver,er} unidentified here; 18 unknown.
  No French verdict possible beyond: not gouvernement.
- **Verdict: GOUVERNEMENT DEAD (no 5-mer). Survivor: 77="le"+78 unidentified.**

### W2 @213 — pairs[208:219] = `44 50 88 19 74 77 78 06 59 46 29`
Sequence at focus: **77 78 06** (77@213, 78@214, 06@215), then 59="est",
46="que" (GT), 29="er" (GT).
- R-gouvernent (77=gou, 78=ver, 06=ent → "they govern"): TWO fatal problems.
  (1) 06="ent" iff pre=82 (ISLET 3); here pre=78 → breaks the islet.
  (2) «gouvernent est» — a conjugated verb directly followed by «est» is
  UNGRAMMATICAL in French (no construction licenses «ils gouvernent est»).
  **KILL (grammatical + islet-break).**
- R-le (77="le"): «le [78] [06] est que er». 78={ver,er}; 06 (pre=78) unidentified.
  Frame «…est que…» present but 77/78/06 unidentified. Not gouvernement-adjacent.
- **Verdict: GOUVERNEMENT/GOVERB DEAD. Survivor: 77="le"+78+06 unidentified.**

### W3 @647 — pairs[642:653] = `20 24 87 61 88 77 78 52 82 94 76`
Sequence at focus: **77 78 52 82 94** — 52="pas" (STRONG) present.
- R-gouv: 5-mer absent (78→52, not 94). **KILL (structural).**
- R-le: «le [78] pas m ne». The «pas» precedes «m»+«ne» — REVERSED for a
  «ne…pas» negation. No French parse found: «le [ver/er] pas» is not a clause,
  and «pas m ne» is ungrammatical in either order. 78="me" also dead here
  (N25: «pas me» era-0 kill-grade). This window is OPAQUE — needs a new idea
  (possibly 52≠"pas" locally, or 94="ne" non-negation, both expensive).
- **Verdict: GOUVERNEMENT DEAD. Window OPAQUE — flagged for the conditioner.**

### W4 @1077 — pairs[1072:1083] = `42 98 98 12 48 77 78 64 06 52 89`
Sequence at focus: **77 78 64 06 52** — 64="qui" (prov), 52="pas" (STRONG).
- R-gouv: 5-mer absent (78→64). **KILL (structural).**
- R-le: «[48] le [78] qui [06] pas». «qui…pas» needs «ne»; 06 sits in the
  «ne» slot but 06="ent"-islet needs pre=82 (pre=64 here) → 06 unidentified.
  «qui [06] pas» with 06≠"ne" is ungrammatical. 48 UNIDENTIFIED compounds it.
- **Verdict: GOUVERNEMENT DEAD. Blocked on 48 and 06 IDs.**

### W5 @1180 — pairs[1172:1189] = `21 85 36 74 32 48 59 37 77 78 94 82 06 06 59 42 06`
**THE DECIDING WINDOW.** The only unresolved 77-78-94-82-06 5-mer in the stream.
Full local read: 59="est"(1178) 37(?) 77 78 94="ne" 82="m"(GT) 06="ent"(islet ✓,
pre=82) 06(?)(1185, pre=06) 59="est"(1186).

**R-gouv** (77=gou, 78=ver, 94=ne word-internal, 82=m, 06=ent → «gouvernement»):
1. Breaks 77="le" (provisional-CONDITIONED) — high cost.
2. Breaks 94="ne" (provisional-STRONG, negation) → word-internal syllable —
   high cost. The @1351 precedent: the IDENTICAL 5-mer resolved to the
   negation reading; 94 cannot be both (frenchman Gate 6, round 10).
3. «gouvernement» as subject needs a determiner (0/10 bare in corpus) →
   forces 37 to be a determiner with zero evidence.
4. Yields «est [37] gouvernement [06] est» — TWO «est»s (1178 and 1186, both
   provisional) with an unidentified 06 between subject and verb.
   Syntactically incoherent.
5. «gouvernement pas»-style frames are era-0; no «pas» here to force anything,
   but the reading buys nothing either.
**→ GOUVERNEMENT KILL (kill-grade: two provisional-breaks + determiner
requirement + double-«est» incoherence + @1351 precedent).**

**R-isl** (77="le", 78=[er/ver], 94="ne" negation, 82="m", 06="ent" islet):
«est [37] le [78] ne ment [06] est».
- Board-consistent throughout (zero provisional-breaks).
- «il ne ment pas» ATTESTED (RdM 1841-Q2) → the «ne ment» core is era-good
  French; the missing «pas» and absent subject are gaps, not kills
  (literary «ne»-without-«pas» exists, e.g. «je ne sais»).
- INCOMPLETE: trailing 06 (1185, pre=06, not islet) + «est» (1186) unexplained;
  leading «est [37] le» unexplained. This is the least-bad reading, not a
  clean win.
**→ SURVIVES as board-consistent LEAD-weak; window NOT cleanly resolved.**

**W5 verdict: GOUVERNEMENT DEAD at the last 5-mer. The thread has no
remaining 77-78-94-82-06 window anywhere in the stream.**

### W6 @1542 — pairs[1537:1548] = `06 21 62 93 88 77 78 43 00 46 70`
Sequence at focus: **77 78 43 00** — 46="que" (GT), 70="pre" (GT) follow.
- R-gouv: 5-mer absent (78→43). **KILL (structural).**
- R-le: «le [78] [43] [00] que pre». 00="pour" (STRONG LEAD) gives
  «…pour que pre…» — the «pour que»+subjunctive frame is era-good, but
  77/78/43 are unidentified so the frame can't be claimed. 00="le"-islet
  alternative also open.
- **Verdict: GOUVERNEMENT DEAD. «pour que pre» frame noted, unidentified head.**

### W7 @521 — pairs[516:527] = `77 80 09 70 91 77 06 55 81 97 47`
Sequence at focus: **77 06** (77@521, 06@522, pre=77≠82 → NOT islet).
Preceding 70="pre" (GT) at 519.
- R-gouv: 77="gouv" needs 78 next; 06 follows instead. **KILL (structural).**
- R-le: «pre [91] le [06]…». «pre»+«le» suggests «prendre le» / «près le»
  frames (91 unidentified). Plausible head, needs 91.
- **Verdict: GOUVERNEMENT DEAD. «pre [91] le» frame live.**

### 06–77 windows (brief — wrong order for "gouvernement", which needs 77 first)
- **@6** (`00 97 51 47 41 06 77 78 18`): 06-77-78 = W1's window (same site, @6/@7/@8).
  Covered above. GOUVERNEMENT DEAD.
- **@206** (`87 11 92 63 42 06 77 44`): 87="ce" 11="la" then 06 77.
  «ce la [06] le/gouv» — «ce la» is itself ungrammatical, suggesting 87 or 11
  is misread locally, or a different segmentation. 06 (pre=42) not islet.
  Not gouvernement-order. No verdict beyond: needs re-segmentation.
- **@789** (`42 94 74 65 84 06 77 64 46`): 94="ne" … 06 77 64="qui" 46="que".
  «ne [06] le/gouv qui que». 06 (pre=84) not islet. Not gouvernement-order.
- **@890** (`37 03 02 00 86 06 77 76 01`) and **@967** (`86 56 41 19 24 06 77 76 01`):
  byte-similar tails **06 77 76 01** at both — likely the same formula.
  86 NULL at both. Not gouvernement-order. The 06-77-76-01 formula is a
  conditioner item (86's value NULL since round 9).
- **@1762** (`17 78 41 15 93 06 77 84 09`): 06 77 84 (84=en-islet/noun).
  Not gouvernement-order.

---

## Kills (with evidence)

| # | Window | Killed reading | Evidence |
|---|---|---|---|
| K1 | @1180 | «gouvernement» (5-mer) | Two provisional-breaks (77="le", 94="ne"); determiner required 0/10 bare (corpus); «est [37] gouvernement [06] est» incoherent; @1351 precedent (identical 5-mer → islet) |
| K2 | @7 | «gouvernement» | 5-mer structurally absent (78→18) |
| K3 | @213 | «gouvernent» (verb) | «gouvernent est» ungrammatical; breaks ISLET 3 (pre=78≠82) |
| K4 | @647 | «gouvernement» | 5-mer absent (78→52); «pas m ne» ungrammatical under all orders |
| K5 | @1077 | «gouvernement» | 5-mer absent (78→64) |
| K6 | @1542 | «gouvernement» | 5-mer absent (78→43) |
| K7 | @521 | «gouvernement» | 77 followed by 06, not 78 |

**Net: the "gouvernement" thread has ZERO remaining windows.** The 5-mer existed
twice (@1180, @1351); @1351 resolved to the islet parse, @1180 killed above.
No 77-78 window anywhere else even has the 5-mer shape.

## Survivors (with French-syntax justification)

- **R-isl @1180** («le [78] ne ment»): board-consistent, «ne ment» era-good
  («il ne ment pas», RdM 1841-Q2); LEAD-weak, incomplete (trailing 06+«est»,
  leading «est [37]»).
- **77="le"+78 frames** @7, @213, @1542, @521: structurally alive, 78/06/91/43
  unidentified. No French verdict possible yet — these are conditioner items.
- **W3 @647** («le [78] pas m ne»): OPAQUE — no grammatical French parse found
  under any board-consistent assignment. Flagged: either 52≠"pas" locally
  (expensive — 52 is STRONG) or the window needs re-segmentation.
- **W4 @1077** («[48] le [78] qui [06] pas»): blocked on 48 (UNIDENTIFIED) and
  06 (pre=64, not islet). The «qui…pas» frame wants «ne» in the 06 slot —
  worth testing if 06 has a «ne»-allophone (48="ne"-allophone was killed,
  but 06 was never tested for it).

## What this means for the 77/78 fork and 77="gouv"

1. **77="gouv" (LEAD) should be DEMOTED or KILLED.** Its entire evidential base
   was the "gouvernement" 5-mer; both 5-mer windows are now resolved against
   it (@1351 → islet, @1180 → killed above). No remaining window supports
   77="gouv". Recommendation: red-team adjudication for demotion to
   disfavored or kill. (This agent makes no status change — ≥2-leg rule.)
2. **The 78={ver,er} fork is UNAFFECTED structurally** — but note the round-9
   Frenchman result stands: er|ne productive (52 tokens/22 types) vs ver|ne
   zero genuine (10.4×, p=3.2e-11). Combined with this re-read (no surviving
   «ver»-internal window), the fork leans (c) 78="er". The fork itself is not
   resolved — 78's value at @1180/@1351 remains unidentified.
3. **06="ent" iff pre=82 (ISLET 3) is STRENGTHENED** — it is the surviving
   reading at both 5-mer windows, and no window required 06="ent" outside
   the islet (W2's «gouvernent» was killed partly on islet-break).
4. **New lead for the conditioner:** test whether 06 has a «ne»-allophone for
   the W4 @1077 «qui [06] pas» slot.

## Methodology notes

- All 77–78 adjacencies enumerated programmatically from the repaired parse
  (7 sites); the 5-mer 77-78-94-82-06 verified to exist at exactly @1180 and
  @1351 and nowhere else.
- Every French grammaticality claim above is either corpus-attested (table)
  or marked structural (5-mer absence) / grammatical (verb+«est»).
- The «il ne ment pas» attestation (RdM 1841-Q2) is the single most valuable
  corpus hit: it licenses the R-c/R-isl «ne ment» core as era-good French.
- Nesselrode v8 was NOT used for «ment» queries (OCR word-split caution);
  the attestation comes from clean RdM text.
