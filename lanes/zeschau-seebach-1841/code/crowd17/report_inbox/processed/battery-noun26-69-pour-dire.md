# Battery verdict: noun26-69-pour-dire

- Target id: `noun26-69-pour-dire`
- Claim: "'[69] 26 pour dire' x3 decides noun-vs-verb via 69's class"
- Date: 2026-10-09
- Worker: agent 0169321f-a469-4c84-a0d9-d270b2dd1eb1
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
- Offset convention: 0-based pair indices (matches the noun26 battery family). The brief's @405/@933/@1627 are the 8-gram starts (69's token); the trigram '26 00 33' sits one pair later.

## Bar (verbatim, pre-registered)

"(a) trigram '26 00 33' x3 re-derived; (b) 69's class named from its full 12-window profile (followers 26 x3, 13 x2, 88 x2, 14, 24, 11, 74, 64; predecessors scattered); (c) '26 pour dire' parses under exactly one class with 69 fixed — or the frame is recorded NULL with the 'pour dire' selection puzzle stated and 1-3 follow-ups proposed"

## Bar restated as numbered pass/fail clauses (frozen before testing)

1. Trigram '26 00 33' occurs exactly 3x on the repaired stream (byte re-derivation).
2. 69's class is named from all 12 of its windows (followers 26 x3, 13 x2, 88 x2, 14, 24, 11, 74, 64; predecessors scattered — both censuses re-derived).
3. With 69's class fixed, '26 pour dire' parses under exactly one class (noun vs verb decided), or the frame is recorded NULL with the 'pour dire' selection puzzle stated plus 1-3 follow-ups.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/noun26-69-pour-dire.lock` on start (deleted on completion). Re-derived the stream in-session (1,847 pairs / 96 types asserted). Standing values used, cited not re-litigated: 11=la, 34=i, 29=er, 40=e, 82=m, 70=pre, 46=que, 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour (A9), 84=on (A15, re-derived unconditioned), 47=ce (A4), 94=ne (STRONG LEAD), 06=ent, 30=pas, 88=verb (promoted), 93=verb (promoted), 98=finite verb (promoted), 24=finite modal verb (promoted; 24-en-verb-conflict is red-team P2), 13=les object pronoun (battery-promoted), 59=est (provisional), 26 positional rule R17-020 (HELD under §7: noun in '11 (02)? 26', verb-class elsewhere), 67 et/veut positional rule (sole true polyvalence).

## Clause 1 — trigram re-derived: PASS

