# Round-16 battery: m (82) — frames, formula, adverse adjudication

Finder report: `code/crowd16/report_inbox/next-token-findings-m.md` (ingested 2026-10-07).
Status entering: 82="m" BANKED (pencil GT). 96="par" PROMOTED. 84="on"
GRANTED-with-conditions (A15). 79="tout" BANKED (A5). A7 L2 "tout me
[48-verb]" frame GRANTED (48 verb-stem candidate).

---

## PRE-REGISTRATION (locked before formal tests)

**Bar M1 (P1 formula):** "vient de me parvenir" word-reading is LEAD-grade
iff the 5-gram 98-83-82-96-21 re-derives byte-identical ×3 AND 96-21 occurs
nowhere else (formula-bound). 98="vient"/83="de" are word-anchored LEADS
(1 phrase type ×3 tokens — not cell-value promotions). The 60/62/68
thirds-homophone-set is NOT granted by assertion — it needs the
{33,86}-precedent standard (joint frames + distribution test); QUEUED.

**Bar M5 (P5 79-adverse):** the "qui"+"tout/tous" double-subject objection
is tested against A7's granted boundary parse ("…qui [X]. Tout me
[48-verb]…"). The boundary parse SURVIVES iff "qui [X]" is a complete
clause at the window (X = verb before the boundary). If the qui-clause is
verbless at both windows, @396/@1227 are FENCED as strained residuals for
79="tout" (2/18) — the banked value stands on its 4 compositional legs;
A7 L2 is untouched (it never depended on these two windows). This REVISES
my tout-battery B4 ("narrow/reducible"), which under-weighted the "qui".

**Bar M6 (P6 84-noun):** REJECTED iff the A15-established "mon" reading of
82-84 @166 accounts for the window — the finder is re-litigating settled
ground (F53 noun-arm KILLED). The "m'84 elision ⇒ vowel-initial" premise is
checked against the actual trigram.

**Bars M2/M3/M4/M7:** counts re-derived; batteries queued, no verdicts.

---

## TESTS

`t = code/crowd16/next-token/test_m.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | 98-83-82-96-21 ×3 @229/@1062/@1785 byte-identical; thirds 60/62/68 | |
| 2 | 96-21 global = [230,1063,1786] (formula-bound, nowhere else) | |
| 3 | 94-82-06-06 ×2 @578/@1182 | |
| 4 | 52-82-94 ×3 @649/@1100/@1574; windows | |
| 5 | 82-16 = 11; 16-91 ×2 | |
| 6 | 82-40 = 0 (bare-82 model) | |
| 7 | @396 wide P[384:402]; @1227 wide P[1215:1235] (qui-clause verb hunt) | |
| 8 | @166: P[162:170] = [24,87,11,24,82,84,53,12] ("mon" vs "m'84") | |
| 9 | @20: P[18:25] (43 verb-stem window) | |
| 10 | @1743: P[1741:1746] (82-46 "m'que") | |

---

## VERDICT

**M1 formula — VERIFIED, word-reading LEAD.** 98-83-82-96-21 byte-identical
×3 @227/@1060/@1783 (finder cited 82-cells @229/@1062/@1785 — convention
note); thirds 60/62/68 @232/@1065/@1788; **96-21 occurs nowhere else
globally** ([230,1063,1786] — formula-bound, not productive "par+X").
"vient de me parvenir" is perfect dispatch French in exact order. 98="vient"
and 83="de" are word-anchored LEADS (1 phrase type ×3 tokens — not cell-value
promotions). The 60/62/68 thirds-homophone-set is NOT granted by assertion:
it needs the {33,86}-precedent standard (joint frames + distribution test)
— QUEUED as a battery, not a finding. 83="de" cross-check windows (@897,
@930) queued with it.

**M5 (79-adverse) — ADJUDICATED: the double-subject point is real; 2
fenced residuals; CORRECTION to my tout battery.**
- The m finder's "qui"+"tout/tous" double-subject objection is VALID for the
  single-clause parse ("qui tout/tous m'[verb]" ungrammatical; corpus: zero
  "qui tout/tous m'" in Nesselrode v8 + Guizot t1–t3).
- A7's granted boundary parse ("…qui [X]. Tout me [48-verb]…", "tout" as
  subject of a new clause, corpus-attested "tout me sourit/ramène/porte/
  frappa") does NOT cleanly work at these windows: the qui-clause is
  verbless at both (@396: "…[73][34][67] qui |"; @1227: "…[9][20][57] qui |"
  — no verb before the boundary).
- **Verdict: @396/@1227 are FENCED as strained residuals for 79="tout"
  (2/18).** The banked value stands on its 4 compositional legs (none has
  the "qui"+"tout" problem). A7's L2 frame (48=verb-stem candidate) is
  UNTOUCHED — it rests on the 4 "me [48]" windows + corpus, never on these
  two parsing as "Tout me [verb]".
- **Correction to next-token-tout.md B4:** my "narrow/reducible to 67/57"
  weighing under-weighted the "qui". B4 is revised to "2 fenced residuals
  (qui+tout double-subject; boundary parse strained by verbless qui-clause;
  'tous m'entourent' core does not survive the preceding 'qui')". The
  tout verdict's CONFIRM stands; the adverse section is corrected.

**M6 (84 = vowel-initial masculine noun) — REJECTED as overtaken.** @166 =
[24,87,11,24,82,84,53,12]: 82-84 = **"mon"** (82="m" + 84="on", possessive;
"en mon [53]"), established by the A15 grant. The finder's "m'84 elision ⇒
vowel-initial" premise misreads the trigram — it is not elision. F53's
noun-arm for 84 is kill-grade dead; 84="on" stands with its 3 fenced
residuals (R1/R2/R3). No re-litigation.

**M2/M3/M4/M7 — counts verified, batteries queued:**
- 94-82-06-06 ×2 @578/@1182 (06 key; feeds the 06 battery and the 94="ne" lead).
- 52-82-94 ×3 @649/@1100/@1574 (52 paradox: "la/qui 52" vs "52-82-94" formula; queued).
- 82-16 ×11 (biggest cluster; 16-91 ×2 @537/@1370 sub-cluster; queued).
- 82-40 = 0 (bare-82 model confirmed).
- @20: [53,17,64,98,82,43,29,47,33,55] = "…fois qui [98] m'[43]-er ce [33]" —
  43 verb-stem lead ("m'[43]er" infinitive after "m'"; 43 takes 00×3/77×2/87×2).
- @1743: [34,94,82,46,56,40] = 82-46 "m'que" (with 94 before: "ne m'que"?) —
  82 word-internal here per the finder's constraint reading; queued.

**Queued:** 60/62/68 thirds-homophone battery ({33,86} standard); 83="de"
cross-check; 06 ent/en battery (P2's key); 52 noun-paradox battery; 16-profile
battery (16-91 sharp end); 43 verb-stem frames.
