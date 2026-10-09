# Battery report: boundary-98-839 — **PROMOTE** (98's distributional function named; 98 is clause-terminal at @838; the @839 clause boundary hardens; particle face does NOT re-open)

**Target:** `boundary-98-839` (P2 per dispatch; queue lists P3)
**Date:** 2026-10-09 (UTC)
**Worker:** 2ade25f6-addf-4cca-b944-9606d462e72a
**Lock:** `code/crowd17/next-token/locks/boundary-98-839.lock` created on start (agent id + UTC 2026-10-09T08:46:48Z); no stale lock present. Deleted on completion.

## Bar (verbatim from queue)

"resolve iff 98's distributional function is named with byte evidence; if 98 is clause-medial, the @839 particle face re-opens"

## Bar restated as numbered clauses (fixed before testing)

- **(c1)** 98's distributional function is NAMED with byte evidence from the n=40 census on the repaired stream. PASS iff a function is named and grounded in the 40-window contact distribution.
- **(c2)** Positional decision: iff 98 is clause-terminal at @838, the @839 clause boundary (stated by particle-20-760-839) hardens and the particle face stands; iff 98 is clause-medial at @838, the @839 particle face re-opens (verdict then null with the re-open as headline, per protocol §5 — this battery declares no red-team verdict).
- Decision rule: (c1) PASS + clause-terminal → **promote**. (c1) PASS + clause-medial → **null** (particle face re-opens; follow-ups). (c1) FAIL → **null** with follow-ups.

## Method

Read BATTERY-PROTOCOL.md first. All stream facts re-derived in-session from the repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: asserts held — 1,847 pairs, 96 types). n(98) = 40 confirmed byte-exact (offsets: 12, 19, 80, 89, 92, 124, 192, 227, 236, 355, 440, 511, 702, 767, 803, 838, 894, 897, 930, 946, 971, 1060, 1073, 1074, 1137, 1139, 1145, 1146, 1284, 1317, 1325, 1373, 1481, 1579, 1601, 1643, 1660, 1661, 1725, 1783). `canonical.py` never touched. R5005, sealed gate instances, red-team adjudication queue untouched. Sibling reports read first: `battery-particle-20-760-839.md` (null; particle face at @760/@839 with clause boundary stated after 98), `battery-vient-98-894-reaudit.md` (promote; 98='vient' survives the 14-verb fence, battery grade, pending red-team ratification), `battery-vient-98-name.md` context. Adverses: none listed in the queue entry.

## Window-level evidence: the 40-window 98 census (re-derived, 0-based @-offsets)

### (c1) 98's distributional function: finite clause-head verb

**Follower census (n=40):** 98→83 x5, 98→82 x3, 98→80 x3, 98→98 x3 (doubled, fenced as formula/residual per vient-98-name clause 2), 98→00 x3, 98→56 x2, 98→20 x2 (@702, @838), then 16 singletons (76, 51, 19, 81, 41, 92, 65, 53, 96, 48, 12, 78, 86, 55, 15, 62, 24, 60, 39).

**Predecessor census:** 62→98 x5, 42→98 x3, 66→98 x3, 98→98 x3, 64→98 x2, 43→98 x2, 01→98 x2, 82→98 x2, 47→98 x2, then singletons incl. 17→98 x1 (only @838), 14→98 x1, 00→98 x1, 16→98 x1, 33→98 x1.

**Complement inventory (the VP-head signature):**
- 83='de' x5 — "vient de X": byte-identical formula `98 83 82 96 21` x3 (@227, @1060, @1783) + @897 `98 83 86 16` ("vient de [86-inf]") + @930 `98 83 56 69` ("vient de [56]").
- 00='pour' x3 — "vient pour X": @1373 `98 00 86 29` ("vient pour [86]er"), @1601 `82 98 00 44` ("m[e] vient pour [44]"), @1137 `98 00 98` (fenced formula cluster @1137–1146 — stated boundary, not load-bearing).
- 82='m' x3 — elided-object complement "vient m'": @19 `98 82 43`, @124 `98 82 48`, @894 `98 82 14` ("vient m'en", 14-residual fenced per re-audit).
- Subject-side contact: 62→98 x5 ("il vient"), 64→98 x2 ("qui vient"), 82→98 x2 ("m(e) vient", clitic-fronted object).

That is the distributional signature of a finite clause-head verb: subject slot left, selected-complement slot right (infinitival via 'de'/'pour', pronominal via elided clitic). 37/40 windows are consistent with the VP-head function; the 3 doubled-98 instances are fenced formula/residual per vient-98-name. The battery-promoted value 'vient' (pending ratification) is used as gloss shorthand; the functional naming rests on contact distribution alone.

### (c2) 98 at @838: clause-terminal, not clause-medial

