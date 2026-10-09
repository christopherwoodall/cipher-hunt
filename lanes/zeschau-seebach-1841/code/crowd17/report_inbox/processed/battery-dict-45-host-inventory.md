# Battery report: dict-45-host-inventory — 45's '-dict-' host inventory

- Target: `dict-45-host-inventory` (battery-queue.json, priority 3, status queued)
- Claim: closed '-dict-' host inventory: 'verdict' the sole host
- Worker: 732ce594-95ed-4b1c-bc69-e317d0f9f190
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered)

"name >=1 non-78 host window parsing as a French dict-word, or certify 'verdict' as the sole host (closed inventory strengthens the positional-polyvalence framing for the red team)"

Numbered clauses (frozen before testing):
1. Arm 1: at least one non-78-hosted window of 45 demonstrably parses as a French word containing the syllable "dict" (d-i-c-t), on stated values with byte-traced windows.
2. Arm 2: if no such window exists, certify 'verdict' (78-45) as the sole host of 45="dict" — i.e. every non-78 window fails to host "dict" on stated grounds (banked/promoted values, distributional kills, or open flanks with no demonstrable French word).

## Method

Re-derived the full 45 census (n=22) on the repaired stream. Split by immediate predecessor = 78 (n=4: @314, @574, @983, @1165) vs != 78 (n=18). For each of the 18 non-78 windows, tested whether the predecessor could be a French stem hosting "dict" (ver-, pré-, malé-, béné-, juri-, contra-, é-, dic-) and whether the follower could complete a dict-word (verdict needs none; diction/dicter/dictée need "tion"/"ter"/"ée"). Kills graded: banked/promoted-value kills first, then distributional kills on the host's own profile, then open-flank (no demonstrable word, no invention allowed).

## Window-level evidence

Certified host set (pre=78, n=4):
- @314 (row a2_04): "24 37 78 45 64" — 78-45-64
- @574 (row a3_02): "52 87 78 45 13" — 78-45-13 (5-gram 78-45-13-55-61, byte-identical x2 with @1165)
- @983 (row a6_01): "76 47 78 45 01" — 78-45-01
- @1165 (row a6_09): "21 67 78 45 13" — 78-45-13 (5-gram 78-45-13-55-61)

Non-78 windows (n=18), all fail to host "dict":

Killed on banked/promoted/provisional values (host+45 or 45+fol forms a non-word):
- @603: 96-45-93 — 96="par" promoted → "pardict" is not French.
- @1214: 96-45-36 — same, "pardict" non-word.
- @1024: 64-45-64 — 64="qui" promoted → "quidictqui" non-word.
- @678: 77-45-23 — 77="le" provisional → "ledict" non-word.
- @1201: 29-45-58 — 29="er" banked → "erdict" non-word.
- @401: 11-45-88 — 11="la" banked → "ladict" non-word.
- @104: 59-45-28 — 59="est" provisional → "estdict" non-word.

Killed by the host's own distribution (host cannot be "ver" or any dict-word stem):
- @262 / @478 / @1055: 74-45-93/93/23. 74: n=34 with 74-74 x6 self-repetition → 74="ver" gives "verver", a non-word; distributional kill. 74-46 x3 also non-"ver"-shaped.
- @332 / @697: 50-45-54/28. 50: n=11; 50-40 ("vere") is a non-word → 50="ver" dead.
- @437: 63-45-46. 63: n=12; 63-00 x4 ("verpour") and 63-29 ("verer") are non-words → 63="ver" dead.
- @974: 51-45-08. 51: n=6; 51-70 ("verpre") is a non-word → 51="ver" dead.
- @1551: 92-45-23. 92: "-ère"-kill holds; 92-98 ("vervient"), 92-79 ("vertout") non-words → 92="ver" dead.
- @340: 14-45-64. 14="sou"/"souv" both killed (souvent-14-06-retest, souv-14-06-repair); 14 is adverb-class; "*[14]dictqui*" (64="qui" promoted) is a non-word.
- @569 / @14: 76-45-94/91. 76 is noun-class (promoted lead); no French word is [noun]+"dict".

Rightward arm (45 + follower as "diction"/"dicter"/"dictée"):
- Followers with standing values give non-words: 64="qui" → "dictqui", 46="que" → "dictque", 94="ne"-lead → "dictne".
- Remaining followers (91, 28, 93, 54, 88, 23, 08, 58, 36) are open-valued; no group anywhere in the stream carries a demonstrated "tion"/"ter"/"ée" value, and inventing one is not permitted. No demonstrable rightward dict-word at any window.

## Per-clause pass/fail

1. Arm 1 (name a non-78 host): FAIL — zero of 18 non-78 windows parse as a French dict-word on stated values; 7 die on banked/promoted/provisional values, 8 die on the host's own distributional profile, and the rightward arm has no demonstrable completion.
2. Arm 2 (certify 'verdict' sole host): PASS — the inventory is closed: the only windows where 45 can sit inside a French "dict"-word are the four 78-45 windows (@314, @574, @983, @1165).

## Adverses

None listed. Two caveats fenced with stated cause:
- 74's value is open; the 74="ver" kill is distributional (74-74 x6), not a value kill. If a future battery names 74 with a "ver"-compatible value, the three 74-45 windows re-open — this verdict's certification is conditional on 74 staying non-"ver".
- This battery certifies the HOST inventory only. Whether 45="dict" requires 78 word-medial (the red team's refined positional candidate) is out of scope — dict-78-45-wordbound and dict-frame-78-45-13-55-61 both returned null on the boundary question and are not re-opened here.

## Verdict

**promote** (narrow, per the claim). The '-dict-' host inventory is closed: 'verdict' (78-45, @314/@574/@983/@1165) is the sole host. No non-78 window of 45 parses as a French dict-word on stated evidence. This is the contact-inventory leg of the 45="dict"-when-78-word-medial candidate; it does NOT by itself promote 45="dict" and does not decide the word boundary.

## Follow-ups

None required (verdict is promote, not null). One note for the red team: the 74-conditional above.
