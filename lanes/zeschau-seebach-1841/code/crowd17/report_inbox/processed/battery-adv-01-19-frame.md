# Battery report: adv-01-19-frame

- Target id: `adv-01-19-frame`
- Claim: test 01 as adverb at @483 ('30 01 19' = 'pas [01] [19-verb]')
- Date: 2026-10-09
- Worker: battery worker (subagent 3acc1318-6595-4631-94c5-7b829980fa85)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  1,847 pairs / 96 types re-derived in-session (asserts held). canonical.py
  never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"name 01's value from independent windows only (no invention); fence iff no
independently-grounded value parses."

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: Name 01's adverb value from independent windows only (no invention) —
   an 01 value grounded at a window other than @483 that parses as an adverb.
2. C2 (fence): If no independently-grounded value parses at @483, fence the
   adverb hypothesis with stated cause (do not invent a value).

Adverses: none listed.

## Method

1. Read BATTERY-PROTOCOL.md first; created
   code/crowd17/next-token/locks/adv-01-19-frame.lock on start
   (2026-10-09T08:03:03Z), deleted on completion.
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types verified).
3. Confirmed the target window byte-exact: @483='30', @484='01', @485='19',
   row a2_11 (`52 30 01 19 64 ...` — "pas [01] [19-verb] qui(64) [76-noun]...").
4. Census of all 28 windows of 01 (0-based pair indices):
   34, 40, 195, 255, 295, 327, 345, 409, 484, 596, 717, 828, 893, 940, 949,
   970, 976, 984, 988, 1029, 1255, 1261, 1440, 1462, 1634, 1653, 1731, 1818.
5. Surveyed standing lane evidence for 01's value/class at independent windows
   (related reports read, not duplicated).

## Window-level evidence

### Standing 01 values (independent windows)

- **"fait" syllable, word-internal** (battery-wordinternal-37-01, PROMOTE,
  battery-level): 01="fait" in 37-01 "satisfait"/"contrefait"-shaped
  3sg finite-verb compounds (37-01 contacts @940, @1634, @1818). Requires
  the 37-01 contact; @484 has 30 before and 19 after — not applicable.
- **Bound "-ci" in ce-contexts only** (ci-01-value KILL of absolute readings;
  battery-ce01-slot-1029 NULL; seg-ceci-87-61 PROMOTE for the 87+01 "ceci"
  fusion): "-ci" is restricted to ce-contexts (87-01 @345/@1029, 47-01 @195,
  45-01 @984). @484's left neighbor is 30='pas', not a ce-group — not
  applicable.
- **"-cier" word-internal** (battery-unit-85-01, KILL of the two-group unit):
  01-29 word-internal "-cier" continuation (@595-596). Requires 29 after 01;
  @484 has 19 after — not applicable.
- **'en' at 01-24 windows** (battery-disc-01-24-ci-X, PROMOTE): 01-24 x3
  (@828, @984, @40). Requires 24 after 01; @484 has 19 after — not
  applicable.
- **Absolute whole-word 01 values kill-grade dead** (battery-faisant-absolute-01,
  KILL): 01='faisant' killed at all four ce-windows. No battery ever named a
  whole-word adverb value for 01 at any of the 28 windows.

### The @483 adverb frame

The frame "pas [adverb] [verb]" is grammatical in French (e.g. "pas encore
dit"), so the adverb hypothesis is not frame-dead. But every independently-
grounded 01 value is bound or word-internal ("-fait", "-ci", "-cier", 'en'
in 01-24 contacts), and none licenses a whole-word 01 at @483. Naming an
adverb value ("si", "mal", "trop", "bien", ...) from @483 alone would be
invention — explicitly barred by the claim. The only other "X 01 19"
window (@327-328, "10 01 19") is likewise ungrounded: 10's class is open,
and it cannot serve as an independent grounding window for 01.

The adverb hypothesis is therefore unfalsified but ungrounded: fence, not kill.

## Per-clause pass/fail

1. C1 (name the value from independent windows): **FAIL.** No independent
   window grounds a whole-word adverb value for 01; all named 01 behaviors
   are bound/word-internal and all require contacts absent at @484.
2. C2 (fence): **PASS.** The "pas [01] [19-verb]" adverb frame is fenced as
   hypothesis-ungrounded with stated cause; @483 keeps all its open readings
   (segmentation, word-internal, class-open).

Adverses: none listed — none to answer. No standing or red-team verdict
contradicted or downgraded; §7 intact.

## Verdict: NULL (fence executed per the bar's else-branch)

## Follow-up targets (2, both verified absent from battery-queue.json)

1. **adv-01-327-sweep** (P4): re-test the adverb hypothesis at the parallel
   "10 01 19" window @327-328 once 10's class is named; the "X 01 19" family
   (n=2) is the only adverb-shaped residual for 01.
2. **01-19-wordinternal-seg** (P3): test "01 19" as a word-internal syllable
   contact at both "X 01 19" windows (@327-328, @483-485); 19 is verb-class,
   so test whether 01 fuses with the following verb stem rather than standing
   as a free token. Coordinate with (do not duplicate) queued `val-01-census`.

## Bookkeeping

- Lock created on start, deleted on completion (verified gone).
- `battery-queue.json`: `adv-01-19-frame` queued -> verdict/null
  (temp-file + rename; pre-write assert confirmed no prior verdict; only this
  entry touched; JSON re-validated).
- R5005, sealed gate instances, red-team adjudication queue untouched.
