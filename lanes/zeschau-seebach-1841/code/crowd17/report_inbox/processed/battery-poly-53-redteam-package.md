# Battery verdict: poly-53-redteam-package — structured evidence package for the red-team S7 docket: the "don"-vs-"doni" irreconcilability

- Target id: `poly-53-redteam-package` (priority 2)
- Claim: "structured evidence package for the red-team S7 docket: the 'don'-vs-'doni' irreconcilability"
- Date: 2026-10-09
- Worker: battery worker (subagent 03c7dc60-9ff4-4f44-b537-49a64fdf9f8f, parent: next-token-supervisor)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed exactly per code/side-keyhunt/repair_parse.py; re-derived in-work: 1,847 pairs / 96 types, n(53)=11). `canonical.py` never used. R5005 untouched. Sealed gates untouched. Red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/poly-53-redteam-package.lock (created 2026-10-09T08:25:41Z; no pre-existing lock; no stale lock found); deleted on completion.
- Role: EVIDENCE PACKAGING for the red team (like battery-noun-44-legs-package.md). This report gathers window-level evidence; it does NOT declare a conditioned split, names no value for 53, and implicates no polyvalence. The venue for the decision is the red-team S7 docket.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"package only; red team decides conditioned split vs re-parse"

Numbered pass/fail clauses (frozen before any window analysis; bar not modified after):

1. **(C1, packaging completeness)** The report contains the full window-level evidence for both 53-value arms: Arm A ("53n" x4 / "donne" x2 compositional, with @-offsets, row ids, and the composition under 53="don" + 12="n" + 48="e") and Arm B ("53 34" word-internal at @403-404 under the wordbound promote, with hapax status, 34='i' banked, and the "[53]i" = "doni" consequence under 53="don").
2. **(C2, load-bearing grants)** Each arm's standing values and battery-grade grants are stated: Arm A loads on 12="n" (promoted letter tier), 48="e" (inflectional), and 53="don"-stem (prof-53 P-A compositional, unbroken at @168/@708); Arm B loads on the ce88-53-wordbound PROMOTE ("53 34" one word "[53]i", boundary reading kill-grade dead) plus the ce88-pronoun-frame PROMOTE (53 as 88's complement at @403).
3. **(C3, conditioning hypotheses)** The conditioning hypotheses are stated with their load-bearing grants, so the red team can decide: conditioned split vs re-parse of Arm A's premises vs re-parse of Arm B's premises.
4. **(C4, package only)** No conditioned split is declared; no value is named for 53; no standing verdict is re-adjudicated or downgraded; §7 (67 et/veut sole true polyvalence) is intact. Every number traces to the repaired stream; R5005, sealed gates, and the red-team adjudication queue are untouched.

Offset convention: all @-offsets are 0-based repaired-stream pair indices; row ids stated beside each. Row-context windows verified in-work.

## Method

