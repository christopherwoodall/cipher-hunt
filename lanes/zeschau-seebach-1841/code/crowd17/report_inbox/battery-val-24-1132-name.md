# Battery verdict: val-24-1132-name

- Target: `val-24-1132-name` (battery-queue.json, priority 3, status queued)
- Claim: "name 24's value at @1132 with battery-grade evidence; its promote fires this target's C1."
- Evidence (pre-registered): "@1132=24 carries only R17-009 finite/modal class (follower 77!=85, so not 'en'; {faire, laisser} value route dead globally); naming the value is the stated C1 gate."

## Bar (verbatim, pre-registered BEFORE testing)

"name 24's value at @1132 with battery-grade evidence."

Numbered clauses:
- C1: Name one French verb value for 24 at @1132 (0-based pair index) with battery-grade evidence (positive frame forcing the lexeme, rival values eliminated at the locus or by standing kills).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. Rendered all 52 windows of 24 (n(24)=52) with standing values. Tested candidate values against the @1132 frame and the global frame inventory.

## Findings

**Locus @1132 (byte-exact):** `43 00 86 52 37 86 [24] 77 86 20 62 98 00 98 78`
= "[43-N] pour [86-INF] [52] [37] [86-INF] [24] le(77,prov) [86-INF] [20] [62] vient pour vient ver"

The tight frame is **"[24] le [86-INF]"** — a finite verb directly followed by "le" + infinitive. Under R17-009 (24 = finite verb, modal-shaped, GRANT PROMOTE class-level), this admits the modal/volition/cognition class: "veut/sait/peut/doit le faire".

**Candidate elimination:**

1. **"dire" KILLED at @1132.** "dit le faire" is ungrammatical — "dire" takes "que"-clauses or prepositional infinitives, never "le + INF". (This kills the "dit ce que/qui" global candidacy at this locus.)

2. **"faire"/"laisser" DEAD globally** — adopted from the target's pre-registered evidence (standing kills), not re-litigated.

3. **"pouvoir"/"doit" killed IF 24 is uniform.** The "[24] cela" frames (@73 "[14] [24] ce la pour", @162 "ne [24] ce la [24]", @829 "[01] [24] ce la le [69-N]") — "87=ce" + "11=la" compose as "cela" (that). "peut cela" and modal "doit cela" are ungrammatical ("pouvoir"/"devoir" take infinitives, not "cela" as direct object). This is conditional on uniformity, which is not established (24's class is under red-team mutual-kill: `battery-24-en-verb-conflict`, 2026-10-09, NULL/escalate).

4. **"savoir" vs "vouloir" — NO DISCRIMINATOR at battery grade.** Both parse @1132 perfectly ("sait le faire" / "veut le faire"). Both parse the "[24] cela" frames ("sait cela" / "veut cela"). Both parse "on [24]", "ne [24]", and the "[24] [85]" modal+infinitive frames. The wider context ("[37] [86-INF]" before, "[20]" after) contains only class-open cells (37 predicative frame value-open, 20 class-open) and provides no selectional leg. Subject animacy does not discriminate (both require sentient subjects).

**Global frame inventory (for the record):** "24 87" ('ce') x10, "24 85" x5, "24 82" ('m') x4, "24 30" ('pas') x3, "24 89" (noun) x3, "on 24" x4, "ne 24" x2, "que 24" x3. The "ce"-frames ("ce la"/"ce qui"/"ce que") are the most idiomatic for "savoir" ("sait ce que" highly idiomatic) but do not reach kill grade against "vouloir".

## Verdict: NULL

C1 FAILS: no single value is forced at @1132. The locus admits at least two values ("sait", "veut") with zero battery-grade discriminator between them. This is substantive inconclusiveness, not a data gap — the frame is fully rendered and the candidate set is exhausted.

**Scope:** locus-level only. Untouched: R17-009 (24 = finite verb, modal-shaped, class-level GRANT), the 24-en-verb-conflict red-team escalation, 24's global value (still open), §7 (no polyvalence declared or needed). No standing/red-team verdict contradicted or downgraded. Canonical-stream caveat stands (row a6_08/a6_09 boundary).

## Follow-ups proposed (§4, all verified ABSENT from battery-queue.json)

1. `sait-veut-24-discriminator` (P3) — find a battery-grade discriminator between "sait" and "veut" for 24 across all 52 windows. Most promising: indirect-interrogative frames ("savoir" licenses "si"/"comment"/"où" + clause; "vouloir" licenses "que" + subjunctive). Name the value or fence as value-split.
2. `val-37-1130-frame` (P4) — name 37's class/value at @1130; the pre-verbal "[37] [86-INF]" frame at @1130–1131 constrains 24's subject and may selectionally discriminate "savoir" vs "vouloir".
3. `dir-24-cela-uniform` (P4) — test whether the "[24] cela" x3 frames (@73/@162/@829) force 24's uniformity; if "cela" kills "peut"/"doit" at battery grade independent of uniformity, the global candidate set narrows to "sait"/"veut".

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-24-1132-name.md` (this file).
- Queue: `val-24-1132-name` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-24-1132-name.tmp` + atomic rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-24-1132-name.lock`: created on start (2026-10-09T19:42:47Z, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
