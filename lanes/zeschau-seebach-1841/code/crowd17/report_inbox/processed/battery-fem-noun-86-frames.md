# Battery verdict: fem-noun-86-frames — PROMOTE

Date: 2026-10-09. Worker: 9a62323f-29c4-4abc-9a0e-75de545feb6d.

## Bar (verbatim from battery-queue.json)

"promote iff >=2 frames parse with a feminine noun value at @671; else fence @671 as a fenced residual with stated cause"

### Numbered clauses (operative, pre-registered)

1. **C1 (promote):** >=2 frames parse with a feminine noun value at @671.
2. **C2 (fence):** else fence @671 as a fenced residual with stated cause.

Listed adverses: none.

## Method

Read `BATTERY-PROTOCOL.md` first; created `locks/fem-noun-86-frames.lock` on
start (deleted on completion). Re-derived the repaired 1,847-pair / 96-type
stream in-session from `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt` parsed per `code/side-keyhunt/repair_parse.py`
(asserts held: 1,847 pairs, 96 types); `canonical.py` never touched; R5005,
sealed gates, red-team adjudication queue untouched.

**Numbering convention:** @-offsets in this report follow the parent 86
batteries' convention — @671 is the 0-based index of the 86 itself
(1-based @672). Byte-verified: idx0 671 = `86` on row a5_00; left neighbor
idx0 670 = `11` (1-based @671), right neighbor idx0 672 = `24`
(1-based @673). Full row a5_00 (1-based @669–@694):
`20 67 11 86 24 80 03 64 37 77 45 23 09 07 00 92 64 29 40 65 94 29 60 03 39 74`.

## Window-level evidence

- **Lone feminine anchor confirmed byte-exact:** exactly 3 determiner-left
  86 windows stream-wide — idx 175 (`87 86`, "ce"), idx 671 (`11 86`,
  "la"), idx 1345 (`47 86`, "ce"). `11 86` occurs exactly once stream-wide.
  11=la is pencil ground truth → any noun value at idx 671 is forced
  feminine. This agrees with battery-noun-86-dlife's KILL evidence, which is
  adopted as premise, not re-litigated.

## Frame tests (all under standing values)

- **F1 — determiner-left "la [86]" (NP-internal licensing): PASS,
  unconditional.** 11=la (pencil GT) immediately left of 86; feminine
  determinative agreement forces feminine noun class. The word-internal
  (syllabic) rival at this window is kill-grade dead per the D-life
  batteries; no other class survives the determiner slot.
- **F2 — subject of finite verb "[86] [24-V]" (clause-external licensing):
  PASS, conditional on battery-promoted 24-verb-class.** With 24 finite/modal
  (battery-promoted class, pending red-team ratification), `67 11 86 24`
  parses as "et(67 positional; follower 11 not infinitive-shaped) la [86-N]
  [24-V]" — a clean S-V clause, "la [N] [V]". The 86 occupies a subject
  slot, an independent licensing relation from F1's determinative
  agreement (cf. prof-88's frame-leg convention: distinct constructions
  count as distinct legs).
- **F3 — predicative/A1 frame:** FAIL. 37 (A1 predicative) sits at idx0 676
  behind granted 64='qui' (idx0 675); no predicative marker governs 86.
- **F4 — feminine agreement (adjective/participle):** FAIL. No feminine
  agreeing adjective or participle adjacent to the window.
- **F5 — appositive/coordinated NP:** FAIL. "et" (67) precedes "la"; no
  antecedent NP exists to coordinate with.
- **F6 — word-internal/syllabic 86:** FAIL — kill-grade dead at this window
  (adopted).
- **F7 — nominalized infinitive:** FAIL — would be masculine ("le"), not
  feminine.
- **F8 — second determiner contact:** FAIL — "11 86" is the lone
  stream-wide instance; no second feminine contact exists.

## Verdict: PROMOTE

C1 passes: two distinct frames (F1 determinative licensing, F2 subject
licensing) parse with 86 as a feminine noun at @671. C2 does not fire.

**Scope and caveats (explicit):**
- Class-level only: no feminine noun *value* is named ("voix"-family was
  0/26 at voi-86-dwindow-composition; naming would be invention).
- F2 is conditional: if the red team rules 24='en' on the 24 docket, the
  subject-verb frame re-opens and only F1 stands.
- This does NOT contradict battery-noun-86-dlife's KILL: that kill targeted
  the *uniform* noun value across the determiner-left subset (gender split
  @175/@1345 masculine vs @671 feminine). A window-local feminine noun
  class at @671 is consistent with the kill's own evidence.
- Canonicality caveat: row a5_00 is one of the 68 unvalidated upstream
  offsets; this is a canonical-stream verdict per protocol.
- No §7 issue: no polyvalence declared.

## Follow-ups

Promote, not null — no follow-ups mandated.
