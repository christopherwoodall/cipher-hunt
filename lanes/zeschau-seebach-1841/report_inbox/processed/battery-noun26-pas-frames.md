# Battery report: noun26-pas-frames

**Target:** noun26-pas-frames — "26 is verb-class: '26 30' x4 = '[verb] pas' kills noun-26 unconditioned"
**Date:** 2026-10-08
**Worker:** a70c604b-d023-4828-b6ba-7b237db15f70
**Lock:** created 2026-10-08T07:26:55Z; no stale lock existed (locks/ held only NOTE.md and fork-78-45-adjudication.lock).
**Verdict: PROMOTE** (frame-level; claim refined per bar clause (e) — see below)

## Bar (verbatim, pre-registered before testing)

"(a) all four '26 30' windows re-derived on the repaired stream; (b) 30 = 'pas'-negation in each (no rival parse); (c) noun-parse of '26 30' shown ungrammatical per window, or a clause boundary fenced with stated cause; (d) 'ne'-audit: 94/12 positions within +/-15 recorded per window (absent 'ne' does NOT fail the bar, but the bare-'pas' 1840s tension is stated and flagged to ne-alone-02-74); (e) @1559's 'la [26]' parsed — state exactly how 'la [26] pas' reads under the winning class, or record @1559 as the residual that forces the positional rule"

Bar copied from battery-queue.json before any stream testing (queue read → lock created → analysis run).

## Bar restated as numbered pass/fail clauses

1. All four "26 30" windows (@654/@991/@1249/@1559) re-derived on the repaired 1,847-pair stream.
2. 30 = "pas"-negation in each of the four windows (no rival parse).
3. Per window: the noun-parse of "26 30" is shown ungrammatical, or a clause boundary is fenced with stated cause.
4. "ne"-audit: every 94/12 within ±15 of each 26 recorded; absent "ne" does not fail; the bare-"pas" 1840s tension is stated and flagged to ne-alone-02-74.
5. @1559's "la [26]" parsed: state exactly how "la [26] pas" reads under the winning (verb) class, or record @1559 as the residual forcing the positional rule.

## Method

- Stream: repaired 1,847-pair parse — data/upstream-ct_R5005.txt + code/side-keyhunt/repaired_offsets.json, parsed exactly like code/side-keyhunt/repair_parse.py (byte-exact upstream tokenization). canonical.py never used. R5005 never touched.
- Offset convention: lane report-@ = 0-based stream index − 1 (finder convention; verified: the four "26 30" bigrams fall at 0-based 655/992/1250/1560).
- Windows shown ±8; ne-audit and wide context ±15; row labels recorded per position.
- Standing inputs: 11="la" (banked GT), 17="fois" (granted), 30="pas" (battery-promoted, pending ratification), 94="ne" (battery-promoted, pending ratification), 12="n"/48="e" (battery-promoted letters), 00="pour" (A9), 67 et/veut sole polyvalence with positional rule, 23~26 split (A2). 76/49/24/06/60 values open. Canonicality caveat stands.

## Window-level evidence

### @654 (0-based 655; row a4_02; ±8: "77 78 52 82 94 76 49 24 [26] 30 03 62 16 00 86 50 80")

- Bigram "26 30" gapless; junction mid-row (26:a4_02, 30:a4_02 — no row boundary).
- Pre-26 = 24 (open; not "la"). Post-30 = 03.
- ne-audit: 94 at @650 (d−4, four groups left). Surface "82 94 76 49 24 26 30" reads "…[82=m, previous-clause tail] | ne [76] [49] [24] [26-verb] pas". Three groups between "ne" and the verb: clitic-chain-compatible (French admits stacked clitics between "ne" and the verb, e.g. "ne le lui en [V] pas"); 76/49/24 values open, so compatibility only, not a proved parse.
- Noun-parse: "[24] [noun] pas" — a bare noun directly followed by the negation particle "pas" is ungrammatical; no article, no clause boundary available (continuous formula row). Excluded.

### @991 (0-based 992; rows a6_01..a6_02; ±8: "01 24 89 48 01 76 49 24 [26] 30 03 60 67 11 96 82 33")

- "26 30" gapless; 6-gram "76 49 24 26 30 03" byte-identical to @654 (verified True) — one frame-type, two instances, counted once per the finder de-dup.
- Pre-26 = 24; post-30 = 03.
- ne-audit: NONE — no 94 and no 12 within ±15. Bare "pas" (1840s tension stated; does not fail per bar; flagged to ne-alone-02-74).
- Noun-parse: same exclusion as @654 ("[noun] pas" ungrammatical; junction mid-row a6_01; no boundary).

### @1249 (0-based 1250; rows a7_01..a7_02; ±8: "87 11 00 33 16 00 67 46 [26] 30 06 65 46 01 61 31 29")

- "26 30" gapless; junction mid-row a7_02.
- Left: "00 67 46" = "pour et/veut que". 67's follower is 46="que" (not infinitive-shaped), so 67="et" by the sole-polyvalence positional rule. Parse: "…pour dire [16], et que [26-subjunctive] pas [06]…" — clean under 26=verb.
- Pre-26 = 46 ("que"); post-30 = 06.
- ne-audit: NONE within ±15. Bare "pas" (tension flagged).
- Noun-parse: "que [noun] pas" ungrammatical. Excluded.

