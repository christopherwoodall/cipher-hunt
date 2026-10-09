# Battery report: reinforced-pour-inf-recall

- Target id: `reinforced-pour-inf-recall`
- Claim: "re-run the reinforced-head + governed exclamatory infinitive search with recall gaps closed"
- Date: 2026-10-09
- Worker: battery worker (subagent c97d61d0-f222-4de0-a519-dbf168ee141a)
- Stream: not applicable — corpus census against period French, per target
  charter. The 1,847-pair repaired parse was not used. R5005, sealed gate
  instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked
with -là or -ci (celui-là, ceux-là, celle-là, celles-là, celui-ci,
ceux-ci, celle-ci, celles-ci). "Exclamatory infinitive" = an infinitive
used as an exclamation ("Moi, me taire !"). "Governed" = the infinitive
is governed by a preposition (pour / à / de). "Recall gap" = a window the
parent battery never searched, so its zero is not evidence of absence.

## Parentage

Follow-up #1 of the NULL `reinforced-pour-inf-diagnostic` (2026-10-09).
That battery fenced reinforced-head + governed exclamatory infinitive
(0/4 genuine) but fenced two recall gaps as limitations: (a) P1 admitted
only [,;:] after the head — dash/parenthesis pause marks were never
searched; (b) the 180-char window cap dropped 73/231 windows with no
sentence end in-window. This battery is a DIFFERENT search, not a
re-run: it targets only the previously unsearched windows.

## Bar (verbatim, pre-registered before testing)

">=1 genuine attestation in the widened search re-opens the pairing; confirmed zero closes the recall gap and hardens the fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE reinforced-demonstrative head + governed
   exclamatory infinitive ("celui-là — pour rire !") exists among the
   previously unsearched windows in the 27.66M-char corpus. If yes: the
   pairing re-opens.
