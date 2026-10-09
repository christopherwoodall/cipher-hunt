# Battery report: cier-85-595-name

- Target id: `cier-85-595-name`
- Claim: "The surviving W1 parse is 'tout [85]cier' + 'e[03]…' — test the -cier nominal family (mercier/épicier/sourcier/financier) against 85's contact profile; name 85's value iff one family member's stem fits 85's other windows."
- Date: 2026-10-09
- Worker: battery worker (subagent c3e29b21-0b86-4662-9dd8-f637c6dd78c4)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; n=1847, 96 types asserted in-session).
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/cier-85-595-name.lock` (created at
  start with agent id + UTC timestamp; deleted on completion; no prior lock
  existed). NOTE: first created one level too high (repo root
  `code/crowd17/...`); removed it and recreated at the lane path before
  testing. No double-dispatch resulted.

## Bar (verbatim, pre-registered before testing)

"name 85's value iff one family member's stem fits 85's other windows"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1, promote) Exactly ONE -cier family member's stem fits ALL of 85's
   other (non-@595) windows — fit = at least one grammatical parse of the
   window exists with 85 carrying that stem, under standing grants only.
   Then name that stem as 85's value.
2. (C2, kill) A window forces the fit-claim false at kill grade — i.e. for
   a candidate stem, some window admits NO grammatical parse with 85 = that
   stem — or no family member fits.

Standing values used: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que); promoted (79=tout, 87=ce, 64=qui, 96=par, 17=fois, 47=ce, 84=on,
00=pour); A3 frame grant (85 verb-stem candidate, value open). NOT assumed:
any value for 85, 01, 58, 08, 33, 56, or the -cier stems.

## Method

1. Re-derived the repaired parse in-session (1,847 pairs, 96 types).
2. Re-derived all 15 windows of 85 with ±6 context; confirmed the census
   matches stem-85's independent table (offsets 54, 97, 375, 595, 733, 746,
   956, 1047, 1173, 1234, 1278, 1439, 1694, 1699, 1755).
3. Fixed the -cier parse's requirement: @595 "79-85-01-29" = "tout [85]cier"
   needs 85 = S, the stem of a French noun in -cier (01="ci"
   word-internal per unit-85-01, 29="er" banked GT; the word after banked
   79="tout" starts at 85, so 85 covers the whole stem).
4. Enumerated the French -cier nominal stem set beyond the bar's four:
   mer, sour, lan (monosyllabic: mercier, sourcier, lancier); épi, finan,
   offi, créan, justi, roman, devan, balan, poli, pla (disyllabic:
   épicier, financier, officier, créancier, justicier, romancier,
   devancier, balancier, policier, placier). Tested every stem against the
   14 non-@595 windows for kill-grade incompatibility.
5. Corpus check: grepped `code/side-period/corpus/` (1.57M chars, 1841
   French + German press) for word-initial "er"+stem for every stem above.

## Window-level evidence

### The kill window: @97 (row a1_02)

Bytes: `41 98 81 97 46 29 85 08 21 62 94 93 59`
= "…[97] que(46) er(29) [85] [08] [21] [62]…"

46='que' is banked pencil GT — a complete word. Therefore the word
containing 29 starts AT 29. For 85 = S (any -cier stem), the surface is
"que er S [08]", with only these segmentations:

- (a) "que" | "erS[08]…" — needs a French word beginning "er"+S.
- (b) "que" | "er" | "S[08]…" — "er" is not a French word. Dead.
- (c) "que"+"er" one word — "quer"+S is not French. Dead.
- (d) 29 attaches leftward across 46 — impossible (46='que' intervenes,
  banked complete). Dead.
- (e) elision "qu'erS…" — still needs "erS" to be a word. Dead.

So (a) is the only live shape, and it needs word-initial "er"+S:

| stem S | needs word-initial | French? |
|---|---|---|
| mer (mercier) | "ermer" | NO |
| sour (sourcier) | "ersour" | NO |
| lan (lancier) | "erlan" | NO |
| épi (épicier) | "erépi" | NO |
| finan (financier) | "erfinan" | NO |
| offi (officier) | "eroffi" | NO |
| créan (créancier) | "ercréan" | NO |
| justi (justicier) | "erjusti" | NO |
| roman (romancier) | "erroman" | NO |
| devan (devancier) | "erdevan" | NO |
| balan (balancier) | "erbalan" | NO |
| poli (policier) | "erpoli" | NO |
| pla (placier) | "erpla" | NO |

Corpus verification (`code/side-period/corpus/`, 1.57M chars): word-initial
"ermer"/"ersour"/"erlan" hits are 100% German-language files (Metternich
Papiere, Allgemeine Zeitung: "Erlangen", "Erlangung", "ermerbeu",
"ermerfung" — German OCR); ZERO French tokens. French "ermer" occurs only
medially ("fermer" ×92, "enfermer" ×28). All other "er"+stem patterns: 0
hits in any language. Sanity: "erreur" ×409, "ermite" ×11 present — the
corpus does contain French er-words; it contains none of the needed ones.

**@97 admits no grammatical parse with 85 = any -cier stem. Kill grade.**
The four bar-named members (mercier/épicier/sourcier/financier) die here,
and so does every other French -cier noun stem, nominal or verbal
("remercier"→"erremer", "négocier"→"ernégo" likewise dead — checked).

### @595 (the -cier window itself, row a4_00)

"79-85-01-29-40" = "tout [85]cier e(40) [03]…". Grammatical per stem
("tout mercier/officier/financier/épicier" all well-formed masculine
"tout"+N). The window is fine — it is the STEM SET that is empty, not the
frame. The parse REQUIRES 85 ∈ {-cier stems}; @97 FORBIDS 85 ∈ {-cier
stems}. Same cipher, same 85. **The "tout [85]cier" parse is therefore
kill-grade dead**, not merely unnamed. (This overturns unit-85-01's
"surviving W1 parse" observation — its KILL of the 85-01 unit stands
untouched; only the survival note for the -cier alternative falls.)

### Other windows (spot status for the monosyllabic stems, mer/sour)

- @54 "tout(79) [85] [58]": compatible only if 85-58 is one masculine word
  (58 open) — weak, not kill-grade.
- @375 "[63] er(29) [85] m(82)": compatible via 63="f" ("fermer"; 63 open)
  — weak, not kill-grade.
- @733/@956/@1694/@1755 "en(24) [85] …": "en mer" = "at sea" grammatical
  (tension with the A3 gerund frame noted, not adjudicated here).
- @746/@1047/@1173/@1278/@1439/@1699: all distinctive neighbors open —
  compatible, uninformative.
- @1234 "ce(47) [33] er(29) [85] [56]": "er"+S onset problem recurs, but
  33 is open (33="f" → "fermer" rescues the onset; left context "ce
  fermer" strained) — not kill-grade.

Only @97 kills; one kill-grade window is sufficient.

## Per-clause pass/fail

1. (C1, promote) **FAIL at kill grade.** Zero of 13 enumerated -cier stems
   (including the bar's four) fits 85's other windows — @97 forces every
   one false. Nothing to name.
2. (C2, kill) **PASS.** @97 admits no grammatical parse with 85 = any
   -cier stem (46='que' banked complete forces word-initial "er"+S; no
   such French word exists, corpus-verified). The fit-claim is false at
   kill grade for every member.
3. Adverses answered: the listed adverse ("would feed the F2 nominal side,
   not the verbal side") is MOOT — a kill feeds neither side. Noted for
   the record: the F2 nominal FUNCTION tension (79='tout' ×2, stem-85
   Adverse 2) stands unchanged; only the -cier VALUE avenue is dead.

## Verdict: KILL

No -cier family member's stem fits 85's windows (@97 kills every stem at
kill grade), so 85's value cannot be named from this family — and
further, the @595 "tout [85]cier" parse that motivated the target is
itself dead at battery grade (it requires 85 to be a -cier stem; @97
forbids it).

## Standing-state consequences

- unit-85-01 KILL (85-01 unit) untouched; its "surviving -cier W1 parse"
  observation is SUPERSEDED by this kill. @595's parse is now fully open
  (neither unit nor -cier).
- A3 frame grant (85 verb-stem candidate) untouched and unweakened — this
  kill removes a nominal VALUE avenue, not a frame leg. No red-team
  verdict contradicted (Round 18 has no value verdict on 85).
- The crowd16 "tout entière" lead (85-01="enti", @595) was NOT tested here
  and is NOT revived by this kill — it becomes the next @595 candidate
  (see follow-up 1). Note it carries its own load: 85="en" vs the five
  "24-85" windows ("en en" ungrammatical under 24='en' A3 GT).
- ci-01-value KILL untouched (this battery never needed 01's value).
- §7 sole-polyvalence law untouched.

## Follow-ups proposed (kill regenerates work)

1. `entier-85-595-reaudit` (P2): @595's parse is now fully open. Test the
   crowd16 "tout entière" rival (85="en", 01="ti", 29-40="ère") against
   85's other 14 windows. Bar: promote "entière" iff 85="en" survives all
   14 (watch the five "24-85" windows: "en en" is ungrammatical under
   24='en' A3 GT — the finite-verb reading of 24 is the only escape);
   kill iff any window forces 85≠"en".
2. `frame-29-85-triple` (P3): the three "29-85" windows (@97/@375/@1234)
   now positively constrain 85: at @97 the word starts at 29 (46='que'
   banked), so 85's value V must satisfy "er"+V beginning a French word
   (e.g. V="reur" → "erreur": "46-29-85-08" = "que erreur [08]" —
   sketch only, test properly). Bar: name 85's value/class iff ≥2 of the
   3 windows converge on it under standing grants; null with the
   constraint set otherwise.
3. `tout-85-54-keyhole` (P3): with the -cier avenue dead, the F2 nominal
   side rests on "tout [85]" ×2 (@54/@595) with 85's value open; @54's
   "79-85-58" makes 58 the keyhole (a nominal 85 needs 85-58 as one
   masculine word). Bar: name 58's value/class iff it closes a
   grammatical "tout [85-58]" noun phrase with ≥1 independent leg;
   null otherwise.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-cier-85-595-name.md`
- Queue: `battery-queue.json` → `cier-85-595-name` status `verdict`,
  result `kill`, date 2026-10-09 (temp-file + rename; pre-write assert
  confirmed queued/verdictless/unlocked; JSON re-validated post-write;
  only this entry touched).
- Lock created at start (lane path), deleted on completion.
