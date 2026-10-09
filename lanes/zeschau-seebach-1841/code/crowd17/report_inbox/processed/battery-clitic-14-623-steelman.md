# Battery report: clitic-14-623-steelman — claim "W1 admits a full-window grammatical parse under 14='en' (clitic)"

- Target id: `clitic-14-623-steelman`
- Claim: "W1 (1-based @623) admits a full-window grammatical parse under 14='en' (clitic)."
- Date: 2026-10-09
- Worker: battery worker (subagent 352bd78c-9df6-45c1-87da-2c38498d3094)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Never used canonical.py. R5005 not touched. No invented data.
- Indexing: @i = 1-based pair index in the repaired stream (matches the
  brief's window convention; see Offset reconciliation).
- Lock: code/crowd17/next-token/locks/clitic-14-623-steelman.lock (created at
  start with agent id + UTC timestamp; deleted at end).

## Offset reconciliation (brief vs repaired stream)

- Repaired-stream convention (authoritative): 1-based pair index over the
  concatenated 1,847-pair stream. Row a4_01 = stream @619–643 (0-based 618–642).
- The brief's window @619–631 is stream-exact: stream @619–631 =
  `29 88 37 76 82 14 59 37 33 29 87 78 67` (13 pairs, row a4_01).
- The brief's W1 '@623' is off by one at this locus: stream @623 = `82`
  (the 'm'), while the brief's quoted 6-gram `76 82 14 59 37 33` sits
  byte-identical at stream @622–627 (unique in the stream; verified by scan).
  So: brief @623 = stream @622 for the `76`; the window @619–631 is unaffected.
- This battery tests the byte-identical window: the 6-gram at stream
  @622–627 inside the brief's @619–631 window. All @-offsets below are
  repaired-stream 1-based.

## Bar (verbatim, pre-registered before testing)

"Produce a complete grammatical parse of 1-based @619-631 (row a4_01) under 14='en' (clitic) with <=1 stated assumption, resolving the '37 33' continuation (boundary placement, 37 re-class, or 33 re-parse); else record the exact blocking adjacency."

Numbered pass/fail clauses (restated before testing, not modified after):

1. A complete grammatical parse of the 13-pair window @619–631 is produced,
   every pair assigned a grammatical role.
2. The parse is under 14='en' (clitic) and spends <=1 stated assumption
   (an assumption = any value outside pencil-GT / red-team-granted /
   provisional / battery-promoted standing).
3. The `37 33` continuation is resolved via boundary placement, 37 re-class,
   or 33 re-parse; ELSE the exact blocking adjacency is recorded.

## Method

1. Rebuilt the repaired parse in-session (1,847 pairs; verified count).
2. Located row a4_01 (stream @619–643) and extracted the brief's window
   @619–631: `29 88 37 76 82 14 59 37 33 29 87 78 67`.
3. Verified the 6-gram `76 82 14 59 37 33` is byte-identical and unique at
   stream @622–627; verified `82 14` occurs x2 (@623, @896).
4. Parsed the core @622–626 (`76 82 14 59 37`) under standing values.
5. Tested each of the three bar-sanctioned resolutions of the `37 33`
   continuation against standing grants and the <=1-assumption budget.
6. Scanned all 15 of 14's windows for any kill-grade contradiction of
   14='en'; censused the `37 33` bigram stream-wide.

Standing values used: pencil 82=m, 29=er, 46=que, 11=la, 40=e;
granted 87=ce, 37/32/42 predicative frames (A1), 33 INF-class (A9/A14),
67=et/veut sole polyvalence; provisional 59=est; battery-promoted 76=noun
(2026-10-08), 94=ne, 48=e(letter). 78='ver' used only as unpromoted LEAD
(R16-005); never banked.

## Window-level evidence

Window @619–631 (row a4_01), repaired-stream 1-based:

| @ | pair | standing value | role in attempted parse |
|---|------|----------------|-------------------------|
| 619 | 29 | 'er' (pencil) | tail of preceding -er word (row opens here; a4_00 ends @618='10') |
| 620 | 88 | OPEN (n=23) | BLOCKER — no granted frame; see below |
| 621 | 37 | predicative (A1) | predicative |
| 622 | 76 | noun (battery-promoted) | subject noun, `le/la [76]` |
| 623 | 82 | 'm' (pencil letter) | `m'` proclitic |
| 624 | 14 | 'en' (claim hypothesis) | clitic `en` → `m'en` |
| 625 | 59 | 'est' (provisional) | copula |
| 626 | 37 | predicative (A1) | predicative complement |
| 627 | 33 | INF class (A9/A14) | BLOCKER — see `37 33` analysis |
| 628 | 29 | 'er' (pencil) | infinitive ending (stem-reading) or orphan (whole-reading) |
| 629 | 87 | 'ce' (promoted) | object `ce` |
| 630 | 78 | 'ver' LEAD (R16-005, unpromoted) | open word-continuation |
| 631 | 67 | et/veut (sole polyvalence) | `et` (follower 08 open; `veut` undecidable) |

### The core parses (clause-level PASS, window-level insufficient)

@622–626: `[76-noun] m'en est [37-predicative]` — literary-grammatical on the
`il m'en est resté / garant` pattern with a lexical noun subject
(cf. "le souvenir m'en est resté"). Letter-strictness holds: 82='m' is a
banked letter and 'me' would require 82+48 ('e'), so `82 14` reads `m'` +
vowel-initial clitic only; `m'en est` is the surviving reading (`m'y est`
dies per the brief's 'être'-takes-no-'y' argument, not re-litigated).
Assumptions spent on the core: ZERO (76=noun battery-promoted 2026-10-08;
59='est' provisional standing; 37 A1-granted; 14='en' is the hypothesis).

Corroboration that 14='en' is viable (claim not falsified):
- Second `82 14` ("m'en"-shaped) leg at @896–897 (`01 98 82 14 98 83 86`).
- `79 14` x2 (@1366, @1690: `62 94 79 14 60 …`) reads as `tout en [60]`,
  the gerundive "tout en + [participle]" construction — a natural 'en' frame.
- 15-window scan of 14: no window forces 14≠'en' at kill grade.

### The three resolutions of `37 33` (@626–627) — all blocked

The `37 33` bigram is a stream-wide HAPAX (1/1847 windows) — no
distributional rescue is available; the adjacency must be resolved or
recorded at this window alone.

(a) Boundary placement: `…m'en est [37-pred]. [33-stem]er ce [78] [67]…`
would need 33 stem-read (A10 HOLD permits) + X named (the -er stem;
erstem-33-id went null 2026-10-08, X unidentified) + 78='ver' (LEAD,
ungranted) + 67 disambiguated (follower 08 open; stem-08 queued) + 88
resolved at the left edge. That is ≥3 ungranted assumptions (88, X, 78)
against a budget of 1. The brief's own adverse ("`[33]er ce [78-ver]`
unparseable") is X-dependent, not refuted, but it cannot be *demonstrated*
grammatical either: no exhibitable instance. BLOCKED on assumption budget.

(b) 37 re-class at @626: contradicts the red-team A1 grant (59→37
predicative frames). Battery level cannot re-class; route is red-team-gated.
(frame-37-reexam already escalated the whole 37 verb/adj question to the red
team, null 2026-10-08 — this battery does not re-decide it.)

(c) 33 re-parse (non-infinitive): contradicts granted INF-class standing
(A9 class-level, A14 set-level strong INF-signal, A10 stem/whole HOLD).
Battery level cannot re-parse; escalate, not decide. Grammar independently
fails: `est [37-pred] [33-noun]` needs a determiner or bare-noun license
("*est resté souvenir" is ungrammatical).

### Left edge @619–621

`29 88 37`: 29='er' tails a preceding word (row-initial; a4_00 ends '10'
@618, so `[10]er`-or-boundary is upstream of the bar's window and fenced as
row-boundary continuation). 88 is OPEN (n=23, no granted frame found in this
battery's scope) — `[88] [37-pred]` cannot be role-assigned without spending
an assumption. This alone defeats clause 1's "complete" requirement.

## Per-clause pass/fail

1. Complete grammatical parse of @619–631: **FAIL** — left edge blocked at
   88 (open value); right edge blocked at the `37 33` hapax adjacency plus
   open X (33-stem) and open 78.
2. <=1 stated assumption: **FAIL** (as applied to the whole window) — the
   core needs 0, but completing the window needs ≥3 (88's class, X the
   33-stem, 78's value). No single assumption completes it.
3. `37 33` resolution: routes (a)/(b)/(c) all blocked within battery
   authority and budget (a: assumption budget; b/c: red-team-gated grants).
   **Else-clause SATISFIED** — exact blocking adjacency recorded below.

## Verdict: null

The claim is NOT falsified: the W1 core `[76] m'en est [37]` parses cleanly
under 14='en' with zero new assumptions, `82 14` has a second "m'en" leg
(@896), and `79 14` x2 fits the gerundive "tout en" frame. But the bar's
full-window parse cannot be completed within battery authority and the
<=1-assumption budget. No standing red-team verdict is contradicted
(78='ver' used as LEAD only; 37's re-class question left with the red team
per frame-37-reexam; 33's INF class untouched).

**Exact blocking adjacency (bar else-clause): stream 1-based @626–627,
`37 33` — A1-predicative immediately followed by bare INF-class 33, a
stream-wide hapax with no grammatical continuation under standing values
and <=1 assumption. Secondary blockers: @620 `88` (open value, left edge),
@627's stem X unidentified (erstem-33-id null), @630 `78` unpromoted LEAD.**

## Follow-up targets (null regenerates work)

1. `x-33-626-identity` (priority 2): decide same-X vs two-X for the two
   byte-identical `33-29-87` windows via left-context class comparison
   (@626's pre=37 vs the other's pre). Narrower than erstem-33-id (global);
   unblocks the boundary route at @627. Bar: same-X demonstrated iff both
   windows' stems share valency class with <=10% orphan, else two-X recorded.
2. `prof-88` (priority 3): name 88's class (n=23) with >=2 frame-legs;
   unblocks W1's left edge (`29 88 37` @619–621). Bar: class assigned iff
   >=2 independent frames parse under one class with zero hard
   contradictions; else fence as residual.
3. `core-14-622-bank` (priority 2): narrower bar — bank the @622–626 core
   (`[76-noun] m'en est [37-pred]`) as a confirmed 'en'-clitic frame for
   14, fencing the @626–627 `37 33` hapax as a red-team residual joint with
   frame-37-reexam. Bar: promote iff core parses with zero new assumptions
   AND >=1 independent 'en'-frame corroborates (the @896 `82 14` leg or the
   `79 14` gerundive x2).

## Standing-constraint compliance (§7)

- Used only pencil GT, grants, provisionals, and battery-promoted values;
  78='ver' kept at LEAD, never banked.
- Did not touch R5005, sealed gates, or the red-team adjudication queue.
- 59='est' used as provisional (flagged conditional per the brief's adverse;
  if it falls, W1 needs re-audit — adverse carried forward, not resolved).
- No verdict downgraded (target was `queued`).
