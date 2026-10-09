# Battery report: comp-61-12-leftward

**Target:** `comp-61-12-leftward` (priority 3)
**Verdict: PROMOTE** — at battery grade, 61 + 12 never composes leftward:
exactly one byte-level 61->12 contact exists in the repaired stream
(@1429 -> @1430, row a7_08), and no named word "[61]n" is statable at
that window under standing values. Adverses answered.

## Bar (verbatim from queue)

> "Test whether 61 + 12 can ever compose leftward at battery grade (any named word '[61]n' at any of 61's windows). A battery-grade kill hardens @1430's 12-independence to kill grade, making the distributional argument 2/2 kill-grade plus one fenced window."

Restated as numbered pass/fail clauses:

- **C1:** Census every 61-window in the repaired 1,847-pair stream and
  identify all 61->12 contacts (leftward composition of 12 onto 61).
- **C2:** At each 61->12 contact window, test whether a named word
  "[61]n" is statable under standing values at battery grade.
- **C3:** The "[61]n" one-word rival is dead at battery grade at every
  contact window (or has no contact windows), hardening @1430's
  12-independence to kill grade for the 61-composition rival.

## Method

- Read BATTERY-PROTOCOL.md in full before testing; lock
  `locks/comp-61-12-leftward.lock` created on start, deleted on
  completion (see Bookkeeping).
- Stream re-derived in-session from
  `code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed byte-exactly per
  `code/side-keyhunt/repair_parse.py` (2-digit pairs from each row's
  repaired offset). Result: **1,847 pairs / 96 types**.
- `canonical.py` never touched. R5005, sealed gate instances, and the
  red-team adjudication queue untouched. Every number below traces to
  the repaired stream. @-offsets are 0-based stream indices.

## Window-level evidence (all byte-traced)

**C1 census: 61 occurs at exactly 18 windows; exactly ONE 61->12 contact.**

| @ | row | L | R | | @ | row | L | R |
|---|---|---|---|---|---|---|---|---|
| 223 | a2_01 | 89 | 96 | | 1206 | a7_00 | 55 | 21 |
| 279 | a2_03 | 37 | 20 | | 1219 | a7_01 | 92 | 24 |
| 281 | a2_03 | 20 | 42 | | 1256 | a7_02 | 01 | 31 |
| 367 | a2_06 | 49 | 70 | | 1281 | a7_03 | 53 | 56 |
| 447 | a2_09 | 62 | 59 | | **1429** | **a7_08** | 91 | **12** |
| 577 | a3_02 | 55 | 94 | | 1455 | a7_09 | 62 | 21 |
| 645 | a4_02 | 87 | 88 | | 1510 | a7_11 | 12 | 59 |
| 926 | a5_10 | 17 | 96 | | 1556 | a8_01 | 93 | 40 |
| 1168 | a6_09 | 55 | 94 | | 1810 | a8_10 | 04 | 15 |

The single contact: **61@1429 -> 12@1430**, row a7_08, ctx
`87 63 91 61 12 16 76 49` — the same @1430 window cited in
tail-12-16-uniform (`33 29 87 63 91 61 | 12 16 | 76 49 64 52 82`).

Reverse-order contact noted for completeness: 12->61 once, @1509 row
a7_11 (`86 56 41 12 61 59 39 81`) — not "[61]n" order, outside the bar.

**C2 statability at the contact window.** Standing values: 12 = 'n'
(letter tier, pending ratification — premise adopted from
tail-12-16-uniform, not re-litigated); 61 is value-open everywhere
except the locus-level "premier" at @1556. At @1429 no standing value
for 61 exists, so no French word "[61]n" can be named there at battery
grade — the left component has no stated value to attach 'n' to. The
fenced locus value cannot rescue it: @1556 is 61 with neighbors 93/40
(ctx `23 99 13 93 61 40 17 11 26`, row a8_01) — no 12 contact, and
"premier"+"n" is not a French word in any case. The byte-level contact
does not compose at battery grade.

## Adverses (answered, not ignored)

- **A1 — "61 is largely value-open outside @1556."** Answered. The
  openness is the reason C2 passes as an absence rather than a kill of
  a stated candidate: with no value statable for 61 at @1429, no
  "[61]n" word is statable either. The locus value "premier" was
  byte-verified at @1556 (neighbors 93/40) and cannot contact 12.
  **Caveat (fenced, not a gap):** if 61 is ever granted a global value,
  the @1429 61->12 contact is the one window that must be re-audited —
  a future "[61]n" naming would reopen this verdict. At battery grade
  under current standing values, the claim holds.
- **A2 — "'70 12' x3 contacts show leftward composition is possible in
  principle for other neighbors."** Answered and verified: 70->12 at
  @347 (a2_05, `87 01 06 70 12 94 74 67 78`), @1118 (a6_07,
  `69 11 88 70 12 06 14 06 11`), @1547 (a8_00,
  `43 00 46 70 12 94 92 45 23`) — the "prenne" family (70 = 'pre',
  banked). So 12 *can* compose leftward in principle; the claim is
  specific to 61, and the 70-control is consistent with it. 12's
  left-neighbor census re-confirms the tail report exactly:
  26 x4, 53 x4, 70 x3, 60 x2, 41 x2, eight singles, n(12) = 23.

## Per-clause results

- **C1: PASS.** 18 windows of 61 censused; exactly one 61->12 contact
  (@1429 -> @1430, row a7_08).
- **C2: PASS.** No named word "[61]n" statable at the contact window
  under standing values (61 value-open at @1429; locus value "premier"
  fenced to @1556 with no 12 contact).
- **C3: PASS.** The "[61]n" one-word rival is dead at battery grade at
  its only contact window and absent at the other 17 windows.
  @1430's 12-independence is hardened to kill grade *against the
  61-composition rival*, making the tail-12-16-uniform distributional
  argument 2/2 kill-grade at decided "12 16" windows (@843 via
  94 = 'ne'; @1430 via this battery) plus the one fenced W2 window.

## Standing state

- No standing verdict contradicted or downgraded; nothing promoted or
  granted beyond this target's claim. tail-12-16-uniform's null stands
  (W2 fence unresolved); this battery confirms and hardens its @1430
  leg. §7 intact.
- Premises used, none challenged: 12 = 'n' (letter tier, pending),
  70 = 'pre' (banked), 94 = 'ne' (STRONG LEAD).

## Follow-ups proposed

None required: verdict is promote, not null. The single fenced caveat
(61's future value grant re-opens @1429) is recorded under A1 and in
the queue entry's notes field for the supervisor.

## Bookkeeping

- Queue: `comp-61-12-leftward` -> status `verdict`, result `promote`,
  report `code/crowd17/report_inbox/battery-comp-61-12-leftward.md`,
  date 2026-10-09 (temp-file + rename; pre-write assert confirmed
  `status == "queued"` and no existing verdict; JSON re-validated).
- Lock created on start (agent id + UTC timestamp), deleted on
  completion. No invented numbers; every number traces to the repaired
  1,847-pair stream.
