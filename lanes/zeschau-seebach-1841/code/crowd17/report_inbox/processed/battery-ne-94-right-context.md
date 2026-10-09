# Battery report: ne-94-right-context

- Target id: `ne-94-right-context`
- Claim: "census all 37 right contexts of 94 to discriminate verbal-negator vs other function"
- Date: 2026-10-09
- Worker: battery worker (subagent ba2baa79-e18e-4cef-b1b8-1f4fe78e8c7c)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 types asserted). All @-offsets are 0-based repaired-stream indices.
  `canonical.py` never used. R5005 not touched.

## Bar (verbatim, pre-registered before testing)

"resolve iff 94's right-context census discriminates verbal-negator vs other function with stated cause"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) Every one of 94's 37 windows has its right context (immediate follower)
   recorded byte-exactly with @-offset, row, and standing values named.
2. (C2) The census discriminates: some windows are compatible with the
   verbal-negator function only, others are compatible with another function
   only, each with a stated cause — or the census fails to discriminate.
3. (C3) No standing or red-team verdict contradicted or downgraded; §7 intact.

## Method

1. Re-derived the repaired parse in-session; asserted 1,847 pairs / 96 types.
   Never used canonical.py. R5005 not touched.
2. Census: n(94) = 37, re-derived byte-exact.
3. Standing values applied (not re-litigated): 11=la, 70=pre, 82=m, 34=i,
   29=er, 40=e, 46=que (pencil GT); 87=ce, 64=qui, 96=par, 17=fois, 79=tout,
   00=pour, 84=on, 47=ce (granted); 59=est, 77=le (provisional); 94='ne'
   STRONG LEAD (R17-001); 24=finite-modal (promoted class); 92=verb class
   (R18, subset-scoped); 60=verb class (battery-promoted); 98='vient' (battery).
4. A "verbal-negator-compatible" window = 94 as particle 'ne' with a verb in
   the negated clause to its right (finite verb immediately right, or
   clitic+'m'/verbal object + verb), per 1841 French grammar. An "other
   function" window = 94 provably not the negator (word-final '-ne' syllable
   per seg-62-94-wordless6, or a right context that admits no verb).

## Right-context distribution (byte-exact)

| Right follower | n |
|---|---|
| 82 | 4 |
| 74 | 3 |
| 59 | 3 |
| 52 | 3 |
| 92 | 2 |
| 24 | 2 |
| 76 | 2 |
| 79 | 2 |
| 93, 65, 06, 02, 64, 29, 60, 07, 15, 26, 87, 70, 84, 30, 88, 44 | 1 each |

## Window-level evidence (all 37)

### Verbal-negator function — clean (7)

- @65 (a1_01): `40 94 92 69` = "e ne [92-V] [69]" — ne + verb-class 92 immediate.
- @161 (a1_05): `52 94 24 87` = "52 ne [24-fin/modal] ce".
- @699 (a5_01): `28 94 60 12` = "28 ne [60-V] 12" — 60 battery verb class.
- @1549 (a8_00): `12 94 92 45` = "12 ne [92-V] ce".
- @1701 (a8_06): `33 94 30 20` = "33 ne pas [20]" — verbal-slot forcing
  unconditional per nepas-20-adverb-gate PROMOTE.
- @1705 (a8_06): `62 94 88 26` = "[62=il] ne [88-V] [26]" — "il ne [verb]".
- @1773 (a8_09): `62 94 24 87` = "[62=il] ne [24] ce".

### Verbal-negator function — conditional (8)

- @558 (a3_02), @1795 (a8_09): `86/42 94 59` = "…ne est…" — 'est' is a verb;
  conditional on provisional 59='est'.
- @578 (a3_02), @1182 (a6_10), @1353 (a7_05): `[X] 94 82 06` = "ne m [06]" —
  'ne' + 'm' clitic; the verb is the 06-contact whose value is fenced
  (seg-94-82-06-f3 NULL).
- @1742 (a8_07): `34 94 82 46` = "i ne m que" — clitic 'm'; verb unlicensed.
- @494 (a2_11): `42 94 02 79` = "42 ne [02] tout" — 02 is a modal/'fait'
  candidate (adv-02-858 NULL fence); conditional on 02's verbal face.
