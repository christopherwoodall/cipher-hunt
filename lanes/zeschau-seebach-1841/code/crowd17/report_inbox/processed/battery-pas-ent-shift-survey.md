# Battery report: pas-ent-shift-survey

- Target id: `pas-ent-shift-survey`
- Claim: Survey 06's fate at the other three '30 06' windows (1b@1252/@1562/@1734); if 06 is placed in a word at any of them, W3's residual is likelier a parsing artifact than genuine.
- Date: 2026-10-09
- Worker: battery worker (subagent f7ea97df-42c6-4f9e-a696-ad2010f2cb64)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset note: all @-offsets below are 1-based pair indices. "@1252" means 30 is pair #1252 and 06 is pair #1253.

Terms (ASD-STE100): "word" = a French word that the cipher writes with number groups. "placed" = 06 is inside a grammatical French word under standing values. "residual" = 06 is not in a licensed word at this window. "fence" = set aside with a stated cause, not killed. "battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"If 06 is placed at any surveyed window, re-audit the W3 window."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 06 is placed in a grammatical word at surveyed window 1 (1b 30@1252 / 06@1253).
2. **C2:** 06 is placed in a grammatical word at surveyed window 2 (1b 30@1562 / 06@1563).
3. **C3:** 06 is placed in a grammatical word at surveyed window 3 (1b 30@1734 / 06@1735).
4. **C4:** If any of C1–C3 passes, the W3 window re-audit fires.

