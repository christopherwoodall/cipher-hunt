# Battery verdict: ne30-1701-tail-reconcile

- Target: `ne30-1701-tail-reconcile` (battery-queue.json, priority 3, status queued)
- Claim: "Reconcile the fused 'n'importe' reading at @1701-1702 with conditional 30='pas' (pasX-leftverb-59): does the fused item hold wherever 30='pas' parses elsewhere; tail reading gates every compound parse at the locus."
- Worker: c5db713b-79bc-43ea-9273-168ff527d2db
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/ne30-1701-tail-reconcile.lock` created on start (no stale lock), deleted on completion.

## Bar

Queue's `bars` field is `None` (recorded, not rewritten). Testable bar taken from the dispatch brief (verbatim):

"Resolve whether the fused 'n'importe' reading survives under conditional 30='pas', or fence it."

Numbered clauses (frozen before testing):
1. The fused 'n'importe' item (94+30 via n'-elision, 30='importe') is licensed at its window(s).
2. Conditional 30='pas' parses at its licensed windows, disjoint from the fused item's window(s).
3. No window admits both readings (strict complementary distribution); the tail (@1703-1719) is compatible with the fused item and gates any compound parse at the locus.

## Method

Full 30 census (n=19, re-derived in-session on the repaired stream; asserts held): for each @30 window, recorded predecessor (94-adjacency test for the fused item; 59-adjacency for the conditional 'pas'), successor, and standing values. Adopted without re-litigation: ne-30-1700 NULL (@1702 fenced; 30='pas' killed at @1702 by "inf ne pas" word order; 'importe' word-formation licensed, clause parse stalled on open 85/33), pas-30 PROMOTE (conditional on red-team ratification; re-open caveat requires clause-level 30='importe' demonstration at @1702), pasX-leftverb-59 PROMOTE ("59 30" = "est pas" at @560/@1716), importe-30-elision-test NULL (no window forces consonant-initial 30; no second "n'importe" frame), contredire-85-33-vehicle PROMOTE (evidence-gathering only; compound unpromoted, red-team venue).

## Window-level evidence

30 census (predecessor → [30] → successor, standing values):

| @ | left | [30] | right |
|---|------|------|-------|
| 30 | 24(verb) | [30] | 03(verb-stem) |
| 45 | 81(?) | [30] | 62(?) |
| 483 | 52(?) | [30] | 01(?) |
| 560 | 59(est) | [30] | 67(?) |
| 656 | 26(noun) | [30] | 03(verb-stem) |
| 742 | 20(?) | [30] | 67(?) |
| 993 | 26(noun) | [30] | 03(verb-stem) |
| 1114 | 38(verb) | [30] | 69(noun) |
| 1222 | 48(e) | [30] | 09(?) |
| 1251 | 26(noun) | [30] | 06(ent) |
| 1269 | 24(verb) | [30] | 20(?) |
| 1309 | 52(?) | [30] | 92(verb) |
| 1327 | 56(?) | [30] | 06(ent) |
| 1368 | 03(verb-stem) | [30] | 82(m) |
| 1561 | 26(noun) | [30] | 06(ent) |
| **1702** | **94(ne)** | **[30]** | 20(?) |
| 1716 | 59(est) | [30] | 64(qui) |
| 1729 | 24(verb) | [30] | 15(?) |
| 1733 | 56(?) | [30] | 06(ent) |

- **94-30 adjacency: exactly 1× stream-wide (@1702).** The fused 'n'importe' item (n'-elision of ne+importe) can form at one window only.
- **59-30 windows: @560, @1716** — the pasX-leftverb-59 conditional contexts ("est pas").
- **@1702 under 30='pas':** dead (adopted ne-30-1700 C1: "[33-inf] ne pas" word order ungrammatical; no clause-boundary rescue since 20 is noun-profiled).
- **Tail @1703-1719:** `20 62 94(ne) 88(gov) 26(noun) 12(n) 06(ent) 29(er) 40(e) 65(noun) 94(ne) 44 59(est) 30(pas) 64(qui) 47(ce) 68(noun)`. The @1713-1716 segment `94-44-59-30` = "ne [44] est pas" parses as an independent 'ne...pas' clause (adopted from ne-30-1700's wider-context note and pas-30's clause-2 frame). The tail is therefore multi-clausal regardless of the @1702 reading: any compound parse at the locus must place "n'importe [20]..." in a clause that ends before or embeds the @1713 clause. The tail constrains (gates) but neither kills nor confirms the fused item — it is compatible with it and independent of it.

## Per-clause results

1. Fused 'n'importe' licensed at its window: **PASS** — @1702 is the sole 94-30 adjacency; n'-elision licensed per the ne-94 grant (adopted); no other window can host the fused item.
2. Conditional 30='pas' parses at disjoint windows: **PASS** — @560/@1716 "est pas" per pasX-leftverb-59 PROMOTE; @1702 excluded by word order (adopted kill). The 'pas' grant never touches the fused item's only window.
3. Strict complementary distribution; tail gates the compound: **PASS** — zero windows admit both readings; the tail's independent "ne [44] est pas" clause gates every compound parse at the locus without deciding the @1702 reading.

## Adverses (answered, not ignored)

- **pas-30 re-open caveat:** NOT triggered. The caveat requires ne-30-1700 (or this battery) to demonstrate 30='importe' at clause level at @1702. This battery demonstrates only the distributional reconciliation (word-formation + complementary distribution); the clause-level parse still stalls on open 85/33/20 (adopted). pas-30's promotion stands untouched.
- **No standing/red-team verdict contradicted, downgraded, or re-litigated.** 94='ne' used with its ratification-pending caveat; 85's value unnamed; 33's dire/croire tie untouched; 67 sole-polyvalence respected; §7 intact.
- **contredire vehicle:** remains evidence-gathered-only, red-team venue; this reconciliation does not adopt or need it.

## Verdict

**PROMOTE** — the reconciliation resolves: the fused 'n'importe' item survives at @1702 (sole 94-30 adjacency, elision-licensed) in strict complementary distribution with conditional 30='pas' (licensed at its disjoint windows, excluded at @1702 by word order). No window admits both readings; no conflict exists between the two grants. The tail (@1703-1719) gates every compound parse at the locus via its independent "ne [44] est pas" clause without deciding the @1702 reading.

Scope: distributional reconciliation only. Does NOT name 30='importe' at clause level, does NOT trigger pas-30's re-open caveat, does NOT name 85's value or resolve the 33 tie. Canonical-stream caveat stands.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ne30-1701-tail-reconcile.md`
- Queue: `ne30-1701-tail-reconcile` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.ne30-1701-tail-reconcile.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
