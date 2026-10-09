# Battery report: adj-78-fence — FENCE (verdict: null)

- Target id: `adj-78-fence` (priority 3)
- Date: 2026-10-09
- Worker: 632d28b5-0e41-4e35-bc4a-8ab5af5a5b56
- Stream: repaired 1,847-pair parse only (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py`; 1,847 pairs and 96 types asserted in-session). `canonical.py` never used. R5005, sealed gates, and the red-team adjudication queue untouched. No data invented. @-offsets 0-based on the repaired stream.
- Lock: `code/crowd17/next-token/locks/adj-78-fence.lock` created 2026-10-09T03:43:49Z (no stale lock; no prior lock for this id), deleted on completion.

## Bar (verbatim from battery-queue.json — pre-registered BEFORE testing)

"fence 78-adjective iff no adjective-shaped frame besides @1542 stands; name 78=adjective iff a second independent leg is found"

## Numbered clauses (frozen before testing; not modified after seeing data)

1. **C1:** no adjective-shaped frame besides the brief's @1542 stands on the repaired stream → fence the 78-adjective reading.
2. **C2:** a second independent adjective-shaped leg is found → name 78=adjective.

## Method

1. Read BATTERY-PROTOCOL.md in full, then the evidence report `code/crowd17/report_inbox/processed/battery-adj-groundwork-refollower.md` (78 census; proposed this target) and the directly-on-point `code/crowd17/report_inbox/battery-ver78-la78-census.md` (null, 2026-10-08: the 9 'le/la 78' windows tested as noun-head frames under 78='ver'; coordinated, not duplicated).
2. Re-derived the full 78 census independently on the repaired stream: **78 n=31** (groundwork said 33; I work from my own byte counts). Offsets: @8, @214, @297, @313, @352, @364, @415, @435, @443, @476, @492, @573, @629, @648, @819, @879, @982, @1012, @1078, @1105, @1140, @1164, @1181, @1352, @1397, @1543, @1621, @1670, @1758, @1771, @1843.
3. Classified every window against adjective-shaped frames of 1841 French: prenominal (DET+ADJ+N), postnominal (DET+N+ADJ), predicative (59-copular — none present), tout-intensifier (no 79+78 contact exists).
4. Standing values used (§7): banked 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; provisional 59=est, 77=le; battery-level 94=ne, 12=n, 48=e, 06=ent, 30=pas; R16-005 78='ver' LEAD (used only as coordinated standing, never as granted); 37's sub-lexical value owned by S5 (per adverses — not decided).

## Window-level evidence (@-offsets, all re-derived; ±5 context)

Claim's collocation counts verified: '37 78' x4 (@313, @415, @476, @1771) — nominal context per adverses; '47 78' x5 (@364, @819, @982, @1105, @1397) — "ce 78" pronominal-shaped. Neither is adjective-shaped.

**DET+78+X candidates (the only prenominal-shaped windows stream-wide):**
- @8: `41 06 77 [78] 18 93 62` — "le[77] 78 18"; 18 n=7, class fully open. No adjective frame stands (18 unvalued).
- @214: `19 74 77 [78] 06 59 46` — "le 78 ent[06]". la78-census soft-failed this window for noun-head too (06-strain shared with the lever rival); no adjective parse stands.
- @297: `01 11 [78] 40 97 86` — "la 78 e[40]"; fenced by the la78-census bar clause (b) as the R16-005 1-window residual ('l'ere'-shaped, votes 'er'). Not an adjective frame.
- @648: `88 77 [78] 52 82 94` — "le 78 52"; 52 open. la78-census parsed it noun-head ("le ver | [52]..."). No adjective frame stands.
- @1078: `12 48 77 [78] 64 06 52` — "le 78 qui[64]" — textbook noun-head + relative clause (64=qui promoted). Nominal, not adjectival.
- @1181: `32 48 59 37 77 [78] 94 82 06` — "le 78 | ne mentent" — noun-head flagship frame. Not adjectival.
- @1352: `62 48 77 [78] 94 82 06 52` — "le 78 | ne me[nt]..." — noun-head. Not adjectival.
- @1543: `93 88 77 [78] 43 00 46` — the brief's "@1542" (1-index offset difference; same window: "93 88 77 78 43 00 46"). "le 78 43": 43 is **noun-profiled** ("par 43" x2, "43 pour" x3; noun-43 queued) — not epithet-shaped. la78-census soft-failed even the noun-head parse here ("43 admits no clean integration") and fenced the window to the lever rival. **The sole claimed prenominal leg does not stand as an adjective frame.**
- @1670: `91 11 [78] 55 81 92` — "la 78 55"; 'la verte'-shaped needs 55=adjective — assumption-only (55's own adjective leg @1205 is single and independent of 78). la78-census soft-failed it ("55 81" bond unexplained). No adjective frame stands.

**Other 78 windows:** postnominal requires a standing noun immediately left of 78 — left-neighbor inventory {77x7, 11x2, 47x5, 87x2, 37x4, 67x4, 86, 98, 84, 16, 50, 80, 17, 93, 88} contains no standing noun: **zero postnominal legs**. No 59+78 contact (no predicative leg). No 79+78 contact (no tout-intensifier leg). 'ce 78 e' windows (@364/@819/@1397 "47 78 48/40"): 48/40='e' is letter-tier; "ce 78-e" is not a standing adjective frame (78 is word-final per inf-37-78-475 promote and W1).

## Per-clause pass/fail

1. **C1 — FIRES.** No adjective-shaped frame besides @1543 stands: the 9 DET+78 windows parse as noun-head (la78-census, 5/9 with stated fences) or soft-fail; @297 is fenced; @1543 itself fails as an adjective frame (43 noun-profiled, not epithet-shaped); zero postnominal, zero predicative, zero tout legs. **78-adjective is FENCED.**
2. **C2 — FAILS.** No second independent adjective leg exists — not even a first leg stands. Nothing to promote.

## Adverses (answered, none ignored)

- "37's sub-lexical value owned by S5 — do not decide 37": honored. @313/@415/@476/@1771 treated as nominal-context evidence only; nothing about 37 decided.
- "'37 78' windows are nominal-context evidence only": honored — excluded from adjective-frame candidacy.

## Standing-state check (no contradiction)

- R16-005 78='ver' LEAD: untouched (fence removes the adjective rival, does not promote or kill the lead).
- inf-37-78-475 promote (78 word-final) and W1: consistent — the fence is on the adjective reading only.
- ver78-la78-census null, ver-78 null, ver-78-rebar null, ver78-ce78-open-succ kill, ne-le-1075 kill, rpos-w1-exception promote: all respected; this battery duplicates none of them (adjective reading was untested by all).
- No existing verdict downgraded. §7 sole-polyvalence (67) untouched; no polyvalence declared.

## Verdict: NULL (fence executed)

C1's fence arm fired; C2's naming arm failed. Not kill-grade: no window forces the adjective reading false (the failure is evidential emptiness, not a forced contradiction), and the bar prescribes the fence as the outcome rather than a kill. 78-adjective is set aside as a fenced residual, revivable only by the gated follow-ups below.

## Follow-up targets (null regeneration; for the supervisor to queue)

1. **adj-78-1543-43-gate** (priority 3): terminal adjudication of @1543 once 43's value is named (noun-43). Bar: if 43 resolves to a noun value, @1543 is DET+N+N and the 78-adjective reading is terminally fenced; revive only if 43 resolves adjective-shaped. Adverses: 43 noun-profiled on current evidence — expect terminal. Evidence: this report §@1543; la78-census soft-fail; "par 43" x2 / "43 pour" x3.
2. **adj-78-1670-55-gate** (priority 3): re-test @1670's 'la verte'-shaped reading once 55's class resolves. Bar: revive 78-adjective iff 55=adjective with 55's own independent legs; fence terminally iff 55 resolves non-adjective. Adverses: do not invent syllable values for 55/81; coordinate with noun-81. Evidence: this report §@1670; "55 81" x6 bond.
3. **adj-78-18-class** (priority 3): test 18's class across its 7 windows (@8: "le 78 18"). Bar: revive 78-adjective iff 18 resolves adjective in a DET+78+18 prenominal frame with <=1 ungranted assumption; fence the @8 leg otherwise. Adverses: 18 class fully open — no invention. Evidence: this report §@8; 18 n=7, all contacts x1.

## Constraints respected

§7 banked/promoted/provisional/killed/split/held values respected; 67 sole polyvalence untouched; uniformity law and canonicality caveat noted. canonical.py never used. No invented numbers: every count re-derived on the repaired 1,847-pair parse in-session. R5005, sealed gates, red-team queue untouched.

---
Lock: `locks/adj-78-fence.lock` created 2026-10-09T03:43:49Z, deleted on completion of this report.
