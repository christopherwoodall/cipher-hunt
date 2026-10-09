# Battery verdict: objpron-88-77-11

- Target id: `objpron-88-77-11`
- Claim: "test the object-pronoun rival across the population: are '88 77'/'88 11' verb+clitic-pronoun frames rather than verb+article-NP?"
- Date: 2026-10-09
- Worker: subagent session e40be722 (parent: next-token battery dispatch)
- Lock note: no pre-existing lock in `code/crowd17/next-token/locks/` at start; created `locks/objpron-88-77-11.lock` 2026-10-09T13:19:55Z, deleted on completion.

## Bar (verbatim, pre-registered)

> "the pronoun reading survives at a window iff the post-pronoun material is licensable under 1841 clitic grammar; @730's 'la en' is the sharpest test"

## Numbered clauses (fixed before testing, not modified after)

- **C1 (@86):** the pronoun reading ("88"+"le"-clitic) survives iff the post-pronoun cell 66 is licensable as the clitic's verb host under 1841 clitic grammar.
- **C2 (@646):** the pronoun reading survives iff the post-pronoun cell 78 is licensable as the clitic's verb host.
- **C3 (@1541):** the pronoun reading survives iff the post-pronoun cell 78 is licensable as the clitic's verb host.
- **C4 (@730):** the pronoun reading ("88"+"la"-clitic) survives iff the post-pronoun material "en 85 93" is licensable as a clitic cluster + verb host. Decisive case.
- **C5 (@1514):** the pronoun reading survives iff the post-pronoun material "31 11 91" is licensable under 1841 clitic grammar.

## Method

Read BATTERY-PROTOCOL.md in full before touching anything. Re-derived the 1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` parsed exactly like `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`; 1847 pairs, 96 types verified). `code/side-keyhunt/canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. All @-offsets are 0-based repaired-stream pair indices.

1841 clitic grammar applied (standard, uncontroversial): object clitics (le/la/les, me/te/se/nous/vous, lui/leur, y, en) are proclitic — they immediately precede the verb they complement, in fixed order me/te/se/nous/vous > le/la/les > lui/leur > y > en (e.g. "il le voit", "pour le voir", "je l'en ai informé", "il veut l'en informer"). Post-verbal clitics occur only with affirmative imperatives ("prends-le"). A clitic "le/la" cannot be followed by a noun (that is the article reading, the rival under test).

## Standing values used

Banked/pencil: 11=la (gt), 82=m, 46=que. Provisional: 77=le, 59=est. Granted: 93=verb class (R19-166), 31=VERBAL (R-CC31, confirmed), 85 verb-stem frame (A3), 00=pour (A9), 86 INF-class. Declared: R24 (R19-191) — 24="en" iff follower=85 (five windows: @732/@955/@1438/@1693/@1754); the 24-85 "en [85]" frame is a standing proclitic-host frame (round-15 CONFIRM + Guizot attestation; 24-en-verb-conflict battery: "'en'-pronoun: 'par ce qu'en [85]' — clean gerund"). 78="ver" LEAD (letters) with nominal word usage: R18-011 grants 44@1839 as whole-word nominal head in "[44] de [21] et [78-word]"; the adopted @1541 frame is "Il [93-fin] [88-inf] le [78]" (fin-88-1541-parallel KILL). 66: no standing value (class open — battery-ce-qui-87-subject, battery-adv-20-760-boundary). Battery premises adopted, not re-litigated: governor-88-value PROMOTE (88=verb-class governor), finiteness-88-86 PROMOTE (88 verb/governor at @86), fin88-646-rerun NULL (88 finiteness open at @646), inf88-object-census NULL (population fenced as inconsistent). §7 intact — no polyvalence declared.

## Population census (re-derived, byte-exact)

n(88)=23. "88 77" x3 at @86/@646/@1541; "88 11" x2 at @730/@1514. Matches the parent census exactly.

## Window-level evidence

### @86 (row a1_02): `62 16 14 06 | 88 77 | 66 98 19 41 98`

