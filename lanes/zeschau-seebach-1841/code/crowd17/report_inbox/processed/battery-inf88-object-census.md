# Battery verdict: inf88-object-census

- Target id: `inf88-object-census`
- Claim: "Census the article followers ('88 77' x3 @86/@646/@1541, '88 11' x2 @730/@1514) to test whether the governed infinitive takes a consistent object class; a consistent class narrows the value space at @1541."
- Date: 2026-10-09
- Worker: subagent session 3d2ded24 (parent: next-token battery dispatch)
- Lock note: no pre-existing lock in `code/crowd17/next-token/locks/` at start; created `locks/inf88-object-census.lock` 2026-10-09T12:37:02Z, deleted on completion.

## Bar (verbatim, pre-registered)

> "Consistent object class confirmed at battery grade, or fenced as inconsistent."

## Numbered clauses (fixed before testing, not modified after)

- **C1:** The article-follower population ("88 77" x3 @86/@646/@1541, "88 11" x2 @730/@1514) shows a consistent object class at battery grade -> promote.
- **C2 (else-arm):** Else, the population is fenced as inconsistent, with stated cause -> null.

## Method

Read BATTERY-PROTOCOL.md in full before touching anything. Re-derived the 1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` parsed exactly like `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`; 1847 pairs, 96 types verified). `code/side-keyhunt/canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. All @-offsets are 0-based repaired-stream pair indices. Standing values used: banked 11=la (pencil gt); provisional 77=le; A9 86 INF-class; R24 (R19-191: 24='en' iff follower=85, the 5 windows); battery premises adopted, not re-litigated: governor-88-value PROMOTE (2026-10-08: 88=verb-class, verb stem/governor, class-level; preposition rival rejected), finiteness-88-86 PROMOTE (2026-10-09: @86 parses with 88 in verb/governor role, "88 le 66" transitive frame under 77='le' provisional), fin-88-1541-parallel KILL (adopted frame "Il [93-fin] [88-inf] le [78]"), fin88-646-rerun NULL (88 finiteness at @646 unresolved).

## Census (re-derived, byte-exact)

- n(88)=23. Successor census top: 77 x3, 11 x2, 24 x2, then 16 singles.
- "88 77" x3 at @86/@646/@1541 (matches the brief exactly).
- "88 11" x2 at @730/@1514 (matches the brief exactly).

## Window-level evidence

### @86 (row a1_02): `62 16 14 06 | 88 77 | 66`

finiteness-88-86 PROMOTE (adopted): 88 in verb/governor role; the "88 le 66" transitive frame parses under 77='le' (provisional). 66's role at @87 is unconfirmed. This is the one "88 77" window NOT followed by 78 (per that report's byte-exact census). 88's finiteness here is verb-class/governor, not established as infinitive.

### @646 (row a4_02): `20 24 87 61 | 88 77 | 78`

Trigram "88 77 78" byte-identical to @1541. 77->78 is 77's top successor collocation stream-wide ("le"+noun, 77='le' provisional). But 88's finiteness at @646 is unresolved (fin88-646-rerun NULL; the @1541 parallel leg is dead). Surface-consistent with @1541, not battery-grade.

### @1541 (row a8_00): `06 21 62 93 | 88 77 | 78`

Adopted frame (fin-88-1541-parallel KILL): "Il [93-fin] [88-inf] le [78]". This is the reference instance: battery-grade [88-infinitive] + [le + noun-78]. The only window in the population where the governed-infinitive + article-noun object frame is confirmed.

### @730 (row a5_02): `11 00 86 48 | 88 11 | 24 85 93`

Byte-exact: @730=88, @731=11, @732=24, @733=85. 11='la' is pencil ground truth. @732 is one of R24's five declared 24-85 windows ([732, 955, 1438, 1693, 1754]), so 24='en' here by red-team declaration (R19-191, §7 exception). Therefore "la" at @731 is followed by the clitic 'en', not a noun: the [88-inf] + [la + noun] object frame does NOT obtain at this window. Under infinitive-88, the object-class shape breaks here; 88's finiteness at @730 is open, so kill grade is not reached, but this window cannot be counted toward consistency.

### @1514 (row a7_11): `61 59 39 81 | 88 11 | 31 11 91`

"88 11 31": 11='la' (pencil gt); 31 unvalued; 88's finiteness open. "la [31]" is an object-NP candidate only if 31 is a noun — unconfirmed. The object-pronoun rival ("[88] la" = verb + feminine clitic) is unexcluded.

## Per-clause pass/fail

- **C1 FAIL:** A consistent object class is not confirmed at battery grade. Only @1541 is battery-grade [governed-infinitive] + [article + noun]. @86 is battery-grade verb+object but 88 is governor-class there (not established as infinitive) with 66 unconfirmed. @646 is surface-identical to @1541 but 88's finiteness is open. @730 breaks the [art+noun] shape under R24 ('en' follows 'la', no noun). @1514 needs 31's class.
- **C2 FIRES:** The population is fenced as inconsistent at battery grade. Stated cause: (1) the governed-infinitive + article-noun frame is confirmed only at @1541; (2) @730's "88 11 24" is byte-incompatible with [art+noun] under red-team law (24='en' at @732 per R24; 11='la' pencil gt; no noun follows); (3) @646/@1514/@86 cannot close the gap at battery grade (88's finiteness open at @646/@730/@1514; 66's role open at @87; 31's class open at @1515).

## Verdict: NULL (fence executed)

Not PROMOTE: C1 fails — consistency is not confirmed at battery grade.
Not KILL: no window forces the claim false at kill grade — 88's finiteness is open at the shape-breaking windows (@730/@1514), so the inconsistency cannot be forced onto a governed-infinitive reading.

## Follow-ups proposed (for supervisor queuing)

1. `fin-88-730-rerun` (P3) — decide 88's finiteness at @730. Bar: if 88=inf, the "la [24='en']" sequence (R24, red-team law) hardens the population inconsistency; if 88=finite, re-test "la" as object pronoun under 1841 clitic-order grammar ("[88-fin] la en" needs licensing).
2. `val-31-1515-noun` (P3) — name 31's class at @1515. Bar: noun-31 makes "la [31]" a battery-grade [art+noun] object at @1514; non-noun kills the object reading there.
3. `objpron-88-77-11` (P3) — test the object-pronoun rival across the population: are "88 77"/"88 11" verb+clitic-pronoun frames rather than verb+article-NP? Bar: the pronoun reading survives at a window iff the post-pronoun material is licensable under 1841 clitic grammar; @730's "la en" is the sharpest test.

## Adverses

None listed on the queue target.

## Standing state

No standing/red-team verdict contradicted or downgraded (R24/R19-191, governor-88-value, finiteness-88-86, fin-88-1541-parallel, fin88-646-rerun all adopted as premises). §7 intact — no polyvalence declared. Canonical-stream caveat stands (rows a1_02/a4_02/a5_02/a7_11/a8_00 offsets unvalidated; the pencil gloss is on a5_03).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-inf88-object-census.md`
- Queue: `inf88-object-census` -> `status: verdict`, `result: null`, 2026-10-09.
- Lock: created on start, deleted on completion.
