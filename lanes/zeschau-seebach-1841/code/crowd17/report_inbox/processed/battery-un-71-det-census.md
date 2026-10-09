# Battery report — un-71-det-census

Worker: battery-worker-un-71-det-census (agent 41be4725-0155-48eb-86f1-c0697a5f1072). Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/un-71-det-census.lock` created 2026-10-09T18:02:00Z, no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py` (replicated, not `canonical.py`). R5005 not touched. Every count below re-derived from the stream in this run.

## Bar (pre-registered verbatim, from battery-queue.json)

`71="une" excluded iff another cell holds "un"/"une" at battery grade; else "une" stays frequency leader.`

Numbered clauses:

1. Another cell (≠71) holds "un" or "une" at battery grade (battery promote or red-team grant) → 71="une" excluded by homophony (67 et/veut is the sole true polyvalence per §7, so no second "une" is licensable without a red-team declaration).
2. Else → "une" stays frequency leader for 71; status quo preserved.

## Method

Census of the cipher's determiner inventory for "un"/"une" across all 96 cells at two grades:
(a) red-team standing — `code/table-grid/table-registry.json` (50 cells, all standing values/grades);
(b) battery grade — full-text search of `code/crowd17/report_inbox/` (inbox + processed/) for any battery verdict naming a cell "un" or "une" as a value.
Window-local readings (explicitly fenced to one locus, never asserted globally) were recorded as such and do not count as "holding" a value. 71's own stream census (n=7: @233/@325/@711/@924/@1336/@1564/@1613) re-derived to confirm the locus set; the quant-71-925-value NULL (underdetermination among une/deux/plusieurs/trois) was not re-litigated.

## Findings

### (a) Red-team registry census

All 50 registry cells with values: 00=pour, 03=verb-stem, 06=ent, 11=la, 12=n, 17=fois, 21=noun, 24=verb, 26=noun, 29=er, 30=pas, 31=VERBAL, 32=verb, 33=INF, 34=i, 35=noun, 36=noun, 38=verb, 39=a/à, 40=e, 42=noun, 43=noun, 45=ce/dict, 46=que, 47=ce, 48=e, 58=nominal, 59=est, 63=verb, 64=qui, 65=noun, 68=noun, 69=noun, 70=pre, 76=noun, 77=le, 78=ver, 79=tout, 82=m, 83=de, 84=on, 86=INF, 87=ce, 88=gov, 89=noun, 92=verb, 93=verb, 94=ne, 96=par, 98=verb.
**No cell holds "un" or "une" at red-team grade.**

### (b) Battery-grade census

Full-corpus grep for value claims `[0-9]{2}="un"` / `[0-9]{2}="une"` across `report_inbox/` (inbox + processed/):
- `"un"` (masculine): **zero value claims anywhere.**
- `"une"`: exactly three cells carry the string in some report — 20, 41, 71. Disposition:
  - **20="une"**: appears only in battery-det-20-value, which explicitly states it "never asserts 20='chaque' or 20='une' globally" — a window-local (@307) reading, fenced scope. Not a value claim; 20 does not hold "une" at battery grade.
  - **41="une"**: appears in battery-noun26-la-frames (@239 "une fois la [N]", "coherent and unfalsified", 18/19 census windows consistent) and battery-fin-41-lexicon ("the determiner arm of the §7 split"). But noun26-la-frames explicitly states 41="une" was "the bar's stipulation at @239" and that "41's global value is owned by queued `donn-41-44`". No battery verdict promotes 41="une" as a value; the four 41-PROMOTE batteries (41-05-class, 41-1016-det-incompatibility, 41-808-role, 41-doubling-audit) name no "une" value. 41 does not hold "une" at battery grade.
  - **71="une"**: the cell under test itself (frequency leader per quant-71-925-value, not a named value).
- No other "un"/"une" value claims at any grade.

### Clause verdicts

1. Another cell holds "un"/"une" at battery grade: **FAIL — zero cells.** The exclusion arm does not fire.
2. "une" stays frequency leader for 71: **HOLDS** — status quo preserved. 71's value remains underdetermined among une/deux/plusieurs/trois per quant-71-925-value; "une" remains the frequency leader by prior standing.

## Verdict: NULL

No exclusion fires; no value is named. "une" stays frequency leader for 71. No standing/red-team verdict contradicted (§5.2 does not fire); §7 intact (no second polyvalence implicated). The window-local 41="une" and 20="une" readings are recorded as scoped, not value claims.

## Follow-ups (§4, all verified ABSENT from battery-queue.json)

1. `un-71-gender-frame` (P3) — test 71's 7 windows (@233/@325/@711/@924/@1336/@1564/@1613) for gendered followers/agreement: feminine agreement supports "une", masculine supports "un". Bar: ≥2 gendered legs name one, or fence as gender-neutral.
2. `un-41-vs-71-homophony` (P3) — re-test the homophony question iff 41's value lands as "une" via queued `donn-41-44`; if 41 takes "une", 71="une" is excluded by homophony. Bar: gate on donn-41-44 verdict.
3. `quant-71-rerun-neighbors` (P4) — re-run the une/deux/plusieurs/trois discrimination if new neighbor values land at @233 or @924 (the two most constrained windows). Bar: name with ≥2 legs or keep fenced.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-un-71-det-census.md`
- Queue: `un-71-det-census` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; disk re-validated; own entry only; no downgrade)
- Lock created on start (2026-10-09T18:02:00Z, no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
