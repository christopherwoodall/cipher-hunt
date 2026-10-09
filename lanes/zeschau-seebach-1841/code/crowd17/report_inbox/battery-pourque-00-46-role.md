# Battery `pourque-00-46-role` — verdict: PROMOTE

## Bar (verbatim, pre-registered)

"Demonstrate complementizer vs restrictive parse at @107 with stated values, or fence"

Restated as numbered clauses:
- C1: the "00 46" at @106–107 parses as complementizer "pour que" under standing values with a grammatical rightward continuation.
- C2: the restrictive-"que" parse of 46 at @107 is excluded at battery grade (or the complementizer parse is the demonstrated survivor).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` via
`repair_parse.py` (`load_rows` + `parse`); asserts 1847/96 held.
`code/side-keyhunt/canonical.py` never used. Locus byte-confirmed:
0-based @100=62 @101=94 @102=93 @103=59 @104=45 @105=28 @106=00 @107=46.
Row note: @100–101 are row a1_02's tail; @102–107 are row a1_03's head —
the decisive "00 46" adjacency is fully inside row a1_03.

Standing values used (§7): 00="pour" (A9, leg-1 class-level, granted),
46="que" (pencil GT), 94="ne" (STRONG LEAD), 11="la" (pencil GT),
59="est" (provisional), 70="pre" (pencil GT), 79="tout" (A5), 24=finite
verb class (R17-009), 65=[noun,cls] (singular evidence).

## Findings

### C1: complementizer "pour que" — PASS

"00 46" occurs exactly 4× stream-wide (@106, @545, @1545, @1680). All four
take grammatical continuations under standing values:

1. **@106 (this locus):** "pour que la [21] [67] [93]..." — purpose clause
   with NP subject "la [21]". Zero ungranted assumptions.
2. **@545 (a3_01):** "pour que [24-fin] ce(47) que(46)..." — purpose clause
   headed by finite verb class 24; 47="ce" (A4).
3. **@1545 (a8_00):** "pour que prenne..." — already battery-validated as
   standing: battery-lever-77-78 parses @1542–1548 "lever [43-obj] pour que
   prenne [92]" and calls the purpose clause "fully grammatical. Strongest
   window." Independent corroboration of the "00 46" complementizer frame.
4. **@1680 (a8_05):** "pour que tout [65-noun]..." — purpose clause with
   79="tout" + noun-class 65.

The complementizer parse of "00 46" at @106–107 is therefore a licensed,
stream-wide frame with a standing-validated instance — not an ad hoc rescue.

### C2: restrictive-"que" excluded at @107 — PASS

Adopted from the standing PROMOTE verdict of the parent battery
`verb-slot-62-1686-cross100` (2026-10-09), whose F1/F2 kill the ne...que
bracket at this exact span:
- F1: "00 46" = "pour que" consumes the terminal "que" the restrictive
  reading needs. Restrictive "que" must directly precede the restricted
  constituent; "*il n'est pour que X" is ungrammatical.
- F2: with que consumed, "ne" strands bare with no second particle or
  expletive licenser — ungrammatical.

No independent restrictive leg for 46 at @107 exists: adjacent "94 46"
occurs 0× stream-wide; the neque-instance-sweep finder catalog lists
@101–107 as a gap-5 candidate, but finder catalogs are not adjudications,
and the parent promote adjudicated it as non-bracket. Nothing re-litigated.

### Adverses answered

- 62="il" kill-grade (R19-106/R20-125) honored: the complementizer parse
  is local to @106–107 and rightward; 62's value is never invoked.
- 94="ne" STRONG LEAD untouched; the restrictive-bracket death is parent
  business, adopted not re-decided.
- Row-boundary caveat stated: the span crosses a1_02|a1_03, but the
  decisive adjacency "00 46" is intra-row.

## Verdict: PROMOTE

46 at @107 is the "pour que" complementizer. The restrictive-"que" parse
is excluded. This closes the open follow-up arm of
`verb-slot-62-1686-cross100` exactly as routed.

## Scope

Locus-level only: 46's role at @107, and the "00 46" complementizer frame
attested at the four windows. No value named, no class granted or changed,
no standing or red-team verdict contradicted or downgraded, §7 intact.
Per the promote precedent, no follow-ups.

## Bookkeeping

- Stream: repaired 1,847-pair / 96-type, asserts held in-session;
  `canonical.py` never used.
- Queue entry `pourque-00-46-role` was `queued`/verdictless on start
  (pre-write assert passed).
- Report: `code/crowd17/report_inbox/battery-pourque-00-46-role.md`.
- Queue update: `status: verdict`, `verdict.result: promote`, dated 2026-10-09,
  via target-id-unique tmp `battery-queue.json.pourque-00-46-role.tmp` +
  atomic rename; disk re-validated; own entry only; no downgrade.
- Lock `code/crowd17/next-token/locks/pourque-00-46-role.lock` created on
  start (agent e023d903-3f23-448d-ba1b-aacc6597fc69 + UTC timestamp),
  deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
- Canonical-stream caveat stands.
