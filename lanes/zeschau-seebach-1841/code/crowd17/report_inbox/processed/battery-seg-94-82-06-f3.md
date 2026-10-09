# Battery report: seg-94-82-06-f3 — value of the second 06 in the 06-06 doublings (NULL — fenced)

**Target:** `seg-94-82-06-f3` (P3)
**Worker:** 92a81052-b85c-43a0-af84-323a38c9195b
**Date:** 2026-10-09
**Parent:** battery-seg-94-82-06.md (NULL, 2026-10-08) — follow-up F3

## Bar (verbatim from battery-queue.json)

> name the second 06's value in the 06-06 doubling frames

## Bar restated as numbered clauses (pre-registered before testing, from the queue bar + F3's scoped test)

1. Both "06-06" doublings exist on the repaired 1,847-pair stream at the stated positions.
2. The "ent ent" (two-word) reading parses both doubling windows with ≤1 ungranted assumption — then the second 06's value is named.
3. Else the new-word "ent…" reading parses both doubling windows with ≤1 ungranted assumption — then the second 06's value is named.
4. Else the second 06's value is fenced with stated cause; no standing red-team verdict is contradicted or downgraded.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/seg-94-82-06-f3.lock` (deleted on completion). Re-derived the repaired 1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (byte-exact tokenizer per repair_parse.py; asserts hold: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. Parent report and sibling follow-ups (f1, f2 — both NULL, in `report_inbox/processed/`) read, not duplicated.

Standing values used as premises only: 94="ne" (R17-001 STRONG LEAD), 82="m" (banked GT letter), 06₁="ent" (F61 conditioned islet, pre=82), 59="est" (provisional; locally confirmed as 'est'-as-word at @1186 by f1 NULL), 84="on" (A15), 46="que" (banked GT). An "ungranted assumption" = any value, edge rule, or frame reading not in protocol §7 or a red-team-adjudicated finding.

## Window-level evidence (0-based pair indices)

**Clause 1 — census: PASS.** "06-06" occurs exactly 2× stream-wide on the repaired stream: 0-based @580 (row a3_02) and @1184 (row a6_10) — matching the parent battery's census exactly.

- Frame A @580 (a3_02, row-internal): `…94 82 06 | 06 50 10 19 18 14 00` (full: `94 52 87 78 45 13 55 61 [94 82 06] 06 50 10 19 18 14 00 97`). Second 06 at @581; right follower 50 (value open).
- Frame C @1184 (a6_10): `…94 82 06 | 06 59 42 06 84 59 46` (row a6_10→a7_00 join). Second 06 at @1185; right followers 59 ('est', f1-confirmed), 42 (open), 06 (standalone "ent" per ent-right-attach-sweep KILL), 84 ("on"), 59, 46 ("que" GT).

The first 06 sits inside the F61 islet (pre=82 → 'ent'); the second 06 is outside it (pre=06). F61's scope is unchanged.

**Clause 2 — "ent ent" two-word: FAIL at kill grade.** "ne ment ent [X]" at both windows requires "ent" to be a standalone French word. French has no such word (no 1841 attestation possible — the lexicon is fixed). This is value-independent: no assumption, granted or ungranted, can license a bare "ent" word at either window. The two-word reading is dead.

**Clause 3 — new-word "ent…": FAIL (bar's ≤1-assumption threshold).**
- Frame A: "ne ment ent[50]…" needs 50's value (open) AND a licensed French word of the shape "ent"+50 = ≥2 ungranted assumptions.
- Frame C: "ne ment ent[59]…" needs a 59 override (f1 just battery-confirmed 59="est"-as-word at @1186 and held the F66 fence — overriding it contradicts a battery-confirmed local reading) AND 42's value (open) = ≥2 ungranted assumptions plus a contradiction.

Neither reading meets the decision bar at either window.

**Clause 4 — adverses answered — PASS.** 94="ne" untouched. F61 islet unchanged (first 06 covered; second outside scope — that is the question, not a change). F72's H4g refutation not re-run (per F3's adverse). F66's frame-C fence not re-litigated (f1 confirmed it locally). No polyvalence declared (§7 intact — homophony not at issue here). No standing or red-team verdict contradicted or downgraded.

**Canonicality caveat:** both doublings are canonical-offset objects (rows a3_02, a6_10 carry unvalidated upstream offsets). Verdict holds on the canonical stream per protocol; offset adoption is a red-team act.

**Residual (not a bar failure):** the bar scoped both readings to second-06='ent'. A second 06 with a non-'ent' value was never tested; 06's global value ('ent' promoted) argues against it, but the doubling context is exactly where a distinct value could hide. Proposed as follow-up #1.

## Verdict: NULL — second 06's value fenced

- "ent ent" (two-word): kill-grade dead — no standalone French word "ent" exists.
- New-word "ent…": unfalsified but unnameable within the ≤1-assumption bar (frame A needs 50's value; frame C is blocked by f1's battery-confirmed 59='est' and open 42).
- Second 06's value stays fenced. The F61 islet's scope question ("which 06s does 'ent' cover") remains open for the red team.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `second-06-nonent` (P3): test second-06 ≠ 'ent' at both doublings — the bar scoped both readings to 'ent'; a non-'ent' second 06 (syllabic or whole-word value) was never tested. Bar: name a value parsing both windows with ≤1 ungranted assumption.
2. `frameA-50-value` (P3): name 50's value — the sole right follower of the @580 doubling; unlocks the new-word "ent…" reading at frame A via a licensed French word.
3. `w580-subject-61` (P4): name 61's value at frame A; if a plural subject, the one-word "mentent" re-read gains a leg (red-team venue per F72/F66 — coordinate, do not re-declare).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/seg-94-82-06-f3.lock` created 2026-10-09T08:03Z, deleted on completion (verified gone).
- `battery-queue.json`: `seg-94-82-06-f3` queued → verdict/null (temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated; own entry only).
- R5005, sealed gates, red-team adjudication queue untouched. `canonical.py` never used.
