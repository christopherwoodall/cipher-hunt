# Battery verdict: seg-30-62-96

**Verdict: NULL** — no grammatical word-medial segmentation of @44–48 exists under standing values; @46 fenced as an irreducible residual with byte evidence. Work regenerates via the three follow-ups below.

## Bar (verbatim, pre-registered)

> produce one grammatical segmentation of @44-48 ("81 30 62 96 00") with 62 word-medial, or fence @46 as an irreducible residual with byte evidence

Numbered clauses (pre-registered before testing):
1. (Arm 1) One grammatical segmentation of @44–48 exists with 62 **strictly word-medial** — inside a multi-pair French word, honoring standing values 30='pas', 96='par', 00='pour'.
2. (Arm 2, alternative) @46 is fenced as an **irreducible residual with byte evidence** — no word-medial placement is grammatically available AND the independent-word route is already exhausted.

## Method

Read BATTERY-PROTOCOL.md first; lock `locks/seg-30-62-96.lock` created on start (agent id + UTC), no stale lock present. Re-derived the window from the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` — same tokenization, re-run inline). `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.

Value key used (all standing, §7): 30='pas' (battery-promoted 2026-10-08), 96='par' (granted), 00='pour' (granted A9), 39='a/à' (promoted), 64='qui' (granted).

## Window-level evidence (@-offsets, repaired stream)

Re-parse of row a1_01 (byte-exact):

| @ | pair | row | standing value |
|---|------|-----|----------------|
| 36 | 91 | a1_01 | — |
| 37 | 39 | a1_01 | à |
| 38 | 64 | a1_01 | qui |
| 39 | 41 | a1_01 | — |
| 40 | 01 | a1_01 | — |
| 41 | 24 | a1_01 | — |
| 42 | 88 | a1_01 | — |
| 43 | 43 | a1_01 | — |
| **44** | **81** | a1_01 | — (open; noun-81 queued) |
| **45** | **30** | a1_01 | **pas** |
| **46** | **62** | a1_01 | — (target) |
| **47** | **96** | a1_01 | **par** |
| **48** | **00** | a1_01 | **pour** |
| 49 | 92 | a1_01 | — |

Window @44–48 = "81 30 62 96 00" = "[81] pas [62] par pour". Confirmed against the repaired stream (1,847 pairs).

## Clause 1 test (Arm 1): word-medial segmentation — FAIL

For 62 to be **strictly word-medial** in a segmentation of @44–48, the word containing @46 must include at least one pair on each side of @46, drawn from @44–48. Candidate containing-words:

- (44,45,46) = 81-30-62 → 62 word-**final**. Excluded by the bar as written.
- (45,46,47) = 30-62-96 → 62 medial. Requires a French word of shape **"pas"+X+"par"** (pairs @45 and @47 are consecutive inside the word and pinned to "pas"/"par").
- (44,45,46,47) = 81-30-62-96 → 62 medial. Requires "[81]pas"+X+"par" — contains "pas"+X+"par" contiguously regardless of 81.
- (45,46,47,48) = 30-62-96-00 → 62 medial. Requires "pas"+X+"par"+"pour".
- (44,45,46,47,48) → whole window one word. Requires "[81]pas"+X+"parpour".

Every medial candidate therefore demands a French word containing **"pas"+X+"par" contiguously**. Lexicon check (single-letter through syllable 62):

- 62 = single letter → "pas?par": no French word.
- 62 = "se" → "passepar": exists **only** inside "passe-partout" (solid "passepartout"). "passe-passe" lacks "par"; "passeport" contains "passepor", not "passepar"; no other "passepar-" word.
- 62 longer → "pas"+X+"par": no other French word family.

The **sole lexicon neighbor is "passe-partout"** = pas/se/par/tout. It fits @45–47 byte-perfectly under 62='se', but @48 = 00 = **'pour' (granted A9)** — the compound needs 'tout'. **Byte-excluded at exactly one pair** (@48: 'pour' vs 'tout').

Result: no grammatical word-medial segmentation of @44–48 exists under standing values. Clause 1 **FAIL**.

## Clause 2 test (Arm 2): fence @46 as irreducible residual — PASS

- Independent-word route: already exhausted by battery-class-62-fullcensus — @46 defeats every word-class hypothesis ("pas il par" ungrammatical; finite verb fails for want of "ne"; noun/adjective/adverb/preposition/determiner all fail). The pas-30 battery glossed @45 as "...pas par... ('not by ...')" and marked it parsing **while leaving 62 itself unparsed** — no contradiction with this fence.
- Word-internal route: exhausted above (Clause 1) — the only lexicon neighbor is byte-killed at @48.
- Byte evidence: pairs @44–48 are fixed bytes (81,30,62,96,00) on row a1_01 of the repaired stream; @45='pas', @47='par', @48='pour' are standing; any medial placement of 62 forces "pas"+X+"par", whose unique French host is byte-excluded.

@46 is therefore fenced as an **irreducible residual**: 62 can be placed neither as an independent word nor word-internally at this window on current evidence. Clause 2 **PASS**.

## Per-clause results

1. Word-medial segmentation produced: **FAIL** — lexicon + byte evidence (sole neighbor "passe-partout" killed at @48 by 00='pour').
2. @46 fenced as irreducible residual with byte evidence: **PASS**.

## Adverses

None stated in the queue entry. Standing constraints honored: 30='pas', 96='par', 00='pour' not re-litigated; the "passe-partout" near-miss is recorded as a follow-up rather than a backdoor re-read of 00 (battery may not overturn the A9 grant — red-team venue).

## Verdict: NULL

The bar's second arm is satisfied (residual fenced), but no positive segmentation was produced and no standing value was confirmed or killed at grade. Null regenerates work:

## Follow-ups (null regenerates work)

1. `lex-passepartout-48` (P2): adjudicate the "passe-partout" near-miss at @45–48. It fits @45–47 byte-perfectly under 62='se' and dies only at @48 (00='pour' granted vs needed 'tout'). Bars: parse @44–48 as "[81] passe-partout" — escalating the 00 conflict to the red team (battery may not overturn A9) — or kill the compound with 00='pour' byte evidence plus 81's profile. Discriminator: any other "passe-X" compound in the corpus.
2. `seg-81-30-boundary` (P3): decide the 81–30 boundary at @44–45 — one word ("[81]pas", e.g. "trépas"-shaped, 81 named) vs two words. Bars: name 81 with the compound parsing, or fence a two-word boundary with 81's class evidence. Narrows 62's left edge for any future segmentation attempt.
3. `adv-62-pas-par` (P3): test 62 as an adverb in "pas [62] par" ("pas même/seulement par"-shaped, "not [even] by"). The pas-30 battery's "...pas par... ('not by ...')" gloss at @45 skipped 62; a named adverb would close the gap with 62 as an independent word. Bars: name the adverb with >=2 independent "pas [adv] par/pour/à" frames on the repaired stream, or fence @46 as adverb-incompatible with stated cause. Narrower than queued class-62-nof94; does not duplicate it.

## Bookkeeping

- Lock `locks/seg-30-62-96.lock` created on start (agent id 7c4b753c + UTC 2026-10-09T02:48:35Z), no stale lock present; deleted on completion.
- `battery-queue.json`: target `seg-30-62-96` queued → verdict/null (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict).
- R5005, sealed gate instances, red-team adjudication queue untouched. No standing verdict contradicted or downgraded.
