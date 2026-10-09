# Battery `leftedge-1024-43-governor` — verdict: NULL (fence executed)

## Bar (pre-registered)

The queue's `bars` field for this target is empty (recorded verbatim: `null`).
Per protocol §2's bar-pre-registration principle, the numbered clauses below are
derived from the claim BEFORE testing and are not modified after seeing data:

- **C1:** the verbless "ce qui par [43]" left chunk licenses under standing
  values with 43's class named (promote-grade reading stated, zero new
  assumptions).
- **C2:** else the chunk is fenced with stated cause.

Claim (verbatim): 'license or fence the verbless "ce qui par [43]" left chunk
now that the skeleton's left edge is "Ceci" — name 43's class or fence the
fragment.' Adverses: none.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `code/side-keyhunt/repair_parse.py`); asserts held (1,847 pairs,
96 types). `canonical.py` never used. 1841 diplomatic French only.
Standing values adopted: 45='ce' (A11 hold, lead), 64='qui' (granted),
96='par' (granted), 43=["noun","cls"] (R19-045, red-team granted, value open),
87='ce' granted with 87-01='ceci' fused (skeleton premise), 67 sole
polyvalence (§7).

## Findings

**Loci byte-confirmed.** The chunk "45 64 96 43 87 01" occurs exactly **2×**
stream-wide (byte-identical), 0-based @340 and @1024:

- @340 (row a2_05): `…40 03 64 31 14 | 45 64 96 43 87 01 | 06 70 12…`
  i.e. "…[14] | ce qui par [43] ceci | ent|pre|n…" (06 70 12 = "entrepren-" stem).
- @1024 (row a6_02/a6_03): `…91 53 84 92 64 | 45 64 96 43 87 01 | 03 29 80…`
  i.e. "…[92] [qui] | ce qui par [43] ceci | [03]er [80]…" — the @1029
  skeleton window ("Ceci, [03]er! [80]-le, la première fois!").

Both windows share the full "ce qui par [43], ceci" frame; only the ceci
continuation differs ("entrepren-" vs "[03]er"). R19-046 context: the par-43
value hunt is open with {nature, nécessité} as live candidates; {condition,
mesure} killed.

**C1 — candidate readings, all tested under standing values:**

1. **Free relative "ce qui" + "par [43]" adjunct** → requires a finite-verb
   predicate; none arrives in the chunk or its right context (both windows:
   "ceci" + infinitive/verb-stem clause, no finite verb). FAIL.
2. **Interrogative "ce qui"** → barred: "ce" binds "qui" (established kill at
   @148, ce-qui-148-par-rival; same grammar). FAIL.
3. **"par [43]" as sentential adjunct to the right clause** ("par [43], ceci
   [03]er!") → leaves "ce qui" as an unlicensed standalone fragment. FAIL.
4. **Verbless equative/cleft with "ceci"** ("ce qui par [43], ceci") →
   French verbless equatives do not take this shape; "ce qui" specifically
   requires a relative predicate; no copula present. FAIL.
5. **Leftward-antecedent "qui"** (@1023's 64): "…[92] qui, ce qui par [43]…"
   → the relative still needs a predicate; none follows. FAIL.
6. **43 as verb-stem** → contradicts the R19-045 noun-class grant; §7 bars
   polyvalence rescues and protocol §5 bars re-litigating red-team verdicts.
   Not tested further. OUT OF SCOPE.
7. **Frozen "par nature"-shaped adjunct** (43 live candidate "nature") →
   could license "par [43]" alone, but the "ce qui" residue remains
   unlicensed; also 43's value is open, so this arm needs a red-team naming
   first. CONDITIONAL, not licensable today.
8. **Dialogue-ellipsis fragment** → R5005 register is diplomatic prose, not
   dialogue; no evidence; invention. FAIL.

No candidate licenses the chunk with zero new assumptions. **C1 FAIL.**

**C2 FIRES — fence "ce qui par [43]" (both windows) with stated cause:**
under standing values the chunk has no licensed parse — the relative reading
needs a finite predicate and none arrives; the interrogative reading is
barred; no verbless-relative license exists in 1841 French; §7 bars
polyvalence rescues (96='par' fixed, 43 nominal by R19-045 grant). The
two-window recurrence ("ce qui par [43], ceci" ×2) is recorded as a
distributional fact, not a license.

**No standing/red-team verdict contradicted or downgraded** (R19-045,
R19-046, R19-064, A11 hold all adopted as premises). §7 intact.
Canonical-stream caveat stands (rows a2_05/a6_02/a6_03 offsets unvalidated).

## Verdict: NULL (fence)

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `ceci-correlative-corpus` (P3) — corpus test: does "ce qui par [N], ceci"
   / "ce qui …, ceci" occur as a correlative frame in 1841 French prose?
   ≥1 genuine attestation licenses the chunk; a confirmed zero hardens the
   fence.
2. `par43-nature-rerun` (P4) — gated re-test of the "par nature"
   sentential-adjunct arm once the red team names 43's value
   (nature/nécessité live per R19-046).
3. `cequi-45-rerun` (P4) — gated re-test of the chunk's left edge once the
   A11 45='ce' hold is adjudicated by the red team.

## Bookkeeping

- Lock: created on start (2026-10-09T12:39:28Z), deleted on completion.
- Queue: `leftedge-1024-43-governor` → `status: verdict`, `result: null`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; JSON re-validated; own entry only; no downgrade).
- R5005, sealed gate instances, red-team adjudication queue untouched.
