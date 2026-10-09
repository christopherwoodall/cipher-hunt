# Battery report: reinforced-pour-inf-zeropause

- Target id: `reinforced-pour-inf-zeropause`
- Claim: "head + governed infinitive with NO pause mark ('celui-la pour rire !')"
- Date: 2026-10-09
- Worker: battery worker (subagent 16edcd29-467e-443d-827f-47e5d3bbe172)
- Stream: not applicable — corpus census against period French, per target
  charter. The 1,847-pair repaired parse was not used. R5005, sealed gate
  instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked
with -là or -ci (celui-là, ceux-là, celle-là, celles-là, celui-ci,
ceux-ci, celle-ci, celles-ci). "Governed infinitive" = an infinitive
governed by a preposition (pour / à / de). "Zero pause" = the head is
followed by no pause mark at all (no comma/semicolon/colon, dash, or
parenthesis) before the governed material. "Genuine" = the shape the
bar tests: reinforced head + governed infinitive + exclamatory
termination ("celui-là pour rire !").

## Parentage

Follow-up #1 (P3) of the NULL `reinforced-pour-inf-recall`
(2026-10-09). The diagnostic and recall batteries both required a pause
mark ([,;:]/dash/paren) after the head; the zero-pause construction was
unsearched. This battery searches it.

## Bar (verbatim, pre-registered before testing)

">=1 genuine attestation re-opens the pairing; confirmed zero keeps the fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE reinforced-demonstrative head + governed
   exclamatory infinitive with NO pause mark ("celui-là pour rire !")
   exists in the 27.66M-char corpus. If yes: the pairing re-opens.
2. If the zero-pause census is a confirmed zero — every candidate
   window classified — the fence extends to the zero-pause shape.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/reinforced-pour-inf-zeropause.lock`
   on start (agent id + UTC timestamp 2026-10-09T08:38:14Z; no stale
   lock for this id existed); deleted on completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/reinforced_pour_inf_zeropause_census.py`
   (same corpus + DEM_REINF inventory as the diagnostic and recall;
   new zero-pause P1/P2/P3). Raw results in
   `code/crowd17/next-token/reinforced-pour-inf-zeropause_census.json`.
3. Corpus, byte-identical to the diagnostic and recall (sizes
   re-verified on disk this session — exact match, no drift):
   - 1841-register lane corpus (French files only): 18 files,
     25,670,258 characters — guizot-memoires t1/t2/t3/t5-t6, nesselrode
     v7/v8/v9/v10, revue-deux-mondes-1841 q1/q2/q3/q4,
     metternich-papiere v4/v6, talleyrand-memoires-v1,
     pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3.
   - Wider 19th-century register: 3 files, 1,987,682 characters —
     data/gutenberg-17489-miserables1.txt (Les Misérables tome 1, 1862),
     data/gutenberg-30513-tocqueville-t1.txt (Démocratie en Amérique t1,
     1835), data/gutenberg-30514-tocqueville-t2.txt (t2, 1840).
   - Total: 21 files, 27,657,940 characters of 19th-century French.
   - German files excluded with cause (same as the diagnostic).
4. Search patterns (verbatim, from the script):
   - HEAD inventory (unchanged): `DEM_REINF` = the eight reinforced
     heads (+ ça-là/ci forms), case-insensitive.
   - ZERO-PAUSE P1: after the head, skip whitespace; the first
     non-space character must NOT be a pause mark
     (`,;:—–-()[]«»"'’`). Implemented manually (not as one regex)
     after an initial lookahead version leaked pause-mark hits via
     `\s*` backtracking (e.g. "celle-ci : Bon Dieu" — caught in
     review, fixed before the reported run; the leak only ever moved
     pause-mark hits INTO the zero-pause set, never the reverse).
   - P2 (exclamatory filter): the window must contain "!" before its
     end.
   - Window = text from the demonstrative through the next `[!?.]`
     (inclusive), NO 180-char cap (sanity ceiling 4000 chars; no
     candidate hit it).
   - P3 (governed-infinitive candidate): same
     `\b(pour|à|a|de|d['’])\s+(?:...){0,2}\b...{2,}(er|ir|re|oir)\b`
     as the diagnostic, applied to window text after the head,
     case-insensitive. Candidates printed for MANUAL classification.
     A "tight" sub-flag marks hits beginning within 60 chars of the
     head end (the "celui-là pour rire !" shape).

## Window-level evidence

### Census yields

- Zero-pause occurrence set: 831 (1841 register) + 98 (wider 19c) =
  **929** previously unsearched reinforced-head occurrences. (For
  reference: the pause-mark inventory stood at 232; the zero-pause
  shape is ~4x more common.)
- P2/P3 candidate set: 5 windows (all in the 1841 register; 0 in the
  wider register). 0 candidates hit the 4000-char ceiling.
- Hand classification of the 5 candidates (file @ offset):
  1. guizot-memoires-t3 @677865 "Ceux-ci sont purs et braves; ...
     de servir leur patrie; ... à Alger!" — head is the subject of
     the FINITE verb "sont"; "de servir" is governed by "faculté",
     "à Alger" has no infinitive. Not genuine.
  2. nesselrode-v7 @210608 "celle-ci suffiraient pour rendre célèbre
     une administration; ... !" — head subject of finite
     "suffiraient"; "pour rendre" governed by that verb, not by the
     head. Not genuine. (Tight flag set.)
  3. nesselrode-v9 @451769 "Celle-ci nous a bien attristés; ... destiné
     à disparaître !" — "à disparaître" governed by "destiné" deep in
     the window. Not genuine.
  4. revue-deux-mondes-1841-q2 @602576 "celui-ci propose, et de traiter
     avec lui d'égal à égal!" — head subject of finite "propose";
     "de traiter" coordinated to it. Not genuine. (Tight flag set.)
  5. revue-deux-mondes-1841-q4 @847271 "celui-ci se fût tenu à ce
     premier triomphe!" — regex false positive: "à ce premier" has no
     infinitive ("premier" ends in -er). Not genuine.
