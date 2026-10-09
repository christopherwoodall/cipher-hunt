# Battery verdict: noun26-26n-exclude

## Bar (verbatim, pre-registered)

"at the 3 la-windows (@129/@240/@1560), exclude the '26n' one-word rival (12 = final 'n') with a window-level boundary test, or fence it"

## Bar restated as numbered pass/fail clauses

Offsets below are 0-based repaired-stream indices of the 26 token
(= 1-based @130/@241/@1561). Stream re-derived in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(1,847 pairs / 96 types verified); `canonical.py` never touched.

1. W1 (0-based @129, row a1_03): "11 02 26 32" — exclude the "26n"
   one-word rival with a window-level boundary test, or fence it.
2. W2 (0-based @240, row a2_01): "11 26 12 16" — exclude the "26n"
   one-word rival with a window-level boundary test, or fence it.
3. W3 (0-based @1560, row a8_01): "11 26 30 06" — exclude the "26n"
   one-word rival with a window-level boundary test, or fence it.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/noun26-26n-exclude.lock`
on start. Re-derived the repaired stream per `repair_parse.py`.
Cited, not re-litigated: battery-noun26-gov-frames (PROMOTE),
battery-noun26-la-frames (PROMOTE), battery-noun-26 (NULL, positional
rule). Standing values used: 11="la" (banked GT), 12="n" letter
(battery-promoted, pending red-team ratification), 30="pas"
(battery-promoted), 06="ent" (R17-007 granted), 94="ne" (STRONG LEAD
R17-001), 96="par" (granted). 16's class/value open; 26's class per
the positional rule (noun in "11 (02)? 26", verb elsewhere).

## Window-level evidence

"26 12" bigram census (0-based, re-derived): exactly 4x stream-wide —
@240 (W2), @842, @1470, @1707. "11 26" exactly 2x (@240, @1560);
"11 02 26" exactly 1x (@129). The three la-windows are the claim's
full scope.

### Clause 1 — W1 @129: EXCLUDED by contact

"93 59 45 28 00 46 11 21 67 93 29 89 68 21 67 14 21 60 90 19 58 66
98 82 48 | 11 02 26 | 32 96 56" (a1_03).

26's right neighbor is 32, not 12. The "26n" one-word rival requires
26+12 adjacency (12 = final "n" of the same word); the necessary
contact is absent at byte level. The rival is inapplicable here —
same exclusion method as gov-frames' @154/@600 ("excluded by
contact").

### Clause 2 — W2 @240: FENCED with stated cause

"41 17 | 11 26 12 16 | 56" (a2_01, row-final). The only la-window
where 26 and 12 are adjacent, so the only window where the rival
can arise. Three readings live:

- (i) 26 | 12-initial: 12 = word-initial "n" of a new word "n[16]".
- (ii) "26n": 12 = final "n", one word "la [26n]".
- (iii) 26 | "n'": 12 = elided "ne" before vowel-initial 16.

Boundary tests attempted (all contact-based):

- 94-test: N/A — no 94 at this window (the gov-frames "ne [noun]"
  kill at @842 does not transfer; see global note below).
- 06-bound test: N/A — 12's right neighbor is 16, not bound 06.
- 16 vowel-initial lead (battery-frame-82-16, NULL: 16 = "a"/"est"
  via elision, "12-16" x3 = "n'a"/"n'est"): makes (iii) concrete
  but does not force it — (ii) "la [26n] a [56]" still parses
  ("la [26n]" as subject of "a").
- ne-licensing: (iii) with 16="a"/"est" needs "pas" downstream
  (absent — row ends at 56; a2_02 opens "43 00 66 91..." with no
  30) or a ne-alone-licensed modal 16 (16's value open). Weakens
  (iii); does not exclude (ii).
- Distributional: "12 16" x3 (@241, @843, @1430). At @843
  ("94 26 12 16"), 94="ne" (STRONG LEAD) forces the 26|12
  boundary ("ne [26n]" ungrammatical). At @1707 ("26 12 06"),
  bound 06="ent" forces 12 to compose rightward. So "26 12"
  segmentation is already position-dependent stream-wide — no
  uniformity argument can force the boundary at W2, and none can
  force its absence either.

No window-level contact forces 26|12 apart at W2. Reading (ii)
remains live and unexcludable here (agrees with la-frames Clause 5:
"Live at @239 (grammatical, unexcludable here)"). FENCED, not
excluded.

### Clause 3 — W3 @1560: EXCLUDED by contact

"61 40 17 | 11 26 | 30 06 60 71 ..." (a8_01).

26's right neighbor is 30="pas", not 12. The "26n" rival's
necessary 26+12 contact is absent at byte level. EXCLUDED —
same method as Clause 1.

## Global note (cited, not re-derived)

The "26n" rival as a UNIFORM value (one word wherever "26 12"
occurs) is already dead: gov-frames excluded it per-window at the
verb windows — @842 ("94 [26n]" = "ne [noun]", ungrammatical
under 94="ne") and @1707 ("26 12 06", bound 06 forces 12
rightward). What survives is only the W2-local reading, fenced
above. No standing verdict contradicted or downgraded; §7 intact
(no polyvalence declared).

## Adverses

- "12='n' letter promoted (pending ratification)" — honored as
  stated; the promotion is load-bearing only for W2's reading
  (ii)/(iii) framing, and the fence does not depend on its
  ratification either way.
- "word-boundary decision must be contact-based" — honored: both
  exclusions rest on adjacency (byte contact), and the W2 fence
  rests on the contact record failing to force a boundary.

## Verdict: NULL (fence executed)

The rival is excluded at 2 of 3 la-windows (W1, W3) by absence of
the necessary 26+12 contact, excluded as a uniform value by prior
batteries, but remains live as a W2-local reading. The exclusion
claim is therefore not established at battery grade.

## Follow-ups proposed (for supervisor queuing)

1. `w2-26n-retest-16gate` (P3) — re-test W2's local "26n" rival once
   16's class/value is decided (gates on the red-team 16
   adjudication): a consonant-initial 16 kills reading (iii); a
   vowel-initial ne-alone modal 16 promotes it; either way the
   (i)-vs-(ii) choice narrows.
2. `tail-12-16-uniform` (P3) — census "12 16" x3 under 16's decided
   value; test whether 12 is uniformly word-initial before 16,
   which would turn the @843 boundary into a distributional
   argument at W2.

## Bookkeeping

- battery-queue.json: `noun26-26n-exclude` → status `verdict`,
  result `null`, date 2026-10-09 (temp-file + rename; pre-write
  assert confirmed queued/verdictless; JSON re-validated).
- Lock created on start, deleted on completion.
- R5005, sealed gates, red-team queue untouched.
