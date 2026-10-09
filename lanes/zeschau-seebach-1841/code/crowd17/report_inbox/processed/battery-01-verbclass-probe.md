# Battery `01-verbclass-probe` — verdict: NULL (avenue A re-opened, not killed)

## Bar (verbatim, from queue)

"Test 01 for finite-verb/modal shape across its full 28-window profile; 0/28 verb-shaped kills the modal-governor avenue at kill grade and hardens the @1028-1031 fence; >=1 verb-shaped window re-opens @1029 with 01 as infinitive governor (subject to the TLFi 'ce'+lexical-verb archaism constraint, which the red team would then adjudicate)"

## Numbered clauses (pre-registered before testing)

- (C1) Census all 28 windows of 01 on the repaired 1,847-pair / 96-type stream for finite-verb/modal shape.
- (C2) If 0/28 verb-shaped → KILL the modal-governor avenue (avenue A of `ce01-slot-1029-infinitive-avenue`) at kill grade; harden the @1028–1031 fence.
- (C3) If >=1 verb-shaped window → RE-OPEN @1029 with 01 as infinitive governor; note the TLFi 'ce'+lexical-verb archaism constraint for red-team adjudication.

## Method

- Read `BATTERY-PROTOCOL.md` first; created `locks/01-verbclass-probe.lock` on start (deleted on completion).
- Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` + `repaired_offsets.json` (a5_03 flipped 1→0). Asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- n(01) = 28 confirmed byte-exact. @-offsets are 1-based lane convention.
- Standard for "verb-shaped": 01 occupies a finite-verb or modal-governor slot in a grammatical 1841-French parse under standing values only (banked GT + promoted/granted; no open-value assumptions). Non-finite (infinitive) shapes are recorded as leads, not counted — the bar says "finite-verb/modal".
- The locus @1030 (`87 01 03 29`, row a6_03) is avenue A itself; it is excluded from the independent verb-shaped count (counting it would be circular). Independent denominator: 27.

## Census — all 28 windows

Context format: three pairs left, `01`, three pairs right. Standing values used: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce, 46=que (granted); 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e (pencil GT); 65=noun class (R18); 30=pas (red-team promoted).

| @ | row | context | assessment |
|---|---|---|---|
| 35 | a1_00 | `03 64 32` 01 `08 91 39` | not verb-shaped — would need 32 nominal subject; 32 not nominal |
| 41 | a1_01 | `39 64 41` 01 `24 88 43` | not verb-shaped — 01 immediately before finite/modal 24; two finites impossible |
| 196 | a2_00 | `98 56 47` 01 `21 60 08` | not verb-shaped — det-01-noun slot: "ce [01] [21-N]" (subject NP-internal) |
| 256 | a2_02 | `63 00 66` 01 `91 32 43` | not verb-shaped — no subject slot; "pour [66] [01] [91-adj]" has no finite frame |
| 296 | a2_03 | `40 65 16` 01 `11 78 40` | not verb-shaped — 01 after infinitive 16, before "la"; no subject |
| 328 | a2_05 | `63 71 10` 01 `19 00 92` | not verb-shaped — no subject slot; neighbors value-open |
| 346 | a2_05 | `96 43 87` 01 `06 70 12` | not verb-shaped — modal arm "ce [01] [entreprendre]" dies on the misspelled complement ("entprenne", `spell-06-entre` KILL) plus TLFi "ce"+lexical-verb archaism |
| 410 | a2_08 | `26 00 33` 01 `02 53 84` | not verb-shaped — no subject slot |
| 485 | a2_11 | `13 52 30` 01 `19 64 76` | not verb-shaped — "pas [01]" without "ne" is ungrammatical in 1841 diplomatic French |
| 597 | a4_00 | `92 79 85` 01 `29 40 03` | LEAD (non-finite) — "[01]er" infinitive composition possible but unforced ("29 40" is independently word-internal "ere"); not counted per bar |
| 718 | a5_01 | `00 66 86` 01 `02 21 80` | not verb-shaped — no finite frame |
| 829 | a5_06 | `59 38 82` 01 `24 87 11` | not verb-shaped — clitic slot "m' [01]" before finite 24 |
| 894 | a5_08 | `06 77 76` 01 `98 82 14` | not verb-shaped — 01 before finite 98='vient' |
| 941 | a5_10 | `21 64 37` 01 `07 50 40` | not verb-shaped — 01 after predicative 37; no subject slot |
| 950 | a6_00 | `98 96 86` 01 `77 86 96` | not verb-shaped — "par [86] [01] le [86] par"; no verb frame |
| 971 | a6_00 | `06 77 76` 01 `98 48 51` | not verb-shaped — same as @894 |
| 977 | a6_01 | `51 45 08` 01 `00 92 07` | FENCED (conditional) — "ce [08] [01] pour [92-inf]" is verb-shaped ONLY if 08 is nominal; 08 value-open |
| 985 | a6_01 | `47 78 45` 01 `24 89 48` | not verb-shaped — "ce [01]" before finite 24 |
| 989 | a6_01 | `24 89 48` 01 `76 49 24` | not verb-shaped — no clean verb frame ("…e [01] [76]…") |
| 1030 | a6_03 | `96 43 87` 01 `03 29 80` | LOCUS (avenue A itself) — excluded from independent count |
| 1256 | a7_02 | `06 65 46` 01 `61 31 29` | **VERB-SHAPED** — see § below |
| 1262 | a7_02 | `29 69 88` 01 `09 11 50` | not verb-shaped — det-01-noun family ("[01] [09-N] la") |
| 1441 | a7_08 | `16 24 85` 01 `52 68 59` | not verb-shaped — 85 is verb-stem (A3): can't be 01's subject; 01 can't follow finite 85 |
| 1463 | a7_09 | `66 79 17` 01 `21 62 48` | not verb-shaped — det-01-noun family ("fois [01] [21-N]") |
| 1635 | a8_03 | `21 64 37` 01 `74 87 74` | not verb-shaped — same as @941 |
| 1654 | a8_04 | `38 82 16` 01 `56 37 11` | not verb-shaped — 01 after infinitive 16; no subject |
| 1732 | a8_07 | `24 30 15` 01 `56 30 06` | LEAD (non-finite) — "pas [15] [01-inf]" possible; not counted per bar |
| 1819 | a8_10 | `06 29 37` 01 `02 09 19` | not verb-shaped — 01 after predicative 37; no subject slot |

## The verb-shaped window: @1256

Wider bytes (row a7_02, 1-based @1249–1264):

`67 46 26 30 06 ‖ 65 46 01 61 31 29 ‖ 69 88 01 09 11`

- 06's left neighbor is 30='pas' (red-team promoted): 06 cannot attach left as '-ent' ("pasent" contradicts 30='pas'), so 06 is standalone. 65 = noun class (R18) → 65 is the antecedent of 46='que' (banked GT).
- **P1 (preferred): "[65-N] que [01-V-finite] [61-S]"** — subject-verb inversion in the "que"-relative ("le livre que lit Marie"-shaped; licensed literary French). 61-nominal is supported: @1430 ("[91-adj] [61-N]"), @578/@1169 (object position), @1220 (subject position).
- **P2 (live rival): "[65-N] que [01-S] [61-V]"** — 01 as subject (nominal), 61 as finite verb, unmarked S-V order. 01-nominal-subject is unprecedented but unkilled; 61-verbal is weakly supported (@1456 "[62] [61] [21]" needs unestablished 62='il' at that window).
- P1 is preferred (61-nominal is better supported than 01-nominal-subject; inversion is licensed), but P2 is live. The P1/P2 §7 tension (01 cannot be both verbal and nominal — 67 is the sole polyvalence) is red-team venue. Either way, **P1 is a grammatical finite-verb parse: 01 shows verb-ness.**

## Per-clause results

- (C1) **PASS** — 28/28 windows examined against bytes; assessments above.
- (C2) **does not fire** — the 0/28 condition is not met: 1 window (@1256/P1) is verb-shaped. The kill-grade kill of avenue A does not execute.
- (C3) **FIRES** — >=1 verb-shaped window (@1256/P1) re-opens @1029 with 01 as infinitive governor.

## Adverse

"TLFi 'ce'+lexical-verb archaism constraint applies if a verb-shaped window is found" — **answered**: a verb-shaped window was found (@1256/P1), but its subject is 61 (inversion), not "ce" — the constraint does not bite there. It WILL bite at @1029 ("ce [01] [03]er") if avenue A is pursued: flagged for red-team adjudication per the bar.

## Verdict: NULL

- C1 passes; C2's kill condition is not met; C3 fires.
- **Avenue A (01 as finite modal governing "[03]er" at @1029) is RE-OPENED, not killed.** The @1028–1031 fence is NOT hardened.
- The claim "01 takes a finite-modal value" is neither promoted (@1256/P1 shows 01 as an intransitive finite verb, not a modal governor; no value named) nor killed → NULL per §4.
- No standing or red-team verdict contradicted or downgraded (the @1028–1031 fence was battery-grade; Round 18 has no verdict on 01's class). §7 intact; the P1/P2 polyvalence tension is red-team venue.
- Caveat: canonical-stream verdict — row a7_02's upstream offset is unvalidated (68/70 upstream offsets unvalidated per protocol §7).

## Follow-ups (null mandate; all verified absent from `battery-queue.json`)

1. `01-1256-p1p2-adjudicate` (P2) — red-team input: adjudicate P1 (01=V finite, inversion, 61=S) vs P2 (01=S nominal, 61=V) at @1256; rule on the §7 tension (01 cannot be both verbal and nominal-subject).
2. `01-nominal-sweep` (P3) — test 01 for nominal (noun/pronoun) shape across its 28 windows; decides P2's viability and bounds 01's class independently of the verb question.
3. `61-verbclass-probe` (P3) — test 61 for finite-verb shape (n=18; lead @1456 "[62] [61] [21]"); a 61-verb finding flips @1256 to P2 and re-kills avenue A.

## Bookkeeping

- Queue: `01-verbclass-probe` → status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/01-verbclass-probe.lock` created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gate instances, red-team adjudication queue untouched.
