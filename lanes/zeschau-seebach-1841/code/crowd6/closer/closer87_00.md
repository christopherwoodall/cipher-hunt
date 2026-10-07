# Round-6 CLOSER: WO-A (84 from the 87-side) + WO-B (00="pour" battery)

Worker: closer_round6 · 2026-10-07 · `code/crowd6/closer/closer87_00.py` +
`closer87_00b.py` · numbers: `closer87_00_results.json` (this file).
Cipher: repaired 1,847-pair parse. Era: Tocqueville t1+t2 elision-split
word model (round-5 convention). F30-legal: word-space legs only.
Status marks: [GT]=pencil crib, [prov]=provisional, [lead]=lead.

## WO-A: what does 87-64-77-84 demand of 84, given 87=ce?

Assumed for the attack (all marked where used): 87=ce [prov],
64=qui [prov], 77=le [prov-CONDITIONED]. 62="on" NOT touched (fenced, N35).

### Re-derived cipher facts
n(84)=25, rank 28/96, P=0.01354. 77→84 ×7 @[145,259,1057,1446,1484,1763,1802],
P(84|77)=7/44=0.1591. 64-77-84 ×3 @[144,1445,1801] (n_eff=1 — one phrase type);
two extend to 64-77-84-59 ×2 @[1445,1801]. 84→59 ×4 (top follower);
46→84 ×2 @[309,472] ("que" [GT]); 94→84 ×1 @1665 ("ne" [prov]);
82→84 ×1 @166 ("m" [GT]); 11→84 ×1 @1620 ("la" [GT]).
Full ±5 windows for all 25: in JSON (`windows84`).

### The constraint
84 must satisfy simultaneously: follows «le»/«qui le» (×7/×3), «que» (×2),
«ne» (×1), «la» (×1), «m'» (×1) — and precedes a finite verb ×4 (59, see below).
Intersection of those classes in French is a singleton: **84="en"**.

