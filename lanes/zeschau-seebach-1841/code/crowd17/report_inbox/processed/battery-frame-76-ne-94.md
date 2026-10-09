# Battery report: frame-76-ne-94 — "ne [76]" x2 verb vs sub-word

- Target id: `frame-76-ne-94`
- Worker: subagent 8d9f8e50-4278-49ff-97a9-6f3a93321b99
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  canonical.py NOT used. R5005 NOT touched. All @-offsets are global pair
  indices on the repaired stream. No stale lock was present; lock created
  2026-10-09T08:28:06Z, deleted on completion.

## Sibling context (read first)

battery-frame-76-tension.md (null, 2026-10-09): 76's noun-vs-verb fork
stands. Verb-side: 94-76 x2 (@652, @1577) = "ne [76]" under 94="ne"
promoted. Noun-side: 77-76 x3 under 77="le" provisional. The 'la [76]'
bigram does not exist on the repaired stream. No class resolution; no
red-team declaration of a second polyvalence.

## Bar (verbatim, pre-registered)

> "resolve iff each 'ne [76]' window parses as verb-with-verb-locked-76 or is re-parsed sub-word with stated byte evidence; state what the '82 94' order anomaly means for the 'ne' reading"

### Numbered clauses

1. Each "ne [76]" window (@652, @1577) parses as "ne" + [76] where 76 is
   verb AND 76 is verb-locked — OR the window is re-parsed sub-word
   (i.e. not "ne"+[76] as separate morphemes) with stated byte evidence.
2. State what the "82 94" clitic-order anomaly means for the "ne" reading.

Reading of "verb-locked": 76 carries a standing verb lock (granted
verb-frame / verb-stem, or adjudicated verb class). Per §7 the granted
verb inventory is 80/89 verb-frames (A8) and 85 verb-stem (A3); 76 is
not in it, and frame-76-tension left 76's class open. No verb lock on
76 exists.

## Method

Re-parsed the repaired stream; censused all 37 windows of 94 ("ne"),
all 3 "82 94" bigrams, all 4 "94 82" bigrams, both 94-76 windows with
+-4 pair context, and ran a byte-level alignment test on the raw digit
string for "9476" / "829476" / "52829476" (pair-aligned vs raw hits).

## Window-level evidence (@-offsets on the repaired stream)

The two "ne [76]" windows, full +-4 context:

- @652 (a4_02): `52 82 94 76 49 24 26 30` — i.e. `...52 | 82 94 76 | 49 24 26 30`
- @1577 (a8_01): `52 82 94 76 47 98 24 53` — i.e. `...52 | 82 94 76 | 47 98 24 53`

Both windows share the identical 4-gram `52 82 94 76` ("82 94 76"
trigram x2 on stream, each preceded by 52).

94 ("ne") census, n=37:
- Predecessors: 62 x9, 12 x3, 42 x3, 82 x3, 61 x2, 65 x2, 22 x2, 78 x2,
  35 x2, singletons (52, 44, 32, 86, 45, 28).
- Successors: 82 x4, 74 x3, 59 x3 ("ne est" = "n'est" elision-shaped,
  under 59="est" provisional), 52 x3, 92 x2, 24 x2, 76 x2, 79 x2,
  singletons (93, 65, 06, 02, 64, 29, 60).
- 94 NEVER precedes a granted verb frame: 94-80 x0, 94-89 x0, 94-85 x0.

Clitic-order census (82="m" pencil, 94="ne" promoted):
- "82 94" (m ne — reversed) x3: @650 (->76), @1101 (->74, context
  `52 82 94 74 47`), @1575 (->76).
- "94 82" (ne m — grammatical order) x4: @578 (`94 82 06 06 50`),
  @1182 (`94 82 06 06 59`), @1353 (`94 82 06 52 37`), @1742
  (`94 82 46 56 40`).
- The "94 82 06" template x2 (@578, @1182) = "ne m' [ent-ent...]"
  under 06="ent" promoted: correct French clitic order before a
  verbal stem. The stream's own clean "ne me [verb]" template uses
  94-82 order, never 82-94.

Right context of 76 at the two windows:
- @652: `76 49 24 26` — this 4-gram occurs x2 on stream (@652, @989;
  @989 = `48 01 76 49 24 26`), i.e. formulaic right context.
