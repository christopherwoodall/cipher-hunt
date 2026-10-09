# Battery verdict: val-41-40-independent

**Verdict: NULL** (no value nameable; qui-licensing gives class only, and the frame itself is phase-contingent).

- Target id: `val-41-40-independent`
- Claim: "name 41 value at @40 via its qui-leg ('qui [41]' frame) independent of 01 — 01-independence by licensing, not by boundary"
- Priority: 3
- Date: 2026-10-09
- Worker: battery worker (subagent 8ee8602d-1652-47fa-b3fc-681b9c1b2718)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs / 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/val-41-40-independent.lock` created on start, deleted on completion.
- Evidence parent: `battery-qui-41-01-boundary.md` NULL 2026-10-09 (follow-up 3 of 3).

## Bar (verbatim from battery-queue.json, pre-registered)

"value named with >=2 independent legs"

Restated as numbered pass/fail clauses (fixed before testing, not modified after):

- **C1:** A specific French word is named as 41's value at @40, forced by the qui-frame licensing.
- **C2:** >=2 independent legs (windows or licensing arguments) force the SAME value.
- **Resolve-arm:** C1 AND C2 pass → promote. **Else-arm:** null (inconclusive) with 1–3 follow-ups per §4.

Adverses listed in queue: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Lock created/deleted as above.
2. Re-derived the repaired stream in-session; byte-verified the @40 locus (1-based @-offsets used throughout, matching lane battery convention).
3. Censused all 19 41-windows for value-forcing frames; tested the qui-licensing argument; tested the qui-frame's phase stability under the rival a1_01 offset.
4. Standing values held fixed per §7. Kills, splits, and the §7 sole-polyvalence rule honored. The split-41-redteam docket (queued, undecided) owns 41's class adjudication — not re-litigated here.

## Window-level evidence (all byte-verified, 1-based @)

### The locus

@37–44, row a1_01, mid-row:

`... 39 [37] 64(qui) [38–39] 41 [@40] 01 [@41] 24(faire) [42] 88 [43] ...`

Raw digits at the locus: `...9139 6441 0124 88...` — the "64 41" span is raw `6441`.

### The qui-licensing argument (class-level)

- 64="qui" is granted (subject relative pronoun, §7).
- In French, subject-"qui" is obligatorily followed by a finite verb phrase.
- At @40, 41 immediately follows "qui" → 41 occupies a finite-verb slot.
- **Class leg: PASS** — 41 is finite-verb-licensed at @40. This is 01-independent in the weak sense: it holds whether "41|01" is a boundary (41 is the verb) or "41-01" is one word (41 is verb-initial).

### Why no VALUE can be named

1. **Licensing gives class, not value.** "qui" requires *a* finite verb; it does not select *which*. Thousands of French finite verbs fit the slot. No letter-tier values exist for 41 at any grade (confirmed: qui-41-01-boundary test (b); letter-41-dist2-tri still running, no results at report time).

2. **The qui-frame itself is phase-contingent.** Row a1_01's repaired offset is 0 (unvalidated; 68 of 70 upstream row offsets unvalidated per the canonicality caveat). Under the rival offset 1, the same raw span re-pairs as `...89 13 96 44 10 12 48...` — the "64 41" frame **dissolves entirely** (verified in-session, byte-exact). The licensing leg exists only under the unvalidated offset choice. Adjudicating the phase is red-team venue (cf. follow-up 1 of qui-41-01-boundary).

3. **41 is class-split stream-wide; a single value needs a §7 ruling.** Census of all 19 windows:
   - Noun arms: @6 "ce [41]ent" ("ce moment"-shaped, battery-41-05-class PROMOTE); @238 "pré-vient [41] fois" (direct object of prévenir; R20 line 332); @1017 "[V-fin] [41] [adv] [inf]" (direct object; R20-108, determiner arm killed there).
   - Finite-verb arm: @40 "qui [41]" (this target).
   - Determiner arm: @238 (battery PROMOTE per 41-05-class, 0-based @237).
   - Remaining 13 windows: no value-forcing frame (predecessors/followers unvalued or non-licensing).
   - Predecessor multiset: 14 distinct (max count 2); follower multiset: 17 distinct (max count 2). Zero repetition to anchor a value.
   
   Naming one French word for 41 across these arms would require either a second polyvalence (§7: 67 et/veut is the SOLE true polyvalence — red-team venue) or a positional split rule (split-41-redteam docket — queued, undecided). Battery must not pre-empt either.

4. **01-independence does not rescue the bar.** Even granting the licensing argument arguendo, it yields "41 is verb-slot-licensed", not a word. The bar demands a named value.

### Per-clause results

- **C1: FAIL.** No specific French word is forced for 41 at @40 by the qui-frame or any other window. (Not kill-grade: the frame is genuine under the standing phase; it underdetermines the value.)
- **C2: MOOT.** With no value named, independent-leg counting does not start.
- **Resolve-arm: not met. Else-arm: TAKEN — null with follow-ups.**

## Adverses

None listed in queue. Honest fences (not kill-grade):
- F-a: The qui class-licensing is real under the standing a1_01 phase but dissolves under the rival phase — the class leg itself carries the canonicality caveat.
- F-b: letter-41-dist2-tri and doublet-41-589 were still running (fresh locks) at report time; their results could supply letter-tier leads this battery could not see.
- F-c: 01="en" local LEAD (R20-016) was deliberately NOT used, per the target's 01-independence instruction. If a future battery licenses "01 24" = "en faire" independently, the @40 verb slot narrows to modal-shaped verbs — still class, not value.

## Verdict: NULL

No standing or red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stated (row a1_01 offset unvalidated; the @40 frame is phase-contingent).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-41-40-classconfirm` (P3) — clean class-level battery: confirm 41's finite-verb CLASS at @40 via the qui-frame (class, not value), with the phase caveat stated; package as input for split-41-redteam. Bar: class named with the qui-frame + one corroborating verb-slot test, phase caveat explicit.
2. `letter-41-qui40-compose` (P4) — once letter-41-dist2-tri lands: test whether any letter lead at @40 composes a finite verb after "qui"; name iff a composed verb parses with zero new assumptions.
3. `a101-phase-40-reaudit` (P4) — if row a1_01's offset is ever adjudicated: re-audit the @40 qui-frame under the decided phase; if offset 1 wins, the qui-leg dissolves and fin-41's @40 leg is void.

## Bookkeeping

- `battery-queue.json`: `val-41-40-independent` queued → verdict/null (temp-file + rename, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated after write).
- Report: `code/crowd17/report_inbox/battery-val-41-40-independent.md`.
- Lock created on start, deleted on completion. No standing verdict contradicted or downgraded. R5005, sealed gates, red-team queue untouched.
