# Battery report: w3-06-attach-62

- Target id: `w3-06-attach-62`
- Claim: W3's stranded 06 re-tested once 62's value is named.
- Date: 2026-10-09
- Worker: battery worker (subagent b94dacb8-2cf7-4344-827c-b66ec9982cc2)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset note: the brief uses 1-based @1327 for the W3 window. This report uses 1-based throughout: 06 is at 1-based @1329 (the parent's 0-based @1328). Same locus.

Terms (ASD-STE100): "word" = a French word that the cipher writes with number groups. "residual" = a number that no licensed word can contain at this window. "fence" = set aside with a stated cause, not killed. "battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"06 placed in a grammatical word at W3 ('ent'+[62] iff 62 names a compatible continuation; else 06 attaches left or fences as a genuine residual, which re-opens the two-word 'pas | ent' shift) or 06 fenced as residual with stated cause"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 06 placed in a grammatical word at W3 via the 'ent'+[62] composition — 62's named value yields a French word.
2. **C2:** else 06 attaches left ("30 06" = "pasent") as a grammatical word.
3. **C3:** else 06 fenced as a genuine residual with stated cause (re-opening the two-word "pas | ent" shift).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/w3-06-attach-62.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session (asserts held). All @-offsets below are 1-based.
3. Adopted standing values, not re-litigated: 30='pas' (battery-promoted, pas-30, conditional); 06='ent' (battery-promoted, ent-06); 94='ne' (battery-promoted, ne-94); 62='il' (battery PROMOTE, il-62, 2026-10-08; registry lead pending red-team adjudication); 62='on' unconditioned KILLED (collision-62-84); 62 noun values (règne/trône) NULL-tied (val-62-ne-noun); §7 (67 et/veut sole polyvalence); 39='a' (battery-promoted, a-39); spell-single-consonant KILL of the clerk "pasent" license.
4. Trigger check: the gate ("62's value being named") fires on il-62's PROMOTE — the only battery-grade 62 value, already the parent's premise (parent used 62='il' as demonstrated rival). No NEW 62 value has landed since the parent (subj-62-plural-94 KILL concerns number, not value; val-62-ne-noun NULL names nothing).

## Window-level evidence

Locus byte-confirmed (row a7_04):
- 1b@1325=62, @1326=98, @1327=56, @1328=30, **@1329=06**, @1330=62, @1331=94, @1332=70.
- "06 62" is a stream hapax (1b@1329 only) — zero repetition leverage for any word-formation precedent.
- "30 06" exactly x4 stream-wide (1b@1252/@1328/@1562/@1734); W3's is instance 2.
- Flanking clauses (parent's, adopted): "…[03]er [80] [08] | il(62) [98-verb] [56] pas" with ne-drop, and "il(62) ne(94) pre[52] a(39) [83]" with lone 'ne'. Both parse under standing values; 06 is the isolated problem.

## Per-clause pass/fail

- **C1 — FAIL.** 'ent'+[62] composition under every 62 candidate: 62='il' → "entil" (not a French word); 62='on' → "enton" (not a French word; value killed unconditioned anyway); 62='règne'/'trône' → "entrègne"/"entrône" (not French words; values NULL-tied and would break the parent's "62 94"='il'+'ne' reconciliation). No named 62 value gives a compatible continuation.
- **C2 — FAIL.** Left-attach "30 06" = "pasent": not a French word; the clerk single-consonant license is dead at kill grade (spell-single-consonant).
- **C3 — FIRES.** 06 fenced as a genuine residual at W3 with stated cause: (1) the only battery-grade 62 value ('il') composes nothing grammatical; (2) left-attach is a non-word; (3) "06 62" is a hapax (no precedent); (4) §7 bars inventing a second 62 value; (5) nothing about 62 changed since the parent — the gate's trigger was already its premise, so this is a confirmed fence, not a new failure. The fence re-opens the two-word "pas | ent" shift: 06 stands word-initial 'ent' with an open continuation, unconstradicted.

## Adverses (answered, not ignored)

- "gated on 62's value being named": ANSWERED — the trigger fires (il-62 PROMOTE, 2026-10-08). The trigger being satisfied does not change the outcome: the named value is incompatible, so the bar's else-arm fires.
- No standing/red-team verdict contradicted or downgraded (30='pas', 06='ent', 94='ne', 62='il' rival, §7, il-62 PROMOTE, collision-62-84 KILL, spell-single-consonant KILL all untouched). Canonical-stream caveat stands (row a7_04 offset unvalidated).

## Verdict: NULL (fence executed per the bar's C3 arm)

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `w3-06-rerun-gated` (P4) — gated re-run of the 'ent'+[62] composition once the red team adjudicates 62's global value (il-62 promote → banked) or a NEW 62 value lands; converts this fence to a place/kill.
2. `pas-ent-shift-survey` (P3) — survey 06's fate at the other three "30 06" windows (1b@1252/@1562/@1734); if 06 is placed in a word at any of them, W3's residual is likelier a parsing artifact than genuine — re-audit the window.
3. `w3-06-a704-validate` (P4) — validate row a7_04's offset against manuscript evidence; an offset shift would move 06's adjacency (and the "06 62" hapax) entirely.

## Bookkeeping

- Queue: `w3-06-attach-62` → status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/w3-06-attach-62.lock` created on start, deleted on completion (verified gone).