- @1577: `76 47 98 24` — 47="ce" (A4) directly follows 76 ("ne [76] ce").

Byte evidence (raw digit string, repaired offsets):
- "9476": 2 raw hits, both pair-aligned (@652 a4_02 raw 16;
  @1577 a8_01 raw 46).
- "829476": 2 raw hits, both pair-aligned.
- "52829476": 2 raw hits, both pair-aligned.
- Zero unaligned hits: the digit stream offers no alternative
  segmentation at either window.

## Per-clause pass/fail

- Clause 1, disjunct A (verb-with-verb-locked-76): FAIL at both
  windows, on two independent grounds.
  1. No verb lock exists on 76 (§7 granted verb inventory: 80/89, 85;
     76's class open per frame-76-tension null). Reading 76 as verb
     at these two windows while it is noun-shaped at 77-76 x3 would
     be a battery-level second polyvalence, forbidden by §7
     (67 et/veut is the sole true polyvalence).
  2. The "82 94" order actively blocks the verb parse: "m ne [76]"
     is reversed French clitic order. The stream's own grammatical
     template for "ne me [verb]" is "94 82 06" x2 ("ne m'ent...",
     06="ent" promoted). A verb read of "82 94 76" would require
     "me ne [verb]", which is ungrammatical — the anomaly is not
     noise, it is a counterexample to the verb parse.
- Clause 1, disjunct B (sub-word re-parse with stated byte evidence):
  FAIL. The byte test is negative: every raw occurrence of
  "9476"/"829476"/"52829476" is exactly the two pair-aligned windows;
  no unaligned hit exists, so no alternative segmentation is
  evidenced. Within the pair stream, no fused-unit reading is grounded
  beyond the bigram itself (the shared "52 82 94 76" 4-gram is noted,
  not explained).
- Clause 2 (meaning of the "82 94" anomaly for the "ne" reading): PASS
  (informational). The anomaly does NOT threaten 94="ne" (promoted,
  left intact): "ne" behaves correctly in "94 82 06" x2 and in
  "62 94 59" ("[?] ne est" = "[?] n'est", @762). What the anomaly
  threatens is the PHRASE "ne [76]": at these windows "ne" sits in
  reversed clitic order ("m ne"), which is incompatible with a verbal
  "ne [76]" parse. The anomaly fences the verb read; it leaves
  "82 94 76" unexplained — consistent with 76 not being a verb here,
  or with a construction the battery cannot name at this level.

## Verdict: null

Rationale: inconclusive, not kill. Neither disjunct of clause 1
resolves: the verb read is blocked by the missing verb lock, the §7
polyvalence ban, and the reversed clitic order; the sub-word re-parse
has no stated byte evidence (byte test negative). No window forces the
claim false at kill grade — the windows remain genuinely ambiguous
("82 94 76" could still be a real construction with an unknown head
class). This contradicts no standing red-team verdict: 76 has no
adjudicated class, and 94="ne" (promoted) is left intact. The 76 class
fork stays open for red team.

Adverses: none listed. All numbers above trace to the repaired stream.

## Follow-ups (null mandates 1–3; nulls regenerate work)

1. frame-76-94-trigram — "82 94 76" x2 plus the third "82 94 74"
   window (@1101, `52 82 94 74 47`): discriminate whether "m ne [X]"
   with X in {76, 74} is a real construction. Census 74's full
   contact profile (n=34) against 76's; if 74 and 76 share class,
   the trigram is a frame with an unknown head class, not a verb
   phrase.
2. ne-94-right-context — census all 37 of 94's right contexts against
   the verb-head inventory (granted 80/89/85, promoted 06 "ent",
   provisional 59 "est"): 94 currently never precedes a granted verb
   frame (94-80/89/85 x0). Test whether "ne"'s right context ever
   resolves verb-shaped; discriminates verbal-negator vs other
   function for 94.
3. Red-team escalation: 76's noun-vs-verb class fork (frame-76-tension
   F3, still open) — the verb disjunct of this battery cannot be
   adjudicated until 76's class is locked or a second polyvalence is
   declared; battery may do neither per §7.
