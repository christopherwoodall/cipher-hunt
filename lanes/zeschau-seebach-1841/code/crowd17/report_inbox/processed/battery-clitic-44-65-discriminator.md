# Battery verdict: clitic-44-65-discriminator

- Target: `clitic-44-65-discriminator`
- Claim: discriminate 'en' vs 'l'' at @1714 via 65's contact profile
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched. All @-offsets 0-indexed, re-derived in-work.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff 65's contact profile favors one reading — a 'de'-complement source or partitive frame supporting 'n'en est pas', or a copular/subject frame supporting 'ne l'est pas' — with the other reading fenced; else record @1714 as permanently undiscriminated and fence the clitic"

Numbered clauses (frozen before testing):
- **C1:** 65's contact profile contains a frame favoring one reading: (a) a 'de'-complement source or partitive frame → favors 'en' ("n'en est pas"); or (b) a copular/subject frame → favors 'l'' ("ne l'est pas").
- **C2:** The non-favored reading is fenced with a stated cause.
- **Fallback:** If neither C1 nor C2 fires, record @1714 as permanently undiscriminated and fence the clitic forcing as value-open window-local.

Listed adverses: "65's value open — do not name it; do not re-litigate 94/59/30."

Note on adverses vs new standing data: since this target was queued, prof-65 PROMOTED 65=noun-class (battery-level, 6 frame-legs). The adverse's "value open" is therefore superseded at class level: this battery uses 65's CLASS (noun) and its contact profile, and names no VALUE for 65. 94='ne', 59='est', 30='pas' are used as given, never re-litigated.

## Method

Re-parsed the repaired stream in-work (1,847 pairs, 96 distinct groups; n(65)=25 confirmed). Built 65's full preceder/follower census and scanned all 25 windows for (i) de-complement frames, (ii) partitive/quantifier frames, (iii) copular/subject frames. Scanned the ~70-token left discourse of the forcing window (@1640–1711) for de-phrases, partitive quantifiers, and predicative antecedents. Checked the lane table-registry for any group valued "de". Read battery-pronoun-44-1714.md (processed/) and battery-prof-65.md; no standing verdict re-litigated.

The forcing window @1712 (row a8_06), 0-indexed: `26 12 06 29 40 65 94 44 59 30 64 47 68`
— i.e. `…[26] n'entere [65] ne [44] est pas qui ce/se [68]…` with 12=n (banked), 06='ent' (battery lead), 94='ne' (promoted), 59='est' (provisional), 30='pas' (promoted), 64='qui' (granted), 47='ce' (granted, allophone tier admits 'se').

## 65's contact profile (25 windows, re-derived)

Preceders: 21 x4, 40 x3, 91/74/24/08/06 x2, 94/60/98/78/41/64/92/79 x1.
Followers: 63 x4, 23/13/64 x3, 94 x2, 16/88/84/14/71/38/46/68/48/34 x1.
`65 94` x2: @687 (`29 40 65 94 29`), @1712 (`29 40 65 94 44`) — both share left trigram `29 40 65` ("[X]ere 65").

Frames relevant to the discrimination (from prof-65, verified against bytes in-work):
- **F-subject-copular:** @1208 `21 65 64 59 32` — "21 65 qui est 32": 65 heads a qui-relative (64=qui granted) whose verb is "est" (59 provisional, used per adverse allowance). 65 is attested as **subject of a copular clause**. Corroborated as qui-relative subject head @724 (`91 65 64 11 00`) and @1340 (`08 65 64 52 38`).
- **F-object:** @812 (`12 48 24 65`), @1383 (`13 24 65 68`) — 65 as direct object of finite verbs.
- **F-post-ere:** @293, @687, @1712 — `29 40 65` ("[X]ere 65").
- **F-quantifier:** @1683 `79 65 13` ("tout 65", 79=tout granted — universal, not partitive); 17=fois occurs at distance 3 in @455 (`79 17 77 60 65`), never adjacent to 65.
- **Copular adjacency:** 59 is NEVER adjacent to 65 in 25 windows; within ±3 only at @1208 (above) and @1712 (the forcing window itself). No "est 65" (predicate-nominal) window exists.

## Arm 1 — 'en' ("n'en est pas"): de-complement source or partitive frame

**Result: ABSENT — three independent absences.**

