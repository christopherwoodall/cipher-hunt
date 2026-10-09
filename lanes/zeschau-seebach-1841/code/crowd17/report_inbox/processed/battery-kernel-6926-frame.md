# Battery report: kernel-6926-frame

- Target id: `kernel-6926-frame`
- Claim: "parse the stable \"69 26 00 33\" kernel at W3 (@406, 56-less) as the base frame; 56 then attaches to a known structure instead of an unknown one"
- Date: 2026-10-09
- Worker: battery worker (subagent 3c9f2096-8ccc-4fa2-908c-dcaedc75fc78)
- Stream: repaired 1,847-pair / 96-type parse, re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "kernel" = the recurring 4-group unit "69 26 00 33". "Base frame" = a grammatical structure the kernel parses as on its own. "New assumption" = a value, class, or structural premise not already standing at battery grade or higher.

Parent: `battery-parse-1626-clause.md` (NULL, 2026-10-09), follow-up 3. That battery established: `69 26 00 33` occurs exactly 3x stream-wide (W1, W2, W3); `56 69 26 00 33` occurs exactly 2x (W1, W2); the kernel is the stable unit and 56 is a W1/W2-specific addition. Offsets below are 0-based `@` on the repaired stream (parent used 1-based; 1-based @406 = 0-based @405).

## Bar (verbatim, pre-registered before testing)

> "resolve iff the kernel parses with <=1 new assumption"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** the kernel "69 26 00 33" parses as a licensed French structure using standing values plus at most one new assumption, uniformly across all three occurrences.
2. **C2:** no licensed zero-assumption rival parse exists (else the "resolve" is ambiguous, not a resolution).

Adverses: none listed on the queue target.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/kernel-6926-frame.lock` on start (agent id + UTC timestamp); deleted on completion.
2. Re-derived the repaired stream in-session; all offsets below are 0-based.
3. Census: "69 26 00 33" exactly 3x — @405 (a2_08), @933 (a5_10), @1627 (a8_03). "69 26" bigram exactly 3x (the same three); "26 00" exactly 3x; "00 33" exactly 8x.
4. Standing values used (all battery grade or higher, none invented):
   - 69 = ["noun","cls"] (R19-109 GRANT PROMOTE; value open, 'ce' value-lead per R19-110)
   - 26 = ["noun","lead"]
   - 00 = ["pour","prom"]
   - 33 = ["INF","cls"]
5. Checked the ce69-global battery (`code/crowd17/report_inbox/processed/battery-ce69-global.md`), which tested 69='ce' at all 12 of 69's windows (0-based), including all three kernel windows.

## Window-level evidence

### The three kernel windows (0-based, byte-confirmed)

- **@405 (a2_08):** `…45 88 53 34 | 69 26 00 33 | 01 02 53…` — the 56-less W3.
- **@933 (a5_10):** `…98 83 56 | 69 26 00 33 | 21 64 37…` — W1; left is the "vient de [56]" break window (red-team 83-conditioning venue, not decided here).
- **@1627 (a8_03):** `…33 46(que) 56 | 69 26 00 33 | 21 64 37…` — W2.

### The resolving parse (C1)

**"69 26 00 33" = "ce [26-noun] pour [33-INF]"** — "this [26] in order to [INF]".

- 69 takes its R19-110 value-lead 'ce' (the single new assumption — adopting a standing battery-grade lead as a parse premise).
- "ce" + 26-noun = licensed determiner phrase ("ce [noun]").
- "pour" + 33-INF = licensed purpose infinitive ("pour [INF]").
- "ce N pour INF" is licensed 1841 French ("ce motif pour agir"-shaped).

The ce69-global battery independently tested exactly this reading at all three kernel windows and found each clean:

- @405: "`53 34 69 26 00` — [53] [34=i] **ce** [26-noun] pour. Clean determiner frame."
- @933: "`83 56 69 26 00` — [83] [56] **ce** [26-noun] pour. Clean determiner frame."
- @1627: "`46 56 69 26 00` — que [56] **ce** [26-noun] pour. Clean determiner frame."

Zero windows force a non-'ce' value for 69 (ce69-global per-clause 2). The parse is uniform across all three occurrences: identical structure, zero window-specific strain.

### Zero-assumption rival check (C2)

Without the 'ce' premise, the kernel is "[69-noun] [26-noun] pour [33-INF]" — two juxtaposed bare nouns. Candidate readings:

- Apposition ("Monsieur le Président"-shaped): unestablished for two bare open-value nouns at battery grade (cf. frame-43-00-boundary: "apposition of two bare nouns is unestablished").
- 'de'-elision ("N de N"): unlicensed at battery grade (same battery).
- 26 as adverb: contradicts standing 26=["noun","lead"]; reviving the adverb arm would itself be a new assumption, not a zero-assumption rival.

No licensed zero-assumption parse exists. The 'ce'-determiner reading is the unique licensed resolution.

### Consequence for 56 (the claim's purpose, not the bar)

At W1/W2, "56 69 26 00 33" now reads "**[56-finite] ce [26] pour [33]**" — 56 as a finite verb taking "ce [26]" as its direct object with a purpose infinitive adjunct. This is the parent's H6 assignment with 69's role fixed as 26's determiner. 56 attaches to a known transitive frame instead of an unknown structure. (W1's "vient de [56]" left edge remains the red team's 83-conditioning venue; the kernel resolution does not decide it.)

## Per-clause pass/fail

1. **C1 PASS.** Kernel parses as "ce [26] pour [33-INF]" with exactly 1 new assumption (69='ce' value-lead premise), uniformly at @405/@933/@1627, corroborated by the ce69-global battery's independent window tests.
2. **C2 PASS.** No licensed zero-assumption rival; the 'ce' reading is the unique licensed parse.

## Verdict: PROMOTE

The kernel is resolved: "69 26 00 33" = "ce [26-noun] pour [33-INF]". One new assumption (69's standing 'ce' value-lead), within the bar's budget. No standing/red-team verdict contradicted or downgraded (R19-109, R19-110, 26-noun lead, 00="pour" prom, 33 INF cls all adopted as premises); §7 intact (no polyvalence declared — using a value-lead as a parse premise is not a value declaration); canonical-stream caveat stands (rows a2_08/a5_10/a8_03 offsets unvalidated).

Per §4, promotes require no follow-ups. The natural continuation (56's valency under the now-fixed "ce [26]" object) belongs to the parent's parse-1626-clause venue, not duplicated here.

## Bookkeeping

- Queue: `kernel-6926-frame` → `status: verdict`, `verdict: {"result": "promote", "report": "code/crowd17/report_inbox/battery-kernel-6926-frame.md", "date": "2026-10-09"}` (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock created on start (2026-10-09T12:37:00Z), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
