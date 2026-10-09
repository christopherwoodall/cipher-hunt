# Battery report: verb-63-frames — "63 is verb-class with >=3 frame legs"

- Worker: battery worker verb-63-frames, agent 8c09d5e9-a82a-4b88-8fdd-c49d2fa23ecd
- Date: 2026-10-09 (lock created 2026-10-09T05:57:00Z; no prior lock, fresh run)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Re-derived in-session: 1,847 pairs / 96 types verified. canonical.py NOT used. R5005, sealed gates, and the red-team adjudication queue untouched. All @-offsets are 0-based repaired-stream pair indices.

## Epistemic status (up front)

Class-level finding only: 63 = verb class. No value named. Battery-grade; needs red-team ratification before entering the banked map. Standing values used as premises only (banked GT: 11, 70, 82, 34, 29, 40, 46; granted: 87, 64, 96, 17, 79, 00, 84, 47; provisional: 59, 77). 65 = noun class is standing (R18-001, registry `["noun","cls"]`, value open) — used as premise, never re-litigated.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"Test 63=verb-class with >=3 independent frame legs.
Legs must include the 63 00 pour-complements (x4), the 12 63 frame, and distribution comparison vs 24/88 verb frames.
Fail closed: if fewer than 3 legs pass, null with follow-ups, not a promote."

Numbered clauses (frozen, not modified after testing):
1. C1: >=3 independent verb frame-legs for 63 pass.
2. C2: all three required components are included (63 00 pour-complements x4, the 12 63 frame, distribution comparison vs 24/88 verb frames).
3. C3: fail-closed honored — if fewer than 3 legs pass, verdict is null with follow-ups, not a promote.

## Method

Re-derived the repaired stream in-session. n(63)=12, byte-confirmed. All 12 windows censused with +/-4 context and full-row context where needed. "63 00" x4 confirmed (@252, @713, @1107, @1531 — all four are "63 00 66"). "12 63" x1 (@713). Successor/predecessor sets computed for 63, 24 (finite modal verb, ne-24-profile promote), 88 (verb class), and 65 (noun class, control).

## Window-level evidence

### Leg A — "65 63 00 66" x3: STRONG (three independent windows)

- @252 (a2_02): `32 44 94 65 63 00 66 01 91` = "[32] [44] ne [65-noun] [63] pour [66] [01] [91]"
- @1107 (a6_06): `74 47 78 65 63 00 66 73 41` = "[74] ce [78] [65-noun] [63] pour [66] [73] [41]"
- @1531 (a8_00): `87 46 21 65 63 00 66 73 41` = "ce que [21] [65-noun] [63] pour [66] [73] [41]"

Parse under 63=finite verb: "[65-subj] [63-verb] pour [66]" — subject + finite verb + purpose "pour"-clause. 66 is infinitive-shaped ("00 66" x7/19; cf. @705 "n [66-inf] [21-obj]", @189 "[16] pour [66] [24-verb]"); the parse also holds if 66 is nominal ("V pour [noun]"). Three distinct rows (a2_02, a6_06, a8_00), distinct left edges ("44 94 65", "47 78 65", "46 21 65"), distinct right tails ("66 01 91" vs "66 73 41" x2) — independent attestations, not a formulaic repeat.

