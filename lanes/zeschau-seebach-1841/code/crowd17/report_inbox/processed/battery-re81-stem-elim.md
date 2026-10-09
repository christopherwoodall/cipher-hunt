# Battery report: re81-stem-elim

- Target id: `re81-stem-elim`
- Claim: Eliminate candidate 81 stems (tour/pas/gard/met/ven/part) across all six 55-81 windows with the 81="prin" kill intact.
- Date: 2026-10-09
- Worker: battery worker (subagent a5c4c2cb-ba37-4870-bb61-471dd62a7558)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-session and asserted). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/re81-stem-elim.lock` created 2026-10-09T14:36:00Z (no pre-existing lock for this id); deleted on completion.
- Offset convention: @n = 0-based pair index in the repaired stream.

## Bar (verbatim, pre-registered)

"Kill 55="re" iff no stem survives any window, or name the surviving stem for a re-test."

## Numbered pass/fail clauses (restated before testing, not modified after)

- **C1:** Test all six stems (tour/pas/gard/met/ven/part) at all six "55 81" windows (@25/@523/@550/@1085/@1094/@1671, 0-based; byte-confirmed n("55 81")=6, matching `class-55-det`'s locus list). A stem "survives" a window iff "re"+stem forms a grammatical 1841-French word that parses in the window under standing (§7) values with zero unstated assumptions. Parses needing assumptions are graded STRAINED, not surviving.
- **C2:** KILL 55="re" iff no stem survives any window; otherwise name the surviving stem(s) for a re-test (no kill).
- **Adverse:** 81="prin" kill intact — no "prin" reading proposed at any window.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/re81-stem-elim.lock` on start (agent id + UTC timestamp); no pre-existing lock for this id.
2. Re-derived the repaired stream in-session; verified 1,847 pairs / 96 types.
3. Byte-confirmed all six "55 81" windows with ±8 context and standing registry values.
4. Adopted (never re-litigated or downgraded): §7 standings; `seg-55-61-21-stem` PROMOTE (55 word-internal "prend"-stem at the "55 61" windows); `class-55-det` KILL (determiner-55 dead); `ce-inf-1841` KILL ("47 33" fenced as ce+verb contact residual); `nom-97-526-adverb` PROMOTE (81 nominal at @524, window-level parse premise); `nom97-525-inf-rival-kill` KILL (nominal "55 81" NP in subject slot at @523; NOM-97 clean); `adj-78-fence` (78-adjective fenced); R19-123 (global noun-81 fence stands; "le [81]" x3 window-level granted).

## Stem inventory (lexical pre-check)

| 81 stem | "re"+stem | 1841 French word? |
|---|---|---|
| tour | retour | yes — m. noun, "return" |
| pas | repas | yes — m. noun, "meal" |
| gard | regard | yes — m. noun, "look/gaze" |
| met | remet | yes — 3sg present of *remettre* |
| ven | reven | **NO** — not a French word in any era (*revenir/revenant/revenu* are all longer) |
| part | repart | yes — 3sg present of *repartir/répartir* |

- **ven is DEAD globally at kill grade** with stated cause: "reven" is not a lexical item. No window's follower (00/97/00/00/06/92) completes "reven…" into a longer word under the fixed "55 81" = word hypothesis. Excluded from per-window tests.

## Window-level evidence

### W1 @25 (a1_00)
`17(fois) 64(qui) 98(verb) 82(m) 43(noun) 29(er) 47(ce) 33(INF) [55 81] 00(pour) 34(i) 24 30(pas) 03(verb-stem) 64(qui)`
- "47 33" is fenced (`ce-inf-1841` KILL: "ce"+verb contact residual, unparseable under 33=verb).
- Verbs (remet/repart): no licensed subject — "ce 33" is fenced, 98 is verb-class and cannot be subject. DEAD.
- Nouns (repas/regard/retour): "ce 33 [noun]" — double nominal head against a fenced left edge. DEAD.
- **All stems DEAD at W1.**

