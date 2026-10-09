# Battery report: tail-12-16-uniform

**Target:** `tail-12-16-uniform` (priority 3)
**Verdict: NULL** — 12 is word-initial at 2/2 decided "12 16" windows, but
uniformity is not established (W2 is the fenced window itself); the
distributional argument is built below and favors 12-independence at W2
without resolving the noun26-26n-exclude fence.

## Bar (verbatim from queue)

> "turn @843 boundary into distributional argument at W2 if uniform"

Restated as numbered pass/fail clauses:

- **C1:** Census "12 16" byte-exact: exactly 3 windows, contexts stated.
- **C2:** Uniformity judged "under 16's decided value" (the claim's premise).
- **C3:** If uniform, the @843 forced 26|12 boundary (plus the other
  windows' 12-contacts) is stated as a distributional argument at W2
  (@241, the fenced la-window) favoring 12-independence over the "26n"
  one-word rival.

## Method

- Read BATTERY-PROTOCOL.md first; lock created/deleted per protocol.
- Stream re-derived in-session from
  `code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per
  `code/side-keyhunt/repair_parse.py` (2-digit pairs from each row's
  repaired offset). Result: **1,847 pairs / 96 types**, byte-identical to
  the canonical stream.
- `canonical.py` never touched. R5005, sealed gate instances, and the
  red-team adjudication queue untouched.
- @-offsets are 0-based stream indices (queue convention).

## Window-level evidence (all byte-traced)

**Census: "12 16" occurs exactly 3x.**

1. **0b@241, row a2_01** (`41 17 | 11 26 | 12 16 | 56 43 00 66 91`):
   the fenced W2 la-window. Three readings remain live per
   noun26-26n-exclude: (i) 26 | 12-initial "n...", (ii) "26n" one word,
   (iii) 26 | "n'" elision + 16. No window-level contact forces a
   boundary here.

2. **0b@843, row a5_06** (`17 98 20 62 | 94 26 | 12 16 | 00 33 96 40 62`):
   **26|12 boundary forced.** 94 = 'ne' is a STRONG LEAD (banked). The
   "26n" one-word rival would give "94 [26n]" = "ne [noun]", which is
   ungrammatical in 1841 French — the rival is kill-grade dead at this
   window (adopted from gov-frames via noun26-26n-exclude, not
   re-litigated). Therefore 12 is its own token here: word-initial 'n'
   (or an "n'" clitic — either way independent of 26).

3. **0b@1430, row a7_08** (`33 29 87 63 91 61 | 12 16 | 76 49 64 52 82`):
   12 is its own token, word-initial. There is no 26 at all, and no
   named leftward-composition target exists: 61's global value is
   fenced (locus-level "premier" only, at @1556), and no French word
   "[61]n" is statable under standing values. 12 does not compose
   leftward here.

**Distributional side-data:** n(12) = 23. Left-neighbor census of 12:
26 x4, 53 x4, 70 x3, 60 x2, 41 x2, others x1. The "70 12" x3 contacts
("prenne" family) show that 12 *can* compose leftward in principle —
so 12's independence before 16 is a window-local finding, not a
stream-wide property. Answered as adverse, not ignored.

## Per-clause results

- **C1: PASS.** Exactly 3 "12 16" windows, contexts byte-confirmed
  above. n(12)=23, n(16)=28, n(26)=17 on the re-derived stream.
- **C2: FAIL (epistemic).** 16's value is not decided: val-16-a-vs-est
  fenced both 'a' and 'est' (NULL), frame-82-16's fit count is
  overstated, and reseg-1481-98 dissolved the window that forced the
  finite-verb class. 16's class/value is red-team territory; the
  claim's premise "under 16's decided value" cannot be met at battery
  grade.
- **C3: CONDITIONAL PASS — the distributional argument is built, but
  it does not resolve the fence.** Of the three W2 readings, (i) and
  (iii) both treat 12 as an independent token — the state attested at
  2/2 decided "12 16" windows. The "26n" one-word rival (ii) has zero
  positive windows: kill-grade dead at @843 (94 = 'ne' contact),
  impossible at @1430 (no 26 present), surviving only at the fenced
  W2 itself. That is a genuine distributional asymmetry favoring
  12-independence at W2. But it does **not** force (i) over (iii) at
  W2 — 16's value is open, which was the fence's stated cause — and
  it does not contact-force the 26|12 boundary there. The
  noun26-26n-exclude fence stands, strengthened but unresolved.

## Standing state

- No standing verdict contradicted or downgraded. The
  noun26-26n-exclude fence at W2 is confirmed, not overturned;
  §7 intact (no polyvalence declared).
- Premises used, none challenged: 12 = 'n' (letter tier, pending
  ratification), 94 = 'ne' STRONG LEAD, 76 = promoted noun.

## Follow-ups proposed (for supervisor queuing)

1. **`distrib-12-wordinitial-stream`** (P3) — census all 23 of 12's
   windows for leftward composition ("70 12" prenne-family x3, "53 12"
   x4, "26 12" x4, etc.): is word-initial-12 the norm or the
   exception stream-wide? Gives this target's uniformity claim a real
   distributional prior.
2. **`comp-61-12-leftward`** (P3) — test whether 61 + 12 can ever
   compose leftward at battery grade (any named word "[61]n" at any of
   61's windows). A battery-grade kill hardens @1430's 12-independence
   to kill grade, making the distributional argument 2/2 kill-grade
   plus one fenced window.

## Bookkeeping

- Queue: `tail-12-16-uniform` -> status `verdict`, result `null`,
  report `code/crowd17/report_inbox/battery-tail-12-16-uniform.md`,
  date 2026-10-09 (temp-file + rename, pre-write assert confirmed
  `queued`/verdictless, JSON re-validated).
- Lock created on start and deleted on completion. No invented numbers;
  every number traces to the repaired stream.
