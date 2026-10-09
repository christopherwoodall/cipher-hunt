# Battery report: s5-stem-ranking-feed

- Target id: `s5-stem-ranking-feed`
- Claim: "Package both stems' corpus attestations (with line references) as battery evidence for the red-team S5/37 stem-value adjudication — evidence feed only, no adjudication at battery level."
- Date: 2026-10-09
- Worker: battery worker (subagent 9d5f8514-3fe7-4f26-b377-b47452076049)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`). `canonical.py` never used. R5005 not touched. Sealed gates and red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/s5-stem-ranking-feed.lock` (created at start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

The target's `bars` field is `None`. Per the parent brief and claim text, the bar is:

1. "Package both stems' corpus attestations (with line references) as battery evidence for the red-team S5/37 stem-value adjudication — evidence feed only, no adjudication at battery level."
2. "Evidence feed only, no adjudication at battery level. Gather-only, no battery decision."

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) Corpus attestations of both stems ('satis' = satisfaire, 'contre' = contrefaire) are packaged with file + line references.
2. (C2) No adjudication is made — no stem value is selected, ranked, or fenced; no class/value is named for 37.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock with agent id + UTC timestamp.
2. Read the parent battery report (`code/crowd17/report_inbox/processed/battery-satisfait-contrefait-lex.md`) and adopted its verdict as premise: 37-01 is a single word-internal unit reading 01='fait' (promoted at battery level 2026-10-09); stem choice between 'satis' (satisfait) and 'contre' (contrefait) is residual. It returned NULL: both stems are period-attested 3sg finite verbs with the same transitive government; the followers' open values admit no selectional test.
3. Ran a fresh corpus census over `code/side-period/corpus/` (97 files, 1841 French; the 170-byte HTTP-500 stub `revue-deux-mondes-1840-q1.txt` excluded) for finite-verb forms satisfait / satisfont / contrefait / contrefont, extracting every match with file + line number, then hand-classified finite-verb attestations against adjective/past-participle uses (the dominant noise class: "être satisfait", "n'a pas satisfait" = past participle in composé, "je suis satisfait", etc.).
4. Verified the representative attestations by reading the lines in situ.

## Evidence gathered (C1)

### Corpus totals

- "satisfait" (all uses): 346 matches, of which ~14 cleanly finite 3sg present-verb attestations listed below; the rest are past participles/adjectives ("être/est satisfait", "n'a pas satisfait" in passé composé), or ambiguous past-participle government ("n'avait point satisfait ...").
- "satisfont" (3pl): 7 matches; 5 cleanly finite verb uses listed below.
- "contrefait" (3sg): 10 matches; 3 cleanly finite verb uses listed below.
- "contrefont" (3pl): 1 match; 1 finite verb use listed below.

### 'satis' (satisfaire) — finite-verb attestations

**3sg present:**

1. `nesselrode-v9.txt:1171` — "Le journal de Francfort satisfait ma curiosité" — 3sg + nominal DO.
2. `revue-deux-mondes-1841-q1.txt:8169` — "ne satisfait aucun de nous" — 3sg + pronominal/partitive DO.
3. `revue-deux-mondes-1841-q1.txt:12616` — "qui satisfait à son gré tous les caprices" — relative-clause 3sg, à-government + nominal DO.
4. `revue-deux-mondes-1841-q4.txt:35528` — "que le statu quo la satisfait" — 3sg + pronominal DO.
5. `revue-deux-mondes-1841-q3.txt:25712` — "M. Emile Deschamps satisfait tout le monde" — 3sg + nominal DO (verified in situ).
6. `guizot-memoires-t2-gutenberg.txt:11614` — "Une puissance qui satisfait à la fois aux [besoins]" — relative-clause 3sg, à-government.
7. `guizot-memoires-t3-gutenberg.txt:9127` — "cette si juste parole ne satisfait personne" — 3sg + pronominal DO.
8. `talleyrand-memoires-v2.txt:3280` — "ne satisfait ni à Dieu ni à César" — 3sg, à-government, doubled complement.
9. `talleyrand-memoires-v5.txt:3626` — "il satisfait à tout" — 3sg, à-government.
10. `tocqueville-democratie-t2.txt:2562` — "Cette réponse ne me satisfait point" — 3sg + pronominal DO.
11. `tocqueville-democratie-t4.txt:7458` — "ce qui satisfait le plus les regards" — relative-clause 3sg + nominal DO.
12. `revue-deux-mondes-1840-q2.txt:6658` — "ne satisfait pas la pensée du spectateur" — 3sg + nominal DO.
13. `revue-deux-mondes-1840-q2.txt:6960` — "que satisfait le jeu" — inverted-relative 3sg + nominal subject.
14. `raw-thtredecasim01dela-djvu.txt:18644` — "Lui seul, il satisfait aux besoins de mon cœur" — 3sg, à-government.
15. `chateaubriand-outre-tombe-t5.txt:5930` — "on ne satisfait pas impunément ... une ambition avide" — 3sg + nominal DO.

