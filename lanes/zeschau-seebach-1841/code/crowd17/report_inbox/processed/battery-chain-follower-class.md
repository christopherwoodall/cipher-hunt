# Battery report: chain-follower-class

- Target: `chain-follower-class`
- Claim: "test whether the four chain followers (46=que, 47=ce, 48=e, 40=e) form one licensed complement class for a single head word"
- Date: 2026-10-09
- Worker: battery worker (subagent 3e7c6ed0-bacd-40d6-b740-3a5f11f3b383)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue
  untouched.
- Lock: `code/crowd17/next-token/locks/chain-follower-class.lock` (created at
  start, deleted at end; no prior lock existed).
- Evidence: `noun-74-formula` NULL (2026-10-09) follow-up #3.

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"state the single complement class with a French frame, or fence the
single-word '49 74 74' reading on heterogeneous government"

## Numbered pass/fail clauses (restated before testing, not modified after)

1. **C1 (license arm)** — there exists a French frame in which a single head
   word takes {que, ce, e, e} as one licensed complement class; state the
   class and the frame with byte evidence.
2. **C2 (fence arm)** — no such frame exists; the government is heterogeneous
   at kill grade; fence the single-word "49 74 74" reading with stated cause.

C1 and C2 are mutually exclusive. C1 PASS → the reading is licensed.
C2 PASS → the reading is fenced.

## Adopted premises (not re-litigated)

- `noun-74-formula` NULL (2026-10-09): the four '49 74 74' chains (W1–W4
  below); the '74 74' doubling (x6) kills whole-word nominal/verb heads at
  kill grade (`noun-74-census`); 49 and 74 are unvalued (§3 bars inventing
  values).
- Standing values (protocol §7): 46=que (GT, pencil); 47=ce (prom, A4
  allophone tier); 48=e (prom); 40=e (GT, pencil).

## The four chains (byte-exact, 0-based, re-derived in-session)

- W1 @416 (row a2_08): `51 37 78 [49 74 74] 46 49 36` — follower @419 = 46
- W2 @815 (row a5_05): `65 14 29 [49 74 74] 47 78 40` — follower @818 = 47
- W3 @860 (row a5_07): `84 02 24 [49 74 74] 48 47 46` — follower @863 = 48
- W4 @918 (row a5_09): `09 02 24 [49 74 74] 40 08 65` — follower @921 = 40

Follower values: 46="que", 47="ce", 48="e", 40="e".

## C1 test — is there a French frame?

The hypothesis under test: "49 74 74" is a single head word H, and
46/47/48/40 are its complements forming one class.

Grammatical categories of the four followers:

| Follower | Value | Category | Word-sized? |
|----------|-------|----------|-------------|
| 46 | "que" | subordinating conjunction / relative pronoun | yes (functional word) |
| 47 | "ce" | demonstrative pronoun | yes (nominal) |
| 48 | "e" | letter | **no (sub-lexical)** |
| 40 | "e" | letter | **no (sub-lexical)** |

A syntactic complement must be a constituent — word-sized or larger
(NP, pronoun, infinitive, clause, PP). A single letter "e" is sub-lexical;
it cannot occupy a complement position. "e" is not a French word, so it
cannot be a complement under any head.

Therefore 48 and 40 cannot be complements of H. The set {que, ce, e, e}
cannot form a "complement class" because two of its four members are not
complements at all.

Exhaustion of head classes (for completeness — all fail on the "e"
followers before any other consideration):

- **H = verb.** "V que" is licensed (verba dicendi + clause); "V ce" is
  marginal-but-possible (demonstrative object). "V e" is impossible —
  "e" is not a word. FAIL.
- **H = noun.** "N que" is licensed (relative clause). "N ce" is
  ungrammatical ("l'homme ce"). "N e" is impossible. FAIL.
- **H = adjective/adverb.** Same "e" impossibility; "ce"/"que"
  government also fails. FAIL.
- **H = functional head.** No functional head governs a bare letter. FAIL.

No French frame licenses a head taking a conjunction, a demonstrative
pronoun, and two bare letters as one complement class. The heterogeneity
is categorical (word vs. sub-lexical), not a matter of degree.

**C1: FAIL** — no frame exists; there is nothing to state.

## C2 test — heterogeneous government at kill grade

The heterogeneity is definitional, hence kill-grade:

1. 46 and 47 are word-sized functional items (conjunction/relative
   pronoun; demonstrative pronoun).
2. 48 and 40 are letters (values "e"; "e" is not a French word).
3. Complements are syntactic constituents; letters are sub-lexical.
4. A single head cannot have both word-sized complements and sub-lexical
   "complements" as one class — the latter are not complements.

Additionally, even among the word-sized followers, "que" (clause-linker)
and "ce" (nominal pronoun) belong to different government types; no
single French head governs both as the same complement class. But the
letter-tier objection alone is sufficient and dispositive.

Consequence: the single-word "49 74 74" reading — under which 46/47/48/40
would be the complements of one head word — is fenced. In W3/W4, the "e"
(48/40) must be word-internal (making "49 74 74" not a complete word
there) or the onset of a following word; either way, "49 74 74" is not a
single stable head word across the four chains.

**C2: PASS** — heterogeneous government demonstrated at kill grade.

## Verdict: KILL

C1 fails (no French frame; the "e" followers cannot be complements).
C2 fires (categorical word/sub-lexical heterogeneity). The single-word
"49 74 74" reading is fenced on heterogeneous government, per the bar.

## Scope

- Fences ONLY the single-word "49 74 74" reading insofar as it requires
  46/47/48/40 to be its complement class. Does not rule out "49 74 74"
  being a word with different government, nor the queued `unit-49-74-74`
  target (which may parse the "e" followers word-internally rather than
  as complements — a different hypothesis, not re-litigated here).
- Does not touch: `noun-74-formula` NULL, `noun-74-census` fence,
  `ne-alone-02-74` KILL, the '74 74' doubling family, 49's class-openness,
  or any standing/red-team verdict. §7 intact (67 et/veut remains the sole
  true polyvalence). Canonical-stream caveat stands (all four chains sit
  on offset-0 rows with unvalidated upstream offsets).

## Adverses answered

- None listed on the target.

## Follow-ups

None required (kill verdict). Note for the supervisor: the queued
`unit-49-74-74` target remains the live venue for any "49 74 74"-as-word
hypothesis; it must parse the W3/W4 "e" followers word-internally (or
explain them) to survive this fence.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-chain-follower-class.md`
  (this file).
- Queue: `battery-queue.json` — `chain-follower-class` status `queued` ->
  `verdict`, result `kill`, date 2026-10-09 (temp-file + rename; pre-write
  assert confirmed queued/verdictless; JSON re-validated post-write; only
  this entry's keys touched).
- Lock created at start, deleted at end (verified gone).
