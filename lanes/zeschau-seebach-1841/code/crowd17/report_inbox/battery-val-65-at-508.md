# Battery verdict: val-65-at-508

- Target: `val-65-at-508` (battery-queue.json, priority 3, status queued)
- Claim: "Name 65's value at the @508 locus ('le [62]ne qui vient [65]')."
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`). `canonical.py` never used. All counts re-derived in-work. @-offsets are 0-based pair indices.
- Parent: `regne-trone-tiebreak` (NULL, 2026-10-09) follow-up #1 — "a landed 65 value creates the selectional pressure this battery lacks: a temporal noun favors 'règne', a concrete/institutional noun re-opens 'trône'."

## Bar (verbatim, pre-registered BEFORE testing)

"Name 65 iff the value parses at @508 with zero new assumptions; the named value decides the règne/trône frame."

Restated as numbered clauses (fixed before the stream work):

- **C1:** A value for 65 is NAMED iff it parses at the @508 locus (0-based @507–512 = `77 62 94 64 98 65`, "le [62]ne qui vient [65]") with zero new assumptions — standing values only.
- **C2:** The named value decides the règne/trône frame (temporal → règne lean; concrete/institutional → trône re-opened).

Listed adverse: "selectional pressure is directional: temporal noun favors règne, concrete/institutional noun re-opens trône."

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/val-65-at-508.lock` on start; deleted on completion (see Bookkeeping).
2. Re-derived the repaired stream in-session: 1,847 pairs / 96 types, asserts held. `canonical.py` never touched. R5005, sealed gate instances, red-team adjudication queue untouched.
3. Byte-confirmed the locus (0-based, row a3_00): @505=21, @506=67, @507=77, @508=62, @509=94, @510=64, @511=98, @512=65, @513=88, @514=56, @515=87. Registry: 65=["noun","cls"], 88=["gov","cls"].
4. Adopted (not re-litigated) standing results: 65 noun-class (R20-047 GRANT); 98='vient' LEAD; 94='ne' STRONG LEAD (R17-001); 64='qui' granted; 77='le' provisional; 62='il' KILLED at kill grade (R19-106, R20-125); 65 singular (battery promote 2026-10-09, pending ratification).
5. Adopted (not re-litigated) the load-bearing fences at this exact window: `vient-65-complement` NULL (98-65 fenced as complement-class residual) and `temp-65-loc-census` NULL (temporal/locative/adverbial reading of 65 fenced TERMINALLY at @512).

## Window-level evidence

The @508 locus, byte-exact: `77(le,prov) 62 94(ne,STRONG LEAD) 64(qui) 98(vient,LEAD) 65(noun-cls)`. 65 sits at @512 as the direct right neighbor of "vient".

### C1: value-naming attempt — exhaustive arm sweep

**Arm 1 — bare-noun complement of "venir": DEAD (valency fact).** "Venir" licenses no direct noun object in any period of French. Every noun value parses identically (ungrammatically). Adopted from `vient-65-complement` ("Bare-NP complement: ungrammatical. 'Venir' licenses no direct noun object").

**Arm 2 — inverted subject ("vient [65-subject]"): DEAD.** 64='qui' is already the subject of "vient" (granted tier); additionally 65 is bare and French inversion requires a determiner ("vient le ministre", never "*vient ministre"). Adopted from `vient-65-complement`.

**Arm 3 — temporal/locative/adverbial reading: FENCED TERMINALLY.** `temp-65-loc-census` C2: "no future 65-value naming re-opens a temporal/locative reading at @512 (any noun value still faces causes 2–3)" — bare temporal/locative noun after "venir" is unlicensed (temporal complements need determiners or are adverbs; locatives need prepositions), 0/2,636 `vient+X` corpus instances take a bare temporal/locative noun, and `98 65` is a hapax (1/1,847). Adverb-65 ("demain"-type) is dead independently: 65 is noun-class (R20-047).

**Arm 4 — purpose ("vient pour [65]"): ABSENT.** No "pour" between 98 and 65.

**Arm 5 — elided preposition ("vient d'[65]", "vient à [65]"): UNGRANTED.** No stream evidence for an elision rule.