### W2 @523 (a3_00) — survival locus
`87(ce) 77(le) 80 09 70(pre) 91 77(le) 06(ent) [55 81] 97 47(ce) 44 59(est) 37 64(qui) 26(noun) 32(verb)`
- Standing parse: "55 81" = nominal NP occupying the subject slot (`nom97-525-inf-rival-kill` KILL, C1); 81 nominal at @524 (`nom-97-526-adverb` PROMOTE); NOM-97 clean.
- Left edge "06(ent) | [55 81]" is a clean word boundary (06 word-final bound ending); the standing parse opens the nominal unit at 55.
- Nouns repas/regard/retour (all masculine): class-compatible with the standing nominal parse; zero unstated assumptions. **SURVIVE.** (Survival is inherited from the standing parse — discriminating *repas* vs *regard* vs *retour* needs 97's value and is re-test venue.)
- Verbs (remet/repart): contradict the standing nominal-"55 81" parse. DEAD at W2.
- Tension noted, not a downgrade: the "re"-prefix rival re-opens 81's word-internal status at @524 (the adverb verdict tested adverbial-vs-nominal only), and 55="re" (55-81) vs 55="prend"-stem (55-61, `seg-55-61-21-stem`) is §7 polyvalence → red-team venue. Neither standing verdict's queue entry is touched.

### W3 @550 (a3_01)
`48(e) 42(noun) 06(ent) 00(pour) 46(que) 24(verb) 47(ce) 46(que) [55 81] 00(pour) 86(INF) 59(est) 34(i) 17(fois)`
- Frame "ce que [W] pour [86-INF]": verbs lack a subject ("que" as relative/complementizer cannot supply one); nouns ungrammatical after "ce que". **All stems DEAD at W3.**

### W4 @1085 (a6_05)
`77(le) 78(ver) 64(qui) 06(ent) 52 89(noun) 24(verb) 02 [55 81] 00(pour) 33(INF) 79(tout) 80 06(ent)`
- Frame "24(verb; R24 finite/modal, follower 02≠85) 02 [W] pour [33-INF]".
- Nouns: parse needs 02 determiner-shaped ("[verb] [det] [noun] pour [INF]") — 02 unvalued. STRAINED (1 unstated assumption).
- Verbs: parse needs 02 as subject NP ("[02] remet pour [INF]") — 02 unvalued. STRAINED (1 unstated assumption).
- **No clean survival at W4; strained parses only.**

### W5 @1094 (a6_06)
`81 00(pour) 33(INF) 79(tout) 80 06(ent) 43(noun) 07 [55 81] 06(ent) 29(er) 67 86(INF) 52 82(m) 94(ne) 74`
- Right edge "[W] ent er": 06="ent" is a bound 3pl ending and cannot follow a complete word; "enter" (06+29) is not French. **All stems DEAD at W5 regardless of left edge.** (Consistent with the standing "[81]ent" 3pl hostile fence at @1096, red-team venue.)

### W6 @1671 (a8_05)
`22 94(ne) 84(on) 64(qui) 06(ent) 91 11(la) 78(ver) [55 81] 92(verb) 60 03(verb-stem) 39(a/à) 74`
- Frame "la(11, pencil GT, feminine) 78(ver) [W]": the noun stems are all masculine → gender clash under the DET reading ("la [78] [W]"); "la 78" as DET+N leaves W a second noun (ungrammatical); "la" as object pronoun is blocked by intervening 78. Nouns DEAD.
- Verbs: "la 78 [remet]" — DET+78+finite verb ungrammatical; pronoun-"la" blocked by 78. DEAD.
- **All stems DEAD at W6.**

## Per-clause pass/fail

- **C1 — PASS.** All 36 stem×window tests executed (ven excluded globally as a non-word, stated cause above).
- **C2 — kill arm does NOT fire.** Three noun stems — *repas*, *regard*, *retour* — survive cleanly at W2 (@523) under the standing nominal-"55 81" parse. Named for re-test: the three masculine-noun stems (class-identical; discrimination is re-test venue).
- **Adverse — ANSWERED.** No "prin" reading proposed at any window; the 81="prin" kill is untouched.

## Verdict: NULL

55="re" is not killed: the noun stems survive at W2. It is not promoted: §7 bars 55="re" (55-81 windows) alongside the standing 55="prend"-stem (55-61 windows) at battery grade — the polyvalence question is red-team venue.

## Follow-ups (all verified ABSENT from battery-queue.json)

1. `re81-W2-noun-discrim` (P3) — discriminate *repas*/*regard*/*retour* at W2 (@523); needs 97's value and the "91 77 06" left-context parse; 55's class stays red-team venue.
2. `re81-W4-02-class` (P4) — name 02's class at W4 (@1085, "24 02 [55 81] pour"); determiner-02 gives the noun stems a second leg, subject-02 gives the verb stems a leg.
3. `redteam-55-class-input` (P2) — evidence package for 55's class: "prend"-stem word-internal (55-61 ×3, `seg-55-61-21-stem`) vs "re"-prefix (55-81 ×6, this report) vs determiner hypothesis (`class-55-det` KILL); gather only, red team decides.

## Bookkeeping

- Queue: `re81-stem-elim` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock created on start, deleted on completion. R5005, sealed gates, red-team adjudication queue untouched. No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands.
