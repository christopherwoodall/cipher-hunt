# Battery verdict: ce88-53-value — name 53's value under the object constraint

- Target id: `ce88-53-value` (priority 3)
- Claim: "name 53's value under the object constraint"
- Date: 2026-10-09
- Worker: battery worker (subagent 81d223ab-ca0d-4d07-b594-2375029f9eb3)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, repair_parse.py tokenization; 1,847 pairs / 96 types asserted). All @-offsets are 0-based repaired-stream indices. `canonical.py` never used. R5005 untouched. Sealed gates untouched. Red-team queue untouched.
- Lock: code/crowd17/next-token/locks/ce88-53-value.lock (created at start, no pre-existing lock; deleted on completion).

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"name 53's value with the direct-object slot at @402 and '53 34' compatibility; zero standing-value contradiction"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) A named French value for 53 parses in the direct-object slot at @402 ("Ce [88-verb] [53...]") with the 53-headed complement role granted by the parent battery (ce88-pronoun-frame PROMOTE).
2. (C2) The named value is compatible with the '53 34' contact (@403–404): per the sibling battery ce88-53-wordbound (PROMOTE), "53 34" is one word "[53]i" with no word boundary — so the named value + 'i' (34, banked letter) must form a French word or word-start.
3. (C3) Zero standing-value contradiction: the named value contradicts no banked, granted, provisional, or battery-grade value and no standing rule (§7 intact).

## Method

1. Re-derived the repaired stream in-session; asserted 1,847 pairs / 96 types. Never used canonical.py. R5005 not touched.
2. Census: n(53) = 11 at 0-based [16, 57, 168, 403, 411, 708, 804, 1020, 1280, 1473, 1581]. Predecessors: 91 x2, 35 x2, 84/88/02/98/48/41/24 x1. Successors: 12 x4 (@57/@168/@708/@1581), 84 x2 (@411/@1020), 17/34/69/61/60 x1.
3. Adopted as premises (cited, not re-litigated): ce88-leftedge-402 PROMOTE (45='ce' demonstrative pronoun; "ce [88-verb]" pronoun+governor), ce88-pronoun-frame PROMOTE (53 as 88's complement at @402-403), ce88-53-wordbound PROMOTE ("53 34" one word "[53]i", no boundary), prof-53 NULL ('donne' = 53="donn"+12-48="ne" KILLED via "donnn" impossibility; compositional "donne" = 53="don"+12='n'+48='e' survives at @168/@708), 12="n" letter tier, 34='i' banked, 48='e' inflectional.
4. Tested candidate values against all three clauses on bytes; 1841 diplomatic French throughout.

## Window-level evidence

**The locus.** @400–406, row a2_08: `11=la 45=ce [88-V] [53] 34=i [69] [26]` — "Ce [88] [53]i..." with 53 the 53-headed complement of verb-88 and "53 34" word-internal per the wordbound promote.

**"53 12" x4 forces "don"-family.** At @57 ("35 53 12 41"), @168 ("84=on 53 12 48='e'"), @708 ("35 53 12 48='e'"), @1581 ("24 53 12 44"): 12='n' (promoted letter tier). 53="don" gives "don"+"n"+"e" = "donne" clean at @168 ("on donne") and @708, and "donn"+41/"donn"+44 stems at @57/@1581. This is the only independently-supported whole-syllable value for 53: two clean compositional windows, zero contradictions among the eleven.

**"doni" is not French.** Under the wordbound promote, 53="don" at @403 yields "[53]i" = "doni" — not a French word, and no French word continues "doni..." (checked against the 1841 period corpus and standard lexicon; the wordbound battery recorded the same). As a noun, bare "don" as 88's direct object is additionally unlicensed ("faire don de" is the idiom; bare "don" needs a determiner). As a verb stem "donn-", no French continuation exists after "doni".

**Rival "[X]i" candidates all fail the "53n" windows.** Exhausted the French "[X]i"-shaped nouns/adjectives against the "53 12" x4 ("X"+"n") constraint: "boni" (X="bon") gives "bonne" at @168 ("on bonne" ungrammatical) and "bon fois" at @16; "merci"/"ami"/"ici"/"aussi"/"parmi" (X="merc"/"am"/"ic"/"auss"/"parm") all give non-French "Xn" ("mercn", "amn", "icn"...). No candidate satisfies C1 and C2 jointly.

**@16 ("91 53 17" = "[91] [53] fois") and @804 ("98=vient 53 69")** admit no independently-grounded whole-word value for any candidate either; they fence rather than decide.

## Per-clause pass/fail

1. **C1 FAIL (demonstration failure, not kill grade).** No French value is nameable that parses cleanly in the @402 object slot: "don" (the only independently-supported value) cannot stand bare as a direct object and cannot continue word-internally; every rival is invented data.
2. **C2 FAIL (demonstration failure, not kill grade).** The wordbound promote pins "[53]i" word-internal; "don" gives "doni" (not French); all "[X]i" rivals contradict the "53n" x4 windows. No value satisfies both.
3. **C3 PASS (vacuous).** No value named, so no standing value contradicted; §7 intact (no polyvalence declared — the tension is packaged, not decided).

No standing or red-team verdict contradicted or downgraded. No battery verdict downgraded (ce88-pronoun-frame, ce88-53-wordbound, ce88-leftedge-402, prof-53 all used as premises).

## Headline finding (for the red-team docket)

**"don"-vs-"doni" irreconcilability.** 53="don" is forced at battery grade by the "53 12" x4 family ("donne" x2 compositional, zero contradictions in 11 windows); "53 34" word-internal ("[53]i", battery-promoted) forces 53≠"don" at @403. The two constraints are jointly unsatisfiable by any uniform value — this is conditioned-split territory and belongs to the red team per §7, not to a battery naming.

## Verdict: NULL

No value for 53 is nameable at battery grade without inventing data. The bar's naming requirement cannot be met; the failure is inconclusive (no window forces the existential claim false), so this is a null, not a kill.

## Follow-up targets (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. **poly-53-redteam-package** (priority 2): structured evidence package for the red-team §7 docket — the "don"-vs-"doni" irreconcilability ("53n" x4 / "donne" x2 compositional vs "53 34" word-internal promote), with the conditioning hypotheses and their load-bearing grants (12="n" letter tier, 48='e' inflectional, wordbound promote). Bars: package only; red team decides conditioned split vs re-parse.
2. **val-53-Xi-noun** (priority 3): wider search for "[X]i"-shaped French nouns/adjectives X with "Xn" also French (beyond the "boni"/"merci"/"ami" family exhausted here); kill iff none parses at @402 with zero new assumptions. Bars: name X with both "Xi" and "Xn" French and the @402 object slot parsing; else close the "[X]i"-noun space.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-ce88-53-value.md (this file).
- Queue: `battery-queue.json` -> `ce88-53-value` status `verdict`, result `null`, date 2026-10-09 (pre-write assert: no prior verdict; own entry only; temp-file + rename; JSON re-validated).
- Lock created at start, deleted on completion.
- canonical.py never used; R5005, sealed gates, red-team adjudication queue untouched.