**Arm 6 — appositive/nominative ("le [62]ne qui vient, [65]"): SPECULATIVE + NON-SELECTIVE.** Needs a clause boundary (new assumption, fails the bar's zero-new-assumptions clause); even granted, no value is selectable — any noun parses identically in the appositive slot (val-03-value-census precedent: parsing ≠ naming). Naming "temps" or "peuple" here would be arbitrary.

**Arm 7 — 65 as subject of the following governor ("…qui vient. [65] [88-gov]…"): UNTESTED, new assumption.** Needs a clause boundary; 88's governor selectional frame is value-open. Not battery-decidable under this bar; proposed as follow-up.

**Result:** no value for 65 parses at @508 with zero new assumptions. C1 FAILS. C2 is moot — there is no named value to decide the règne/trône frame.

### Adverse answered

"Selectional pressure is directional: temporal noun favors règne, concrete/institutional noun re-opens trône." The temporal arm — the premise the directionality needs — is **terminally fenced at this locus** (`temp-65-loc-census` C2, quoted above). The directionality cannot fire at @508: a temporal 65 cannot parse here at all, and the concrete/institutional arm (Arms 1–2) parses no better. The adverse is answered, not ignored: 65's value at @508 decides nothing about the règne/trône frame, in either direction.

## Per-clause pass/fail

- **C1 (name the value with zero new assumptions): FAIL.** Arms 1–5 dead/fenced/absent/ungranted on standing values; Arms 6–7 need new assumptions and select no value.
- **C2 (named value decides the frame): MOOT.** No value named.

## Verdict: NULL

65's value cannot be named at the @508 locus with zero new assumptions. The @512 contact remains a complement-class residual: the strain belongs to 65's distribution (and the @512–517 open-value cluster), not to 62 — consistent with `vient-65-complement` ("the strain at @511 localizes to the open-value complements (65/88/56/87/77/80), not to 98") and with the parent `regne-trone-tiebreak` NULL (the keyhole this battery was asked to test does not open).

## Scope

- Names nothing; fences nothing new — the terminal fences on Arms 1–5 are adopted, not re-litigated.
- Untouched: the standing battery-grade @508 "trône" locus promote (about 62's value, not 65's — per §5 it is not downgraded here); `regne-trone-tiebreak` NULL; `temp-65-loc-census` terminal fence; 65's noun-class (R20-047 GRANT); 65's singular (pending ratification); 98='vient' LEAD; §7 (no split declared).
- Not pre-empted: `subj-65-512-inversion` (queued, P4 — structural adjudication of "vient [65] [88]"), `val-65-value-census` (queued, P4 — global uniform-value census), `redteam-508-reread` (queued, P2 — red-team adjudication of the @508 promote vs règne evidence), `trone-vient-register` (queued, P3). This battery tests lexeme-naming only.
- Canonical-stream caveat stands (row a3_00's upstream offset unvalidated).

## Follow-ups proposed (all verified ABSENT from queue, for supervisor queuing)

1. `gov-88-513-subject` (P4) — the one untested structural arm at @512: test whether @513=88's governor class can take @512=65 as its subject across a clause boundary ("…qui vient. [65] [88-governor]…"). Bar: name 65's value iff 88's selectional frame selects exactly one lexeme at battery grade with stated values; else fence the rightward arm. Resolves the residual rightward rather than leftward.
2. `val-65-512-boundary` (P4) — test the appositive/vocative arm (Arm 6): "le [62]ne qui vient, [65]". Bar: name a value iff the appositive parse selects exactly one lexeme with zero new assumptions beyond the boundary; else fence the appositive arm terminally, closing the last speculative parse at @512.

Not duplicated: `val-65-value-census`, `subj-65-512-inversion`, `redteam-508-reread`, `trone-vient-register` already queued.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-65-at-508.md` (this file)
- Queue: `val-65-at-508` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-65-at-508.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock: `locks/val-65-at-508.lock` created on start (2026-10-09T20:23:00Z, no stale lock), deleted on completion (verified gone)
- R5005, sealed gate instances, red-team adjudication queue untouched
