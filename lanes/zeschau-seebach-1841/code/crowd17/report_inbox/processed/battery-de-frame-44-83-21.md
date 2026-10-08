# Battery report: de-frame-44-83-21 — "'44-83-21-67-78' x2 reads '[44] de [21] [67] [78]' under 83='de'"

- Worker: battery-worker de-frame-44-83-21, agent 18b1e3fb-6311-4168-a3e9-96c39f0acc82
- Date: 2026-10-08 (lock created 2026-10-08T18:39:13Z)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). canonical.py NOT used. R5005 untouched. All @-offsets are repaired-stream indices.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"(a) both windows parse with 44 noun-shaped and 83='de'; (b) 21-67-78 resolves with stated values (67's positional rule, 78's 'ver'-lead or stated alternative); (c) zero contradiction across both windows"

Numbered clauses (frozen before testing):
1. Both 5-gram windows (@1160, @1839) parse with 44 noun-shaped and 83='de'.
2. The '21-67-78' trigram resolves with stated values: 67 via the §7 positional rule (67='veut' iff follower infinitive-shaped), 78 via the 'ver'-lead (or a stated alternative).
3. Zero contradiction across both windows.

## Method

Re-parsed the repaired stream in-work (1,847 pairs confirmed). Verified the byte-identical 5-gram '44-83-21-67-78' occurs exactly twice (@1160, @1839) and the '21-67-78' trigram exactly twice (@1162, @1841 — both inside the 5-grams). Ran predecessor/successor censuses for 21 (n=30), 67 (n=38), 78 (n=31), 44 (n=15), 83 (n=15), 22 (n=3), 42 (n=20). Parses use only standing values: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce allophone); battery-promoted (94=ne, 12=n + 48=e, 30=pas, 06=ent); provisional (59=est, 77=le); class-level promotes (24=finite verb modal-shaped, 86 INF-class). No value is named for 44 or 21 (both open; no duplication of noun-44's value arm).

STATUS CHANGE vs the queue entry (recorded, not re-litigated): noun-44 is no longer "queued" — it was KILLED 2026-10-08 (code/crowd17/report_inbox/processed/battery-noun-44.md), conditional on 94='ne' (battery-promoted, pending ratification) and 59='est' (provisional). The kill fences @1160's '82 44' as word-internal "le m[44]" (82='m' letter + 44 nominal stem) and proposes stem-44-nominal as follow-up.

## Window-level evidence

**Window @1160 (row a6_09):** `80 17 77 82 | 44 83 21 67 78 | 45 13 55 61 94 87 83 21 85 36`
- '17 77 82' = "fois le m": 17='fois' (promoted), 77='le' (provisional; le-77 battery null, not killed), 82='m' (GT letter). The '77 82' bigram occurs exactly twice stream-wide: @1041 ("fois le m[63]") and @1157 ("fois le m[44]") — both after 17='fois'. The parallel "le m[X]" frame supports the word-internal reading: 'le' + 'm' + nominal stem.
- 44: nominal stem per the noun-44 kill's own fencing ("most naturally word-internal 'le m[44]'"). Noun-shaped at slot level; no value named.
- '44 83 21': "[44] de [21]" — 83='de' (lead) + 'de'-complement. '83 21' occurs x3 (@1161, @1171, @1840); 83->21 is one of 83's top successors (x3/15).
- '21 67 78': 21 = noun (stated class): 'la [21]' x2 (@108, @358), 'de [21]' x3, 21-67 x8/30 (21's top successor). 67: follower is 78; 78 is not infinitive-shaped ('ver'-word: 'ce [78]' x7, 'le [78]' x7, 'er' killed distributionally per ver-78) → positional rule gives 67='et'. 78 = 'ver'-word lead (R16-005 graded LEAD, ver-78 battery null — lead not settled; used conditionally as the bar permits). Reading: "de [21] et [ver…]" — 'de' shared across the coordination ("de Y et Z"), grammatical French NP: "le m[44] de [21] et [ver-word]".
- Right context: '78 45' @1164 = 'verdict'-shaped (78-45 x4 stream-wide). '94 87 83 21' @1169: "ne ce [83] [21]" — the @1170/1171 '87 83' is the fenced 'ce de' adverse, owned by queued frame-87-83-cede ('cède' composition rival); not re-litigated here.

**Window @1839 (row a8_11, stream-final):** `59 36 69 64 22 42 | 44 83 21 67 78 | 49 74 93` (stream ends @1846)
- Left: 59='est' (provisional), 64='qui' (granted). '64 22' is hapax (@1836 only); 22 n=3 (@770 '80 22 94', @1663 '10 22 94', @1837). 42: A1 predicative frame, value open. The stretch 'qui [22] [42]' is unresolved (stated residual — 22 hapax-adjacent, 42 value-open) but forces no contradiction on 44.
- 44: head of the NP "[44] de [21] et [78-word]". The 'de [21]' complement + 'et [78]' coordination is NP-internal: only a nominal 44 is grammatical here (a finite verb or adjective cannot head "…de [21] et [ver-word]" in this position; the adjective-'de'-complement rival, e.g. "digne de", is noted but the noun reading is the natural one and the bar asks only for noun-shaped). 83='de' grammatical.
- 67/78: same as @1160 — 67='et' by positional rule, 78='ver'-word lead. '21-67-78' identical trigram.
- Right: '78 49 74 93' — 49/74/93 open (93 class open; verb-93 queued). Stream ends at @1846; incompleteness is not contradiction.
- Left-context flag (lead-level, out of claim scope): @1829 '83 24' = "m [38] de [24]" — under ne-24-profile's class-level promote (24 = finite modal-shaped verb, 2026-10-08), 'de' + finite verb is ungrammatical. The le83-window battery (null, 2026-10-08) counted @1829's '83 24' as de-compatible; that count is stale by one window under the 24 promotion. This is a NEW adverse for the shared 83='de' lead, not for this 5-gram claim (different token). Flagged for the de-83-residuals worker (lock active at run time); not adjudicated here.

**Cross-window checks (all re-derived from the stream, not copied):**
- '44 83' x2/15 of 83's predecessors; '83 21' x3; '21 67' x8/30; '67 78' x4/38; '78 45' x4/31.
- 67's positional rule is the §7 sole-polyvalence law; applied identically at both windows.

## Per-clause verdicts

1. (a) Both windows parse with 44 noun-shaped + 83='de': PASS at slot level. @1160: "le m[44] de [21]" (word-internal nominal stem, consistent with the noun-44 kill's fencing). @1839: "[44] de [21] et [78-word]" (44 heads the 'de'-NP; only nominal slot grammatical). Residual: 'qui [22] [42]' left edge at @1839 unresolved (22 hapax-adjacent n=3; 42 value-open) — no forced contradiction.
2. (b) '21-67-78' resolves: PASS. 21 = noun (stated class: 'la [21]' x2, 'de [21]' x3, 21-67 x8/30; no value named). 67 = 'et' (positional rule: 78 not infinitive-shaped). 78 = 'ver'-word lead (conditional, per R16-005/ver-78 null). "de [21] et [ver…]" grammatical.
3. (c) Zero contradiction across both windows: PASS within claim scope. No window forces the 5-gram reading false. The in-window @1171 '87 83' is the fenced 'cède' adverse (frame-87-83-cede owns). The @1829 '83 24' tension is lead-level (different token) and flagged for de-83-residuals.

## Adverses (all listed adverses answered or fenced — none ignored)

- "44's value open — coordinate with queued noun-44 (do not duplicate)": noun-44 is now KILLED (2026-10-08), not queued — status change recorded. No value named for 44 here (no duplication). @1160's nominal-stem parse is consistent with the kill's fencing. @1839's nominal-head parse is window-local; its global implications are the escalation below.
- "21's class open": stated as noun class (evidence above); value not named.
- "67 is the sole polyvalence (positional rule required)": positional rule applied; 67='et' at both windows. No second polyvalence invoked.
- "the shared 83='de' lead carries the @911/@614/@1171 adverses (fenced at fence-911-de / frame-87-83-cede)": @911 — fence-911-de (null 2026-10-08; kill-grade failure of UNCONDITIONED 83='de' recorded, escalated to red team; no battery-level kill per its bar). @614/@1171 ('87 83' x2) — frame-87-83-cede owns (queued). Not re-litigated. NEW: @1829 '83 24' adverse for the lead flagged above for de-83-residuals.

## Verdict: NULL — escalate to red team

Headline: clauses (a)–(c) pass at window level — the 5-gram reads "[44-nominal] de [21-noun] et [ver-word]" cleanly at both windows — but promotion is BLOCKED by the standing noun-44 kill under the §7 sole-polyvalence law. The kill (conditional on 94='ne' + 59='est') forces 44 into a clitic slot at @1714; asserting nominal-44 at @1839 (whole-word head of the 'de'-NP) would require 44 to carry two values, which only the red team can declare (67 et/veut is the sole true polyvalence). This battery cannot promote around the kill and will not re-litigate it.

No standing red-team verdict is contradicted or downgraded: noun-44's kill is battery-level (conditional, with its own escalation path escalate-1714-ne44); ver-78's null/LEAD grading is used exactly as graded; fence-911-de's escalation is left standing. Per protocol §5.2 the conflict is marked null and escalated, not overwritten.

Epistemic status (marked up front): if the red team overturns the @1714 clitic-forcing (via escalate-1714-ne44) or declares a second polyvalence for 44, this target's clauses already pass and the claim is promotion-ready. If the kill stands unconditioned, clause (a)'s @1839 nominal-head reading is unavailable and the 5-gram needs re-barring (stem-only?).

## Follow-ups (null regenerates work)

1. **de-frame-21-class** (priority 2): name 21's class independently of the 5-gram. Evidence: 'de [21]' x3 (@1161/@1171/@1840), 'la [21]' x2 (@108/@358), 21-67 x8/30 (top successor), 21-62 x5 / 21-60 x4 / 21-65 x4. Bar: "resolve iff 21's class is named (noun vs infinitive) with 'de [21]' x3 + 'la [21]' x2 parsing under one class and the 21-67 x8 contact explained; value not named." Unblocks clause (b)'s open class.
2. **stem-44-1839** (priority 2): adjudicate 44's morphological status at @1838–1840 (word-internal stem vs whole-word nominal head); coordinate with noun-44's stem-44-nominal follow-up — do not duplicate it, this target is the @1839 instance only. Bar: "resolve iff 44 at @1839 is decided stem-vs-whole with the '42 44' contact explained; do not name a global value; do not re-litigate @1714." Decides whether clause (a)'s @1839 reading can be stem-level (kill-compatible) or must be whole-word (escalation only).
3. **escalate-44-deframe** (red team): the @1839 nominal-head vs @1714 clitic-forcing conflict under the §7 sole-polyvalence law. Battery finding: both windows parse cleanly with nominal-44; promotion needs either (i) a red-team-declared second polyvalence for 44, or (ii) revisit of the noun-44 kill via escalate-1714-ne44 ('65ne word-final + 30-predicative' re-parse), or (iii) a ruling that the 5-gram's 44 is stem-level only. Battery may not decide.

## Provenance

Every count re-derived from the repaired 1,847-pair stream in-work: 5-gram x2 (@1160/@1839), '21-67-78' x2 (@1162/@1841), n(21)=30, n(67)=38, n(78)=31, n(44)=15, n(83)=15, n(22)=3, n(42)=20; bigrams '11-21' x2, '21-67' x8, '67-78' x4, '78-45' x4, '83-21' x3, '77-82' x2, '64-22' x1 (hapax), '42-44' x2. No invented data. R5005, sealed gates, and the red-team adjudication queue untouched. Lock deleted on completion.
