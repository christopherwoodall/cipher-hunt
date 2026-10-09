# Battery `val-41-1016` — verdict: NULL (fence)

Worker: 64ef0096-b113-463c-ae48-07fca32cb0b4 · 2026-10-09T13:29:54Z start
Follow-up #2 of `15-value-id` NULL (2026-10-09). Decides whether W_C
(@1017 "[41] [15] [66]") can ever license 15='plus'.

## Bar (verbatim, pre-registered)

> "41's value named with battery-grade evidence; else fence W_C for 'plus' permanently."

Restated as numbered pass/fail clauses (before testing):
- C1: 41's value named with battery-grade evidence — at least two
  independent legs, zero ungranted assumptions, and the value fits all 19
  of 41's windows under §7's sole-polyvalence rule (67 is the only true
  polyvalence; 41 may not split at battery grade).
- C2 (else-arm): if C1 fails, fence W_C (@1017 "[41] [15] [66]") for
  'plus' permanently — record with cause that no future battery may
  license 15='plus' through the "[41] plus [66]" frame.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs,
96 types; 0-based @-offsets). `canonical.py` never used. Adopted premises
(not re-litigated): 47='ce', 64='qui', 17='fois', 11='la', 00='pour',
79='tout', 84='on', 77='le' (prov), 85 verb-stem (A3), 24 finite/modal
(R24: follower 41 is not 85, so 24 is finite/modal here), 66
infinitive-shaped, 15 adverb-class (15-noun-verify, noun arm killed),
§7 (67 sole true polyvalence; 1690 uniformity necessary but insufficient).
Standing 41 results adopted: `val-41-det-windows` PROMOTE (determiner arm
at the fois window, values une/chaque/deux/plusieurs unforced);
`split-41-redteam` queued (red-team adjudication of 41's §7 split
candidacy — not decided, not touched). Corpus:
`code/side-period/corpus` (63 files, 31,664,431 chars) for kill-grade
grammaticality counts. R5005, sealed gates, red-team queue untouched.

## Window-level evidence (byte-exact, 0-based)

**Target W0 @1016** (row a6_02):
`@1008..1023 = 35 18 79 80 78 47 03 24 | 41 | 15 66 91 53 | 84`
→ "…[47=ce] 03 [24-fin] [41] [15-adv] [66-inf] 91 53 | [84=on]…"
(@1020 starts row a6_03.) 24's follower is 41 (not 85), so 24 is
finite/modal per R24. 15 is adverb-class; its noun reading is killed, so
15 cannot be the nominal after a determiner-41.

**41 census: n(41)=19** — [@5, @39, @59, @91, @237, @444, @489, @589,
@590, @808, @964, @1016, @1048, @1111, @1472, @1499, @1508, @1535,
@1759]. Predecessors: {12 x2, 78 x2, 24 x2, 56 x2, 73 x2, 47, 64, 19,
98, 42, 97, 41, 85, 89}. Followers: {12 x2, 15 x2, 06, 01, 08, 98,
17, 10, 20, 41, 09, 19, 88, 65, 53, 74, 62}.

**Discriminating windows:**
- **D1 @237** (a2_01): `71 51 70 98 | 41 | 17 11 26 12` →
  "[98] [41] [17=fois] [11=la]". The promoted determiner arm lives here
  ("[V] [det] fois"-shaped; val-41-det-windows). Corpus "X fois la"
  census: only {la, une, seconde, première, mille, dernière, cette}
  attest — determiners, ordinals, numerals. No adverb, preposition, or
  verb directly precedes "fois la" in 31.6M chars.
- **D2 @589/@590** (a3_02 → a4_00): `00=pour 97 | 41 41 | 09 00=pour` →
  41 DOUBLED across the row boundary. Verified present in upstream's
  original 1,846-pair parse too — not a repair artifact. Corpus:
  "sans sans" 0 hits; no formal-1841 word doubles ("très très",
  "bien bien", "tout tout" are colloquial or ungrammatical). Every
  single-word candidate dies here.
- **D3 @5** (a1_00): `00=pour 97 51 47=ce | 41 | 06 77=le` → "ce [41]":
  kills numerals/determiners (*"ce deux", *"ce une"), kills adverbs
  (*"ce bien"); admits adjectives ("ce même [N]") — but adjectives die
  at D1 (*"[adj] fois").
- **D4 @39** (a1_01): `39 64=qui | 41 | 01 24` → "qui [41] 01 [24-fin]":
  kills finite verbs ("qui V 01 V" ungrammatical), kills numerals
  (*"qui deux 01 V").
- **D5 @1048** (a6_04): `76 85=verb-stem | 41 | 88 29=er` → adverb- or
  preposition-compatible ("[V] [adv/prep] …").

