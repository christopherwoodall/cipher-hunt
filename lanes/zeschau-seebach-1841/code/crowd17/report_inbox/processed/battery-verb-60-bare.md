# Battery report: verb-60-bare

Worker: verb-60-bare subagent (session facabc32-d277-4d78-bb25-3402d6472135).
Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py
(re-implemented inline; n=1847 asserted). canonical.py never used. R5005,
sealed gates, and the red-team adjudication queue untouched. @i = 0-based
pair index.
Lock: code/crowd17/next-token/locks/verb-60-bare.lock created at start
(2026-10-09T02:06:07Z), no prior lockfile (no stale-lock note needed).
No red-team verdict on 60 exists — no contradiction, no escalation.

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"name one verb with stem 60 parsing all four frames with stated syllable
boundaries, using only banked/granted/promoted values; 60='on' excluded
(84='on' granted)"

Numbered clauses (fixed before data examination):

1. (C1) ONE verb is named (a specific French verb) with 60 as its stem,
   such that 60 takes that stem value in all four frames V1–V4, with
   stated syllable boundaries.
2. (C2) All four frames parse grammatically under C1, using only
   banked/granted/promoted values (11=la, 70=pre, 82=m, 34=i, 29=er,
   40=e, 46=que; 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
   84=on, 47=ce; 59=est, 77=le; 94=ne STRONG LEAD, 06=ent, 12=n,
   48=e, 30=pas), with @-offsets cited; open neighbors (08/98/53)
   fenced with stated cause.
3. (C3) 60='on' is excluded (84='on' granted A15).
4. (C4, kill-check) No frame forces 60 non-verbal under the named verb,
   and no cleaner rival verb covers the four frames.