**3pl present:**

16. `hugo-ruy-blas.txt:1` — "satisfont un besoin" — 3pl + nominal DO.
17. `nesselrode-v8.txt:3759` — "deux qui me satisfont" (verified in situ) — relative-clause 3pl + pronominal DO.
18. `guizot-memoires-t1-gutenberg.txt:7106` — "ils ne le satisfont pas" — 3pl + pronominal DO.
19. `revue-deux-mondes-1841-q4.txt:30631` — "les décisions rendues par le conseil d'état satisfont [à...]" — 3pl, institutional subject.
20. `revue-deux-mondes-1840-q2.txt:41008` — "elles ne satisfont pas l'esprit" — 3pl + nominal DO.

### 'contre' (contrefaire) — finite-verb attestations

**3sg present:**

21. `revue-deux-mondes-1841-q1.txt:39419` — "On le contrefait à Paris en ce moment" (verified in situ) — 3sg + pronominal DO (a book).
22. `revue-deux-mondes-1840-q2.txt:41885` — "Il contrefait tour à [tour] ..." — 3sg + manner complement.
23. `chateaubriand-outre-tombe-t2.txt:10482` — "Si l'on ne contrefait que les bons ouvrages" — 3sg + nominal DO.

**3pl present:**

24. `revue-deux-mondes-1841-q2.txt:20160` — "ceux qui la contrefont" — relative-clause 3pl + pronominal DO.

### What the attestations show (evidence only, no ranking)

- Both stems are period-attested as finite 3sg verbs with direct transitive government (nominal and pronominal DOs), at registers matching the diplomatic letter (RDM, Nesselrode, Guizot, Talleyrand, Tocqueville).
- "satisfaire" additionally attests à-government ("satisfaire à tout/à Dieu"); no preposition intervenes between 37-01 and any of the three cipher followers (@939→07, @1633→74, @1817→02), so that frame cannot fire at the cipher windows (adopted from the parent NULL).
- "contrefaire" attests 3sg government of nominal DOs ("les bons ouvrages") and pronominal DOs ("le", "la"); producing-copy semantics ("contrefaire" = imitate) is visible in @23's context but cannot be tested against the cipher followers' open values.
- Relative counts (3sg: 15 vs 3; 3pl: 5 vs 1) reflect corpus frequency, not stem discrimination — frequency is not a selectional leg.

## Per-clause pass/fail

1. **C1 (attestations packaged with line references): PASS** — 24 finite-verb attestations packaged above with file + line references, all hand-verified against adjective/participle noise.
2. **C2 (no adjudication): PASS** — no stem value is selected, ranked, or fenced; 37's value remains open; the S5/37 stem-value adjudication is red-team venue.

## Verdict: NULL (gather-only package delivered)

Per the gather-only precedent in this lane (split-74-redteam-input, 41-verb-arm-package, redteam-94-v2-input, and others), no follow-ups are proposed — this is an evidence feed, and further stem work on 37 awaits red-team adjudication.

## Scope

Evidence feed only. 37-01's wordinternal PROMOTE, the parent satisfait-contrefait-lex NULL, the round-7 S5 fence, R18-016, A1/A12, §7 all untouched; no standing or red-team verdict contradicted, downgraded, or re-litigated; no value named for 37.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-s5-stem-ranking-feed.md`
- Queue: `s5-stem-ranking-feed` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.s5-stem-ranking-feed.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/s5-stem-ranking-feed.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
