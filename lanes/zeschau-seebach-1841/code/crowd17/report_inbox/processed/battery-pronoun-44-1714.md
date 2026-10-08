# Battery report: pronoun-44-1714 — "test the clitic reading forced at @1714: 44 = 'en' or 'l'-shaped"

- Worker: battery-worker pronoun-44-1714, agent 53a5bd13-41f0-49f3-9ab5-322d0b4b2cc7
- Date: 2026-10-08 (lock created 2026-10-08T20:54:46Z)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per repair_parse.py). canonical.py NOT used. R5005 untouched. All @-offsets are repaired-stream indices, re-derived in-work.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff one clitic value parses at @1714 AND survives the four global frames ('le 44' x2, 'ce 44 est', '44 pour' x3) or is fenced as window-local; else record the clitic forcing as the standing residual"

Numbered clauses (frozen before testing):
1. One clitic value ('en' or 'l''-shaped) parses at @1714 ('65 94 44 59 30') as "n'en est pas" / "ne l'est pas" under standing values (94='ne' battery-promoted, 59='est' provisional, 30='pas' battery-promoted).
2. That value survives the four global frames — '77 44' x2 (@207, @1678), '47 44 59' @526-528 ('ce 44 est'), '44 00' x3 (@1311, @1583, @1679) — with grammatical parses at every instance, OR is fenced as window-local with a stated cause that names the value and explains the global failures.

## Method

Re-parsed the repaired stream in-work (1,847 pairs, 96 distinct, n(44)=15 confirmed). Enumerated all 15 windows of 44; verified '94 44' occurs exactly once globally (@1713→1714). Tested both rival values ('en', 'l'') at @1714 and at each of the four global frame-types using only standing values: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); battery-promoted (94=ne, 12=n + 48=e, 30=pas, 06=ent); provisional (59=est, 77=le). Prior reports read: battery-noun-44.md (kill mechanism source), battery-de-frame-44-83-21.md (status context). No standing verdict re-litigated; 94='ne' and 30='pas' used, not overturned (the clitic-forcing reading tensions them only if a rival parse were adopted — none is).

## Window-level evidence

**@1714 (row a8_06): '06 29 40 65 94 44 59 30 64 47 68'** — the forcing window.
- 44='en': "[65] n'en est pas qui…" — ne→n' elision before vowel-initial 'en'; partitive/genitive clitic. Grammatical.
- 44='l'': "[65] ne l'est pas qui…" — 'l'' = elided le/la before 'est'; direct-object clitic. Grammatical.
- Both rivals parse cleanly. No discriminator at the window: left context 65 is nominal ('65 qui' x3; n(65)=25; '65 94' x2 @687/@1712 but '65 94 44' unique to @1712), right context @1717=64='qui' (granted) accepts both readings. 44's promoted masculine gender leans weakly toward 'le'→'l'' over 'la', but 'en' is gender-neutral — the lean excludes nothing. The two rivals are indistinguishable here.

**Global frame 1: '77 44' x2** (@207: '42 06 77 44 50 88'; @1678: '39 74 77 44 00 46').
- 44='en': "le en [50]" / "le en pour" — ungrammatical ('en' cannot follow the article 'le' as a content word). FAIL.
- 44='l'': "le l' [50]" / "le l' pour" — ungrammatical (article+clitic stack; 'l'' requires a vowel-initial follower, 50 and 00='pour' are not). FAIL.

**Global frame 2: '47 44 59' ('ce 44 est')** (@526: '81 97 47 44 59 37 64 26').
- 44='en': "ce en est [37]" — ungrammatical. FAIL.
- 44='l'': "ce l'est [37]" — ungrammatical ("ce l'est" is not a French form; the elided copula is "c'est" = 87+59 composition). FAIL.

**Global frame 3: '44 00' x3** (@1311: '52 30 92 44 00 36 74'; @1583: '24 53 12 44 00 36 70'; @1679: '39 74 77 44 00 46 79').
- 44='en': "[92] en pour" / "n en pour" / "le en pour" — ungrammatical (preposition+preposition adjacency). FAIL all three.
- 44='l'': "[92] l' pour" / "n l' pour" / "le l' pour" — ungrammatical ('l'' before consonant-initial 'pour'). FAIL all three.

**Fencing arm:** window-local fencing requires naming ONE value with a stated cause. The two rivals are indistinguishable at @1714 (both parse; gender lean is non-excluding; no contact discriminator). Fencing either one as the window-local value would be forcing — exactly what the adverses forbid. The fencing arm is therefore unavailable, not merely unattempted.

## Per-clause verdicts

1. Clitic value parses at @1714: PASS — both 'en' ("n'en est pas") and 'l'' ("ne l'est pas") parse grammatically under standing values; undiscriminated.
2. Global survival or window-local fencing: FAIL on both arms — 'en' fails all four global frame-types (2+1+3 = 6 instances); 'l'' fails all four frame-types (6 instances); single-value window-local fencing would be forcing (adverses) given the rivals' indistinguishability at the window.

## Adverses (answered, none ignored)

- "do not force; neither rival is expected to survive the 'le 44' x2 / 'ce 44 est' / '44 pour' x3 frames globally": CONFIRMED and honored. Neither rival survives any of the six frame instances; no value is named, no single-value window-local fence erected. Nothing forced.

## Verdict: NULL

Headline: the bar's fallback fires exactly as designed. @1714 forces 44 into a clitic slot (confirming the noun-44 kill's mechanism — no lexical noun can intervene between 'ne' and 'est'), both 'en' and 'l'' parse there, but neither survives the four global frames and they cannot be discriminated at the window, so no single value can be fenced as window-local without forcing. **The clitic forcing at @1714 is recorded as the standing residual**: 44 occupies a clitic slot at @1714 with value ∈ {'en', 'l''}, unresolved.

