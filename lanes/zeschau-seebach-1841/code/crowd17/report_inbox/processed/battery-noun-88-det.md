# Battery verdict: noun-88-det — name the noun at the determiner-governed windows

- Target: `noun-88-det` (priority 2)
- Claim: name the noun at the determiner-governed windows (@402, @1117)
- Worker: battery-worker noun-88-det (agent d94a5830-0482-4c09-9bab-9562a4af40e9)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, repair_parse.py tokenization). canonical.py never used. R5005 untouched. Sealed gates untouched. Red-team queue untouched. No invented numbers.
- Lock: created code/crowd17/next-token/locks/noun-88-det.lock on start (no pre-existing lock; nothing stale to note).
- Verdict: **NULL**

## 1. Bar (verbatim from battery-queue.json)

"name the noun value iff one noun parses both @402 ("ce [88]") and @1117 ("la [88]")"

Numbered clauses (pre-registered from the queue text BEFORE any window analysis; bar not modified after seeing data):

1. @402 parses as "ce" (45, granted A4) + [88 = masculine noun].
2. @1117 parses as "la" (11, pencil) + [88 = feminine noun].
3. ONE noun value satisfies both clauses (gender-compatible, grammatical in both windows).
4. The named noun is determined by the windows, not unconstrained speculation.

## 2. Method

Re-derived the full stream independently (1,847 pairs / 96 types verified). Extracted both windows ±10 pairs. Checked 88's full census (n=23, positions re-derived) for further determiner-governed instances: predecessors 45 x1 (@402) and 11 x1 (@1117) are the ONLY determiner-before-88 contacts; 39 x2 (@765, @1727) is the preposition "a", 69 x2 (@1260, @1267) is open. The bar's two windows are exhaustive for the determiner-governed frame. Tested candidate nouns against 1841 French gender/number government. Standing values used: banked pencil (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que), granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce, 45=ce A4), promoted letters (12=n, 48=e, 06=ent), provisional (59=est, 77=le). Battery-level items cited with status labels, never as standing.

## 3. Window-level evidence

**@402** — `73 34 67 64 79 82 48 06 11 45 88 53 34 69 26 00 33 01 02 53 84` (row a2_08).
@400=11, @401=45, @402=88, @403=53. Under standing values: "...[06-ent] la ce [88] [53]...".
"ce"+noun is clean French (parent battery battery-name-88-value.md H0 PASS, not re-litigated).
Noted: the literal left edge is "11 45" = "la ce", which is ungrammatical as two words;
the "ce [88]" reading requires 11 to belong leftward (clause boundary or prior word).
The contact is recorded, not resolved — it bounds but does not break the frame.

**@1117** — `63 00 66 73 41 65 38 30 69 11 88 70 12 06 14 06 11 52 37 43 00` (row a6_07).
@1114=30, @1115=69, @1116=11, @1117=88, @1118=70, @1119=12, @1120=06, @1121=14, @1122=06, @1123=11.
Three strains on the "la [88]" reading, all recorded:
(a) Segmentation contested: battery-promoted (pending round-18 red-team adjudication)
cela-69-11-word reads @1115-1116 "69 11" as one word "cela"; if it stands, 11 is
word-internal and the "la [88]" determiner frame dissolves.
(b) Number tension: "la [88-sg] ... [70-12-06]" — the 70-12-06 trigram is the 3pl
verb frame ("prennent" per battery breaker-b4-1121); singular article + plural verb
needs a clause-boundary or re-segmentation rescue, each ungranted.
(c) Spelling caveat: letter-spelling 70-12-06 = "pre"+"n"+"ent" = "prenent" (single n),
not "prennent"; the clerk-spelling question is owned by queued spell-single-consonant,
fenced here, not decided.

## 4. Per-clause pass/fail

1. @402 "ce [88]" noun frame: **PASS at class level** (parent battery's H0 PASS stands;
"ce"+masculine-noun clean; "la ce" left-edge contact noted as unresolved, non-breaking).
2. @1117 "la [88]" noun frame: **CONDITIONAL** — passes only if round-18 rejects the
"cela" segmentation AND the number tension is resolved with a granted rescue. Neither
is available at battery level.
3. One noun value for both windows: **FAIL** — structural gender clash. "ce" (45)
selects masculine (consonant-initial: "ce", not "cet"); "la" (11) selects feminine
singular. No regular French noun is both. Epicene nouns (identical m/f forms) exist
in principle, but no period-attested consonant-initial epicene is determined by these
windows — naming one (e.g. "ministre", "dentiste") would be invention, and in 1841
usage these were masculine-only, so even the rescue is ungranted.
4. Value determined by the windows: **FAIL** — the windows carry no semantic or
distributional hook for any specific noun; @402's follower (53) and @1117's context
underdetermine the value completely.

## 5. Adverses

None listed. Parent-battery context honored: the noun-class forcing at @402/@1117
(battery-name-88-value.md, KILL of one-value-ness) is NOT overturned — this battery
tests naming, not class. §7 sole-polyvalence rule respected: no value declared.

## 6. Verdict: NULL

The bar's iff-condition cannot be satisfied: no single noun value is both
gender-compatible with "ce" and "la" and determined by the windows. The failure is
epistemic (cannot name), not a falsification of 88=noun at these windows — the
parent battery's class-level forcing stands, so this is not a kill.

## 7. Recommended follow-up targets (for supervisor queueing)

F1. id: `ce88-leftedge-402` | priority: 2
claim: "resolve the @400-401 '11 45' ('la ce') contact at @402"
bars: "decide whether 11 belongs leftward (clause boundary / prior word), 11 is non-'la' here, or 45 is non-determiner; the 'ce [88]' frame stands or falls on the answer"
evidence: "this battery: @402 = '...06 11 45 88 53...' — 'la ce' ungrammatical as two words"
adverses: "45='ce' granted A4; 11='la' pencil"

F2. id: `cela-1117-frame` | priority: 2
claim: "adjudicate the effect of battery-promoted cela-69-11-word on @1117's determiner frame"
bars: "if '69 11'='cela' stands at @1115-1116, the 'la [88]' window dissolves and noun-88-det's bar is moot; if rejected, re-test clauses 2-4 above"
evidence: "this battery §3(b); battery-cela-69-11-word.md (promote, in round-18 adjudication)"
adverses: "do not re-litigate the 'cela' value itself — owned by round-18 red team; coordinate, do not duplicate"

F3. id: `noun-88-epicene` | priority: 3
claim: "constrained epicene-noun test for 88, gated on F1+F2 keeping both determiner frames alive"
bars: "name a period-attested (1841) consonant-initial epicene noun parsing both @402 and @1117 with distributional support beyond these two windows; kill iff none exists"
evidence: "this battery §4 clause 3 — gender clash is the structural blocker"
adverses: "§7 sole-polyvalence rule; no invented values"
