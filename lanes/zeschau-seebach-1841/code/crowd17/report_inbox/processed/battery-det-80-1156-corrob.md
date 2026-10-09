# Battery verdict: det-80-1156-corrob

- Target: `det-80-1156-corrob` (priority 2)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 NOT touched.

## Bar (verbatim, pre-registered before testing)

"(a) identify 92's value in the '[92]er' infinitive governing @1156; (b) test the 92-29-80 word-internal escape byte-exactly; (c) census 'X fois' determiner slots to type 80's quantifier value."

Numbered clauses:

- **C1**: 92's value in the "[92]er" infinitive governing @1156 is identified (named, not just classed).
- **C2**: the 92-29-80 word-internal escape is tested byte-exactly (confirmed or refuted with exact counts).
- **C3**: a census of "X fois" (X-17) determiner slots types 80's quantifier value (names the quantifier or narrows it to a decided paradigm).

## Adverses (from queue)

- 92's class open (coordinate with class-92 / verb-92-subset / prenne-92-noun, do not duplicate their bars).
- @1156 HARD determiner stands per det-adj-80-adjudicate.

Coordination observed: verb-92-subset (PROMOTE, 2026-10-08): 92=verb on the
verbal-governor subset, value unnamed, split/polyvalence escalated to red team.
prenne-92-noun (KILL, 2026-10-08): noun VALUE arm dead; A14 set-level INF-signal
grant untouched. Neither bar re-run; both cited. No battery in the lane has ever
named a VALUE for 92 (inbox grep 2026-10-09: zero `92="<value>"` proposals).

## Method

Re-derived the @1156 window byte-exactly on the repaired stream; censused all 22
windows of 92, all 15 "X 17" windows, all 29-80 bigrams, and the 92-29-80 trigram.
Standing values used: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (pencil);
00=pour (A9), 84=on (A15), 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 47=ce
(A4); provisional 59=est, 77=le. Row a6_09 offset grade PROBABLE-WEAK per
crowd18 offset-validation (no offset requires change) — taken as given, not
re-audited. 1841 diplomatic French grammar throughout.

## Window-level evidence

### The @1156 frame (byte-exact)

@1154=92, @1155=29, @1156=80, @1157=17, row a6_09:
`84 02 00 92 29 80 17 77 82 44 83 21`
= `... pour [92]er [80] fois [le] ...` (00=pour, 29=er, 17=fois, 77=le prov.).

### C1 — 92's value

- 92-29 ("[92]er" infinitive) occurs **exactly once** in the stream (@1154). Hapax legomenon: no cross-window distributional leg exists to name the verb.
- 92's full census (n=22, re-derived): followers 79 x2, 69 x2, 60 x2, 64 x2, 62 x2, 63/50/98/47/67 x1...; predecessors 00 x6, 11 x3, 94/84 x2... The six "00 92" ("pour 92") windows (@49, @330, @593, @683, @978, @1154) share the governor but no shared stem evidence names a verb.
- Best available identification: **verb class** on the verbal-governor subset (verb-92-subset PROMOTE, coordinated not duplicated). The specific verb value (e.g. which -er infinitive sits in "pour [92]er [80] fois") is **open across the whole lane** — no battery has ever proposed one.
- "prendre"-family check: 92-29 = [92]+er; a "pren-" stem would give "prener", not French ("prendre" is 3rd group). No rescue via the prenne batteries (noun arm killed; 70-12-94 "prenne" fence is about 12/94, not 92).
- **C1: FAIL** — value not identified at battery grade. (Epistemic failure, not falsification: no window forces a value false.)

### C2 — 92-29-80 word-internal escape (byte-exact)

- Trigram 92-29-80: **1 occurrence** (@1154–1156). No distributional support for a word-internal reading.
- Bigram 29-80: **4 occurrences** — @1031 (`01 03 29 80 77 11`), @1155 (the target window), @1321 (`24 03 29 80 08 62`), @1595 (`81 03 29 80 67 77`). In the three non-target windows 80 sits in nominal/object slots ("[X]er [80] le", "[X]er [80] et"), never demonstrably word-internal.
- Decisive point (corroborating det-adj-80-adjudicate escape (a)): even if 92-29-80 were one word ("pour [92er80] fois"), the **determiner gap before "fois" persists** — the escape does not supply the missing determiner. Dead on arrival, independent of word boundaries.
- **C2: PASS** — escape tested byte-exactly and confirmed dead (unique trigram, no word-internal support, determiner gap persists regardless).

### C3 — "X fois" census (15 windows)