Placement arms tested at each window (the W3 battery's template, standing values only, no invented values, no polyvalence declared):
- Arm A (left-attach): "30 06" = "pasent". The clerk single-consonant license is KILLED lane-wide (spell-single-consonant) — "pasent" is not a French word.
- Arm B (right-composition): 'ent'+[follower] composes a French word — fires only if the follower has a named value compatible with 'ent'.
- Arm C (other licensed): 82+06 '-ment' (needs 82 immediately left — absent at all windows, left is 30); 06 word-final '-ent' on a verb stem (left is 30='pas', a whole promoted word, not a stem — absent).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/pas-ent-shift-survey.lock` on start (agent id + UTC timestamp); deleted on completion. No fresh lock was present.
2. Re-derived the repaired stream in-session (asserts held: 1,847 pairs, 96 types). Verified the survey's premise byte-level: '30 06' occurs exactly x4 stream-wide at 1-based 30-positions 1252 / 1328 / 1562 / 1734. W3's window (1b 30@1328 / 06@1329) is instance 2 — confirmed.
3. Adopted standing values, not re-litigated: 30='pas' (battery-promoted, pas-30); 06='ent' (battery-promoted verb ending, ent-06; '-ment'=82+06 compositional); 94='ne' (battery-promoted, ne-94); 65 = noun-class, value unnamed (battery-promoted, prof-65); 60 = value open (noun-60, adj-60, dit-60-syncretic all KILLED; no value promoted for 60 anywhere in the queue); 67 et/veut = sole true polyvalence (§7); 62='il' battery-promoted (il-62).
4. Surveyed each window's ±6 context and tested Arms A–C. "Open continuation" (06 word-initial 'ent' with unconstradicted continuation) counts as NOT placed — the W3 report's own fence/place distinction.

## Window-level evidence

**Window 1 — 1b 30@1252 / 06@1253** (rows a7_01/a7_02):
- Context: `33@1246 16@1247 00@1248 67@1249 46@1250 26@1251 30@1252 06@1253 65@1254 46@1255 01@1256 61@1257 31@1258 29@1259 69@1260`
- Arm A: "pasent" — FAIL (kill-grade dead license).
- Arm B: 'ent'+65 — FAIL. 65 is noun-class with NO named value (prof-65 promotes the class only; det-65-gender-adjudicate is NULL). 'ent'+[unnamed noun] composes no French word. (Note: 06@1253 65@1254 46@1255 = "[ent] [65-noun] que 01" — 06 is word-initial 'ent' with open continuation, unconstradicted: the same residual shape as W3.)
- Arm C: left is 30, not 82; no stem to the left. FAIL.
- Structural note: preceded by 26@1251, giving the "26 30 06" trigram (see window 3).

**Window 2 — 1b 30@1562 / 06@1563** (row a8_01):
- Context: `93@1556 61@1557 40@1558 17@1559 11@1560 26@1561 30@1562 06@1563 60@1564 71@1565 50@1566 29@1567 24@1568 74@1569 62@1570`
- Arm A: "pasent" — FAIL (kill-grade dead license).
- Arm B: 'ent'+60 — FAIL. 60's value is open (noun-60, adj-60, dit-60-syncretic KILLED; no promote verdict names a 60 value anywhere in the queue). 'ent'+[unnamed] composes no French word.
- Arm C: left is 30, not 82; no stem to the left. FAIL.
- Structural note: preceded by 26@1561 — the same "26 30 06" trigram as window 1. Both windows residual in the same way: a structural parallel, not a contradiction.

**Window 3 — 1b 30@1734 / 06@1735** (row a8_07):
- Context: `88@1728 24@1729 30@1730 15@1731 01@1732 56@1733 30@1734 06@1735 60@1736 12@1737 48@1738 52@1739 86@1740 12@1741 34@1742`
- Arm A: "pasent" — FAIL (kill-grade dead license).
- Arm B: 'ent'+60 — FAIL (60's value open, same as window 2). Downstream 12@1737 48@1738 = 'n'+'e' (banked letters) attaches to 60, not to 06; no licensed path re-routes 06 into that word.
- Arm C: left is 30, not 82; no stem to the left. FAIL.
- Structural note: the doubled 30 (1b 30@1730 and 30@1734) is the clause-boundary adjacency already recorded in the pas-30 battery; it does not change 06's fate.

## Per-clause pass/fail

- **C1 — FAIL.** 06 is not placed in a word at 1b@1252: all three arms fail. 06's fate = residual (word-initial 'ent' with open continuation), same shape as W3.
- **C2 — FAIL.** 06 is not placed in a word at 1b@1562: all three arms fail. Residual, same shape.
- **C3 — FAIL.** 06 is not placed in a word at 1b@1734: all three arms fail. Residual, same shape.
- **C4 — DOES NOT FIRE.** No placement at any surveyed window, so the bar's trigger condition is cleanly negative: no W3 re-audit is mandated by this battery.

## Adverses (answered, not ignored)

- Target listed adverses: none.
- Self-found adverse: canonical-stream caveat (68 of 70 upstream row offsets unvalidated; rows a7_01/a7_02/a8_01/a8_07 offsets unvalidated). FENCED with stated cause: this survey is parse-internal — it compares the four '30 06' instances within the same repaired parse. A systematic offset error would displace all four instances identically and cannot discriminate placement-vs-residual across instances, so the caveat does not change the survey outcome. The caveat stands lane-wide as before.
- Self-found: windows 1 and 3 share the "26 30 06" trigram — ANSWERED as a structural parallel (both residual the same way), consistent, not a contradiction.

## Verdict: KILL

The bar's testable proposition — "06 is placed in a word at >=1 of the other three '30 06' windows" — fails at all three windows under full battery-grade inspection (Arms A–C exhausted, no invented values, no polyvalence). The artifact-discriminator this survey was chartered to test is rejected at the lane's standard: 06's stranding is consistent across all four '30 06' instances, so W3's residual is genuine under standing values, not a parsing artifact discriminable via the other windows. The bar's trigger does not fire — no W3 re-audit is mandated by this battery. The independently-queued `w3-06-rerun-gated` and `w3-06-a704-validate` (both still queued) remain the vehicles for any future W3 re-audit on their own triggers. No standing or red-team verdict is contradicted or downgraded (30='pas', 06='ent', 94='ne', 65 noun-class, spell-single-consonant KILL, §7 all untouched).

## Follow-ups

None — this is a KILL, not a null. The survey exhausted its axis (all four '30 06' instances share one fate); no narrower bar regenerates useful work here.

## Bookkeeping

- Queue: `pas-ent-shift-survey` → status `verdict`, result `kill`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/pas-ent-shift-survey.lock` created on start, deleted on completion (verified gone).