1. Re-derived the repaired stream in-work from repaired_offsets.json + upstream-ct_R5005.txt exactly per repair_parse.py (1,847 pairs / 96 types confirmed). Never used canonical.py.
2. Re-derived 53's full positional census in-work (n(53)=11), byte-identical to the prior reports: [16, 57, 168, 403, 411, 708, 804, 1020, 1280, 1473, 1581].
3. Read the four premise reports in full and cited them as premises (not re-litigated): battery-ce88-53-value.md (NULL 2026-10-09 — the irreconcilability finding), battery-ce88-53-wordbound.md (PROMOTE 2026-10-09 — "53 34" one word "[53]i"), battery-ce88-pronoun-frame.md (PROMOTE 2026-10-09 — 53 as 88's complement at @403), battery-prof-53 (NULL 2026-10-08 — "donne" compositional clean at @168/@708).
4. Re-verified each packaged window's predecessor/successor groups against the repaired stream with ±3-group context.

## Window-level evidence

### ARM A — "53n" x4 / "donne" x2 compositional (53 = "don"-family)

53="don" is the only independently-supported whole-syllable value for 53. All windows 0-based, byte-verified in-work:

- **@168 (row a1_05):** `166:82 167:84 168:53 169:12 170:48 171:21` — "84=on 53 12 48" → "on" + "don"+"n"+"e" = **"on donne"**, compositionally clean under 53="don", 12="n", 48="e". (prof-53 P-A: CLEAN.)
- **@708 (row a5_01):** `706:21 707:35 708:53 709:12 710:48 711:71` — "35 53 12 48" → "donne" compositionally clean under the same grants. (prof-53 P-A: CLEAN.)
- **@57 (row a1_01):** `56:35 57:53 58:12 59:41` — "35 53 12 41" → "don"+"n"+41: the "donn"-stem arm; the 'donne' whole-word reading (P-B) is killed here ("donnen[41]" broken), but the compositional "donn"+41 stem reading survives, requiring 53="don" + 12="n".
- **@1581 (row a8_02):** `1580:24 1581:53 1582:12 1583:44` — "24 53 12 44" → "donn"+44: same stem arm; whole-word "donne" killed here too ("donnen[44]" broken), compositional "don"+"n" survives.

Arm A in one line: 53 is followed by 12 x4 stream-wide (successors: 12 x4, 84 x2, 17/34/69/61/60 x1), and at all four 53-12 windows the "don"-stem parses with zero contradictions among the eleven windows. No other whole-syllable value is independently supported.

**Fencing windows (admit no independently-grounded whole-word value for any candidate; they fence, not decide):** @16 (a1_00: `15:91 16:53 17:17` = "[91] [53] fois", 17=fois granted); @804 (a5_05: `803:98 804:53 805:69` = "98=vient 53 69='ce'"); @411 (a2_08: `410:02 411:53 412:84` = "[02] [53] on"); @1020 (a6_02/a6_03: `1019:91 1020:53 1021:84` = "[91] [53] on"); @1280 (a7_03: `1279:48 1280:53 1281:61`); @1473 (a7_10: `1472:41 1473:53 1474:60`).

**Rival "[X]i" candidates exhausted** (ce88-53-value §4, cited): "boni" (X="bon") gives "bonne" at @168 ("on bonne" ungrammatical) and "bon fois" at @16; "merci"/"ami"/"ici"/"aussi"/"parmi" all give non-French "Xn" ("mercn", "amn", "icn"...). No rival satisfies Arm A's windows and Arm B jointly.

### ARM B — "53 34" word-internal at @403-404 ("[53]i")

- **The locus @400-407 (row a2_08):** `400:11 401:45 402:88 403:53 404:34 405:69 406:26 407:00` = "la ce [88-V] [53] [34='i'] [69='ce'] [26-noun] pour". 53 is 88's post-verbal complement (ce88-pronoun-frame PROMOTE: "ce [88] [53...]" with 45='ce' demonstrative pronoun per ce88-leftedge-402 PROMOTE; "45 88" hapax bigram 1x stream-wide; cross-checked @86/@646/@1541 with "88 le X" transitive frames).
- **"53 34" is a stream hapax** (exactly 1x in 1,847 pairs, at @403-404; re-verified in-work).
- **Wordbound promote (ce88-53-wordbound PROMOTE):** NO word boundary between 53 and 34 — "53 34" is one word "[53]i" with 34='i' (banked letter) word-final. The boundary reading is kill-grade dead: 34 never stands alone as a word anywhere (no standalone French word "i"), and the word-initial sub-reading "34 69" = "ice" is not a French word while 69 is a standalone "ce" at @405 (ce69-global PROMOTE, "69 26" = "ce [26-noun]").
- **The consequence:** under 53="don" (forced by Arm A), "[53]i" = **"doni" — not a French word**, and no French word continues "doni..." (checked against the 1841 period corpus and standard lexicon; the wordbound battery recorded the same). As a noun, bare "don" as 88's direct object is additionally unlicensed ("faire don de" is the idiom; bare "don" needs a determiner).

### The irreconcilability (headline finding, restated from ce88-53-value NULL)

53="don" is forced at battery grade by the "53 12" x4 family ("donne" x2 compositional, zero contradictions in 11 windows); "53 34" word-internal ("[53]i", battery-promoted) forces 53≠"don" at @403. **The two constraints are jointly unsatisfiable by any uniform value.** This is the red team's §7 territory, not a battery naming.

## Conditioning hypotheses (for the red-team decision)

- **H1 — conditioned split (the split option):** 53 is not one uniform value; a conditioned value where the "don"-family reading holds under successor-12 conditioning (@57/@168/@708/@1581) and a different continuation holds word-internally at @403 ("[53]i"). Battery level may NOT declare this: §7 names 67 et/veut the sole true polyvalence, and only the red team can ratify a second conditioned split.
- **H2 — re-parse Arm A's premises:** 12 is not the "n" letter tier, or 48 is not the "e" inflectional ending, or the "don"-stem is otherwise re-parsed. Cost: must answer the clean compositional windows @168 ("on donne") and @708 ("donne"), the two "donn"+41/44 stems @57/@1581, and prof-53's P-A fencing (already null, not killed).
- **H3 — re-parse Arm B's premises:** a word boundary exists between 53 and 34 after all (53 as bare direct object + 34='i' word-initial or standalone). Cost: must answer wordbound E3 (boundary kill-grade dead: no standalone French "i"; "ice" not a word; 69='ce' standalone at @405) and the bare-"don"-as-direct-object licensing problem.
- **H4 — re-parse the frame:** 88's governor role or 45='ce' pronoun status is re-parsed. Cost: must answer ce88-pronoun-frame's three cross-check windows (@86/@646/@1541, "88 le X" transitive frames) and ce88-leftedge-402's hapax-"45 88" analysis.

## Per-clause pass/fail

1. **C1 (packaging completeness): PASS** — Arm A (four "53 12" windows, "donne" x2 compositional) and Arm B ("53 34" @403-404 word-internal, "doni" consequence) fully window-evidenced above with 0-based @-offsets, row ids, and byte-verified ±3 contexts; fencing windows and the exhausted rival family also cited.
2. **C2 (load-bearing grants): PASS** — stated for each arm: Arm A loads on 12="n" (promoted letter tier) + 48="e" (inflectional) + 53="don"-stem (prof-53 P-A compositional, clean @168/@708, whole-word P-B killed at @57/@1581); Arm B loads on the ce88-53-wordbound PROMOTE (no boundary; kill-grade dead boundary reading) + ce88-pronoun-frame PROMOTE (53 as 88's complement at @403) + 34='i' banked.
3. **C3 (conditioning hypotheses): PASS** — H1 conditioned split, H2 re-parse Arm A, H3 re-parse Arm B, H4 re-parse the frame, each stated with its load-bearing grants and its answering cost.
4. **C4 (package only): PASS** — no conditioned split declared; no value named for 53; no verdict downgraded or re-adjudicated (ce88-53-value, ce88-53-wordbound, ce88-pronoun-frame, ce88-leftedge-402, prof-53 used as premises); §7 intact (no polyvalence declared — the 67 rule is untouched); every number traces to the repaired stream; R5005, sealed gates, and the red-team adjudication queue untouched.

## Verdict: PROMOTE (packaging complete)

The evidence package is delivered as commissioned: both arms of the "don"-vs-"doni" irreconcilability are window-evidenced against the repaired 1,847-pair stream on standing values and battery-grade premises, with the conditioning hypotheses (conditioned split vs re-parse) and their answering costs stated for the red-team S7 docket. This promote endorses the package's completeness and honesty only — it names no value for 53, decides nothing about the split, and implicates no polyvalence.

## Follow-ups

None required: this is a promote verdict, not a null. The open question (conditioned split vs re-parse for 53) already has its red-team venue (the S7 docket) — this package feeds it; the queue duplicate `val-53-Xi-noun` (queued) already covers the "[X]i"-noun search follow-up from ce88-53-value. Nothing further regenerated.

## Provenance

Every number re-derived from the repaired stream in-work: 1,847 pairs / 96 types / n(53)=11 at 0-based [16, 57, 168, 403, 411, 708, 804, 1020, 1280, 1473, 1581]; "53 12" x4 at @57/@168/@708/@1581; "53 34" hapax at @403-404; locus window @400-407 row a2_08. Premise reports read in full, not re-litigated. Lock created on start, deleted on completion. No invented data.
