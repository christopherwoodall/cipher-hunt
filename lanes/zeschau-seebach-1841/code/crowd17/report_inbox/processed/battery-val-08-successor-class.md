# Battery report: val-08-successor-class — verdict: PROMOTE

**Target:** `val-08-successor-class`
**Date:** 2026-10-09
**Stream:** repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, re-derived in-session; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim)

"classes named at battery grade"

Numbered clauses:
- **C1:** 31's class named at battery grade.
- **C2:** 62's class named at battery grade.
- **C3:** 65's class named at battery grade.
- **C4:** 21's class named at battery grade.
- **C5:** 43's class named at battery grade.
- **C6 (claim's frame test):** decide whether 08 licenses a coherent frame class from the right (particle-like) or is word-internal.

## Method

Full 08 census: n(08)=18. Followers: 31×3, 65×2, 62×2, 91/34/21/67/24/52/29/01/43 ×1. For each of the five named followers, every 08-window was pulled byte-exact (±4), the follower's class was determined from standing grants plus window frames, and 08's attachment direction was tested from the left neighbor's wordhood (a complete-word left neighbor forces right-attachment; "40 08"="et" proves left-attachment).

## Findings

### C1 — 31: SPLIT (finite VERB / word-internal SYLLABLE). PASS.

- **Verb arm (battery grade, 2 independent legs):** "qui [31]" at @338 (a2_05: `64 31 14`) and @1647 (a8_04: `64 31 10`). 64=qui is granted; a relative pronoun must be followed by a verb. (Matches val-31-verb-test C1.)
- **Syllable arm (battery grade, 3 legs):** at all three 08-windows the left neighbor is a proven complete word, forcing 08 to attach right, so "08 31" is a word-initial "t[31]" unit and 31 is word-internal:
  - 08@881 → 31@882 (a5_08): left 17=fois, granted standalone in all 15 windows (x17-wordbound-audit, battery grade). Window: `17 08 31 79`.
  - 08@1488 → 31@1489 (a7_10): left 87=ce, granted word (§7). Window: `87 08 31 92`.
  - 08@1520 → 31@1521 (a7_11): left 67=et/veut; positional rule gives 67="et" here (follower 08='t' is not infinitive-shaped), a complete word. Window: `67 08 31 24`.
- Consistent with the surviving word-internal arm at @1257 (val-31-1257-word NULL).

### C2 — 62: NOUN. PASS.

- 08@944 → 62@945 (a5_10): `40 08 62 98` = "et [62] vient". "40 08" is "et" (val-08 PROMOTE), a complete word, so 62 opens a new word; 98=vient (LEAD) is finite, so 62 is its subject → noun. Zero new assumptions.
- 08@1323 → 62@1324 (a7_04): `80 08 62 98` — 62 again directly pre-verbal to "vient" → noun subject (corroborating leg). ("08 62" as one word is impossible: 62 is a noun root, "t"+root is not a word; 08 attaches left.)
- Standing: 62='il' killed at kill grade (R19-106/R20-125); noun-root tie (règne/trône) open but both are nouns.

### C3 — 65: NOUN. PASS.

- Standing red-team grant: 65 is noun-class (R20-047).
- 08@922 → 65@923 (a5_09): `40 08 65 71` = "et [65] …" — new word after "et" → noun, consistent with grant.
- 08@1339 → 65@1340 (a7_05): `60 08 65 64` = "…[65] qui…" — 64=qui follows, so 65 is the relative pronoun's nominal antecedent. ("t"+noun-word impossible → 08 attaches left; "[60t]" left contact unresolved, does not touch 65.)

### C4 — 21: NOUN (battery grade), with one fenced verb-forcing tension. PASS.

- **Noun legs (5, battery grade):**
  - "par [21]" ×3: @231 (a2_01: `96 21 60`), @1064 (a6_04: `96 21 62`), @1787 (a8_09: `96 21 68`). 96=par is granted; a preposition cannot be followed by a finite verb → noun (infinitive marginal, noun clean).
  - "[21] qui" ×2: @937 (a5_10) and @1631 (a8_03), both `33 21 64` — 21 as nominal antecedent of the relative pronoun.
- **Fenced tension:** @134 (a1_04): `64 21 65` = "qui [21] [65-noun]" — "qui" must be followed by a verb, forcing a verb reading here. Single leg: below battery-grade threshold for a split declaration. Fenced with cause (needs a second verb-frame leg or a "64 21" wordhood re-parse); does not overturn the 5 noun legs.
- At the 08-window (08@98 → 21@99, a1_02: `85 08 21 62`), 21's class is not independently discriminated; the noun classification rests on the 5 global legs.

### C5 — 43: NOUN. PASS.

- Standing red-team grant: 43=["noun","cls"] (R19-064, re-confirmed R20-117).
- 08@1302 → 43@1303 (a7_03): `37 08 43 21`. "08 43" as one word ("t"+noun-word) is implausible, so 08 attaches left and 43 stands as its own word → consistent with the noun grant. ("[37t]" left contact unresolved; does not touch 43.)

### C6 — 08 does NOT license a coherent frame class; 08 is word-internal 't'. Particle hypothesis KILLED.

- **Bidirectional attachment (proven both ways):** left-attachment at 08@922 and 08@944 ("40 08"="et", val-08 PROMOTE); right-attachment at 08@881/@1488/@1520 ("08 31" with complete-word left neighbors, C1). A particle has fixed directionality; a word-internal letter does not.
- **Heterogeneous right-neighbors:** nouns (62, 65, 43), verbs (24=faire at 08@534, finite-31), conjunction (67=et at 08@198), GT letters (34=i at 08@60, 29=er at 08@779). A particle selects one complement class; 08 selects none.
- **Corroborating 't' compositions:** "45 08"=@975 and "47 08"=@1592 (47=ce A4, 45=ce A11) parse as "cet" (ce+'t' before vowel); "37 08 29"=@779 gives "t"+"er"="ter" syllable contact. All word-internal.

## Per-clause results

| Clause | Result |
|---|---|
| C1 (31) | PASS — SPLIT: finite VERB ("qui [31]" ×2) / SYLLABLE ("t[31]" ×3) |
| C2 (62) | PASS — NOUN ("et [62] vient", "[62] vient") |
| C3 (65) | PASS — NOUN (R20-047 grant + "et [65]", "[65] qui") |
| C4 (21) | PASS — NOUN ("par [21]" ×3, "[21] qui" ×2); @134 verb tension fenced |
| C5 (43) | PASS — NOUN (R19-064/R20-117 grant, @1302 consistent) |
| C6 (frame test) | 08 word-internal 't'; particle hypothesis KILLED |

## Verdict: PROMOTE

All five follower classes named at battery grade; no listed adverses (target carries none); no standing/red-team verdict contradicted; §7 intact (no new polyvalence declared — 31's and 21's splits are positional/class splits, both arms evidenced, neither names a second value).

## Scope

Names classes only, not values. 31's split is battery-grade on both arms; 21's @134 tension is fenced, not resolved (see follow-up). The particle-kill for 08 sharpens val-08's 't' PROMOTE: 08 is a word-internal letter, never a governing particle.

## Follow-ups (tension only, not required by verdict)

1. `verb-21-second-leg` (P3) — find a second verb-frame 21 window ("qui 21" or finite-frame) to battery-grade the @134 verb arm, or re-parse "64 21" wordhood; decides whether 21's split is real.
2. `cet-08-975-1592` (P4) — verify "cet" parses at @975/@1592 against 01's and 81's vowel-initial status once valued; hardens 08='t' left-attachment.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-08-successor-class.md`
- Queue: `val-08-successor-class` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; own entry only; no downgrade)
- Lock `code/crowd17/next-token/locks/val-08-successor-class.lock` created on start (agent d9b777a6-5ef6-4596-9412-674014a7aa37, 2026-10-09T17:32:01Z), deleted on completion.
