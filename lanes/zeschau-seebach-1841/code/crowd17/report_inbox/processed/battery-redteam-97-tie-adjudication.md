# Battery report: `redteam-97-tie-adjudication`

Date: 2026-10-09. Worker: battery worker (subagent, supervisor-dispatched).

## Bar (verbatim, pre-registered)

> "battery gathers only (§7); the class decision is red-team venue; package delivered to the red-team docket"

Restated as numbered pass/fail clauses (before testing):

- **C1:** This battery makes no class decision. The INF/NOM tie is not resolved, named, promoted, or killed here (§7). PASS iff the report contains no class verdict.
- **C2:** The package carries all four required components, byte-exact on the repaired stream: (a) the leg tally with @-offsets, (b) the @525 clean NOM parse, (c) the pour-window discriminator, (d) the @566 13-blocker status. PASS iff all four are present and every number traces to the stream.
- **C3:** The package is delivered to the red-team docket through the pipeline intake (`code/crowd17/report_inbox/`, which the supervisor ingests); the red-team adjudication queue is untouched. PASS iff the report is filed and the class decision is explicitly deferred.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`). Asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, and the red-team adjudication queue untouched. No numbers invented. All @-offsets 0-based.

Adopted (not re-litigated): §7 standing values (00='pour' A9, 86 INF-class A9, 46='que' banked, 47='ce' A4 promoted, 59='est' provisional, 81-nominal at @524 battery-grade window-level from `nom-97-526-adverb`, 80 verb-frame A8, 76 noun-class, 37/32/42 predicative A1); `frame-97-profile` (97 infinitive-class, class-level PROMOTE, 2026-10-08 — standing, not downgraded); `val-97-verb-test` (97 finite-verb KILL; INF/NOM NULL tie, 2026-10-09); `nom-97-526-class` (parent report: @525 C1 PASS, C2 FAIL, verdict NULL, 2026-10-09); `noun-97-568` (the "97 13 76" wall, 2026-10-09). Canonical-stream caveat stands (row a3_00/a3_02 offsets unvalidated).

## Package component (a): leg tally with windows

Re-derived n(97) = 10 at 0b **[2, 94, 288, 299, 525, 566, 588, 751, 1412, 1823]** (matches `frame-97-profile`). Successors (in position order): [51, 46, 09, 86, 47, 13, 41, 40, 69, 00] — all distinct, ×1 each. Predecessors: [00, 81, 00, 40, 81, 80, 00, 02, 16, 00].

**INF arm — 6 positive legs (adopted from `val-97-verb-test`, byte-exact re-verified):**

1. @2 (row a1_00): `09 00 [97] 51 47` — "pour [97]", bare, no article.
2. @288 (row a2_03): `28 00 [97] 09 64` — "pour [97]", bare, no article.
3. @588 (row a3_02): `14 00 [97] 41 41` — "pour [97]", bare, no article.
4. @1823 (row a8_10): `09 00 [97] 00 86` — "pour [97]", bare, no article.
5. @1823 parallel (row a8_10): `00 [97] 00 86` (0b@1822–1825) — "pour 97 pour 86" with 86 in explicit infinitive form alongside 97.
6. @94 que-valency (row a1_02): `98 81 [97] 46 29` — "dire que"-shaped que-valency (precedent: 33-46 ×2, A10), conditional tail.

**NOM arm — 4 clean windows (adopted, re-verified):**

1. @525 (row a3_00): `81 [97] 47 44 59 37` — "[81] [97-noun]" appositive NP + A1 copula "ce(47) [44] est(59) [37]". C1 PASS from parent (`nom-97-526-class`); see component (b).
2. @94 (row a1_02): `81 [97] 46 29 85` — "[81] [97-N] que [relative]" (81-nominal left, que successor).
3. @566 (row a3_02): `80 [97] 13 76` — "[80-V] [97-N]" object (80 verb-frame A8). 13-blocker: see component (d).
4. @1412 (row a7_07): `16 [97] 69 74` — "[16-INF] [97-N]" object.

**Unforced (fenced, not counted):** @299 `40 [97] 86` ("40 97 86" hapax, fenced); @751 `02 [97] 40` ("02 97 40", sole leg conditional on fenced 02='fait' — `adv-02-858` NULL).

**Armed summary for adjudication:** INF 6 positive legs, zero contradictions. NOM 4 clean favoring windows, universal consistency. Neither forced nor killed. Tie is genuine at battery grade (`val-97-verb-test` NULL — standing, not re-decided here).

## Package component (b): the @525 clean NOM parse

Byte-exact window, 0b@520–532 (row a3_00):
`91 @520 | 77 @521 | 06 @522 | 55 @523 | 81 @524 | 97 @525 | 47 @526 | 44 @527 | 59 @528 | 37 @529 | 64 @530 | 26 @531 | 32 @532`

Parse under noun-97: "[81-nominal] [97-noun] ce(47) [44] est(59) [37]" — appositive NP (81-nominal @524, battery-grade window-level; re-verified n(81)=14 with predecessors 55×6/77×4/43/98/39/08×1) + the A1 copula clause "ce [44] est [predicative-37]".

Ungranted-assumption audit (from parent, re-verified counts): the sole ungranted assumption is noun-97 itself. No 13-class dependency at this window (unlike @566).

Parent verdict on this window (`nom-97-526-class`, adopted): C1 (clean parse) PASS; C2 (class promote from @525 alone) FAIL — blocked by the standing class-level infinitive verdict (`frame-97-profile`), the symmetric 10-window tie, and the pour-window discriminator; report verdict NULL. The class question stays with the red team.

## Package component (c): the pour-window discriminator

00 successor census, re-derived byte-exact (n(00)=55):
- Bare takes: 86×12, 33×8, 66×7, 92×6, **97×4**, 36×3, 34×1, 13×1, 20×1, 64×1, 98×1, 67×1, 44×1
- Article-mediated: 11×4 ("pour la…" @76/@378/@1287/@1405 per `val-97-verb-test`)
- "pour que": 46×4 (@106/@545/@1545/@1680)

The discriminator claim (from `nom-97-526-class` / `val-97-verb-test`, NOT decided here): 00's bare takes are verb-frame cells (86/33/92/66/97), while 00's nominal takes are article-mediated (00→11×4). Zero 00→bare-noun windows stream-wide. Under this pattern the four "pour [97]" windows (@2/@288/@588/@1823) read INF-favoring.

Status for the red team: the pattern is reported with the raw census above (the small bare takes — 36×3, 34/13/20/64/98/67/44×1 — are unclassified in the battery record). The formal battery test is separately queued as **`pour-97-noun-discriminator`** (P3, status: queued) — bar: a single verified 00→bare-noun take collapses the discriminator and gives NOM-97 four windows. Cited here as in-flight; NOT duplicated.

## Package component (d): the @566 13-blocker status

Byte-exact window, 0b@565–569 (row a3_02): `80 @565 | 97 @566 | 13 @567 | 76 @568` (tail: `45 @569`).

The NOM leg at @566 is "[80-V] [97-N]" object — but 97's successor is **13**, the unresolved 13-class problem. The "97 13 76" wall (`noun-97-568`, 2026-10-09, adopted): C1 PASS via the infinitive arm (determiner-97 kill-grade dead; finite verb standing-killed); C2 FAIL — 0/10 wall-killed uniform-13 candidates revive under "[97-INF] [13-X] [76-N]", and the wall is class-independent (holds under nominal-97 too). The wall's decisive-discriminator status stands.

Blocker status for the red team: 13's class is battery-unresolved. The residual 13 space is explicitly fenced to red-team venue (sub-lexical-13 route: `letter-13-verdicts`, queued P3; the §7 split: `split-13-redteam`, queued P2 — both from `noun-97-568`). The @566 NOM leg therefore carries a 13-class dependency the battery grade cannot clear. Cited here as a package component, not decided.

Also cited (separately queued, not duplicated): **`nom97-525-inf-rival-kill`** (P3, status: queued) — kill-seeks the INF rival at @525 specifically.

## Per-clause pass/fail

1. C1 (no class decision in this report): **PASS.** The tie is not named, promoted, or killed. `frame-97-profile` (INF, class-level) and `val-97-verb-test` (NULL tie) stand untouched; no verdict downgraded.
2. C2 (all four components present, byte-exact): **PASS.** Leg tally (10 positions, 6 INF legs, 4 NOM windows, 2 unforced), @525 parse, pour-window discriminator (full census), @566 13-blocker status — all re-derived from the repaired stream, none invented.
3. C3 (package delivered to the red-team docket; adjudication queue untouched): **PASS.** Report filed at `code/crowd17/report_inbox/battery-redteam-97-tie-adjudication.md` (supervisor ingest intake); the red-team adjudication queue was not touched. The class decision is deferred to the red team, with the live tie state fully attached.

## Verdict: PROMOTE

The package is complete: leg tally, @525 NOM parse, pour-window discriminator, and @566 13-blocker status are all gathered, byte-exact, and delivered to the docket. The class decision is red-team venue. Adverses: none listed.

Standing-rule compliance: §7 intact (no polyvalence declared, banked/promoted/granted/provisional values untouched, kills and holds unreopened); `canonical.py` never used; R5005, sealed gates, and the red-team adjudication queue untouched; no numbers invented; canonical-stream caveat (rows a3_00/a3_02 offsets unvalidated) carried forward for the red team's adjudication.

## Bookkeeping

- Report: this file.
- Queue: `redteam-97-tie-adjudication` → `status: verdict`, `result: promote`, 2026-10-09 (update follows; pre-write assert: was queued/verdictless; temp-file + rename; own entry only; no downgrade).
- Lock `locks/redteam-97-tie-adjudication.lock` held (supervisor-created reservation), deleted on completion (verified gone).