### Battery for 84="en" (elision-aware: cipher writes unelided, cf. A1 "c'est"=87-01)
| leg | cipher | era | verdict |
|---|---|---|---|
| E1 unigram | 0.01354 | P("en")=0.01231 | **1.10×** ✅ |
| E2 "qu'en" | P(84\|46)=0.0690 (×2) | P(en\|qu)=0.0507 (n=109) | **1.36×** ✅ |
| E3 "n'en" | 94→84 ×1 | P(en\|n')=0.0536 (n=73) | ✅ common |
| E4 "l'en" | P(84\|77)=0.1591 (×7) | P(en\|l')=0.0011 (n=6) | **141×** ❌ BLOCKING (63× vs Les Mis) |
| E5 "m'en" | 82→84 ×1 | P(en\|m')=0.0160 (n=2) | weak ✅ |
| E6 "qui l'en" | ×3 (n_eff=1) | 0 | weak ❌ (rare construction, not ungrammatical) |

24/25 windows read cleanly as "en" ("l'en [V]", "qu'en [V]", "n'en",
"m'en [V]", "[V] en [N]" ×9 comparatives = "mettre/croire en"-type).
Residual: @146 "qui l'en er" ×1 (fenced).

### Rival kills
- **84="plus" KILLED** (was inconclusive): given 59="est" [lead] below,
  "plus"+"est" is era-~0 ("plus" almost never directly precedes a finite verb:
  3/1505); P(84|77)=0.1591 vs era P(plus|le)=0.0361 = 4.41× over.
- **84="a" KILLED**: "a"+"est" ungrammatical given 59="est"; unigram 2.22× out.
- **84=finite-verb KILLED**: verb+finite-verb ×4, era ~0.
- 84="y": unigram + "l'y"~0. 84="fait": prior kill stands.

### Verdict WO-A
**84="en": LEAD (sole survivor) — promotion BLOCKED on E4.**
Four independent positive legs (E1 rate; E2 GT-anchored bigram; E3 prov-anchored;
E5 GT-anchored) + full rival sweep, but "l'en" at 141×/63× over era is
kill-grade under the standing 77="le" [prov]. The @1800 thread now reads
"ce qui l'en [59]" — corroboration for 87=ce, not proof.
**Not resolved to provisional. Honest partial.**

### Coordination flags for the Bigram Closer (77-side owns these, NOT claimed here)
1. **"s'en" alternative**: if 77 carries a "se"-islet in exactly the 77→84
   frames, E4' = P(84|77) vs era P(en|s') = 0.0589 → **2.70×** (borderline,
   genre-fenceable) instead of 141×. Testing this touches promoted 77="le" —
   needs red-team adjudication; flagged, not claimed.
2. E4/E6 need independent 77-side verification.
3. **84/94 "en"-allophony** (F33-allowed 1-sound→2-groups): "m'en" via 94 ×3
   (the conditioned "en"-islet) AND via 84 ×1 @166 — convergent, like the
   61/78 "ver" allophony (F39). Corroboration, not a leg.
4. **Conflict note (their round-6 note read post-battery):** bigram closer
   grades 84=masculine-NOUN [LEAD-grade, identity NULL] vs my 84="en" [LEAD].
   Their noun fails "ne 84"/"m' 84"/"que 84" (grammatical zeros); my "en"
   fails the "l'en" rate. Candidate resolution for round 7 (untested):
   conditioned polyvalence — 84="en" iff pre∈{46,94,82}, 84=noun iff
   pre∈{77,11} (9/25 predecessors unclassified — needs its own battery).
   Agreement: their 59=verb [LEAD] vs my 59="est" [STRONG LEAD] are
   compatible (mine specific); their 59→37 ×6 = "[c']est le" (S5, 6.47×
   over, conditional on 37="le" [MEDIUM] — fenced).

### Bonus anchor: 59="est" (the "another non-circular anchor")
n(59)=27, rank 24, P=0.01462. Followers/preds: finite-verb profile
("qui"→59 ×3, "ne"→59 ×3, 59→"que" ×2 @[216,1190], "on ne"→59 @761–763).
| leg | cipher | era | verdict |
|---|---|---|---|
| S1 unigram | 0.01462 | P("est")=0.01054 | **1.39×** ✅ |
| S2 "qui est" | 64→59 ×3 | n=83 | ✅ |
| S3 "n'est" | 94→59 ×3 | P(est\|n')=0.2377 (n=324) | ✅✅ |
| S4 "est que" | P(46\|59)=0.0741 (×2) | P(que\|est)=0.0137 | **5.40×** ❌ adverse (murky contexts, fenced) |
Rivals killed on rate alone: doute 44.9×, dit 26.5×, fait 7.3×, veut ~30×,
peut ~7× — "est" the unique rate-survivor.
**Verdict: 59="est" STRONG LEAD** (promotion-ready pending red-team:
S4 adverse + interaction below).
**Interaction flagged (not resolved):** 87→59 ×1 @824 = "c'est" — if 59="est",
then /ɛ/ → {01, 59} allophony with the 01="est" [lead] (F33-allowed), OR
01≠"est" (which would weaken A1's "c'est"-count). Red-team/coordinator call.

## WO-B: 00="pour" battery (F40 lead)

### Re-derived cipher facts
n(00)=55, rank 1/96, P=0.02976. 00→46 ×4 @[106,545,1545,1680] ("pour que"),
P(46|00)=0.0727. **00→86 ×12 vs 00→06 ×0** (M1 governor frame, F40).
06→00 ×4 @[184,544,666,738] ("[V] pour [X]"). 00→11 ×4 ("pour la").
87-11-00 ×3 ("cela pour").

### Battery
| leg | cipher | era | verdict |
|---|---|---|---|
| B1 unigram | 0.02976 | P("pour")=0.00482 (rank 30) | **6.22×** ❌ BLOCKING |
| B2a governor | 00→86 ×12 vs 00→06 ×0 | "pour"+bare-inf | ✅ (M1-ACCEPTED; cond. on 86=inf [prov]) |
| B2b cond. inf | P(86\|00)=0.218 | P(inf\|pour)=0.310 | **0.70×** ✅ |
| B3 "pour que" | P(46\|00)=0.0727 | P(que\|pour)=0.0189 | **3.85×** ❌ adverse (n=4) |
| B4 rivals | — | — | ✅ "pour" unique survivor (below) |
| B5 "[V] pour" | 06→00 ×4 | grammatical | ✅ (cond. on 06=verb-stem [prov]) |
| "pour la" | P(11\|00)=0.0727 | P(la\|pour)=0.0671 | **1.08×** ✅ |

Rival sweep (grammatical, band-free): à/de/en/par/dans/sur/avec killed by
00→46 ×4 ("X que" era-0: à 0/4177, de 1/9151, en 2/2722, par 0/1036);
avant/afin/pendant killed by 00→86 ×12 ("X"+bare-infinitive era-0);
sans killed 11.4× + "sans que" 2.8× over; après killed 49.5×;
**et killed 6.5×** (P(inf|et)=0.034 vs cipher 0.218 — the discriminating leg).
Adverse fenced: "cela pour" 3/7 vs era 0/47 (genre: cipher is cela-dense, F31).

### Verdict WO-B
**00="pour": STRONG LEAD — promotion BLOCKED on B1 (6.22×) + B3 (3.85×).**
The grammatical core is clean (governor frame, conditional rates, full rival
sweep, "pour la" 1.08×); the marginal-rate adverses need the diplomatic corpus
(standing blocker, same as 47="ce"). Shape right, scale wrong.

## Nulls preserved
- 84 NOT resolved to provisional (E4 blocks).
- 00 NOT promoted (B1/B3 block).
- 59=«est» offered as STRONG LEAD, not provisional (red-team gates).
- The "s'en" alternative is flagged untested, not claimed.

## Traceability
Every cipher number recomputed from `code/side-keyhunt/repaired_offsets.json`
+ `data/upstream-ct_R5005.txt` via `code/crowd4/repaired_parse.py` in the two
scripts above. Era: Tocqueville t1+t2 elision-split (round-5 convention);
Les Mis used once as robustness check (E4). JSON: `closer87_00_results.json`.
