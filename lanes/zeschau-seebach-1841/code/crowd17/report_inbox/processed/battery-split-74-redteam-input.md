# Battery verdict: split-74-redteam-input

- Target: `split-74-redteam-input` (battery-queue.json, priority 2, status queued)
- Claim: "Package 74's split shape (verb forced: 'ne [74]' @350/@786/@1103, 'on [74]' @261; noun forced: 'ce [74]' @1637 with granted 87, 'le [74]' @1307 with provisional 77) for §7 split adjudication."
- Bars: "Package delivered; no battery-level split declaration."
- Mode: **gather-only, no adjudication, no battery-level split declaration.** Per the gather-only precedent, no follow-ups are proposed.

## Verdict: NULL (gather-only package delivered)

**Bar tested (verbatim, pre-registered):** "Package delivered; no battery-level split declaration." →
C1 (package delivered) PASS / C2 (no battery-level split declaration) PASS.

## Package contents

### Standing base (adopted, not re-litigated)

- 94='ne' STRONG LEAD (R17-001); 87='ce' granted; 77='le' provisional; 84='on' granted (A15); 29='er' pencil GT.
- 67 et/veut remains the sole ratified polyvalence (§7 intact).
- 74's class is battery-unresolved: n(74)=34 stream-wide, no global class grant, no value named.

### Arm A — verb-forced windows (battery grade)

All loci byte-verified in-session on the repaired 1,847-pair / 96-type stream (0-based; asserts held; `canonical.py` never used):

- **@350** `70(pre) 12(n) 94(ne) [74] 67 78(ver) 40(e)`: "ne [74]" — 94='ne' before a bare 74 licenses a finite verb only (adopted: val-74-212 C1 — noun/adjective/adverb/letter arms all fail on "[_] le ver"; "ne [74]" finite-verb frame confirmed at @212's locus; transfer of the "ne forces finite verb" frame is battery-grade via subj-74-261-1500's finite-verb-slot finding).
- **@786** `24(verb) 42(noun) 94(ne) [74] 65(noun) 84(on) 06(ent)`: "ne [74]".
- **@1103** `52 82(m) 94(ne) [74] 47(ce) 78(ver) 65(noun)`: "ne [74]".
- **@261** `43(noun) 77(le) 84(on) [74] 45(ce/dict) 93(verb)`: "on [74]" — subject pronoun "on" requires a finite verb (adopted: val-74-212).
- Supporting: subj-74-261-1500 (KILL of the nominal/formula reading — 74 in the finite-verb slot, both subject-frame and inversion-side); ne-alone-02-74 (KILL of the bare-'ne' reading). val-74-212 (NULL, fence executed): 74 is verb-shaped at @212 by local elimination, but the subject-NP licensing arm is fenced.

### Arm B — noun-forced windows (battery grade)

- **@1637** `01 [74]@1635 87(ce) [74]@1637 74@1638 35(noun)`: "ce [74]" at @1636–1637 — granted 87='ce' before 74 forces noun (determiner + bare cell; a verb cannot follow a determiner). NOTE: 74 also occurs at @1635 and @1638 (74×3 contact @1635–1638); only @1637 sits in the "ce [74]" frame.
- **@1307** `21(noun) 43(noun) 77(le) [74]@1307 52 30(pas)`: "le [74]" — provisional 77='le' before 74 forces noun.

### The split shape

- Verb-forced: 5 windows (3× "ne [74]", 1× "on [74]", 1× verb-shaped @212).
- Noun-forced: 2 windows ("ce [74]", "le [74]").
- The two arms are mutually exclusive under uniformity: a uniform 74 cannot be both finite-verb and post-determiner noun. This is the classic §7 conditioned-split shape — parallel to poly-66-split (pour-governed non-finite ×7 vs finite-verb-shaped "66-84" ×2) and the 09 nominal/adverbial split package.
- Residuals: noun-74-census NULL (fenced per bar's else-branch); noun-74-formula NULL; tail-74-78-frame NULL (fence executed — no licensed '74 et 78' frame, residual extended to @352).

### Adjudication question for the red team

Declared split (verb class at the @350/@786/@1103/@261/@212 windows, noun class at @1636–1637 and @1306–1307) vs second polyvalence under §7. No battery decision made; no adverse pending.

## Scope

Gather-only package; no bankable content added beyond the record; §7 intact — no split declared, no value named, no class granted. No standing/red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (rows a2_05, a1_01, a8_04 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-split-74-redteam-input.md`
- Queue: `split-74-redteam-input` queued → `verdict`/`null` 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.split-74-redteam-input.tmp` + atomic rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/split-74-redteam-input.lock`: created on start (agent 81775f03, 2026-10-09T20:01:50Z, no stale lock), deleted on completion (verified gone)
- R5005, sealed gate instances, red-team adjudication queue untouched.
