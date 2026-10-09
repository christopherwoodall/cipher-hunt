# Battery report: on-01-84-distrib-package (gather-only consolidation)

## Bar (verbatim, pre-registered)

"Gather-only: deliver the consolidated package; no adjudication"

Numbered clauses:
- C1: deliver the consolidated package (01 positional distributions + on-01-893-970-corpus result) as input to the already-queued `redteam-01-split-docket`.
- C2: no adjudication — no value named, no class named, no split declared, §7 untouched.

## Method

Gather-only consolidation. Sources: `battery-on-01-vs-84-homophony` (2026-10-09, processed) and `battery-on-01-893-970-corpus` (2026-10-09, inbox). Stream references are 0-based on the repaired 1,847-pair / 96-type parse. `canonical.py` never used. No new stream work; no new corpus work.

## C1 — the consolidated package

### Part A: 01 positional distribution (from on-01-vs-84-homophony)

The four 01='on' legs, byte-exact (±3):

- **@40** (a1_01): `39 64 41 01 24 88 43` — 01 immediately preverbal (follower 24={faire}, R20-016 GRANT LEAD), preceded by 41 (open). Reading: "qui [41] on [24]". Tension: R20-016 also grants 01="en" local LEAD at the 01-24 windows ("en faire" vs "on [24-fin]"); 24's finiteness open.
- **@893** (a5_08): `06 77 76 01 98 82 14` — 01 immediately preverbal (follower 98="vient", LEAD, finite 3sg), preceded by 76 (noun, promoted R19-111). Reading: "[06] le [76-N] on vient" — grammatical, zero new assumptions.
- **@970** (a6_00): `06 77 76 01 98 48 51` — byte-identical left 4-gram "06 77 76 01" to @893; same "on vient" reading, independent window.
- **@984** (a6_01): `47 78 45 01 24 89 48` — **leg dead by red-team grant.** R20-113 (GRANT): "ce(47) [78] ceci(45-01) fait(24)" wins, locus-restricted to @983–986, conditional on the A11 HOLD. 45-01 is one word ("ceci"); 01 is a bound '-ci' syllable — mutually exclusive with standalone 01='on'.

Common positional signature of the surviving legs: 01 is **immediately preverbal** in all three (@40/@893/@970); predecessors are 41 / 76 / 76. 01 never appears in an elision/post-clitic slot.

### Part B: 84='on' positional distribution (A15, unconditioned)

n(84)=25. Elision slot (post-clitic), 9 windows: 77-84 ×7 (@146/@260/@1058/@1447/@1485/@1764/@1803, "l'on" frames, C1), 46-84 ×2 (@310/@473, "qu'on"). Non-elision slots, 16 windows: @154/@167/@276/@391/@412/@788/@857/@1021/@1151/@1189/@1290/@1378/@1418/@1501/@1620/@1665. Per A15-C2 (resolved), 84='on' is **unconditioned** — holds across elision and non-elision slots alike.

### Part C: overlap test (from the homophony battery)

84's distribution (unconditioned, 25 windows incl. 9 post-clitic) vs 01='on' (preverbal-only, 3 surviving legs). The frames do not coincide: 01='on' never occupies 84's elision slot, and 84's grant needs no positional license. This is NOT the homophone shape — it is the **conditioned-split shape**: 01='on' iff immediately preverbal (cf. the 67 precedent, 67="veut" iff follower infinitive-shaped). Declaring it is red-team venue under §7 (second polyvalence); the battery escalated, not declared.

### Part D: the on-01-893-970-corpus result (2026-10-09, verdict NULL)

- Bar: ">=1 genuine frame attestation or fence the shape as stream-coincidence."
- Method: regex `\b(le|la|les|un|une|des|du|au|aux)\s+\w{2,}\s+on\s+\w{2,}` over 97 files / 61,065,841 bytes of 1841 French (widened corpus, prose + drama) → **250 raw hits; every hit's context hand-checked; zero genuine single-clause "le [N] on V".** All 250 are: fronted temporal adverbial + new clause (~40%), fronted locative PP + new clause (~30%), manner/adverbial PP + new clause, gerundive/subordinate clause + new main clause, enumerations, sentence boundaries/headings/stage directions, or OCR garbage.
- **Verdict NULL (fence executed):** the single-clause "le [N] on vient" shape is unattested; the "on" reading of 01 at @893/@970 cannot be licensed by a corpus frame.
- Explicitly out of scope: the "en" readings at the same windows (different shape, untested); @40's "[41] on [24-fin]" shape (different shape, untested); the boundary parse "…le [N] | on vient…" (the corpus-attested shape — proposed as follow-up `boundary-76-01-893`).

### What the corpus result changes for the docket

1. The preverbal-'on' arm at **@893/@970 loses its corpus license**. Part A listed these two as "grammatical, zero new assumptions" — that was grammaticality-only; the corpus fence now says the single-clause shape is unattested in 61M chars. The arm's only live rescue is the boundary parse ("on" opens a new clause after a complete left clause ending at 76).
2. **@40 is untouched** by this fence: its shape ("[41] on [24-fin]", no "le [N]" left of 01) was not the tested shape. `on-01-40-corpus` remains the open leg.
3. **The "en" rival is untouched**: "le [N] en vient" (en as clitic) was not tested. The uniform-'en' kill at @893/@970 (val-01-census, "en vient" ungrammatical with finite 98) still stands — so @893/@970's 01 has neither an "on" corpus leg nor an "en" grammatical leg. The window is a residual pending red-team adjudication of the 01 split.
4. The conditioned-split shape (Part C) is unaffected in structure: it now reads "01='on' iff immediately preverbal, with the @893/@970 instances corpus-unlicensed and the @40 instance corpus-untested."

## C2 — no adjudication

No value named, no class named, no split declared. 01's value stays open. 98='vient' LEAD untouched. §7 intact. No standing/red-team verdict contradicted or re-litigated. Canonical-stream caveat stands (rows a5_08/a6_00/a1_01 offsets unvalidated).

## Verdict: NULL (gather-only package delivered)

C1 PASS (package delivered) / C2 PASS (no adjudication). Per the gather-only precedent, no follow-up targets proposed — the queued `redteam-01-split-docket` is the venue; the corpus battery's own follow-ups (`en-01-893-970-corpus`, `on-01-40-corpus`, `boundary-76-01-893`) stand as its proposed next steps.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-on-01-84-distrib-package.md`
- Queue: `on-01-84-distrib-package` queued → `verdict`/`null` 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.on-01-84-distrib-package.tmp` + atomic rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/on-01-84-distrib-package.lock`: created on start (agent 191c7427-c2d4-4995-992a-dc559b234959, 2026-10-09T19:45:00Z, no stale lock), deleted on completion (verified gone)
- R5005, sealed gates, red-team adjudication queue untouched
