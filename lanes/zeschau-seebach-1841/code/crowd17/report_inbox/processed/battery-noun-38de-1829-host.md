# Battery `noun-38de-1829-host` — verdict: NULL (fence executed)

- Target id: `noun-38de-1829-host` (priority 3)
- Claim: "[38]de" as a NOUN subject of finite 24 at @1829 (the surviving '-de'-final-word fork).
- Date: 2026-10-09
- Worker: 720a4e84-5097-4fe8-95c8-7f5847c33ff8

## Bar (verbatim, pre-registered)

"name the noun and parse the full window "86 29 82 38 83 24 82 16" under standing values (candidate shape: "[N-de] [24-modal] me [16-INF]"), or fence the noun fork with cause"

## Bar restated as numbered pass/fail clauses

1. C1: A noun value is named for the [38]+"de" host word, and the full window parses under standing values with the noun as subject of finite 24.
2. C2: Failing C1, the noun fork is fenced with stated cause.

## Method

Re-derived the repaired stream per `code/side-keyhunt/repair_parse.py`
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`):
1,847 pairs confirmed, 96 types confirmed. `canonical.py` never used.
R5005, sealed gates, red-team adjudication queue untouched. No invented data;
every number below traces to the stream. All @-offsets 0-based.

Adopted as premises (stated, not re-run):
- battery-syll-83-de-1829 (2026-10-09, NULL): the '-de'-final VERB fork is
  fenced at kill grade (finite+finite adjacency ungrammatical); the '-de'-final
  NOUN fork survives as a live residual. 83 = syllabic '-de', word-final.
- battery-syll-38-value-census (2026-10-09, NULL): 38's class promoted
  (verb-form, uniform); value narrowed to a vouloir/devoir 2-way tie.
- battery-ne-24-profile (verdict promote): 24 is class-level finite verb
  ("peut"/"sait"-shaped, modal/infinitive-taking).
- battery-de-83-residuals (2026-10-08, promote): @1829's word-level 'de'
  reading is dead.
- Standing values: 82='m' (pencil GT letter), 29='er', 86 INF-class,
  83='de' (LEAD). 16's class open. 38's spelling value open.

## Window-level evidence

Byte-confirmed (row a8_11): `@1825=86 @1826=29('er') @1827=82('m') @1828=38 @1829=83 @1830=24 @1831=82('m') @1832=16 @1833=59('est',provisional)`.

Note: the target's "@1829" names the 83 position; the "38 83" contact is
@1828–1829. Substance unaffected.

The "38 83" contact is a **stream hapax** (1/1,847). The fork lives or dies
at @1828 alone.

n(38)=7, all other windows verb-shaped: @384 "16 52 38 37 43", @826
"87 59 38 82 01" ("est 38"), @1113 "41 65 38 30 69" ("65 38 pas"),
@1343 "64 52 38 47 86" ("qui 52 38"), @1469 "02 62 38 26 12", @1650
"10 03 38 82 16" ("03-stem 38"). Zero spelling legs for 38 anywhere.

## C1: name the noun — FAIL

Naming the noun requires 38's spelling value as a syllable. 38 has zero
battery-grade spelling evidence: all 7 windows are verb-shaped, and the
standing vouloir/devoir tie is a VERB value, not a spelling. Candidate
nouns — "monde" (38="on"/"mon"), "garde" (38="gar"), "demande"
(38="deman"), "aide" (38="ai"), "mode" (38="mo"), "corde" (38="cor"),
"bande" (38="ban") — are fully underdetermined; no window discriminates
among them. Naming any one would be arbitrary (lane precedent:
masc-noun-86-name, 2026-10-09). The full-window parse additionally needs
16=INF (open) and a determiner for the noun (absent — see C2).

## C2: fence with cause — PASS

Two independent causes:

**(a) Determiner absence (grammatical).** The -de host word has no
determiner. @1827=82='m' is a pencil-GT letter, not a determiner: "m"
alone is not a French determiner, and "mon"+"de" does not compose. A bare
singular common noun cannot be the subject of finite 24 ("*monde doit me
croire" without "le"). The "m'"-elision rescue fails: "m'" is the object
pronoun "me" elided, and "me"+noun is ungrammatical — "m'" cannot
introduce a noun. The word-internal "m[38]de" reading ("monde" via
38="on") still leaves the noun determiner-less. Remaining rescues —
proper noun, vocative, closed idiom — have zero battery-grade legs
(the bare-nominal corpus kill, 30.8M chars, leaves exactly these
exceptions; none is evidenced here).

**(b) §7 block (structural).** A sub-lexical 38 at @1828 contradicts 38's
promoted uniform verb-form class (6/7 windows verb-shaped). Licensing it
requires the split-38de decision, which is red-team venue. The battery
cannot declare it (per brief NOTE).

The noun fork is therefore fenced, not killed: the proper-noun rescue is
logically open (a name ending in "-de" needs no determiner), so no window
forces the fork false at kill grade — but no battery-grade path promotes
it either.

## Scope

Fences only the '-de'-final NOUN fork at @1828. Untouched: 38's verb LEAD
and vouloir/devoir tie, 24's finite-verb class grant, 83's LEAD, the
syll-83-de-1829 verb-fork kill, de-83-residuals, §7 intact. No standing or
red-team verdict contradicted, downgraded, or re-litigated.
Canonical-stream caveat stands.

## Follow-ups (§4; all verified ABSENT from battery-queue.json)

1. `bare-subj-corpus` (P3) — corpus census: do bare singular -de-final
   nouns ever serve as finite-verb subjects in 1841 French? Closes the
   proper-noun/vocative rescue at grammaticality grade.
2. `split-38de-redteam-input` (P2, gather-only) — package the §7 split
   evidence (verb-form uniform 38 ×6 windows vs sub-lexical 38 at @1828)
   for red-team adjudication.
3. `val-16-1832-class` (P4) — name 16's class at @1832: INF-16 completes
   the "[N-de] 24 me INF" right half; non-INF kills the modal-complement
   shape independently of the noun.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-noun-38de-1829-host.md`
- Queue: `noun-38de-1829-host` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique temp
  file `battery-queue.json.noun-38de-1829-host.tmp` + atomic rename;
  disk re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/noun-38de-1829-host.lock`: created on
  start (2026-10-09T19:30:00Z, no stale lock), deleted on completion
  (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