1. **No de-complement source.** No group in `code/table-grid/table-registry.json` carries value "de" (registry grep: zero hits). None of 65's 25 windows shows an X-de-65 or 65-de-X frame; no de-shaped bigram neighbors 65 in the preceder/follower census above.
2. **No partitive frame.** 65's adjacent quantifiers are "tout" (universal, @1683) and "fois" only at distance 3 (@455); no numerals, no "pas de", no partitive de-phrase anywhere in 65's 25 windows. The ~70-token left discourse @1640–1711 likewise contains no de-phrase and no partitive quantifier (nearest: "que tout 65" @1679–1681, universal).
3. **Selectional/idiomatic.** The productive 1841 "n'en est pas" constructions — "il n'en est pas question", "il n'en est rien", "il n'en est pas de même" — take impersonal subjects. A lexical-noun subject (65, noun-class promoted) with partitive 'en' and no partitive/de antecedent is unlicensed in 1841 diplomatic French.

'en' is therefore **FENCED** (not killed — a de-source could in principle surface elsewhere; fence = set aside with stated cause, per the three causes above).

## Arm 2 — 'l'' ("ne l'est pas"): copular/subject frame

**Result: PRESENT.**

- @1208 `21 65 64 59 32` ("21 65 qui est 32"): 65 is the subject of copular "est" — exactly the frame the bar names. 65 is the kind of noun that occupies the subject slot of a copular predication, which is what "65 ne l'est pas" requires (l' = predicative anaphor, "is not it/so").
- At @1712, "65 ne [44] est pas" places 65 in the subject-of-negated-copula slot; 'l'' (elided le/la) supplies the predicative anaphor — a routine 1841 construction.
- Consonant (non-discriminating, recorded): 44's weak masculine-gender promotion leans 'le'→'l''; noted, not relied upon.
- **Caveat, fenced:** l''s predicative antecedent is NOT identified in 65's profile or the @1640–1711 discourse — recorded as discourse-anaphoric, unresolved. The bar does not require the antecedent, only the frame; the gap is fenced, not hidden (see live-end follow-up below).

## Adverses (answered, none ignored)

- "65's value open — do not name it": HONORED as modified by standing data. No value named for 65; only its promoted noun-class and distributional frames used. (The adverse predates the prof-65 promote; the class-level use is the minimal update the new standing data requires.)
- "do not re-litigate 94/59/30": HONORED. 94='ne', 59='est', 30='pas' used as given throughout.
- Observation fenced out-of-scope per adverse: @687's `65 94 29` ("…65 ne er…") is ungrammatical under 94='ne'-negator + 29='er'-syllable, hinting at the lane-wide 12/94 duality at that window — NOT pursued here (adverse); at @1712 the `94…30` ("ne…pas") bracketing secures 94='ne' independently.

## Per-clause pass/fail

- **C1:** PASS for 'l'' — copular/subject frame present in 65's contact profile (@1208 "65 qui est 32", corroborated @724/@1340). The 'en'-favoring frame (de-complement/partitive) is absent on three independent checks.
- **C2:** PASS — 'en' fenced with three stated causes (no de-source lane-wide or in-profile; no partitive frame in 25 windows or left discourse; impersonal-subject idiom mismatch).
- **Fallback:** not reached.

## Verdict: PROMOTE

@1714 discriminates to **"ne l'est pas" — 44='l'' (elided le/la), window-local**. 'en' is fenced per C2. Scope discipline, inherited from battery-pronoun-44-1714: neither value survives the four global frames ('77 44' x2, '47 44 59', '44 00' x3 — all fail under 'l'' too), so **44='l'' does NOT generalize beyond @1714**; it is a window-local value assignment. No standing verdict contradicted or downgraded: consistent with the pronoun-44-1714 null residual (value ∈ {'en','l''} now resolved to 'l'' at this window), with 44's masculine-gender promotion, and with the noun-44 kill. §7 sole-polyvalence law untouched (one window-local value, no second value declared for 44 anywhere). No red-team verdict on 44's value exists to contradict (red-team resolution of 44 still pending per lane state).

## Live-end follow-up (verdict is promote; not a required null follow-up)

1. **antecedent-44-l-prime** (priority 3): locate l''s predicative antecedent. Evidence: @1714 "65 ne l'est pas" needs a predicative adjective/noun antecedent; none identified in @1640–1711. Bars: "resolve iff a predicative adjective or noun antecedent for l' is identified within the @1712 clause or the @1640–1711 discourse with byte offsets, else fence l' as discourse-anaphoric (antecedent outside the scanned window)." Adverses: do not re-litigate 94/59/30; 65's value stays unnamed.

## Provenance

Every number re-derived from the repaired 1,847-pair stream in-work: n(65)=25; preceder/follower census as tabulated; `65 94` x2 (@687, @1712); `29 40 65` x3 (@293, @687, @1712); 59 never adjacent to 65; registry "de" grep zero hits. No invented data. Lock `locks/clitic-44-65-discriminator.lock` created on start with UTC timestamp, deleted on completion.
