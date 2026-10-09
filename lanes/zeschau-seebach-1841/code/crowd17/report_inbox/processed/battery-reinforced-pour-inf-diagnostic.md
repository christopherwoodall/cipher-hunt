# Battery report: reinforced-pour-inf-diagnostic

- Target id: `reinforced-pour-inf-diagnostic`
- Claim: "test whether reinforced heads license the EXCLAMATORY infinitive
  when the infinitive is governed ('celui-la, pour rire !' shape)"
- Date: 2026-10-09
- Worker: battery worker (subagent 81a46d47-eb23-43d0-bc2b-ca1f3f56b961)
- Stream: not applicable — corpus census against period French, per target
  charter. The 1,847-pair repaired parse was not used. R5005, sealed gate
  instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked
with -là or -ci (celui-là, ceux-là, celle-là, celles-là, celui-ci,
ceux-ci, celle-ci, celles-ci), as opposed to the bare tonic heads (cela,
ceci, ça). "Exclamatory infinitive" = an infinitive used as an
exclamation ("Moi, me taire !" = "me, to shut up!"). "Governed" = the
infinitive is governed by a preposition (pour / à / de), as in
"celui-là, pour rire !". "Genuine attestation" = the reinforced head
actually governs/heads an exclamatory infinitive: the infinitive is the
exclaimed phrase, not embedded in a downstream finite clause.

## Parentage

Follow-up #3 of the NULL `disloc-demonstrative-reinforced` (2026-10-09).
That battery fenced reinforced-head + BARE exclamatory infinitive
(0/7 genuine; 231 reinforced heads occur in topic position). Its
near-misses were all preposition-governed infinitives (pour/à/de).
This battery asks whether loosening "bare" to "governed" licenses the
pairing. Does not duplicate `disloc-demonstrative-inf` (bare tonic
heads, bare infinitive), `disloc-demonstrative-reinforced` (bare
infinitive), `disloc-demonstrative-drama` (bare heads, drama corpus),
or `dislocation-ce-sweep` (bare atonic "ce").

## Bar (verbatim, pre-registered before testing)