No standing verdict is contradicted or downgraded: the noun-44 kill (conditional on 94='ne' + 59='est') is consistent with this result — this battery tested its regeneration #1 and confirms the forcing while declining to name the value. 94='ne' and 30='pas' battery promotions are used, not overturned. 44's masculine gender promotion stands (weak, non-discriminating lean noted). §7 sole-polyvalence law untouched (no second value asserted for 44 anywhere). Not a kill: neither rival is forced false at @1714, and no cleaner rival value is demonstrated. Not a promote: clause 2 fails.

## Follow-ups (null regenerates work)

1. **clitic-44-65-discriminator** (priority 2): discriminate 'en' vs 'l'' at @1714 via 65's profile. Evidence: '65 94' x2 (@687 'qui [29] e [65] ne [29]…', @1712 the forcing window) but '65 94 44' unique to @1712; '65 qui' x3; n(65)=25; '29-40-65' x3 '[X]ere [65]' direct-object slot (prof-65, queued). Bars: "resolve iff 65's contact profile favors one reading — a 'de'-complement source or partitive frame supporting 'n'en est pas', or a copular/subject frame supporting 'ne l'est pas' — with the other reading fenced; else record @1714 as permanently undiscriminated and fence the clitic forcing as value-open window-local." Adverses: 65's value open — do not name it; do not re-litigate 94/59/30.
2. **clitic-44-census** (priority 3): complete clitic-slot census of 44's 15 windows. Evidence: '94 44' x1 (@1713) is the only 'ne 44' adjacency on the repaired stream; remaining windows carry successors 50/94/59/29/77/74/83/00/11 — classify each as whole-word nominal, word-internal stem, or clitic-slot. Bars: "resolve iff all 15 windows of 44 are classified (whole-word nominal / word-internal stem / clitic-slot) with @1714 the sole clitic-slot window, or a second clitic-slot window is found and parsed under 'en'/'l''; deliver the classification table." Adverses: coordinate with stem-44-nominal (stem-vs-whole adjudication) and stem-44-1839 (@1839 instance) — this census classifies slots only, names no values, and does not re-adjudicate stem-vs-whole.

## Provenance

Every number re-derived from the repaired 1,847-pair stream in-work: n(44)=15; '94 44' x1 (@1713); '77 44' x2 (@207, @1678); '47 44 59' x1 (@526-528); '44 00' x3 (@1311, @1583, @1679); n(65)=25; '65 94' x2 (@687, @1712); '65 94 44' x1 (@1712). No invented data. R5005, sealed gates, and the red-team adjudication queue untouched.
