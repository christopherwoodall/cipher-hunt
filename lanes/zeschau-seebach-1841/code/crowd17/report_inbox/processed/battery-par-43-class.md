# Battery `par-43-class` — verdict: PROMOTE

## Bar (verbatim from battery-queue.json, pre-registered before testing)

> "Class named at battery grade with zero contradiction across all 43 windows' predecessors; else fence."

Numbered clauses:
- **C1:** 43's class is named at battery grade at the 'par [43]' windows (0-based @343/@1027; byte-identical '45 64 96 [43] 87 01' = 'ce qui par [43] ce [01]').
- **C2:** Zero contradiction with the named class across all 16 43-windows' predecessors.
- **C3:** Else-arm: if C1 or C2 fails, fence with stated cause.

Claim (verbatim): "Name 43's class at the 'par [43]' windows (byte-identical '45 64 96 [43] 87 01' @343/@1027 = 'ce qui par [43] ce [01]'); 'par' takes a nominal complement in 1841 French." Adverses: none.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair / 96-type stream in-session exactly like `code/side-keyhunt/repair_parse.py` from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (byte-exact two-char cells; asserts held: 1,847 pairs, 96 types, 70 rows). `canonical.py` never used. @-offsets are 0-based pair positions (battery convention). 1841 diplomatic French only. R5005, sealed gate instances, red-team adjudication queue untouched. No data invented.

Adopted, not re-litigated (protocol §5 — never downgrade):
- R19-045: 43=["noun","cls"] at class tier, value open; @21 excluded (R19-063: no second polyvalence; §7 holds). Value hunt open: {nature, nécessité} live; {suite, manière, condition, mesure} killed (R19-046/063).
- Standing values: 96='par' (granted), 45='ce' (A11 hold), 64='qui' (granted), 87='ce' (granted), 11='la', 47='ce' (A4), 46='que' (GT), 82='m' (GT), 06='ent' (R17-007 conditional), 37/32 predicative (A1), 88 verb-frame (A8), 78='ver' (LEAD, value open).

## Window-level evidence

n(43)=16, all 16 censused byte-exact. The 'par [43]' 6-gram '45 64 96 43 87 01' occurs exactly 2x stream-wide (byte-identical), 0-based @340–345 (row a2_05) and @1024–1029 (row a6_02/a6_03).

### C1 — the 'par [43]' windows

- @343 (row a2_05): `…45 64 96 [43] 87 01 06…` = "ce qui par [43] ce [01]…"
- @1027 (row a6_03): `…45 64 96 [43] 87 01 03…` = "ce qui par [43] ce [01]…" (byte-identical on the 6-gram; right continuation differs)

'par' takes a nominal complement in 1841 French. Under standing values the sequence is "ce qui par [nominal] ce [01]" — 43 occupies a licensed nominal slot after 'par'. Nothing forces a non-nominal reading at either window. C1 PASS.

Value-level corroboration (class only per bar, but supports the open value hunt): the live value candidates {nature, nécessité} are both idiomatic after 'par' in the lane's period corpus (`code/side-period/corpus/`): 'par nécessité' attested (re-confirmed), 'par nature' ×12.

### C2 — predecessor census across all 16 windows

| @ | pred | window | nominal-43 fit |
|---|------|--------|----------------|
| 21 | 82='m' (GT) | `64 98 82 [43] 29 47 33` | EXCLUDED from noun-43 by R19-045 itself (en43 word-internal letter use); standing carve-out, not a contradiction |
| 43 | 88 (A8 verb-frame) | `01 24 88 [43] 81 30 62` | infinitive-shaped 88 + [43] = direct-object slot; nominal consistent |
| 244 | 56 (verb) | `12 16 56 [43] 00 66 91` | verb + [43] = object slot; nominal consistent |
| 258 | 32 (A1 predicative) | `01 91 32 [43] 77 84 74` | predicative + [43] + 'le'; nominal-complement position; consistent |
| 343 | 96='par' | C1 | nominal |
| 386 | 37 (A1 predicative) | `52 38 37 [43] 91 36 62` | predicative + nominal slot; consistent |
| 439 | 46='que' (GT) | `63 45 46 [43] 98 80 50` | "que [43] [98-fin]" = relative subject of a finite verb; strong nominal leg |
| 563 | 11='la' (GT) | `30 67 11 [43] 24 80 97` | "la [43] [24-fin]" = DET + noun + finite verb; strong nominal leg |
| 1027 | 96='par' | C1 | nominal |
| 1092 | 06='ent' (R17-007) | `79 80 06 [43] 07 55 81` | "tout [80]ent [43]" — 43 after the verb complex; nominal complement; consistent |
| 1126 | 37 (A1 predicative) | `11 52 37 [43] 00 86 52` | predicative + [43] + 'pour' + INF; nominal governing pour-INF; consistent |
| 1204 | 47='ce' (A4) | `45 58 47 [43] 55 61 21` | "ce [43]" = determiner + noun; strong nominal leg |
| 1303 | 08 (unvalued letter) | `70 37 08 [43] 21 43 77` | nothing forces non-nominal; consistent |
| 1305 | 21 (unvalued) | `08 43 21 [43] 77 74 52` | doublet '[43] 21 [43] le'; unvalued 21 names nothing; consistent |
| 1544 | 78='ver' (LEAD) | `88 77 78 [43] 00 46 70` | "le [78] [43]" — appositive/modifier after a nominal head; nominal consistent (clause-level reading already fenced by frame-43-00-boundary; the noun class is untouched) |
| 1724 | 37 (A1 predicative) | `11 52 37 [43] 98 39 88` | predicative + [43] + finite verb; nominal consistent |

Zero contradiction with nominal-43 in any window. Positive nominal legs: @563 ('la [43]'), @1204 ('ce [43]'), @439 ('que [43] [finite]'). C2 PASS (the @21 exclusion is the standing R19-045 carve-out, adopted as premise).

## Per-clause verdicts

1. **C1 — PASS.** 'par [43]' licenses nominal-43 at battery grade at both byte-identical windows; 'par' + noun is the canonical 1841 government.
2. **C2 — PASS.** All 16 predecessors surveyed; none contradicts noun-43; three windows are positive nominal legs.
3. **C3 — does not fire.**

## Verdict: PROMOTE

43's class is confirmed at battery grade at the 'par [43]' windows with zero contradiction across all 16 windows' predecessors. This is delivered as a battery-grade confirmation package **consistent with the standing red-team grant** (R19-045, registry ["43","noun","cls"]) — no new class is declared, no registry change is requested, no value is named (value hunt stays open with {nature, nécessité}), and no new red-team act is requested. No standing or red-team verdict is contradicted or downgraded; §7 intact (67 sole polyvalence); no polyvalence declared. Canonical-stream caveat stands (68/70 row offsets unvalidated).

Lock: created `code/crowd17/next-token/locks/par-43-class.lock` on start; no stale-lock note needed; deleted on completion.
