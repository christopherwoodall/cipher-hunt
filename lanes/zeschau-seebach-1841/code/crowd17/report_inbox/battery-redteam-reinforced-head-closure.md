# Battery report: redteam-reinforced-head-closure

- Target id: `redteam-reinforced-head-closure`
- Claim: "Package grandparent (reinforced-pour-inf-drama) + parent (reinforced-head-topology-drama) + this battery as the closure input for the reinforced-head venue."
- Date: 2026-10-09
- Worker: battery worker (subagent f80e83c0-5c15-4841-8f30-196dd730a784)
- Stream: not applicable — this is a gather-only consolidation of three corpus batteries. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched. `canonical.py` never used.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, ceux-là, celle-là, celles-là, celui-ci, ceux-ci, celle-ci, celles-ci), as opposed to bare tonic heads (cela, ceci, ça). "Exclamatory infinitive" = an infinitive used as an exclamation ("Moi, me taire !" = "me, to shut up!"). "Governed" = the infinitive is governed by a preposition (pour / à / de), as in "celui-là, pour rire !". "Genuine attestation" = the reinforced head actually governs/heads an exclamatory infinitive: the infinitive is the exclaimed phrase, not embedded in a downstream finite clause.

## Bar (verbatim, pre-registered before testing)

"Package delivered; no battery decision requested"

Numbered clauses:

1. C1 — the closure package is delivered (grandparent + parent + this battery consolidated for the reinforced-head venue). PASS.
2. C2 — no battery-level adjudication is made. PASS.

## Package contents

### 1. Grandparent: `reinforced-pour-inf-drama` — NULL

- Claim: run the governed-infinitive search in the drama corpus (the theorised natural habitat of exclamatory infinitives).
- Corpus: 14 files, 2,939,372 chars of 19th-century French drama.
- Finding: **zero genuine dislocated reinforced-demonstrative + governed exclamatory infinitive attestations** (1/1 candidate classified: dislocated topic resumed by clitic inside a finite clause — not an infinitive exclamation).
- Its parent (`reinforced-pour-inf-diagnostic`) found 0 genuine in 27.66M chars of 19th-c prose (4 candidates, all classified).
- Report: `code/crowd17/report_inbox/processed/battery-reinforced-pour-inf-drama.md`

### 2. Parent: `reinforced-head-topology-drama` — NULL (map complete; sharpening not earned)

- Claim: full-resolution map of all 41 dem-comma windows in the drama corpus.
- Method: re-ran the DEM_REINF pattern verbatim over the same 14 drama files; reproduced exactly 41 dem-comma hits; every window hand-classified with ±500-char context; governed-infinitive regex sweep over all 41 windows, every hit hand-audited.
- The 41 windows, classified:
  - A. Copular/cleft "c'est" identification — 13
  - B. Clitic resumption in a finite clause — 6
  - C. Clitic resumption + governed/bare infinitive complement, head = the infinitive's object — 3 (incl. #38 "ceux-là, je ne suis pas libre de les accueillir" — de-governed infinitive under "libre", head resumed by "les")
  - D. Finite clause, anaphoric, no clitic resumption — 8
  - E. Verbless appositive / NP enumeration — 4
  - F. Colon-introduced direct speech / vocative — 2
  - G. Relative-clause continuation — 2
  - H. Adjectival apposition + exclamation — 1 (#4 "celle-ci, pleine de jeunes gens, de valets !" — the corpus's closest approach to an exclamatory shape with a reinforced head, but the exclaimed phrase is an adjectival apposition, NOT an infinitive)
- "Head + exclamatory infinitive" shape: **0/41**.
- Positive boundary the map supports: reinforced heads in topic position resolve by resumption (22/41: c'est-identification, clitic, or possessive); they co-occur with governed infinitives only as the infinitive's (resumed) object inside finite complement clauses.
- Report: `code/crowd17/report_inbox/processed/battery-reinforced-head-topology-drama.md`

### 3. This battery (closure)

The closure statement for the red-team venue:

- The reinforced-head + exclamatory-infinitive pairing is now at **confirmed zero in both registers**: 0 genuine in 27.66M chars of 19th-c prose (4/4 candidates classified) and 0 genuine in 2.94M chars of 19th-c drama (1/1 candidate classified) — and drama was the theorised natural habitat.
- The 41-window topology map exhausts the drama evidence: every dislocated reinforced head has a stated resolution; the only exclamatory-shaped window (#4) exclaims an adjectival apposition, not an infinitive.
- Government runs the wrong way for any future "head governs infinitive" claim: the 3 infinitive-complement windows all have the head as the infinitive's resumed OBJECT inside finite clauses.
- Register positive control (from the drama-ingest battery): drama DOES use bare exclamatory infinitives — Hernani "Gouverner tout cela !" — but with the demonstrative as OBJECT after the infinitive, not as a reinforced head before it.
- The blocker's standing: the pairing is unattested in both registers at the lane's corpus-grammaticality standard. No battery-level adjudication is made here; the closure input is delivered for the red-team venue.

## Verdict: NULL (gather-only package delivered)

C1 PASS / C2 PASS. No adjudication, no §7 declaration, no registry change. Per the gather-only precedent (R19-182; battery-redteam-tonic-fence-input), no follow-up targets are proposed by this worker — the corpus batteries' own follow-ups (modal/perception-governed, causative, exclamatory-non-infinitive censuses) remain queued.

## Scope

Gather-only consolidation. Untouched: the two source verdicts (both NULL), all §7 questions, all standing/red-team verdicts. No standing/red-team verdict contradicted or downgraded. Canonical-stream caveat stands.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-redteam-reinforced-head-closure.md` (this file)
- Queue: `redteam-reinforced-head-closure` queued -> verdict/null, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.redteam-reinforced-head-closure.tmp` + atomic rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/redteam-reinforced-head-closure.lock`: created on start (2026-10-09T20:01:00Z, no stale lock), deleted on completion (verified gone)
- R5005, sealed gates, red-team adjudication queue untouched
