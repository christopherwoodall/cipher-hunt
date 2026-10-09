# Battery `val-49-74-frame` — verdict: NULL (fence executed)

- Target: `val-49-74-frame`
- Claim: "name 49 via its dominant "49 74" x5 frame (@416/@815/@860/@918/@1844); 49 value is the keyhole for both this boundary and the queued frame-367-la-pre"
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/val-49-74-frame.lock` (created at start 2026-10-09T15:40:32Z, no prior lock; deleted on completion).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"name 49 value iff >=2 of the five windows parse under one value with zero new assumptions; else fence"

## Numbered pass/fail clauses (restated before testing, not modified after)

1. **C1 (name arm)** — one value of 49 parses ≥2 of the five windows with zero new assumptions (standing values/grants only, plus the hypothesis under test).
2. **C2 (fence arm)** — else the naming claim is fenced at the five windows.

## Adopted premises (not re-litigated)

- 49 is class-open: verb, determiner, relative/interrogative pronoun dead at kill grade (`formula-49-value` NULL); adjective dead at kill grade (`adj-49-420-366` KILL). Surviving: noun (strained), adverb (strained). R20-080 fenced `formula-76-49-24` after the adjective leg died.
- 74 is class-open; the '74 74' doubling (×6) contradicts every whole-word class at kill grade — no noun, verb, adjective, pronoun, adverb, or determiner doubles adjacently in French prose (`noun-74-census` NULL/fence, `noun-74-formula` NULL). The four '49 74 74' chains' nominal-head and formula readings both FAIL at kill grade (`noun-74-formula`).
- Standing values: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (GT pencil); 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce (granted); 59=est, 77=le (provisional); 78='ver' lead; 94='ne' strong lead; 83='de' conditioned lead; 24=en/finite-modal (R24); 65=noun (R20-047); 36=noun (R18); 76=masc noun (R19); 48='e' letter-tier (F86); 93=verb-class (R19).
- §7: 67 is the sole true polyvalence; 67="veut" iff follower infinitive-shaped. Canonical-stream caveat stands.

## Method

Byte-exact extraction of the five "49 74" windows (±6) from the repaired stream. For each window, tested whether a single 49 value under either surviving class (noun, adverb) parses the window using standing values only. A parse that requires 74's class/value is a new assumption (74 unvalued, letter-tier ungranted). The standing kill-grade doubling finding applies to all four chain windows.

## Window-level evidence (byte-exact, 0-based)

| # | pos | row | window |
|---|-----|-----|--------|
| W1 | @416 | a2_08 | `02 53 84 51 37 78 [49] 74 74 46 49 36 29 47` |
| W2 | @815 | a5_05 | `12 48 24 65 14 29 [49] 74 74 47 78 40 95 13` |
| W3 | @860 | a5_07 | `64 32 48 84 02 24 [49] 74 74 48 47 46 00 86` |
| W4 | @918 | a5_09 | `59 37 96 09 02 24 [49] 74 74 40 08 65 71 17` |
| W5 | @1844 | a8_11 | `42 44 83 21 67 78 [49] 74 93` (row-final; stream ends @1846) |

Resolved with standing values:

- **W1**: `…on [51] [37-pred] [78-ver] 49 74 74 que 49 [36-noun] er ce` — 84=on, 46=que GT, 36=noun, 29=er, 47=ce.
- **W2**: `…[48-e] en [65-noun] en er 49 74 74 ce [78-ver] e…` — 48='e' letter, 24=en (R24: follower 65≠85 → here 24@814 has follower 49≠85, so finite/modal verb), 65=noun, 14='en', 29=er, 47=ce.
- **W3**: `qui [32-pred] [48-e] on 02 en 49 74 74 [48-e] ce que pour [86]` — 64=qui, 84=on, 24@865 finite/modal (follower 49≠85), 46=que, 00=pour.
- **W4**: `est [37-pred] par [09] 02 en 49 74 74 e [08] [65-noun] [71] fois` — 59=est prov, 96=par, 24@922 finite/modal (follower 49≠85), 40=e GT, 65=noun, 17=fois.
- **W5**: `[42-noun] [44] de [21] et [78-ver] 49 74 [93-verb]` — 42=noun, 83='de' conditioned lead, 67="et" (follower 78 not infinitive-shaped), 93=verb-class.

## C1 test — value naming

**Noun-49.** In W1–W4 the frame is "49 74 74". Two identical adjacent content words are ungrammatical in French prose at kill grade (standing finding), so "49-N 74 74" fails at all four chain windows independent of the noun chosen. The only rescue is 74 at sub-word (letter/syllable) tier — ungranted, a new assumption, which the bar forbids. At W5 ("78 49 74 93"), 74's class is open and 93's value is deferred (R20); naming 49 there requires 74's role — again a new assumption. Zero windows parse under noun-49 with zero new assumptions.

**Adverb-49.** "49-adv 74 74" faces the identical doubling blocker in W1–W4; at W5 the same 74-role assumption is needed. Zero windows parse.

**Result: C1 FAIL.** No value of 49 parses even one window under the bar's terms, let alone two. The blocker is structural (the '74 74' doubling + 74's open class), not value-specific: no candidate value can clear it without a new assumption about 74.

## C2 test — fence

C1 fails; the bar's else-arm fires. The "name 49 via the '49 74' x5 frame" claim is fenced at all five windows. This fence is consistent with and narrower than the standing fences: `formula-49-value` (49 class-open), `noun-74-formula` (chain readings dead), `noun-74-census` (74 class-open). Nothing about 49's class elsewhere, 74's value, or the queued `unit-49-74-74` word-unit reading is decided here.

**C2: FIRES.**

## Verdict: NULL

The bar's naming arm is untestable-as-satisfiable: the '74 74' doubling is a kill-grade blocker for any whole-word parse of the chains, and 74's class is open, so no 49 value can parse ≥2 windows with zero new assumptions. Fence executed per the bar. No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands.

## Adverses

- None listed on the target.

## Follow-ups proposed (nulls regenerate work; all three verified ABSENT from battery-queue.json)

1. `val-74-letter` (P3): test 74 as a letter cell — the doubling kill is scoped to whole-word 74; a letter reading (doubled "ss"/"ll"-type) would dissolve '74 74' at all 6 windows. Bar: name the letter with byte evidence (collocation profile à la 40='e') or fence letter-74.
2. `noun-49-nonchain` (P3): test noun-49 at the non-chain windows (@653/@990 "76 49 24 26 30 03" ×2, @909 "54 49 qui", @875, @1433) where 74 is not adjacent. Bar: name noun-49 iff ≥2 parse with zero new assumptions; else fence noun-49 globally.
3. `adv-49-653-990` (P3): test adverb-49 at the byte-identical "76 49 24" ×2 frame (@653/@990). Bar: name iff both parse with ≤1 total unstated assumption; else fence adverb-49.

(`unit-49-74-74` already queued — not re-proposed.)

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-49-74-frame.md`
- Queue: `val-49-74-frame` → `status: verdict`, `result: null` (pre-write assert: queued/verdictless; temp-file + rename; re-validated from disk; own entry only; no downgrade)
- Lock created on start, deleted on completion. R5005, sealed gates, red-team adjudication queue untouched.
