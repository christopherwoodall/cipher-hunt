# Battery verdict: head-77-62-94-noun

## Bar (verbatim, pre-registered)

"name the head with left context @503-506 (39-68-21-67; 67=et/veut positional)"

## Bar restated as numbered clauses

- **C1:** The left context @503–506 parses under standing values with the 67 positional rule applied.
- **C2:** Under the forced syllabic-94 reading, the head of "77-62-94" is NAMED (a specific French word, forced by bytes — not merely compatible).

## Method

Read BATTERY-PROTOCOL.md first. Lock created on start (`locks/head-77-62-94-noun.lock`), deleted on completion. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py`. `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched. Offset convention: 0-based (matches the brief's "@503-506 (39-68-21-67)").

## Window re-derivation (0-based, row a3_00)

| @ | group |
|---|-------|
| 503 | 39 |
| 504 | 68 |
| 505 | 21 |
| 506 | 67 |
| 507 | 77 |
| 508 | 62 |
| 509 | 94 |
| 510 | 64 |
| 511 | 98 |
| 512 | 65 |

Brief's "@503-506 (39-68-21-67)" byte-confirmed. "77-62-94" is the unique stream-wide occurrence (only "77-62" bigram in the full 1,847-pair stream).

## C1: left-context parse — PASS

Standing values applied:
- 39: open (39='à' NOT granted — battery-de-83-sweep).
- 68: open.
- 21: noun-class (registry `21 -> ["noun","cls"]`).
- 67: positional rule (67="veut" iff follower infinitive-shaped). Follower is 77="le" (provisional) — a determiner, not infinitive-shaped. Therefore **67="et"**.
- 77: "le" (provisional).
- 64: "qui" (promoted).
- 98: finite verb (battery-promoted "vient"-type).
- 65: noun-class.

Parse: "[39] [68] [21-noun] et le [62]ne qui [98] [65-noun]…" = "[39] [68] [noun] and the [62]ne which [verb]s [noun]…". The "77-62-94" slot is a masculine NP ("le" + head) coordinated via "et" with the [21]-noun, and headed-relative "qui [98]" follows. Grammatical under standing values.

## C2: name the head — FAIL (epistemic, not kill-grade)

Under the forced syllabic-94 reading, "77-62-94" = "le [62]ne": 77="le" (determiner), 62 = nominal stem (the syntactic head), 94="ne" (STRONG LEAD, R17-001) as word-final syllable. The head must be a French masculine noun ending "-ne".

Candidate masculine "-ne" nouns in 1841 French: **règne**, **trône**, **domaine**, **moine**, **cône**, **patrimoine**…

None is forced by bytes:

1. **62's value is open.** battery-sel-62-48-94 (KILL) demonstrated no uniform 62 value covers 62-48 / 62-94 / 62-06 simultaneously. 62='il' is kill-grade dead (class-62-fullcensus); 62='on' unconditioned is killed (collision-62-84); the conditioned-62 question at this very window (@508) is red-team territory (redteam-62-conditioned, queued). Naming "règne" (62="règ"), "trône" (62="trô"), or "domaine" (62="domai") would each assume a 62 value no battery has demonstrated.
2. **The left context does not discriminate.** 39 and 68 are open; 21 is noun-class with open value — the "[21] et le [62]ne" coordination gives no semantic-field constraint.
3. **The right context ("qui [98] [65]") does not discriminate.** "le règne qui vient", "le trône qui vient", "le domaine qui vient" are all grammatical.
4. **The syllabic-94 premise itself is unestablished.** battery-ne-94-non12-prefamily fenced @508 as the *sole* non-12 pre-94 'ne'-final candidate — a hypothesis, not a finding. The bar's "forced" reading is conditional, and the condition is not met at battery grade.

Per protocol §4 and the stem-03-value precedent: a battery promote needs the value FORCED, not merely compatible. "règne" is compatible (and "qui vient" even favors it stylistically), but compatibility is not forcing.

Not kill-grade: no window forces the syllabic reading false; the structural analysis (62 = nominal head, "-ne"-final masculine noun) stands as the locus parse.

## Adverses

None listed.

## Standing-state check

No contradiction or downgrade: 94='ne' STRONG LEAD untouched; 77="le" provisional untouched; 67 positional rule applied, not modified; sel-62-48-94 KILL respected (no uniform 62 value named); ne-94-non12-prefamily's fence respected (not re-litigated); §7 intact — no polyvalence declared.

## Verdict: NULL

The head's syntactic slot is identified (62, masculine nominal stem, "-ne"-final under the conditional syllabic-94 reading), but no lexical value is forced. The "77-62-94" word cannot be named at battery grade.

## Follow-ups proposed (for supervisor queuing)

1. `val-62-ne-noun` (P3) — discriminate "règne" / "trône" / "domaine" for 62 via the 62-06 windows ("règnent"/"trônent" parseable; *"domaient" kills "domaine") and the six 62-48 windows; then re-test the @508 head.
2. `head-62-94-21coord` (P3) — name 21's value; the "[21] et le [62]ne" coordination may select the semantic field once 21 resolves.
3. `syll-94-508-verify` (P2) — independently establish (or kill) the syllabic-94 reading at @508; the forced premise is currently hypothetical.

## Bookkeeping

`battery-queue.json`: `head-77-62-94-noun` → status `verdict`, result `null`, date 2026-10-09 (temp-file + rename, pre-write assert confirmed queued/verdictless, JSON re-validated post-write). Lock created on start and deleted on completion. `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched.
