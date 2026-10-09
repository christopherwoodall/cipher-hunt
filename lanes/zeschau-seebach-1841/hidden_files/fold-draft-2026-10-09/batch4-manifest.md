# Batch 4 manifest (2026-10-09 UTC, 6 reports)

Third batch continues from F279/N376 already inserted. All F-numbers (F280,
F281) and N-numbers (N377–N380) verified free via grep before assignment
(`**F280**`…`**N380**`, 0 hits each in REPORT.md). All 6 battery names
verified absent from REPORT.md (0 hits each). REPORT.md NOT edited, inbox
files NOT moved, no push.

## Verdicts

| Report | Verdict | Section | Number |
|---|---|---|---|
| battery-letter-41-dist2-tri.md | NULL (fence fires — keep 41 outside letter tier) | §5 failures/nulls | N377 |
| battery-syll-39-de-host.md | KILL (@1334 '-de'-final-verb leg dead) | §5 failures/nulls | N378 |
| battery-syll-83-de-1829.md | NULL (verb fork fenced, noun fork live) | §5 failures/nulls | N379 |
| battery-val-08-successor-class.md | PROMOTE (31 split; 62/65/21/43 noun; 08 word-internal 't'; particle killed) | §4 findings | F280 |
| battery-val-42-ne-noun.md | KILL ([42ne]-as-noun-word dead, inventory exhausted) | §5 failures/nulls | N380 |
| battery-val-52-630-frame.md | PROMOTE (52 non-verbal sub-lexical at @630; "et 08 [52-V]" killed) | §4 findings | F281 |

## Uncertain calls / caveats

- **syll-83-de-1829 NULL vs KILL:** the report argues NULL per precedent
  ("name X or fence" bars that fence resolve to NULL when the claim itself
  is not falsified) — the '-de'-final-word fork survives on the noun arm.
  Followed the report's verdict; the verb-fork fence is kill-grade in any
  case.
- **"prière" (41=p) is a lead, not a finding:** letter-41-dist2-tri's best
  reading is explicitly not kill-grade (underdetermined segmentation,
  value-open 08). Folded under N377's null entry and the hypotheses
  subsection — never as a value claim.
- **val-52-630-frame is conditional on battery-grade 08='t':** the report
  states the premise explicitly and corroborates it distributionally (08
  never standalone in 18/18 windows). Flagged in F281 and hypotheses.
- **val-42-ne-noun kill scope:** closes the one-word [42ne] composition
  entirely (noun was the only live class); the three '42 94' windows are
  forced into composition (b) "[42-N] + ne(clausal) + X". This is the
  report's consequence — folded in §6, not as a new parse claim.
- **Gate rule check:** no gate claims in any of the 6 reports; verified
  against `code/crowd17/report_inbox/processed/next-token-redteam-r20.md`.
  No gate satisfied, none armed or fired by this batch. 62='il' kill
  (R19-106/R20-125) stands — ne-508-reseg-gate62 stays refused.
- **ASD-STE100:** entries use short sentences and simple words; terms
  defined on first use where new.
