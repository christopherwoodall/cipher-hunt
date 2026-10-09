# Battery report: ne-508-reseg-gate62 — verdict: NULL (§5.2 contradiction)

## Bar (verbatim, pre-registered)

"one coherent word-internal parse with every pair's syllable role stated and the French word named; else the word-internal arm closes and @508 stays a fenced res."

Numbered clauses:
- C1: Produce one coherent word-internal parse of @507-509 with every pair's
  syllable role stated and the French word named.
- C2 (else-arm): If C1 fails, the word-internal arm closes and @508 stays a
  fenced residual.

## Headline: task premise contradicts standing red-team verdicts — escalated

The dispatch brief instructed: "Run now with 62='il'." That premise is dead at
red-team level:

- **R19-097 (il-62 — REJECT):** the 62='il' battery promote (2026-10-08) "fails
  its own bar"; "'il' is killed at kill grade per R19-106."
- **R19-106:** attacker's 5-leg kill of 62='il' (corroborated and extended).
- **R20-125 (redteam-62-conditioned — REJECT, confirm R19-106):** "The
  conditioned 'il' lead stays REJECTED (§7-DOA per R17-022; @508 unclean);
  'il' stays KILLED at kill grade, permanent. 62's cell stays absent."

The gate's trigger ("a 62='il' battery promote") did fire at battery level on
2026-10-08 — but the promote it fired on was REJECTED by R19-097 the next day
and the value KILLED permanently by R20-125. The gate verified "satisfied" on a
dead premise. Per protocol §5.2 I do not run the re-test with 62='il' and do
not overwrite the standing verdicts: result NULL, contradiction headlined,
escalated to the red team.

## Byte verification (repaired 1,847-pair stream; asserts held: 1,847 pairs, 96 types)

- Locus @505–@511: 21, 67, **77, 62, 94**, 64, 98 (row a3_00). @507='77',
  @508='62', @509='94' confirmed byte-exact.
- '62 94' bigrams: 9 stream-wide (matches N52's "62's nine 62→94 frames").
  n(62)=35, n(94)=37.
- Standing neighbors: 94='ne' STRONG LEAD (R17-001); 77='le' provisional
  SURVIVES (R20-131); 62's cell absent (R20-125).

The bar's else-arm outcome is already the standing state: @508 is a fenced
residual (N52: "8 clean, @508 fenced residual"; R20-125: "@508 unclean"), and
the distributional-only fence on '62 94' = subject+'ne' HARDENED (R20-125).
This battery changes nothing; it records why the gate must not fire again on
this premise.

## Verdict

**NULL** per §5.2 (contradiction with standing red-team verdicts R19-097 /
R19-106 / R20-125 — escalated). No value named, no registry change requested,
no standing verdict contradicted or downgraded by this battery.

## Follow-ups (both verified ABSENT from battery-queue.json)

1. `ne-508-reseg-rearm` (P3) — Re-test the @507-509 word-internal arm ONLY when
   62's cell is granted at red-team level (value named by red-team ruling, not
   merely battery-promoted). Bar: one coherent word-internal parse of @507-509
   with every pair's syllable role stated and the French word named under the
   granted 62 value; else the arm closes permanently and @508 stays a fenced
   residual.
2. `redteam-gate-trigger-input` (P2) — Red-team evidence package (gather-only):
   the ne-508-reseg-gate62 gate fired on a battery promote that R19-097
   rejected and R20-125 killed permanently. Recommend gate triggers require
   red-team ratification of the gating value, not a battery promote alone.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/ne-508-reseg-gate62.lock` created on
  start (agent 043ba305-8de7-4c28-af39-e52af0995e8a, 2026-10-09T15:29:46Z),
  deleted on completion.
- Queue: `ne-508-reseg-gate62` → `status: verdict`, `result: null`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; own entry only; no downgrade).
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue
  untouched. §7 intact.
