# Battery report: w3-01-adjudicate

- Target id: `w3-01-adjudicate`
- Claim: "resolve 01@984 between 'en' (disc-01-24-ci-X battery promote) and '-ci' demonstrative suffix"
- Date: 2026-10-08
- Worker: battery worker (session 994bb671-e46d-412f-afac-b551c61596b5)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
  re-derived in-session: 1,847 pairs confirmed). `canonical.py` never used.
  R5005, sealed gate instances, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/w3-01-adjudicate.lock (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"name 01@984 iff one value parses @981-988 with zero dangling tokens and the
other leaves >=1 token unparsed or needs >=1 extra assumption; the loser is
fenced with stated cause — no queue verdict is downgraded, this is the
adjudication the never-downgrade rule requires before either can promote"

Numbered pass/fail clauses (restated before testing, not modified after):

1. R2 ('en') parses @981-988 with zero dangling tokens beyond the tokens
   that are open-valued identically under both readings (48@987 and
   01@988, whose values are open at every grade; neither reading claims them).
2. R1 ('-ci') needs >=1 extra assumption relative to R2 (an assumption not
   covered by any standing granted or battery-promoted verdict).
3. The loser is fenced with stated cause; no queue verdict is downgraded.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs confirmed). Window
   @981-988 (row a6_01) = `47 78 45 01 24 89 48 01` — re-derived, not cited.
   Verified: n(01)=28, n(24)=52; 01-24 windows exactly @40/@828/@984
   (so @984 sits inside disc-01-24-ci-X's stated 01='en' locality);
   45-01 occurs exactly once on the stream (@983); 78-45 x4 at
   @313/@573/@982/@1164. Trailing context @987-993 = `48 01 76 49 24 26 30`
   (the 49-24-26-30 block is disc-01-24-ci-X's fenced "[76] [49] fait [26]
   pas" @989-993; the 48@987 and 01@988 are claimed by neither reading).
2. Did not re-run disc-01-24-ci-X, dict-45-w3-ceci, ci-01-value,
   ci-bound-01, ver-78-rebar, or ne-24-profile. Coordinated only, against
   their standing verdicts: disc-01-24-ci-X battery-PROMOTE (01='en' local
   to the three 01-24 windows; 24='faire'); dict-45-w3-ceci NULL (R1 vs R2
   head-to-head, mutual-conditionality finding); ci-01-value kill of general
   01='ci'; ci-bound-01 NULL (bound '-ci' fenced to ce-adjacent positions);
   ver-78-rebar NULL (78='ver' LEAD, red-team).
3. Compared the two readings token-by-token over the fixed window @981-988,
   holding the shared base constant: 47='ce' (A4 granted), 24='faire'
   (battery-PROMOTE, unratified), 89=verb-frame (A8 granted), 48 and 01@988
   open-valued under both.

## Window-level evidence (@981-988 = 47 78 45 01 24 89 48 01)

### R2 ('en'): "ce(47) [78] ce(45) en(01) fait(24) [89-inf] [48] [01]"

- 45='ce' per A11 HOLD (granted, positional allophone account). 01='en' per
  disc-01-24-ci-X battery promote, local to the 01-24 windows — @984 is one
  of exactly three such windows (verified: 01-24 at @40/@828/@984 only).
  "ce en fait [89]" parses as reported ("en" clitic-climbed object of the
  infinitive [89] under causative "faire").
- 78's value is NOT load-bearing for R2: the reading holds whether 78 is
  'ver' or open. 48 and 01@988 are open-valued (not claimed by any standing
  verdict). No assumption beyond standing verdicts is needed.

### R1 ('-ci'): "ce(47) verdict(78-45) -ci(01) fait(24) [89-inf] [48] [01]"

- Grammatical ("ce verdict-ci fait [89]" = standard discontinuous French
  demonstrative), but every load-bearing token past 47 carries an
  un-settled dependency:
  - 78-45='verdict' is load-bearing on 78='ver' (LEAD, ver-78-rebar NULL,
    red-team). R2 has no such load.
  - 45='dict-syllable' is a lead (R16-004) conditional on that same NULL
    78='ver' — and the dict-45-w3-ceci circularity finding stands: this
    window was already counted once, conditionally, by ver-78-rebar, so
    R1's 'verdict' composition re-counts the same conditional window and
    adds no independent leg.
  - 01='-ci' is un-named at every grade. The fenced bound-'-ci'
    (ci-01-value fence; ci-bound-01 NULL) covers only ce-adjacent positions
    (87-01 x2, 47-01, 45-01@984-as-ceci). Post-nominal '-ci' after a noun
    ('verdict') is a NEW environment with no other window on record —
    owned by follow-up ci-demonstrative-census (queued).
- R1's extra assumptions vs R2: (a) a novel, un-named '-ci' environment;
  (b) the NULL-conditional 'dict'-syllable leg; (c) the mutual-conditionality
  re-count; (d) load-bearing dependence on NULL 78='ver' where R2 needs
  nothing of 78. That is >=1 extra assumption by any count.

## Per-clause pass/fail

1. R2 parses @981-988 with zero dangling tokens beyond the shared open
   tokens: PASS. Every reading-specific token (45, 01) parses under standing
   verdicts (A11 HOLD, battery-PROMOTE). The only unparsed tokens (48,
   01@988) are unparsed identically under R1 — they are open values, not
   R2's dangling debt.
2. R1 needs >=1 extra assumption relative to R2: PASS (four enumerated
   above; the novel un-named '-ci' environment alone satisfies the clause).
3. Loser fenced with stated cause, no downgrade: PASS (see verdict).

## Adverses

1. "78='ver' NULL (both readings conditional — state the dependency, do not
   re-litigate)": FENCED with stated cause. Both readings are conditional
   on the 78='ver' LEAD (ver-78-rebar NULL, escalated to red team), but the
   dependency is asymmetric: R1 is load-bearing on it (78-45='verdict'),
   R2 is not (78's value does not touch "ce en fait [89]"). Not
   re-litigated; owned by the red team (ver78-45-dependency-gate queued).
2. "§7 sole-polyvalence (exactly one value may win)": ANSWERED. Exactly one
   value is named at 01@984 ('en'). '-ci' is fenced AT THIS WINDOW, not
   globally: the bound-'-ci' ceci frames (87-01 x2, 47-01) stay fenced as
   ci-bound-01 left them, and ci-demonstrative-census (queued) still owns
   the census question. 01='en' stays local to the three 01-24 windows per
   disc-01-24-ci-X's scope limit; 01@988's value is NOT named here.

## Verdict: PROMOTE (battery-level, unratified)

01@984 = 'en'. The bar's discriminator fired: R2 parses with no extra
assumptions beyond standing verdicts; R1 needs >=1 extra assumption
(novel un-named '-ci' environment + NULL-conditional 'dict' leg +
mutual-conditionality re-count + load-bearing NULL 78='ver'). The loser
'-ci' demonstrative suffix at @984 is FENCED with stated cause:

- '-ci' is un-named at every grade; its only fence (ci-bound-01) restricts
  bound '-ci' to ce-adjacent positions, and the post-nominal demonstrative
  environment is new and untested (ci-demonstrative-census queued).
- R1's 'verdict' composition is load-bearing on 78='ver' (NULL, red-team)
  and re-counts a window already conditionally counted by ver-78-rebar
  (dict-45-w3-ceci circularity finding) — it adds no independent leg for
  45='dict' or 01='-ci'.
- §7 sole-polyvalence: with 'en' named, '-ci' cannot also hold 01@984.

No queue verdict is downgraded: this CONFIRMS disc-01-24-ci-X's standing
battery promote of 01='en' at @984 (the never-downgrade adjudication the
bar required before either value could promote). No red-team verdict is
contradicted or touched (A4, A11 HOLD, A8 relied on; R16-005 LEAD,
ver-78-rebar NULL, ci-01-value kill all left standing). Ratification of the
promote stays red-team-only per standing constraints.

Note on scope: this verdict names 01@984 only. It does not promote a global
01='en' (locality stands), does not decide 01@988, and does not alter the
fenced ceci frames. The queued follow-ups dict-45-circle-break and
ci-demonstrative-census are unaffected and still needed: the former gives
45='dict'-syllable its independent leg away from 01; the latter tests the
'-ci'-after-noun environment that this fence flagged.

## Reproducibility

Stream re-derivation: `code/side-keyhunt/repair_parse.py` (`load_rows` +
`parse` with `rep['a5_03']=0`), run in-session 2026-10-08: 1,847 pairs;
@978-988 = `92 07 76 47 78 45 01 24 89 48 01` (row a6_01); 01-24 windows
@40/@828/@984; 45-01 x1 @983; 78-45 x4 @313/@573/@982/@1164; n(01)=28,
n(24)=52. No writes outside this report, the queue entry, and the lockfile.
