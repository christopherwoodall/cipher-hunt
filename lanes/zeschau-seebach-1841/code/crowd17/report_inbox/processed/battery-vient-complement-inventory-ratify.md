# Battery verdict: vient-complement-inventory-ratify

- Target id: `vient-complement-inventory-ratify`
- Claim (RED-TEAM INPUT): consolidate the {de, pour, elided clitic} inventory across all 40 vient windows (successors 83x5, 82x3, 00x3); if any inventory member breaks, 98-76 and 98-65 both re-open. Evidence only, no adjudication.
- Date: 2026-10-09
- Worker: battery worker (subagent cf08b50f-d977-43a0-a35e-038e0b275c2b)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

Terms (ASD-STE100): "inventory" = the standing set of complement types that 98 ('vient', battery-promoted) takes. "member" = one complement type: 'de' (via 83), 'pour' (via 00), elided clitic (via 82='m'). "break" = a member is falsified at battery grade at one or more of its windows. "residual" = a window whose complement lies outside the inventory (98-76, 98-65, both fenced). "re-open" = a fenced residual returns to active candidate status for a complement reading.

## Bar (verbatim, pre-registered before testing)

"input package for the red team"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** The 'de' member (83x5) is byte-consolidated: each of the 5 windows' parses graded under current standing values.
2. **C2:** The 'pour' member (00x3) is byte-consolidated under current standing values.
3. **C3:** The elided-clitic member (82x3) is byte-consolidated under current standing values.
4. **C4:** Any member break is documented with its drivers, and the brief's consequence rule (98-76 and 98-65 re-open) is applied as instructed — as a package statement, not an adjudication.
5. **C5:** The package is delivered for red-team adjudication; no value is adjudicated and no standing/red-team verdict is contradicted or downgraded.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/vient-complement-inventory-ratify.lock` on start (agent id + 2026-10-09T12:04Z); no stale lock was present.
2. Re-derived the repaired stream byte-exact per `repair_parse.py`. All @-offsets below are 0-based pair indices.
3. Full 98 census re-derived in-session: n(98)=40, byte-exact; successor profile: 83x5, 82x3, 80x3, 98x3, 00x3, 56x2, 20x2, plus 19 singletons (76, 51, 19, 81, 41, 92, 65, 53, 96, 48, 12, 78, 86, 55, 15, 62, 24, 60, 39). Matches the brief's parenthesized counts.
4. Adopted, not re-litigated (§7): 98='vient' (battery PROMOTE, vient-98-name, 2026-10-08; 37/40 windows consistent); 82='m' (pencil ground truth); 96='par' (granted); 46='que' (pencil); 64='qui' (granted); 29='er' (pencil); 00='pour' (A9, leg-1 class-level); 86 INF-class (A9, class-level); 80/89 verb-frames (A8); 87='ce' (promoted); 47='ce' (A4); 17='fois' (promoted); 67="et"/"veut" sole polyvalence with positional rule. New since vient-98-name: `form-56-1627` PROMOTE (2026-10-09: 56 is 3sg finite, "crée"-shaped, at @932/@1626, bare-X inflection model); `de83-932-gate` NULL-with-kill-grade-gate (2026-10-09: 83≠'de' at the @930 window at kill grade; 83's value otherwise open); `frame-vient-parvenir` KILL (the source of the 83='de' lead is dead); `fin-88-1541-parallel` KILL (88 non-finite at @1541; does not touch this inventory).

## Window-level evidence

### Member 'de' — 83x5

- **@227** (`89 61 96 87 46 [98] 83 82 96 21 60 71`, row a2_01): "…par(96) ce(87) que(46) vient [83] m(82) par(96) [21]…". Byte-identical formula 5-gram `98 83 82 96 21` (third=60). Under 83='de': "que vient de me par[ler]" — the only grammatical reading of the 5-gram (82='m' banked, 96='par' banked). **Clean.**
- **@1060** (`45 23 77 84 09 [98] 83 82 96 21 62 18`, row a6_05): byte-identical 5-gram (third=62): "…on(84)… vient de me par[21]…". **Clean.**
- **@1783** (`19 48 74 65 23 [98] 83 82 96 21 68 47`, row a8_09): byte-identical 5-gram (third=68): "…vient de me par[21]…". **Clean.**
- **@897** (`76 01 98 82 14 [98] 83 86 16 92 67 16`, row a5_06): "[01] vient m(82) [14] vient [83] [86] [16]…". Under 83='de': "vient de [86-inf]" (86 INF-class, A9). **Clean** (conditional on 86 infinitive, class-granted).
- **@930** (`17 61 96 48 82 [98] 83 56 69 26 00 33`, row a5_09): "…m(82) vient [83] [56] [69] [26] pour(00) [33]". **BROKEN at kill grade.** The 56 at this window is 0-based @932 — exactly `form-56-1627`'s W1, promoted as 3sg finite ("crée"-shaped) on 2026-10-09. `de83-932-gate` (2026-10-09) closed this gate at kill grade: with 56 finite, 83='de' gives "*vient de crée" — 'de' does not govern a finite verb in 1841 French. §7 bars a polyvalence rescue. No alternative 'de'-parse exists (no licensed boundary, no elided infinitive). The 'de' member is falsified at this window under two standing battery verdicts.

Member 'de' status: **4/5 clean, 1/5 broken at kill grade.** The break is new since `vient-98-name` (2026-10-08), which had fenced @930 only as a complement-class residual on the then-open question of 56's class. `form-56-1627` resolved that question.

### Member 'pour' — 00x3

- **@1373** (`30 82 16 91 67 [98] 00 86 29 89 84 92`, row a7_05): "…et(67) vient pour(00) [86]er(29) [89]". "vient pour [86]er" — clean (00='pour' promoted, 86 INF-class). **Clean.**
- **@1601** (`80 67 77 81 82 [98] 00 44 70 39 11 92`, row a8_02): "[81] m(82) vient pour(00) [44] pre(70) [39]". Adopted from vient-98-name clause 6 (resolved): proclitic 'me' before finite 'vient' ("l'idée me vient" shape) + 'pour' + complement; conditional on 81 noun-like and 44 complement-like (both open). **Clean-conditional; no break.**
- **@1137** (`24 77 86 20 62 [98] 00 98 78 62 16 29`, row a6_08): "[62] vient pour(00) vient(98) [78] [62]". The second 98 is finite ('vient' promoted) — "pour [vient-fin]" is ungrammatical; complement of 'pour' needs infinitive 'venir' (inflectional alternation = red-team act per §7). **Inherited fence** from vient-98-name clause 4 (same fence as @1139 'pour [98]'). The member 'pour' is not falsified — the window needs a red-team inflectional ruling, not a different preposition.

Member 'pour' status: **no break.** 1/3 clean, 1/3 clean-conditional, 1/3 inherited fence (red-team venue).

### Member 'elided clitic' — 82x3

- **@19** (`45 91 53 17 64 [98] 82 43 29 47 33 55`, row a1_01): "…fois(17) qui(64) vient m(82) [43]er(29) ce(47)". "qui vient m'[43]er" — elided clitic + infinitive shape (82='m' pencil GT, 29='er' pencil GT). **Clean.**
- **@124** (`60 90 19 58 66 [98] 82 48 11 02 26 32`, row a1_06): "…vient m(82) [48] la(11) [02]…". The clitic arm holds ("vient m'…"); the complement [48] is the inherited 48-residual (vient-98-name: 48 is verb-stem frame A7-L2, no 'er' here). **Member holds; complement fenced as 48-residual. No break.**
- **@894** (`86 06 77 76 01 [98] 82 14 98 83 86 16`, row a5_06): "[01] vient m(82) [14] vient [83]…". "vient m'[14]" — conditional on 14 vowel-initial (open). Adopted from vient-98-name (subject attribution 14 vs 01 fenced as underdetermined — does not break the frame). **Clean-conditional; no break.**

Member 'elided clitic' status: **no break.**

### Other successors (outside the three-member inventory, catalogued not adjudicated)

- 80x3 (@440, @767, @1661): "vient [80]" under the A8 verb-frame grant (conditional pass per vient-98-name; 80's class/value is red-team venue in `poly-80-docket`).
- 98x3 (@1073, @1145, @1660): doubled-98, fenced with stated cause (vient-98-name clause 2; systematic reduplication, red-team venue).
- 56x2 (@192, @1325): "[X] vient [56]" — subject-side windows, not complement inventory.
- 20x2 (@702 "n'vient" fenced; @838 underdetermined), singletons neutral or fenced per vient-98-name.
- **98-76 (@12)**: fenced as second complement-class residual (`inv-98-76-12`, verdict null, 2026-10-09).
- **98-65 (@511)**: fenced as first complement-class residual (`vient-65-complement`, verdict null, 2026-10-09).

## Per-clause pass/fail

1. **C1 PASS** — 'de' member byte-consolidated: 4/5 windows clean (@227/@897/@1060/@1783, including the ×3 byte-identical formula); @930 broken at kill grade under standing verdicts (drivers: `form-56-1627` PROMOTE + `de83-932-gate` kill-grade gate closure).
2. **C2 PASS** — 'pour' member byte-consolidated: no break (1 clean, 1 clean-conditional, 1 inherited red-team fence at @1137).
3. **C3 PASS** — elided-clitic member byte-consolidated: no break (1 clean, 1 clean-conditional, 1 inherited 48-residual at @124).
4. **C4 PASS** — the @930 member break is documented above with its drivers. Per the brief's consequence rule, **98-76 and 98-65 both re-open**: both fences (`inv-98-76-12`, `vient-65-complement`) were predicated on the inventory being intact, and the 'de' member — the inventory's most frequent — is no longer uniform. This is a package statement for the red team, not an adjudication: the red team may (a) accept the break and re-open the residuals, (b) rule 83 window-conditioned at @930 (their §7 act), or (c) overturn one of the two driving battery verdicts.
5. **C5 PASS** — package delivered; no value adjudicated. Adverses answered: this is a red-team input package only; the red-team adjudication queue was not touched, no adjudication was performed, and no standing or red-team verdict was contradicted or downgraded (`form-56-1627`, `de83-932-gate`, `frame-vient-parvenir`, `vient-98-name`, `inv-98-76-12`, `vient-65-complement` all used as premises, none overturned). §7 intact — no polyvalence declared.

## Verdict: PROMOTE (evidence package delivered; no value named, no adjudication claimed)

Headline for the red team: the 'de' member of the vient complement inventory is **4/5 clean, 1/5 broken at kill grade** (@930: "vient de crée" is ungrammatical under the now-promoted 3sg-finite 56 at the same window). The 'pour' and elided-clitic members show no break. Per the brief's stated consequence rule, the member break re-opens 98-76 and 98-65. Canonical-stream caveat stands (row offsets unvalidated except where gloss-anchored).

## Bookkeeping

- Queue: `vient-complement-inventory-ratify` queued → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/vient-complement-inventory-ratify.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
