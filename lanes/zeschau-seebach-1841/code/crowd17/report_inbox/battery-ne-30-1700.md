# Battery report: ne-30-1700 — 'n'importe' rival (30='importe') vs pas-30 at @1700

- Target: `ne-30-1700` (battery-queue.json, priority 2, status queued)
- Claim: 'n'importe' rival (30='importe') vs pas-30 at @1700
- Worker: 2182f0ce-f8db-4b56-8fe3-2792b629c951
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/ne-30-1700.lock` created on start, no stale lock present.

## Bar (verbatim, pre-registered)

"resolve iff @1700 parses under one of {30='pas', 30='importe'} with standing values; else fence"

Numbered clauses (frozen before testing):
1. @1700 parses under 30='pas' with standing values.
2. @1700 parses under 30='importe' with standing values.
3. Resolution: exactly one of clauses 1-2 passes cleanly -> resolve to that value; if neither passes -> fence @1700 with stated cause.

## Method

Extracted the @1700 window with full +/-3-group context from the repaired stream
and tested both rival values of 30 against standing values only: banked pencil
(11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que), promoted/granted
(87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce),
battery-promoted 94='ne' (pending red-team ratification — caveat inherited),
provisional 59='est', 67 et/veut sole polyvalence. NOT assumed: 33='dire'
(still queued/tied with croire per dire-33 / croire-33-tiebreak — both null),
85's value (A3 verb-stem frame grant only, value open), 20/62 values.
Census check: all 19 @30 windows scanned for 94-adjacency (elision test).

## Window-level evidence

+/-3-group window @1697-1703 (row a8_06):

| @ | pair | standing value / status |
|---|------|--------------------------|
| 1697 | 23 | open (23~26 SPLIT, A2) |
| 1698 | 91 | open |
| 1699 | 85 | verb-stem FRAME (A3 grant); value open — not named here |
| 1700 | 33 | infinitive-class (A10); dire/croire tied, NOT promoted |
| 1701 | 94 | 'ne' (battery-promoted, ratification pending) |
| 1702 | 30 | under test: 'pas' vs 'importe' |
| 1703 | 20 | open, noun-profile ("20 62 94" frame family) |

Wider right context @1703-1716: 20 62 94 88 26 12 06 29=er 40=e 65 94=ne 44 59=est 30 —
note @1713-1716 = 94-44-59-30, the pas-30 battery's clause-2 'ne...pas' frame
("ne [44] est pas"), which parses independently of this target.

Census: @1702 is the ONLY 94-30 adjacency among all 19 @30 windows in the
stream. Every other 30 sits in 'pas'-compatible slots (post-"ne ... [material]"
or standalone). So the "n'importe" word-reading is exclusive to this window —
a hapax word-formation, not a recurring frame.

**Clause-1 test (30='pas'):** window reads "85 [33-inf] ne pas 20".
French "ne pas" PRECEDES infinitives ("ne pas dire"); "ne + finite-verb + pas"
needs a finite verb. 33 is infinitive-class per A10 and the dire-33-set
battery (whole-windows parse as infinitive; no finite-33 evidence anywhere).
"....[inf] ne pas..." is categorically ungrammatical — the finder's
"'dire ne' order" objection stands even with 33 unpromoted (holds for croire
too). Clause-boundary rescue "....33. Ne pas [inf]..." requires @1703=20 to be
infinitival; 20's standing profile is noun-shaped ("20 62 94" frames, zero
infinitive legs) — fails. No parse under standing values. FAIL.

**Clause-2 test (30='importe'):** 94@1701='ne' + 30@1702='importe'
(vowel-initial) -> "n'importe" via n'-elision. The elision is licensed: the
ne-94 battery granted 'n\'' elision frames, and "n'importe" = "ne"+"importe"
is exactly that frame. Word-formation: PASS — and it is the stream's sole
94-30 adjacency, so the elision reading has no competing frame. Clause-level
parse: "[85]-[33-inf] n'importe [20]...". This stalls on open values: 85's
value is open (A3 frame only — 85 named solely as verb-stem frame per brief),
33 is tied dire/croire (unpromoted). Bare post-verbal "n'importe" (absolute
"no matter") is marginal literary French; with 20 as its complement it fails
20's profile; the 'contredire' compound vehicle (85='contre' + 33='dire',
flagged in croire-33-tiebreak) would need red-team-declared polyvalence for
85 per §7 and is NOT usable at battery level. So: coherent word, no clean
clause parse under standing values alone. CONDITIONAL — not a clean pass.

## Per-clause results

1. @1700 parses under 30='pas' with standing values: FAIL — "inf ne pas"
   word order ungrammatical; no clause-boundary rescue (20 not infinitival).
2. @1700 parses under 30='importe' with standing values: CONDITIONAL —
   "n'importe" word-formation licensed (n'-elision per ne-94 grant; sole
   94-30 adjacency in stream), but clause-level parse needs non-granted
   85/33 values; the 'contredire' vehicle needs red-team polyvalence.
3. Resolution: neither clause passes cleanly -> FENCE @1700 with stated
   cause (target adverse's instructed outcome).

## Adverses (answered, not ignored)

- **Reconcile with pas-30:** the pas-30 battery (promote, 2026-10-08)
  deliberately excluded @1701/1702 and fenced it to this target. This battery
  fences it back with cause: 30='pas' is ungrammatical at this window, and
  30='importe' is not demonstrated at clause level. The pas-30 verdict's
  re-open caveat ("if ne-30-1700 demonstrates 30='importe' here") is NOT
  triggered — 'importe' is demonstrated only at word-formation level, which
  does not meet the caveat's bar. pas-30 promotion stands; no downgrade.
- **No contradiction with any standing red-team verdict.** 94='ne' used with
  its ratification-pending caveat; 33 not promoted here; 85's value not named;
  67 sole-polyvalence respected (no new polyvalence declared).

## Verdict

**null** — @1700 FENCED: neither 30='pas' nor 30='importe' yields a clean
clause-level parse under standing values. 'pas' is excluded by word order;
'importe' survives only as a well-formed word ("n'importe", elision-licensed,
stream-unique 94-30 adjacency) awaiting 85's value and the 33 tiebreak.
Fencing is the bar's instructed outcome, not a failure to test.

## Follow-ups (null regenerates work; supervisor to queue)

1. `importe-30-elision-test` — vowel-initial value test for 30. Census all 19
   @30 windows for n'-elision consistency: @1702 is the sole 94-30 adjacency;
   test whether any other window forces 30 consonant-initial (killing the
   'importe' rival at word level) or admits a second "n'importe" frame.
   Bar: kill 30='importe' iff >=1 window forces consonant-initial 30;
   promote-consideration iff a second grammatical "n'importe" frame is found.
2. `stem-85-then-1700` — gated on stem-85 naming 85's value. Once named,
   re-test @1699-1702 as "[85]-[33] n'importe" vs "[85]-[33] ne pas": both
   current parses stall on open 85, so 85's value is the true discriminator.
   Bar: resolve @1700 iff the named 85 yields a grammatical clause under
   exactly one of the two 30 values.
3. `contredire-85-33-vehicle` — test the 85-33 'contredire' compound lead
   (flagged in croire-33-tiebreak, untested) as the vehicle for the
   "n'importe" parse. NOTE: if 85 must carry 'contre' as a second function,
   that is a second polyvalence and red-team territory per §7 — this battery
   may only gather the window evidence (85-33 contact profile, compound
   plausibility), not declare it.

(No existing verdict touched. Supervisor: ingest this report; do NOT edit
battery-queue.json — worker updates it per protocol §5.)
