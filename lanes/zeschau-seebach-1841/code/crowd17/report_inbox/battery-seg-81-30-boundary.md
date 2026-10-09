# Battery verdict: seg-81-30-boundary

## Bar (verbatim, pre-registered)

"one segmentation of the @44–45 junction parsing under standing values, or fence"

Restated as numbered clauses:
- **C1:** A word-MEDIAL segmentation of the @44–45 junction (81–30 as one word, e.g. "[81]pas") parses under standing values — the compound word is identified and grammatical at the junction, with no standing-value contradiction at 81's other windows.
- **C2:** A word-BOUNDARY segmentation (81 ‖ 30, two words) parses under standing values — "[81-noun] pas" is grammatical at the junction with 30's standing value and no ungranted-value assumption.
- **Clause rule:** exactly one of C1/C2 may promote (they are mutually exclusive). If neither parses, the junction is FENCED with stated cause and the verdict is NULL.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/seg-81-30-boundary.lock` on start (agent id + UTC timestamp). Re-derived the stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (1,847 pairs / 96 types verified). `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched. @-offsets below use the lane's 0-based global convention, matching the parent report `processed/battery-seg-30-62-96.md` (@44=81, @45=30, @46=62, @47=96, @48=00).

## Byte evidence

Window @44–48 (row a1_01) = "81 30 62 96 00". Full row a1_01 (@35–69):

```
08 91 39 64 41 01 24 88 | 43 81 30 62 96 00 | 92 79 37 11 79 85 58 35 53 12 41 08 34 29 40 12 94 92 69 13 24
```

- **81–30 bigram occurs exactly 1x stream-wide** (hapax contact). No corroborating "[81]pas" compound window exists anywhere on the stream.
- No ne-particle (94/48/12) occurs anywhere left of @45 on row a1_01 (@41=24 is 24=finite modal per battery ne-24-profile promote; @58=12, @65=94 are right of the junction).
- Standing values used (battery-grade counted as standing per the parent report's convention): 30='pas' (battery promote 2026-10-08), 81 = masculine abstract noun, value open (battery promote 2026-10-09), 96='par' (granted), 00='pour' (A9 class-level), 24 = finite modal (battery promote), 88 = verb class (battery 2026-10-09, six legs). Open neighbors: 43 (noun-43 nulled, verb-stem lead open), 62 ('on' unconditioned ELIMINATED; 'il' rival demonstrated not promoted), 88's finiteness open.

## C1: word-medial "[81]pas" — FAIL (does not parse under standing values)

French "-pas" final compounds form a closed tiny set: "trépas" (death, masc. noun), "contrepas" (dance step, masc. noun).

- **"trépas" (81="tré"):** class-compatible with 81's noun class, and "le trépas" parses at @1242/@1403 ("le [81] cela"). BUT: (a) 81="tré" has zero positive legs — the 81–30 contact is a hapax (x1), and "trépas" is a rare literary word with no supporting window; (b) "trépas" is strained at the two purpose-complement windows that underpin 81's class promote — @552 "…le trépas pour [86-er]…" and @1087 "…le trépas pour [33-er]…" ("death" taking "pour + infinitive" purpose clauses is semantically anomalous; the class promote rested on the moyen/ordre/droit/besoin agentive family). Not promotable on a hapax with adverse windows.
- **"contrepas" (81="contre"):** zero evidence; "contre" attribution elsewhere (85) is itself a red-team tension. Rejected.
- Sub-word composition is licensed lane-wide (n-e-12-48 letter duality), but no identified word parses the junction. C1 FAILS.

## C2: word boundary "[81] pas" — FAIL (does not parse under standing values alone)

With 30='pas' (battery promote):

- **"pas" as negation:** no "ne" in the left clause. The lane's ne-drop precedent (pas-30) licenses "pas" without "ne", but negation still needs a verb and an object: the only candidate frame is "…[88-verb] [43] [81] pas…" = "…[verb] [43] [81] not" with ne dropped. This needs THREE ungranted assumptions: 88 = finite verb (only verb-class battery), 43 = NP-internal modifier (43's class open; noun-43 nulled), and "pas" clause-final after the object. Not a clean parse — fenced, not promoted.
- **"pas" as noun ("step"):** "[81-noun] [pas-noun]" needs "de" or a determiner — absent. Fails.
- **"pas" in a frozen compound ("pas à pas", "au pas"):** no 30-contact supports any frozen form at this junction. Fails.

C2 FAILS: every grammatical two-word reading needs an open value (43's class, 62's value, 88's finiteness).

## Junction fence

- The @44–45 junction is **FENCED**: 81–30 is a hapax contact (x1); neither a word-medial compound nor a word boundary parses under standing values alone. The fence's blockers are named: 43's class (left edge), 62's value (right edge — 62='on' unconditioned ELIMINATED, 'il' rival unpromoted), 88's finiteness.
- No contradiction with any standing verdict: pas-30's legs are @558/@1713-class ne-frames, not @45; noun-81's promote is class-level (value open) and its @45 window was already fenced on open 43; seg-30-62-96's @46 fence stands untouched.
- Context note: the rival-phase question (battery 04:52:59 — offset-1 reparse of row a1_01 is constraint-clean) may dissolve this junction entirely; queued as a follow-up below.

## Per-clause results

| Clause | Result |
|---|---|
| C1 (word-medial "[81]pas" parses) | FAIL — "trépas" hapax-backed with adverse windows; "contrepas" unevidenced |
| C2 (word boundary parses) | FAIL — needs open values (43 class, 88 finiteness) |
| Fence | HELD — junction fenced with stated cause |

## Verdict: NULL

Neither segmentation parses under standing values. The 81–30 boundary at @44–45 stays fenced, not decided.

## Follow-ups (null regenerates work)

1. `seg-81-30-trépas-kill` (P3): kill-grade adjudication of 81="tré". Bars: (a) corpus test — "trépas pour + infinitive" in 1841 diplomatic French (zero hits expected); if the @552/@1087 purpose-complement windows cannot host "trépas", kill "trépas" as 81's value; (b) any second "[81]pas" contact stream-wide kills or saves the compound arm. Discriminator: the purpose-complement leg set.
2. `prof-43-object` (P2): 43's class census to decide the two-word parse's left edge. Bars: name 43's class with >=3 frame legs; if "43 81" forms a direct-object NP under 81-noun, the "…[88] [43] [81] pas" ne-drop-negation parse becomes promotable and this fence re-opens.
3. `seg-81-30-offset1` (P3): offset-1 reparse of row a1_01. Bars: re-derive the @44–45 junction under the rival phase (battery 04:52:59: offset-1 reparse constraint-clean, dissolves "la tout"); if the junction dissolves, close this line with byte evidence; if it survives, re-test C1/C2 under the rival phase.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-81-30-boundary.md` (this file).
- Queue: `battery-queue.json` `seg-81-30-boundary` → status `verdict`, result `null`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated post-write).
- Lock: `locks/seg-81-30-boundary.lock` created on start, deleted on completion.
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched; all counts re-derived on the repaired 1,847-pair stream.
