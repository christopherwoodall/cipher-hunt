# Battery `mannequin-62-98-test` — verdict: KILL

**Bar (verbatim, pre-registered):** "kill or fence the near-miss (62-94 x9 "manne", 62-48 x6 with 48="e" banked, 62-98 x5)"

**Numbered clauses:**
- K1: the joint claim 62="man" / 98="n" is killed iff a window forces either half false at kill grade (a window parses no French under the claim with no granted rescue).
- K2: else the near-miss is fenced with stated cause (null).

**Method:** Read BATTERY-PROTOCOL.md first. Created `locks/mannequin-62-98-test.lock` on start. Re-derived the full 1,847-pair stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (verified 1,847 pairs / 96 types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched. Counts re-derived: 62 n=35, 98 n=40; 62-94 x9 @100/@508/@761/@840/@1329/@1362/@1686/@1704/@1772; 62-48 x6 @360/@425/@1315/@1349/@1464/@1569; 62-98 x5 @11/@802/@945/@1136/@1324. All match the bar.

**Standing values used:** 48="e" general letter value (red-team granted, R17-003; A7-L2 verb-stem frame narrowed to its exclusive legs). 46="que", 82="m", 64="qui" ground truth. 98="vient" battery-level (4 frame types, zero contradictions across 40 windows) — cited, not re-tested.

## Findings

**K1a — 62="man" killed by 62-48 x6 ("mane").**
Under 62="man", every 62-48 window reads "man"+"e"="mane". "Mane" is not a French word in any period (English: a lion's mane; French is "crinière"). The only granted non-letter reading of 48 is the A7-L2 verb-stem frame ("tout me [48-verb]"), which requires "79 82" immediately left. Left context of the six windows: @360 "47 11 21 |62 48", @425 "29 47 14 |62 48", @1315 "00 36 74 |62 48", @1349 "66 73 34 |62 48", @1464 "17 01 21 |62 48", @1569 "29 24 74 |62 48". None is "79 82", so the A7-L2 narrowing is inapplicable at all six; 48="e" letter reading holds. Six windows force the claim false. Kill grade.

**K1b — 98="n" killed by 98-83 x5 (stranded 'n').**
Under 98="n", "98 83" = "n"+"de". The 'n' must be word-final or word-initial; "nde" is not a French word, so it must be word-final, with the stem in the preceding group(s). The five windows: @227 "46 98 83" (46="que" GT — "que n de": 'n' attaches to neither side), @897 "14 98 83", @930 "82 98 83" (82="m" GT letter — "m n de": no), @1060 "09 98 83", @1783 "23 98 83". In every window the 'n' is stranded: the left group is a complete word or letter that cannot absorb a final 'n', and "nde" is not French. Kill grade. (98-82 x3 gives "n"+"m"="nm", dead on arrival the same way.)

**K1c — 62-98 x5 ("mann") dead on arrival.** Under both halves, "man"+"n"="mann" — not a French word; and both halves are independently dead above.

**On the near-miss that motivated the claim:** 62-94 x9 = "man"+"ne"="manne" is genuinely good French (une manne = wicker hamper; la manne = manna). That is the entire near-miss: one contact type parses, and the other two ("mane" x6, "mann" x5) do not. A global value must cover all 35/40 windows; the near-miss cannot.

**No rescue at battery level:** a conditioned/polyvalent reading (62="man" only at 62-94) would need a second polyvalence declaration, which is red-team's act under §7 (67 et/veut sole). The "62='il' dead" battery finding (@46 "pas 62 par") is consistent but not needed; this kill stands on banked values alone.

## Verdict: KILL (clause K1 fires; K2 not reached)

No follow-ups required by a kill verdict. The "mannequin" letter-family for 62/98 is closed.
