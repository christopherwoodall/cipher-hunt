# Battery report: ci345-fence-refresh

- Target id: `ci345-fence-refresh`
- Claim: Refresh ci-bound-01's @345 fence statement-of-cause post spell-06-entre-kill: with the verb-ID leg killed and 06's left neighbor open, 06 at @346 is syllabic 'ent' per the attachment rule; the cause is now the "entprenne" non-word, not a stemless ending.
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `code/side-keyhunt/repair_parse.py`); asserts held (1,847 pairs, 96 types). All @-offsets 0-based. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/ci345-fence-refresh.lock` (created on start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"re-state the @345 fence cause using only standing values post-kill; confirm the fence's 01-value-independence under the new mechanism; flag any dependency change for the red-team docket"

## Bar restated as numbered pass/fail clauses

- **C1 (re-state cause):** state the @345 fence cause using only standing values after the spell-06-entre kill. PASS iff the re-stated cause uses no value outside the standing set and does not contradict any standing grant/kill.
- **C2 (01-value-independence preserved):** confirm the fence is identical under 01='ceci' (bound), 01='ce' (free), and 01=open. PASS iff the breakage does not vary with 01's reading.
- **C3 (dependency change flagged):** flag any dependency change vs ci-bound-01's original statement for the red-team docket. PASS iff dependencies are enumerated and any delta is stated (or "none" with cause).

## Standing state adopted (not re-litigated)

- 87='ce' granted; 70='pre' pencil GT; 12='n' promoted letter; 94='ne' R17-001 STRONG LEAD.
- 06='ent' single value (ent-06 PROMOTE; 06-forces-84; ent-06-host-census attachment rule: finite -ent ending iff left neighbor is a verb stem, else syllabic 'ent').
- spell-06-entre KILL (2026-10-09): the 06 "entreprenne" verb-ID leg is dead — 06-70-12-94 spells "entprenne" under every licensed value, which is not French, kill grade. "06-70" is stream-hapax.
- ci-bound-01 (NULL): W3 @345 fenced as 06-driven residual; old mechanism was "ceci followed by a bare verb ending 'ent' with no stem between 01 and 06" plus the then-live "entreprenne" leg. Not -ci-specific; breakage under every reading.
- residual-345-06 (NULL), w1-342-tail-parse (NULL): both adopted; @345 fence's 01-value-independence already checked there.

## Method

1. Read BATTERY-PROTOCOL.md in full first; created lock on start.
2. Re-derived the repaired stream in-session; byte-verified the locus.
3. Re-stated the fence cause under the post-kill standing set; checked 01-value-independence by substitution under each 01 reading.

## Window-level evidence (0-based @)

Byte-confirmed locus @344–352: `87(ce) 01 06(ent) 70(pre) 12(n) 94(ne) 74 67(et) 78` (a2_05 rows @344–350; a2_06 seam @351).

- @346's left neighbor is @345=01, which is open (01's value unnameable outside ce-contexts; ci-01-value KILL on general 'ci'; 01 not a verb stem) → per the 06-attachment rule, 06 is **syllabic 'ent'** here; no finite-ending reading is available at @346.
- 06-70-12-94 = "entprenne" with standing values only (06='ent', 70='pre', 12='n', 94='ne') → non-word, kill grade (spell-06-entre adopted). The "06-70" bigram is stream-hapax.

## C1: refreshed statement of cause — PASS

**Old cause (ci-bound-01 W3, pre-kill):** "ceci followed by a bare verb ending 'ent' with NO stem between 01 and 06 — ungrammatical"; the then-live "entreprenne" verb leg made the clause read as "...ce [01] entreprenne..." with the missing-'que' as a secondary defect.

**New cause (post-kill):** the window breaks on a **bare non-word**, not a stemless ending. Under standing values, @346–349 = "entprenne" ("ent" syllabic per the attachment rule since 01 is open + not a verb stem; "pre" pencil GT; "n" promoted letter; "ne" STRONG LEAD), and "entprenne" is not French under any licensed value combination (spell-06-entre KILL, adopted). The verb-ID reading that made this a verb-slot failure is dead; what remains is a four-cell non-word, so the window is unparseable under every reading — free 'ce', bound 'ceci', or 01 open. No invented values, no contradiction with any standing grant.

## C2: 01-value-independence — PASS

Substitution under each 01 reading, holding the post-kill cause fixed:

- 01='ceci' (bound): "ceci entprenne [74]..." — non-word in the verb slot. Dead.
- 01='ce' (free): "ce [01] entprenne..." — identical non-word. Dead.
- 01=open: same non-word. Dead.

The breakage is invariant to 01's reading because it sits downstream at @346–349. The supporting frame facts are unchanged: kill-grade-dead "ce qui par" left edge (edge-340-31-14 adopted), zero 46='que' in ±20 (adopted from residual-345-06), and @345's open left context. The fence's verdict stands; its independence property is preserved under the new mechanism.

## C3: dependency change — PASS

Original dependencies: ent-06's PROMOTE (06='ent'), plus the then-live "entreprenne" verb leg for the mechanism's flavor.

Current dependencies: (1) ent-06 PROMOTE (06='ent' single value) — unchanged, still load-bearing; if overturned, @345 re-opens (as ci-bound-01 stated). (2) The ent-06-host-census attachment rule — now explicitly load-bearing (it is what rules out the finite-ending reading at @346); it was already standing, so no new dependency. (3) spell-06-entre KILL — newly listed, but it is *derived from* (1)+(standing values), so it adds no independent load-bearing premise; an overturn of (1) would take it down with it.

**Delta for the red-team docket: no new independent dependency.** The fence's support now rests on the same single standing grant as before (ent-06), plus a standing rule (attachment) and a derived kill (spell-06-entre). If ent-06's single-value grant is overturned, @345, ci-bound-01's W3, residual-345-06, and this fence all re-open together.

## Verdict: PROMOTE

All bar clauses pass. The fence's verdict stands with its cause refreshed: the @345 breakage is the "entprenne" non-word at @346–349 (syllabic 'ent' per the attachment rule; the "entreprenne" verb leg is killed), not a stemless ending. 01-value-independence confirmed; no new dependency for the red-team docket beyond the standing ent-06 grant.

## Adverses

Bookkeeping battery per the adverse: the fence's verdict stands — only its stated mechanism was updated. No standing or red-team verdict contradicted, downgraded, or re-litigated. §7 intact.

## Follow-ups

None — bookkeeping target with a deliverable bar; both clauses verified and recorded. The parent battery's companion follow-up `tail-74-78-frame` was already queued by the parent report and is not duplicated.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ci345-fence-refresh.md` (this file).
- Queue: `ci345-fence-refresh` queued → `verdict`/`promote` via target-id-unique temp `battery-queue.json.ci345-fence-refresh.tmp` + atomic rename; own entry only; pre-write assert passed (was queued/verdictless); no downgrade; no tmp leftover; JSON re-validated post-write.
- Lock `code/crowd17/next-token/locks/ci345-fence-refresh.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
