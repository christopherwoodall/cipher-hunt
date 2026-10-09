# Battery `41-doubling-audit` — verdict: PROMOTE (doubling confirmed stream-real)

Worker: 280dc897-797d-481f-bf04-a41687509fdd · 2026-10-09T13:45:31Z start
Follow-up #1 of `val-41-1016` NULL (2026-10-09). Audits the `@589/590` "41 41"
doubling against the unvalidated a3_02/a4_00 row offsets.

## Bar (verbatim, pre-registered)

> "byte-audit the doubling against offsets; artifact finding re-opens the 41
> naming, confirmed-real keeps W_C fenced."

Restated as numbered pass/fail clauses (before testing):
- C1: byte-audit the `@589/590` doubling against the a3_02/a4_00 raw digits
  and row offsets — determine whether the doubling is stream-real (present in
  the raw transcription under the standing offsets, no digit duplication) or an
  offset artifact.
- C2 (artifact arm): if the doubling is an offset artifact, report the cause;
  41 naming re-opens and `val-41-1016` re-opens.
- C3 (confirmed-real arm): if the doubling is confirmed stream-real, the W_C
  (@1017 "[41] [15] [66]") fence for 'plus' stands — kept, not re-opened.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs,
96 types; 0-based @-offsets). Independently re-derived the upstream
1,846-pair parse from `data/upstream-offsets.json` for the repair-artifact
check. `canonical.py` never used. Adopted premises (not re-litigated):
§7 sole-polyvalence; `val-41-1016` NULL + W_C fence (A2 carried the offset
question here). R5005, sealed gates, red-team adjudication queue untouched.

## Window-level evidence (byte-exact)

**The doubling is the only one stream-wide.** Exactly one "41 41" adjacency
in 1,847 pairs: @589/@590, straddling the a3_02|a4_00 row boundary.
Context `@588..591 = 97 41 | 41 09`, rows a3_02 → a4_00.

**Raw transcription (upstream-ct_R5005.txt):**
- a3_02 (line 21): `9459306711432480971376459452877845135561948206065010191814009741`
  — 64 digits, raw tail `...1814009741`.
- a4_00 (line 22): `41090092798501294003392696459354643964025847778783708810`
  — 56 digits, raw head `410900927985...`.

**Standing offsets:** both rows offset 0 (upstream EM choice; repaired parse
unchanged). Both rows even-length → zero digits dropped at the boundary.

**Byte positions of the two 41s:**
- @589 = a3_02 digits[62:64] = "41" (the row's final pair).
- @590 = a4_00 digits[0:2] = "41" (the row's first pair).
The two 41s occupy distinct raw digit positions. No digit is duplicated.
The doubling is written in the transcription itself.

**Repair-artifact check:** the doubling is present identically in upstream's
original 1,846-pair parse (`@588..591 = 97 41 | 41 09`, doubling at 589/590
in both parses). All rows before a5_03 are pairing-identical between the
parses. Not a repair artifact.

**Offset-phasing table (re-derived per row, all four phasings):**

| off(a3_02) | off(a4_00) | a3_02 ends       | a4_00 starts    | doubling | pairs lost |
|------------|------------|------------------|-----------------|----------|------------|
| 0 (standing) | 0 (standing) | 00 97 41      | 41 09 00        | YES      | 0 / 0      |
| 0          | 1          | 00 97 41         | 10 90 09        | no       | 0 / 1      |
| 1          | 0          | 40 09 74         | 41 09 00        | no       | 1 / 0      |
| 1          | 1          | 40 09 74         | 10 90 09        | no       | 1 / 1      |

The doubling is phase-dependent: any single-row flip removes it. But a flip
is not a correction — it re-pairs the whole row, drops a pair (a head digit),
and renames @589/@590 to '74'/'10'. There is no byte-level evidence favoring
any flip:
- No manuscript gloss covers a3_02 or a4_00 (glosses cover a5_03 and a8_05
  only; the a5_03 flip was gloss-driven — no such evidence exists here).
- The upstream EM chose offset 0 for both rows; both rows are even-length,
  so the boundary is the cleanest possible (no digit lost, none duplicated).
- Choosing a flip to rescue 41's value would be result-driven, not
  evidence-driven; the audit standard requires positive evidence of a wrong
  offset, and none exists.

**Verdict on the artifact question:** no artifact found. The doubling is
stream-real under the standing canonical parse.

## Per-clause results

- **C1: PASS.** The doubling is byte-real: present in the raw transcription,
  present in both the upstream and repaired parses, no digit duplication,
  both boundary rows even-length with offset 0 and zero dropped digits.
  The only way to remove it (offset flip) has no byte-level evidence and
  destroys the local evidence base rather than correcting it.
- **C2 (artifact arm): does not fire.** No artifact found; 41 naming does
  not re-open.
- **C3 (confirmed-real arm): FIRES.** The W_C fence from `val-41-1016`
  stands: the D2 "41 41" kill on single-word 41 candidates (e.g. 'sans' →
  "sans sans", 0 hits in 31.6M period-French chars) rests on a stream-real
  doubling. `val-41-1016` does not re-open on this ground.

## Adverses

None pre-listed. Found in testing: none — the phase-dependence concern
(the offset-phasing table) was tested and answered with byte evidence
above; it is not an artifact, it is the standing canonicality caveat,
which is unchanged and out of battery scope (offset validation is not a
battery act).

## Verdict: PROMOTE

The audit claim is confirmed with byte-level evidence: the @589/590 "41 41"
doubling is stream-real, and the W_C fence is kept. No follow-ups required
per §4 (promote). The standing canonicality caveat (68 of 70 row offsets
unvalidated, including a3_02/a4_00) is unchanged — it was not tested away,
and this battery found no evidence against the standing offsets.

## Scope

Confirms the evidence base of the `val-41-1016` W_C fence only. Untouched:
41's value (still unnameable), `split-41-redteam` (queued, red-team venue),
all §7 standings, R5005, sealed gates, red-team adjudication queue. No
standing or red-team verdict contradicted or downgraded.
