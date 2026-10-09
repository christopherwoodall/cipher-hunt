# Battery report: pasX-leftverb-59

- Target: `pasX-leftverb-59` (battery-queue.json, priority 3, status queued)
- Claim: at @560 and @1716 the LEFT neighbor is 59 ("est", provisional) — test "59 30" as "[n']est pas" (ordinary ne-drop negation with a leftward verb host), dissolving the "verb-less" premise for those two windows with no ellipsis at all.
- Worker: 0c6baa1e-801d-4a15-8179-c3b003d94992
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched. All @-offsets 0-based pair indices.

## Bar (verbatim, pre-registered)

"promote iff "59 30" parses as "[ne] est pas" with 59="est" attested independently of these windows; fence iff 59!="est" or the post-pas complement stays ungrammatical."

Numbered clauses (frozen before testing):
1. "59 30" at @559-560 parses as "[ne] est pas".
2. "59 30" at @1715-1716 parses as "[ne] est pas".
3. 59="est" is attested independently of @559/@1715 (the adverse).
4. Fence arm: fires iff 59!="est" or a post-"pas" complement stays ungrammatical.

## Method

Enumerated all "59 30" bigrams stream-wide (n=2: @559, @1715 — byte-exact, no others). Full census of 59 (n=27) with ±4 context to test the adverse. Period-corpus check of the W2 post-"pas" geometry ("pas qui ce") over `code/side-period/corpus` (77 files, ~35M chars). Standing values used: 94="ne" (STRONG LEAD, R17-001/R20-007 — not granted), 59="est" (provisional), 30="pas" (battery-promoted, conditional on 94-lead + 59-provisional per R20), 11="la" GT, 64="qui" granted, 47="ce" (A4), 44="l'" (battery-grade, clitic-44 census), 24="en" (R24), 67 et/veut positional rule, 43 nominal class, 98="vient" (battery-grade).

## Window-level evidence

**W1 — @559-560 (row a3_02, row starts at @558):**
`@555-570: 34 17 86 94 59 30 67 11 43 24 80 97 13 76 45 94`
Reads: "…[34=i] [17=fois] [86] ne est pas [67] la [43] en [80]…"
- "94 59 30" = "ne est pas" in canonical order, verb host 59 left-adjacent to 30. No ellipsis: the clause "…[86] n'est pas" is complete.
- Post-"pas": 67="et" (positional rule: follower 11="la" is not infinitive-shaped, so "et"), then "la [43] en [80]…" = "et la [43]…" — grammatical clause continuation ("and the [43]…"). 43 nominal class confirmed.
- Fully clean parse. No ungranted assumptions beyond standing/lead values.

**W2 — @1715-1716 (row a8_06):**
`@1708-1728: 12 06 29 40 65 94 44 59 30 64 47 68 06 11 52 37 43 98 39 88 24`
Reads: "…[40=e] [65] ne [44=l'] est pas qui ce [68]…"
- "94 44 59 30" = "ne l' est pas" — the "59 30" pair parses as "est pas" with 59 as verb host; the "ne…pas" clause is complete ("[65] ne l'est pas" = "[65] is not it"). No ellipsis needed for the pair parse.
- Post-"pas": "64 47 68 06 11 52 37 43…" = "qui ce [68] [06] la [52] [37] [43]…". This geometry is strained: no clean 1841-French gloss for "pas qui ce [68]" was found, and the exact geometry "pas qui ce" is unattested in the ~35M-char period corpus (0 hits; control "est pas" ×33 in one FR file, so the corpus is not empty of the neighborhood).
- Not kill-grade: the sibling battery `43-1126-1725-joint` builds live continuations on exactly "30@1716 64@1717 47@1718 68@1719…" without killing it, and a strained-but-grammatical reading exists: appositive "ce [68]" inside the relative clause — "…[65], qui, ce [68], [06-verb]-ent…" ("which — this [68] — verbs…"), a literary apposition to the relative pronoun. Strained, fenced as residual, not forced-false.
- Row break at @1719 (a8_07 starts) carries no clause information.

**Adverse — 59="est" independent attestation (n(59)=27, full census):**
Clean independent "est" legs, none touching @559/@1715:
- "est [predicative]" A1 frames: @316 ("64=qui 59 32…"), @448 ("61 59 32…"), @624 ("14 59 37…"), @1178 ("48 59 37…"), @1210 ("64=qui 59 32…"), @1443 ("68 59 37…"), @1796 ("94=ne 59 37…").
- "est que/qui" frames: @216 ("06 59 46=que…"), @1190 ("59 46=que…"), @1777 ("64=qui 59 19…"), @1833 ("16 59 36…").
- Two odd windows do not overturn the uniform value at battery grade: @103 ("93 59 45…", 93 inflectional-ending context) and @554 ("86 59 34=i 17=fois…", letter-adjacent) — neither forces 59!="est"; a split is red-team venue, not battery-grade.
- Adverse ANSWERED: 59="est" holds on 10+ independent legs.

## Per-clause results

1. "59 30" @559-560 parses as "[ne] est pas": PASS — "86 ne est pas, et la [43]…", fully grammatical, zero ellipsis.
2. "59 30" @1715-1716 parses as "[ne] est pas": PASS — "…ne l'est pas" complete; W2 post-"pas" "qui ce [68]…" strained (corpus-unattested) but not kill-grade (appositive reading available; sibling batteries keep it live).
3. 59="est" independent attestation: PASS — 10+ clean legs listed above.
4. Fence arm: DOES NOT FIRE — 59="est" holds; neither post-"pas" complement is established ungrammatical at the lane's kill-grade standard (W1 clean, W2 strained-but-live).

## Caveats (epistemic status, marked up front)

- 94="ne" is STRONG LEAD (R17-001, confirmed R20-007) — the "ne" half of "[ne] est pas" inherits lead tier, not granted.
- 59="est" remains provisional; 30="pas" conditional on 94-lead + 59-provisional (R20).
- W2's post-"pas" "qui ce [68]" continuation is a fenced residual: strained, corpus-unattested geometry; owned by the 43-family batteries (`43-1126-1725-joint` and follow-ups), which treat it as live. This residual does not touch the "59 30" pair parse.
- Canonicality caveat stands (§7).

## Verdict

**PROMOTE** — all bar clauses pass; the single adverse (59="est" independence) is answered on 10+ legs; the fence arm does not fire at the lane's kill-grade standard. The "verb-less" premise for both "59 30" windows is dissolved: 59 is the leftward verb host, and neither window needs ellipsis for the "est pas" parse.

(No null, so no follow-up targets required per §4.)

## Bookkeeping

- Lock `code/crowd17/next-token/locks/pasX-leftverb-59.lock` created 2026-10-09T15:24:06Z, deleted on completion.
- Queue: `pasX-leftverb-59` → `status: verdict`, `verdict: {result: promote, report: code/crowd17/report_inbox/battery-pasX-leftverb-59.md, date: 2026-10-09}` (temp-file + rename; pre-write assert passed: was queued/verdictless; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched. No standing/red-team verdict contradicted or downgraded.