Rivals exhausted at all three:
- 63=noun: "[65] [63] pour [66]" = bare N-N juxtaposition before a "pour"-clause — ungrammatical (65's noun promote is standing; §5 bars overwriting it, so 65 cannot be re-valued to rescue).
- 63=adjective without boundary: "[65-noun] [63-adj] pour [66]" — "pour"-clause stranded after an NP with no verb — ungrammatical.
- 63=adjective WITH clause boundary ("[65] [63-adj]. Pour [66], …"): fronted purpose "pour [66]" is grammatical, but the boundary has zero byte evidence (all three mid-row, no punctuation/formula marker) — fenced per the bound-96-00-clause precedent (fence iff no boundary evidence exists).
- 63 composes with 65 or 00: no evidence; 00='pour' is A9-granted as a word.

Leg A = 3 strong legs. The verb reading is the unique clean parse at each window.

### Leg B — the "12 63" frame: CONDITIONAL (included per bar)

- @713 (a5_01): `12 48 71 12 63 00 66 86 01` = "n e [71] n [63] pour [66] [86] [01]"

Right edge "[63] pour [66-inf]" is the identical verb frame as Leg A. 12='n' (letter tier): fenced as word-final 'n' of an open word ("[71]n [63-verb] pour [66]") — 71's value is open, so the left contact cannot be resolved further. Supporting parallel: "12 66" x1 (@705: "[20] n [66-inf] [21-obj]") shows the same "n [X]" word-initial pattern with X=66 (infinitive), consistent with 63 being word-initial here. Conditional leg: verb-compatible with one fenced contact.

### Leg C — "78 63 45 46" @436 (a2_09): CONDITIONAL

`29 82 16 78 63 45 46 43 98 80 …` = "er m [16] [78] [63] ce que [43] [98-fin] …"

Under 63=finite verb: "[78?] [63-verb] ce que [43] [98-fin]" — verb + "ce que" complement clause ("ce que [43-subj] [98-verb]" is well-formed; 98 is finite-verb class). Clean parse, conditional on nominal-78 (78's class is open; redteam-78 docket is red-team venue — not decided here).

### Leg D — distribution vs 24/88 verb frames: SUPPORTING (stated weakness)

- Successor-set overlap, one-sided hypergeometric (N=96):
  - 63-suc (n=9: {00,11,29,42,45,71,74,77,91}) ∩ 24-suc (n=25): 5 keys {00,11,42,74,77}, expected 2.34, **p=0.049** — marginal at the 0.05 lane standard; stated openly, not oversold.
  - 63-suc ∩ 88-suc (n=19): 3 keys {11,29,77}, expected 1.78, p=0.25 — null.
  - 63-suc ∩ 65-suc noun-class control (n=15): 1 key {71}, expected 1.41, p=0.80 — 63's distribution DISSOCIATES from the noun class.
- "pour"-taker ranking (groups with n>=5): 63 is #2 stream-wide at P(00|g)=4/12=0.333 (28: 0.50 n=6; 19: 0.222; 81: 0.214; …). "pour"+infinitive is a verbal-complement signature; 63 is an outlier-high pour-taker.

Net: weak-to-moderate distributional support — marginal-positive vs the finite-modal frame, null vs 88, clean dissociation from the noun class, outlier pour-rate. Counted as a supporting leg with the p-values on the table.

### Fenced windows (not legs, not kills)

- @204 (a2_00): "…92 63 42 06 77 44…" — verb-63 needs "42 06" word-internal (else two finite verbs); nominal-63 needs 42 as verb stem. Both contacts open. Fenced, undecidable at standing grade.
- @324 (a2_05): row-initial "63 71 10 01 19 00 92…" — V1/imperative verb-initial clause possible; "63 71" composition unevidenced. Conditional only, not counted.
- @429 (a2_09): "…42 63 77 86 29 82 16…" — postverbal "le" (77='le' provisional) kills the verb reading IF 77='le'; but "77 86 29" = "le [86]er" is independently ungrammatical under standing values (86=INF class + 29=er). The window's ungrammaticality localizes to "77 86 29", independent of 63's class. Fenced with stated cause; 77's value is red-team venue (lon-77-le-gate).
- @634 (a4_01): "…52 67 63 74 46 60 67…" — 67=et gives "[63-verb] [74] que [60]" (possible); 67=veut needs infinitive-shaped "63 74" (unverifiable — 74 open). Both readings live. Fenced.
- @1043 (a6_03): row-final "…17 77 82 63 11" = "fois le m [63] la" — verb-63 strands ("m [63-verb] la": no subject, double object); nominal-63 ("le [m63] la") also ungrammatical. Residual for all readings — not a kill of verb-63 (no clean rival parse). Fenced.
- @1427 (a7_08): "…33 29 87 63 91 61 12 16" = "…[33]er ce [63] [91]…" — ADVERSARIAL, fenced not killed: verb-63 needs "ce" as subject of a content verb (strained in 1841 French — "ce"-subjects are near-restricted to être); nominal-63 ("ce [63-noun] [91]") needs 91 adjectival (91's class open; val-91-pp-adj's participle naming is locus-level at 16-91 windows only, not importable). Both readings carry exactly one open slot — genuine fence, recorded as the standing adverse on the claim.
- @373 (a2_06): "…17 06 21 65 63 29 85 82 48" — "63 29" admits the infinitive reading "[63-stem]er" (cf. 03-29 precedent) but no governing verb is available in the window; the finite reading strands "er". Residual under all classes. Fenced.

No window forces 63≠verb at kill grade: every anti-verb window either has no clean rival parse (@1043, @373, @204, @429, @634) or carries a symmetric open slot (@1427).

## Per-clause pass/fail

1. C1 (>=3 independent verb frame-legs): **PASS** — 3 strong legs (Leg A trio) + Leg B/C conditional + Leg D distributional.
2. C2 (all three required components included): **PASS** — 63 00 pour-complements x4 (3 strong + 1 conditional), 12 63 frame (conditional), distribution vs 24/88 (supporting, p-values stated).
3. C3 (fail-closed): N/A — C1 passes; no null needed.

Adverses: none listed in the queue entry. The @1427 "ce"-subject strain is the standing window-level adverse — fenced with stated cause above, not ignored.

## Hinge closure (claim's stated consequence)

suite-21-qui-que escalation #2 was: "@1529 parses conditionally on 65's class; pending prof-65." prof-65 has since promoted 65 = NOUN class (R18-001), killing the 65-verb conditional. Under verb-63, @1529 parses as:

`…par ce que [21] [65-noun] [63-verb] pour [66] [73] [41]`

= "que" + NP-subject + finite verb + "pour"-clause. The subject span "21-65" must compose as a unit NP (one stated compositional assumption; A12 "37-01 unit" is the lane precedent for two-group units) — 21's value is open and 65 alone cannot carry 21. The hinge closes: the missing finite verb the escalation needed is 63, and the 65-verb alternative is dead per the standing promote. @371 ("…21 65 63 29 85…") does NOT parse cleanly under verb-63 ("63 29" = ungoverned "[63]er" vs stranded "er") — fenced as residual with stated cause, not hidden. The suite VALUE kill at @134 stands independently and is untouched.

## Verdict: PROMOTE (finding grade, class level)

63 = verb class, value open. 3 strong frame-legs + conditional + distributional support; no kill-grade counter-window; the one window-level adverse (@1427) fenced with stated cause. Battery-grade — requires red-team ratification before entering the banked map. No standing verdict contradicted or downgraded; §7 intact (one class, no polyvalence declared).

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-verb-63-frames.md (this file)
- Queue: battery-queue.json `verb-63-frames` → status `verdict`, result `promote` (temp-file + rename; pre-write assert passed; JSON re-validated)
- Lock: created on start, deleted on completion
- Stream re-derived in-session (1,847 pairs / 96 types); canonical.py never used; R5005, sealed gates, red-team queue untouched
