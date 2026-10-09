# Battery report: det-55-1206

- Target id: `det-55-1206`
- Claim: test 55's class at @1206 (1-based; 0-based @1205); a non-verbal (article/determiner-shaped) 55 re-opens "55 premier [21-N]" as a prenominal-adjective frame.
- Date: 2026-10-09
- Worker: battery worker (subagent f4ef662d-65ef-4bb2-8ef6-35797784cf8c)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-session and asserted). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"class named at battery grade"

## Numbered pass/fail clauses (restated before testing, not modified after)

- **C1:** 55's class is named at battery grade at the locus (0-based @1205, 1-based @1206) with byte-exact evidence.
- **C2:** If the named class is non-verbal (article/determiner-shaped), the "55 premier [21-N]" prenominal-adjective frame re-opens with a stated licensed parse under standing values.

Verdict rule: **promote** iff all clauses pass and all listed adverses are answered. **kill** iff a clause fails at kill grade or a cleaner rival is demonstrated. **null** otherwise (with 1-3 follow-ups).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/det-55-1206.lock` on start (agent id + UTC timestamp); no pre-existing lock for this id.
2. Re-derived the repaired stream in-session; verified 1,847 pairs / 96 types.
3. Byte-confirmed the locus and re-ran the distributional test independently.
4. Adopted (never re-litigated or downgraded) the standing verdicts: `seg-55-61-21-stem` PROMOTE (2026-10-09, discriminator success: 55-61 = bare finite stem "prend" + noun object at @1205), `class-55-det` KILL (2026-10-09: determiner-shaped particle claim killed at kill grade, clause 2 forced false at W3 = this locus), `premier-61-flank-census` NULL (2026-10-09: @1206 EXCLUDED from 'premier'-admission — prenominal "premier [21-N]" needs a determiner and 55 is verb-class).

## Window-level evidence

### The locus — 0-based @1205 (1-based @1206), row a7_00

Byte-exact ±6: `1199=64(qui) 1200=29(er) 1201=45 1202=58 1203=47(ce) 1204=43 | 1205=55 1206=61 1207=21(N) | 1208=65(N) 1209=64(qui) 1210=59(est) 1211=32 1212=48(e) 1213=96(par) 1214=45`

Full-context parse (adopted from standing `seg-55-61-21-stem`, re-verified byte-exact): "[58] ce(47) [43] prend(55-61) [21-N] — [65-N] qui(64) est(59) [32]e(48) par(96) [36]…"
- "prend" = 3sg present of *prendre*, agreeing with subject "ce [43]".
- 21 = direct object, noun class (R18).
- The missing 94 (cf. the sibling "55 61 94" windows @576/@1167) was accounted for by the parent: finite "prend" appears where the clause has no subjunctive trigger.

### C1 — class named at battery grade: PASS (verb)

- The verb-class reading is the standing battery promote at this exact locus; the discriminator bar passed all three clauses on 2026-10-09.
- The only rival class with any battery-grade legs is determiner-shaped — and it is KILL-grade dead at this window: `class-55-det` clause 2 fails at kill grade because W3 (@1205) forces 55 word-internal under the promoted "prend(55-61)" discriminator, and §7's sole-polyvalence rule bars a separate-at-11 / word-internal-at-1 split at battery level. (Clause 1 of that bar also failed: only 1 clean pre-noun slot of the required >=2.)
- Distributional check re-derived in-session: n(55)=12; successors {81 x6, 61 x3, 83 x2, 68 x1}; the three "55 61" windows (@576, @1167, @1205) all sit in verb-compatible frames; none supplies a fresh article-shaped leg the kill bar did not already test and fail.
- No new byte evidence since the standing verdicts alters the picture: `val-61-premier` (locus-level only, global kill stands) and `premier-61-flank-census` do not touch 55's class; nothing in the 55 profile contradicts the verb reading.
- No standing/red-team verdict contradicted or downgraded. §7 intact.

### C2 — re-open condition: DOES NOT FIRE

The named class is verbal, so the conditional's antecedent is false — the re-open does not fire. Two independent fences make this decisive:

1. **55's side:** an article/determiner-shaped 55 at @1205 is kill-grade dead (class-55-det). Under §7, the battery cannot hold "prend(55-61)" verb and article-55 at the same window.
2. **61's side:** even if 55 were re-opened, the re-open needs 61 = "premier" as the middle term — and `premier-61-flank-census` EXCLUDED @1206 from 'premier'-admission (1 admitted @1556, 1 flank-supported @645, 15 excluded). The "55 premier [21-N]" prenominal-adjective frame is closed from both ends.

Additionally, the article route has no licensed NP shape at this window under standing values: left context is "ce(47) [43]" — 47='ce' is a granted determiner/demonstrative, and a second article 55 directly after "ce [43]" would give an ungrammatical double-determiner NP ("ce [43] [article] [adj] [noun]"). The finite-verb parse is the only licensed reading.

## Adverses

None listed. Adopted-premise check: `val-61-premier`'s locus promote does not propagate to @1206 (explicitly locus-level); the canonical-stream caveat stands (row a7_00 offset unvalidated).

## Verdict: PROMOTE

All bar clauses pass; no adverses. Scope: the `det-55-1206` question is closed — 55's class at @1206 is verb-class at battery grade, and the "55 premier [21-N]" prenominal-adjective re-open does NOT fire. No new class or value is declared; this verdict confirms the standing `seg-55-61-21-stem` promote and `class-55-det` kill at this locus.

## Supervisor note (not a finding, no follow-up queued per §4)

`class-55-det`'s observation stands: the 11-vs-1 segmentation tension (separate-word 55 at eleven windows vs the promoted one-word "prend" at W3) is a positional-polyvalence-shaped tension between two standing battery verdicts. If the red team ever declares a second polyvalence or a positional segmentation rule, the '55 81' x6 determiner-shaped legs (@550 clean, @1094 left-licensed) are the live evidence. Red-team venue; no battery action.
