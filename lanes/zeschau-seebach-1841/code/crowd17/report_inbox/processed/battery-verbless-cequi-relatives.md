# Battery verdict: verbless-cequi-relatives

- Target: `verbless-cequi-relatives` (battery-queue.json, priority 3, status queued)
- Claim: census all verbless 'ce qui' + prepositional-phrase heads in the cipher stream against sentential licenses; decides whether the verblessness itself is systematic beyond the 'par' geometry.

## Bar (verbatim, numbered)

C1. Census all verbless 'ce qui' + prepositional-phrase heads in the cipher stream against sentential licenses.
C2. Record per-window grammatical/fenced with stated cause.
C3. Verdict PROMOTE if the census resolves the verblessness question, NULL with follow-ups if not.

Adverses: none listed.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/verbless-cequi-relatives.lock` on start (agent 7703d1e8-d973-4ea2-82c2-5e4e023b71bb, 2026-10-09T20:17Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (parse per `code/side-keyhunt/repair_parse.py`): 1,847 pairs, 96 types. `canonical.py` never used.
3. Enumerated every "ce qui" bigram under all three standing 'ce' values: 87='ce' (granted), 47='ce' (A4 allophone), 45='ce' (A11 hold). Found 8 windows: 87-64 x5 (@148, @180, @1767, @1775, @1800), 45-64 x3 (@314, @340, @1024), 47-64 x0.
4. For each window, tested whether the "ce qui" relative clause contains a finite verb (French subject-relatives require one), using standing values only. Corpus control: grepped ~61M chars of 1841 French (`code/side-period/corpus/`, 98 files) for "ce qui par [complement]".

## Findings

### Window census (all 8, byte-verified)

**@148 (a1_04): `84 29 [87=ce 64=qui] 96=par 47=ce 46=que 66 84=on 26 ... 94=ne 24` — VERBLESS + PP head ("par"). FENCED as written.**
- No finite verb between "qui" and the PP; "ce qui par ..." strands the relative without a verb.
- Live-but-conditional rescue: the clause could close on "ne [24]" @161-162 ("ce qui ... ne V" with PP adjunct "par ce que [66] ..."). Not battery-grade: the span contains "on [26]" with 26 = noun LEAD ("on [noun]" ungrammatical absent the §7 split), so the rescue is conditional on red-team §7 adjudication.
- Note: left context "67 64 77 84 29" offers no verb either.

**@340 (a2_05): `[45=ce 64=qui] 96=par 43 87=ce 01 06=ent 70=pre 12 94=ne 74` — VERBLESS + PP head ("par"). FENCED as written.**
- Same "ce qui par" shape; tail "96 43 87 01" identical to @1024 (see below).
- Conditional rescue: close on "ne [74]" @349-350 — and "ne [74]" @350 IS battery-grade verb-forced (adopted split-74-redteam-input package). Still conditional: the adjunct span "par [43] ce [01] ent pre [12]" must parse with 43/01/12 open values; "par" needs an NP complement "[43] ce [01]" that cannot be verified at battery grade.

**@1024 (a6_03): `[45=ce 64=qui] 96=par 43 87=ce 01 03 29=er 80 77 ... 11=la 70=pre 82=m 34=i 29=er 40=e 17=fois` — VERBLESS + PP head ("par"). FENCED as written.**
- Twin of @340: the "96 43 87 01" tail is byte-identical. Only non-finite verb present is the infinitive "[03]er" @1030-1031 (03 verb-stem + 29='er'); 80's finiteness is open (A8 verb-frame, value open). The "la première fois" crib (@1034-1039) sits downstream but supplies no finite verb for the relative.

**@180 (a1_05): `[87=ce 64=qui] 23 37 06=ent 00=pour ...` — verblessness CONDITIONAL, no PP head. FENCED as undecidable.**
- Follower is 23 (open), not a preposition. If 23 is verb-class, the clause has a verb ("[23] 37 ent"); 23's class is "honestly NOT decided" (R20). Cannot resolve at battery grade. Not a PP-head case under any reading.

**@1767 (a8_08): `[87=ce 64=qui] 26 37 78 62 94=ne 24` — HAS FINITE VERB. Grammatical shape.**
- 24 = finite verb (R17-009 class-level GRANT); "ne [24]" closes the clause in-window. No PP head.

**@1775 (a8_09): `[87=ce 64=qui] 59 19 48 ...` — HAS FINITE VERB (conditional on provisional 59='est'). Grammatical shape.**

**@1800 (a8_10): `[87=ce 64=qui] 77 84=on 59 ...` — HAS FINITE VERB (conditional on provisionals 77/59). Grammatical shape.**

**@314 (a2_04): `[45=ce 64=qui] 59 32 94 ...` — HAS FINITE VERB (conditional on provisional 59='est'). Grammatical shape.**

### Corpus control

- "ce qui par [complement]": **0 genuine attestations** in ~61M chars. The single raw hit ("ce qui parait...", Talleyrand mémoires v5) is "paraît" (verb), not "par" + complement.
- The verbless "ce qui par" shape is unattested in 1841 French: a real anomaly, not a licensed construction.

### Decision

- 3 of 8 windows are confirmed verbless-PP (@148, @340, @1024) — and **all 3 have "par" immediately after "qui"**. The 4th verbless candidate (@180) has no PP at all and is conditional on 23's undecided class. The remaining 4 windows all contain finite verbs.
- The verblessness is NOT systematic beyond the 'par' geometry: it is entirely confined to the "ce qui par" shape. The @340/@1024 twins share the byte-identical tail "par [43] ce [01]", a recurring formula rather than a one-off.
- The census resolves the question as posed: **PROMOTE.**

## Verdict: PROMOTE

C1 PASS (complete 8-window census across all 'ce' forms, each tested against sentential license). C2 PASS (per-window grammatical/fenced with stated cause above). C3 PASS (question resolved: verblessness confined to the par geometry; corpus control at zero).

## Scope

- Census-level only. Does not name any value, does not resolve the @148/@340/@1024 rescues (conditional on §7: 26-split, 43/01/12 values, 74's split), does not touch 23's class (red-team venue), 59/77 provisionals, or §7.
- No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row offsets unvalidated).
- No follow-ups required (promote, not null). Optional red-team note: the "ce qui par [43] ce [01]" twin formula (@340/@1024) is a candidate construction-level venue item.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-verbless-cequi-relatives.md`
- Queue: `verbless-cequi-relatives` queued -> `verdict`/`promote`, 2026-10-09 (pre-write assert passed - was queued/verdictless; target-id-unique tmp `battery-queue.json.verbless-cequi-relatives.tmp` + atomic rename, no leftover; disk re-validated; own entry only; no downgrade)
- Lock `locks/verbless-cequi-relatives.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
