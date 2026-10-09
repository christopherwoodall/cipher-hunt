# Battery verdict: class-41-contact

**Worker:** d3ba2329-e5fd-497f-91c3-af9f8c82fd82
**Date:** 2026-10-09
**Verdict: NULL** — no uniform class covers the three standing-value contacts; 41 is a §7 split candidate (verb @40 vs determiner @238). No polyvalence declared at battery level; split candidacy escalated to the red team.

## Method
- Read BATTERY-PROTOCOL.md first; lock created on start, deleted on completion.
- Stream re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py`: 1,847 pairs / 96 groups verified.
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered)

> "verb/noun/determiner discriminator; coordinate with (do not duplicate) any queued 41-class work"

Restated as numbered clauses:
- **C1:** name 41's class via the three standing-value contacts (@40 'qui(64) [41]', @1017 'faire(24) [41]', @238 '[98] [41] fois(17)'), tested as verb/noun/determiner — PASS iff exactly one class survives all three contacts.
- **C2:** coordinate with (do not duplicate) other queued 41-class work — PASS iff no duplication occurred.

## Census (all re-derived, 1-based offsets)

41 n=19. Windows with 1-based @, row, pre/suc context:
- @6 (a1_00): 47 41 06
- **@40 (a1_01): 64 41 01** ← standing-value contact 1
- @60 (a1_01): 12 41 08
- @92 (a1_02): 19 41 98
- **@238 (a2_01): 98 41 17** ← standing-value contact 3
- @445 (a2_09): 78 41 10
- @490 (a2_11): 42 41 20
- @590 (a3_02): 97 41 41
- @591 (a4_00): 41 41 09
- @809 (a5_05): 24 41 12
- @965 (a6_00): 56 41 19
- **@1017 (a6_02): 24 41 15** ← standing-value contact 2
- @1049 (a6_04): 85 41 88
- @1112 (a6_06): 73 41 65
- @1473 (a7_10): 12 41 53
- @1500 (a7_11): 89 41 74
- @1509 (a7_11): 56 41 12
- @1536 (a8_00): 73 41 62 (subj-62-06-1537's window — not re-litigated)
- @1760 (a8_08): 78 41 15

## Per-clause results

**C1 — FAIL (no uniform class).** Contact-level discrimination:

| Contact | Window (1-based) | verb-41 | noun-41 | determiner-41 |
|---|---|---|---|---|
| 1 | @40: `64(qui) 41 01` | PASS ("qui [verb]" relative clause) | FAIL ("qui [noun] [01]": 01 never verb-shaped, so no verbal head follows the noun) | FAIL ("qui [det] [01]": 01 is 'en'/'ci'-shaped, never a nominal head) |
| 2 | @238: `98 41 17(fois)` | FAIL ("[verb] [verb] fois": two finite verbs in sequence) | FAIL ("[verb] [noun] fois": bare noun before "fois" is ungrammatical — "fois" requires a determiner/quantifier) | PASS ("vient [det] fois": "chaque fois"/"une fois"-shaped) |
| 3 | @1017: `24(faire) 41 15` | PASS ("faire [inf]") | PASS ("faire [noun]" direct object) | CONDITIONAL ("faire [det] [15]": needs nominal 15; 15's value open) |

- 64='qui' is granted; 24='faire' is battery-promoted (imp-80-set); 17='fois' is promoted; 98 is battery-promoted finite verb (prof-98, pending ratification — verb-class suffices for the "two finite verbs" rejection).
- Contact 1 forces **verb**; contact 2 forces **determiner**; contact 3 is compatible with all three. No single class survives all three contacts → bar fails at class-uniformity grade, epistemic (open values at 01/15 could in principle reframe contacts 1/3, but contact 1 vs contact 2 is a direct verb-vs-determiner clash under banked values).

**C2 — PASS (no duplication).** Queued 41-class work: `venir-a-1841-corpus` (period-corpus check, no overlap) and `subj-62-06-1537` (41 as 3pl subject at @1536 — different window, not touched here).

## Adverses answered
- "no candidate value parses ≥2 windows (class open)" → answered at class level: the issue is not that no *value* fits two windows, but that no *class* fits @40 and @238 together. Value-naming is moot until the class question is adjudicated.
- "'donne'-window @58 is the W2 forced contradiction from prof-53, not a leg" → honored. Byte-check: 1-based @58–64 = `11 79 85 58 35 53 12 41 08` (row a1_01): 41 sits in the letter slot of the "53 12 [41]" composition ("don"+'n'+[41]). donn-41-44's letter-kill ('41 41' doubling @590–591, "ee" not a French digraph) holds — 41 is word-internal here, not word-level. Kept excluded as a leg; it additionally reinforces the split picture (a third, word-internal role for 41).

## Standing-state check
- donn-41-44 (null, 2026-10-09): its findings adopted, not re-litigated; nothing contradicted.
- subj-62-06-1537 (queued): untouched.
- No red-team verdict on 41 exists; no standing verdict contradicted or downgraded. §7 intact — no polyvalence declared; the split is a *candidacy* for the red team.

## Headline for the red team
41 shows three incompatible roles under standing values: **verb** at @40 ("qui [41]"), **determiner** at @238 ("[98] [det] fois"), **word-internal letter** at @61 ("53 12 [41]"). This is a §7 split candidacy — red-team adjudication territory.

## Follow-ups proposed (for supervisor queuing)
1. `val-41-det-windows` (P3) — sweep the determiner-shaped 41 windows (@238 + any quantifier/"fois"-frame windows) to package the determiner arm for the red team.
2. `verb-41-value` (P3) — discriminate verb values at @40 ("qui [verb] [01]"): test infinitive vs finite via 01's value.
3. `split-41-redteam` (P2) — package the §7 split candidacy (verb @40 vs determiner @238 vs letter-slot @58–61) as a red-team adjudication docket item.
