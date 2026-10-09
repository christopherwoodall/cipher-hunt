# Battery report: seg-62-48-word

- Target id: `seg-62-48-word`
- Claim: Test whether "62 48" x6 (@360, @425, @1315, @1349, @1464, @1569) is one word ("62e"); resolves the word boundary currently blocking both the noun and adjective readings of the largest sub-family.
- Date: 2026-10-09
- Worker: battery worker (subagent 6486118e-9c3c-42bc-9dd7-f9eb3cce076a)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`); asserts held (1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

"Byte-level left/right attachment profile decides one-word vs two-word, or fence with stated cause."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** Re-derive the six "62 48" windows byte-exact and state 62's and 48's left/right attachment profiles at battery grade.
2. **C2:** Decide one-word vs two-word on the attachment profile with byte evidence; kill-grade if a window forces one reading false.
3. **C3:** If undecidable, fence with stated cause.

## Method

Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/seg-62-48-word.lock` on start (agent id + UTC timestamp); deleted on completion. Adopted, never re-litigated: `il-62` PROMOTE (2026-10-08, battery: all 35 62-windows parse under 62='il', zero hard contradictions), `sel-62-48-94` KILL (2026-10-09: no 62 value makes 62-48 and 62-94 one morpheme — nn-final X space exhausted, every candidate dies at 62-06 or @1772), `seg-62-94-wordfinal` KILL, `part-62-elsewhere` KILL (no participial 62). Adverses honored: `redteam-62-conditioned` (queued P1) not re-litigated — no polyvalence declared here.

## C1 — attachment profiles (all re-derived in-session)

n(62)=35, n(48)=38. "62 48" occurs exactly 6x: @360 a2_06, @425 a2_09, @1315 a7_04, @1349 a7_05, @1464 a7_09, @1569 a8_01.

- **62's profile:** 12 distinct predecessors (21x5, 20x4, 74x3, 93x2, 03x2, 08x2, 78x2, 92x2, then singletons), 13 distinct successors (94x9, 48x6, 98x5, 16x4, 61x2, 06x2, then singletons). Free-combining on both sides — the free-word signature, consistent with il-62's subject-pronoun parse of all 35 windows.
- **48's profile:** 15 distinct predecessors (62x6 top, 12x5, 82x4, 32x4, 89x3, 78x2, 24x2, then singletons), highly heterogeneous successors (21/52/76/20/47/77/96/29/56 x2 each, then singletons). 48="e" (letter) composes word-internally elsewhere ("ne"=12 48 x5; "me"=82 48 x4 possible), so 48 is not forced word-final at the 62 loci — the question is whether 62 is bound.
- **Six loci (±3):**
  - @360: `47 11 21 | 62 48 | 76 47 78` — "ce(47) la(11) [21-N] [62] e[48] [76] ce(47) [78]"
  - @425: `29 47 14 | 62 48 | 76 42 63` — "er(29) ce(47) [14] [62] e[48] [76] [42]"
  - @1315: `00 36 74 | 62 48 | 98 15 24` — "pour(00) [36] [74] [62] e[48] vient(98)"
  - @1349: `66 73 34 | 62 48 | 77 78 94` — "[66] [73] i(34) [62] e[48] le(77) [78] ne(94)"
  - @1464: `17 01 21 | 62 48 | 21 02 62` — "fois(17) [01] [21] [62] e[48] [21] [02] [62]"
  - @1569: `29 24 74 | 62 48 | 56 32 28` — "er(29) [24] [74] [62] e[48] [56] [32]"

## C2 — decision: TWO WORDS (kill of the one-word "62e" reading)

1. **Under the standing value 62='il'** (il-62 PROMOTE: all 35 windows parse, zero hard contradictions), 62 is a free word at every window including the six loci. The one-word reading "62e" = "ile" is not a French word — forced false at all six windows. **Kill grade.**
2. **No rival letter value rescues the one-word reading.** The only letter-tier candidates that make "X+e" French are nn-final stems (don/donn/men/vien/tien/person), and `sel-62-48-94` exhaustively killed that space: every candidate dies at the 62-06 discriminator ("donent" not French, "donne" triple-n, "mene" impossible) or at @1772's grammar. No other 62 letter value stands at any grade.
3. **The attachment profile independently forces two-word under the lane's "word-internal iff bound" standard** (the 89-word-internal fork kill precedent): 62 is free-combining on both sides and determinably a free word (il-62), while 48's heterogeneity shows no unit signature with 62 (no bigram formula, 6/35 of 62's followers, 6/38 of 48's predecessors). 48 at the six loci reads as the word-initial "e" of its right neighbor's word.

**C2 fires at kill grade.** C3 does not fire.

The queued `redteam-62-conditioned` (conditioned split: 62='il' in the 62-94 clitic sequence vs independent 62 elsewhere) is not pre-judged: under the split, independent-62-elsewhere still yields two words at the 62-48 loci — the split only concerns the 62-94 sequence. No second polyvalence declared; §7 intact.

## Adverses

- "Does not duplicate queued redteam-62-conditioned" — honored: the conditioned split is untouched (see above).
- "stem-62-ent-665-1536 covers the '62 06' x2 windows" — honored, not re-litigated; the 62-06 discriminator is adopted as premise via sel-62-48-94.

## Verdict: KILL

The one-word "62e" reading is forced false at kill grade under the standing 62 value (62='il', free word at all 35 windows) and has no surviving letter-tier rival. "62 48" x6 is two words: free 62 + e-initial right neighbor. No standing/red-team verdict contradicted or downgraded (§5: the banked 40-cell registry contains no 62 cell; redteam-62-conditioned remains queued and is consistent with this verdict). Canonical-stream caveat stands (loci rows unvalidated).

## Supervisor observations (kills regenerate no follow-ups per §4; not queued targets)

- Per the target's premise, the word boundary that blocked 62's noun/adjective readings at the largest sub-family is now resolved two-word: the 62-48 loci parse as independent-word 62 (value 'il' per il-62) followed by an e-word.
- The e-word following 62 at @360/@425 (@76 successor x2) remains the sharpest residual of the six windows.