2. If the widened census is a confirmed zero — every candidate window
   classified, the 4 already-classified candidates excluded from
   re-classification — the recall gap is closed and the fence hardens.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/reinforced-pour-inf-recall.lock` on
   start (agent id + UTC timestamp 2026-10-09T08:32:22Z; no stale lock
   for this id existed); deleted on completion.
2. Ran a reproducible recall census script:
   `code/crowd17/next-token/reinforced_pour_inf_recall_census.py`
   (same corpus + DEM_REINF inventory as the diagnostic, new recall
   P1/P2). Raw results in
   `code/crowd17/next-token/reinforced-pour-inf-recall_census.json`.
3. Corpus, byte-identical to the diagnostic (sizes re-verified on disk
   this session — exact match, no drift):
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
   - RECALL P1 (pause mark): `\s*(?:[,;:]|[—–-]|\()` — admits
     comma/semicolon/colon (old shape), em/en-dash and hyphen pause
     marks, and opening parenthesis after the head.
   - Already-searched exclusion: an old-style `[,;:]` occurrence whose
     180-char window contains any sentence end `[!?.]` was searched by
     the diagnostic (158 occurrences incl. the 4 classified candidates)
     and is EXCLUDED from this census. No window is classified twice.
   - RECALL P2 (exclamatory filter): the window must contain "!" before
     its end.
   - Window = text from the demonstrative through the next `[!?.]`
     (inclusive), NO 180-char cap (sanity ceiling 4000 chars; no
     candidate hit it).
   - RECALL P3 (governed-infinitive candidate): same
     `\b(pour|à|a|de|d['’])\s+(?:...){0,2}\b...{2,}(er|ir|re|oir)\b`
     as the diagnostic, applied to window text after the pause mark,
     case-insensitive. Candidates printed for manual classification.
5. Recall-set audit (reproduced in-session, independent of the script's
   own counts): the diagnostic's 206 old-style dem-comma hits in the
   1841 register split into 140 searched + 66 dropped; the wider
   register's 25 split into 18 searched + 7 dropped. 66 + 7 = 73 —
   exactly the diagnostic's 73 dropped windows. Dash/paren pause marks
   add 1 occurrence in the 1841 register (a footnote marker
   "ceux-ci (1)") and 0 in the wider register.

## Window-level evidence

### Census yields

- Recall occurrence set: 67 (1841 register) + 7 (wider 19c) = 74
  previously unsearched reinforced-head occurrences.
  - 73 = the diagnostic's dropped windows, searched uncapped (new
    windows end at the true next sentence end, up to 4000 chars).
  - 1 = the dash/paren pause-mark occurrence ("ceux-ci (1)", a
    footnote marker in revue-deux-mondes-1841-q3 — not a dislocation).
- **0 of the 74 recall windows contains an exclamation mark anywhere
  in its full (uncapped) window through the next sentence end.**
  The exclamatory filter (P2) excludes every recall window before the
  governed-infinitive filter is ever applied — this is a confirmed
  zero by construction, not a classification judgment.
- 0 governed-infinitive candidates; nothing to hand-classify.
- The 4 diagnostic candidates were excluded from this census by the
  already-searched rule (their windows carried sentence ends within
  180 chars); they are not re-classified here.

### Due-diligence checks

- The reinforced-head inventory is real in this corpus (231 dem-comma
  hits across both registers; 232 with the footnote occurrence) — the
  zero is not an empty-search artifact.
- The pause-mark widening added almost nothing: only 1 dash/paren
  occurrence in 27.66M characters (a footnote marker). 1841 French
  print dislocates reinforced heads almost exclusively with
  comma/semicolon/colon.
- The uncapped windows genuinely re-opened the search space: the 73
  dropped windows were searched to their true sentence ends (no
  candidate hit the 4000-char ceiling). None was exclamatory.
- The zero is therefore no longer an absence-in-unsearched-space: all
  232 reinforced-head + pause-mark occurrences in the corpus have now
  been searched for the governed exclamatory shape (158 by the
  diagnostic + 74 here), and 0 of 232 show the pairing.
- No genuine "celui-là — pour rire !" shaped window exists even with
  the loosened pause inventory: the whole corpus is now covered.

## Per-clause pass/fail

1. ≥1 genuine attestation in the widened search re-opens the pairing:
   **FAIL (confirmed zero).** 74/74 previously unsearched windows
   classified by construction (0 carry "!", 0 governed-infinitive
   candidates); the 4 already-classified candidates correctly excluded.
2. Confirmed zero → recall gap closed, fence hardens:
   **EXECUTED.** All 232 reinforced-head + pause-mark occurrences in
   27.66M characters are now searched for the governed exclamatory
   infinitive; 0 attest it. Per §4 this is a **null**, not a kill
   (zero is an absence, not a refutation — no window forces the claim
   false).

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this null contradict the parent NULL
  (reinforced-pour-inf-diagnostic)? No — it closes its fenced
  limitation exactly as chartered (the parent's follow-up #1). The
  fence at the reinforced head now stands on the complete corpus,
  not on 68.3% of it.
- Self-check: does this null contradict the standing NULL
  (gov-excl-inf-register, any-topic governed exclamatory census)?
  No — different inventory (reinforced heads vs any topic); both
  nulls point the same way (the construction does not pair with
  reinforced demonstratives anywhere in the corpus).
- §5.2: no standing red-team verdict touched; no overwrite, no
  escalation required.

## Verdict: NULL (recall gap closed; fence hardens)

Zero reinforced-head + governed exclamatory infinitive attestations
across the complete 232-occurrence inventory (158 searched by the
diagnostic, 74 searched here uncapped) in 27,657,940 characters of
19th-century French. The diagnostic's two recall gaps are closed: the
pause inventory adds exactly one occurrence (a footnote marker), and
the 73 dropped windows are confirmed non-exclamatory at their true
sentence ends. Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **reinforced-pour-inf-zeropause** (P3): search reinforced head
   directly followed by governed infinitive with NO pause mark at all
   ("celui-là pour rire !"). Both batteries required a pause mark
   ([,;:]/dash/paren) after the head; zero-pause dislocation is
   unsearched. Bar: ≥1 genuine attestation re-opens the pairing;
   confirmed zero extends the fence to the zero-pause shape.
2. **reinforced-pour-inf-interro** (P3): admit "?" as the exclamatory
   termination mark in the recall windows (rhetorical-question shape:
   "celui-là, pour croire ?"). Both batteries required "!" in-window;
   "?" windows were filtered out. Bar: ≥1 genuine attestation
   re-opens; confirmed zero closes the punctuation gap.
3. **reinforced-pour-inf-widercorpus** (P3): run the governed-infinitive
   census (diagnostic P1–P3, no recall needed — this target already
   covers the lane corpus) against a second 19th-century French corpus
   (e.g. Gutenberg Balzac/Zola, named in the worker brief). Bar:
   ≥1 genuine attestation re-opens; confirmed zero hardens the fence
   beyond the lane corpus to 19th-century French generally. (Distinct
   from gov-excl-inf-register, which tested ANY topic — this is the
   reinforced-head inventory on new ground.)

## Bookkeeping

- Census script:
  code/crowd17/next-token/reinforced_pour_inf_recall_census.py
  (re-runnable; same corpus + DEM_REINF inventory as the diagnostic;
  outputs reinforced-pour-inf-recall_census.json with per-file sizes,
  recall-occurrence counts, and candidates).
- Report: code/crowd17/report_inbox/battery-reinforced-pour-inf-recall.md
  (this file).
- battery-queue.json: `reinforced-pour-inf-recall` queued ->
  verdict/null via temp-file + rename (own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp
  2026-10-09T08:32:22Z), deleted on completion. No stale lock for
  this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus files or the census script; no invented data.
