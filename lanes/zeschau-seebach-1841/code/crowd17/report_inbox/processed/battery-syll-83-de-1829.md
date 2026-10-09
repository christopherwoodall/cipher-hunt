# Battery `syll-83-de-1829` — verdict: NULL (verb fork fenced at kill grade; noun fork live)

- Target id: `syll-83-de-1829` (priority 3)
- Claim: "the @1829 '-de'-final-word fork ('38'+'de') fenced to this target by de-83-residuals"
- Date: 2026-10-09
- Worker: 359a2176-8e7b-493d-b9af-24638f6a81ba
- Verdict: **NULL** — the '-de'-final VERB fork is fenced at kill grade (grammatical impossibility); the '-de'-final NOUN fork survives as a live residual.
- Lock: created `code/crowd17/next-token/locks/syll-83-de-1829.lock` 2026-10-09T17:31:53Z, deleted on completion. No stale lock encountered.

## Bar (verbatim, pre-registered)

"host verb named and @1829 parsed, or fenced with cause"

## Bar restated as numbered pass/fail clauses

1. C1: A host verb is named at @1829 with 83='-de' as its final syllable, and the window parses under standing values.
2. C2: Failing C1, the verb fork is fenced with stated cause (or the '-de' fork is otherwise resolved).

## Method

Re-derived the repaired stream per `code/side-keyhunt/repair_parse.py`
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`):
1,847 pairs confirmed, 96 types confirmed. `canonical.py` never used.
R5005, sealed gates, red-team adjudication queue untouched. No invented data;
every number below traces to the stream. All @-offsets 0-based.

Adopted as premises (stated, not re-run):
- battery-de-83-residuals (2026-10-08, verdict promote): @1829's word-level
  'de' reading is dead (24 is a promoted finite verb; "de" + finite verb is
  ungrammatical); the '-de'-final-word fork ("38"+"de", syllabic 83) fenced
  TO this target.
- battery-ne-24-profile (verdict promote): 24 is a class-level promoted
  FINITE verb ("peut"/"sait"-shaped, modal/infinitive-taking).
- Standing values: 82='m' (pencil GT letter), 29='er', 86 INF-class,
  00='pour', 59='est' (provisional). 38 is open (n=7, no standing value).

## Window-level evidence

### @1829 — row a8_11 (byte-verified)

`... 00 97 00 86 29 82 [38 83 24] 82 16 59 36 69 64 ...`

Full 0-based indices:
- @1825=86, @1826=29('er'), @1827=82('m'), @1828=38, @1829=83,
  @1830=24, @1831=82('m'), @1832=16, @1833=59, @1834=36, @1835=69

Under the fork premise (83 = syllabic '-de', word-final), the host word ends
in the syllable sequence [38][de]. 24 (finite verb) follows immediately.
The left neighbor 82='m' is either word-internal ("m[38]de") or the elided
"m'" — either way the word's final syllable is 'de'.

### C1: naming a host verb — FAIL at kill grade

French verb morphology (verified against the lane period corpus,
76 files; de-final token census below): the ONLY French verb forms ending
in orthographic 'de' are finite —
- 1sg/3sg present indicative of -der verbs: aide, cède, décide, garde,
  demande, commande, regarde, guide, possède, procède, accède, ...
- 1sg/3sg present subjunctive of -der verbs (same forms),
- 2sg imperative of -der verbs (aide!, cède!, ...).

No infinitive, past participle, present participle, or gerund ends in 'de'.
Corpus check (sample of 6 files, 801 distinct de-final tokens): top forms
are monde, grande, demande, garde, mode, regarde, possède, aide — nouns,
adjectives, and finite verbs only; zero non-finite verb forms.

The host word ends in 'de'. If it is a verb, it is FINITE (1/3sg or
imperative). It is immediately followed by 24, a class-level promoted
FINITE verb. Two finite verbs juxtaposed without conjunction, relative
pronoun, or punctuation is ungrammatical in French in every period
("*il aide peut", "*elle demande vient"). No punctuation cell intervenes
("83 24" are adjacent pairs).

Therefore no verb can host the '-de' at @1829. C1 fails at kill grade —
not from lack of evidence (38 is open) but from grammatical impossibility.
This holds regardless of the word's left extent (whether "38de", "m38de",
or longer): the final 'de' forces finiteness, and finite+finite adjacency
is ungrammatical.

### C2: fence with cause — PASS

The '-de'-final VERB fork at @1829 is fenced: a verb ending in 'de' is
necessarily finite, and cannot immediately precede the finite verb 24.
Cause is grammatical (not evidentiary), so it stands regardless of 38's
future value and regardless of the 83='de' adjudication.

Explicitly NOT fenced: the '-de'-final NOUN fork. A noun ending in 'de'
can precede a finite verb as its subject ("la demande peut me surprendre"
is grammatical). 38 is open, so no noun is ruled out. The noun fork is
a live residual, fenced to follow-up 1 below.

Scope of the fence: verb-only. The syllabic 'de' fork itself (83 as
word-final syllable) is not killed — only its verb-host realization at
this window.

## Per-clause results

- C1 (host verb named and @1829 parsed): FAIL at kill grade — grammatical
  impossibility (finite '-de' verb + finite 24 adjacency).
- C2 (fenced with cause): PASS — verb fork fenced; noun fork noted live.

## Verdict: NULL

The bar's fence arm is satisfied, but the target's fork is narrowed rather
than resolved: the verb host is dead, the noun host is live. Per precedent
(verb-slot-62-1686-neque, val-31-1257-word: "name X or fence" bars that
fence resolve to NULL), and because the '-de'-final-word claim itself is
not falsified (noun fork survives), the verdict is NULL, not KILL.

## Adverses

None listed on the target. Coordinated (not duplicated):
- battery-de-83-residuals (promote): this battery executes the fork it
  fenced here; its @1829 out-of-class fence is consistent with (and
  strengthened by) this result.
- battery-syll-83-de (NULL): its follow-up 2 is this target; its
  "verb rival stays live" assessment concerned @614, not @1829 — no
  contradiction.
- battery-frame-87-83-cede (NULL): untouched; no 87-83 window involved.

## Standing red-team check

No standing red-team verdict on 83='de' or on 38 exists; nothing is
overwritten or contradicted. §7 intact (no polyvalence declared; the
fence is grammatical, not a value claim).

## Follow-up targets (null regenerates work; both verified ABSENT from queue)

1. **noun-38de-1829-host** (P3): test "[38]de" as a NOUN subject of finite
   24 at @1829 (the surviving fork). Bar: name the noun and parse the full
   window "86 29 82 38 83 24 82 16" under standing values (candidate shape:
   "[N-de] [24-modal] me [16-INF]"), or fence the noun fork with cause.
   Discriminating evidence: 38's value; the "82 38 83" = "m[38]de"
   letter-syllable composition (cf. "mode" if 38='o').
2. **syll-38-value-census** (P3): census 38's 7 windows (@384/@826/@1113/
   @1343/@1469/@1650/@1828) to name 38's syllable value. Bar: name with
   ≥2 independent legs, or fence as unnameable at battery grade. Decides
   both the noun-host candidate and the "82 38" / "38 82" letter contacts.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-syll-83-de-1829.md`
- Queue: `syll-83-de-1829` → `status: verdict`, `verdict: {result: null,
  report: code/crowd17/report_inbox/battery-syll-83-de-1829.md,
  date: 2026-10-09}` (pre-write assert passed — was queued/verdictless;
  temp-file + rename; disk re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion. R5005, sealed gates,
  red-team adjudication queue untouched.