Post-pronoun cell: 66 (class open, no standing value). For "le" to be a proclitic, 66 must be the verb it complements ("[88] le [66-verb]"). Naming 66 a verb invents a value (§3 of the battery rules — no invention). The grammatical shape exists ("[88-fin] le [66-inf]" = "il veut le voir"-shaped, with 88 finite per finiteness-88-86's verb/governor role), but it is not licensable at battery grade: zero standing supports 66 as a verb. The imperative+enclitic rival ("[88-imp]-le", "prends-le"-shaped) needs 88=imperative (unvalued) plus 66 starting new material (unvalued) — ≥2 ungranted assumptions, over budget.

### @646 (row a4_02): `20 24 87 61 | 88 77 | 78 52 82 94 76`

Post-pronoun cell: 78. 78 is nominal in all its standing uses: R18-011's "[78-word]", the adopted @1541 "le [78]" article+NP frame, 78="ver" LEAD (letters spell "ver" — "le ver", the worm, is a grammatical French NP). 78 has no verb standing anywhere. For proclitic "le", the verb host must be the immediately following cell — 78 — which is nominal. Naming 78 a verb invents a value and contradicts standing nominal usage. The imperative+enclitic rescue ("[88-imp]-le") is over-budget here too (88=imperative unvalued; 78 must start a new clause, unvalued; and 24@643 is finite/modal per R24, making a paratactic imperative marginal in this register). 88's open finiteness (fin88-646-rerun NULL) does not help: even a finite 88 cannot host a following proclitic "le".

### @1541 (row a8_00): `06 21 62 93 | 88 77 | 78 43 00 46 70`

Adopted frame (fin-88-1541-parallel KILL): "Il [93-fin] [88-inf] le [78]". Proclitic "le" needs 78 as its verb — 78 is nominal (see @646 evidence). Dead on the same ground. The rescues are additionally blocked by adopted standings: 88 is infinitive here (finite-88 killed), so "[88-inf] le [78-verb]" would stack two infinitives ("il veut prendre le voir" — ungrammatical); 93 is finite ("Il [93-fin]"), so the imperative+enclitic rescue is impossible (imperatives do not complement finite verbs: *"il veut prends-le"). "le" cannot be the object of 93 either — clitics are strictly pre-verbal and cannot be separated from their verb by 88.

### @730 (row a5_02): `11 00 86 48 | 88 11 | 24 85 93 76 18`

Byte-exact: @730=88, @731=11 ("la", pencil gt), @732=24, @733=85, @734=93. @732 is one of R24's five declared 24-85 windows, so 24="en" by red-team declaration; the standing en85 frame makes "en" a proclitic hosted by 85 (A3 verb-stem). Post-pronoun material: "en [85] [93]".

Clitic-cluster test: "la" (3rd-person DO) + "en" — the order DO-before-"en" is the correct 1841 cluster order ("je l'en ai informé", "il veut l'en informer"). The cluster immediately precedes 85, satisfying proclisis. 85 hosts proclitics per the standing A3/"en [85]" frame (round-15 CONFIRM + Guizot attestation); adding "la" in the pre-"en" slot follows the standard cluster order, so "la en [85]" is structurally parallel to a standing frame. Two sub-readings are both grammatical: (a) 85 as infinitive — "[88-fin] la en [85-inf]" = "il veut l'en informer"-shaped (complement); (b) 85 as gerund — "[88] la en [85-gerund]" = "en l'informant"-shaped (adjunct, "pour réussir en s'appliquant"-shaped). The article rival is dead here (no noun follows "la"; "en" follows — established by the parent census).

Caveats (not killers): "la" needs a feminine discourse antecedent (not resolvable at battery grade — normal for pronouns); surface "la en" would elide to "l'en" in print, but the cipher encodes underlying forms without elision marking (cf. the pencil gloss "la pre m i er e"), so this is orthographic, not structural. The wider clause (88's finiteness — queued fin-88-730-rerun; 93's role) remains open, so the survival is conditional, not a full parse.

### @1514 (row a7_11): `61 59 39 81 | 88 11 | 31 11 91 67 08`

Post-pronoun material: "31 11 91". 31=VERBAL is granted (R-CC31, confirmed) — so "la"(@1515) has a verb host: "[88] la [31-verb]" with "la" proclitic to 31. But 31's direct-object slot is then filled by the clitic, and the trailing "la [91]"(@1516-1517) follows: if "la"[91] is article+NP (91's class open, noun not excluded), 31 carries two direct objects — ungrammatical for a monotransitive verb ("*il la voit la femme" without dislocation). The examined rescues: (i) "la"(@1516) as a second clitic proclitic to 91 — needs 91=verb (invention) and leaves 31's clause boundary unlicensed (French is not pro-drop); (ii) right-dislocation ("il la voit, la femme"-shaped) — grammatical in speech but needs an unvalued prosody/punctuation assumption plus 91=noun, over budget at battery grade; (iii) 31 intransitive — then "la"(@1515) has no verb host at all. All dead or over-budget. Note: the article reading ("la"+31) is equally dead here (31=VERBAL), so @1514's "88 11 31" is currently a residual under both rivals — but only the pronoun rival is this target's scope.

