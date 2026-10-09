# Battery `noun-49-nonchain` — verdict: PROMOTE (fence executed, bar's else-arm)

- Target: `noun-49-nonchain` (battery-queue.json, priority 3, status queued → verdict)
- Claim: "test noun-49 at the non-chain windows (@653/@990 '76 49 24 26 30 03' x2, @909 '54 49 qui', @875, @1433) where 74 is not adjacent"
- Worker: a80cf7af-79e8-4831-87b7-35a6d9f4bf4a. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/noun-49-nonchain.lock` created on start (no prior lock; no stale lock); deleted on completion.

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"name noun-49 iff >=2 windows parse with zero new assumptions; else fence noun-49 globally"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name arm):** >=2 of the five named windows (@653, @990, @909, @875, @1433) parse with 49 as a noun, using zero new assumptions — i.e. standing values/grants only, plus the hypothesis under test (49=noun). An "unstated/new assumption" is anything the parse needs that is not a standing value/grant or the hypothesis itself.
2. **C2 (else arm):** fence noun-49 globally.

## Adopted premises (not re-litigated)

- 76 = masculine noun (promoted R19); 24 = finite/modal verb at @653/@990 (R24: follower 26 ≠ 85); 46='que' (GT); 36 = noun class (R18); 64='qui' (promoted); 59='est' (provisional).
- 49's global kills stand: verb, determiner, relative/interrogative pronoun (`formula-49-value` null); adjective killed at kill grade (`adj-49-420-366`, 2026-10-09); adverb fenced at the "[N] [49] [Vfin]" geometry (`adv-49-653-990`, 2026-10-09).
- 54, 74, 16 unvalued; 74's class open (`noun-74-census` null, `noun-74-formula` null; 74 as negated verb killed in `ne-alone-02-74`).
- §7: 67 is the sole true polyvalence — no second class declared here.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed all five loci and their ±4 context; censused n(49)=12 stream-wide.
3. For each window, enumerated the grammatical routes for 49-as-noun and counted the minimum new assumptions each route needs under standing values.

## Window-level evidence (byte-exact, 0-based pair indices)

n(49) = 12 stream-wide: @366, @416, @420, @653, @815, @860, @875, @909, @918, @990, @1433, @1844.

| window | row | ±4 context (49 bracketed) |
|--------|-----|---------------------------|
| @653 | a4_02 | `52 82 94 [76 49 24] 26 30 03` |
| @990 | a6_01 | `89 48 01 [76 49 24] 26 30 03` |
| @909 | a5_09 | `18 55 83 [54 49 64] 83 59 37` |
| @875 | a5_08 | `89 48 20 [74 49 16] 77 86 78` |
| @1433 | a7_08 | `61 12 16 [76 49 64] 52 82 16` |

Adverse window @420 (row a2_08): `49 74 74 46 [49] 36 29 47 14` — i.e. "…46(que) [49] 36…".

## Finding (framing correction, recorded before clause results)

The claim lists @875 among windows "where 74 is not adjacent". In the repaired stream @875 is `74 49 16` — **74 IS adjacent** (immediately left of 49). The claim mislabels this window. It is tested below anyway as named; the mislabel does not change the clause results.

## Clause results

**W1 @653 — FAIL.** Standing parse: `[76 N-masc] [49] [24 Vfin]`. 49 as noun gives "NOUN NOUN Vfin" — ungrammatical in 1841 French; no licensed apposition/compound frame exists under standing values. 0-assumption parse: none. (Reading-independent under standing classes; kill-grade exclusion of noun-49 at this window.)

**W2 @990 — FAIL.** Byte-identical geometry to W1 (`76 49 24`, same standing classes). Same exclusion. 0-assumption parse: none.

**W3 @909 — FAIL.** `54 [49] 64=qui`. The only noun-49 route is "[54-det] [49-N] qui…" — 54 is unvalued (n=3 stream-wide; prev {45,93,83}, next {88,64,49}), so naming 54 a determiner/host is 1 new assumption. No 0-assumption parse.

**W4 @875 — FAIL.** `74 [49] 16`. 74's class is open and 16 is unvalued; the noun-49 route needs 74 as a determiner/preposition-class host — 1 new assumption. (The adjective-49 route is unavailable: adjective-49 is dead at kill grade.) No 0-assumption parse.

**W5 @1433 — FAIL.** `[76 N-masc] [49] [64=qui]` — "NOUN NOUN qui": 76 is banked as masculine noun (R19), so 49-as-noun sits noun-adjacent to a noun with no license. 0-assumption parse: none. (Reading-independent; kill-grade exclusion.)

**C1: FAIL — 0 of 5 windows parse with zero new assumptions** (name arm needed >=2).

**C2: FIRES — noun-49 fenced globally.** The fence rests on kill-grade structural exclusions at @653/@990/@1433 (noun-49 ungrammatical under standing classes, reading-independent) plus 0-assumption failures at @909/@875 (each needs a new class assumption about unvalued 54/74). No window among the five — the noun leg's best non-chain shots — supports 49 as a noun.

## Adverses answered

1. **"noun-49 strained at @420 ('que 49 [36-noun]')"** — answered: consistent, resolved by the fence. @420 is "que [49] [36-N]"; a noun-49 there would be "que NOUN NOUN", ungrammatical — the strain was a symptom of the same structural impossibility the fence records. No re-parse needed; the fence is the stated cause.
2. **"adjective-49 dead at kill grade (adj-49-420-366)"** — answered: consistent, no conflict. Adjective and noun are now both down for 49; per the `adv-49-653-990` scope note, 49's remaining viable tier is syllable/letter.

## Scope (explicit)

- Fenced: noun as 49's class, globally — noun-49 is no longer a live hypothesis at any window.
- Untouched: 49's remaining class question (syllable/letter tier) at all windows; no value named; the chain-window verdicts and standing kills (§7) unchanged; the @420 strain stands as recorded above, not re-pronounced.
- No standing or red-team verdict contradicted or downgraded.

## Verdict: PROMOTE (fence executed, bar's else-arm)

Per §4, a fired fence arm regenerates no mandatory follow-ups: none proposed. (Convention follows `adv-49-653-990`.)

Natural next questions (not queued — fence verdict):
- 49's surviving tier is syllable/letter — a letter-49 battery is the natural next naming attempt.
- Queued `noun-49-909-875` (P4) tests the noun leg at @909/@875; this fence moots it — supervisor should re-scope or close it.
- Queued `val-49-61-pair` tests 49's class at @365–367; the noun option there is now fenced (context, not a pronouncement).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-noun-49-nonchain.md` (this file).
- Queue: `battery-queue.json` — `noun-49-nonchain` status `queued` -> `verdict`, result `promote` (fence executed), date 2026-10-09 (pre-write assert confirmed queued/verdictless; temp-file + rename; JSON re-validated post-write; only this entry's keys touched; no downgrade).
- Lock `locks/noun-49-nonchain.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
