# Battery report: val-23-182-semantic

- Target id: `val-23-182-semantic`
- Claim: name 23's value at @182 (finite verb under 'qui')
- Date: 2026-10-09
- Worker: battery worker (subagent 518fd016-9122-41e2-84f8-def7a93227b3)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "Battery grade" = the evidence standard of this pipeline. "NULL-licensed" = a reading that parses and contradicts nothing but cannot be promoted. "Fence" = the route is closed at battery grade, re-openable on new evidence.

## Bar (verbatim, pre-registered before testing)

"the verb's semantics ('rendre' vs 'sembler' vs 'demeurer') is the only byte-internal discriminator that could select the -ent adjective; else fence the semantic route"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 23's value at @182 is forced at battery grade to exactly one semantic candidate (rendre / sembler / demeurer) — i.e., the verb's semantics discriminates the -ent adjective and thereby names the verb → name the value.
2. **C2 (else arm):** fence the semantic route — 23's semantics cannot discriminate the -ent adjective at battery grade.

Adverses listed: 23~26 split hold (S7); does not touch 06='ent' (R17-007 conditional) or the 23=verb class.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-23-182-semantic.lock` on start (agent id + 2026-10-09T20:44:30Z); no prior/stale lock.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Adopted, never re-litigated: 64="qui" granted; 23=verb class PROMOTE (`battery-23-1697-class`, 2026-10-09 — @182 is its kill-grade "qui [23]" leg forcing a finite verb); 37/32/42 predicative frames (A1); 06='ent' conditional (R17-007, R20-011); `val-37ent-adjective` NULL (the "37 06" -ent-adjective reading is licensed but unnameable; "37 06" is a stream-unique hapax); 23~26 standing split; 00="pour" class-level (A9).
4. 1841 diplomatic French throughout.

## Findings

**Locus byte-confirmed** (0-based, row a1_05):

```
@176=21 @177=69(noun) @178=14 @179=24(verb-cls) @180=87(ce) @181=64(qui) @182=[23] @183=37 @184=06(ent) @185=00(pour) @186=33 @187=16 @188=00 @189=66
```

Frame: "qui [23-fin] [37-pred] [06] pour [33] …" — "qui" forces a finite verb (kill grade, adopted); 37 takes the A1 predicative frame; 06='ent' is word-final so "37 06" reads as one word "[Xent]" under the NULL-licensed adjective reading.

**C1 analysis — no semantic candidate is forced:**

- **The candidate set is not closed.** The bar names rendre/sembler/demeurer as the semantic discriminator, but these are examples from the parent battery, not a closed battery-grade candidate list. Every French finite 3sg verb parses "qui [23] [37]ent pour …" identically at the frame level: dit, fait, veut, pense, tient, met, croit, doit, peut, semble, demeure, paraît, reste, devient, rend… The frame supplies zero selectional pressure beyond "finite verb" — no agreement controller beyond 3sg, no object, no complement with standing values, no letter-tier/spelling leg. Per the lane's standing precedent (val-03-value-census, masc-noun-86-name), parsing ≠ naming. Naming any one candidate would be arbitrary.
- **Even under the NULL-licensed -ent-adjective premise, sembler vs demeurer are indistinguishable.** If "37 06" is a predicative -ent adjective, the verb must license a predicative complement — the copular subset {sembler, demeurer, paraître, rester, devenir}. Every one of these parses "qui [V-cop] [Xent-adj] pour [33] …" identically: no agreement, object, or complement in the window selects between them. The semantic route narrows the field but names nothing.
- **"Rendre" cannot be killed at battery grade.** Under the adjective premise, "rendre" would need a direct object (none present), but the adjective premise is itself only NULL-licensed, not proven — killing a candidate on an unproven premise is not battery grade. Under rival 37 readings (class open), "rendre" parses as well as any verb.
- **The premise the semantic route depends on is unproven.** The parent battery established that the "37 06" -ent-adjective reading is licensed but cannot be promoted (no adjective nameable; "37 06" hapax, no second window). A discriminator that depends on an unpromoted premise cannot force a value at battery grade.

**C1 FAILS** — no value is forced; the semantic route names nothing.

**C2 fires** — the semantic route is fenced: 23's semantics cannot discriminate the -ent adjective at battery grade, for three independent reasons: (a) the semantic candidate field is open, not closed; (b) the predicative-compatible candidates (sembler/demeurer/paraître/rester/devenir) parse identically; (c) the adjective premise that would license the semantic narrowing is itself only NULL-licensed. Fence is evidentiary, not terminal — re-openable if a closed candidate set emerges (e.g., a named 33 constrains "pour [33]", which constrains the adjective, which constrains the verb).

**Adverses honored:** no split declared (23~26 standing split untouched); 06='ent' conditional untouched; 23=verb class untouched (no value or class named, no downgrade); no standing/red-team verdict contradicted or re-litigated. Canonical-stream caveat stands (row a1_05 offsets unvalidated).

## Per-clause pass/fail

1. **C1 — FAIL.** No semantic candidate is forced at battery grade; the candidate field is open and all candidates parse identically.
2. **C2 — FIRES.** The semantic route is fenced with three stated causes (open field; identical parses among predicative candidates; unproven adjective premise).

## Verdict: NULL (fence executed)

The verb's semantics cannot select the -ent adjective at battery grade. The semantic route is fenced; 23's value at @182 remains open.

## Scope

- Locus-level only (@182). Does not name 23's value, does not touch 23=verb class, does not touch the A1 frame grant, 06='ent', the 23~26 split, or any standing/red-team verdict. §7 intact.
- 23's other 7 windows untouched; the "37ent" spelling remains a live single-leg NULL reading per the parent battery.

## Follow-ups proposed (§4, all verified ABSENT from battery-queue.json)

`adj-ent-pour-frame-census` and `val-37-participle-183` are already queued — not duplicated.

1. `val-33-182-verb` (P4) — name 33's value at @186 ("pour [33]"); a named complement (e.g., "pour dire") selectionally constrains the -ent adjective, which closes the candidate field and re-opens the verb-semantic route with a closed set.
2. `val-23-182-copula-narrow` (P4) — test whether the predicative frame (37+06 as -ent adjective) narrows 23 to the copular class at @182 (class-narrowing, not value-naming); a copular-class leg would close the semantic candidate field for any future re-test.
3. `kill-23-182-rendre` (P4) — locus-kill attempt on "rendre" at @182: "rendre" needs a direct object and no object slot exists under any licensed parse of the window; removes one of the bar's three candidates.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-23-182-semantic.md` (this file).
- Queue: `val-23-182-semantic` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-23-182-semantic.tmp` + atomic rename; JSON re-validated on disk; own entry only; no downgrade; no tmp leftover).
- Lock `code/crowd17/next-token/locks/val-23-182-semantic.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