### @1559 (0-based 1560; rows a8_00..a8_01; ±8: "23 99 13 93 61 40 17 11 [26] 30 06 60 71 50 29 24 74"; ±15 left reaches "00 46 70 12 94" @1544–1548)

- "26 30" gapless; junction mid-row a8_01.
- Pre-26 = 11 = "la" (BANKED article). 26 is FORCED nominal here: "40 17 11 26" = "e fois la [26]" (absolute "une fois la [N]", cf. @239).
- ne-audit: 12 at @1547 (d−12), 94 at @1548 (d−11) — both belong to the "00 46 70 12 94" = "pour que [70-12-94]" prenne frame (joint with prenne-70-12-94, not re-litigated). No "ne" licenses the "26 pas" clause: bare "pas".
- "la [26] pas" under the winning (verb) class: NO parse, stated exactly — "la" + finite verb is ungrammatical under banked 11="la"; "la" as object pronoun would need a subject and "ne" ("ne la [V] pas") — both absent; substantivized-infinitive rescue fails ("la" + infinitive is ungrammatical; substantivized infinitives take "le").
- Fence (clause 3, second disjunct): clause boundary between 26 and 30 with stated cause — the positional rule (forced by banked "la") makes 26 nominal at this window, so 30="pas" cannot left-adjoin as its negation particle; the junction is a boundary by grammatical necessity. Right side recorded as residual: bare-"pas" fragment head (anomaly flagged to ne-alone-02-74); the "pas"-side resolution is owned by noun26-la-frames bar (b) (cross-referenced, not duplicated).

## Per-clause pass/fail

1. **PASS** — exactly 4 "26 30" bigrams stream-wide, at 0-based 655/992/1250/1560 = @654/@991/@1249/@1559; @654/@991 6-gram byte-identical ("76 49 24 26 30 03"), counted once.
2. **PASS** — 30="pas"-negation (battery-promoted standing value) in all four; n'importe rival excluded per window (pre-30 = 26 in all four; the single stream-wide 94→30 bigram is @1700, fenced to ne-30-1700); pas-noun rival has no determiner in any window. Caveat: 30="pas" awaits red-team ratification.
3. **PASS** — @654/@991/@1249: noun-parse ("[noun] pas") ungrammatical, no boundary available (gapless bigram, mid-row junctions, no article). @1559: boundary fenced with stated cause (positional rule forces nominal 26; "pas" cannot left-adjoin).
4. **PASS** — audit: @654: 94@d−4 (@650); @991: none; @1249: none; @1559: 12@d−12 (@1547) + 94@d−11 (@1548), both prenne-frame. Bare-"pas" 1840s tension stated for @991/@1249/@1559 and flagged to ne-alone-02-74.
5. **PASS (residual disjunct)** — "la [26] pas" has no verb-class parse (shown above); @1559 recorded as the residual forcing the positional rule: **26 = feminine noun iff immediately preceded by 11="la" (banked article), else verb-class.** Polyvalence cost stated below for the red team.

## Adverses (all answered, none ignored)

1. **@1559's "la" (banked article) forces noun in the same window** — answered via the positional rule: one reading gives way per position. 26 is verb-class everywhere except the "la"-frame, where banked 11="la" forces the noun. The rule is recorded as a finding; its polyvalence cost is stated for the red team (below), not declared by this battery.
2. **23~26 split granted (no homophone rescue via 23)** — respected. 23 absent within ±8 at @654/@991/@1249; at @1559 a 23 stands at @1551 (d−8, "…92 45 23 99 13 93 61 40 17 11 [26]…"), structurally distant inside its own frame — no rescue attempted or needed.
3. **"26n" one-word rival (12 = final "n")** — fenced with stated cause. "26 12 30" occurs 0x stream-wide; "26 12" x4 (@239/@841/@1469/@1706) never coincides with a "26 30" window; all four "26 30" bigrams are gapless, so no "n" intervenes. The composition rival is live only at the "26 12" windows (F6, joint with homophone-12-30 / the noun-26 war generally). A final-"n" internal to 26's own spelling is untestable at battery level and non-discriminating here: "[26n-noun] pas" is still noun+"pas" and changes nothing.

## Verdict: PROMOTE (frame-level, with recorded positional exception)

26 is verb-class; "26 30" = "[verb] pas" is demonstrated at @654/@991/@1249 (noun-parse excluded per window; ne-audit complete; no rival parse of 30). Noun-26 is killed in every non-"la" window. @1559 is the recorded residual: banked "la" forces nominal 26 there, which forces the positional rule **"26 = feminine noun iff immediately preceded by 11='la', else verb-class"**.

**Red-team referral (not a declaration):** the positional rule is a second positional polyvalence and therefore stands in tension with the §7 lane law ("67 et/veut is the sole true polyvalence"). This battery declares no polyvalence, names no value for 26, and overwrites no verdict. The rule is recorded as a finding with its cost stated; declaration is a red-team act. Joint with queued noun26-la-frames (whose bar (b) owns the "pas"-side resolution at @1559) and flagged to ne-alone-02-74 (bare-"pas" licensing @991/@1249/@1559).

## Caveats

- 30="pas", 94="ne", 12="n"/48="e" are battery-promoted, pending red-team ratification; 59="est" provisional (not load-bearing here).
- 76/49/24 values open: @654's "ne … pas" is clitic-chain-COMPATIBLE, not a proved parse.
- Canonicality caveat stands (68 of 70 upstream row offsets unvalidated).
- @-convention: @ = 0-based stream index − 1 throughout.
