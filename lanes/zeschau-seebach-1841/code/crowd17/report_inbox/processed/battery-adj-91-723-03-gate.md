# Battery report: adj-91-723-03-gate (PROMOTE — locus-level)

**Target:** adj-91-723-03-gate (priority 3). Supervisor-dispatched worker. Date: 2026-10-09.
**Stream:** repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs, 96 types, asserts hold). `canonical.py` never used. R5005 untouched. Sealed gates untouched. Red-team adjudication queue untouched. No data invented. @-offsets 0-indexed on the repaired stream.
**Lock:** `code/crowd17/next-token/locks/adj-91-723-03-gate.lock` created on start (no stale lock existed; no prior lock for this id), deleted on completion.

## Bar (verbatim from battery-queue.json — pre-registered BEFORE testing)

"@723 stands as an adjective leg iff 03 parses noun-shaped under standing values at this window; if 03 is verb-stem here, the single leg is fenced too"

## Bar as numbered pass/fail clause (frozen before testing; not modified after seeing data)

1. **C1 (iff gate):** 03 parses noun-shaped under standing values at @722 → @723 stands as an adjective leg. Else (03 verb-stem here) → the leg is fenced too.

## Method

1. Read BATTERY-PROTOCOL.md in full. Read evidence reports: battery-adj-91-723-second-leg.md (NULL/fence, 2026-10-09; granted leg @723 = "…[80] le[77] [03] [91] [65] qui la…", DET+N+91 postnominal), battery-stem-03.md (class PROMOTE: 03 = verb stem class, 3 verb-stem frames), battery-stem-03-value.md (value NULL; 20-window profile: verb family "[03]er" x3 vs noun/word family x17).
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types, byte-exact). Re-derived the @722 window and 03's full contact census.
3. Tested whether 03 at @722 admits a noun-shaped parse under standing values (protocol §7), and whether anything forces verb-stem there.

## Window-level evidence (@-offsets, all re-derived)

**Target window (byte-exact, mid-row a5_02, offset 0):**
- @717=01, @718=02, @719=21, @720=80, **@721=77, @722=03, @723=91**, @724=65, @725=64, @726=11, @727=00, @728=86, @729=48.
- Standing values: 77="le" (provisional), 64="qui" (banked), 11="la" (banked), 17=fois (promoted), 65=noun class (R18-001), 80=verb-frame (A8, value open).

**03's contact census (n=20, re-derived):** left neighbors {30x3, 40x2, 80x2, 60x4, 77x1, 37x1, 47x2, 01x1, 10x2, 24x1, 81x1}; right neighbors {64x4, 39x3, 62x2, 91x1, 02x1, 60x1, 24x1, 29x3, 40x1, 30x1, 38x1, 00x1}.

**The verb-stem family is exactly the "03 29" bigram — 3x stream-wide** (@1030, @1320, @1594; the three infinitive frames from battery-stem-03: "faire [03]er", exclamatory "[03]er! [80]-le", "[81] [03]er"). @722's right neighbor is 91, not 29: **"03 91" is a stream singleton**; nothing at @722 is verb-forcing (no 29, no "faire", no infinitive marker).

**"le [03]" forces nominal at @721-722:** under standing values 77="le" is a determiner. A bare verb stem cannot follow a determiner in 1841 French ("le [stem]" is ungrammatical). The determiner+03 shape is attested: "47 03" ("ce [03]") x2 (@1014, @1790). "77 03" is unique (@721-722) but belongs to the same DET+03 family.

**stem-03-value's own note:** the "[80]-le [03] [91]" context at @720-722 "favors a nominal/word reading of 03 there."

**Consistency with the class verdict:** battery-stem-03's PROMOTE explicitly records that the remaining 17 windows are "not all verb-compatible" and flags a §7 split question for the red team. @722 belongs to the noun/word family, not to the three verb-stem windows — no contradiction with the class promote.

## Per-clause pass/fail

- **C1 (iff gate): PASS.** 03 parses noun-shaped at @722 under standing values: the left determiner "le" requires a nominal; the determiner+03 shape is precedented ("ce [03]" x2); none of the verb-stem family features (03+29 infinitive, "faire" causative) is present. Therefore @723 stands as an adjective leg: "le [03-noun] [91-adj]".

## Adverses (answered, none ignored)

- "do not re-litigate stem-03 (class bar) — take its verdict": honored. The three "03 29" infinitive frames and the class-level promote are taken as premises, not re-tested.
- "do not declare polyvalence (§7)": honored. No polyvalence declared. The locus-level noun-shaped reading is packaged as consistent with battery-stem-03's own split-material note; the §7 adjudication stays with the red team.

## Verdict: PROMOTE (locus-level)

@723 stands as an adjective leg: 03 parses noun-shaped at @722 under standing values (determiner "le" left neighbor; no verb-forcing features; determiner+03 precedented). No value named for 03 or 91; no standing verdict contradicted or downgraded; §7 intact.

**Scope guard (not hidden):** this verdict keeps the single leg standing; it does not name 91=adjective. battery-adj-91-723-second-leg's fence (91's adjective reading fenced for lack of a second independent window) is untouched — the ≥2-window bar still fails. If the red team rejects provisional 77="le", this leg dissolves with it.

## Standing constraints observed

- §7: standing values only; no invented values; 67 sole-polyvalence untouched; all cited verdicts respected, none downgraded.
- No invented numbers: every count re-derived above on the repaired 1,847-pair parse.

---
Lock: `locks/adj-91-723-03-gate.lock` created 2026-10-09T05:50:00Z, deleted on completion of this report.
