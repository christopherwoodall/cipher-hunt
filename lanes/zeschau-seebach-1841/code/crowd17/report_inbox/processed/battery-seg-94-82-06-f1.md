# Battery report: seg-94-82-06-f1 (NULL — 59 resolves "est"-as-word at 1186; frame-C re-test fails, F66 fence confirmed)

**Target:** seg-94-82-06-f1 — 59's local value at pair 1186 ("est"-as-word vs verb-unit); decides frame C of the 94-82-06 segmentation
**Worker:** 40c0578a-73cd-4c25-92ea-e25e4d19e249 | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py; 1,847 pairs / 96 types re-verified). Never canonical.py. No R5005 touched. No sealed gates touched. No data invented. Every @-offset re-derived from the stream. Lock: locks/seg-94-82-06-f1.lock created 2026-10-09T03:24:03Z, deleted on completion.

## Bar (verbatim from battery-queue.json)

> resolve 59's local value at pair 1186; then re-test frame C's "ne mentent/entendent est" parse

## Bar as numbered clauses (pre-registered before testing)

1. 59's local value at 0-based pair 1186 is named under standing values with <=1 ungranted assumption ("est"-as-word vs a bisyllabic verb-unit).
2. Frame C's "ne mentent/entendent est" parse is re-tested under the resolved value: it parses grammatically in 1841 French, or it is shown ungrammatical with rescues exhausted at battery grade.
3. Adverses answered: 59="est" stays provisional (no global promotion claimed here); F72's H4g refutation stands (the 94-82-06-06 4-gram is not re-declared a unit — 59's local value only).

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (asserts hold: 1,847 pairs, 96 distinct groups).
2. Verified frame C at 0-based 1182 [a6_10]: `78(1181) 94(1182) 82(1183) 06(1184) 06(1185) 59(1186) 42(1187) 06(1188) 84(1189) 59(1190) 46(1191)`.
3. Full census of 59 (n=27): every window tested for "est"-as-word compatibility; perfect legs vs compatible-with-caveat separated.
4. Enumerated every lexical candidate for a "bisyllabic verb-unit" reading of 59 at 1186 (06-59 leftward, 59-42 rightward, 59 as inflectional ending) and tested each against the lexicon.
5. Re-tested "ne mentent est" / "ne m'entendent est" for grammaticality in 1841 French with all rescues (noun-"est", clause boundary, inversion, predicate-noun with subject recovery).

## Window-level evidence (0-based pair indices)

**59 census (n=27): "est"-as-word compatible in 27/27; perfect legs in 15.**

Perfect "est" legs (zero assumptions): 94-59 "n'est" x3 — @559 [a3_02] `86 94 59 30 67 11` ("n'est pas" canonical), @763 [a5_03] `62 94 59 39 88` ("[62] n'est [39]"), @1796 [a8_10] `42 94 59 37 91` ("[42] n'est [37]"); 87-59 "c'est" @825 [a5_06] `13 24 87 59 38 82 01`; 87-11-59 "cela est" @463 [a2_10] `79 87 11 59 42 96 00` ("cela(87-11, granted compound) est [42-noun]" — copula + predicate noun, perfect); 64-59 "qui est" x3 — @1210 [a7_00] `21 65 64 59 32 48 96`, @1777 [a8_09] `24 87 64 59 19 48 74`, @316 [a2_04] `78 45 64 59 32 94 06` ("ce(45) qui(64) est [32]"); 84-59 "on est" x3 — @1291 [a7_03] `11 17 84 59 35 94 52`, @1448 [a7_09] `64 77 84 59 36 67 33`, @1804 [a8_10] `64 77 84 59 35 94 52`; 94-44-59 "ne l'est" @1715 [a8_06] `65 94 44 59 30 64 47` ("ne [44] est pas(30)" — the @1714 "ne l'est pas" promote); 76-59 @834 [a5_06] `11 77 76 59 35 56 17` ("[76-masculine-noun, promoted] est [35]").

Compatible (open neighbors, no contradiction): @103 `62 94 93 59 45 28 00` ("ne [93] est-ce(45)"); @448 `10 62 61 59 32 48 79` ("[62] [61] est [32]"); @528 `97 47 44 59 37 64 26` ("ce(47) [44] est [37]"); @554 `81 00 86 59 34 17 86` ("[86] est-i[l](34)" inversion reading available); @624 `76 82 14 59 37 33 29` ("m(82) [14] est [37]"); @912 `49 64 83 59 37 96 09` ("qui(64) [83] est [37]"); @1178 `74 32 48 59 37 77 78` ("[48] est [37]"); @1443 `01 52 68 59 37 64 77` ("[68] est [37]"); @1496 `00 66 15 59 24 89 41` ("[15] est [24]"); @1511 `41 12 61 59 39 81 88` ("[61] est [39]"); @1833 `24 82 16 59 36 69 64` ("[16] est [36]").

Compatible with caveat (flagged, not load-bearing): @216 [a2_00] `74 77 78 06 59 46 29 42` ("…[78] [06] est que(46)" — "est que" needs the 78/06 left block resolved); @1190 [a6_10] `42 06 84 59 46 07 24` ("on(84) est que(46)" — restrictive-"que" or "than" reading open).

