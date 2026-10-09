# Battery report: imp-80-finite-rival-1156-1596

- Target id: `imp-80-finite-rival-1156-1596`
- Claim: test the finite-verb rival readings at @1156/@1596 ("...pour [92]er ... [80]" / "[03]er ... [80]" as finite verbs continuing the prior clause)
- Date: 2026-10-09
- Worker: battery worker (subagent 71f89f50-62a4-4dd8-83b8-1e1d6c0d7b0e)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`); re-derived in-session: **1,847 pairs, 96 types**. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "finite-verb rival" = 80 read as a conjugated verb (not imperative, not infinitive, not determiner) carrying tense/person, which must have an overt or infinitive subject and matching agreement.

## Bar (verbatim, pre-registered before testing)

"promote iff subject + agreement license parses with zero ungranted assumptions"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** at @1156, 80 as finite verb has a licensed subject and licensed agreement with zero ungranted assumptions.
2. **C2:** at @1596, 80 as finite verb has a licensed subject and licensed agreement with zero ungranted assumptions.

## Parentage

Follow-up 1 of the NULL `imp-80-bare-1156-1596` (2026-10-09, in processed/). That battery fenced the bare-verb imperative readings at both windows and listed the finite-verb rival as live-but-untested. This battery tests it. Also adopted: R19-120's locus-conditioned window findings — W1 imperative ("[80]-le", conditional on 77='le' provisional) and W2 determiner ("[80] fois", unique survivor among named rivals at @1156).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/imp-80-finite-rival-1156-1596.lock` on start (agent id + 2026-10-09T12:25:42Z); no stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types confirmed).
3. Registry standings consulted (read-only): 02=null, 66=null, 81=null, 92=["verb","cls"], 03=["verb-stem","cls"], 80=null. Ground truth: 29=er, 84=on, 00=pour, 47=ce, 17=fois, 77=le (provisional), 67=et/veut (sole polyvalence; 'et' here since follower 77 is not infinitive-shaped).

## Window-level evidence

### @1156 (row a6_09) — `66 84 02 | 00 92 29 | 80 | 17 77 82 44 83 21`

Candidate parse: "on [02] pour [92]er [80-fin] fois" — 80 as finite verb continuing the "on [02] …" clause.

- Same-clause reading dead: 92=verb cls + 29='er' gives a governed infinitive under 00='pour' (granted A9). A bare finite verb directly after "pour [92]er" ("*pour parler dit") is ungrammatical every period — no coordination, no boundary license.
- Continuing-clause reading: the subject would be 84='on' and the clause verb 02 — but 02's class/value is **unvalued** (registry null). "on [02]" is not a licensed clause at battery grade. 66 is also unvalued. Zero-ungranted-assumptions standard cannot be met.
- Agreement: 80's value is unvalued; 3sg/any-person agreement is undemonstrable.
- **C1: FAIL.** Not kill grade: naming 02 as finite revives the reading, so it stays fenced, not dead. R19-120's granted determiner window finding ("[80] fois", unique survivor) is untouched — no contradiction.

### @1596 (row a8_02) — `65 48 29 | 47 08 81 | 03 29 | 80 | 67 77 81 82 98`

Candidate parse: "[03]er [80-fin]" — 80 as finite verb with infinitive subject, or with subject "ce [08][81]".

- 03=verb-stem cls (R19) + 29='er' → "[03]er" is an infinitive (not re-litigated).
- Infinitive-subject reading ("[03]er [80-fin]"): grammatical in French only if 80 is a 3sg finite form ("Vouloir, c'est pouvoir"-shaped). 80's value is **unvalued** — agreement unlicensable with zero ungranted assumptions.
- Subject-NP reading ("ce [08][81] … [80-fin]"): the bare infinitive "[03]er" sits between the NP and the finite verb — ungrammatical without "à/de" (*"ce mot parler est"). No rescue.
- Follower 67='et' (positional rule) + 77='le' provisional: "[80-fin] et le [81]…" leaves "et le [81]" verb-less — no coordination license for a finite 80.
- **C2: FAIL.** Not kill grade: a named 3sg-finite 80 revives the infinitive-subject reading, so it stays fenced, not dead.

## Verdict: NULL

Both finite-verb rival readings fail the bar at battery grade — neither is licensed with zero ungranted assumptions. Neither is forced false (revival paths exist), so neither is killed. No standing or red-team verdict contradicted or downgraded (R19-120's W1/W2 window findings stand; A8 verb-frame for 80's global class untouched); §7 intact; canonical-stream caveat stands (rows a6_09/a8_02 unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-02-1153` (P3) — name 02's class/value at @1153; a finite-02 revives the @1156 finite-80 reading (the only live resurrection path).
2. `val-66-1150` (P3) — name 66's class at @1150; completes the "66 on [02]" left frame feeding @1156.
3. `val-80-1596-3sg` (P3) — name 80's value at @1596; a 3sg finite form licenses the infinitive-subject reading under "[03]er [80-fin]".

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-imp-80-finite-rival-1156-1596.md`
- Queue: `imp-80-finite-rival-1156-1596` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
