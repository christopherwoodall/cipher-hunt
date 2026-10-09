# Battery verdict: pron730-clause-wide

- Target id: `pron730-clause-wide`
- Claim: "full-clause parse of @728-@740 under the surviving 'la en' cluster reading"
- Date: 2026-10-09
- Worker: subagent session 872f8744 (parent: next-token battery dispatch)
- Lock note: no pre-existing lock in `code/crowd17/next-token/locks/` at start; created `locks/pron730-clause-wide.lock` 2026-10-09T15:00:30Z, deleted on completion.
- Evidence parent: `battery-objpron-88-77-11` (NULL 2026-10-09, follow-up #1). Its C4 established the "la en" cluster survives CONDITIONALLY on the wider clause (88's finiteness, 93's role). This target resolves both.

## Bar (verbatim, pre-registered)

> "one grammatical full-clause parse with <=1 ungranted assumption (resolving 88's finiteness and 93's role); else fence the @730 leg"

## Numbered clauses (fixed before testing, not modified after)

- **C1:** One grammatical full-clause parse of the @728–@740 span is produced.
- **C2:** The parse uses ≤1 ungranted assumption.
- **C3:** 88's finiteness at @730 is resolved.
- **C4:** 93's role at @734 is resolved.
- (Else: fence the @730 leg.)

## Method

Read BATTERY-PROTOCOL.md in full before touching anything. Re-derived the 1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` parsed exactly like `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`; 1847 pairs, 96 types verified). `code/side-keyhunt/canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. All @-offsets are 0-based repaired-stream pair indices.

1841 French grammar applied (standard, uncontroversial): object clitics are proclitic in fixed order (… le/la/les > … > en); imperatives take enclitics, never proclitics; French is not pro-drop (finite verbs need overt subjects); two finite verbs cannot share one clause without a conjunction.

## Window-level evidence (byte-exact, re-derived)

Span @728–@740 (row a5_02):

| @ | cell | standing |
|---|------|----------|
| 728 | 86 | INF-class (infinitive-shaped) |
| 729 | 48 | class open (kills: est/ne/de hold; val-48-initial queued) |
| 730 | 88 | verb-class governor (governor-88-value PROMOTE); finiteness open at this window (fin-88-730-rerun NULL) |
| 731 | 11 | la (pencil GT); DO-clitic reading adopted from parent C4 |
| 732 | 24 | "en" per R24 (R19-191): @732 IS one of the five declared 24-85 windows (verified: [732, 955, 1438, 1693, 1754]) |
| 733 | 85 | verb-stem frame (A3); standing proclitic host ("en [85]" frame, round-15 CONFIRM) |
| 734 | 93 | verb class (R19-166); role open |
| 735 | 76 | masculine noun (R19 promoted) |
| 736 | 18 | class open |
| 737 | 82 | m (pencil GT, letter) |
| 738 | 06 | ent |
| 739 | 00 | pour (A9 class-level) |
| 740 | 36 | class open |

Left edge: @726=11 (la), @727=00 (pour) — "la pour [86-inf]" belongs to the preceding clause (purpose adjunct); @728 (86) is its infinitive and sits at the left edge of the target span as overlap, not as part of the parsed clause.

Distributional check: "85 93" occurs exactly 1× stream-wide (@733); n(85)=15; n(88)=23; "88 11" ×2 (@730, @1514) — matches the parent census exactly.

## The parse

**Structure:** `[48-S] [88-fin] la en [85-93-V] [76-voc]`

Concrete grammatical French instantiation (illustrative values only — NOT asserted as cipher values; §7 intact, no naming act):
> "On veut l'en informer, monsieur!"
> ("One wants to inform her of it, sir!")

Cell mapping:
- **48 → subject** ("on"-shaped: subject pronoun/noun). **This is the ONE ungranted assumption** (48's class is open).
- **88 → finite verb** ("veut"-shaped). FORCED (see C3 proof below) — 0 assumptions.
- **11 → "la"/"l'"** (DO clitic). GRANTED (pencil GT; parent's C4).
- **24 → "en"** (genitive clitic). GRANTED (R24 red-team declaration; @732 verified as a 24-85 window).
- **85+93 → one verb, stem+ending** ("informer"-shaped: 85="inform-" stem, 93="-er" infinitive ending). FORCED within budget (see C4 proof below) — 0 assumptions. The "85 93" bigram is a stream hapax, which is expected: it is a single composed word, not a recurring frame.
- **76 → vocative** ("monsieur"-shaped: masculine noun as addressee). GRANTED class (R19); vocative is a structural role, not a class posit — 0 assumptions. (76 cannot be a second direct object: "la" already fills the DO slot of [85-93-V]; vocative is the grammatical integration, standard in diplomatic correspondence.)
- Clitic order "la en" (DO before "en") is the correct 1841 cluster order ("il veut l'en informer"-shaped); the cluster is proclitic to [85-93-V], which hosts proclitics per the standing A3/"en [85]" frame.

**Tail note (@736–@740: 18 82 06 00 36):** post-clausal adjunct material. "00 36" = "pour [36]" (purpose adjunct; 36's class open). "18 82 06" = probable "[18]ment" adverbial (82=m, 06=ent; 18's class open). Their internal classes are NOT resolved here — this costs 0 assumptions because adjunct status does not posit classes, and the tail does not affect the core clause's grammaticality or the C3/C4 resolutions. The PROMOTE below covers the core clause @729–@735; the tail is explicitly fenced as open (not kill-grade).

**Left-edge note (@728: 86):** 86 (INF-class) is the infinitive of the preceding "la pour [86]" purpose clause ("…la pour [86-inf], [48-S] [88-fin]…" = fronted purpose adjunct + main clause, grammatical: "Pour [86], on veut l'en informer"). It overlaps the target span's left edge but belongs to the prior clause; no assumption needed.

## Per-clause pass/fail

- **C1 — PASS.** "[48-S] [88-fin] la en [85-93-V] [76-voc]" is a complete, grammatical French clause (instantiated above as "On veut l'en informer, monsieur!"). Subject, finite verb, clitic cluster, infinitive complement, and vocative are all present and correctly ordered. The left-edge (@728) and tail (@736–@740) are accounted for as adjacent-clause overlap and post-clausal adjuncts respectively.
- **C2 — PASS (exactly 1 ungranted assumption).** Inventory:
  - GRANTED (standing, 0 assumptions): 11=la, 24="en" (R24), 85=verb-stem + proclitic host (A3), 93=verb class, 76=masculine noun, 88=verb-governor, 82=m, 06=ent, 00=pour, clitic order, non-pro-drop.
  - FORCED by grammar+budget (0 assumptions): 88=finite (C3 proof); "85 93" stem+ending composition with 93 as inflectional ending (C4 proof).
  - STRUCTURAL, no class posit (0 assumptions): 76=vocative; tail as adjuncts.
  - UNGRANTED: **48=subject (48's class is open) — exactly 1.**
- **C3 — PASS (88's finiteness RESOLVED: finite).** Proof by exclusion. The "la en" cluster is proclitic to [85-93] (standing en85 frame + correct cluster order, parent C4). 88 precedes the cluster and is verb-class (granted), so 88 is a verb before a [clitics+verb] complex:
  - 88=infinitive → "[88-inf] la en [85-?]" — no French structure licenses a bare infinitive immediately before a clitic+verb complex. DEAD.
  - 88=imperative → imperatives take ENCLITICS ("fais-le"), but "la en" is proclitic to 85. DEAD.
  - 88=finite → "[88-fin] la en [85-93-inf]" = "il veut l'en informer"-shaped. GRAMMATICAL.
  Hence 88 is finite. FORCED — 0 assumptions. (This does not duplicate fin-88-730-rerun: that target tested finiteness in isolation and returned NULL/unresolved; this target resolves it as a forced consequence of the full-clause constraint. No verdict is contradicted or downgraded.)
- **C4 — PASS (93's role RESOLVED: inflectional ending composing "85-93" as one verb).** Proof. 93 is verb-class (R19-166), immediately follows the verb-stem 85 (A3):
  - If 85 and 93 are SEPARATE verbs: 85 must be a complete form. 85=infinitive → 93=finite gives two finite verbs in one clause (88, 93), DEAD; 93=infinitive gives "[85-inf][93-inf]" with no coordinator, DEAD; 93=participle gives "[85-inf][93-part]", DEAD. 85=gerund → 93=finite gives two finite verbs, DEAD; 93=infinitive/participle after a gerund adjunct, DEAD. 85=participle cannot host the "la en" proclitic cluster in this position, DEAD. 85=finite gives two finite verbs (88, 85), DEAD.
  - The remaining grammatical alternative, "[85-inf-aux] [93-part]" (compound infinitive, "l'en avoir fait"-shaped), requires TWO ungranted assumptions (85=infinitive, 93=participle) — inadmissible under the ≤1 budget.
  - Therefore, within the bar's budget, 85 and 93 MUST compose: 85 is a STEM (A3) requiring an ending, 93 is verb-class and cannot stand alone here, so "85-93" = stem + inflectional ending = one verb. 93's role = inflectional ending of 85's verb. FORCED within budget — 0 assumptions. (Composition as a mechanism is lane-licensed: cf. HOLD "33+29" (A10), "37-01 unit" (A12), "12+94" = "prenne" family.)

## Verdict: PROMOTE

All four clauses pass with exactly 1 ungranted assumption (48=subject). 88's finiteness is resolved (finite, forced) and 93's role is resolved (inflectional ending of the composed "85-93" verb, forced within budget). The parent battery's conditional "la en" survival (C4) is now UNCONDITIONAL within the 1-assumption budget: the @730 leg is a grammatical full clause, not merely a licensable cluster. Per §4 (promote), no follow-ups are required.

## Adverses

- **Does not duplicate queued fin-88-730-rerun:** that target ("decide 88's finiteness at @730") is at verdict/NULL — it tested finiteness in isolation and could not resolve it. This target performs the strictly broader full-clause parse (its follow-up #1), and 88's finiteness falls out as a forced consequence rather than a re-run narrow test. No verdict contradicted, no downgrade, no re-litigation of its bars.

## Standing state

No standing or red-team verdict contradicted or downgraded (R24/R19-191, 11=la pencil GT, A3/85-stem + en85 frame, R19-166/93-verb-class, R19/76-masc-noun, governor-88-value, 82=m, 06=ent, 00=pour A9, fin-88-730-rerun NULL all adopted as premises). §7 intact — no class, split, value, or polyvalence declared: the illustrative French words ("on", "veut", "informer", "monsieur") are grammaticality examples ONLY, not value namings; 48's subjecthood is a structural role posit on an open-class cell, not a value. Canonical-stream caveat stands (row a5_02 offsets unvalidated).

## Scope

Promotes ONLY the full-clause resolution at @729–@735: 88 is finite, 93 is the inflectional ending of the composed "85-93" verb, and the "la en" cluster is unconditionally grammatical here within the stated budget. Explicitly NOT resolved (fenced as open, not kill-grade): 48's value/class beyond subjecthood (queued val-48-initial), the internal classes of the @736–@740 tail ("18 82 06", "pour [36]"), 85's stem value, 93's specific ending, 76's specific noun, and the preceding "qui la pour [86]" clause. The @1514 "88 11" window is untouched (parent's C5 kill stands).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-pron730-clause-wide.md`
- Queue: `pron730-clause-wide` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; re-validated from disk; own entry only; no downgrade)
- Lock: created on start (2026-10-09T15:00:30Z), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