'26 00 33' occurs exactly **3x**: 0-based @406, @934, @1628 (26-token index). The 8-gram '69 26 00 33 21 64 37 01' occurs 2x at 0-based @933 and @1627 — **byte-identical**, formula-bound, counted once (as the brief's evidence already records). The third attestation @405-408 ('34 69 26 00 33 01') is independent: different left edge ('34 69' vs '56 69') and different tail ('33 01' vs '33 21 64 37 01'). So: 3 trigram tokens, **2 independent attestations**.

## Clause 2 — 69's class from the full 12-window profile

Re-derived: 69 n=12 @ [67, 177, 405, 805, 933, 1115, 1259, 1266, 1380, 1413, 1627, 1835]. Follower census matches the brief exactly: 26 x3, 13 x2, 88 x2, 14, 24, 11, 74, 64. Predecessors scattered: 92 x2, 56 x2, 21, 34, 53, 30, 29, 46, 97, 36 (singletons).

Window-by-window class test (noun vs verb). Nominal-69 = 69 heads or modifies a nominal phrase; verbal-69 = 69 heads a verb phrase.

- @67 `12 94(ne) 92 | 69 | 13(les) 24(V) 56`: "ne [92] [69] les [24-V]". 92 = noun (solid: 'la 92' x3, '92 qui' x2, 'pour 92' x6). Verb-69 fails ("ne [92] [69-V] les [24-V]" = double finite verb, clitic misordered). Nominal-69 parses: subject NP "92 69" (69 = head noun or adjective) + clitic "les" + finite 24. **Nominal.**
- @177 `87(ce) 86 21 | 69 | 14 24(V) 87(ce)`: "ce [86] [21] [69] [14] [24-V] ce". Subject "ce 86 21 69" + verb 24 (14 = intervening adverb/participle, fenced). Verb-69 fails. **Nominal.**
- @405 `88(V) 53 34(i) | 69 | 26 00(pour) 33`: double finite verb (88, 26) forces a clause boundary: "[88-V] [53] i. [69-N-subj] [26-V] pour [33]". (53/34 contact fenced: values open.) Verb-69 fails outright. **Nominal** — and this is formula attestation 1.
- @805 `98(finV) 53 | 69 | 24(V) 24(V) 41`: "[98-V] [53]. [69-N-subj] [24-V] [24] [41]" — parses up to the '24 24' contact (@806), which is a known independent puzzle (fenced to 24's class; cf. disc-01-24-ci-X, red-team P2 24-en-verb-conflict). Verb-69 fails earlier. **Nominal** (tail fenced with stated cause).
- @933 `98(finV) 83 56 | 69 | 26 00(pour) 33 21 64(qui)`: "[98-V] [83] [56]. [69-N-subj] [26-V] pour [33] [21] qui [37]". **Nominal** — formula attestation 2a. (21's value open, fenced; "pour [33] [21] qui" is purpose-clause-shaped regardless.)
- @1115 `65(N) 38 30(pas) | 69 | 11(la) 88(V) 70(pre)`: nominal-69 fails ("pas [69-N]" — 'pas' cannot precede a bare noun; "la [88-V]" then dangles without a subject). Verbal-69 parses: "[65 38 NP] … pas [69-modal-inf] la [88-inf]" — the standard negated-infinitive construction "ne pas [modal] la [infinitive]" (cf. "ne pas pouvoir la voir"). The "70 12 06 14" tail is fenced (70='pre' banked as prefix; its standalone role here unresolved — does not affect the "pas 69 la 88" core). **Verbal (modal infinitive).** This is the brief's "'69 11' pulls both ways" window: it pulls verb, cleanly.
- @1259 `61 31 29(er) | 69 | 88(V) 01 09`: "[31]er [69-N-subj] [88-V] [01] [09]". Verb-69 fails ("er [69-V] [88-V]"). **Nominal.**
- @1266 `11(la) 50 46(que) | 69 | 88(V) 24(V) 30(pas)`: "la [50] que [69-N-subj] [88-V]. [24-V] pas [20] qui(64) ce(47)" — relative clause "que 69 88" complete, then a new clause "[24-V] pas [20]" = bare-'pas' negation, licensed by lane precedent (w2-pas-nelicense: 16/19 'pas' windows lack "ne"). Verb-69 fails ("que [69-V] [88-V]"). **Nominal.**
- @1380 `00(pour) 86 29(er) 89 84(on) 92(N) | 69 | 13(les) 24(V) 65(N)`: right edge "69 les 24" excludes verb-69 (object clitic must precede its verb: "[69-V] les [24-V]" impossible). Nominal-69: "…on [92-N] [69-N], les [24-V] [65]" with "92 69" as a parenthetical ("on, [92] [69], les [24] [65]" = "one Vs them [65]") — or the left edge stays unresolved. **Nominal-leaning; left edge fenced** with stated cause (84='on' unconditioned per A15 re-derivation, 92 = noun solid, the "on + NP" collision has no better licensed parse; class-92 queued).
- @1413 `42 16 97 | 69 | 74 34(i) 52`: "[16] [97] [69-N-subj] [74-V?] i [52]". Verb-69 fails ("[69-V] [74-V]"). **Nominal** (74's class fenced).
- @1627 `33 46(que) 56 | 69 | 26 00(pour) 33 21 64(qui)`: "que [56] [69-N-subj] [26-V] pour [33] [21] qui [37]". **Nominal** — formula attestation 2b.
- @1835 `16 59(est) 36 | 69 | 64(qui) 22 42`: "est [36] [69-N] qui [22-V]" — predicate nominal + relative clause; 'qui' requires a nominal antecedent, so verb-69 is impossible here. **Nominal — strongest leg.** (The brief's "'69 64' pulls both ways" is a misread: it pulls noun, decisively.)

**Class named: 69 = NOUN — 10 of 12 windows nominal (9 solid + @1380 leaning), with exactly one verbal window (@1115, modal infinitive).** The @1115 leg is not fenceable with an innocent cause: "pas [69] la [88-inf]" is a clean modal parse. Per the val-71-quant-nominal precedent (promote, finding-grade), 69 is therefore packaged as a **§7 split candidate** (noun-dominant 10–11/12 vs verbal 1/12) for red-team adjudication. Battery does not declare polyvalence.

## Clause 3 — '26 pour dire' parses under exactly one class: PASS (conditional)

With 69 = noun fixed — true at **all three** formula windows — each attestation parses identically:

- @405: "[69-N-subj] [26-V-fin] pour [33] [01]" — "…[69] [26]s, in order to [33] [01]"
- @933: "[69-N-subj] [26-V-fin] pour [33] [21] qui [37]"
- @1627: "que [56] [69-N-subj] [26-V-fin] pour [33] [21] qui [37]"

**26 = VERB (finite) in all three.** The noun arm for 26 is excluded three independent ways: (i) positional rule R17-020 (HELD under §7): 26 is not in the '11 (02)? 26' article slot at any formula window → verb branch; (ii) 69 is never determiner-shaped (10–11/12 nominal-head windows; followers include finite verbs 88/24 and 'qui'), so "69 [26-noun]" has no licensor; (iii) with 69 occupying the subject slot, 26 must head the predicate — a second noun ("69-N 26-N" compound) is unfounded.

The frame therefore **decides noun-vs-verb via 69's class**, as claimed: 69's nominal class forces the subject slot, which forces 26 = verb. Exactly one class.

**Condition (fenced, red-team territory): 33's word-vs-stem.** "00 33" occurs 8x stream-wide and 33 is NEVER followed by 29 there (0/8); "33 29" occurs 5x and is NEVER preceded by 00. The frames are in complementary distribution. "67 33 29" x3 = "veut croire" (67="veut" iff follower infinitive-shaped; "33"+"29" = "croi"+"er") forces the stem reading at the "33 29" windows, while "pour [33]" without 29 needs 33 word-shaped ("dire"). So 33 is itself a §7 split candidate (stem "croi-" vs word "dire") — for red team, not this battery. **It does not affect 26's class**: "pour [33]" is a purpose clause under either rival ("pour dire" / "pour croire"), and 26 = finite verb stands regardless.

## Adverses answered

- "Formulaic 8-gram weakens independence" → answered: the @933/@1627 8-gram is byte-identical and counted once; @405 is a genuine second attestation (different left edge, different tail). Both parse identically under 69=noun.
- "'69 11' (@1115) pulls both ways" → answered: it pulls **verb** ("pas [69-modal-inf] la [88-inf]"), and is packaged as the §7 split candidate's verbal leg. It does not occur at any formula window.
- "'69 64' pulls both ways" → answered as a misread: @1835 ("est [36] [69-N] qui [22]") is the strongest **nominal** leg — 'qui' needs a nominal antecedent.
- "33's value open" → answered/fenced: the purpose-clause structure holds under both live rivals; 33's word-vs-stem split is complementary-distribution evidence packaged for red team and fenced out of 26's class decision.

## Verdict: PROMOTE (finding-grade, battery-level — red-team ratification required)

1. **Frame finding:** "[69] 26 pour dire" (2 independent attestations, 3 trigram tokens) decides 26 = **VERB** via 69's nominal (subject) class. The noun arm for 26 is dead in this frame (positional rule + no determiner licensor + subject slot occupied).
2. **Class finding:** 69 = **noun** (10–11/12 windows), with @1115 ("pas [69-modal-inf] la [88-inf]") as a live verbal leg → **§7 split candidate** for red team (cf. val-71-quant-nominal precedent).
3. **Packaged for red team:** 33's word-vs-stem split ("00 33" never +29, 0/8; "33 29" never after 00; "veut croire" x3) — conditional only for the "pour dire" gloss, not for 26's class.

No standing verdict contradicted or downgraded. No value promoted for 69 or 33 (class/split findings only). 26's verb class here agrees with R17-020's elsewhere-branch.

## Suggested follow-ups (non-binding; red-team owns the §7 docket)

- `split-69-adjudicate`: red-team venue — 10–11x nominal vs 1x modal-infinitive (@1115); needs the §7 polyvalence/split decision.
- `val-33-word-stem`: discriminate 33 word ("dire") vs stem ("croi-") via the complementary "00 33"/"33 29" distribution; feeds the "pour dire" gloss.
- `leftedge-1380`: resolve "on 92-N 69 les 24" (parenthetical "92 69" vs re-segmentation); dependent on class-92.
