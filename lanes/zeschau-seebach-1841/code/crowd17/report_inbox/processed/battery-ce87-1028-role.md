# Battery report: ce87-1028-role

- Target id: `ce87-1028-role`
- Claim: "discriminate 87's new role at @1028 once the bare-'ce'-topic is dead."
- Date: 2026-10-09
- Worker: battery worker (subagent 0ee8073f-daa4-4f00-ae38-d5e9e1d2958d)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Re-derived in-session: 1,847 pairs, 96 types confirmed. canonical.py never
  used. R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/ce87-1028-role.lock (created at start,
  deleted on completion; no prior lock for this id existed).

## Bar (verbatim, pre-registered before testing)

"derive numbered bars from the claim before testing: (1) enumerate the
admissible roles for 87 at @1028 under standing values given the
bare-'ce'-topic kill; (2) adopt one iff it parses with zero new
assumptions and kills or fences all rivals; (3) else fence 87's role
at @1028 with the surviving candidates."

Numbered pass/fail clauses (restated before testing, not modified after):

1. The admissible roles for 87 at @1028 are enumerated exhaustively under
   standing values, with the bare-'ce'-topic kill honored.
2. One role is ADOPTED iff it parses with zero new assumptions AND every
   rival is killed or fenced with stated cause.
3. Otherwise 87's role at @1028 is FENCED with the surviving candidates
   ranked.

## Method

1. Read BATTERY-PROTOCOL.md first. Created/deleted the lock per protocol.
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types).
   Byte-verified the window: @1024-1040 = "45 64 96 43 87 01 03 29 80 77
   11 70 82 34 29 40 17" (row a6_03); @1028 = 87.
3. Adopted as premises (not re-litigated): ce87-topic-licensing KILL
   (bare-'ce' topic cannot head an exclamatory infinitive; A/B at @1029
   both dead), ci-bound-01 NULL (bound '-ci' in ce-contexts; @1029
   specifically fenced as a 03/80-driven residual, not promoted),
   ce01-slot-1029 NULL (01 'en'/'se' profile; clause-boundary C killed),
   ce-frame-45-64-96-43-87-01 NULL ("ce qui par [43] ce [01]" left edge,
   43's value open), poly-80-x29-frame PROMOTE ("03 29 80 77" =
   "[03]er [80]-le", imperative + enclitic 'le', "la première fois"
   byte-anchored), stem-03 conditioned split (verb stem only in
   "03 29 = [03]er" x3, @1030 one of the three), edge-1024-clause-boundary
   KILL (no boundary split in @1020-1029).
4. Ran a fresh corpus census in the lane's 1841-register period corpus
   (code/side-period/corpus/, the same 24.4M-character set used by
   ce87-topic-licensing) for the one construction that could license
   the surviving 87 role: dislocated tonic demonstrative + bare
   exclamatory infinitive ("ceci/cela, [inf]").

## Window-level evidence

### The window (byte-exact, repaired stream)

@1024-1042 (row a6_03):
`45 64 96 43 | 87 01 | 03 29 80 77 | 11 70 82 34 29 40 | 17 77 82 63 11`
= "ce(45) qui(64) par(96) [43] | ce(87) [01] | [03]er [80]-le(77) |
   la(11) pre(70) m(82) i(34) er(29) e(40) | fois(17) le(77) m(82)
   [63] la(11)"

### Clause 1 — admissible roles for 87 at @1028 (exhaustive)

Live candidates:

**(a) 87-01 = "ceci": 87 fuses with 01 as the tonic demonstrative,
topic of an exclamatory infinitive** — "Ceci, [03]er ! [80]-le, la
première fois !" The dissolution model is granted (cela = 87-11, n=7;
ceci = 87-61 promoted at @644); the specific 87-01 compound is
battery-NULL (ci-bound-01: clean pass only at @984, @1029 fenced as
residual). NOT touched by the bare-'ce' kill: "ceci" is tonic, and
the kill's grammar rule (clitics cannot dislocate) does not apply to
it.

