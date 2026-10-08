# Battery report: noun-44 — "44 is a noun"

- Worker: battery-worker noun-44, agent 985231f6-0e1d-42e6-8f2c-8950f7a99287
- Date: 2026-10-08 (lock created 2026-10-08T16:26:49Z)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per repair_parse.py). canonical.py NOT used. R5005 untouched.
- 44: n=15 on the repaired stream. All @-offsets below are repaired-stream indices (verified by re-parse; they coincide with the finder brief's indices).

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"(1) article/demonstrative frames hold: '77 44' x2 (@207, @1678) and '47 44 59 37' @527 ('ce 44 est 37'); (2) complement frames hold: '44 00=pour' x3 (@1311, @1583, @1679); (3) @1714 'ne 44 est pas' resolves via ONE stated parse (e.g. '...65ne' word-final + '44 est [30-predicative]', or a 59/30 re-value); (4) '44 11' @1617 and '44 29 48' @540 ('44ere') resolve or are fenced with stated cause"

Numbered clauses (frozen before testing):
1. '77 44' x2 (@208, @1679 repaired) and '47 44 59 37' @527 hold as article/demonstrative + noun frames.
2. '44 00' (=pour) x3 (@1311, @1583, @1679 repaired) hold as complement frames.
3. @1714 '94 44 59 30' resolves via ONE stated parse with 44 as noun (bar's examples: '65ne' word-final + '44 est [30-predicative]', or a 59/30 re-value).
4. '42 44 11' @1617-1619 (repaired @1617=42 @1618=44 @1619=11) and '44 29 48' @540 ('44ere') resolve or are fenced with stated cause.

## Method

Enumerated all 15 windows of 44 on the repaired stream with ±10 context. Parses use only standing values: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); battery-promoted/queue-standing (94=ne, 12=n + 48=e, 30=pas, 06=ent); provisional (59=est, 77=le). Positional table (predecessor/successor bigrams):

@208: 77 44 50 | @249: 32 44 94 | @527: 47 44 59 | @540: 12 44 29 | @797: 37 44 77 | @800: 86 44 74 | @1070: 11 44 74 | @1160: 82 44 83 | @1311: 92 44 00 | @1583: 12 44 00 | @1603: 00 44 70 | @1618: 42 44 11 | @1679: 77 44 00 | @1714: 94 44 59 | @1839: 42 44 83

'94 44' occurs exactly ONCE globally (this is the only 'ne 44' adjacency in the corpus).

## Window-level evidence

**Clause-1 frames.**
- @207-208 '77 44': full window '42 06 77 44 50' — "06 77 44" = "[ent] le [44]": '77 44' = 'le [44]' holds given 77='le' (provisional, §7-usable; le-77 battery returned null, not kill). 44 reads as article-headed noun (direct object of a 3pl "[42]ent" verb or of the clause — 42's own contact is 42's business, not adjudicated here).
- @1677-1681 '74 77 44 00 46': "74 le [44] pour que" — article + noun + 'pour que' complement. Clean under 77='le' (prov), 00='pour' (granted A9), 46='que' (GT).
- @526-530 '47 44 59 37 64': "ce [44] est [37] qui" — 47='ce' (granted A4), 59='est' (provisional), 37 predicative frame (granted A1), 64='qui' (granted). "ce [N] est [pred] qui…" grammatical with 44 as subject noun. Flagship holds; load-bearing on 59='est' as briefed.

**Clause-2 frames.** '44 00' x3, all with @+1 = 00='pour' (granted A9): @1311 ('92 44 00 36': "[92] [44] pour [36]"), @1583 ('53 12 44 00 36': "53 n [44] pour [36]" — left edge fenced: 53/12 open, non-discriminating for the bigram), @1679 ('77 44 00 46': "le [44] pour que"). All three hold as noun + 'pour'-complement ("le [44] pour que…" = "le moyen/motif pour…" shape).

**Supporting windows (outside the bar, recorded for the record).**
- @248-251 '32 44 94 65': "91 [32] [44] ne [65]" — 44 as SUBJECT noun before 'ne' ("[32-adj] [44] ne [verb-65]…", bare 'ne' per the queued ne-alone-02-74 hypothesis). Supports noun-44; shows 94='ne' does not always force a clitic after it (44 precedes 'ne' here).
- @1069-1070 '11 44': "70 39 11 44" = "pre [a/à] la [44]" — 'la [44]' article + noun frame. Supports.
- @1602-1603 '00 44': "pour [44] pre…" — 'pour' + noun. Supports.

**Clause-3 window @1712-1716** ('65 94 44 59 30', row a8_06): 94='ne' (battery-promoted, 6 independent legs, zero contradictions — @1713 was NOT one of its legs), 59='est' (provisional; 'n'est' frames hardened by the est-59-frames promote battery), 30='pas' (battery-promoted; @1713 WAS its clause-2 leg, read there as "ne [44] est pas" with 44 in "clitic/adverb slot"). French grammar (textbook, not distributional): between 'ne' and the finite verb ONLY clitic pronouns (le/la/les/lui/leur/en/y/me/te/se/nous/vous) may intervene. A lexical noun can never occupy the 44 slot in "ne [44] est pas". Candidate parses, each tested:
  (a) Bar's '65ne' word-final + '44 est [30-predicative]': requires 94 ≠ 'ne'-particle at @1713 (word-final syllable on 65) AND 30 ≠ 'pas' at @1716. This overturns pas-30's clause-2 leg (this very window) and tensions ne-94's unconditioned promotion — not available at battery level without escalation. Rejected as a resolution; recorded as an escalation path (see follow-ups).
  (b) Bar's 59/30 re-value: structurally insufficient — the ungrammaticality is the ne–44 adjacency, not 59/30. 'ne 44 [59≠est] [30=pas]' still puts a noun between 'ne' and the verb; 'ne 44 est [30≠pas]' likewise. Re-value of neither 59 nor 30 removes the ne+noun violation. Fails.
  (c) Clitic reading ("n'en est pas" / "ne l'est pas" shapes, cf. pas-30's own parse): grammatical, but 44 is then a pronoun/clitic, not a noun — kills the claim as stated (second value at one window needs a red-team polyvalence declaration per §7; 67 is the sole true polyvalence).
  (d) 65-as-subject ("[65-noun] ne [44]…" — 65 takes 'qui' x3, looks nominal): the verb must still immediately follow 'ne' modulo clitics, so 44 is again forced into verb-or-clitic slot; "65 ne [44-verb] est pas" and "65 ne [44] [59] pas" are both ungrammatical. Fails.
  (e) Elision ("n'[44] est pas", 44 vowel-initial): same structural violation. Fails.
  No stated parse resolves "ne 44 est pas" with 44 as a lexical noun under standing values. **Clause 3 FAILS at kill grade: the window forces 44 into a non-noun (clitic) slot.**

**Clause-4 adverses (fenced with stated cause).**
- @1617-1620 '42 44 11 84' ("[42] [44] la on"): '11 84' = 'la on' is ungrammatical under banked 11='la' + granted 84='on' for EVERY value of 44 — the anomaly localizes to the right edge, independent of 44. Fenced as non-discriminating for 44 (the '44 la' adjacency needs a clause boundary whose right side does not parse under open 78/76/31). No value of 44 repairs 'la on'; no reading of 44 is forced false here.
- @538-543 '91 12 44 29 48 42' ("91 n [44]er e 42"): with 12='n' (battery), 29='er' + 48='e' (pencil + battery), the only grammatical parse is word-internal composition — feminine stem '44'+'ere' ("[X]ère"/"[X]ere"-shaped, cf. 'manière'/'première'). Fenced with stated cause: 44 as nominal STEM here (parallel to @1160 '82 44' = "m[44]", 82='m' letter + 44, most naturally word-internal "le m[44]"), distinct from the whole-word noun frames. Consistent with 44 being nominal; neither confirms nor kills whole-word noun-44 (cf. A10 stem/whole HOLD precedent for 33/86).

## Per-clause verdicts

1. Article/demonstrative frames: PASS ('77 44' x2, '47 44 59 37' all hold; load-bearing values provisional-or-better).
2. Complement frames: PASS ('44 00' x3 all hold under 00='pour').
3. @1714 'ne 44 est pas': FAIL at kill grade — no stated parse admits a lexical noun between 'ne' and 'est'; both bar-suggested escapes tested and rejected ((a) needs overturning standing battery verdicts = escalation, not resolution; (b) structurally insufficient).
4. Adverses @1618 / @540: FENCED with stated cause (right-edge 'la on' ungrammatical independent of 44; '44ere' = word-internal feminine-stem composition).

## Verdict: KILL

One bar clause fails at kill grade per §4 ("a window forces the claim false"): @1714 '94 44 59 30' forces 44 into a clitic/pronoun slot under standing values (94='ne' battery-promoted on 6 independent legs; 59='est' provisional, 'n'est' frames hardened by est-59-frames). A lexical noun cannot intervene between 'ne' and the finite verb; the only grammatical roles for 44 there are clitic/adverb ("n'en est pas"/"ne l'est pas" shapes). A second value for 44 at one window would need a red-team polyvalence declaration (§7: 67 is the sole true polyvalence). No cleaner global rival is demonstrated ('en'/'le' shapes fail 'le 44' x2, 'ce 44 est', '44 pour' x3); the kill rests on the single-window forcing, which §4 expressly allows.

Epistemic status (marked up front): the kill is conditional on 94='ne' (battery-promoted, PENDING red-team ratification) and 59='est' (provisional) standing. If the red team rejects either, this kill must be revisited. The kill is CONSISTENT with all standing verdicts — in particular it agrees with pas-30's own reading of this window (44 in "clitic/adverb slot"); no standing verdict is contradicted or downgraded.

Note on the bar's escape hatch: the '65ne word-final + 44 est [30-predicative]' parse was tested and is unavailable at battery level because it overturns pas-30's clause-2 leg (this window) — that path is an escalation to the red team, not a battery-level resolution. 65's profile ('qui' x3, nominal-looking) does not rescue it: "[65] ne [44]…" still forces 44 into verb-or-clitic slot (tested as parse (d), fails).

## Follow-ups (regeneration notes; kill ends the claim, the work continues)

1. **pronoun-44-1714**: test the clitic reading forced at @1714 — is 44 'en' ("n'en est pas") or 'l'-shaped ("ne l'est pas") at this window, and does EITHER value survive the 'le 44' x2 / 'ce 44 est' / '44 pour' x3 frames? (Expectation: neither survives globally → 44's class question stays open; do not force.)
2. **stem-44-nominal**: adjudicate 44 as nominal STEM vs whole word — '44ere' @540, 'm[44]' @1160 ('82 44'), vs whole-word frames ('le 44' x2, 'la 44' @1070, '44 pour' x3, subject-44 @249/@527). Coordinate with the A10 stem/whole HOLD precedent (33/86).
3. **escalate-1714-ne44** (red team): the '65ne word-final + 30-predicative' re-parse of @1712-1716, which would re-open pas-30's clause-2 leg. Battery-level finding: unavailable without overturning standing verdicts; needs red-team adjudication of 94's conditioning and 30's window-local values.

## Provenance

Every number above traces to the repaired 1,847-pair stream (re-parse verified in-work: n(44)=15; bigram counts '77 44' x2, '44 00' x3, '42 44' x2, '94 44' x1 re-derived from the stream, not copied from the brief). No invented data. R5005, sealed gates, and the red-team adjudication queue untouched. Lock deleted on completion.