Row a5_06: `…87 11 77 76 59 35 56 17 [98] 20 62 94 26 12 16 00 33 96 40 62` ("…ce la le 76 est 35 56 fois vient [20] il ne 26 n 16 pour 33 par e il").

1. **Complement inventory absent at @838.** Follower is 20, which is not in 98's complement set {83, 00, 82}. The row tail after @839 (`20 62 94 26 12 16 00 33 96 40 62`) contains no complement of 98: the one 00 there sits inside the particle clause (`16 00 33` = "[16] pour [33]"), governing 33 rightward, six positions downstream of 98 with 20's clause intervening — it cannot be 98's complement.
2. **20 cannot be clause-medial inside 98's clause — re-derived without assuming the boundary.** Noun reading: bare noun after an intransitive finite verb with no preposition — ungrammatical. Det/adj reading: no head to modify (98 is a verb). Medial-adverb reading: French medial adverbs in this slot require the "ne" before them; there is none before 20. So 20 is clause-initial of its own clause under every word-class — the clause break is between @838 and @839 regardless of what 98's value is.
3. **The 98→20 collocation is boundary-shaped at both stream instances.** 98→20 occurs exactly x2 (@702, @838). @702 (`…60 12 [98] 20 12 66 21 35 53`, row a5_01: "…ne [60] n(e) vient [20] n(e) [66]…") also parses only as a clause break before 20. No standing frame re-segments `98 20` (x2, both boundary-shaped) or `17 98 20` (x1, @837–839) as one constituent.
4. **98's clause-medial capacities elsewhere do not transfer.** 98 does occur clause-medially with its complements (`98 83 …` x5, `98 00 …` x2 clean, `98 82 …` x3) — none present here. Postposed material at @1481 (`98 62 46` = "vient il que") is VP-internal, not a threat: at @838 no such material exists.

**Conclusion on (c2):** 98 is clause-terminal at @838. Its clause ends where its complement inventory ends and a clause-initial-shaped 20 begins. The particle battery's stated boundary ("clause boundary after 98 (@838)") is independently confirmed by 98's contact distribution. **The @839 particle face does not re-open.**

## Per-clause pass/fail

- **(c1) PASS.** 98's distributional function named from the n=40 census: finite clause-head verb (subject slot left: 62/64/82 contact; selected-complement slot right: 83 x5 'de'-infinitival, 00 x2–3 'pour'-infinitival, 82 x3 elided clitic), 37/40 consistent, 3 doubled instances fenced as formula/residual.
- **(c2) PASS.** 98 is clause-terminal at @838 (complement inventory absent; no complement in the row tail; 20 unattachable clause-medially under any word-class, re-derived independently; 98→20 x2 both boundary-shaped). The @839 particle face does NOT re-open. Null disjunct does not fire.

## Adverses

None listed in the queue entry. One external tension noted, not an adverse: 98='vient' is battery-promoted, pending red-team ratification — this battery's boundary hardening uses the distributional function (contact inventory), not the value, and stands regardless of ratification outcome.

## Verdict: **PROMOTE** — the @839 clause boundary is hardened

98's distributional function is named with byte evidence (finite clause-head verb, complement inventory {83, 00, 82}); at @838 it is clause-terminal, confirming particle-20-760-839's boundary statement from the contact distribution. No standing or red-team verdict contradicted or downgraded (particle battery's null untouched and strengthened; 98='vient' promote used as gloss only, not re-litigated; §7 intact).

## Caveats and fences (stated, not hidden)

- **Subject of 'vient' at @838 unresolved:** left edge reads "…35 56 fois vient" (35/56 open; 17='fois' immediately precedes). Clause-terminality is established rightward and does not depend on the subject parse; the left edge is flagged for the verb line, not a boundary threat.
- **@1137–1146 formula cluster fenced:** 98→00 x1 of the inventory (@1137 "98 00 98") sits in the fenced doubled-98 cluster; the 'pour'-complement leg rests on @1373/@1601.
- **Canonicality:** row a5_06's upstream offset is unvalidated under the standing canonicality caveat; the verdict holds on the canonical repaired stream per protocol.
- **Scope:** this battery hardens the boundary; it names no value and adjudicates nothing at red-team level.

## Follow-ups

None required (promote, not null). Suggested (non-mandated): `subj-98-838-leftedge` (P4) — name the subject of 98 at @838 ("…35 56 fois vient" left edge; 35/56/76 open) for the verb line; `particle-20-value-rivals` already queued covers the value-naming.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-boundary-98-839.md` (this file)
- Queue: `boundary-98-839` → status `verdict`, result `promote`, report path above, date 2026-10-09 (pre-write assert confirmed queued/verdictless; temp-file + atomic rename; JSON re-validated; only this entry touched; no downgrade)
- Lock created on start, deleted on completion. `canonical.py` never used; R5005, sealed gate instances, red-team adjudication queue untouched.
