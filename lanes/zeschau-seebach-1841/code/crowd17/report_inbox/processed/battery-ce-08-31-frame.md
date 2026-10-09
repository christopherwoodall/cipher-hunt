# Battery report: ce-08-31-frame

- Target id: `ce-08-31-frame`
- Claim: test "87 08 31" @1488 as "ce"+[word] vs standalone-08; discriminates 08's word status independent of the 80 frame.
- Date: 2026-10-09
- Worker: battery worker (session 5e9fa0cd-cbc2-4a90-abdb-98f8227ee766)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "word-internal" = a cipher number that is a letter inside a word, not a word itself. "word-initial letter" = the first letter of a word. "standalone" = the number is a whole word. "battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, from battery-queue.json)

"Bar: test "87 08 31" @1488 as "ce"+[word] vs standalone-08; discriminates 08's word status independent of the 80 frame."

## Numbered pass/fail clauses (pre-registered before testing)

1. **C1:** "ce"+[word] parses at battery grade at the locus — 87=ce (determiner) + a word composed [08][31]… with 08 word-internal (word-initial letter), zero new assumptions.
2. **C2:** standalone-08 fails at battery grade at the locus — no window forces 08 as a word; a standalone 08 contradicts the adopted `stem-08-letter-probe` PROMOTE under §7.
3. **Verdict rule:** promote iff C1 and C2 both pass; fence with stated cause if undecidable.

Adverses listed: none.

## Method

1. Read `BATTERY-PROTOCOL.md` first. Created `code/crowd17/next-token/locks/ce-08-31-frame.lock` on start (agent id + UTC timestamp); no stale lock pre-existed.
2. Re-derived the repaired stream in-session byte-exact per `repair_parse.py`. All @-offsets below are 0-based. The brief's "@1488" is 1-based; the trigram sits at 0b@1487–1489 (87@1487, 08@1488, 31@1489).
3. Adopted, never re-litigated: `stem-08-letter-probe` PROMOTE (2026-10-09: 08 word-internal; three letter contacts segmentally licensed; C2 kill-grade scan found no forced-standalone window; sole standalone rescue 08='on' kill-grade dead under the on-08-homophony KILL), 87=ce (promoted/granted), 46=que (pencil GT), 84=on (A15), `fin24-1486-parallel` PROMOTE ("que l'on [24-fin]" forced at @1486), §7 (67 et/veut sole true polyvalence).
4. Verified the three letter-probe contacts byte-exact in-session: @60 (`41 [08] 34 29` — 08→34='i'), @922 (`74 40 [08] 65 71` — 40='e'→08), @944 (`50 40 [08] 62 98` — 40='e'→08). Census re-derived: n(08)=18, confirmed.

## Window-level evidence

### Locus — 0b@1487–1489, row a7_10

`…82 16 98 62 | 46(que) 77 84(on) 24 [87=ce] [08] [31] 92 39 24 00 66 15…`

The wider clause is the `fin24-1486-parallel` frame: "que l'on [24-fin] ce [08] [31] [92] [39]…". Trigram "87 08 31" is **1× stream-wide**; bigram "08 31" is **3×** (@881: `17('fois') 08 31 79`, @1488: `87('ce') 08 31 92`, @1520: `67('et/veut') 08 31 24`).

### C1 — "ce"+[word] — PASS

- 87=ce is a granted/promoted free word; at the locus it takes the determiner arm ("ce" + following NP), the same arm licensed battery-wide ("ce [78-N]" ×2, `det-87-644-function` PROMOTE).
- 08 is word-internal per the adopted letter-probe verdict; at the locus it fills the **word-initial-letter** slot of a word whose second syllable is 31: [08][31]…. This keeps 08 word-internal — no new premise, no §7 conflict.
- The composition is uniform across the three "08 31" windows: after promoted 'fois' (@881: "fois [08][31]"), after 'ce' (@1488: "ce [08][31]"), after 'et/veut' (@1520). At @1520 the positional rule puts 67='et' (follower 08 is not infinitive-shaped), giving "et [08][31]" — conjunction + word, same composition. Parallel determiner geometry at @1592 ("47('ce'-allophone) 08 81"): "ce [08][81]…".
- No French grammar is violated: "ce" + nominal/adjectival word is the standard determiner frame. The clause reads "…que l'on [24-fin] ce [08-31-word]…"; under the conditional 24='faire' lead this is "que l'on fait ce [X]" — grammatical, noted as consistency only (24's value open, not a premise).

### C2 — standalone-08 fails — PASS (arm dead at battery grade)

- A standalone-08 reading ("ce [08-word] [31]") requires 08 to be a word. The adopted `stem-08-letter-probe` PROMOTE names 08 word-internal with a kill-grade scan finding **no window that forces a standalone reading**; its sole standalone rescue (08='on') is kill-grade dead. Under §7 (67 sole polyvalence), a word-internal 08 cannot also stand as a word.
- In-session re-derivation of the full 18-window 08 census confirms the premise holds at this window too: no window in the profile forces standalone (all non-contact neighbors are open-class; the three letter contacts are the only single-letter adjacencies).
- Leftward fusion ("ce"+"08" as one word) has no license: 87=ce is a promoted free word, not a bound prefix; "c'est" requires 59, absent.

## Per-clause pass/fail

1. **C1 — PASS.** "ce"+[word] parses with zero new assumptions under standing values.
2. **C2 — PASS.** standalone-08 is battery-grade dead (adopted letter-probe PROMOTE + §7); nothing at the locus rescues it.

## Verdict: PROMOTE (reading-level)

"87 08 31" at @1488 = **"ce" + [word]**, with 08 as the word's initial letter (word-internal), not a standalone word. This discriminates 08's word status independent of the 80 frame, as chartered.

## Scope and caveats

- Reading-level only: 08's letter value and the [08][31]-word's identity stay open; no value named. 08's global word-internal status (letter-probe) is adopted, not re-decided here.
- The `x29-80-1322-det` fence (08 resists standalone-nominal at @1322) is consistent with this result, not duplicated by it — this battery tests the determiner-frame geometry ("ce X"), a different host.
- The `wordint-08-62-word` follow-up ("08 62" as one noun at @1323–1324) tests the same word-internal family at a different locus; untouched here.
- Canonical-stream caveat stands (row a7_10 offset unvalidated).

## Follow-ups

Promote needs none per §4. One narrow continuation is already queued (`wordint-08-62-word`, P3) and needs no re-proposal. No new follow-ups proposed.

## Bookkeeping

- Queue: `ce-08-31-frame` → `status: verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/ce-08-31-frame.lock` created on start, deleted on completion (verified below).
- R5005, sealed gates, red-team adjudication queue untouched. No standing/red-team verdict contradicted or downgraded; §7 intact.
