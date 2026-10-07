# 67-FINISHER round 10 — residual classification report
**Executor:** finisher67 (WO-5) · **Date:** 2026-10-07
**Package:** `code/crowd10/finisher67/` (PREREG.md timestamped 2026-10-07 20:39:15 UTC,
written before any round-10 computation; `score67_r10.py`; `results_r10.json`)
**Status:** recommendation only — red team adjudicates every status change.

## Verdict: 0 of 6 classified — all 6 stay open-residual

Three ≥2-leg bars were pre-registered (E3, E4, E7; general bar: F0 byte-verify
+ L1 era-conditioned frame + L2 GT-anchored nominal contact, thresholds fixed
at design). **Every bar failed on at least one leg.** No window met the
≥2-leg bar. The 6 open-residuals from round 9 remain open-residual, now with
explicit missing-leg diagnoses below. This is a clean null on the
classification question, not a fork threat: residuals are unclassified, not
counterdata.

## Per-window results

### @1519 (11-91-67-08-31) — bar E3, FAILS on L2; closest call
- L1 (era "et l'" vs "veut l'"): **63:1 PASS** (E_et=63 ≥ 20, E_veut=1 ≤ 3,
  ratio 63 ≥ 10). Single-leg et-lean stands, UNSCORED.
- L2 (cipher nominal): n(11→31) = **1 < 2, FAIL**.
- Adverse observation (not a leg, recorded): n(64→31) = 2 ("qui 31" ×2,
  64="qui" provisional) vs n(11→31) = 1 ("la 31" ×1) — 31 leans verbal, which
  favors the C2 competing parse "veut l'[31-verb]" (the single era "veut l'"
  is exactly "qui veut l'entendre", pronominal-l' + infinitive). The et-lean
  is genuinely contested.
- Contact (unscored): suc=08 shared with @630 (et-CONDITIONAL); pre=91 shared
  with @1372 (open).
- **Missing:** an independent second leg — nominal evidence for 31 at n≥2,
  or resolution of 31's verbal-vs-nominal contradiction, or C1∧C2
  adjudication inputs.

### @1372 (16-91-67-98-00) — bar E4, FAILS on both legs
- L1 (era "et * pour" vs "veut * pour", cond. 00="pour" strong lead):
  E_et=**11 < 20**, E_veut=0 — the "et ? pour" frame is rarer than the bar
  assumed. FAIL.
- L2: n(11→98) = **0, FAIL**.
- Contact (unscored): pre=91 shared with @1519 (open); suc=98 unique.
- **Missing:** both legs — a denser era frame for "X 98 pour" and any
  GT-anchored nominal contact for 98.

### @1450 (59-36-67-33-46) — bar E7, FAILS on both legs
- L1 (era "et * que" vs "veut * que", cond. 46=que GT): E_et=**16 < 20**,
  E_veut=2 (middles: "coûte" ×1, "prouver" ×1 — "veut [infinitive] que" is
  grammatical, so the veut-arm is genuinely alive; ratio 8 < 10). FAIL.
- L2: n(11→33) = **0, FAIL**.
- Contact (unscored): suc=33 census {et:3 (@272,@1148,@1476 — all R_et1
  pre-confounded), veut:1 (@1423, R_veut1), open:1 (@1623)} — mixed,
  tracks pre-side rules, not a leg (design-time exclusion upheld).
- **Missing:** 33's class is the decider — if 33 is an infinitive the
  veut-arm lives ("veut prouver que"); if nominal, et is favored. Also
  36's reading for a pre-side frame.

### @1623 (78-66-67-33-46) — bar E7, FAILS identically to @1450
- Same L1 (16 vs 2) and L2 (0) numbers — same frame "X 33 que".
- Contact (unscored): suc=33 census as @1450 (mirror).
- **Missing:** same as @1450 (33's class); 66-class is confirmed but yields
  no conditionable frame here.

### @633 (08-52-67-63-74) — design-time null, confirmed isolate
- No ≥2-leg bar designable (PREREG): 52/63 unread; no era-conditionable
  frame. Census: pre=52 and suc=63 are both unique across all 67 windows —
  total contact isolate. The 11→52 ×3 nominal contact is a single leg with
  no independent second.
- **Missing:** a board-grade reading for 52 or 63, or any second leg.

### @902 (16-92-67-16-88) — design-time null, confirmed isolate
- No ≥2-leg bar designable (PREREG): era frame blocked ("i"-as-word for 16
  unestablished — the n("et i")=n("veut i")=0 observation cannot fence
  without it); 92 unread. Census: pre=92 and suc=16 both unique — total
  isolate.
- **Missing:** 92's class, or establishment of 16 as the word "i" (which
  would make an N1-style NEITHER bar designable).

## @1248 counterdatum — weight ruling

- Standing (F67, adjudicator GRANT): @1248 "pour 67 que" NEITHER-fence
  UPHELD; new arm declined with evidence ("pour * que" middles {cela:3,
  empêcher:1}, no single-syllable X with era support; finite-verb arm
  vetoed by frenchman Gate 4).
- **This executor ran no new-arm census at @1248** — WO-4 (arm-builder) owns
  that work; no duplication. (Note: `code/crowd10/` did not exist when this
  work began; no arm-builder artifacts were present to coordinate with —
  the window was left untouched per the work order.)
- **Weight ruling:** @1248 is fenced n=1 with both fork arms era-zero and no
  era-supported new arm. Its weight against the fork is **scope amendment
  only, not refutation**: the fork claim is conditioned on the fenced set,
  and a genuine fenced exception bounds the claim rather than breaking it.
  If WO-4's arm-builder produces a ≥2-leg non-finite arm (cela/peu-class
  or infinitive per Gate 4), the fork re-scopes per that bar; until then the
  fence holds. 62-WO3 blocker carried forward (no 62-interaction found).

## Fork scope verdict (unchanged)

Fork stays **SUPPORTED with amended scope (fenced n=2)**: 36 in-scope
windows = 29 classified (et 18 / veut 11) + @630 et-CONDITIONAL(C1∧C2) + 6
open-residual; 2 fenced out (@1248 NEITHER, @199 NEITHER-conditional-on-08).
Round 10 adds no classifications, no new fences, no scope change. The six
residuals are absence-of-bar, not counterdata — the bar held a ninth round.

## Files
- `code/crowd10/finisher67/PREREG.md` — pre-registered bars, design-time
  nulls, @1248 weight ruling (timestamp 2026-10-07 20:39:15 UTC)
- `code/crowd10/finisher67/score67_r10.py` — implements exactly the
  pre-registered bars; era tokenizer vendored from round-9 scorer
- `code/crowd10/finisher67/results_r10.json` — F0 byte-verifications
  (6/6 pass), era frame counts, L2 contacts, bar outcomes, unscored
  contact census