**(b) Standalone "ce", stranded (residual).** Every standalone role
fails under standing values: dislocated topic killed
(ce87-topic-licensing); subject of a following verb — "ce" + infinitive
killed at kill grade (ce-inf-1841), and no finite verb is adjacent
(01 dead as verb; 03 is infinitive; 80 is 4 pairs away with "[01]
[03]er" intervening); "c'est" — no 59="est" adjacent; determiner —
no following noun; "par [43] ce" — "par" + bare demonstrative is
ungrammatical. Role-less, fenced.

**(c) Leftward attachment (43-87 compound).** No compositional
precedent for a 43-87 unit anywhere in the stream; 43's class is open
(prof-43-object running). Unevidenced, fenced.

Dead on arrival (killed, not merely fenced):

- Bare-'ce' topic (87 alone as dislocated topic): KILL per
  ce87-topic-licensing (zero attestations in 24.4M characters;
  atonic-clitic grammar rule). Honored, not re-litigated.
- 01 = 'en' / 'se' with any 87 role (A/B revived): both A and B
  required the bare-'ce' topic as their single shared load-bearing
  element; with it dead, no alternative 87 role makes "ce en [inf]"
  or "ce se [inf]" grammatical ("ce" + infinitive is kill-grade
  dead independently). Dead.
- "c'est ... que de" structure: requires 59="est" adjacent to 87;
  @1029 = 01. Dead at battery grade.
- Cleft "ce qui par [43] ce ...": "ce qui" (45 64) requires a
  following verb; "par [43]" intervenes and no verb follows
  (43 open, 87 = ce, 01 dead as verb). Dead at battery grade.
- Clause boundary at @1027|@1028 ("par [43]. Ce ..."): strands
  verbless "par [43]"; edge-1024-clause-boundary KILL rejected every
  boundary split in @1020-1029. Dead.

### Corpus census: demonstrative + bare exclamatory infinitive

Targeted search of the 24.4M-character 1841-register corpus:

- "ceci/cela, [bare infinitive]" (dislocated demonstrative +
  exclamatory infinitive): **0 attestations.** All comma-hits are
  false friends ("cela, cher ami" vocative; "outre cela, provoquer"
  prepositional; "cela, inspiré par" participle).
- Shape precedent: **"Moi, voler !"** (revue-deux-mondes-1841-q1,
  genuine: "— Moi, voler ! répond le bon Charlemagne") — dislocated
  TONIC topic + bare exclamatory infinitive, no clitic resume,
  attested in the 1841 register. Other "moi, [inf]" hits are false
  friends (parenthetical "moi" inside finite clauses).
- Tonic-demonstrative topic slot: cela/ceci/ça as fronted topics,
  335x (per ce87-topic-licensing, adopted).

So arm (a) combines two attested pieces — tonic demonstratives own
the dislocated-topic slot (335x), and dislocated tonic topic + bare
exclamatory infinitive is grammatical in the register (1x, "moi") —
but the specific demonstrative + bare-infinitive combination is
unattested. Genuine support, sub-promote-grade.

### Left-edge strain (recorded, not adjudicated)

"45 64 96 43" = "ce qui par [43]" needs a verb that never comes
under standing values ("ce qui" + parenthetical "par [43]" still
requires its verb after the parenthesis; candidates 43/87/01/03
are open / non-verbal / infinitive). edge-1024-clause-boundary's
KILL means no boundary rescues it. This is a clause-level strain on
ANY skeleton built on arm (a); it belongs to skeleton-1032-revise /
the F2 follow-up, not to 87's role discrimination. It does not
change the role ranking: 87's only role-giving reading is still (a).

### Word-internal "01-03" rival

residual-1029-infinitive's bar mentions a word-internal "01-03"
lead ("87 [01-03]er"). It conflicts with the battery-promoted
conditioned 03 split: @1030-1031 "03 29" is one of the three
"[03]er" verb-stem legs, so consuming 03 into a longer word
contradicts the split at battery grade. Fenced (red team owns the
split), not an admissible 87 role.

## Per-clause pass/fail

1. Admissible roles enumerated: **PASS.** (a) ceci-compound, (b)
   stranded-"ce", (c) leftward-attach; six dead readings killed
   with stated cause.
2. Adopt one role with zero new assumptions: **FAIL.** Arm (a) is
   the only role-giving reading, but it is load-bearing on
   battery-NULL 01 = '-ci' (ci-bound-01 did not promote; @1029
   specifically fenced as residual) — a non-granted assumption, so
   the "zero new assumptions" standard is not met. Arm (b) gives 87
   no grammatical role. Arm (c) is unevidenced. No adoption.
3. Fence with ranked candidates: **EXECUTED.**
   1. (a) 87-01 = "ceci", tonic demonstrative topic of the
      exclamatory-infinitive clause — LEADING. Only role-giving
      reading; dissolution model granted; register shape precedent
      ("Moi, voler !"); specific combination unattested (0x).
   2. (b) Standalone "ce", stranded residual — 87 role-less under
      all standing values; stands iff 01 resolves valueless at
      @1029.
   3. (c) Leftward 43-87 attachment — no precedent, lowest.

## Adverses

- None listed in the brief. Standing verdicts: none contradicted or
  downgraded. This battery builds on (does not re-litigate)
  ce87-topic-licensing's KILL, ci-bound-01's NULL,
  ce01-slot-1029's NULL, and poly-80-x29-frame's PROMOTE. §7 intact:
  no polyvalence declared (pronoun/determiner readings not invoked).

## Verdict: NULL (fence executed per clause 3)

87's role at @1028 is fenced, not named: the leading arm is the
"ceci" compound (87 + bound '-ci'), with stranded-"ce" as the
residual arm and leftward attachment unevidenced. Adoption is
blocked on the battery-NULL 01 = '-ci' premise and on the unattested
demonstrative + bare-infinitive combination.

## Follow-ups (nulls regenerate work; both verified absent from queue)

1. **disloc-demonstrative-inf** (P3): corpus test for dislocated
   demonstrative + bare exclamatory infinitive ("cela/ceci/ça,
   [inf]") in the wider 19th-century register, beyond the lane's
   1841 corpus. Baseline from this battery: 0 attestations in
   24.4M characters of 1841-register French; 1 shape precedent
   ("Moi, voler !", RDM 1841-q1); 335x tonic-demonstrative topic
   slot. Bar: >=1 genuine demonstrative attestation strengthens
   arm (a) to promote-grade; confirmed zero keeps it fenced.
   (Does not duplicate ceci-1841-corpus, which tests 'faire ceci'
   attestation — a different construction.)
2. **quice-verb-1024** (P3): find the verb for "ce qui" @1024-1025.
   Test "ce qui, par [43], [V]" with V in {43 iff verb-class
   (coordinate with running prof-43-object, do not duplicate),
   80, elided/finite elsewhere}. Bar: name the verb in a
   grammatical 1841-French parse, or fence "ce qui par [43]" as a
   verbless fragment — which independently strains any
   ceci-based skeleton of @1028-1040. (Does not duplicate
   residual-1029-infinitive, which covers @1029's infinitive, or
   the killed edge-1024-clause-boundary.)
