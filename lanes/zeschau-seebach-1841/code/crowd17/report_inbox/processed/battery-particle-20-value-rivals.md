# Battery report: particle-20-value-rivals — **NULL** (no left-context frame separates 'mais' from its rivals at both windows)

**Target:** `particle-20-value-rivals` (P3)
**Date:** 2026-10-09 (UTC)
**Worker:** a3860f45-d59d-4ed2-be54-e5ddef81501d
**Lock:** `code/crowd17/next-token/locks/particle-20-value-rivals.lock` created on start (agent id + UTC 2026-10-09T14:38:11Z); no stale lock present.

## Bar (verbatim from queue)

"resolve iff a discriminating frame separates 'mais' from its rivals at both windows; feeds poly-20-docket"

## Bar restated as numbered clauses (fixed before testing)

- (c1) A left-context frame tested against 1841 French separates 'mais' from 'or'/'donc'/'cependant' at @760 (0-based; left context `40 67 | 11 70 82 34 29 40 = "la première"` then `20 62=il 94=ne`). PASS iff the frame is attested for 'mais' and excluded for all three rivals at battery grade.
- (c2) A left-context frame tested against 1841 French separates 'mais' from 'or'/'donc'/'cependant' at @839 (0-based; left context `… 17=fois 98 |` then `20 62=il 94=ne`). PASS iff the frame is attested for 'mais' and excluded for all three rivals at battery grade.
- (c3) Decision rule (pre-registered): resolve iff (c1) AND (c2) PASS → verdict promote (narrowing recorded for `poly-20-docket`). If either fails → NULL with follow-ups. A window forcing the parent's 'mais' naming false would be KILL (not observed).

## Method

Read BATTERY-PROTOCOL.md in full first. Stream facts re-derived in-session from the repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never touched. R5005, sealed gate instances, red-team adjudication queue untouched.

Corpus: the lane's 1841 French corpus (`code/side-period/corpus`), two cuts: diplomatic subset (9 files: levant-correspondence-1841-p3, metternich-papiere-v4/v6, pozzo-di-borgo-correspondance-v1, talleyrand-memoires-v1, guizot-memoires-t1/t2/t3/t5-t6) and full French (59 files, German allgemeine-zeitung and PROVENANCE excluded). Clause-initial particle = clause (split on `[.;:!?…]` and paragraph breaks only — single newlines are OCR line-wraps, not boundaries) whose first word is Mais/Or/Donc/Cependant.

Three left-context frames tested:
- **F1 fragment-follow:** preceding clause contains no finite verb form. Finite set = 4,250 generated+hand-listed forms (`code/crowd17/next-token/finite_forms.py`: regular -er/-ir/-re conjugations for ~150 common infinitives + full irregular paradigms); apostrophe elisions split (`c'est` → `c`,`est`). Every fragment-classified hit for or/cependant/donc in the diplomatic cut, plus the full-French or/donc samples, hand-audited; false-positive sources (drama speaker names, page numbers, OCR garbage, infinitive phrases, missed verbs) identified per hit.
- **F2 ordinal-ellipsis-final (@760 exact frame):** preceding clause ends with a nominalized ordinal (`la/le/les première(s)/premier(s)/seconde…`), head noun elided — byte-analogous to `…et la première | [20]`.
- **F3 fois-final (@839 frame):** preceding clause has `fois` in its last 2 word positions — byte-analogous to `…fois [98] | [20]`.

Scripts: `code/crowd17/next-token/particle20_rivals_census.py`, `finite_forms.py`; outputs `particle20_rivals_census.json`, `particle20_verbless3_{diplomatic,full_french}.json`.

## Window-level evidence (byte-exact, 0-based)

- `20 62 94` trigram occurs exactly ×3 stream-wide: @760, @839, @1703. (@1703 is the verbal face, fenced by parent.)
- @760 (row a5_03): `… 40 67 | 11 70 82 34 29 40 | 20 62 94 59 39 88 …` = `…[e] [67] | la première | [20] il ne est …`. Under the exceptionless 67 positional rule (R19: 67="veut" iff follower infinitive-shaped; follower here is 11="la") 67="et", so the immediate left constituent is the elliptical NP `et la première`. Whether the fuller left clause (`00 64 02 97 40` = `pour qui [02] [97] [e]`) is a fragment depends on unvalued 02/97 — **cannot be asserted at battery grade** (stated caveat).
- @839 (row a5_06): `… 17=fois 98 | 20 62 94 26 12 16 00 33 96 …` = `…fois [98]. [20] il ne …`. Left clause contains 59="est" (provisional) — a full clause.

