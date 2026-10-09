# Battery report: qui-2326-prefix

- Target id: `qui-2326-prefix` (priority 2)
- Claim: "name 24/87 in \"qui [23/26] 37\" frames"
- Date: 2026-10-08
- Worker: agent 8c9abf12-cf4a-43b3-8171-dfd78eae2874
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
  All @-offsets are repaired-stream 0-based pair indices (matches this
  target's evidence field; note the noun-26 battery used 1-based: its @1769
  = this report's @1768).

## Bar (verbatim, pre-registered before testing)

"parse the real 24-87-64-23/26-37 windows (@181, @1768) with 24 and 87 named;
test whether the frames stay verb-position after naming; coordinate with
noun-26"

Numbered pass/fail clauses (restated, not modified):

1. Parse the real 24-87-64-23/26-37 windows (@181, @1768) with 24 and 87 named.
2. Test whether the frames stay verb-position after naming.
3. Coordinate with noun-26.

## Method

1. Re-parsed the repaired stream (1,847 pairs; `canonical.py` never touched).
2. Verified the two target windows and censused all `24-87-64` trigrams (3)
   and all `64-[23|26]-37` windows (2) stream-wide.
3. Named 24 and 87 from decided battery evidence only (no new value claims):
   87=ce (granted, §7), 64=qui (granted, §7), 24=finite modal verb
   (class-level PROMOTE, battery-ne-24-profile, 2026-10-08; value open).
4. Checked consistency against noun26-encequi-triple (PROMOTE), noun-26
   umbrella (NULL), frame-37-reexam (NULL), and the §7 registry.

## Window-level evidence

Re-derived on the repaired stream, 0-based:

- @181 [a1_05]: `... 69 14 [24] [87] [64] [23] [37] 06 ...`
  (0-based pairs 179–183 = 24 87 64 23 37)
- @1768 [a8_08]: `... 84 09 [24] [87] [64] [26] [37] 78 ...`
  (0-based pairs 1766–1770 = 24 87 64 26 37)

Stream census: `24-87-64` occurs exactly 3x (@179, @1766, @1774);
`64-23-37` occurs 1x (@181); `64-26-37` occurs 1x (@1768).
The third trigram window @1774 [a8_09]: `62 94 [24] [87] [64] 59 19 48`.

Named parse (decided namings only):

- @181: `... 14 [24-modal]. ce(87) qui(64) [23] [37] ...`
- @1768: `... 09 [24-modal]. ce(87) qui(64) [26] [37] ...`
- @1774 (corroborating, out of bar scope): `62 94 [24-modal]. ce qui est(59)
  [19] [48]` — "ce qui est" is a clean French relative clause; the
  ne-24-profile battery already reads this window as "[62-subj] ne [24].
  Ce qui est [19]".

The "en ce qui" reading (24=en, preposition) is NOT available: the promoted
battery-ne-24-profile killed the preposition arm for 24 at kill grade (eight
windows ungrammatical with 24 as preposition, including @1774 "ne [24]").
The clause-boundary parse above is that battery's promoted account of the
24→87 contact (10/52, including @179 and @1766 — exactly our two windows).

## Per-clause pass/fail

1. Parse windows with 24 and 87 named: PASS. Both windows parse
   grammatically with 87=ce (granted), 64=qui (granted), and 24=finite
   modal verb (class PROMOTE; value open) followed by a clause boundary,
   then the relative clause "ce qui [23|26] [37]". 24's value is not
   named here — that belongs to a future value battery (ne-24-profile
   left "peut"/"sait"/"doit" open); class-level naming satisfies the bar.
2. Frames stay verb-position after naming: PASS. After naming, the frame is
   "qui [23|26] [37]" = relative pronoun + verb slot + post-verbal 37.
   A relative clause requires a finite verb after "qui", so the [23|26]
   slot is verb-position by construction. At @1768, 26=verb in this slot
   is decided (noun26-encequi-triple PROMOTE). At @181, 23 occupies the
   identical slot; the granted 23~26 split (A2) is respected (distinct
   values, parallel position) — 23 = "the other verb (value open)" per
   encequi-triple bar (d). 37 stays post-verbal predicative, consistent
   with the A1 predicative grant; no verb-shift of 37 occurs. The
   subject-reading rival ("qui [26-subject] [37-verb]") was already
   excluded at promote grade by encequi-triple bar (e) via 59='est'
   (provisional) in the identical slot at @1774.
3. Coordinate with noun-26: PASS. No re-litigation: noun-26's umbrella
   NULL (class unresolved) is untouched — this report makes no claim
   about 26's class unconditioned and relies only on decided legs
   (encequi-triple PROMOTE for the post-qui slot; noun26-pas-frames
   PROMOTE for the '26 30' frames). The "en ce qui" gloss inside
   encequi-triple's claim wording is superseded for 24 only (preposition
   arm killed by ne-24-profile); the promoted core — 26=verb in the
   post-qui slot — is untouched and consistent with the clause-boundary
   parse ("ce qui [26-verb] [37]"). No standing verdict is overwritten.

## Adverses

- "noun-26 class-unresolved": ANSWERED (fenced with stated cause). The
  umbrella class question is red-team adjudication territory (noun-26
  verdict NULL). This target's results are confined to the two formula
  windows and are compatible with either umbrella outcome; if the red
  team later rules 26=noun unconditioned, @1768's "ce qui [26] [37]"
  would need re-parsing (37 would have to take the verb slot, in tension
  with A1) — flagged as a downstream consequence, not decided here.
- "do not re-bar 'en ce qui' as written": ANSWERED. The killed 40-45-64
  form was never invoked; moreover the preposition reading of 24 is now
  killed at kill grade by the promoted ne-24-profile battery, so "en ce
  qui" cannot be re-barred in the 24-87-64 windows at all. The windows
  parse with a clause boundary instead.

## Verdict

**promote** — both windows parse with 24/87 named (24=finite modal verb,
class-level; 87=ce; 64=qui) and the "qui [23/26] 37" frames stay in
verb-position after naming (23/26 in the post-qui verb slot, 37
post-verbal predicative per A1). All listed adverses answered. §7
sole-polyvalence law respected; no new polyvalence declared. R5005,
sealed gates, and the red-team adjudication queue untouched. No standing
red-team verdict constrains 24's class or this formula; no escalation.
