# battery-personal-tonic-pour-inf-drama — report

## Bar (verbatim, pre-registered)

">=1 genuine locates the governor; confirmed zero hardens the fence at the governor class"

## Numbered clauses

1. **Clause 1 (attest arm):** ≥1 genuine tonic-pronoun + "pour"-governed infinitive window in the drama register locates the governor.
2. **Clause 2 (fence arm):** a confirmed zero (every candidate classified with cause) hardens the fence at the governor class.

## Method

- Venue per dispatch: the repaired 1,847-pair stream — `code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`, parsed exactly as `code/side-keyhunt/repair_parse.py`
  (`[s[i:i+2] for i in range(o, len(s)-1, 2)]` per row with the repaired offsets;
  verified 1,847 pairs, 96 distinct groups, crib "11 70 82 34 29 40" pair-aligned,
  row a8_05 ending on "46"). `canonical.py` never touched. R5005 read only.
- Decoded only with standing §7 values: banked 11=la, 70=pre, 82=m, 34=i, 29=er,
  40=e, 46=que; promoted 87=ce, 64=qui, 96=par, 17=fois, 79="tout", 00="pour" (A9),
  84="on" (A15), 47="ce" (A4); provisional 59=est, 77="le". No other group read.
- Attempted instantiation of the bar on the stream: (a) locate group(s) reading a
  personal tonic pronoun (moi/toi/lui/elle/nous/vous/eux — the sibling batteries'
  inventory); (b) scope the drama register in the stream; (c) enumerate 00-loci and
  classify followers with standing values/frames.

## Window-level evidence (@-offsets, 0-based pair index)

- 55 occurrences of 00 ("pour", A9) at pair offsets:
  @1, @27, @48, @76, @106, @185, @188, @245, @253, @287, @329, @378, @407, @466,
  @480, @545, @552, @587, @592, @660, @667, @682, @714, @727, @739, @748, @845,
  @866, @888, @935, @961, @977, @1001, @1087, @1108, @1127, @1138, @1153, @1244,
  @1247, @1287, @1312, @1374, @1405, @1493, @1505, @1532, @1545, @1584, @1602,
  @1629, @1680, @1791, @1822, @1824.
- Follower+1 distribution (top): 86 x12, 33 x8, 66 x7, 92 x6, 97 x4, 11 x4
  (11="la"), 46 x4 (46="que" — "pour que"), 36 x3, 34 x1, 13 x1, 20 x1, 64 x1.
  This reproduces the A9 grant note verbatim (00→86 x12, 00→33 x8) on the
  repaired parse — the governor locus is well-formed at group level.
- 00 followed by a granted verb-frame (80/89 A8, 85 A3): 0.
- Tonic-pronoun locus: NONE. No standing value reads a personal tonic pronoun.
  84="on" (25x) is granted but "on" is outside the sibling tonic inventory
  (moi/toi/lui/elle/nous/vous/eux) and never dislocated in the stream's
  annotation-free group sequence.
- Register scope: NONE. The stream is a single French diplomatic despatch
  (DECODE R5005, Dresden→St Petersburg); rows carry page-region tags
  (a1_00..a8_11), no register annotation. "In drama" cannot be scoped.
- Exclamatory channel: NONE. The stream is unseparated digit groups; no
  punctuation or prosody survives, so the "governed-exclamatory" illocutionary
  gate from the sibling battery cannot be applied.

## Per-clause pass/fail

1. **Clause 1: UNTESTABLE — antecedent cannot be instantiated.** Locating a
   "tonic-pronoun + pour-governed infinitive" window requires a tonic-pronoun
   group, a drama-register scope, and an exclamatory channel; all three are
   absent on the repaired stream. Inventing a group reading to force
   instantiation is forbidden. The attest arm cannot run here.
2. **Clause 2: UNTESTABLE — no confirmable zero.** A confirmed zero requires
   classifying every candidate with cause; with no locatable tonic heads there
   are no candidates to classify, so the zero cannot be confirmed and the
   governor-class fence cannot be hardened from this venue.

## Verdict

**NULL** — BATTERY-PROTOCOL.md §2: the bar is genuinely untestable as written on
the dispatched venue (repaired 1,847-pair stream). This is a venue mismatch, not
a refutation: the claim's intended venue is the plaintext drama register
corpus (`code/side-period/corpus/`, 14 plays, 2,969,582 chars), where the sibling
battery's P1/P2/P3 taxonomy can actually run. Nothing in this run contradicts a
standing red-team verdict; no verdict was downgraded; no data invented.

## Follow-ups proposed (nulls regenerate work)

1. **personal-tonic-pour-inf-drama-corpus (P3)** — run the intended test on the
   plaintext drama corpus (`code/side-period/corpus/`, 14 plays, 2,969,582 chars)
   with the sibling's P1/P2/P3 taxonomy restricted to the pour-only governor:
   ≥1 genuine locates the governor in the true drama venue; a confirmed zero
   hardens the fence at the governor class where the bar is actually testable.
   Verified absent from battery-queue.json.
2. **tonic-pronoun-stream-locate (P3)** — stream prerequisite battery: locate
   candidate personal-tonic-pronoun groups in the repaired 1,847-pair stream
   (distributional + gloss-anchored, e.g. the 25 loci of 84="on" and unmapped
   pronoun-shaped high-frequency groups). Until a tonic group is granted, NO
   stream battery can instantiate a tonic-pronoun claim. Verified absent.
3. **governor-00-inf-locus (P3)** — stream census of the 55 00-loci above with
   follower-frame typing against granted frames (80/89 A8, 85 A3; 00→86 x12,
   00→33 x8, 00→46 x4 "pour que"): a stream-native characterization of the
   pour-governor's actual follower class — the part of the governor-class fence
   question the stream CAN answer. Verified absent.

## Standing items

- R5005: read only (upstream-ct_R5005.txt + repaired_offsets.json). Sealed gates,
  red-team adjudication queue: untouched.
- Standing §7 values: untouched, none contradicted (00→86 x12 / 00→33 x8 / 00→46 x4
  reproduce the A9 grant on the repaired parse).
- No numbers invented: every count above traces to the repaired-stream parse.
- Lock: created on start (c6b2ff3b-c46e-4ae9-a8ff-97e548079b31, 2026-10-09T14:47:00Z),
  deleted on completion.
