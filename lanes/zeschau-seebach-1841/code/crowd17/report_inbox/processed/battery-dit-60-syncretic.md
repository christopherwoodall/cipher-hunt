# Battery report: dit-60-syncretic

Worker: dit-60-syncretic subagent (session 46959c28-f6c8-44ab-ad8e-5818339f8d5d).
Date: 2026-10-09.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py
(re-implemented inline; n=1847 asserted, 96 groups asserted). canonical.py
never used. R5005, sealed gates, and the red-team adjudication queue untouched.
@i = 0-based pair index.
Lock: code/crowd17/next-token/locks/dit-60-syncretic.lock created at start
with agent id + UTC timestamp. No prior lockfile (no stale-lock note needed).
No red-team verdict on 60's value exists — no contradiction, no overwrite.
Coordinated with (did not duplicate) participle-60's V1/V2 and
npframe-60-454's findings; both cited, neither re-run.

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"test 60="dit" across the six windows; promote iff all parse with <=1 total
unstated assumption; kill iff any window forces otherwise"

Numbered clauses (fixed before data examination):

1. (C1) The stated value is 60="dit" (dire — past participle and 3sg present
   are syncretic: one surface form, one lexeme; monovalent if it holds).
2. (C2) PROMOTE iff all six windows (@454/@690/@1644/@1674/@1338/@700)
   parse grammatically in 1841 diplomatic French under 60="dit", with a
   TOTAL of <= 1 unstated assumption across all six parses. (Unstated
   assumption = any value, boundary, or re-segmentation not in the
   banked/granted/promoted/provisional set, per participle-60's C3.)
3. (C3) KILL iff any window forces otherwise — i.e. no grammatical parse
   exists under 60="dit" with standing values, and no available
   re-segmentation rescues it.
4. (C4) Adverses answered: @1644 hostile ("98 60" wants infinitive under
   98="vient") and @690 hostile ("ne er dit [03]" looks ungrammatical)
   tested, not assumed away; participle-60's V1 (present participle,
   killed at @1338 on class grounds) and V2 (finite -dre stem, killed at
   @700 by impossibility proof) cited, not re-run.

Standing values used: banked 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 47=ce (A4),
84=on (A15), 12=n, 48=e, 30=pas, 06=ent; provisional 59=est, 77=le;
94=ne STRONG LEAD (R17-001); 65=noun-class (prof-65); 98="vient"
battery-level (unratified).

## Method

Fresh parse per protocol; all six windows re-derived on the repaired
stream (verified byte-identical to the contexts in participle-60 and
npframe-60-454). 60="dit" tested as BOTH its syncretic forms at every
window (past participle and 3sg present of dire). 1841 diplomatic French
for all grammaticality judgments.

## Window-level evidence (re-derived on the repaired stream)