">=1 genuine attestation pinpoints the fence exactly at the governed-vs-bare infinitive line"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated reinforced-demonstrative head
   (celui-là / ceux-là / celle-là / celles-là / celui-ci / ceux-ci /
   celle-ci / celles-ci) + governed exclamatory infinitive ("celui-là,
   pour rire !") exists in the 27.66M-char corpus. If yes: the fence is
   pinpointed exactly at the governed-vs-bare infinitive line (the
   topic is licit; only the bare construction is blocked).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends and OCR excluded with cause — the whole
   reinforced-head pairing stays fenced (null per §4: zero is an
   absence, not a refutation).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/reinforced-pour-inf-diagnostic.lock` on
   start (agent id + UTC timestamp; no stale lock for this id existed);
   deleted on completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/reinforced_pour_inf_diagnostic_census.py`
   (same corpus + DEM_REINF inventory as
   `disloc_demonstrative_reinforced_census.py`, new P3 governor filter).
   Raw results in
   `code/crowd17/next-token/reinforced-pour-inf-diagnostic_census.json`.
3. Corpus, identical to disloc-demonstrative-inf/-reinforced (character
   counts recomputed in-session):
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
   - German files excluded with cause (register is French, not 1841
     French): allgemeine-zeitung-augsburg-1841-01-11 through -01-24
     (14 files) and adb-zeschau-heinrich-anton-von.txt.
4. Search patterns (verbatim, from the script):
   - P1 (dislocation): `DEM_REINF\s*[,;:]` where DEM_REINF =
     `((?:celui|ceux|celle|celles)[-–— ]?(?:l[àa]|ci)|ça[-–— ]?(?:l[àa]|ci))`,
     case-insensitive — hyphen or space forms of the eight reinforced
     heads. Window = text from the demonstrative through the next
     sentence-ending `[!?.]`, capped at 180 characters.
   - P2 (exclamatory filter): the window must contain "!" before its end.
   - P3 (governed-infinitive candidate): `\b(pour|à|a|de|d['’])\s+
     (?:[a-zàâäçéèêëîïôöùûü'-]{1,6}\s+){0,2}
     \b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b` applied to the window
     text AFTER the comma, case-insensitive: a preposition (pour/à/a/
     de/d') + up to two short tokens (clitics, articles, pronouns —
     m', l', en, y) + an infinitive-shaped word. All candidates were
     classified by hand (regex cannot separate -er infinitives from
     nouns/adjectives in -er; unaccented "a" is verb-avoir noise).
5. Recall due-diligence: of the 231 dem-comma hits, 73 are truncated at
   the 180-char cap with no sentence-end at all inside the window and
   are dropped by P2. This is a genuine recall gap (a governed
   exclamatory infinitive beyond 180 chars would be missed); it is
   fenced as a limitation below and becomes follow-up #1's target.

## Window-level evidence

### Census yields

- 1841 register: 206 dem-comma hits → 4 governed-infinitive exclamatory
  candidates. Wider 19c: 25 dem-comma hits → 0 candidates.
- **0 of 4 candidates is genuine.** All four are the exact windows the
  parent battery excluded from the bare census; re-classified here
  against the governed shape (windows verbatim; "/" marks line breaks):

1. `celle-ci,  je  me  suis  convaincu  qu'il  n'y  a /
   aucun  inconvénient  à  en  donner  lecture  in  extenso  ; /
   qu'il  y  a  même  nécessité  à  le  faire,  puisqu'il  en  es!`
   (nesselrode-v10) — "celle-ci" is the subject of a finite clause
   ("je me suis convaincu que..."). The infinitives "donner" and
   "faire" are "à"-governed inside embedded nominals ("aucun
   inconvénient à en donner lecture"; "nécessité à le faire"). No
   exclamatory infinitive is headed by the topic; the "!" is
   sentence-terminal punctuation of the whole reporting clause.
   Excluded with cause.
2. `celle-ci, / de  celle-là,  et  comme  on  a  vite  fait  de  faire
   penser / hommes  et  femmes  sur  toute  chose!` (nesselrode-v8) —
   "de faire penser" is "de"-governed inside the fixed expression "on
   a vite fait de faire penser", embedded in the finite comparative
   clause "comme on a vite fait de...". The reinforced head sits in a
   topic chain ("celle-ci, de celle-là"), not as the head of an
   exclaimed infinitive. The "!" marks the sentence end; "faire
   penser" is not an exclamation. Excluded with cause.
3. `celle-là,  et  comme  on  a  vite  fait  de  faire  penser /
   hommes  et  femmes  sur  toute  chose!` (nesselrode-v8) — same
   sentence as #2 (sibling topic in the same chain); identical cause.
   Excluded with cause.
4. `celle-ci  :  Bon / Dieu ,  béni  sois-tu  pour  m'avoir  donné  de
   bons  yeux!` (revue-deux-mondes-1841-q1) — "celle-ci:" introduces a
   quotation/vocative (a prayer). "m'avoir" is a past infinitive
   governed by "pour" inside the prayer itself; the head "celle-ci"
   does not govern it. Not the "celui-là, pour rire !" shape.
   Excluded with cause.

### Due-diligence checks

- The reinforced-head inventory is real in this corpus: 231
  dem-comma hits, so the zero is not an empty-search artifact — the
  heads exist in topic position; they never head an exclamatory
  infinitive, bare or governed.
- The governed corpus signal is otherwise real: "pour/à/de +
  infinitive" is frequent in the corpus (hundreds of occurrences,
  e.g. "à en donner lecture"), but it never pairs with a reinforced
  demonstrative head in exclamatory shape. The zero is therefore
  specific to the HEAD pairing, not a gap in governed infinitives
  generally.
- Limitation fenced with cause: P1 admits only [,;:] after the head,
  and P2's 180-char cap drops 73/231 windows (31.7%) with no sentence
  end in-window. Dash- or colon-delimited dislocations ("celui-là —
  pour rire !") and long sentences fall outside this census — they are
  not zero-evidence, they are unsearched. Follow-up #1 closes this.
- No genuine "celui-là, pour rire !" shaped window was found even
  with generous classification: windows #1–#4 are the only
  reinforced-head + governed-infinitive + "!" windows in 27.66M
  characters, and none is headed by the topic.

## Per-clause pass/fail

1. ≥1 genuine reinforced-head + governed-exclamatory-infinitive
   attestation in the 27.66M-char corpus: **FAIL (confirmed zero).**
   4/4 candidates classified; 0 genuine in 27,657,940 characters.
2. Confirmed zero → whole reinforced pairing stays fenced:
   **EXECUTED.** Zero is an absence, not a refutation — the "Moi,
   voler !" precedent proves the exclamatory-infinitive shape is
   grammatical in 1841 French with a personal tonic topic, and
   governed infinitives are frequent in the corpus. The failure is
   local to the reinforced-demonstrative HEAD licensing, bare or
   governed. Per §4 this is a **null**, not a kill.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this null contradict the parent NULL
  (disloc-demonstrative-reinforced)? No — it completes it. The parent
  fenced the bare construction; this fences the governed variant.
  The "pinpoint the fence at the governed-vs-bare line" fork is
  resolved: there is no fence line inside the pairing to pinpoint —
  the whole pairing is fenced at the head.
- Self-check: does this null contradict the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head the construction)? No —
  different head (tonic vs atonic); nothing bare-"ce" surfaced.
- §5.2: no standing red-team verdict touched; no overwrite, no
  escalation required.

## Verdict: NULL (whole pairing fenced per clause 2)

Zero genuine dislocated reinforced-demonstrative + governed
exclamatory infinitive attestations in 27.66M characters of
19th-century French (4/4 candidates classified: 1 finite-clause
subject, 2 fixed-expression "de"-governed embeddings, 1
quotation-introducing head with "pour"-governed past infinitive in
the quotation). Loosening the bar from "bare" to "governed" does not
attest the pairing: the fence is not at the governed-vs-bare line —
the whole reinforced-head + exclamatory-infinitive pairing is
fenced. Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **reinforced-pour-inf-recall** (P3): re-run with the two recall
   gaps closed — admit dash/parenthesis pause marks after the head
   ("celui-là — pour rire !"; P1 currently only [,;:]) and lift the
   180-char window cap on the 73 dropped windows. Bar: ≥1 genuine
   attestation in the widened search re-opens the pairing; confirmed
   zero closes the recall gap and hardens the fence. (Different
   search, not a re-run — targets unsearched windows only.)
2. **gov-excl-inf-register** (P3): corpus-wide census of governed
   exclamatory infinitives ("pour rire !", "à donner lecture !",
   "de croire !") with ANY topic in the same 27.66M-char corpus.
   Bar: if the construction is unattested corpus-wide, the zero here
   is register-level (the construction itself is absent from 1841
   French print, so head-licensing is moot); if it attests with other
   topics, the demonstrative-head gap is specific and the fence
   stands. (Discriminating frames; distinguishes two explanations of
   this null.)
3. **reinforced-pour-inf-drama** (P3): run this battery's governed
   search in the drama corpus (the in-flight sibling
   `disloc-demonstrative-drama`'s register — the natural habitat of
   exclamatory infinitives) with the reinforced-head inventory. Bar:
   ≥1 genuine "celui-là, pour rire !" attestation in drama re-opens
   the pairing at register level; confirmed zero fences it across
   both registers. (Coordinates with, does not duplicate, the
   in-flight drama battery: governed construction, reinforced
   inventory, new corpus.)

## Bookkeeping

- Census script:
  code/crowd17/next-token/reinforced_pour_inf_diagnostic_census.py
  (re-runnable; same corpus + DEM_REINF inventory as
  disloc_demonstrative_reinforced_census.py; outputs
  reinforced-pour-inf-diagnostic_census.json with per-file sizes, hit
  counts, and all 4 candidate windows).
- Report: code/crowd17/report_inbox/battery-reinforced-pour-inf-diagnostic.md
  (this file).
- battery-queue.json: `reinforced-pour-inf-diagnostic` queued ->
  verdict/null via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on
  completion. No stale lock for this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus files or the census script; no invented data.
