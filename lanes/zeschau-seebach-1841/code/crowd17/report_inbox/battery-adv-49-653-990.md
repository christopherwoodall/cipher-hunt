# Battery verdict: adv-49-653-990

- Target: `adv-49-653-990` (battery-queue.json, priority 3, status queued → verdict)
- Claim: test adverb-49 at the byte-identical '76 49 24' x2 frame (@653/@990).
- Worker: 09a190b5-b1af-44d9-b82d-ff12c45436f9. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/adv-49-653-990.lock` created on start (no stale lock); deleted on completion.

## Bar (verbatim, pre-registered)

"name iff both windows parse with <=1 total unstated assumption; else fence adverb-49"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name arm):** both windows (@653 and @990) parse with 49 as an adverb, using at most 1 total unstated assumption across both windows.
2. **C2 (else arm):** fence adverb-49.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed both loci and their full ±10 context.
3. Fixed the standing frame from protocol §7 + red-team rounds: 76 noun-class (promoted), 24 finite/modal (R24: follower 26 ≠ 85, so 24 ≠ 'en' here), 94 = "ne" STRONG LEAD (R17-001), 30 = "pas" conditional (R20).
4. Tested the adverb-49 parse against the 1841-French adverb inventory for the required geometry "[76-N] [49-adv] [24-Vfin]" (bare, no punctuation).

## Window-level evidence

**W1 @653 (row a4_02):** `61 88 77(le*) 78 52 82(m) 94(ne-L) | 76 49 24 | 26 30 03 62 16 00(pour) 86`
**W2 @990 (row a6_01):** `48 01 76 49 24 | 26 30 03 60 67 11(la) 96(par)` — preceded by `07 76 47(ce) 78 45(ce) 01 24 89 48 01`.

- The bigram "76 49 24" is byte-exact at @652–654 and @989–991 (49 at @653/@990).
- The 6-gram "76 49 24 26 30 03" is byte-identical ×2 (divergence only at the 7th cell: 62 vs 60).
- n(49) = 12 stream-wide; the "[N] 49 [Vfin]" geometry occurs ONLY at these two windows (@1433 is "76 49 64", different frame).

## Clause results

- **C1: FAIL — at kill grade, on grammaticality, with zero new assumptions.** The adverb-49 parse requires the bare geometry "[76-N] [49-adv] [24-Vfin]": an adverb sitting unpunctuated between a subject nominal and its finite verb. No adverb in the 1841 inventory licenses this position — bien/tout/si/plus/tant/encore/toujours/souvent/déjà/presque/soudain/ainsi are post-verbal or parenthetical; pronominal "y"/"en" would need "ne" after the subject ("n'y vient"), but here 94="ne" precedes the nominal 76. The failure is structural, not lexical: even granting 49 any adverb value (the 1 permitted assumption), no grammatical parse results at either window. The "ne … pas" frame ("94 … 24 … 30") cannot rescue it — "ne" before a subject NP is unlicensed.
- **C2: FIRES — adverb-49 fenced** at the "[N] [49] [Vfin]" geometry (both windows; the only two windows with this geometry).

## Adverses

1. **"adverb-49 strained at @909 ('[54] [49-adv] qui')"** — answered: consistent and independent. This fence does not depend on @909; @909's strain stands as its own locus finding.
2. **"noun-74-formula scope"** — answered: consistent with R20's coordinator override fencing formula-76-49-24 (the N-ADJ-Vfin license proved vacuous after adjective-49 died at kill grade). This battery's N-ADV-Vfin fence is the adverb-side twin, narrower and independently derived.

## Verdict: PROMOTE (fence executed, bar's else-arm)

The fence is kill-grade in character (reading-independent grammatical impossibility under standing classes) but is recorded as the bar's fence arm, locus-scoped to the "76 49 24" frame geometry. Per §4 (promote), no follow-ups required.

## Scope

Fences adverb-49 at the "[N] [49] [Vfin]" geometry only (@653/@990 — the sole two windows with this geometry). 49's class at its other 10 windows untouched; no value named; no class granted. No standing/red-team verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands.

Natural next questions (not queued — promote verdict): `val-74-letter` (already queued by sibling battery) bears on the '74 74' chain windows; 49's remaining viable tiers are noun (strained) and syllable/letter.

## Bookkeeping

- `battery-queue.json`: `adv-49-653-990` queued → verdict/promote (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/adv-49-653-990.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
