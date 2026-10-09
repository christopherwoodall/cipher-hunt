# Battery verdict: val-61-contact

**Verdict: KILL** — no single French value can cover the four discriminating frames.
The @644 frame forces 61 into the nominal class ("ce __") while @1510 forces 61 into
the clitic/adverb class ("n' __ est"); the two classes are disjoint, so the bar's
primary disjunct ("one value covering ...") is deductively false given standing
values. Fencing five disjoint classes is not fenceable polyvalence in the lane's
sense (cf. 67 et/veut: two values, one positional rule). Partial rivals cover at
most three frames.

## Target

- id: `val-61-contact` (priority 2)
- claim: dedicated 61 value triangulation on the four discriminating frames
- evidence: battery-seg-61-94-word.md follow-up #2
- adverses: none stated

## Bar (verbatim from battery-queue.json)

one value covering "ce 61" @644, "61 par ce que" @223, "n 61 est" @1510, "61 e/pre fois" @1556/@367, or fenced polyvalence escalated to red team

## Numbered pass/fail clauses (pre-registered before testing — bar not modified after data)

1. **Clause 1 ("ce 61" @644):** PASS iff one single French word value for 61 renders the
   window `... 24 87 61 88 77 ...` grammatical with banked values held fixed
   (87=ce granted; 77=le provisional).
2. **Clause 2 ("61 par ce que" @223):** PASS iff the SAME value renders
   `... 89 61 96 87 46 ...` grammatical (96=par promoted, 87=ce granted, 46=que pencil;
   "par ce que" read as "parce que" or "par ce que", reading stated in evidence).
3. **Clause 3 ("n 61 est" @1510):** PASS iff the SAME value renders
   `... 12 61 59 39 ...` grammatical (12=n clitic, 59=est provisional held fixed).
4. **Clause 4 ("61 e/pre fois" @1556/@367):** PASS iff the SAME value renders BOTH
   `... 93 61 40 17 ...` ("61 e fois": 40=e pencil, 17=fois promoted) and
   `... 49 61 70 17 ...` ("61 pre fois": 70=pre pencil, 17=fois promoted) grammatical.
5. **Clause 5 (fenced-polyvalence fallback):** if no single value passes 1–4, PASS iff the
   four frames fence into a principled polyvalence (disjoint frame classes, stated
   positional/class resolution rule, no contradiction with any standing verdict in §7) —
   escalated to the red team; overall verdict then null per §4.

