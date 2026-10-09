# Battery verdict: frame-43-pour-census

- Target: `frame-43-pour-census`
- Claim: The 4 -> 2 discrimination (suite/maniere killed, condition/mesure survive) holds across ALL of 43's 'pour' windows, not just @1126
- Worker: battery worker frame-43-pour-census (worker-43pourcensus-a170b68c)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py. 1,847 pairs / 96 types re-verified in-session. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. No data invented. @-offsets are 0-based stream indices (this battery family's convention).
- Lock: created `code/crowd17/next-token/locks/frame-43-pour-census.lock` on start, deleted on completion. No prior/fresh lock existed.

## 1. Bar (verbatim from battery-queue.json)

"confirm-or-reject the 4 -> 2 at every 43-00 window (@244 '43 pour [66]', @1126 '43 pour [86-INF]', @1544 '43 pour que [70]') plus the second 43-98 window (@439 '43-98-80'); record per-window survivor sets"

Numbered clauses (pre-registered before testing; not modified after seeing data):
- **C1:** PASS iff at @1126 ("43 pour [86-INF]") the pour+INF frame kills suite and maniere while admitting condition and mesure (4 -> 2 confirmed at this window).
- **C2:** PASS iff at @1544 ("43 pour que [70]") the discrimination reads 4 -> 2 under the government reading (suite/maniere killed, condition/mesure survive); record the boundary alternative (non-discriminating, 4 -> 4) without pre-empting queued frame-43-pour-que-1544's boundary adjudication.
- **C3:** PASS iff at @244 ("43 pour [66]") the discrimination confirms 4 -> 2; else FENCE with stated cause if 66's class blocks the pour-INF government (66 value-open per the listed adverse).
- **C4:** PASS iff at @439 (43-98-80, second 43-98 window) a per-window survivor set is recorded for the candidate set {suite, condition, maniere, mesure}.

Note on scope: "survive" in the claim means survives THE POUR FRAME at that window, not survives globally. Globally, the noun-43 survivor set is EMPTY per battery-cond-mesure-43full (NULL, 2026-10-09: condition and mesure both fail par-43 x2 and @21 at kill grade; battery-par43-adverbial-attestation PROMOTE, 2026-10-09, closed the par-43 escape). This census tests frame-local discrimination only, per the bar's "per-window survivor sets".

## 2. Method

- Read BATTERY-PROTOCOL.md first. Re-derived all four windows from the repaired stream in-session (byte-verified below).
- Adopted as premises, never re-litigated (protocol §5 — never downgrade an existing verdict):
  - battery-frame-43-la-52-37 (NULL, 2026-10-08): 43->00 x3/16 (19% pour-government); 43->98 x2/16; continuation-A discrimination 4 -> 2 at @1126.
  - battery-noun-43-discriminator (KILL, 2026-10-08): the 'pour que' discriminator — under the government reading "condition pour que" ✓, "mesure pour que" ✓, "suite pour que" ✗, "maniere pour que" ✗; "suite" killed at kill grade (@21 forces 43!="suite"); "maniere" dead (fails par-43 and pour-que).
  - battery-noun-43 (NULL, 2026-10-09): 43 census n=16; @1544 byte-reading adopted.
  - The candidate set {suite, condition, maniere, mesure} is adopted from the discriminator battery; not re-derived. No open group named (66/70/98/52/37/32/80 untouched).
- Grammaticality judgments below are the discriminator batteries' standing findings applied per window, not new litigation.

## 3. Window-level evidence (all byte-traced from the repaired stream)

**@1126 (row a6_07) — the reference window:**
`[1118]70 [1119]12 [1120]06 [1121]14 [1122]06 [1123]11 [1124]52 [1125]37 [1126]43 [1127]00 [1128]86 [1129]52 [1130]37 [1131]86 ...`
"43-00-86" = "[43] pour [86-INF]" (00='pour' A9 leg-1 class-level; 86=INF-class A9 class-level). Adopted from frame-43-la-52-37 clause (b): "la suite pour [inf]" not idiomatic; "la maniere pour [inf]" not idiomatic ("maniere de"); "les conditions pour [inf]" idiomatic; "des mesures pour [inf]" idiomatic. Survivor set: {condition, mesure} — 4 -> 2 confirmed at this window. Byte reading verified byte-identical to the 2026-10-08 report.

**@244 (row a2_02):**
`[236]98 [237]41 [238]17 [239]11 [240]26 [241]12 [242]16 [243]56 [244]43 [245]00 [246]66 [247]91 [248]32 [249]44 [250]94 [251]65 [252]63 [253]00`
"43-00-66" = "[43] pour [66]". 66 value OPEN (listed adverse; 66 profile n=19: predecessors 00 x7 — "pour 66" occurs 7x stream-wide — successors 98/73 x3; battery-poly-66-split returned NULL; adv-66-conditional is queued). 66 carries NO INF-class grant, so the pour+INF government the discrimination requires is not established at @244. The byte-identical string "43 00 [follower]" does NOT carry the discrimination: at @1126 it is the INF class of the follower (86, granted) that makes the frame discriminating, and 66 is not 86-class. Survivor set: UNTESTABLE at battery grade — fenced, stated cause: 66 value open; conditional only: IF 66 proves INF-class, the discrimination would carry 4 -> 2 identically to @1126.

**@1544 (row a8_00):**
`[1536]62 [1537]06 [1538]21 [1539]62 [1540]93 [1541]88 [1542]77 [1543]78 [1544]43 [1545]00 [1546]46 [1547]70 [1548]12 [1549]94 [1550]92 [1551]45 [1552]23 [1553]99`
"43-00-46-70" = "[43] pour que [70-prenne]" (00+46 "pour que"; 70-12-94 = "prenne" subjunctive, battery-promoted, per battery-noun-43). Under the government reading ("[43] pour que [subj]"), adopted from noun-43-discriminator: condition ✓, mesure ✓, suite ✗, maniere ✗ — 4 -> 2. Under the boundary alternative ("...78 43. Pour que prenne 92...", purpose clause after a clause-final noun), all four pass — 4 -> 4, non-discriminating. The boundary adjudication is owned by queued frame-43-pour-que-1544 (priority 3); this battery does not decide it. Survivor set: {condition, mesure} under government; {suite, condition, maniere, mesure} under boundary — recorded, fenced pending the queued adjudication.

**@439 (row a2_09) — second 43-98 window:**
`[431]86 [432]29 [433]82 [434]16 [435]78 [436]63 [437]45 [438]46 [439]43 [440]98 [441]80 [442]50 [443]78 [444]41 [445]10`
"46-43-98-80" = "que [43] [98] [80-verb]". No pour frame at this window. "que"+noun needs a boundary for all four candidates (adopted from noun-43-discriminator) — 4 -> 4, non-discriminating. 98-80: 98 value OPEN (n=40), 80 is a granted verb-frame (A8); "43 [98] [80]" cannot discriminate noun values. Survivor set: {suite, condition, maniere, mesure} (all four pass only under a boundary parse) — recorded, fenced with stated cause (98 open, 80 verb-frame).

## 4. Per-clause pass/fail

- **C1 (@1126): PASS.** 4 -> 2 confirmed: suite and maniere killed by the pour+INF frame; condition and mesure admitted. (Survival is frame-local; global standing per §1 note.)
- **C2 (@1544): CONDITIONAL PASS.** 4 -> 2 under the government reading (adopted discriminator finding); 4 -> 4 under the boundary reading; boundary adjudication left to queued frame-43-pour-que-1544. Not decided here.
- **C3 (@244): FENCED.** Untestable at battery grade — 66 value-open, pour-INF government not established; the byte string "43 00 [follower]" alone does not carry the discrimination. Stated cause recorded.
- **C4 (@439): PASS (recorded).** 4 -> 4, non-discriminating; 98-80 fenced (98 open, 80 verb-frame A8).

## 5. Adverses answered

- **"@439's 98-80 (verb-frame follower, not 98-39)": ANSWERED, fenced with stated cause.** 98 value open; 80 granted verb-frame (A8). The follower cannot discriminate noun values; "que 43" needs a boundary for all four. Recorded 4 -> 4.
- **"66/70 followers open": ANSWERED, fenced.** 66 open (n=19; poly-66-split null; adv-66-conditional queued) — blocks the @244 government claim. 70 open-ish (provisional "pre"; "prenne" compositional, battery-promoted) — does not block the @1544 government reading's discrimination, which lives in "pour que + subj" government, not in 70's exact value.
- **"feeds (does not duplicate) the parallel noun-43-discriminator naming bar": ANSWERED.** The discriminator's verdicts are adopted wholesale (suite kill, maniere dead, pour-que positive set); no naming attempted here. The 'pour que' boundary question is owned by queued frame-43-pour-que-1544; the 66 class question by queued adv-66-conditional / the red team's poly-66 docket.

## 6. Verdict: NULL

The claim "holds across ALL of 43's 'pour' windows" is neither confirmed nor falsified at battery grade:
- @1126: 4 -> 2 confirmed (C1 pass).
- @1544: 4 -> 2 under the government reading; undecided pending queued frame-43-pour-que-1544 (C2 conditional).
- @244: untestable at battery grade (66 open) — fenced, not failed (C3 fence).
No window forces the claim false (kill grade not met: an open follower and an undecided boundary are fences, not falsifications). No standing verdict is contradicted or downgraded: suite/maniere kills stand; cond-mesure-43full's empty global survivor set stands (this census is frame-local); par43-adverbial-attestation's promote stands; no red-team ruling exists on 43's value. §7 intact. R5005, sealed gates, red-team queue untouched.

## 7. Follow-up targets (null regenerates work)

1. `pour66-class-rerun` (P3) — re-run C3 of this census once 66's class is named: coordinate with queued adv-66-conditional (do not duplicate its bar) and battery-poly-66-split's null finding ("pour-governed non-finite" arm). Bars: "confirm-or-reject the 4 -> 2 at @244 iff 66 is named with an INF-compatible class; if 66 is verb-shaped or otherwise, record @244 as permanently non-discriminating and close the census." Evidence: @244 "43 00 66 91" (re-derived above); 66 n=19, "pour 66" x7 stream-wide; @1126 reference. Adverses: 66 value open; polyvalence barred at battery level (67 sole); this battery's C1/C2/C4 not re-run.
2. `pour1544-post-adjudication-rerun` (P3) — re-run C2 of this census once queued frame-43-pour-que-1544 adjudicates @1544 boundary-vs-government: if government, the census closes 4 -> 2 at @1126 AND @1544 (@244 modulo 66); if boundary, @1544 drops out of the census permanently and the claim's "ALL windows" reading is rejected at battery grade. Bars: "record the adjudicated @1544 survivor set and the census's terminal claim verdict (promote/kill) with no new grammaticality litigation." Evidence: this report §3 @1544; frame-43-pour-que-1544's verdict when it lands. Adverses: none new (do not re-litigate 'pour que' government).
