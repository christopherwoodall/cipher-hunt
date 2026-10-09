# Battery verdict: ver78-65-completion

- Target: `ver78-65-completion`
- Claim: "@1105's 'ce ver[65]' completes a French ver-word once 65 is named"
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` not used. All counts re-derived in-work. @-offsets are 0-indexed pair positions. R5005, sealed gates, red-team adjudication queue untouched. Lock `locks/ver78-65-completion.lock` created 2026-10-09T05:47:27Z (no stale lock present); deleted on completion.

## Bar (verbatim from battery-queue.json)

"(a) 65's value taken from prof-65's verdict, NOT re-derived; (b) 'ce ver[65]' reads as a French ver-word ('ce vers'/'ce vert'/other) under that value — or @1105 is fenced as non-completing"

Restated as numbered pass/fail clauses (pre-registered before testing):

- **C1:** 65's value is taken from prof-65's verdict, not re-derived by this battery.
- **C2:** 'ce ver[65]' reads as a French ver-word ('ce vers'/'ce vert'/other) under that value — OR @1105 is fenced as non-completing with stated cause.

Listed adverses: "65 open until prof-65 lands; 63's value open".

## Coordination (C1 — no duplication)

prof-65 verdict taken as input (report `code/crowd17/report_inbox/processed/battery-prof-65.md`, PROMOTE 2026-10-08): **65 = NOUN-CLASS; verb rival killed at kill grade; value unnamed.** Nothing re-derived: this battery did not re-test 65's class, only re-ran byte censuses for token positions in the repaired stream. The "65 open" adverse is therefore ANSWERED — it has landed.

## Window-level evidence (re-derived on the repaired stream)

@1105 (row a6_06): `... 1100:52 1101:82 1102:94 1103:74 1104:47 1105:78 1106:65 1107:63 1108:00 1109:66 1110:73 1111:41 ...`
Under standing values: `... 52 [82=m] [94=ne] [74] [47=ce granted A4] [78=ver LEAD premise] [65 NOUN-class] [63] [00=pour A9] ...`

Position facts (re-derived, repaired stream):
- 78 occurs x31; **78-65 occurs exactly once in the corpus, at @1105** — the completion question has exactly one window.
- 78 with ce (87/47) at -1: 7 windows (@364, @573, @629, @819, @982, @1105, @1397); @1105 is the unique 65-follower.
- 65 occurs x25; predecessors {21:x4, 40:x3, ...}; 65 followers {63:x4, 23:x3, 64=x3(qui), ...}. 65's top successor is 63, not part of any ver-word shape.

## Completion test (C2)

The French ver-word candidates under the claim's own 78="ver" premise:
- 65='s' → "ce vers"; 65='t' → "ce vert"; 65='e' → "ce vere" (not a French word anyway); 65='re' → "ce verre" needs v-e-r-r-e (second r absent, and 65 is one cell).

prof-65's PROMOTE verdict (taken as input per C1) makes all of these kill-grade impossible:
- A letter completion ('s', 't', 're') requires 65 to be a syllable/letter cell. 65 is NOUN-CLASS — a whole word, not a word tail. prof-65 demonstrated the noun class on 6 frame-legs (qui-relative heads x3, que-relative head, post-finite-verb direct object x2, post-"[X]ere" x3) and killed the verb rival at kill grade; a fortiori the letter reading is excluded.
- §7 standing constraint: 67 et/veut is the SOLE true polyvalence. Reading 65 as simultaneously a noun (prof-65 verdict) and a word-tail syllable would require a red-team-declared second polyvalence. No such declaration exists.
- No "other" French ver-word is composed as "ver" + a whole noun: the ver-family (vers, vert, verre, verse, verve, verger, verdict...) is not "ver"+[noun]. "ce ver[65]" under 65=noun is a two-word sequence.

Therefore 'ce ver[65]' **cannot** complete a French ver-word under 65's verdict. Per the bar's pre-registered disjunct, **@1105 is fenced as non-completing** with cause:

> Fence: under prof-65 (65=noun-class, PROMOTE), the only lane-legal parse of @1105 is "ce ver [65-noun] [63] pour" — a complete ver-word "ce ver" (under the claim's own 78="ver" LEAD premise) followed by a noun, then 63 (verb-shaped per prof-65 L6: `63 00` "63 pour" complements x4, lead-level) and 00=pour (granted A9). Grammatical under standing values; no ver-word completion exists at this window. This does not promote 78="ver" — the LEAD premise is only used, per the claim's framing.

## Adverses answered

- "65 open until prof-65 lands": **ANSWERED.** prof-65 landed 2026-10-08 with PROMOTE (noun-class). Taken as input, nothing re-derived.
- "63's value open": **FENCED as non-blocking.** The completion verdict is class-level (65=noun cannot be a word-tail syllable); 63's value cannot restore a syllable reading of 65. Under prof-65 L6, 63 is verb-shaped (lead-level: 63-00 x4 pour-complements), consistent with the fenced parse "[65-noun] [63-verb?] pour". 63's exact value is 63's battery's business (recommended follow-up verb-63-frames already exists in prof-65's report) — it gates nothing here.

## Per-clause pass/fail

- **C1:** PASS — 65's value taken from prof-65's verdict (NOUN-CLASS, PROMOTE 2026-10-08, verb rival killed); no re-derivation.
- **C2:** PASS via the bar's fence disjunct — the ver-word completion is kill-grade impossible under 65's noun-class verdict (§7 sole-polyvalence bars the noun+syllable dual reading); @1105 is fenced as non-completing with stated cause.

## Verdict: KILL

The claim "@1105's 'ce ver[65]' completes a French ver-word" is forced false at kill grade by prof-65's standing PROMOTE verdict: 65 is noun-class, and under §7's sole-polyvalence rule a noun-class cell cannot supply the word-tail syllable ('s'/'t'/'re') the completion needs. The bar pre-registered this resolution: @1105 is fenced as non-completing.

Scope of the kill (fenced): this kills only the @1105 successor-completion claim. It does not touch 78="ver" as a LEAD (R16-005 grading stands — 78="ver" was never re-graded here), does not downgrade 65's PROMOTE (used, not re-litigated), and contradicts no standing red-team verdict. It is consistent with battery-ver78-ce78-open-succ's fenced scope (successor-completion kill only; the @1105 residue was exactly this target).

## Provenance

No invented data. Stream byte census re-derived in-session. All non-@1105 claims (prof-65's class verdict, 63 verb-shape, 78="ver" LEAD, 94="ne", 82="m", 00="pour", 47="ce", 67 sole polyvalence) are standing values cited, never derived here.