## Per-clause pass/fail

- **C1 (@86): FAIL — fence.** Post-pronoun 66 is unvalued; the pronoun reading is not licensable at battery grade (needs 66=verb, an invented value). Not kill grade: 66's class is open, so the window does not force the reading false.
- **C2 (@646): FAIL — kill grade.** 78 is nominal in all standing uses (R18-011 "[78-word]"; 78="ver" LEAD; adopted @1541 "le [78]"); no verb host exists for proclitic "le". Imperative+enclitic rescue over-budget (≥2 ungranted assumptions).
- **C3 (@1541): FAIL — kill grade.** Same 78-nominal ground as C2, reinforced by the adopted "Il [93-fin] [88-inf] le [78]" frame: 88 infinitive blocks the stacked-verb rescue, 93 finite blocks the imperative rescue, and "le" cannot skip 88 to complement 93.
- **C4 (@730): PASS — conditional.** "la en" is a correctly-ordered clitic cluster immediately preceding 85; 85 hosts proclitics per the standing A3/"en [85]" frame. Both the infinitive-complement and gerund-adjunct sub-readings are grammatical. Survival is conditional on the wider clause (88's finiteness, 93's role — both open).
- **C5 (@1514): FAIL — kill grade.** 31=VERBAL gives "la" a host, but the trailing "la [91]" then forces a double-direct-object violation; all rescues dead or over-budget (dislocation needs unvalued prosody + 91=noun).

## Verdict: NULL (fence executed on the population rival; one conditional leg survives)

Not PROMOTE: the pronoun reading does not survive population-wide (killed at @646/@1541/@1514, fenced at @86). Not KILL: it survives at @730 (C4), so the rival is not globally dead. The uniform verb+clitic-pronoun rival across the "88 77"/"88 11" population is fenced as inconsistent: the only window where the clitic frame is licensable is @730's "la en" cluster, and there only conditionally (88's finiteness and 93's role unresolved). The @1541 reference window — the one place the article+NP frame is battery-grade — rejects the pronoun reading at kill grade, which also closes the uniform-rival route via §7 (78 cannot be verb-at-@646 and noun-at-@1541).

## Follow-ups proposed (all verified ABSENT from battery-queue.json; 2026-10-09)

1. `pron730-clause-wide` (P3) — full-clause parse of @728–@740 under the surviving "la en" cluster reading. Bar: one grammatical full-clause parse with ≤1 ungranted assumption (resolving 88's finiteness and 93's role); else fence the @730 leg. (Does not duplicate queued fin-88-730-rerun, which tests only 88's finiteness.)
2. `val-66-87-verb` (P3) — name 66's class at @87. Bar: verb-66 (infinitive-shaped) revives the @86 pronoun leg as "[88-fin] le [66-inf]" ("il veut le voir"-shaped); non-verb kills it.
3. `pron1514-dislocation-corpus` (P4) — corpus check: does 1841 diplomatic French attest right-dislocated "clitic-DO … la [NP]" ("il la voit, la femme"-shaped) in writing? Bar: ≥1 genuine attestation revives the @1514 pronoun leg via the dislocation rescue; confirmed zero hardens the kill.

## Adverses

- **77='le' provisional:** adopted as premise. The @86/@646/@1541 tests use 77 as "le"; the kills at @646/@1541 rest on 78's nominal standing, not on 'le' being correct — if the red team later rejects 77='le', the pronoun hypothesis does not even start. No conflict with any standing verdict.
- **11=la banked:** adopted (pencil ground truth = the letters l-a). The pronoun reading uses "la" as a clitic pronoun — same letters, different role — so there is no conflict with the banked value. The @730/@1514 tests concern role, not letters.

## Standing state

No standing or red-team verdict contradicted or downgraded (R24/R19-191, R19-166, R-CC31, R18-011, A3/en85 frame, governor-88-value, finiteness-88-86, fin-88-1541-parallel, fin88-646-rerun, inf88-object-census all adopted as premises). §7 intact — no class, split, value, or polyvalence declared. Canonical-stream caveat stands (rows a1_02/a4_02/a5_02/a7_11/a8_00 offsets unvalidated; the pencil gloss is on a5_03).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-objpron-88-77-11.md`
- Queue: `objpron-88-77-11` -> `status: verdict`, `result: null`, 2026-10-09.
- Lock: created on start, deleted on completion.