| @ | row | X | X known? |
|---|-----|---|----------|
| 16 | a1_00 | 53 | open |
| 237 | a2_01 | 41 | open |
| 307 | a2_04 | 20 | open (feminine-noun filter) |
| 367 | a2_06 | 70 | **=pre (pencil)** — "pre fois" ungrammatical as two words |
| 450 | a2_09 | 79 | **=tout (A5)** — "tout fois" ungrammatical |
| 554 | a3_01 | 34 | **=i (pencil)** — "i fois" ungrammatical |
| 836 | a5_06 | 56 | open |
| 879 | a5_08 | 78 | open ("ver" lead) |
| 924 | a5_10 | 71 | open |
| 1038 | a6_03 | 40 | **=e (pencil)** — `11 70 82 34 29 40 17` = "la première fois": 40 word-internal |
| 1156 | a6_09 | 80 | **target** — "pour [92]er [80] fois" |
| 1287 | a7_03 | 11 | **=la (pencil)** — "pour la fois": bare, marginal without adjective |
| 1459 | a7_09 | 79 | =tout (A5) again |
| 1556 | a8_01 | 40 | =e (pencil) |
| 1756 | a8_08 | 58 | open |

13 distinct X values across 15 windows. The X-slot is **heterogeneous**: @1038 proves
X can be a word-internal syllable (40="e", last syllable of "première", with
17=fois standalone — the full "la première fois" phrase byte-confirmed
`11 70 82 34 29 40 17`); @367 (70="pre") and @450/@1459 (79="tout") cannot be
standalone determiners of "fois" either. The naive "X = determiner of fois"
frame fails lane-wide, so the census **cannot type 80's quantifier value**.
- Corroborating uniqueness: 80-17 bigram occurs **once** (@1156); @1156 is the only "pour [inf] [80] fois" in the stream.
- French paradigm for the slot ("pour [inf] [Q] fois"): une / deux / plusieurs / quelques / chaque / maintes — no distributional leg at battery grade picks among them.
- **C3: FAIL** — quantifier value stays open. (What stands: 80 is determiner/quantifier-CLASS at @1156, HARD per det-adj-80-adjudicate, corroborated by C2.)

## Per-clause pass/fail

1. C1 (identify 92's value): FAIL — hapax infinitive; value open lane-wide; verb class only (coordinated promote).
2. C2 (92-29-80 escape byte-exact): PASS — tested, confirmed dead (unique trigram; determiner gap persists regardless).
3. C3 (type 80's quantifier value): FAIL — X-slot heterogeneous (word-internal syllables proven: 40="e" in "première" @1038); no quantifier paradigm emerges; value open.

## Adverses answered

- 92's class open: respected — class-level verb finding cited from verb-92-subset, not re-derived; no value invented; noun arm's kill acknowledged.
- @1156 HARD determiner: not re-litigated — C2 corroborates it (escape dead); the standing null's escalation to poly-80-docket is untouched.

## Verdict: NULL

The frame is not closed: neither 92's verb value nor 80's quantifier value is
identified at battery grade. The failures are epistemic (hapax + heterogeneous
census), not falsifications — no window forces the claim false, so this is not
a kill. Positive residue: (i) the 92-29-80 escape is dead byte-exactly,
corroborating @1156's HARD determiner; (ii) the X-17 census proves the
"determiner slot" frame is not uniform lane-wide (word-internal X's exist),
which constrains all future "fois"-slot typing; (iii) "la première fois" byte-
confirmed at @1035–1041 (`11 70 82 34 29 40 17`). No standing verdict
contradicted or downgraded. R5005, sealed gates, and the red-team adjudication
queue untouched. Feeds poly-80-docket (unchanged docket evidence + this
corroboration).

## Follow-ups (null regenerates work)

1. `verb-92-value` (P2): name 92's verb value. The [92]er hapax cannot do it;
   test the other five "pour 92" windows (@49, @330, @593, @683, @978) for a
   shared verb stem, or coordinate with the split-92 red-team docket once the
   class question resolves. Do not duplicate verb-92-subset's class bars.
2. `quant-80-paradigm` (P3): type 80's quantifier (une/deux/plusieurs/quelques/
   chaque paradigm) via agreement or ellipsis frames; gate on poly-80-docket —
   if 80 goes positional-resolution, the quantifier value may resolve with it.
3. `x17-wordbound-audit` (P3): audit all 15 X-17 windows for word-internal vs
   standalone-17 boundaries (this battery proved heterogeneity at @1038/@367;
   complete the audit). Resolves whether 17=fois is uniformly standalone;
   feeds any future "fois"-slot typing.

## Bookkeeping

- Lock `locks/det-80-1156-corrob.lock` created 2026-10-09T02:41:15Z, deleted on completion.
- `battery-queue.json`: target `det-80-1156-corrob` queued → verdict/null, own entry only via temp-file + rename, no downgrade (no prior verdict existed).
