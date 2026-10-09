# Battery verdict: part-62-46-slot

## Target
- id: `part-62-46-slot` (priority 3)
- CLAIM: test 62 as past-participle/participial at @46: 'pas [62-part] par' is the last open word-class between 'pas' and 'par' under granted values
- Source: follow-up #1 of battery-adv-62-pas-par (null, 2026-10-09), which fenced the adverb arm at @46.

## Bar (verbatim, pre-registered)
"'pas [62-part] par' parses with a participial candidate, or fence iff no participial candidate parses"

Restated as numbered pass/fail clauses:
- **C1 (parse arm):** 'pas [62-part] par' parses at @46 with a participial candidate for 62 stated and compatible with 62's byte-derived profile.
- **C2 (fence arm):** iff no participial candidate parses, fence @46 as participial-incompatible with stated cause.

## Verdict: NULL (fence executed)

## Method
Read BATTERY-PROTOCOL.md first. Created `locks/part-62-46-slot.lock` on start
(agent id + UTC timestamp), deleted on completion. Re-derived the repaired
stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`):
1,847 pairs / 96 groups verified. `canonical.py` never touched. R5005, sealed
gate instances, and the red-team adjudication queue untouched. 1841 diplomatic
French only.

## Window-level evidence (byte-traced)

1-based @44-49 (0-based indices 43-48), row a1_01, mid-row:

| 1-based @ | group | standing value |
|---|---|---|
| 44 | 43 | open |
| 45 | 81 | open |
| 46 | 30 | 'pas' (promoted) |
| 47 | 62 | open (this battery's subject) |
| 48 | 96 | 'par' (banked GT) |
| 49 | 00 | 'pour' (A9-granted) |
| 50 | 92 | open |

Full row a1_01 (35 pairs, @36-70): `08 91 39 64 41 01 24 88 43 81 30 62 96 00 92 79 37 11 79 85 58 35 53 12 41 08 34 29 40 12 94 92 69 13 24`. The target trigram sits mid-row; **no byte evidence for a clause boundary between @47 (96) and @48 (00)**. Byte-identical to battery-adv-62-pas-par's re-parse ("[81] pas [62] par pour").

## Per-clause results

### C1 (parse arm): FAIL

The frame 'pas [PP] par [agent]' is grammatical in 1841 French in the
abstract ("pas touché par", "pas convaincu par"). But no participial candidate
for 62 parses **at @46 under standing values**, for two independent,
byte-grounded reasons:

1. **Right-edge kill.** @47-48 = "par pour" is ungrammatical in French at any
   period: 96='par' is banked ground truth (requires a nominal complement);
   00='pour' is A9-granted (promoted, leg-1 class-level). 'pour' cannot supply
   'par''s complement. No clause boundary is byte-evidenced (mid-row a1_01).
   A battery worker cannot override A9's grant; the conditioned-'contre'
   question belongs to the red team (venue: contre-00-three-windows,
   seg-par-pour-96-00, both battery-null; not re-litigated here).

2. **Granularity mismatch.** 62's standing byte profile is stem-sized and
   nn-final: '62 06' x2 reads "donnent"/"mènent" (3pl; sel-62-48-94 KILL,
   standing), forcing 62 to carry the stem ("donn-") while 06 carries the
   ending. A single group 62 cannot carry a whole past participle
   ("donné"/"mené") — the "é" has no carrier: left neighbor 30='pas' and
   right neighbor 96='par' are both complete words. No participle-shaped
   composition with neighbors is available at @46.

The best 62-compatible candidate family (nn-final participles: "donné",
"mené") dies on both counts: the stem/ending split leaves the participle
incomplete, and even a whole-word rescue ("pas donné par") is killed by the
"par pour" right edge.

### C2 (fence arm): FIRES

@46 is fenced as participial-incompatible, with stated cause:
(a) the "par pour" right edge is ungrammatical under granted values and
unrescuable at battery grade (see C1.1); (b) 62's stem-sized profile admits no
participial composition at this window (see C1.2); (c) the '30 62 96' trigram
is hapax (n=1, @45, per adv-62-pas-par) — thin data, so fence, not kill.

This exhausts the parent battery's word-class inventory at @46: adverb
fenced (adv-62-pas-par), participle now fenced. 62's global class stays open
(class-62-nof94 null); the fence is locus-specific.

## Adverses answered

- "coordinates with queued seg-81-30-boundary (left edge)": HONORED. The
  left edge (@43-44: "43 81") is seg-81-30-boundary's venue (still queued);
  nothing re-litigated or duplicated. This fence rests on the right edge and
  62's profile, independent of the left edge.
- "class-62-nof94 null (class still open); do not duplicate": HONORED. No
  class is named for 62 globally; no value is proposed.

## Standing-state check

No standing verdict contradicted or downgraded. adv-62-pas-par (null) stands
untouched. §7 intact: no polyvalence declared (67 et/veut remains the sole
declared polyvalence). The fence is explicitly conditional: a red-team
re-valuation of 00 after 96='par' (conditioned "contre") would revive the
participial reading, since "pas [62-part] par contre" is grammatical
19th-century French.

## Follow-ups proposed (for supervisor queuing; both verified absent from queue)

1. `part-62-46-contre-gate` (P3) — re-test the participial reading at @46 iff
   the red team rules on 00's conditioned value after 96='par' (venue:
   contre-00-three-windows / seg-par-pour-96-00). "pas [62-part] par contre"
   is grammatical; this fence dissolves on that ruling.
2. `part-62-elsewhere` (P3) — census 62's other windows (62-94 x9, 62-48 x6,
   62-98 x5, 62-16 x4, 62-61 x2, 62-06 x2, 62-96 x1) for a participial-shaped
   environment with a clean right edge, i.e. a "pas/participle + agent"
   frame without the 'pour' collision.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-part-62-46-slot.md`
- Queue: `part-62-46-slot` → status `verdict`, result `null`, date 2026-10-09
  (temp-file + rename, own entry only; pre-write assert confirmed no prior
  verdict; JSON re-validated post-write).
- Lock created on start with agent id + UTC timestamp, deleted on completion.
