# Battery report: adj-91-723-second-leg (NULL — fence executed)

**Target:** adj-91-723-second-leg (priority 3). Worker session 320b7625-2b54-49f9-bbcc-3e4de9821bd6 (supervisor-dispatched). Date: 2026-10-09.
**Stream:** repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`; 1,847 pairs, 96 groups, asserts hold). `canonical.py` never used. R5005 untouched. Sealed gates untouched. Red-team adjudication queue untouched. No data invented. @-offsets 0-indexed on the repaired stream.
**Lock:** `code/crowd17/next-token/locks/adj-91-723-second-leg.lock` created on start (no stale lock existed; no prior lock for this id), deleted on completion.

## Bar (verbatim from battery-queue.json — pre-registered BEFORE testing)

"name 91=adjective iff >=2 independent adjective-shaped windows stand; fence iff the @723 window stands alone"

## Bar as numbered pass/fail clauses (frozen before testing; not modified after seeing data)

1. **C1 (naming arm):** >=2 independent adjective-shaped windows for 91 stand → name 91=adjective.
2. **C2 (fence arm):** @723 stands alone as the sole adjective-shaped window → fence the adjective reading.

## Method

1. Read BATTERY-PROTOCOL.md in full. Read the evidence report processed/battery-adj-groundwork-refollower.md (91 census n=21, "exactly ONE adjective-shaped window (@723)").
2. Re-derived the full 91 census independently on the repaired stream (n=21, byte-identical to groundwork: @15/@36/@137/@247/@256/@277/@301/@387/@390/@520/@538/@723/@852/@1005/@1019/@1371/@1428/@1518/@1668/@1698/@1798).
3. Tested every window against standing-value adjective frames (protocol §7): prenominal DET(11/77/87/47)+91+N; postnominal DET+N+91; bare N-91 / 91-N with N in nominal-supported {03,43,17} or noun-class 36. Banked values: 11=la,70=pre,82=m,34=i,29=er,40=e,46=que; granted 87=ce,64=qui,96=par,17=fois,79=tout,00=pour,84=on,47=ce; provisional 59=est,77=le; battery-promoted 94=ne,12=n,48=e,06=ent,30=pas,39=/a/; 36=noun-class (R18); 67=et/veut sole polyvalence.
4. Adjudicated the three marginal candidates as independent adjective legs.

## Window-level evidence (@-offsets, all re-derived)

**The granted leg — @723 (a5_02):** `01 02 21 80 77 03 91 65 64 11 00 86 48` → "…[80] le[77,provisional] [03] [91] [65] qui[64] la[11]…". DET + N + 91 postnominal: the single adjective-shaped window. (03,91) x1 stream-wide (@722) — unique.

**Marginal candidate 1 — @386–387 (a2_07):** `82 16 52 38 37 43 91 36 62 91 84 73 34` → "…[37-A1pred] [43] [91] [36-noun-class] [62] [91] on[84]…". (43,91) x1 stream-wide; (91,36) x1 stream-wide. REJECTED as an adjective leg: 91 sits between two noun-profiled groups with NO determiner, inside a 37-predicative frame ("37 43" = [pred] [43]). Attributive adjective needs determiner support or a clean attributive frame; "N [91] N" in predicative territory is not adjective-shaped. The second 91 ("62 91 on") is equally unshaped.

**Marginal candidate 2 — @1517 (a7_11):** `39 81 88 11 31 11 91 67 08 31 24 11 11` → "…la[11] 31 la[11] [91] et/veut[67]…". (11,91) x1 stream-wide. REJECTED: 91 is in HEAD position after "la" ("la [91]"), followed by et/veut. DET+X with X as the modified head is nominal, not adjectival — the adjective reading is not framed.

**Marginal candidate 3 — @1004 (a6_02):** `86 56 47 91 11 52 35` → "…ce[47] [91] la[11]…". (47,91) x1 stream-wide. REJECTED: same as candidate 2 — 91 in head position after "ce" ("ce [91] la"), not modifier position.

**Remaining 15 windows** (@15/@36/@137/@247/@256/@277/@301/@520/@538/@852/@1019/@1371/@1428/@1668/@1698): none adjective-shaped. Notable dead-ends: @36 "08 91 à[39]" (91 before promoted preposition "à" — noun-shaped); @15 "45 91 53" (91 head after 45); @520 "pre[70] 91 le[77]" (91 between "pre" and "le"); @137 "[23] 91 [65-noun-class]" (91 before noun but no determiner — same defect as candidate 1); @1428 "63 91 61" (61 globally fenced, locus-"premier" only); @1698 "23 91 [85-verb-stem]" (91 before granted verb stem); @538 "16 91 n[12]" (12='n' letter contact).

**Excluded per adverses:** @1798 (a8_10) `94 59 37 91 79 87 64` = "n'est[59] [37] [91]" — predicative-59 territory, not counted.

## Per-clause pass/fail

- **C1 (naming arm): FAIL.** Only @723 stands as adjective-shaped. The three marginals (@386–387, @1517, @1004) fail independently: no determiner-supported attributive frame, or 91 in head position rather than modifier position. The remaining 15 windows are all non-adjectival on standing values.
- **C2 (fence arm): FIRES.** @723 stands alone. The adjective reading of 91 is FENCED: no second independent adjective-shaped window exists on the repaired stream.

## Adverses (answered, none ignored)

- "@1798 'n'est 37 91' is predicative-59 territory — excluded; do not re-litigate est-59-frames": honored. @1798 was never counted as an adjective leg; est-59-frames was not re-tested.

## Standing-state check (no contradiction, no downgrade)

- No red-team verdict on 91 exists; 91's value stays open. The fence removes a rival reading, it does not promote or kill any value.
- Groundwork report's census (n=21, one leg) is confirmed byte-exact; nothing overturned.
- §7 honored: no polyvalence declared; 67 sole-polyvalence untouched.

## Verdict: NULL (fence executed)

Headline: 91's adjective reading is fenced — @723 ("le 03 91") stands alone; no second independent adjective-shaped window exists among 91's 21 windows on the repaired stream. Not kill-grade on any 91 value: the fence constrains the class, not the value. Note for the red team: @723's own leg is conditional on 03's class at that window (03's profile is split — verb-stem "[03]er" x3 vs noun/word family — per battery-stem-03-value NULL; if 03 is verb-stem at @723, even the single leg dissolves).

## Follow-up targets (null regeneration; for the supervisor to queue)

1. **adj-91-723-03-gate** (priority 3): re-test @723's postnominal reading once 03's class is decided. Bar: @723 stands as an adjective leg iff 03 parses noun-shaped under standing values at this window; if 03 is verb-stem here, the single leg is fenced too. Adverses: do not re-litigate stem-03 (class bar) — take its verdict; do not declare polyvalence (§7). Evidence: this report's @723 analysis; battery-stem-03-value's 03 split profile.
2. **adj-91-386-43-gate** (priority 3): re-test "43 91 36" @386–387 once noun-43 names 43. Bar: 91=postnominal adjective iff a determiner-supported attributive parse of "43 91 36" stands under the named 43; else the window stays fenced. Adverses: predicative-37 territory (37's value S5-owned — do not decide); do not duplicate noun-43. Evidence: this report's candidate-1 rejection.

## Standing constraints observed

- §7: standing values only; no invented values; 67 sole-polyvalence untouched; all cited verdicts respected, none downgraded.
- No invented numbers: every count re-derived above on the repaired 1,847-pair parse.

---
Lock: `locks/adj-91-723-second-leg.lock` created 2026-10-09T03:57:20Z, deleted on completion of this report.