Coordination (from brief, not re-litigated): V3 is also
adjective-compatible — adj-frame-995-solo (2026-10-08) PROMOTED the
@995 frame as '[03-N] [60-adj] et[67] la[11]' postnominal at frame
level (60's value unnamed; global adjudication with poly-60-redteam).
This battery does not contradict that frame promotion: it tests only
whether the VERB reading remains available at V3. V4's '[60ent] veut
[inf]' adjacency stays fenced (clause boundary or 53 re-parse needed).

## Method

Fresh parse per protocol. No prior counts trusted. The four frames
re-derived on the repaired stream:

- V1 @1338: pairs @1332–1345 = `52 39 83 86 71 64 60 08 65 64 52 38 47 86`
  → `...[71] qui[64] [60] [08] [65-noun] qui[64]...`
- V2 @700: pairs @694–705 = `46 02 50 45 28 94 60 12 98 20 12 66`
  → `que[46] [02] [50] ce[45] [28] ne[94] [60] n[12] [98] [20]...`
- V3 @995: pairs @989–1000 = `76 49 24 26 30 03 60 67 11 96 82 33`
  → `pas[30] [03] [60] et[67] la[11] par[96] m[82] [33]...`
  (67='et': follower 11='la' banked, non-infinitive-shaped, per the
  sole-polyvalence positional rule)
- V4 @1474: pairs @1468–1481 = `62 38 26 12 41 53 60 06 67 33 29 82 16 98`
  → `[41] [53] [60] ent[06] veut[67] [33] er[29]...`
  (67='veut': follower 33 is INF-class; "67-33-29" = "veut [X]er";
  06='ent' battery-promoted as verb ending)

Candidate sweep: every French verb family whose 3sg form could sit bare
in V1/V3 and whose 3pl is stem+"ent" in V4 was tested against V2.

## Window-level evidence

### V1, V3, V4 cohere under the -dre family (exact stem match)

-dre verbs have 3sg = stem and 3pl = stem+"ent" with zero allomorphy,
so one group 60 covers both:

| verb | V1 "qui [60] [08]" | V3 "[03] [60] et" | V4 "[53] [60]ent" |
|---|---|---|---|
| répondre (60="répond") | "qui répond [08]" ✓ | "[03] répond et" ✓ | "[53] répondent" = "répond"+"ent" ✓ |
| vendre (60="vend") | "qui vend [08]" ✓ | "[03] vend et" ✓ | "[53] vendent" ✓ |
| tendre (60="tend") | ✓ | ✓ | "tendent" ✓ |
| rendre (60="rend") | ✓ | ✓ | "rendent" ✓ |
| attendre (60="attend") | ✓ | ✓ | "attendent" ✓ |
| entendre (60="entend") | ✓ | ✓ | "entendent" ✓ |
| défendre (60="défend") | ✓ | ✓ | "défendent" ✓ |
| descendre (60="descend") | ✓ | ✓ | "descendent" ✓ |

08/53 stay open and fenced (adverse acknowledged): 08's value is
unconstrained by these frames ("qui répond [08]" needs only 08 to be
verb-compatible-adjacent, e.g. adverbial); 53's value is open
(prof-53 null 2026-10-08). The V4 right-edge adjacency
("[60]ent veut [inf]") stays fenced per the brief — it fences the
clause, not 60's verb-hood. The -er family ("parl-": V4 "parlent"
exact, V1/V3 need the mute -e) is a live rival, strictly weaker than
-dre on V1/V3 (mute-e unwritten vs -dre's exact 3sg). "prendre"
("qui prend" ✓ / "[03] prend et" ✓) fails V4 at exactness:
"prennent" is "prenn"+"ent", and the "70-12-94 prenne" fence shows
the cipher does NOT merge nn across groups, so "prend"+"ent" is
not a clean parse. "mettre" fails the same way ("mettent").

### V2 is ungrammatical under EVERY French verb — the impossibility proof

V2 = `94 60 12 98` = "ne[94] [60] n[12] [98]" (94='ne' STRONG LEAD
R17-001, 12='n' promoted). For a verb to parse here, the verb form
must be either (a) "[60]n" (12 verb-final), or (b) "[60]" + "n[98]"
(12 word-initial).

(a) Verb-final -n is impossible. Exhaustion: no French finite verb
form ends in the bare letter -n. 3sg/3pl of -er/-ir/-re verbs end
in -e/-s/-t/-d/-x/-ent/-ont; irregulars (vient, tient, devient,
prend, met, dit, fait, peut, veut, doit, sait, est, a, va, font,
vont, sont, ont) end in -t/-d/-s/-e/-x, never bare -n. Subjunctive,
imperative, infinitive, and participle forms likewise never end
in -n. Therefore "[60]n" cannot be a French verb under any value
of 60. (Note: "vient"/"tient" end in -nt; reading 12 as "nt"
contradicts promoted 12='n'.)

(b) "n[98]" word-initial options all fail:
  - 12 = "n'" (elision) before vowel-initial 98 → "ne [60] n'[98]"
    = "ne VERB ne-..." — DOUBLE "ne" in one clause, ungrammatical
    in 1841 French (verified: every "n'"+vowel expansion is "ne"+X).
    The only rescue is a clause boundary between 60 and 12, for
    which there is no independent evidence — fenced, not assumed.
  - 12+98 = "non"/"nous"/"notre"/"nul"/"nom"/"nombre": none yields
    a grammatical "ne VERB nX [20]" ("ne [60] non [98]" is marginal
    at best and needs 98="on", a new value; "nous"/"notre" need
    preverbal position or a following noun 98 is not).
  - 12+98 = "nulle" ("ne [60] nulle [20-fem]", 1841-valid
    "ne...nulle") needs 98="ulle", a new value — barred.

(c) Re-segmenting 94 does not rescue the n: 94@699's left neighbor
28 is a hapax predecessor ("28 94" x1 on stream); the twin anomaly
@841 ("94 26 12": "ne[94] [26-noun-lead] n[12]") shows "ne"+noun is
likewise ungrammatical, corroborating that 94 has segmentation
problems (cf. ne-ce-1169's 94-87 hapax finding, 2026-10-08), but no
re-segmentation tested here produces a grammatical V2 either —
that is follow-up work, not assumed.

Therefore V2, as segmented, admits NO grammatical French parse with
a verb in the 60 slot. C1 cannot be satisfied: the -dre family (and
every rival) parses V1/V3/V4 exactly but cannot parse V2.

## Per-clause pass/fail

- C1: FAIL. No verb parses all four frames. The -dre family
  (répondre/vendre/tendre/rendre/attendre/entendre/défendre/descendre)
  parses V1/V3/V4 with exact syllable boundaries (3sg=stem,
  3pl=stem+"ent") but V2's "ne [60]n [98]" is ungrammatical for every
  French verb (§"impossibility proof" above).
- C2: FAIL (consequence). V1/V3/V4 parse cleanly (08/53/98 fenced
  open; V4 adjacency fenced per brief); V2 does not parse.
- C3: PASS. 60='on' never invoked; the "entonne" candidate stays
  excluded (84='on' granted; it also fails V2 independently).
- C4: PASS. No frame forces 60 non-verbal: V1/V3/V4 are verb-parsed
  under -dre; V2's failure is a segmentation/parse failure, not a
  non-verbal forcing (no noun/adjective rival parses V2 either —
  noun-60 and adj-60 single-value claims are both killed, standing).
  No cleaner rival verb covers the four frames (all fail V2).

## Verdict

**NULL** — V1, V3, V4 cohere exactly under the -dre verb family
(60 = "répond"/"vend"/"tend"/"rend"/"attend"/"entend"/"défend"/
"descend", 3sg=stem, 3pl=stem+"ent"), but V2's "ne [60]n [98]" is
provably ungrammatical under every French verb: no verb form ends
in bare -n, the "n'"-elision rescue yields double "ne", and no
"n[98]" word fits. Per the verb-60 precedent (C1 fail → null, not
kill: the verbal class is not defeated, only the naming), this is a
null. The structural result: V2 is a segmentation residual, not a
verb-naming problem. No standing verdict contradicted or downgraded;
the @995 adjective frame promotion (adj-frame-995-solo) is untouched;
global 60 adjudication stays with poly-60-redteam.

## Follow-ups (work regenerates; none duplicates queued targets)

1. **seg-94-60-12** (priority 2): re-segment V2's "94 60 12 98"
   (@699–702). Bar: "produce one grammatical parse of @699–702 under
   standing values with stated word boundaries — testing (i) 94
   leftward ('[28]ne'), (ii) 94='ni' with 12+98='ni', (iii) a clause
   boundary between 60 and 12 — using only banked/granted/promoted
   values; else fence V2 as a segmentation residual with stated
   cause." Evidence: this battery (§impossibility proof); the @841
   "94 26[noun] 12" twin anomaly; ne-ce-1169's 94-segmentation
   finding (2026-10-08). Adverses: 94='ne' STRONG LEAD R17-001 (do
   not overturn without red-team declaration — fence, don't declare);
   28 hapax predecessor.
2. **verb-60-dre** (priority 2): name the -dre verb across V1/V3/V4
   (+ @197 "21 60 08 67" as a fifth leg). Bar: "name one -dre verb
   (répondre/vendre/tendre/rendre/attendre/entendre/défendre/
   descendre/prétendre) with 60=stem parsing V1 ('qui [60] [08]'),
   V3 ('[03] [60] et'), V4 ('[53] [60]ent'), and @197 ('[21] [60]
   [08] et') with stated boundaries, using only
   banked/granted/promoted values; V2 excluded pending seg-94-60-12."
   Evidence: this battery (exact 3sg/3pl stem match). Adverses:
   08/53 open; V4 adjacency fenced; @197's 21 context open;
   coordinate with poly-60-redteam (do not pre-empt global
   adjudication).
3. **verb-60-er** (priority 3): test -er stems as the rival family.
   Bar: "name one -er stem with 60=stem; V4 '[53] [60]ent' must parse
   exact; state how V1/V3's missing mute -e is handled (08='e'? 08
   adverbial with unwritten e?); V2 excluded pending seg-94-60-12;
   rank against verb-60-dre's -dre exactness." Evidence: this
   battery (-er weaker on V1/V3). Adverses: mute-e handling must be
   stated, not assumed; 08's distribution ('08 31' x3) must be
   reconciled with any 08='e' claim.

## Files

- Report: code/crowd17/report_inbox/battery-verb-60-bare.md (this file)
- Queue: battery-queue.json `verb-60-bare` → status `verdict`, result
  `null` (own entry only, temp-file + rename; pre-write assert: no
  prior verdict existed)
- Lock: code/crowd17/next-token/locks/verb-60-bare.lock created on
  start, deleted on completion
