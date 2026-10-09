# Battery report: stem-03-nounfamily

- Target id: `stem-03-nounfamily`
- Claim: "Test whether 03's non-infinitive windows converge on one noun/word value; if yes, package the stem-vs-noun split for red-team adjudication (conditioned split vs polyvalence)."
- Date: 2026-10-09
- Worker: battery worker (subagent 81c5096b-761f-4aa5-bff3-a8a68f9f6140)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`). All @-offsets are 0-based repaired-stream indices. n(03) = 20.
- Lock: `code/crowd17/next-token/locks/stem-03-nounfamily.lock` (created at start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"test whether 03's non-infinitive windows ('pas [03]' x3, '[03] qui' x4, 'ce [03]' x2, '[03] a' x3, '[03]e' @1237) converge on one noun/word value; if yes, package the stem-vs-noun split for red-team adjudication (conditioned split vs polyvalence)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) 'pas [03]' x3 (@31, @657, @994): each window is noun-compatible (nominal 03), with no window forcing a non-noun reading.
2. (C2) '[03] qui' x4 (@31, @336, @674, @1645): nominal 03 is forced at each (64='qui' banked GT needs a nominal antecedent; a verb cannot head a relative clause).
3. (C3) 'ce [03]' x2 (@1014, @1790, via 47='ce' A4-granted): demonstrative + noun forced at each.
4. (C4) '[03] a' x3 (@599, @691, @1675, via '03 39' with 39='a/à' battery-promoted): each window noun-compatible; no window forces a non-noun reading.
5. (C5) '[03]e' @1237: noun-compatible (a noun with -e ending).
6. (C6) If C1–C5 all pass (convergence), the stem-vs-noun split evidence package is delivered in this report for red-team adjudication (conditioned split vs §7 polyvalence); if any clause fails, fence instead.
7. (C7) Adverses answered (see below).

## Method

1. Re-derived the repaired parse in-session (1,847 pairs, 96 groups asserted). Never used `canonical.py`. R5005 untouched.
2. Enumerated all 20 windows of 03 with ±7 context; verified the bar's frame counts byte-exact: '30 03' x3, '03 64' x4, '47 03' x2, '03 39' x3, '03 40' @1237. Distinct test windows: 12 (@31 in both 'pas [03]' and '[03] qui').
3. Tested each test window for (a) noun-compatibility, (b) forced-nominal status, (c) any forced non-noun reading.
4. The infinitive windows '03 29' x3 (@1030, @1320, @1594) were excluded from the test per the bar (they are the verb-stem arm, owned by queued `stem-03`); they were not re-litigated, only cited.

## Window-level evidence

### C1 — 'pas [03]' x3 (30='pas' battery-promoted)

- **W1 @31** (row a1_00): `34 24 30 03 64 32 01` = "[24-fin] pas [03] qui [32]". Nominal 03: "pas [noun], qui [32-verb]…" — 03 heads the 'qui'-relative (see C2). Noun-compatible.
- **W2 @657** (row a4_02): `24 26 30 03 62 16 00` = "[24] [26] pas [03] [62] [16] pour [86]". "pas [03]" as negated nominal object (ne-drop is lane precedent). Noun-compatible; successor 62 imposes no nominal-hostile shape.
- **W3 @994** (row a6_01): `24 26 30 03 60 67 11` = "[24] [26] pas [03] [60] et la par". Same shape as W2. Noun-compatible.

### C2 — '[03] qui' x4 (64='qui' banked GT — requires a nominal antecedent)

- **W4 @31** (a1_00): "pas [03] qui [32]" — 03 heads the relative clause. Forced nominal.
- **W5 @336** (a2_05): `88 40 03 64 31 14 45` = "[88]e [03] qui [31] [14] ce qui par". 03 as nominal apposition head of the 'qui'-clause. Forced nominal. (Downstream breakage at "ce qui par" is edge-340-31-14's fence — it does not touch 03's class.)
- **W6 @674** (a5_00): `24 80 03 64 37 77 45` = "[24-fin] [80] [03] qui [37] le ce". 03 heads the relative clause. Forced nominal.
- **W7 @1645** (a8_04): `98 60 03 64 31 10 03 38` = "[98] [60] [03] qui [31] [10] [03] [38]". 03 heads the relative clause. Forced nominal.

A verb reading of 03 is ungrammatical at all four (a verb cannot head a 'qui'-relative). This is the strongest convergence leg.

### C3 — 'ce [03]' x2 (47='ce' A4-granted, allophone tier)

- **W8 @1014** (a6_02): `80 78 47 03 24 41 15` = "[80] [78] ce [03] [24] [41]". Demonstrative determiner + noun, then finite 24: "ce [noun] [24]…". Forced nominal (a demonstrative requires a nominal complement).
- **W9 @1790** (a8_09): `68 47 03 00 86 56 42` = "[68] ce [03] pour [86] [56]". "ce [noun] pour [INF]…". Forced nominal.

### C4 — '[03] a' x3 ('03 39', 39='a/à' battery-promoted, pending ratification)

- **W10 @599** (a4_00): `01 29 40 03 39 26 96 45` = "[01]er-e [03] a [26] par ce [93]". Under 39='a' (avoir 3sg): "…[03] a [26]" — "[noun] has [26]" (26's finite-verb promote is scoped to the [69]-formula windows; its class is open here, so no contradiction). Under 39='à': "[03] à [26]" — noun + 'à' + complement, grammatical with suitable nouns. Noun-compatible under both 39 values. Noted ambiguity: "40 03" could in principle be word-internal ("[01]er-e[03]"), but that reading is unforced and undemonstrated; it does not falsify the nominal reading.
- **W11 @691** (a5_00): `94 29 60 03 39 74 46` = "ne er [60] [03] a [74] que [02]". "ne [60]er [03] a [74]" — 03 as nominal object of the infinitive, then "a [74]". Noun-compatible.
- **W12 @1675** (a8_05): `92 60 03 39 74 77 44` = "[92] [60] [03] a [74] le [44] pour que". Same shape as W11. Noun-compatible.

No window in this group forces a non-noun reading; all three admit the nominal parse with standing or open values only.

### C5 — '[03]e' @1237

- **W13 @1237** (a7_01): `85 56 10 03 40 67 77 81` = "[85] [56] [10] [03]e et le [81]". With 67='et' per the §7 positional rule (follower 77='le' provisional is not infinitive-shaped): "[10] [03]e et le [81]" — "[03]e" as a noun with -e ending. Noun-compatible.

### Extra non-infinitive windows (completeness, outside the bar's set)

- **@664** (a4_02): `50 80 03 62 06 00` = "[50] [80] [03] [62] [06] pour". Whether 80 is A8 verb-frame or adverbial-'le', 03 sits in the nominal slot (object or 'le [03]'). Noun-compatible.
- **@722** (a5_02): `02 21 80 77 03 91 65` = "[02] [21] [80] le [03] [91]" — "le [03] [91]": forced nominal under provisional 77='le', corroborated by the locus-level battery finding that 91 is adjective-shaped here ("le [03-noun] [91-adj]"). This is the adverse-cited @720-721 window (1-based).
- **@886** (a5_08): `79 68 37 03 02 00` = "tout [68] [37] [03] [02] pour". FENCED as indeterminate: neither a nominal nor a verb-stem parse is forced; it is noun-compatible but not probative. Does not break convergence (it forces nothing).
- **@1367** (a7_06): `94 79 14 60 03 30 82 16` = "ne tout [14] [60] [03] pas m [16]". FENCED as indeterminate: "[60] [03] pas" admits no clean parse under any standing value, but no grammatical verb reading of 03 exists either. Noun-compatible-or-opaque; does not break convergence.
- **@1649** (a8_04): `31 10 03 38 82 16` = "[31] [10] [03] [38] m [16]". "[10] [03] [38]": noun-compatible (38 is adjective-shaped at two battery loci, determiner arm killed — "[03-noun] [38-adj]" is a live shape). Conditional, not probative.

### Excluded infinitive arm (cited, not re-tested)

'03 29' x3 (@1030 a6_03, @1320 a7_04, @1594 a8_02) = "[03]er" infinitive — the verb-stem arm, owned by queued `stem-03` (class bar). No '03 29' window overlaps the test set.

## Per-clause pass/fail

1. C1 ('pas [03]' x3): PASS — all three noun-compatible; @31 additionally forced-nominal.
2. C2 ('[03] qui' x4): PASS — nominal forced at all four; verb reading ungrammatical.
3. C3 ('ce [03]' x2): PASS — demonstrative + noun forced at both.
4. C4 ('[03] a' x3): PASS — all three noun-compatible under 39='a/à'; nothing forces non-noun.
5. C5 ('[03]e' @1237): PASS — noun with -e ending.
6. C6 (convergence → package): PASS — convergence holds (12/12 test windows noun-compatible; 7 of 12 forced-nominal: @31, @336, @674, @1645, @1014, @1790, and @722 under provisional 77='le'). The split package is delivered below.
7. C7 (adverses):
   - (a) "No polyvalence declared at battery level" — SATISFIED: this report packages a **conditioned split** for red-team adjudication (split by frame position), not a polyvalence declaration. 67 et/veut remains the sole true polyvalence per §7.
   - (b) "@720-721: 03 follows '80-le' … favoring a nominal/word reading" — INCORPORATED: @722 (0-based) = "80 77 03 91" is a forced-nominal leg under provisional 77='le'.
   - (c) "Coordinates with (does not duplicate) queued stem-03" — SATISFIED: the '03 29' verb-stem arm is cited, not re-tested; this battery tested only the non-infinitive windows.

## Verdict: PROMOTE (finding grade — stem-vs-noun split evidence package, battery-grade)

All bar clauses pass. The convergence is real and one-sided: within the non-infinitive windows, 03 is uniformly noun-shaped, with 7 forced-nominal windows. Against the excluded '03 29' x3 infinitive arm, this constitutes the stem-vs-noun split. Per §7 this is packaged for red-team adjudication, not declared.

### Split package for the red team

- **Arm A — verb stem (frame-conditioned):** '03 29' x3 (@1030, @1320, @1594) = "[03]er" infinitive. Conditioned on 29-following. Owned by queued `stem-03`; cited here only.
- **Arm B — noun (frame-conditioned):** all 17 other windows. Strong legs: '[03] qui' x4 (nominal antecedent required), 'ce [03]' x2 (demonstrative requires nominal complement), 'le [03] [91]' @722 (locus-level adjective-91 finding). Weak/conditional legs: 'pas [03]' x3 (W2/W3), '[03] a' x3 (conditional on 39='a/à' ratification and open 26/74 classes), '[03]e' @1237, @664, @1649.
- **Fenced residuals:** @886 and @1367 (indeterminate, noun-compatible, not probative).
- **Conditioning hypothesis (red-team venue):** 03's function is conditioned by position — verb stem in the "03 29" infinitive frame, noun elsewhere. This is a conditioned split, not free polyvalence; §7 adjudication (conditioned split vs polyvalence) belongs to the red team.
- **No specific noun value is named** — the bar asked for convergence on a noun/word *reading*, not a lexeme. Naming the noun value is follow-up 1.

### Caveats (stated, not hidden)

- Canonicality: all windows lie on offset-0 rows (68 of 70 upstream row offsets unvalidated). The convergence holds on the canonical stream per protocol; none of the windows sit on the known phase-uncertain rows (a1_01, a7_10).
- 39='a/à' is battery-promoted, pending ratification — C4's nominal legs are conditional on it; if the 39 promote falls, C4 re-opens.
- @722's forced-nominal leg is conditional on provisional 77='le'.
- 26's finite-verb promote is scoped to the [69]-formula windows; C4's parses do not depend on it.

## Follow-ups (optional; this is a promote, not a null)

1. `val-03-noun` (P3) — name 03's noun value: test candidate lexemes against the forced-nominal windows (@336, @674, @1645, @1014, @1790, @722); kill candidates that fail any.
2. `resid-03-886-1367` (P4) — re-test the two fenced residuals (@886, @1367) once 38's class and 60's split adjudication land; promote to a leg or kill-grade fence.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-stem-03-nounfamily.md`
- Queue: `battery-queue.json` → `stem-03-nounfamily` status `verdict`, result `promote`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated post-write; only this entry touched).
- Lock: created on start, deleted on completion.
- No standing verdict contradicted or downgraded. No red-team verdict touched. R5005, sealed gates, red-team queue untouched. `canonical.py` never used.
