# Battery report: seg-ceci-87-61

- Target id: `seg-ceci-87-61`
- Claim: compositional "ceci"=87+61 at @644, parallel to promoted "cela"=87+11
- Date: 2026-10-09
- Worker: battery worker (subagent 4cf97fb7-3ea6-48b9-948c-22bc6c8e1d4b)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; n=1847, 96 groups asserted
  in-session). `canonical.py` never used. R5005, sealed gates, red-team
  adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/seg-ceci-87-61.lock` (created at
  start, deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"demonstrate the composition at @644; weakness is the single occurrence;
must not disturb cela-87-11"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) The bigram 87-61 at @644 (0-based; 1-based @645) fuses to ONE
   French word "ceci" (87="ce" + 61="ci") under the lane's granted
   dissolution model.
2. (C2) The fused "ceci" occupies a licensed grammatical slot in the
   window, parallel to a granted "cela" leg.
3. (C3) The single occurrence is acknowledged (locus-level only); the
   granted cela-87-11 (n=7) is not disturbed and no global 61 value is
   claimed.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 types
   asserted). Never used `canonical.py`. R5005 not touched.
2. Byte-exact census: "87 61" occurs exactly 1x stream-wide, 0-based
   @644 (1-based @645), row a4_02 — pairs 0-1 of that row (row span
   @643..@667, 25 pairs), i.e. row-internal, at the row head.
3. Compared against the granted 87-11="cela" legs (n=7) and the
   locus-level 69-11="cela" promote (battery-cela-69-11-word).
4. Tested rival parses of the bigram against 61's contact profile
   (n(61)=18).

## Window-level evidence

@644 window (0-based), row a4_02 (pairs 0-1 = the bigram):

`... 63 74 46 60 67 77 89 48 20 24 | 87 61 | 88 77 78 52 82 94 76 49 24 26 30`

Reads with standing values: "...que(46) [60] [et/veut] le(77)
[89][48][20] [24-modal] **ceci** [88] le(77) ver(78) [52] m(82)
ne(94) [76] [49] [24] [26] pas(30)".

**E1 — the dissolution model is granted.** 87-11="cela" is granted at
n=7 (0-based @74, @163, @201, @461, @830, @1242, @1403); 47-11="cela"
granted; 69-11="cela" promoted locus-level (cela-69-11-word). Rationale
per cela-69-11-word E1: "ce"+"la" as two words is ungrammatical in
French, so the groups fuse. The identical rationale applies to
"ce"+"ci": no two-word "ce ci" exists in French, so 87="ce" (granted)
+ 61="ci" fuses to "ceci".

**E2 — 61="ci" has an independent parallel.** "17 61" @925
("65 71 17 61 96" = "[65] [71] fois [61] par"): "fois-ci" — the
postposed demonstrative particle -ci, the same French morpheme. No
61 window forces a conflicting value at this locus.

**E3 — the object slot is byte-identical to the granted "cela" leg.**
@830 (0-based): "...01 24 87 11 77..." = "[01] [24-modal] cela le(77)".
@644: "...20 24 87 61 88..." = "[20] [24-modal] ceci [88]". In both,
modal-24 takes the fused ce-demonstrative as direct object
("faire cela" / "faire ceci"), then a new constituent opens (77 /
88). 24=finite-modal is battery-promoted (ne-24-profile); the
"faire"-complement family is the standing frame.

**E4 — no rival parse is stateable.** (a) Determiner+noun:
"ce [61-noun]" needs 61 nominal — zero nominal legs in n(61)=18
(followers: 96 x2, 94 x2, 21, 31, 42, 48, 56, 12, 15, 59, 68, 83,
87, 88). (b) Word-internal "61 88": the 61-88 bigram is a hapax with
no compositional precedent anywhere in the stream. (c) No 61 value is
promoted lane-wide, so no cleaner rival exists on these frames.

**E5 — right edge fenced, not solved.** 88's exact role after "ceci"
is fenced: 88 is verb-class at battery grade but its finiteness is
open (queued `finiteness-88-86`). The composition demonstration does
not depend on it — the parallel @830 likewise leaves its right edge
(77) as a new constituent.

## Per-clause pass/fail

1. **C1 PASS.** 87-61 @644 fuses to "ceci": 87="ce" granted; "ce ci"
   two-word ungrammatical; dissolution precedented (E1); 61="ci"
   paralleled by "fois-ci" @925 (E2); no rival parse stateable (E4).
2. **C2 PASS.** "ceci" is the direct object of modal-24 ("faire ceci"),
   byte-parallel to granted "faire cela" @829-830 (E3); right edge
   fenced with cause (E5).
3. **C3 PASS.** Composition is locus-level only (@644 is the sole
   87-61 bigram stream-wide); no global 61 value claimed — 61's other
   17 windows untouched; cela-87-11 (n=7, granted) undisturbed.

## Adverses answered

- **Single occurrence:** acknowledged per the bar; graded as
  locus-level, exactly like the promoted cela-69-11-word.
- **cela-87-11 promoted — do not disturb:** untouched; the claim adds
  a fourth ce-compound locus (87-61) alongside the three established
  cela loci families, reusing their dissolution rationale.

## Caveats (stated, not hidden)

1. The object-slot license is conditional on 24=finite-modal
   (ne-24-profile, battery-promote). `24-en-verb-conflict` is a live
   red-team docket; under 24="en" the slot dies ("en ceci" is
   ungrammatical).
2. Canonicality: a4_02 offset 0 = upstream offset 0, unvalidated
   (68/70 upstream rows unvalidated); the bigram is row-internal.
3. Battery-grade only; needs red-team ratification before banked use.

## Verdict: PROMOTE (locus-level composition)

87-61 @644 reads **"ceci"** (one word; 87="ce" + 61="ci"). No global
61 value is named.

## Follow-ups

None required (promote, not null). Optional P4 if the supervisor
wants it: `ceci-1841-corpus` — corpus check that "faire ceci" is
attested in 1841 diplomatic French (strengthens E3 from
grammaticality to attestation).
