# PRE-REGISTRATION — Round-7 Closer battery for 59="est" promotion

Date: 2026-10-07. Executor: closer (round-7 work order 7).
Claim under test: **59="est" — promotion from STRONG LEAD to provisional.**
Standing legs (banked, F45, red-team UPHELD): S1 unigram 1.387× (n59=27,
P=0.01462 vs Tocqueville P("est")=0.01054); S2 64→59 ×3 @315/1209/1795...
@[1209]/1776 "qui est" (era n=83); S3 94→59 ×3 @558/762/1795 "n'est"
(era P(est|n')=0.2377, n=324); rivals doute/dit/fait/veut/peut killed 7–45×
on rate alone (Tocqueville rates).

Named blockers (red-team F45 ruling — genuine, unresolved):
(a) S4 "est que" 5.41× adverse: 59→46 ×2 @216/@1190; cipher P(46|59)=2/27=0.0741
    vs Tocqueville P(que|est)=0.0137. n=2.
(b) 01="est"-lead interaction: 87→59 ×1 @824 = "c'est" candidate vs 01="est"
    [MEDIUM lead, frenchman single-window @295 ear reading "16 est la 78"];
    A1's "c'est" count (87→01 ×2 @344/@1028 + 47→01 ×1 @194) rides on 01.
    Both-hold needs /ɛ/→{01,59} allophony (F33-allowed class, no conditioning
    rule stated) OR 01≠"est" (weakens A1).

## Battery legs (pre-registered, run after this file is written)

### Blocker (a) — S4 resolution
- **L1 [diplomatic-register rate leg].** Compute P(que|est) in the period
  diplomatic corpus (`code/side-period/corpus/`; primary: guizot-memoires-t5-t6
  — Guizot's printed 1840–42 foreign-minister despatches; nesselrode-v8 —
  actual 1840–46 chancellery correspondence incl. full 1841 run; combined
  "diplomatic" aggregate reported too). Compare cipher P(46|59)=2/27=0.0741.
  Bars (either passes L1):
  (i) binomial tail: under diplomatic p, P(X≥2 | n=27) ≥ 0.05 → n=2 adverse
      not a significant contradiction (small-sample artifact);
  (ii) cipher/diplomatic ratio ≤ 2 (lane band; NOTE red-team F26-1: factor-2
      band UNCALIBRATED — raw ratio reported, band status marked).
  L1 passes only if the adverse specifically shrinks vs the Tocqueville
  figure (register attribution), not merely on (ii) alone with Tocqueville.
- **L2 [S4 structural leg].** Examine both S4 windows (pairs[215:220],
  pairs[1189:1194]): predecessors pairs[215]/pairs[1189], successors
  pairs[218]/pairs[1192]. Test the licensed frames: "NP est que" cleft
  ("le fait est que"/"la vérité est que"-type: noun-typed predecessor) and
  "n'est que" ("ce n'est que": predecessor 94). Bar: both windows must admit
  a licensed grammatical frame with mutually consistent contexts and no
  frame hostility (e.g., predecessor provably non-nominal kills the cleft
  reading). PASS = structural explanation independent of L1's statistics.

### Blocker (b) — 01="est" interaction resolution
- **I1 [joint unigram].** n(01) + combined (n59+n01)/1847 vs diplomatic
  P("est"). Bar: if combined/era > 3×, both-hold as the same plain word
  "est" is REJECTED → one reading must be conditioned or one misvalued.
- **I2 [01 bigram profile].** 01's follower/predecessor profile: does 01 show
  finite-verb grammar (46-follower? 64/94/87-predecessors?) consistent with
  "est", and consistent with its A1 "c'est" role (87→01 ×2, 47→01 ×1)?
  Bar: PASS if 01's profile is verb-shaped and non-contradictory with 59's
  profile (both-hold as F33-class allophony stays live); FAIL-suspect if
  01's profile is non-verbal (then 01="est" is the weak reading, not 59).
- **I3 [@824 frame].** pairs[822:828] grammatical parse under banked 87="ce"
  (provisional) + candidate 59="est": does "c'est" read cleanly (predecessor
  of 87 @823 compatible; successor of 59 @825–826 compatible with "c'est X"
  grammar)? Bar: PASS if clean; if hostile, @824 is not "c'est" and the
  interaction is moot for 59 (allophony claim there unsupported).

### Re-verification legs (diplomatic corpus — the standing legs must survive register change)
- **L3 [S2 refreshed].** 64→59 ×3 vs diplomatic P(est|qui), n64=47.
  Bar: ratio ≤2× or binomial-compatible (P(X≥3|n=47,p) not < 0.05 adverse).
- **L4 [S3 refreshed].** 94→59 ×3 vs diplomatic P(est|ne/n'), n94=37.
  Bar: same.
- **L5 [rival re-kill on diplomatic rates].** doute/dit/fait/veut/peut vs
  diplomatic unigrams, cipher P(59)=0.01462. Bar: kill stands if ratio ≥5×
  away (either direction); <5× → rival survives, needs a second leg.

## Verdict rule (pre-registered)
- **PROMOTE to provisional** iff: (a) resolved by L1 or L2; AND (b) resolved
  by I1+I2+I3 (both-hold with a stated conditioning/allophony status, or
  01="est" shown to cost 59 nothing); AND L3, L4, L5 hold; AND ≥2
  independent legs among {L1,L2,L3,L4,L5} pass (independent = different
  cipher cells or cipher-internal vs corpus-external); AND red-team sign-off
  (kill authority — this verdict is a recommendation, not a merge).
- **HOLD at strong lead** iff S4 or the 01-interaction remains genuinely
  unresolved after the battery.
- **DEMOTE** iff any core leg (S1/S2/S3) is destroyed by the corrected
  reading (diplomatic rates or joint-unigram).

## Method notes
- Canonical parse: repaired 1,847-pair (`code/side-keyhunt/repaired_offsets.json`);
  positions per `code/crowd4/REINDEX.md`; cite corrected lists from
  `code/crowd7/redteam/verify_f26_17.py` (61/61 PASS, supersedes NOTES.md).
- Corpus: French files only (Allgemeine Zeitung is German — excluded from
  French rates). Elision-split tokenization ("c'est"→c'/est etc.);
  word-space rates per round-4+ rule (era word-space legs survive; no
  syllable-conditionals on fragments).
- No new claims merged without red-team ruling. Report note at
  `code/crowd7/report_inbox/closer-59-est.md`.
