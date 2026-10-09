# battery-personal-tonic-governed-excl-recall — report

## Target
`personal-tonic-governed-excl-recall` (P3)

## Claim
400-char windows + '?'-termination recall-gap closure for tonic-pronoun +
governed exclamatory infinitives in drama.

## Bar (verbatim, pre-registered)
"0 genuine confirms the zero is not a window/termination artifact; any
genuine re-opens"

## Numbered clauses
1. **C1 (zero arm):** 0 genuine hand-classified candidates under the widened
   net (400-char windows, '!' or '?' termination) confirms the parent zero was
   not a window/termination artifact.
2. **C2 (re-open arm):** any genuine tonic-topic + governed exclamatory
   infinitive re-opens the licensor class.

## Method
- Parent: `battery-personal-tonic-governed-excl-drama` (null, 2026-10-09):
  29 candidates (15 strict, 14 loose-only), 0 genuine, 180-char windows,
  '!' locality only.
- Re-runnable script: `code/crowd17/next-token/personal_tonic_governed_excl_recall_census.py`,
  output `personal-tonic-governed-excl-recall_census.json`.
- Identical P1 (dislocation): `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]`
  (case-insensitive). Identical P3 (governed infinitive, strict and loose
  clitic-tolerant regexes). Differences from parent ONLY:
  window = text from the pronoun through the next `[!?]` (inclusive), capped
  at 400 chars (parent: 180 chars, `[!?.]`); exclamatory filter = window must
  contain `!` or `?` (parent: `!` only).
- Corpus gate verified on disk: identical 14-play drama set, 2,969,582 chars,
  `hugo-hernani.txt` present-but-excluded (duplicate Hernani edition).
- Yield: **356 recall candidates** (211 strict, 145 loose-only; 158 '?'-terminated,
  198 '!'-terminated). All 29 parent candidates re-appear in the net (offset-set
  overlap verified = 29/29); **327 are new** and were hand-classified in full
  window context (two near-misses re-checked against 700 chars of wider context
  on disk). No numbers invented: every count traces to the census script output.

## Classification (327 new candidates)

**0 genuine.** Confound classes:
- **Finite-matrix-governed infinitive (dominant, ~300):** the governor
  infinitive is the complement/adjunct of a finite verb inside the widened
  window, e.g. [02] "Quel moment prenez-vous ... Pour faire, vous, barons,
  ce métier de bandits ?" (purpose adjunct of "prenez"), [63]
  "peut-être elle me permettra de rester près d'elle", [75] "ils s'engagent
  à s'aider mutuellement à monter", [234] "c'est pour lui donner une année
  de richesse ... que j'ai tout dissipé". Same dominant confound as the parent
  battery (15/29 there); the 400-char window only catches MORE finite verbs.
- **Non-topic pronoun matches (~20):** "devant moi ," ([261], re-checked:
  object of "devant"; infinitive "pour savoir" governed by "Attendez-vous"),
  "dites-moi ," ([326], re-checked: imperative clitic), "moi , je" subject
  hits, "nous , Henri de Valois" royal plural, inverted "prenez-vous" tails
  ([13]).
- **Ellipsis-interrupted, force not on infinitive (2 near-misses):** [110]
  kean @105373 "elle, pour te disculper…" and [159] bertrand-et-raton @77029
  "moi, Raton de Burkenstaff… et pour escorter mademoiselle…" — both are
  interrupted governed-infinitive phrases, but the "!" in each window
  terminates a LATER clause ("plus que ma vie !", "À la bonne heure !"), not
  the infinitive phrase. Fail the force-on-the-infinitive gate; proposed as a
  distinct-shape follow-up below.
- **à + noun / non-infinitive (~4):** [144] "moi, à dîner ?" (noun, not INF);
  "à l'ombre" hits where the window's infinitive is elsewhere in the frame.
- **True-shape absent everywhere:** no window in the 327 shows a tonic
  pronoun as the dislocated topic of a self-contained governed exclamatory
  infinitive terminated by '!' or '?' with the illocutionary force falling on
  the infinitive phrase.

## Per-clause pass/fail
1. **C1 (zero arm): PASS.** 0 genuine across all 327 new candidates, on top of
   the parent's 29/29 zero. The parent's zero is confirmed under 400-char
   windows and '?'-termination: it was not a window/termination artifact.
2. **C2 (re-open arm): does not fire** — antecedent false.

## Verdict
**NULL** — confirmed zero at recall depth, not a refutation (§4: zero is an
absence, not a kill). The reinforced-head fence now stands on a 356-candidate
drama base (parent 29 + recall 327), 0 genuine, and the recall gap for
window-size and '?'-termination is closed at drama-register level.

## Follow-ups proposed (nulls regenerate work; both verified ABSENT from queue)
1. **personal-tonic-governed-excl-prose-recall (P3)** — mirror recall-gap
   closure on the 27.66M-char prose corpus (battery-personal-tonic-governed-excl-prose
   null, 2026-10-09): 400-char windows + '?' termination; prose zero closes the
   recall gap across registers, any genuine re-opens register-wide.
2. **gov-excl-inf-ellipsis-shape (P4)** — the two ellipsis near-misses
   (kean @105373, bertrand-et-raton @77029) suggest a distinct interrupted-
   utterance shape: pronoun-topic + governed infinitive cut by "…". Distinct
   detection (ellipsis-terminated governed infinitives after pronoun-comma)
   and a distinct force test: does the ellipsis mark a self-contained
   exclamatory infinitive (a third shape alongside the force-terminated one),
   or is it always a broken-off finite-matrix dependency? 0 genuine keeps it
   a near-miss class; ≥1 genuine names the shape.

## Standing items
- R5005, sealed gates, red-team adjudication queue: untouched.
- Standing §7 values (banked/promoted/kills/splits/holds): untouched, none
  contradicted.
- `canonical.py` never used; repaired 1,847-pair stream not needed here
  (corpus battery, but the stream caveat stands).
- Lock created on start (2026-10-09T14:59:52Z), deleted on completion.
