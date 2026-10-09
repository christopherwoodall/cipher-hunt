# Battery verdict: val-41-40-classconfirm

- Target: `val-41-40-classconfirm` (battery-queue.json, priority 3, status queued)
- Claim: Clean class-level battery: confirm 41's finite-verb CLASS at @40 via the qui-frame (class, not value), with the phase caveat stated; package as input for split-41-redteam.

## Bar (verbatim, numbered)

"class named with the qui-frame + one corroborating verb-slot test, phase caveat explicit; else fence"

- C1. The qui-frame names 41's class as finite verb at the @40 locus.
- C2. One corroborating verb-slot test independently supports the finite-verb class.
- C3. Phase caveat stated explicitly.
- Else: fence.

Note: "adverses" field = "class-level only; feeds split-41-redteam - no split declaration". No split is declared here.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/val-41-40-classconfirm.lock` on start (agent a6f9be7e-8c40-4543-a243-bcbfcbe71db9, 2026-10-09T20:34:00Z).
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types. Asserts held. `canonical.py` never used.
3. Byte-confirmed the locus (0-based): @36=91, @37=39, @38=64, @39=41, @40=01, @41=24, @42=88, @43=43, all row a1_01. n(41)=19 stream-wide (loci verified: 5, 39, 59, 91, 237, 444, 489, 589, 590, 808, 964, 1016, 1048, 1111, 1472, 1499, 1508, 1535, 1759).
4. Adopted (not re-litigated): 64='qui' (granted, protocol §7); 41-808-role PROMOTE (41 standalone word at @808); val-01-40-41-boundary NULL (41|01 word boundary holds; '[41]en'/'[41]tain' composition arms fenced terminally); 41-05-class PROMOTE (41 is the noun-stem of "41+ent" at @5 — the noun arm, locus-specific); 24 = verb-class registry (R17-009); the split-41 question is red-team venue (split-41-redteam docket).

## Findings

### C1 — qui-frame: PASS

0-based @38=64 ('qui', granted) immediately precedes @39=41. The relative pronoun "qui" (subject form, distinct from 46='que') requires a finite verb as the head of its relative clause: "qui [V-fin]" is the canonical subject-relative shape. The interrogative rescue ("qui [V]?") likewise requires a finite verb head. Under every standing analysis of 64, the cell immediately following "qui" must be a finite verb. 41 occupies that slot → **41 = finite-verb CLASS at @39, locus-level, zero new assumptions.**

Rival classes at this slot, all fail:
- Noun: "qui [N]" cannot head a subject relative clause; a noun reading strands "qui" without a verb — ungrammatical.
- Infinitive: "qui [INF]" is ungrammatical as a subject relative (infinitives cannot head a "qui"-relative).
- Sub-lexical (stem/syllable): the 41|01 word boundary holds (adopted val-01-40-41-boundary: both composition arms fenced terminally), so 41 is a standalone word here, not a bound element.

### C2 — corroborating verb-slot test: PASS

Independent locus-level test: the noun-rival elimination via follower mismatch + word-boundary hold.

- The only positive noun-41 evidence stream-wide is "41+ent" at @5 (41-05-class PROMOTE: 41 is the noun-stem of "41+ent" in "ce [N-ent] le [78]"). That noun reading is follower-conditioned on 06 ('ent').
- At @39, the follower is 01, and "41+01" composition is fenced terminally (val-01-40-41-boundary). The noun arm's positive evidence does not transfer to this locus.
- 41 is a standalone word at two independent loci (@39 after "qui"; @808 after finite verbs, 41-808-role PROMOTE), and at @39 the standalone word sits in the finite-verb head slot of the "qui"-relative. Wordhood + slot requirement converge on finite-verb class with no alternative class surviving.

No window forces a non-verb class at @39; the verb slot is exclusively finite-verb.

### C3 — phase caveat: STATED

The target names the locus "@40" in 1-based @-notation. On the repaired 1,847-pair stream (0-based indexing, as used by repair_parse.py), the 41 in question sits at **0-based @39**; "qui" is at 0-based @38. All @-offsets in this report are 0-based. The canonical-stream caveat stands (row a1_01 offsets unvalidated against the manuscript).

## Verdict: PROMOTE

C1, C2, C3 all pass. 41's finite-verb CLASS is confirmed at the @40 (1-based) / @39 (0-based) locus via the qui-frame, with an independent corroborating verb-slot test. The listed adverse is honored: class-level only, no value named, no split declared.

## Scope

- Names only the CLASS (finite verb) at this single locus. No value named.
- No uniformity claim: 41's other 18 windows are untouched; the noun arm at @5 (41-05-class PROMOTE) and the split-41 question remain red-team venue (split-41-redteam docket). §7 intact.
- No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands.
- No follow-ups required (promote, not null). The split-41-redteam docket owns the global question.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-41-40-classconfirm.md`
- Queue: `val-41-40-classconfirm` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-41-40-classconfirm.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/val-41-40-classconfirm.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
