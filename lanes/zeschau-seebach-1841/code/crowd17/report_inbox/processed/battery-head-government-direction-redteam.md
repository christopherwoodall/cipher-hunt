# RED-TEAM INPUT — direction-of-government package (gather-only)

- Target id: `head-government-direction-redteam`
- Date: 2026-10-09
- Worker: battery worker (subagent 73964b3d-6488-4435-9f05-2badb23af1b9)
- Verdict: **NULL** (gather-only by design — no adjudication, no battery-level decision)
- Origin: follow-up #3 of the NULL `reinforced-head-topology-drama` (2026-10-09, P2, red-team input, gather-only).
- Corpus basis: 14-play drama corpus in `code/side-period/corpus`, 2,939,372 chars.
  Re-runnable script: `code/crowd17/next-token/reinforced_head_topology_drama.py`
  (reproduces the 41 windows with 500-char context). The 1,847-pair repaired parse
  was not used (corpus census per target charter). `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked with
-l� or -ci (celui-l�, ceux-l�, celle-l�, celles-l�, celui-ci, ceux-ci, celle-ci,
celles-ci). "Dem-comma window" = a reinforced head followed by `[,;:]`.
"Governed infinitive" = an infinitive governed by a preposition (pour / � / de);
bare modal-complement infinitives ("il faut partir") are NOT counted as governed.
"Direction of government" = which participant governs the infinitive and which is
governed by it: in "head governs infinitive" the head is the subject/controller
of the infinitive; in "head is the infinitive's object" the infinitive governs
the (resumed) head.

## Bar (verbatim, pre-registered)

"evidence package for red-team adjudication; gather-only, no battery decision"

Numbered clauses (restated before testing, not modified after):

1. C1 (package): deliver the direction-of-government finding (heads are the
   infinitive's object, never its governor) as ruling-ready red-team input for
   the reinforced-head family.
2. C2 (no adjudication): no red-team verdict proposed, confirmed, or
   overturned; no battery-level decision declared.

## Method

1. Read BATTERY-PROTOCOL.md. Created
   `locks/head-government-direction-redteam.lock` on start; no lock, stale or
   fresh, existed for this id.
2. Read in full: `battery-reinforced-head-topology-drama.md` (the originating
   NULL, 41/41 windows mapped into 9 resolution classes), the REPORT.md fold
   entries F266–F269 and the §6 rephrase item, and the sibling red-team input
   `battery-redteam-tonic-fence-input.md` for package format. All window
   counts below are taken verbatim from the originating report; no window was
   re-classified by this worker.
3. Extracted the direction-of-government ratios and the wording conflict that
   makes them red-team material.

## Findings — the package

### (a) The direction-of-government finding

From the originating battery's full-resolution map of all 41 dem-comma windows
(#0–#40, file + char-offset evidence in the parent report):

- **0/41**: a reinforced head governing ANY infinitive as its subject/controller.
  In every window containing an infinitive, the head is the infinitive's
  OBJECT (via clitic resumption), never its governor.
- **1/41 strict**: a reinforced head as the resumed object of a
  preposition-governed infinitive in complement position — #38
  "ceux-l�, je ne suis pas libre de les accueillir" (verre-d-eau @36952,
  de-governed infinitive under "libre", head resumed by "les"; the parent's
  classified near-miss).
- **3/41 loose**: a reinforced head as the (resumed) object of an infinitive
  in a complement clause — #24 "celui-l�, il faut le sauver" (tour-de-nesle
  @20203, bare infinitive under modal "faut", head resumed by "le"), #35
  "ceux-l�, et, s'il fallait les perdre ou les voir compromis... j'aimerais
  mieux mourir !" (bertrand-et-raton @110103, bare infinitives under
  "fallait", head resumed by "les"), #38 (above).
- **22/41**: resumption-dominant resolutions (classes A 13 copular/cleft
  "c'est"-identifications + B 6 clitic resum
...[truncated 4703 chars]