- **0 of 929 zero-pause windows carries a genuine head + governed
  exclamatory infinitive.**

### Due-diligence checks

- The zero-pause inventory is real (929 occurrences; sampled contexts
  are ordinary head+finite-verb or head-at-sentence-end shapes) — the
  zero is not an empty-search artifact.
- Exact-shape sweep (independent of the candidate pipeline): 74 of
  the 929 occurrences have the head DIRECTLY followed by a
  preposition; of those, 16 have the preposition directly followed by
  an infinitive (e.g. guizot-memoires-t1 @466086 "celle-ci pour
  conquérir le droit, celle-là pour retenir le privilège.",
  revue-deux-mondes-1841-q1 @168528 "ceux-ci pour moudre le grain,
  ceux-là pour scier les planches..."). **All 16 are non-exclamatory
  ("." termination)** — the zero-pause governed infinitive exists in
  declarative prose, but the EXCLAMATORY pairing ("celui-là pour rire
  !") has zero attestations.
- The 16 declarative attestations were separately re-scanned with a
  2000-char frame: none carries "!" anywhere after the head before
  the window's sentence end.

## Per-clause pass/fail

1. ≥1 genuine attestation re-opens the pairing: **FAIL (confirmed
   zero).** 5/5 candidates hand-classified non-genuine; the exact-shape
   sweep (74 head+preposition, 16 head+preposition+infinitive) finds 0
   with exclamatory termination.
2. Confirmed zero → fence extends to the zero-pause shape:
   **EXECUTED.** All 929 zero-pause reinforced-head occurrences in
   27,657,940 characters are now searched for the governed
   exclamatory infinitive; 0 attest it. Per §4 this is a **null**,
   not a kill (zero is an absence, not a refutation — no window
   forces the claim false).

## Adverses, answered

- None pre-registered ("Adverses: null").
- Self-check: does this null contradict the parent NULL
  (reinforced-pour-inf-recall)? No — it closes its chartered
  follow-up #1 exactly. The reinforced head now stands fenced under
  the complete pause-mark inventory (232, both batteries) AND the
  complete zero-pause inventory (929, this battery).
- Self-check: does this null contradict the standing NULL
  (gov-excl-inf-register)? No — different inventory (reinforced
  heads vs any topic); both nulls point the same way.
- §5.2: no standing red-team verdict touched; no overwrite, no
  escalation required.

## Verdict: NULL (zero-pause searched; fence extends)

Zero genuine reinforced-head + governed exclamatory infinitive
attestations across all 929 zero-pause occurrences in 27,657,940
characters of 19th-century French. The declarative zero-pause
governed infinitive exists (16 attestations), but the exclamatory
pairing does not. Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **reinforced-pour-inf-interro** (P3): admit "?" as the exclamatory
   termination mark across both inventories (pause-mark 232 + this
   battery's zero-pause 929) — rhetorical-question shape
   ("celui-là, pour croire ?"). Both battery generations required
   "!" in-window; "?" windows were filtered out. Bar: ≥1 genuine
   attestation re-opens the pairing; confirmed zero closes the
   punctuation gap.
2. **reinforced-pour-inf-widercorpus** (P3): run this battery's
   zero-pause census (verbatim script + DEM_REINF inventory, no
   recall needed) against a second 19th-century French corpus (e.g.
   Gutenberg Balzac/Zola, named in the worker brief). Bar: ≥1
   genuine attestation re-opens; confirmed zero hardens the fence
   beyond the lane corpus to 19th-century French generally. (Distinct
   from gov-excl-inf-register, which tested ANY topic — this is the
   reinforced-head inventory on new ground.)
3. **reinforced-pour-inf-adjacent-excl** (P3): re-examine the 16
   declarative head+preposition+infinitive windows found here with a
   ±500-char frame for an adjacent exclamatory clause sharing the
   head ("celle-ci pour conquérir le droit !") — rules out the recall
   gap "the exclamation lives in the next sentence". Bar: ≥1
   genuine attestation re-opens; confirmed zero hardens the fence.

## Bookkeeping

- Census script:
  code/crowd17/next-token/reinforced_pour_inf_zeropause_census.py
  (re-runnable; same corpus + DEM_REINF inventory as diagnostic and
  recall; outputs reinforced-pour-inf-zeropause_census.json with
  per-file sizes, zero-pause counts, and candidates). One bug caught
  and fixed in review: the first ZERO_P1 lookahead version leaked
  pause-mark hits via `\s*` backtracking; the reported numbers come
  from the fixed manual-skip version.
- Report: code/crowd17/report_inbox/battery-reinforced-pour-inf-zeropause.md
  (this file).
- battery-queue.json: `reinforced-pour-inf-zeropause` queued ->
  verdict/null via temp-file + rename (own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp
  2026-10-09T08:38:14Z), deleted on completion. No stale lock for
  this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus files or the census script; no invented data.
