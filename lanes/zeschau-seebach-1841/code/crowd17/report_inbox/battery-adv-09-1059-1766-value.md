# Battery verdict: adv-09-1059-1766-value

**Target:** `adv-09-1059-1766-value` (P3)
**Date:** 2026-10-09
**Worker:** battery worker adv-09-1059-1766-value (subagent 9fc98d23-2596-4ca0-9025-93304f1ee483)

## Bar (verbatim, pre-registered)

"Value named with >=2 legs or fenced; CONDITIONAL on 77='le' surviving (lon-77-le-gate)"

Restated as numbered clauses:
- C1: name 09's adverbial value ('y' vs 'en'-shaped) at the two "l'on __ V"
  windows (@1059, @1765) with >=2 independent legs → PASS/FAIL.
- C2 (else-branch): fence with stated cause if the value is unnameable at
  battery level → PASS/FAIL.
- C3 (condition): 77='le' must survive (lon-77-le-gate). If 77='le' dies, the
  "l'on" frame dissolves and this target's premise fails → record.

## Method

Read BATTERY-PROTOCOL.md in full before touching anything. Created
`locks/adv-09-1059-1766-value.lock` on start (agent id + 2026-10-09T20:21:55Z),
deleted on completion per protocol. Re-derived the repaired 1,847-pair /
96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` +
`../data/upstream-ct_R5005.txt`, tokenized per `code/side-keyhunt/repair_parse.py`
(asserts: n=1847, 96 types — both hold). `canonical.py` never used. R5005,
sealed gate instances, and the red-team adjudication queue untouched.
Pre-dispatch check: target had no verdict and no lockfile; queue entry re-read
fresh immediately before the lock was created.

Standing values used (§7): GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on (A15
conditional), 47=ce; provisional 59=est, 77=le. Battery-grade (not standing):
98='vient' (vient-98-894-reaudit promote), 94='ne' STRONG LEAD, 24 docketed
('en' vs finite-modal, unresolved — 24-redteam-adjudication QUEUED,
24-en-verb-conflict NULL, ratify-24-modal-input promote). Kills honored:
09/92 "-ère" (A6), 09-verb (lon-09-verb), 09~92 hold (A6), 67 sole true
polyvalence. No red-team verdict on 09's class or value exists.

All offsets below are 0-based @ on the repaired stream.

## Window evidence (byte-exact, re-derived)

Exactly two `77 84 09` windows exist (lon-09-reseg inventory, confirmed):

- **W1 @1059 (row a6_04):**
  `... 74 74 45 23 | 77 84 [09] | 98 83 82 96 21 62 18 ...`
  = "[74][74] ce(45-A11) [23] | l'on (77 prov, 84 granted) [09] |
  vient (98 batt) [83] m(82 GT) par(96 granted) [21] [62] ..."
  (77@1057, 84@1058, 09@1059, 98@1060.)
- **W2 @1765 (row a8_08):**
  `... 15 93 06 | 77 84 [09] | 24 87 64 26 37 78 ...`
  = "[15][93] ent(06 batt) | l'on [09] | [24 modal-docket] ce(87) qui(64)
  [26] [37] [78] ..."
  (77@1763, 84@1764, 09@1765, 24@1766.)

09 census (n=12, all forced-class reviewed in doublet-589-09-role): followers
are {00, 87, 64, 70, 00, 07, 02, 98, 20, 11, 24, 19}. No 09 token other than
W1/W2 sits in a pre-verbal adverbial-pronoun slot. Parallel frame for
contrast: @1486 `46 77 84 [24] 87 08` = "que l'on [24] ce [08]" — 24 directly
after 84 with NO 09, showing the adverbial slot's optionality at 'l'on'
frames (fin24-1486-parallel promote).

## Value legs ('y' vs 'en')

- **Leg 1 ('y', W1, verb-selection):** 98='vient' (battery-grade) is a motion
  verb. 'y' is the canonical locative adverbial pronoun with verbs of motion
  ("l'on y vient" = "one comes there"); 'en' is partitive and requires an
  explicit or implied de-source, and the W1 clause
  `23 77 84 09 98 83 82 96 21 62` contains no de-complement. This leg names
  'y' at W1 — but it is itself conditional on battery-grade 98='vient', not
  §7 standing. One leg, conditional. No second independent leg was found:
  the "98 83 82" tail recurs (@897, @930, @1783: `74 65 23 [98] 83 82`) but
  that is the same window's continuation, not an independent value-naming
  leg; no elision data exists for 09 (followers 00..19 include no confirmed
  vowel-initial neighbor, and both 'y' and 'en' are vowel-initial anyway —
  elision would not discriminate).
- **W2 gives no independent leg:** 24's value is docketed and unresolved
  ('en' vs finite-modal; red-team adjudication queued). The selectional
  argument cannot be run against an unnamed verb, and on the rival reading
  24='en', W2 is not a "l'on __ V" window at all (see F2).

## Per-clause findings

- **C3 (condition): PASS.** 77='le' survives: provisional, never killed
  (le-77 NULL; lon-77-le-gate NULL; lon-77-le-gate-rerun NULL;
  lon-77-le-gate-rerun-2 QUEUED). 84='on' conditional grant stands
  (elision-77-84 promote supports the A15-C1 elision frame). The "l'on"
  reading holds; the frame does not dissolve.
- **C1 (>=2 legs name one value): FAIL.** Exactly one discriminating leg
  exists ('y' via W1 motion-verb selection, itself conditional on
  battery-grade 98='vient'); 'en' is not killed but unnamed by any leg.
- **C2 (fence): FIRES.** Per §2/§4 the bar as written covers the fence
  outcome; recording the fence (counts as null).

## Fence causes (stated)

- **F1:** Only one value-discriminating leg ('y' at W1, verb-selection;
  conditional on 98='vient' battery-grade). No second independent leg for
  'y' or 'en' exists in the stream at battery level.
- **F2:** W2's membership in the claim's "two 'l'on __ V' windows" is
  unstable. 24='en' vs finite-modal is docketed unresolved at red-team. On
  the rival 'en' reading, W2 re-parses as "l'on [09] ‖ en ce qui [26]..."
  (S3, lon-09-reseg) — the second window leaves the target's scope and the
  claim's "two windows" premise collapses to W1 alone. This rival is
  material to the claim but is NOT listed in the target's adverses field
  (queue-data note for the supervisor).
- **F3:** The adverbial-particle class arm survives (conditions hold per C3),
  but 'y' vs 'en' value-naming is unfalsifiable at battery level with the
  current evidence.

## Adverses

Listed adverse ("Conditional on 77='le' provisional + 84='on' conditional
grant"): ANSWERED — both hold (C3). Unlisted but material adverse
(24='en' vs finite-modal docket): FENCED per F2, not ignored. Standing-state
check: no red-team verdict on 09 contradicted or downgraded; no polyvalence
declared (§7 sole-polyvalence honored); this null is consistent with the
promoted split-09-redteam-input framing (battery gathers; red team declares).

## Verdict: NULL (fence executed)

## Follow-ups proposed (per §4; all IDs verified ABSENT from battery-queue.json)

1. `sel-09-y-en-selection` (P3) — selectional-frame census: catalog all 41
   '98' windows and all 48 '24' windows for de- vs locative-complement
   licensing; pass iff >=2 independent licensing legs name one of 'y'/'en'
   (targets: resolve the W1 "98 83 82" tail's 83; find a locative-NP anaphor
   or de-source in W1's wider clause). Gated on vient-98-894-reaudit
   standing (already promote).
2. `w2-frame-24-docket-gate` (P2, gated) — re-test the W2 "l'on __ V" premise
   once the 24='en' vs finite-modal docket (24-redteam-adjudication) resolves:
   if 24='en' is ratified, W2 leaves this value-naming target's scope
   (S3 "en ce qui" frame) and the value question collapses to a W1-only
   re-run; if modal is ratified, W2 rejoins with 24's named value as a
   second selectional leg.
3. `en24-cequi-1766` (P3) — test the S3 "En ce qui [26]..." parse at @1765
   under the 24='en' reading: name 26's class (concerne-frame?); outcome
   feeds follow-up 2's gate directly. (Substance of lon-09-reseg's
   follow-up 2, verified absent from the queue.)

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-adv-09-1059-1766-value.md`
- Queue: `adv-09-1059-1766-value` → `status: verdict`,
  `verdict: {result: null, report: ..., date: 2026-10-09}` (pre-write assert:
  was queued/verdictless; target-id-unique tmp + rename; own entry only;
  no downgrade).
- Lock: created on start (agent id 9fc98d23-2596-4ca0-9025-93304f1ee483 +
  2026-10-09T20:21:55Z), deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
