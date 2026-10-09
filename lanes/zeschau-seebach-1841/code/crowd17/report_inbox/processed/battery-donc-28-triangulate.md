# Battery verdict: donc-28-triangulate

Worker: 1f58bade-c270-4344-9d2f-af10629cf868. Date: 2026-10-09.
Lock: code/crowd17/next-token/locks/donc-28-triangulate.lock (created 2026-10-09T03:39:43Z; no prior lock).
Target id: donc-28-triangulate. Queue status at take: queued, priority 2, no verdict.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005, sealed gates, red-team adjudication queue untouched.
No data invented. @-offsets are 0-based stream indices.

## Bar (pre-registered verbatim from battery-queue.json, BEFORE testing)

"test 28='donc' at @286/@747/@1573/@1751 with @698's "ce donc" failure held as a separate contact question; kill 'donc' iff @698's 45 is 'ce'"

Numbered clauses:
1. 28='donc' parses at @286, @747, @1573, @1751 (the four non-"ce" windows).
2. @698's "ce donc" failure is held as a separate contact question (not re-litigated here).
3. Kill 'donc' iff @698's 45 is 'ce'.

## Method

1. Re-derived the full 1,847-pair / 96-type stream from repaired_offsets.json +
   data/upstream-ct_R5005.txt. 28 census: n=6 at @105/@286/@698/@747/@1573/@1751
   (byte-matches est-ce-104's census).
2. Re-derived 45's full distribution (n=22) and the 45-28 contacts (45-positions
   @104/@697, i.e. 28 at @105/@698).
3. Tested 28='donc' for 1841-French grammaticality at each of the four windows,
   with banked/promoted neighbor values substituted (00='pour', 64='qui',
   34='i' GT letter; 85 verb-stem A3 frame, 32 verb-class A1 frame as classes).
4. Adjudicated clause 3 against the standing A11 HOLD (45="ce", red-team
   confirmed round-15), checking for any window-specific byte evidence that
   45 is not 'ce' at @697.

## Window-level evidence

**@286 (a2_03):** "48 52 89 28 00 97 09 64" = "[48] [52] [89] donc pour [97]
[09] qui". "donc pour" = "therefore, in order to": donc as conjunction
between a clause and a purpose clause. Grammatical shape. PASS.

**@747 (a5_02):** "77 81 85 28 00 64 02 97" = "[le?] [81] [85] donc pour qui
[02] [97]". 85 carries the A3 verb-stem frame. "[verb] donc pour qui" =
"therefore for whom": donc post-verbal, "pour qui" purpose/beneficiary.
No contradiction. PASS.

**@1573 (a8_01):** "48 56 32 28 52 82 94 76" = "[48] [56] [32] donc [52] m
ne [76]". 32 carries the A1 predicative verb-class frame. "[verb] donc
[52]": post-verbal "donc" ("est donc...") is canonical French. PASS.

**@1751 (a8_08):** "65 34 07 28 89 26 24 85" = "[65] i [07] donc [89] [26]
[24] [85]". 34='i' is banked GT (letter), so "34 07" ends a word in 'i'.
"[word] donc [89]": donc as coordinating conjunction "X, therefore Y"
("il pleut, donc je reste"). Standard. PASS.

**@698 (a5_01, contact question):** "46 02 50 45 28 94 60 12" = "que [02]
[50] ce(HOLD) [28] ne(LEAD) [60] [12]". Under 28='donc': "ce donc ne" —
bare demonstrative "ce" + interposed "donc" before "ne" has no grammatical
function in 1841 French ("donc" licenses after "est"/"c'est"/imperatives,
never after bare "ce"). Rescues tested and rejected: clause-boundary
"donc ne [60]" (conjunction + "ne" with no subject — ungrammatical);
"donc" as interjection (needs imperative/est-ce host — absent);
28+94 one-word ("doncne" — no French word). The "ce donc" failure stands
as given by the bar and est-ce-104.

**45='ce' at @697 (clause 3):** Standing A11 HOLD (45="ce", red-team
confirmed round-15, "correctly unpromoted") treats 45 as 'ce'
provisionally; battery workers honor standing constraints. 45's
re-derived distribution supports the HOLD globally: 64 x3 ("ce qui" with
64='qui' GT), 46 x1 ("ce que" with 46='que' GT), 93 x3, 23 x3, 28 x2.
Window-specific check: the 50-45 bigram occurs x2 (@331/@696); @331
("00 92 50 45 54 88" = "pour [92] [50] ce [54] [88]") shows no
contradiction with 45='ce' in the same bigram. No byte-level evidence
anywhere in the stream forces 45 to be other than 'ce' at @697. The
contact question is therefore answered in the affirmative at battery
grade: 45 IS 'ce' at @698's contact.

## Per-clause pass/fail

1. **donc at the four windows: PASS.** All four parse with zero forced
   contradictions (@286/@747/@1573/@1751).
2. **@698 held as separate contact question: HONORED.** Not re-litigated
   as a naming question; used only for the kill clause.
3. **Kill iff @698's 45 is 'ce': FIRES.** A11 HOLD stands; no
   window-specific evidence against 45='ce' at @697; "ce donc ne" is
   ungrammatical. The bar's kill condition is met.

## Adverses answered

- "28 unknown": CONFIRMED — the kill removes 'donc' but names nothing;
  28 stays unknown. No battery has named 28.
- "@698's 45='ce' contact question open": ANSWERED — per the standing A11
  HOLD and the absence of any contrary byte evidence at @697, 45='ce'
  holds at this window at battery grade. The kill fires. (If the red team
  ever re-values 45 at @697, 'donc' has a clean revival path — see
  follow-up 1.)

## Verdict: KILL

28='donc' is killed at kill grade: @698 forces the claim false under the
standing A11 HOLD ("ce donc ne" ungrammatical). The triangulation is
informative in defeat — 'donc' was 5/6 clean across the 28 census
(@105 "est-ce donc pour que" also parses), and it dies on exactly one
contact whose resolution belongs to the 45 question, not the 28 question.
No standing verdict contradicted or downgraded.

## Follow-ups proposed (for supervisor queuing)

1. `ce28-contact` (P2): adjudicate the "45 28" bigram x2 (@104/@697) — is
   45='ce' at @697? If 45 is not 'ce' there, the @698 constraint on 28
   dissolves and 'donc' revives (5/6 clean). (Proposed by est-ce-104;
   not yet in queue — verified absent 2026-10-09.)
2. `x-pour-que-paradigm` (P3): census "X 00 46" trigrams stream-wide for
   the corpus-internal "pour que" paradigm; discriminates the remaining
   28 candidates (bien/aussi/encore/là) by distribution. (Proposed by
   est-ce-104; not yet in queue — verified absent 2026-10-09.)

## Bookkeeping

Report: code/crowd17/report_inbox/battery-donc-28-triangulate.md. Queue to
be updated via temp-file + rename (donc-28-triangulate: queued ->
verdict/kill; pre-write assert: no prior verdict). Lock to be deleted on
completion.
