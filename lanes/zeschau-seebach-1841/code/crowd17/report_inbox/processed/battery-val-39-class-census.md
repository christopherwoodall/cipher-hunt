# Battery val-39-class-census — verdict: KILL (verb-39 arm)

Target: `val-39-class-census`. Worker: 5d4b2666-c7b3-446d-995c-dd817d33289e. Date: 2026-10-09.

## Bar tested (verbatim, pre-registered)

"promote verb-39 iff >=2 independent verb-frame legs; else fence"

Numbered clauses:
- **C1** (promote verb-39): FAIL — 0 independent verb-frame legs across all 13 windows of 39.
- **C2** (else fence): FIRES — exceeded to kill grade: 4 independent windows force 39 non-verb at kill grade.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `code/side-keyhunt/repair_parse.py`). Asserts held: 1,847 pairs,
96 types. `canonical.py` never used. n(39)=13; all windows graded with ±5
context against standing values only (kill-grade legs use granted/GT values;
battery-grade legs noted as such).

Standing values used: 11=la, 70=pre, 82=m, 29=er, 40=e, 46=que (pencil GT);
87=ce, 64=qui, 96=par, 17=fois (granted); 00=pour (A9), 84=on (A15), 47=ce (A4),
79=tout (A5) (promoted); 59=est (provisional); 94=ne (strong lead);
88 verb-frame A8 (granted frame); 37/32 verb-class (GT letter).
R17-005: 39=/a/ allophone at LEAD tier (confirmed R20-010) — not contradicted.

## Findings — window-by-window (0-based @)

1. **@37** `37 64 32 01 08 91 | 39 | 64 41 01 24 88` — **KILL at kill grade.**
   "…[91] [39] qui [41]…": 64=qui is GRANTED. A verb directly followed by
   relative "qui" is ungrammatical in French; the only grammatical reading
   makes 39 the nominal antecedent of the relative clause ("[91] [39-N]
   qui [41]…"). Verb-39 forced false.
2. **@503** `47 11 29 40 56 | 39 | 68 21 67 77 62` — indeterminate.
   Letter-tier composition ("ce"+"la"+"er"+"e" = "cela"+"ere"…) leaves 39
   inside a letter/syllable tier; no verb frame statable.
3. **@600** `85 01 29 40 03 | 39 | 26 96 45 93 54` — indeterminate.
   39 as standalone verb would need 03 nominal (ungranted); 85-stem left
   context admits word-internal 39.
4. **@607** `96 45 93 54 64 | 39 | 64 02 58 47 77` — indeterminate (hostile).
   "qui [39] qui": the second "qui" (granted) has no antecedent/role under
   either verb-39 or noun-39; window resists all standalone readings.
5. **@692** `65 94 29 60 03 | 39 | 74 46 02 50 45` — battery-grade anti-verb.
   65=noun-class; 94=ne (strong lead) must directly precede its verb
   (modulo clitics); "er 60 03" intervene between "ne" and 39, so
   standalone-finite-39 is excluded — 39 is word-internal or the window
   is unparseable.
6. **@764** `40 20 62 94 59 | 39 | 88 66 98 80 10` — **KILL at kill grade.**
   "ne est [39] [88]": 59=est provisional, 94=ne strong lead, 88 granted
   verb-frame A8. "n'est [39-Vfin] [88-V]" = two adjacent verbs — no French
   license; "n'est [39-inf] [88]" and "n'est [39-pp] [88]" equally
   ungrammatical. No verb-39 reading; 39 must be nominal/adjectival (with
   a clause boundary) or the locus is unparseable.
7. **@1068** `96 21 62 18 70 | 39 | 11 44 74 42 98` — **KILL at kill grade.**
   70=pre is a BOUND pencil-GT syllable immediately left-adjacent: "pre[39]"
   is one word, 39 is word-internal (syllable/stem tier). Standalone verb-39
   impossible.
8. **@1333** `06 62 94 70 52 | 39 | 83 86 71 64 60` — indeterminate.
   "ne pre[52] [39] de [86]": "ne" separated from 39 by "pre[52]";
   52 unvalued; no clean verb frame.
9. **@1491** `24 87 08 31 92 | 39 | 24 00 66 15 59` — indeterminate.
   "…[92] [39] en pour [66]": "en pour" is ungrammatical under every
   39 reading; no verb leg.
10. **@1512** `56 41 12 61 59 | 39 | 81 88 11 31 11` — indeterminate.
    "est [39] [81] [88-V]": no finite/infinitive/participle reading gives
    39 a verb frame; predicative nominal/adjective possible with boundary.
11. **@1605** `82 98 00 44 70 | 39 | 11 92 65 23 08` — **KILL at kill grade.**
    Second "pre[39]" window (bound 70 left-adjacent): "pour [44] pre[39]
    la [92]…". 39 word-internal; standalone verb-39 impossible. Independent
    of @1068 (different row, different frame).
12. **@1676** `55 81 92 60 03 | 39 | 74 77 44 00 46` — indeterminate.
    Standalone verb-39 would need 03 nominal (ungranted).
13. **@1726** `11 52 37 43 98 | 39 | 88 24 30 15 01` — battery-grade anti-verb.
    98='vient' (lead), 88 verb-frame (granted): "[98] [39-V] [88-V]" =
    adjacent verbs, ungrammatical; 39 must be non-verb (nominal with
    boundary).

Tally: 0 independent verb-frame legs; 4 kill-grade anti-verb windows
(@37, @764, @1068, @1605); 2 battery-grade anti-verb (@692, @1726);
7 indeterminate. C1 fails; the verb-39 arm is dead at kill grade, not
merely unfound.

## Scope

- Kills ONLY the verb-39 arm (standalone finite/stem verb 39). 39's class
  stays open: nominal-39 is forced at @37 (relative-clause antecedent),
  syllable-tier 39 forced in "pre[39]" ×2 (@1068, @1605).
- R17-005 (/a/ allophone, LEAD) untouched — compatible with all findings.
- **Route E at @609 does NOT re-open**: the claim's re-open condition
  (forced verb-39) is dead, so the second-"qui" attachment question is
  unchanged.
- No standing/red-team verdict contradicted or downgraded; §7 intact.
  Canonical-stream caveat stands.

## Natural next questions (recommendations; not queued by this worker)

1. `nominal-39-37` (P3) — name nominal-39's value at @37 ("[91] [39-N]
   qui [41]…") with zero new assumptions.
2. `syllable-39-pre` (P3) — state 39's syllable content in "pre[39]" ×2
   (@1068, @1605) with byte/lexicon evidence.

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/val-39-class-census.lock` created on
  start (agent id + 2026-10-09T15:40:00Z), deleted on completion.
- Queue: `val-39-class-census` → `status: verdict`,
  `verdict: {result: "kill", report: "code/crowd17/report_inbox/battery-val-39-class-census.md", date: "2026-10-09"}`.
  Pre-write assert passed (was queued/verdictless); temp-file + rename;
  disk re-read confirms verdict/kill; own entry only; no downgrade.
- R5005, sealed gates, red-team adjudication queue untouched.
  `canonical.py` never used. §7 uncontradicted.
