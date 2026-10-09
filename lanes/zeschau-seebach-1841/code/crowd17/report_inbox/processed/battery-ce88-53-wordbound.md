# Battery report: ce88-53-wordbound

- Target id: `ce88-53-wordbound`
- Claim: "decide the '53 34' word boundary at @403-404"
- Date: 2026-10-09
- Worker: battery worker (subagent 2cb27956-97c4-414e-8d47-1f5a6a58096d)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 types asserted). All @-offsets are 0-based repaired-stream indices.
  `canonical.py` never used. R5005 not touched; sealed gates and red-team queue untouched.
- Lock: code/crowd17/next-token/locks/ce88-53-wordbound.lock (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"state the word boundary between 53 and 34 with byte evidence; complement 53-headed either way"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) State the word boundary between 53 and 34 with byte evidence —
   boundary present vs "53 34" as one word "[53]i".
2. (C2) The complement of 88 at @402–404 remains 53-headed under the stated
   boundary.

## Method

1. Re-derived the repaired parse in-session; asserted 1,847 pairs / 96 types.
2. Byte-confirmed the locus window and the full positional census of 34 (n=11)
   and of the "53 34" bigram (hapax, 1/1,847).
3. Adopted as premises (not re-litigated): 34='i' banked letter (§7 standing
   constraints); ce69-global PROMOTE (2026-10-09, battery grade: 69='ce' across
   all 12 windows, zero forced contradictions, "69 26" = "ce [26-noun]" clean
   determiner frame at @405–406); ce88-leftedge-402 PROMOTE (88 = verb-class
   governor at @402, 53-headed complement). 53's value is open
   (ce88-53-value is the separate naming venue) — this battery does not name it.

## Window-level evidence

**Locus (byte-confirmed):** @400–407 on row a2_08 =
`11 45 88 53 34 69 26 00` = "la ce [88-V] [53] [34='i'] [69='ce'] [26-noun] pour".

**E1 — "53 34" is a stream hapax.** The bigram occurs exactly 1× in 1,847
pairs, at @403–404. No distributional precedent for the contact itself.

**E2 — 34's positional profile (n=11, all re-derived byte-exact):**

| @ | window | 34's position |
|---|---|---|
| 61 (a1_01) | 08 34 29 40 | word-internal "-ier" (34-29 = 'i'+'er') |
| 757 (a5_03) | 82 34 29 40 | word-internal, "première" crib |
| 1037 (a6_03) | 82 34 29 40 | word-internal, "première" crib |
| 1741 (a8_07) | 12 34 94 | word-final: "ni" = 12-34, then 94='ne' |
| 28, 393, 404, 555, 1348, 1415, 1749 | various | open/fenced |

34 is word-internal or word-final at 4 of 11 windows (the three "-ier"
endings and the "ni" word-final). 34 NEVER stands alone as a word anywhere
in the stream — and it cannot: there is no standalone French word "i" in
1841 French.

**E3 — the boundary reading is kill-grade dead on both sub-readings.**
A word boundary between 53 and 34 would require 34 to be (a) a standalone
word "i" — no such French word exists (E2); or (b) word-initial of a word
continuing into 69: "34 69" = "i"+"ce" = "ice" — not a French word, and 69
is a standalone word "ce" at @405 ("69 26" = "ce [26-noun]" clean determiner
frame, ce69-global PROMOTE). Both sub-readings demand a non-French word.
The boundary is forced false on bytes.

**E4 — word-internal "53 34" = "[53]i" parses clean.**
"ce [88-V] [53]i ce [26-noun] pour" — 53-headed one-word complement + "ce"
determiner + noun. 34's word-final 'i' is directly parallel to the "ni"
(12-34) word-final at @1741 and to 34's word-internal life in the crib and
the "-ier" endings. The complement is 53-headed either way, per the bar.

## Per-clause pass/fail

1. **C1 PASS** — NO word boundary between 53 and 34. "53 34" @403–404 is one
   word "[53]i" with 34='i' word-final. The boundary reading is kill-grade
   dead (E3); the word-internal reading is byte-supported (E1, E2, E4).
2. **C2 PASS** — the complement of 88 remains 53-headed: "[53]i" is the
   53-headed post-verbal complement, followed by "ce [26]" (E4).

Adverses: none listed. No standing or red-team verdict contradicted or
downgraded; §7 intact (no polyvalence implicated — this is segmentation,
not value).

## Verdict: PROMOTE

"53 34" @403–404 is one word "[53]i"; no word boundary between 53 and 34.
The complement of 88 stays 53-headed. 53's exact value remains the venue of
ce88-53-value (not named here).

## Caveats (stated, not hidden)

- Canonicality: a2_08's upstream offsets are unvalidated; the locus is a
  canonical-offset object and dissolves under the row's rival phase.
- "[53]i"'s exact French form depends on 53's value (open); the "don" lead
  would give "doni" (not French), but 53's value is not adjudicated here.
- Battery grade only; needs red-team ratification before banked use.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-ce88-53-wordbound.md
- Queue: `battery-queue.json` → `ce88-53-wordbound` status `verdict`,
  result `promote`, date 2026-10-09 (pre-write assert passed —
  was `queued`/verdictless; temp-file + rename; JSON re-validated; only
  this entry touched).
- Lock created on start, deleted on completion (verified gone).
- No follow-ups required (promote, not null).