**Candidate 'sans' (the bar's motivating example) — KILLED at kill grade:**
'sans' fits W0 ("[V] sans plus [inf]" if 15='plus'), D4 ("qui sans [01]
[V]" — "qui sans doute/cese [V]"-shaped), D5, and ten further windows
as a preposition+NP — but D1 kills it ("sans fois": 0 hits in 31.6M
chars of period French; *"sans fois" ungrammatical — "fois" needs a
determiner) and D2 kills it ("sans sans": 0 hits; undoubled
prepositions do not double). Two independent kill-grade windows.
'sans' is closed as 41's value; no future battery should re-propose it
without new stream evidence.

**Determiner arm vs W0 — incompatible:** under the promoted @237
determiner arm, W0 reads "[24-fin] [det] [15-adv] [66-inf]". A
determiner between a finite verb and an adverb+infinitive has no French
parse for any of the four unforced values (une/chaque/deux/plusieurs:
*"veut deux plus [inf]", *"veut une plus [inf]" — and 15-as-noun, the
only nominal 41 could determine here, is killed). So either 41 is not
determiner-class at @1016 (split — red-team territory, already queued
as split-41-redteam) or no single value covers both windows.

## Per-clause results

- **C1: FAIL.** No value is nameable at battery grade. 'sans' — the only
  candidate that makes W0 parse — is killed at kill grade on two
  independent windows (D1, D2). The determiner arm (promoted at D1) is
  ungrammatical at W0. The D2 doubling kills every remaining
  single-word class under §7's sole-polyvalence rule. The three
  constraint sets (D1: {det/ordinal/numeral}; D2: {nothing doubles};
  D3/D4: {not det, not adverb, not verb}) are jointly unsatisfiable by
  one French word.
- **C2: FIRES.** Per the bar's else-arm: NULL, fence W_C for 'plus'
  permanently.

## The W_C fence (cause, permanent)

W_C (@1017 "[41] [15] [66]") can never license 15='plus'. The only
grammatical "[41] plus [66]" parse under standing values was
41='sans' → "sans plus [inf]" (15-value-id C5). 41='sans' is now killed
at kill grade (D1 "sans fois" 0/31.6M; D2 "sans sans" 0/31.6M). No other
41 value makes "[41] plus [66]" parse, and 41's value is unnameable
(C1). The fence binds future batteries: 15='plus' must be licensed via
W_A ("ne plus [33]", stands) or W_B (needs 01's class, val-01-class
line) — never via W_C. This fence does not kill 15='plus' itself.

## Adverses (none pre-listed; found in testing)

- A1 (val-41-det-windows PROMOTE): the determiner arm at D1 is
  incompatible with every W0 parse under single-value §7. Cannot be
  "answered" at battery grade — it is the split question. Referred to
  the already-queued `split-41-redteam`; not re-opened here.
- A2 (D2 doubling vs upstream offsets): the doubling survives in
  upstream's original parse, so it is not a repair artifact — but rows
  a3_02/a4_00 offsets are among the 68 unvalidated upstream offsets
  (canonicality caveat). Fenced to follow-up 1 below, not decided here.
- A3 (§7 sole-polyvalence): blocks declaring 41=det at D1 and 41=sans
  at W0 simultaneously at battery grade. Standing rule, not re-opened.

## Kill-grade note for the supervisor

'sans' as 41's global value is dead at kill grade (D1+D2, corpus zeros)
— stronger than this target needs. The target verdict stays NULL per
the bar's explicit else-arm ("else fence"); do NOT harden NULL→KILL
while `split-41-redteam` is still queued, because a granted split would
re-open per-window naming (including @1016).

## Verdict: NULL (fence)

## Follow-ups (all verified ABSENT from battery-queue.json 2026-10-09;
## none duplicate queued targets: split-41-redteam, fin-41-lexicon-r2,
## seg-41-08-leftedge, wordinternal-41-census, val-41-40-independent)

1. `41-doubling-audit` (P3) — byte-level audit of the @589/590 "41 41"
   doubling: re-derive rows a3_02/a4_00 from raw digits under both
   offset phasings for a4_00; determine stream-real vs offset artifact.
   If artifact, 41 becomes nameable and this target re-opens. Bar: the
   doubling stands or falls with byte-level evidence; else fence.
   Evidence: `@588..592 = 97 41 41 09 00`, rows a3_02/a4_00; doubling
   present in upstream 1,846-pair parse. Adverses: none listed.
2. `41-1016-det-incompatibility` (P3) — deliver the W0-vs-determiner-arm
   incompatibility to the split-41-redteam docket: test each unforced
   det value (une/chaque/deux/plusieurs) against "[24-fin] [det]
   [15-adv] [66-inf]" @1016 with corpus counts; either all four fail
   (split forced) or a clause boundary inside @1015..1017 rescues one.
   Bar: per-value pass/fail with corpus evidence; else fence.
   Evidence: W0 `@1008..1023` above; 15-as-noun killed (15-noun-verify).
   Adverses: A1 (det arm) — carried, not answered.
3. `98-237-frame` (P3) — name 98's class/value at @236 ("71 51 70=pre
   98 41 17=fois la"): 98='par' licenses "par [41] fois" (numeral arm);
   98=finite verb licenses "[V] [41] fois la [NP]"; any other value
   reframes D1. Decides what the determiner arm's strong leg stands on.
   Bar: 98's class named with >=2 independent legs; else fence.
   Evidence: n(98)=40; @236 window above; no existing 98 target covers
   @236 (checked: prof-98, cont98-43-value, vient-98-*, val-98-subject
   are verdict or target other windows). Adverses: none listed.

## Scope

Fences 41's nameability at @1016 and W_C-for-'plus' only. Untouched:
all §7 standings, `val-41-det-windows` PROMOTE, `split-41-redteam`
(queued), `val-41-40-independent` (queued, different window — no claim
made about @40), R5005, sealed gates, red-team adjudication queue. No
standing or red-team verdict contradicted or downgraded. Canonicality
caveat stands (rows a3_02/a4_00 offsets unvalidated — see follow-up 1).