**Zero windows force a non-"est" reading of 59.** 59 is word-standalone in all 27 windows; no window shows 59 word-internal.

**The 59-42 bigram (x2) is the local parallel:** @463 "cela est [42-noun]" is perfect with 59="est"-as-word and 42 noun-class (registry: 42=["noun","cls"]). At @1186 the same bigram recurs: `06 06 59 42` — "…[06] est [42]". The bigram behaves as "est"+"[42]" at 463; uniformity favors the same segmentation at 1186.

**Verb-unit candidates at 1186 — all dead:**
- 06(1185)-59(1186) = "ent"+"est" = "entest": non-lexical in French. (Note: 06(1185)'s pre is 06, not 82, so it sits outside the F61 islet in any case.)
- 59(1186)-42(1187) as one "est[42]"-word: contradicted by the @463 parallel, where "cela est [42]" parses perfectly as two words; a one-word reading there would be perverse. French "est-"-initial words (estimer etc.) would also need 42's value named (= ungranted) and clash with 42's noun class.
- 59 as an inflectional verb ending ("…entest"): no French verb form ends in "-entest".
- "s'est" (06(1185)="s'" + 59): "ne mentent s'est [42]" still lacks a subject; "mentent" cannot serve as one.

**Frame-C re-test under resolved 59="est"-as-word** (`78 94 82 06 06 59` → "…[78] ne mentent est" / "…[78] ne m'entendent est"):
- "ne mentent est": a finite verb followed by bare "est" is ungrammatical — French has no finite+est compound (auxiliary precedes the participle: "ont menti", never "mentent est").
- "ne m'entendent est": independently dead — "entendent" = en-tend-ent needs three post-82 groups ("ent"+"end"+"ent"); only two 06 groups exist ("ent"+"ent" ≠ "entendent"). The parent's elision fence stands.
- Rescues exhausted: noun-"est" ("l'est", the East) needs an article — bare "est" as noun is ungrammatical; clause boundary ("…ne mentent. Est [42]…") — "est" cannot open a declarative clause; "est-il" inversion needs 42="il" (42 is noun-class; interrogative mood ungranted); predicate-noun "est [42]" needs a subject left of 59, and the only left material is the negated VP "ne mentent", which cannot be a subject.
- 78's own value does not rescue the parse: the failure is at "mentent est" regardless of 78.

## Per-clause pass/fail

1. **59's local value at 1186 resolved — PASS.** "est"-as-word: 0 ungranted assumptions (rests on 59's provisional standing, the 27/27 global compatibility with 15 perfect legs, and the @463 59-42 parallel). The verb-unit alternative has no lexical candidate.
2. **Frame-C re-test — TESTED, PARSE FAILS.** "ne mentent/entendent est" is ungrammatical under the resolved value; every rescue fails at battery grade (each needs 2+ ungranted assumptions or contradicts standing values).
3. **Adverses answered — PASS.** 59="est" stays provisional — no global promotion is claimed; this battery resolves the local value only, which the provisional standing already permits. F72's H4g refutation untouched: the 94-82-06-06 4-gram is not re-declared a unit anywhere in this report.

## Verdict

**NULL.** 59's local value at pair 1186 resolves to "est"-as-word, but the re-test fails: frame C's "ne mentent/entendent est" does not parse. The F66 fence on frame C stands CONFIRMED at the local level — the fence is not lifted, and no segmentation is named. No standing verdict contradicted or downgraded. R5005, sealed gates, and the red-team queue untouched.

## Follow-up targets for the supervisor queue (null regeneration)

**F1a. id: "subject-1186-est42" | priority: 2**
claim: "name the subject of 'est [42]' at pair 1186, or fence the 1186 clause as subjectless"
bars: "one grammatical subject left of 59@1186 (ellipsis/subject-recovery with stated frame evidence, or 'est-il' inversion under 42's class) with <=1 ungranted assumption; else fence 1186 as a subjectless-'est' residual with stated cause"
evidence: "seg-94-82-06-f1 null (2026-10-09): 59@1186 resolved 'est'-as-word; 'est [42-noun]' is a clean copula+predicate but has no subject on its left (only the negated VP 'ne mentent')"
adverses: "42 is noun-class (battery) — 'il'-readings need red-team authority; do not re-test the 'mentent est' contact (decided here)"

**F1b. id: "val-42-estframes" | priority: 3**
claim: "name 42's value at the 59-42 bigram (@463/@1186)"
bars: "one value for 42 parsing both 'cela est [42]' @463 and 'est [42]' @1186 as predicate nouns with <=1 ungranted assumption; kill iff no value does"
evidence: "seg-94-82-06-f1 null (2026-10-09): 59-42 x2, both 'est'-as-word frames; 42 is noun-class with value open"
adverses: "42's class is battery-promoted — class standing is not re-opened, value only"

---
Lock: locks/seg-94-82-06-f1.lock created 2026-10-09T03:24:03Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No promotions made. No red-team verdicts modified or downgraded.
