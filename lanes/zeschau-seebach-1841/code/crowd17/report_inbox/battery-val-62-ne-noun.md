# Battery verdict: val-62-ne-noun

**Verdict: NULL** — domaine is eliminated (kill-grade at C1), but "règne" vs
"trône" is a genuine tie: the two are grammatically identical in every test
frame, so no unique value can be named at battery grade. Surviving set:
{règne, trône}.

## Bar (verbatim, pre-registered)

> 62-06 parse test ("regnent"/"tronent" vs *"domaient"); six 62-48 windows

Restated as numbered clauses (before testing):

- **C1**: At the two 62-06 windows, "62 06" parses as a French word iff
  62 is "règn-" or "trôn-" ("règnent"/"trônent" are real 3pl verbs);
  *"domaient" is not French, so domaine is eliminated.
- **C2**: The six 62-48 windows are compatible with 62 = "règn-"/"trôn-"
  (no forced contradiction under the -ne-final nominal stem).

Claim (from queue): discriminate "regne"/"trone"/"domaine" for 62 via 62-06
windows and six 62-48 windows; then re-test the @508 head.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/val-62-ne-noun.lock` on start
(agent id + UTC timestamp). Re-derived the repaired stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed per `repair_parse.py`): 1,847 pairs / 96 types verified.
`canonical.py` never touched. R5005, sealed gates, red-team adjudication
queue untouched.

All @-offsets below are 0-based pair indices (queue convention).

Standing values used as premises (never re-litigated): 11=la, 29=er, 40=e,
46=que, 64=qui, 34=i (banked); 87=ce, 96=par, 17=fois, 47=ce (A4 allophone),
00=pour (A9 leg-1 class-level), 84=on (A15) (promoted/granted); 77=le
(provisional); 94=ne letter-tier (R17-003); 48=e letter-tier (R17-003),
feminine/inflectional -e function (fem-e-48 PROMOTE); 06=ent letters-tier
with the ent-06-host-census decision rule (06 is a finite "-ent" 3pl ending
iff its left neighbor is a verb stem; otherwise 06 is a syllable);
ne-drop is lane precedent (w2-pas-nelicense PROMOTE).

Prior 62 state adopted: 62='il' kill-grade dead globally; sel-62-48-94 KILL
(no uniform value); class-62-fullcensus NULL (no single class parses all 35
windows; conditioned split is red-team §7 territory); syll-94-508-verify
PROMOTE (conditional): at @508, particle-94 is kill-grade dead and "62 94"
composes leftward as "[62]ne", word-final 'ne' syllable — conditional on
provisional 77="le".

## C1: the 62-06 parse test

62 takes 06 as its follower at exactly two windows (matches the
class-62-fullcensus follower census "06 x2"):

**Window A — 0-based @665-666** (row a4_02):
`... 86 50 80 03 [62] [06] 00 20 67 11 86 24 80 03 64 ...`
Left of 62 is 03; right of 06 is 00='pour' (a whole word).

**Window B — 0-based @1536-1537** (row a8_00):
`... 00 66 73 41 [62] [06] 21 62 93 88 77 78 43 00 46 ...`
Left of 62 is 41; right of 06 is 21 (noun-class, word-level per the
table registry — 21 takes postposed adjective 60 in "21 60" frames).

Attachment logic (applies at both windows):
- 06 cannot stand alone: "ent" is not a French word.
- 06 cannot attach rightward: at A the right neighbor is 00='pour'
  (a whole word); at B the right neighbor is 21 (word-level noun).
  06 composing rightward into either is impossible.
- Therefore 06 MUST attach leftward to 62, forming one morphological
  word "[62]ent".

Lexical test of "[62]ent" under each candidate (62 carries "n"+"e"
per "[62]ne" @508 and "[62]e" at the 62-48 windows):
- 62 = "règn-": "règnent" — 3pl present of "régner". Real French word. PASS.
- 62 = "trôn-": "trônent" — 3pl present of "trôner" (Littré-attested).
  Real French word. PASS.
- 62 = "domain-": *"domaient" — no verb "domaier"/"domainer" exists in
  French ("dominer" gives "dominent", a different stem). Not a French
  word. FAIL at kill grade.

Window B is the clean kill: no prefix candidate precedes 62 there
(left is 41), so "[62]ent" is forced and *"domaient" is impossible.
Domaine is eliminated as a global value.

Caveat at Window A: the queued target re-prefix-03-665 tests the
one-stem "re-[62]ent" reading (03 as prefixal "re-"). If 03 is prefixal,
"62 06" at A is not "[62]ent" alone. This does not rescue domaine:
Window B kills it independently. The re-prefix hypothesis is not
duplicated here; it is noted as a live alternative for Window A only.

Per the ent-06-host-census decision rule, 06 as a finite "-ent" ending
requires 62 to be a verb stem at these windows. Under "règn-"/"trôn-"
this is satisfiable (both are verb stems: "régner"/"trôner"). This
forces a VERB-STEM function for 62 at @665/@1536 — compatible with the
nominal claim because "règne"/"trône" are noun/verb homographs sharing
one stem (same pattern as 32: one lexeme with nominal uses, R17-008).
The noun/verb scope mapping is proposed as a follow-up; no §7
polyvalence is declared at battery level.

**C1: PASS** — the parse test discriminates as written: {règne, trône}
survive, domaine is kill-grade eliminated.

## C2: the six 62-48 windows

62 takes 48 as its follower at exactly six windows (matches the
class-62-fullcensus follower census "48 x6"). 48='e' (letter-tier),
so "62 48" = "[62]e" = "règne"/"trône" (word-final -e):

1. **@360** (a2_06): `... 47 11 21 [62] 48 76 47 78 48 ...`
   = "ce la [21-N] [62]e [76-N] ce [78]e". "[21] [62]e": as noun,
   N-N apposition (strained); as 3sg verb, "la [21] règne/trône"
   (subject+verb, clean) with "[76]" needing a new-clause role
   ("régner"/"trôner" are intransitive). STRAINED, no forced
   contradiction. (The "47 11" = "ce la" contact is an independent
   problem, not charged to 62.)
2. **@425** (a2_09): `... 36 29 47 14 [62] 48 76 42 ...`
   = "[36?]er ce [14] [62]e [76]". If 14='le' (determiner; surviving
   'le'-legs at @72/@117/@178 stand), "le [62]e" = "le règne"/"le trône"
   — a clean nominal. COMPATIBLE, nominal-supporting.
3. **@1315** (a7_04): `... 44 00 36 74 [62] 48 98 15 ...`
   = "[44] pour [36] [74] [62]e [98-fin]". [62]e CANNOT be a finite verb
   here ("[règne] [98]" would be V-V, ungrammatical), so [62]e is
   non-finite: noun "règne"/"trône" fits ("[74?] [subject-N] [98-verb]"
   frame). COMPATIBLE, and forces the non-verbal reading here —
   supports the nominal claim.
4. **@1349** (a7_05): `... 86 66 73 34 [62] 48 77 78 94 ...`
   = "[86] [66] [73] i[34] [62]e le[77] [78] ne[94]". "i [62]e" with
   34='i' as "y" (adverbial pronoun): "y règne/trône" (3sg verb,
   "reigns there") is grammatical; then "le [78]" is strained
   (intransitive verb + determiner). STRAINED, no forced contradiction.
5. **@1464** (a7_09): `... 79 17 01 21 [62] 48 21 02 62 38 ...`
   = "tout fois [01] [21-N] [62]e [21-N]". N-[62]e-N: as noun,
   apposition (strained); as 3sg verb, "[21] règne/trône [21]"
   with the second [21] needing a new clause (intransitive).
   STRAINED, no forced contradiction.
6. **@1569** (a8_01): `... 50 29 24 74 [62] 48 56 32 28 ...`
   = "[50] er [24] [74] [62]e [56] [32-verb-lexeme]". Neighbors open
   (74, 56 both value-open). No forced contradiction under
   "règne"/"trône" as noun or verb-stem. OPEN/COMPATIBLE.

No window forces "62 ≠ règne" or "62 ≠ trône". The two best windows
for the nominal claim are @425 ("le [62]e", conditional on 14='le')
and @1315 ([62]e forced non-verbal before finite 98).

**C2: PASS** — all six windows are compatible with 62 = "règn-"/"trôn-";
none forces a contradiction. (Compatibility, not confirmation: most
windows are strained and several neighbors are value-open.)

## @508 head re-test (claim's second step)

0-based @507-511 (row a3_00): `77 [62] 94 64 98 65`
= "le[77] [62] ne[94] qui[64] [98] [65]".
Under "règne": "le règne qui [98] [65]" — grammatical.
Under "trône": "le trône qui [98] [65]" — grammatical.
No discrimination (agrees with head-77-62-94-noun NULL). The
syll-94-508-verify conditional promote ("[62]ne" word-final) stands
unchanged; 62's lexical value stays open between the two survivors.

## Why the verdict is NULL and not PROMOTE or KILL

- Not PROMOTE: C1+C2 narrow the field to {règne, trône}, but the two
  are grammatically identical in every test frame (both masculine
  nouns, both -er verb stems with identical conjugations:
  "règne"/"trône", "règnent"/"trônent"). No battery-grade discriminator
  exists between them. Naming one would be a guess, not a finding.
- Not KILL: no bar clause fails at kill grade. C1 eliminates domaine
  (a candidate, not the claim). C2 finds no forced contradiction with
  the -ne-final nominal stem hypothesis. No cleaner rival value is
  demonstrated on these frames (the "re-[62]ent"/"reprennent" shape at
  Window A belongs to the queued re-prefix-03-665 target and is not
  decided here).

## Follow-ups proposed (for supervisor queuing)

1. `regne-trone-tiebreak` (P3) — Break the "règne"/"trône" tie. The two
   are grammatically identical, so this needs either (a) 1841 diplomatic
   French corpus collocational data for the attested frames ("le [62]ne
   qui", "[62]e [76]", "[62]ent"), or (b) a landed neighbor value
   (76, 98, 65, 93, 21) creating selectional pressure that admits one
   but not the other. Bar: produce a frame where "règne" and "trône"
   make different grammaticality/collocation predictions, or fence as
   lexically tied pending neighbor resolution.
2. `scope-62-verb-noun` (P3) — Map 62's verb-stem vs nominal windows
   under the surviving {règn-, trôn-} stem. C1 forces verb-stem at
   @665/@1536 (06 as finite "-ent" per the 06 decision rule); C2's
   @1315 forces non-verbal; @425 supports nominal ("le [62]e").
   Bar: classify all 35 windows as stem-verbal vs nominal; if the
   alternation cannot be carried by one lexeme, package the §7
   split candidacy for the red team (battery declares no polyvalence).
3. `domaine-kill-harden` (P4) — Harden C1's *"domaient" elimination with
   a dictionary check (Littré): confirm no verb "domaier"/"domainer" is
   attested in 19th-c. French. Bar: dictionary confirms the gap
   (kill stands), or attestation revives domaine.

## Adverses

None listed in the queue entry. Notes: the re-prefix-03-665 interaction
at Window A is fenced with stated cause above (Window B kills domaine
independently); the missing 3pl subject for "[62]ent" at @665/@1536 is
fenced as a residual (the bar is a word-form parse test; subject
placement is out of scope and affects all surviving candidates equally).

## Standing state

No standing verdict contradicted or downgraded. §7 intact (no
polyvalence declared; the noun/verb scope question is escalated as a
follow-up, not decided). The conditioned-62 red-team venue
(redteam-62-conditioned) is untouched; this battery's {règne, trône}
narrowing is an evidence package for it.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-62-ne-noun.md` (this file)
- Queue: `battery-queue.json` `val-62-ne-noun` → status `verdict`,
  result `null`, date 2026-10-09 (temp-file + rename, own entry only;
  pre-write assert confirmed `queued`/verdictless; JSON re-validated
  post-write)
- Lock: `locks/val-62-ne-noun.lock` created on start, deleted on
  completion