Verdict rule: **promote** iff clauses 1–4 pass and every stated adverse is answered
(none stated). **kill** iff a clause fails at kill grade (a window forces the claim
false, or a distributional test rejects at the lane's standard), or a cleaner rival
value is demonstrated on the same frames. **null** otherwise, with 1–3 follow-up
targets proposed in-report.

## Method

Read BATTERY-PROTOCOL.md §1–§8 in full before testing. Created
`code/crowd17/next-token/locks/val-61-contact.lock` on start (agent id +
2026-10-09T02:52:00Z); no stale lock present. Parsed the repaired 1,847-pair stream
from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` with the
upstream byte-exact tokenization (`[s[i:i+2] for i in range(o, len(s)-1, 2)]`,
same as `code/side-keyhunt/repair_parse.py`). `canonical.py` never touched. R5005,
sealed gates, and the red-team adjudication queue untouched. All four @-offsets
re-derived on the repaired stream (18 windows of 61 total; offsets match the
seg-61-94-word census). No prior counts trusted. Standing values held fixed per §7.

## Window-level evidence

All windows byte-verified on the repaired stream (1,847 pairs, 18 windows of 61).

### Frame A — "ce 61" @644 (row a4_02)

`[643]24 [644]87(ce) [645]61 [646]88 [647]77(le*) [648]78 [649]52 [650]82(m) [651]94(ne)`
Left: `... 89 48 20 24 87 61 88 77 78 ...`. With 87="ce" (granted), 61 must satisfy
"ce __": 61 is forced into the **nominal class** (noun or adjective: "ce fait",
"ce temps", "ce premier", "ce seul", "ce même"), or the compositional "ci"
("ce"+"ci"="ceci", parallel to promoted "cela"=87+11).

### Frame B — "61 par ce que" @223 (row a2_01)

`[222]89 [223]61 [224]96(par) [225]87(ce) [226]46(que) [227]98 [228]83 [229]82(m)
[230]96(par) [231]21`. "89 61 par ce que 98 ...". Read "par ce que" as "parce que"
(1841 orthography): 61 must be a **3rd-person verb** ("89 fait/dit parce que") or,
if 89 is a verb, an **object noun** ("89 ceci/cela parce que" — "dit ceci parce
que" is clean French). 89's profile (n=14; pre {29:5, 24:3}; fol {48:3, 84:2})
does not resolve its class; both readings kept open.

### Frame C — "n 61 est" @1510 (row a7_11)

`[1508]41 [1509]12(n) [1510]61 [1511]59(est) [1512]39 [1513]81 [1514]88
[1515]11(la)`. 12="n" (prenne-fenced: 12 followers include 94 x3, "70 12" x3) and
59="est" (provisional but distributionally firm: n=27, predecessors 84=on x4,
64=qui x3, 94=ne x3; followers 37 x6, 32 x3, 35 x3 — predicative frames A1).
"41 n 61 est 39": between ne/n' and "est" only a clitic or adverbial pronoun fits.
61 is forced into **{y, en, l', s'}**: "n'y est", "n'en est" ("il n'en est rien"
if 39="rien"), "ne s'est", "ne l'est". This conclusion is robust to 59's exact
value (holds for 59="est" or "a": "n'y a"). No nominal reading is available.

### Frame D — "61 e/pre fois" @1556 (row a8_01) / @367 (row a2_06)

- @1556: `[1555]93 [1556]61 [1557]40(e) [1558]17(fois) [1559]11(la)`. 40="e" is the
  pencil feminine adjectival "e" (crib "11 70 82 34 29 40" = "la pre m i er e").
  "40 17" ("e fois") occurs exactly 2x stream-wide: @1039 (crib tail
  "82 34 29 40 17" = "m i er e fois", i.e. "première fois") and @1557 ("61 40 17").
  61 **substitutes for "70 82 34 29" ("premier")** positionally: "61"+"e"+"fois" =
  "première fois" with 61="premier" (masculine ordinal stem). Crib-grade structural
  parallel — the strongest positive finding of this battery.
- @367: `[366]49 [367]61 [368]70(pre) [369]17(fois)`. "70 17" ("pre fois") occurs
  exactly **1x stream-wide**, here. "61 pre fois" admits no clean single-word
  reading with 61="premier" ("premier pre fois" is ungrammatical). Best available
  reading: 61="la" + "pre" as manuscript abbreviation of "première"
  ("la pre[mière] fois", cf. the crib's full spelling "70 82 34 29 40") —
  but that assigns 61 a **determiner** value disjoint from the ordinal stem.

### Class inventory across the four frames

| frame | forced class for 61 |
|---|---|
| @644 "ce __" | nominal (noun/adj), or "ci" (→"ceci") |
| @223 "__ par ce que" | verb (3sg), or object noun (needs 89=verb) |
| @1510 "n' __ est" | clitic/adverbial {y, en, l', s'} |
| @1556 "__ e fois" | ordinal stem (premier/second/dernier/seul → "seule") |
| @367 "__ pre fois" | determiner (la/une) before abbreviated "pre" |

Five disjoint classes. {y,en,l',s'} ∩ nominal = ∅ ("ce y", "ce en", "ce l'",
"ce s'" all ungrammatical); ordinal stems and determiners are disjoint from the
clitic set as well.

### Candidate sweep (best partial rivals — all fail the full bar)

- **61="premier"**: passes @1556 ("première fois", crib-parallel); @644 "ce premier
  88" grammatical iff 88 is a noun (88's followers: 77=le x3, 11=la x2 — 88 takes
  determiners after it, consistent with 88=verb or noun; unresolved). Fails @223
  ("89 premier parce que" ungrammatical), @1510 ("ne premier est" ungrammatical),
  @367 ("premier pre fois" ungrammatical).
- **61="seul"**: passes @644 ("ce seul [noun]"), @223 ("89 seul parce que" iff
  89=verb — "il reste seul parce que"), @1556 ("seule fois" — "la seule fois" is
  idiomatic). Best single-value coverage: 3 of 5 sub-frames. Fails @1510
  ("ne seul est") and @367 ("seul pre fois").
- **61="ci" (→"ceci"=87+61)**: passes @644 ("ceci 88 le ..." iff 88=verb);
  elegant parallel to promoted "cela"=87+11, but single occurrence (weak) and
  fails @223 ("89 ci par ce que" needs 89="ce", undemonstrated; "ceci parce que"
  is ungrammatical), @1510, @1556/@367.
- **61="fait"**: passes @644 ("ce fait") and @223 ("89 fait parce que"); fails
  @1510, @1556, @367.
- **61="y"/"en"/"s'"**: pass @1510 only; fail @644 ("ce y/en/s'" ungrammatical),
  @223, @1556, @367.

No candidate passes clauses 1 and 3 jointly; none passes all of 1–4.

## Per-clause pass/fail

1. **Clause 1 ("ce 61" @644): FAIL at kill grade for every value admitted by
   clause 3.** @1510 forces 61 ∈ {y, en, l', s'} (P2 above, robust); none of
   these renders "ce __" grammatical. The @644/@1510 class collision is
   deductive given standing values (87=ce granted; 12="n" prenne-fenced;
   59="est" distributionally firm) — a window-pair forcing the single-value
   claim false.
2. **Clause 2 ("61 par ce que" @223): FAIL** — no value passing clause 1's
   nominal requirement ("ce __") also satisfies the verbal/object slot, and
   the clause-3 set {y,en,l',s'} fails here too ("89 y par ce que" violates
   pronoun order; "89 en/s' par ce que" ungrammatical).
3. **Clause 3 ("n 61 est" @1510): FAIL for every value admitted by clause 1** —
   the converse of (1); the collision is symmetric.
4. **Clause 4 ("61 e/pre fois"): FAIL** — @1556 wants an ordinal stem
   (61="premier", crib-parallel), @367 wants a determiner (61="la" before
   abbreviated "pre"); no single value covers both sub-frames.
5. **Clause 5 (fenced polyvalence): FAIL** — five disjoint classes with no
   principled positional/class resolution rule (contrast 67 et/veut: two values,
   one rule). Stipulating five frame-specific values is not fencing; nothing to
   escalate as polyvalence.

**Overall: KILL.** The bar's primary disjunct is false by class-collision proof,
not by inconclusive testing; the polyvalence disjunct is unfenceable. This is a
kill of the *single-value claim*, not of 61 as an object of study — the token
needs re-segmentation (cf. the 55-61-94 lead in battery-seg-61-94-word) or a
multi-value treatment under narrower bars.

Caveat: the kill rests on standing values (87=ce, 12="n", 59="est"). If the red
team revalues any of the three, this kill is re-openable — recorded here, not
hidden.

## Follow-ups proposed (kill verdict; queued per the supervisor's audit rule —
nulls regenerate work, and these leads should not die with the single-value claim)

1. **`val-61-premier`** (P2): narrow bar on the ordinal frame only. Test 61="premier"
   (masculine ordinal stem): (a) "61 40 17" @1556 = "première fois" with the
   crib-structural parallel stated (61 substitutes "70 82 34 29"); (b) "ce premier
   88" @644 with 88's class resolved (88 followers 77=le x3, 11=la x2); (c) fence
   @223/@1510/@367 as out-of-scope for this value (expected fails → split, not
   promotion).
2. **`seg-ceci-87-61`** (P3): test compositional "ceci"=87+61 at @644, parallel to
   promoted "cela"=87+11. Bars: (a) 88 verb-class confirmation for "ceci 88 le";
   (b) single occurrence (@644) recorded as the central weakness; (c) do not
   disturb cela-87-11.
3. **`frame-367-la-pre`** (P3): resolve @367 "49 61 70 17". Test 61="la" +
   "70"=manuscript abbreviation of "première" (cf. crib's full "70 82 34 29 40"):
   needs 49's value ("c'est la première fois"? 49: n=12, followers 74 x5, 24 x2,
   64 x2). "70 17" is unique stream-wide — abbreviation vs. encoding anomaly is
   the discriminating question.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-61-contact.md` (this file).
- Queue: `val-61-contact` → status `verdict`, result `kill`, date 2026-10-08
  (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict).
- Lock `locks/val-61-contact.lock` created on start (no stale lock present),
  deleted on completion.
- Standing verdicts: none contradicted, none downgraded. R5005, sealed gates,
  red-team adjudication queue untouched.
- Bar + numbered clauses were written into this report BEFORE testing (§2);
  the bar was not modified after seeing data.
