# Battery verdict: un-71-gender-frame

- Target: `un-71-gender-frame` (battery-queue.json, priority 3, status queued)
- Claim: "Test 71's 7 windows (@233/@325/@711/@924/@1336/@1564/@1613) for gendered followers/agreement: feminine agreement supports 'une', masculine supports 'un'."

## Bar (verbatim, pre-registered)

">=2 gendered legs name one, or fence as gender-neutral."

Numbered clauses:
- C1: >=2 gendered legs converge on feminine → name 'une'.
- C2: >=2 gendered legs converge on masculine → name 'un'.
- C3: else → fence 71's gender as gender-neutral (undetermined at battery grade).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session (repaired_offsets.json + upstream-ct_R5005.txt; asserts held; `canonical.py` never used). Rendered all 7 windows of 71 with ±6 context under standing values. Gendered cells in the standing record: 11=la (feminine), 77=le (provisional, masculine), 17=fois (feminine noun, granted). A "gendered leg" = a window where 71's gender is forced by agreement with an adjacent gender-marked cell.

## Window-level evidence

| @ | window (0-based) | gendered contact |
|---|---|---|
| 233 | `par [21-N] [60] [71] [51] pre [98-verb]` | none (pre 60, fol 51 unvalued) |
| 325 | `[63-verb] [71] [10] [01]...` | none (pre 63 verb-class, fol 10 unvalued) |
| 711 | `n e [71] n [63-verb] pour` | none — letter-tier "12 48 [71] 12" (pre 48='e', fol 12='n') |
| 924 | `[65-N] [71] fois [61] par` | **fol 17='fois' FEMININE** |
| 1336 | `de [86-INF] [71] qui [60]` | none (fol 64='qui' is gender-neutral) |
| 1564 | `[60] [71] [50] er [24-verb]` | none (fol 50 open) |
| 1613 | `de [71] e [31-VERBAL]` | none (pre 83='de' unmarked, fol 48='e' letter) |

Stream-wide check: @924 is the ONLY 71 window with any gendered contact (11/77/17). 71 never contacts 11 or 77 anywhere.

### The @924 leg (feminine, single)

`[65-N] [71] fois [61] par` — "fois" (feminine, granted) requires a determiner; 65 is noun-class and cannot determine it; no other determiner candidate is adjacent. The only grammatical parse puts 71 in determiner position: "[71] fois" = "une fois". The "[71] fois [61] par" shape matches the French "une fois [time-unit] par" frame ("once a [week/month]"), with 61 unvalued as the putative time noun. 71 is therefore feminine at @924 → 'une' leg. Conditional only on the lane-standard grammaticality premise; the left boundary (65's role) does not affect 71's gender.

### Masculine legs: zero

No 71 window has a masculine gendered contact. The @1336 nominal arm ("[86-INF] [71] qui") has 'qui' as follower — gender-neutral, no leg either way.

## Per-clause pass/fail

- C1 (≥2 feminine legs → 'une'): **FAIL** — exactly 1 feminine leg (@924); bar requires 2.
- C2 (≥2 masculine legs → 'un'): **FAIL** — 0 masculine legs stream-wide.
- C3 (else → fence as gender-neutral): **FIRES**.

## Verdict: NULL (fence executed)

71's gender is fenced as undetermined at battery grade: one solid feminine leg (@924, coherent with the split package's determiner-arm window) against zero masculine legs and zero second feminine legs. The single @924 leg is recorded, not named — naming 'une' on one leg would violate the bar's own ≥2 standard.

## Scope

Fences only the gender question. Untouched: the 71 split package (nominal @1336 vs non-nominal @924, red-team venue), the @233 adjective fence, 98='vient' LEAD, 61's open value, §7. No standing/red-team verdict contradicted or downgraded. Canonical-stream caveat stands.

## Follow-ups proposed (§4; all verified ABSENT from battery-queue.json)

1. `val-61-925-timeunit` (P3) — name 61's value at @925; a time-unit noun completes "une fois [61] par" and hardens the @924 feminine leg to battery grade.
2. `un71-gender-widen` (P4) — stream-wide census of 71's contacts with gendered cells (11/77/17) beyond the 7 listed windows, plus gendered agreement via newly-valued adjectives/participles; any second gendered leg names the gender.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-un-71-gender-frame.md`
- Queue: `un-71-gender-frame` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.un-71-gender-frame.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/un-71-gender-frame.lock`: created on start (agent d2eab828, 2026-10-09T19:29:06Z, no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