## Corpus results

**F1 fragment-follow — all four particles occur after genuine verbless fragments:**
- mais: ubiquitous (11.9% diplomatic / 25.4% full French of clause-initial uses; drama dialogue inflates the full-French rate).
- or: genuine hits — `Vive le roi. Or, voici quel était en ce moment le véritable état de la France` (revue-deux-mondes-1841-q3); `en un mot, le dogme de la liberté morale opposé au fatalisme. Or, en ceci, l'histoire positive sera…` (q1). (Diplomatic-cut hits were false positives: infinitive phrases, missed verbs, OCR garbage — none genuine there, but the construction is licensed in 1841 French.)
- cependant: genuine hits — `Vive le Roi! Cependant MM…` (guizot-memoires-t1); `Le 12, même nuit, même inquiétude dans ce quartier. Cependant les barricades sont presque abandonnées` (guizot-memoires-t3).
- donc: genuine hits — `En toute étude, les faits d'abord, et les formules beaucoup plus tard. Donc, le principe de la science moderne… a pris racine…` (revue-deux-mondes-1841-q1); `Moi, l'avenir. donc le présent nous gêne` (raw-thtredecasim03dela). **This kills the grammatical shortcut**: 'donc' does follow fragments when the fragment carries propositional content, so no a-priori exclusion of 'donc' at @760.

**F2 ordinal-ellipsis-final (full French): mais=5, or=0, donc=0, cependant=0.** The five mais hits are exact-frame analogues, e.g. `…ruse à jeter par-dessus la première. Mais voici bien autre chose` (revue-deux-mondes-1841-q1); `J'en conviens le premier. mais c'est une faiblesse,` (raw-thtredecasim01dela). Suggestive but **n=5 is underpowered** (P(all-mais | null) ≈ 0.48) — not battery-grade separation.

**F3 fois-final (full French): mais=10, or=2, cependant=1, donc=0.** 'Donc' absent but expected count ≈ 0.3 at its base rate — underpowered, no exclusion. Mais/or/cependant all live.

## Per-clause pass/fail

- **(c1) FAIL.** No battery-grade frame separates 'mais' from all three rivals at @760: the exact-frame census (5-0-0-0) is underpowered, and the fragment frame is shared by all four particles (genuine attestations for each). The 'donc'-needs-premise grammatical argument fails empirically (fragments with propositional content license 'donc').
- **(c2) FAIL.** The fois-final frame attests mais, or, and cependant; 'donc' is absent but underpowered. No separation.
- **(c3) does not fire.** The parent's 'mais' naming stands unrefuted; nothing here forces it false (no KILL).

## Verdict: **NULL** — rivals undiscriminated at battery grade; 'mais' remains the routed candidate for `poly-20-docket`

**Headline:** left-context particle requirements do not separate 'mais' from 'or'/'donc'/'cependant' at either window. At @760 the exact ordinal-ellipsis frame favors 'mais' 5-0-0-0 but is underpowered; at @839 mais/or/cependant are all live. The most promising exclusion route ('donc' after fragments) died on genuine counterexamples. No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands.

## Follow-ups proposed (null regenerates work; all verified ABSENT from queue)

1. `or-fragment-license` (P3) — Targeted corpus test: is 'or' after verbless/exclamative fragments licensed in DIPLOMATIC prose specifically (current genuine hits are revue/nesselrode, not diplomatic)? Bar: ≥3 genuine diplomatic attestations licenses 'or' at @760's fragment reading; confirmed zero across the diplomatic cut narrows the rival set. (Does not decide 'mais'.)
2. `ordinal-particle-boost` (P3) — Expand the F2 ordinal-ellipsis-final census (spelling variants, `premier(s)`, `seconds`, larger 19th-c corpus) to power the 5-0-0-0 observation. Bar: separation declared iff 'mais' stays exclusive at n≥20 with rivals at zero; else the frame is abandoned as a discriminator.
3. `donc-839-premise` (P4, gated) — Gate: name 98's class first. Then test whether the @839 left clause (`…est [35] [56] fois [98]`) can serve as a 'donc' premise given 98's value; if the clause is non-propositional under the named 98, 'donc' drops at @839. (Battery gathers only until 98 resolves.)

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-particle-20-value-rivals.md` (this file)
- Queue: `particle-20-value-rivals` → status `verdict`, result `null`, report path above, date 2026-10-09 (temp-file + atomic rename; only this entry touched; JSON re-validated after write)
- Lock created on start, deleted on completion. `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched.