W1 — @454: `48 79 17 77 60 65 13 66 14`
"77 60 65" = "le[77] dit[60] [65-noun]" — "ledit [65]", past participle
used adjectivally, fully productive in 1841 diplomatic French ("ledit
traite", "ladite somme"; npframe-60-454 (c), Littré s.v. "dit"). PARSES.
Cost: the value hypothesis itself (1).

W2 — @690: `40 65 94 29 60 03 39 74 46`
Critical span "65 94 29 60 03" = "[65-noun] ne[94] er[29] dit[60] [03]".
- As past participle: "ne er dit" — "ne" cannot negate a bare participle;
  no auxiliary; "er" (banked pencil GT 29="er") is not a clitic. Dead.
- As 3sg present: "ne" + "er" + finite verb — "er" is not a pronoun or
  adverb; no French clause shape "ne er V". Dead.
- Re-segmentation audit (exhaustive): 94 leftward ("[65]ne er dit") leaves
  "er dit" = "erdit", not a French word. 94-29 fused ("nerdit") not a
  word. 29-60 boundary fixed by the group parse ("erdit" not a word).
  60-03 continuation ("dites"/"dit-il") cannot fix the "ne er" left edge.
  "redit" (re+dit) would need 29="re" — contradicts banked 29="er".
  "interdit"/"medit"/"credit" would need 94-29 to spell "inter"/"me"/"cre"
  — contradicts banked 29="er" and the 94="ne" strong lead.
  NO rescue exists under any 94 value: the failure is robust to 94's
  segmentation duality because banked "er" directly abuts 60.
  FAILS AT KILL GRADE — the window forces 60 != "dit".

W3 — @1644: `56 12 33 98 60 03 64 31 10`
"[33-INF] [98] dit[60] [03] qui[64]". Under battery-level 98="vient",
"vient dit" is ungrammatical (venir governs the infinitive: "vient
dire"; "dit" is not an infinitive; no compound-tense auxiliary).
As 3sg present, "[98-subj] dit [03-obj]" needs 98 nominal — 98's class
is open (1+ unstated assumptions). HOSTILE, not kill-grade (98's value
is unratified). Adverse @1644 answered as hostile, consistent with the
brief.

W4 — @1674: `78 55 81 92 60 03 39 74 77`
"[92] dit[60] [03]" — "[92] says [03]" parses iff 92 is nominal;
92's class is open (92 unresolved per lane state). No forced failure.
OPEN, neutral.

W5 — @1338: `83 86 71 64 60 08 65 64 52`
"qui[64] dit[60] [08] [65-noun] qui[64]" — "qui dit [08] [65]",
3sg present heading the relative clause. This is exactly the window
where participle-60's V1 died on class grounds ("qui" requires a finite
verb) — "dit" as 3sg present satisfies it. PARSES. Cost: 0 new
assumptions beyond the value hypothesis.

W6 — @700: `50 45 28 94 60 12 98 20 12`
"ce[45] [28] ne[94] dit[60] n[12] [98] [20]". "ne dit n'[98]":
"ne" + finite "dit" requires "pas" or a negation complement ("ne dit
mot"); "n'[98]" cannot complete it, and 12-98 re-segmentations
("n'[vowel]") still leave "ne dit" bare. 94-leftward ("[28]ne dit
n'[98]") leaves "dit n'" dead. The "ne...ni" rescue would need 98
i-initial plus a second "ni" — unevidenced. FAILS TO PARSE under
standing values; not ranked kill-grade only because 94's segmentation
duality and 98's open value are live elsewhere (cf. participle-60's
@700 caveat) — the kill is carried by W2, which has no such caveat.

## Per-clause pass/fail

- C1: PASS. Value stated: 60="dit", syncretic pp/3sg-present of dire.
- C2: FAIL. W1 and W5 parse within budget, but W2/W3/W6 do not parse at
  all under 60="dit"; W4 is open. Promotion impossible.
- C3: FIRES. W2 @690 forces 60 != "dit" at kill grade: "ne er dit [03]"
  admits no grammatical parse under standing values, and the failure is
  robust to every 94 re-segmentation because banked pencil GT 29="er"
  directly abuts 60 ("erdit"/"nerdit" are not French words; "redit"
  would contradict 29="er").
- C4: PASS. Adverses answered: @1644 hostile confirmed (not kill-grade,
  98 open); @690 hostile confirmed at kill grade; participle-60 V1/V2
  cited not re-run ("dit" as 3sg present is precisely what V1 lacked
  at @1338 — and it still dies at @690).

## Verdict

**KILL** — 60="dit" is forced false at @690. The irony is clean: "dit"
is the unique value that parses both @454 ("ledit [65]") and @1338
("qui dit"), the two windows that motivated it, but "ne er dit" at
@690 is ungrammatical under every available segmentation, with banked
29="er" as the immovable obstacle. One lexeme does not make 60
monovalent. The polyvalence question (participle-60, fed to
poly-60-redteam) is unaffected: this kill removes a candidate value,
not the question.

No standing verdict contradicted or downgraded (no red-team value
verdict on 60 exists).

## Suggested next targets (for supervisor triage)

1. `dit-60-690-rescue` (P3): the only anti-kill route is overturning
   banked 29="er" at @689 or the 94="ne" strong lead with byte-level
   evidence — state the bar as "produce the French word spanning
   @688-690 or kill the rescue". Expected outcome: kill.
2. `npframe-60-690` (P2, already proposed by npframe-60-454): mirror
   class adjudication at @690 — does ANY verbal 60 parse "94 29 60 03"
   within budget? Pairs with npframe-60-454 to map which NP frames
   admit verbal 60.

## Files

- Report: code/crowd17/report_inbox/battery-dit-60-syncretic.md (this file)
- Queue: battery-queue.json `dit-60-syncretic` → status `verdict`, result
  `kill` (own entry only, temp-file + rename; pre-write assert: no prior
  verdict existed; JSON re-validated after write)
- Lock: locks/dit-60-syncretic.lock created at start with agent id + UTC
  timestamp, deleted on completion
- R5005, sealed gate instances, and the red-team adjudication queue
  untouched throughout