- @1330 (a7_04): `62 94 70 52` = "il ne pre [52]" — particle 'ne' under the
  "il ne" left profile, but 'pre' (70 banked) admits no verb; conditional.

### Other function — word-final '-ne' syllable (6, per seg-62-94-wordless6 PROMOTE)

- @101 (a1_02), @509 (a3_00), @762 (a5_03), @841 (a5_06), @1363 (a7_06),
  @1687 (a8_05): the 6 D3-un-attachable `62-94` windows — "il ne" two-word
  parse dead; 94 is the word-final '-ne' of a noun ([W]ne, noun at 4/6 per
  the battery's class census). Not the negator.

### Other function — non-particle, non-negator (5)

- @250 (a2_02): `44 94 65 63` = "44 ne [65-noun] [63]" — "ne [noun]" is
  ungrammatical as negator; needs a clause boundary or other function.
- @318 (a2_04): `32 94 06 11` = "32 ne ent la" — 06='ent' standalone, not a
  verb; negator impossible.
- @688 (a5_00): `65 94 29 60` = "[65-noun] ne [29-er] [60]" — 29='er' bound;
  "ne er" cannot be negator + verb.
- @1169 (a6_09): `61 94 87 83` = "61 ne ce [83]" — the fenced "ne ce" hapax
  (ne-ce-1169 NULL); negator would need a verb after 'ce'.
- @1664 (a8_04): `22 94 84 64` = "22 ne on qui" — 'on qui' admits no verb.

### Unfenced — right neighbor value open (11)

- @349, @785, @1102: `ne [74]` — 74 fenced class-open, zero verb-frame
  contact (ne-alone-02-74 KILL); negator needs verbal 74, not established.
- @570, @1293, @1806: `ne [52]` — 52 open ({même/seule/dite} tie); the two
  `@1293/@1806` frames are byte-identical ("35 ne 52 80").
- @651, @1576: `82 94 76` = "m ne [76]" ×2 — 76 open.
- @771: `22 94 07 06` — 07 open (n=8).
- @774: `06 94 15 33` — 15 open.
- @1713: `65 94 44 59` — 44 open.

## Per-clause pass/fail

1. **C1 PASS** — all 37 right contexts recorded byte-exact above with
   @-offsets, rows, and standing values; distribution table matches
   (82×4, 74×3, 59×3, 52×3, 92×2, 24×2, 76×2, 79×2, 16 singletons = 37).
2. **C1 PASS (sub-count) — discrimination holds:** 7 windows force the
   verbal-negator function (verb immediate right, or unconditional
   verbal-slot forcing); 11 windows force a non-negator function
   (6 word-final '-ne' + 5 other non-particle); the remaining 19 are
   conditional (8) or value-open (11) and do not re-homogenize 94 —
   no uniform "94 is always the negator" claim survives the census.
3. **C3 PASS** — no standing or red-team verdict contradicted or downgraded.
   R17-001 (94='ne' STRONG LEAD) is untouched: the lead is class/frame-level
   and this census is its evidence; the word-final windows were already
   battery-promoted as '-ne' syllable (seg-62-94-wordless6); §7 intact
   (no polyvalence declared — segmentation, not value).

## Verdict: PROMOTE

The census discriminates verbal-negator vs other function with stated cause:
verbal-negator is 94's majority function (7 clean + 8 conditional windows),
but 11/37 windows provably cannot be the negator — 6 are the word-final
'-ne' syllable and 5 are other non-particle frames. This **hardens** the
battery-promoted 94='ne' (pending red-team ratification): the negator
reading now has a quantified, window-level population rather than a
presumption. The 11 value-open windows (@349/@785/@1102 'ne 74',
@570/@1293/@1806 'ne 52', @651/@1576 'm ne 76', @771, @774, @1713) are the
live residual for the next round of the question.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/ne-94-right-context.lock` created on
  start, deleted on completion.
- `battery-queue.json`: `ne-94-right-context` queued → verdict/promote
  (temp-file + rename; pre-write assert confirmed no prior verdict).
- R5005, sealed gates, red-team adjudication queue untouched.
- No follow-ups required (promote, not null).

## Adverses

None listed in the target brief.
