# Battery report: est-59-frame-census

- Target id: `est-59-frame-census`
- Claim: "Harden the copular control: full census of 59 (n=27); '59 37' x6, '59 32' x3, '59 35' x3 are predicative followers"
- Date: 2026-10-09
- Worker: battery worker (subagent e93854e2-877a-4987-b733-a6821ee3c3aa)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 types asserted). All @-offsets are 0-based repaired-stream indices.
  `canonical.py` never used. R5005 not touched.
- Lock: code/crowd17/next-token/locks/est-59-frame-census.lock (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"harden iff ≥80% of 59's windows parse as copular ('est' + predicative/nominal complement) with residuals fenced"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) ≥80% of 59's 27 windows parse as copular ('est' + predicative/nominal
   complement) under standing values.
2. (C2) Every non-copular window is fenced with stated cause (no open,
   unexplained contradiction of the copular reading).

The bar is read as: copular coverage must reach the 80% threshold AND the
remainder must be fenced. Fencing alone does not count toward coverage.

## Method

1. Re-derived the repaired parse in-session; asserted 1,847 pairs / 96 types.
   Never used canonical.py. R5005 not touched.
2. Census: n(59) = 27, 0-based indices
   [103, 216, 316, 448, 463, 528, 554, 559, 624, 763, 825, 834, 912, 1178,
   1186, 1190, 1210, 1291, 1443, 1448, 1496, 1511, 1715, 1777, 1796, 1804, 1833].
   Byte-exact re-derivation; matches the claim's n=27.
3. Tested each window for a copular parse ('est' + predicative/nominal
   complement) under standing values: pencil GT (11=la, 70=pre, 82=m, 34=i,
   29=er, 40=e, 46=que), granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout,
   00=pour, 84=on, 47=ce), provisional (59=est, 77=le), frames (37/32/42
   predicative A1, 80/89 verb-frames A8, 85 verb-stem A3, 37-01 unit A12,
   "tout me [48-verb]" A7-L2). Battery-grade premises cited explicitly where
   load-bearing.

## Follower census (byte-exact)

- 59 37 x6 (@528, @624, @912, @1178, @1443, @1796) — A1 predicative.
- 59 32 x3 (@316, @448, @1210) — A1 predicative; @448/@1210 with 48='e'
  feminine inflection (R17 letter-tier grant).
- 59 35 x3 (@834, @1291, @1804) — 35=noun battery-PROMOTE (prof-35).
- 59 36 x2 (@1448, @1833) — 36=NOUN class, R18-ratified.
- 59 38 x1 (@825) — 38=verb-form battery-PROMOTE (noun26-38-profile C1).
- 59 30 x2 (@559, @1715) — 30="pas" battery-promoted conditional; both with
  94='ne' STRONG LEAD at -1 (negated copular frames).
- 59 39 x2 (@763, @1511) — 39="a/à" battery LEAD (report sweep F-promote).
- 59 19 x1 (@1777) — 19=verb lexeme battery-PROMOTE (verb19-lexeme-test),
  with 48='e' inflection.
- 59 45 x1 (@103), 59 42 x2 (@463, @1186), 59 46 x2 (@216, @1190),
  59 34 x1 (@554), 59 24 x1 (@1496).

## Window-level evidence

### Copular — 20 windows

**Predicative complement (A1 grants) — 9 windows, all clean:**
- @528 (a3_00): `97 47 44 59 37 64 26` — "[47=ce] [44] est [37-pred] qui" — clean.
- @624 (a4_01): `76 82 14 59 37 33 29` — "[76-noun] m'en est [37-pred]" — clean
  (the @622-626 'en'-clitic core banked by core-14-622-bank).
- @912 (a5_09): `49 64 83 59 37 96 09` — "qui de est [37-pred]" — clean.
- @1178 (a6_10): `74 32 48 59 37 77 78` — "32e est [37-pred] le [78]" — clean.
- @1443 (a7_09): `01 52 68 59 37 64 77` — "[68] est [37-pred] qui le" — clean.
- @1796 (a8_10): `56 42 94 59 37 91 79` — "ne est [37-pred] [91] tout" — clean.
- @316 (a2_04): `78 45 64 59 32 94 06` — "ce qui est [32-pred] ne ent" — clean.
- @448 (a2_09): `10 62 61 59 32 48 79` — "[61] est 32e tout" — clean.
- @1210 (a7_00): `21 65 64 59 32 48 96` — "qui est 32e par" — clean
  (fem32e-1211-redteam-input's canonical passive shape).

**Nominal complement — 5 windows:**
- @1448 (a7_09): `64 77 84 59 36 67 33` — "qui le on est [36-NOUN] et" — clean
  (36=NOUN R18-ratified).
- @1833 (a8_11): `24 82 16 59 36 69 64` — "m' [16] est [36-NOUN] ce qui" — clean.
- @834 (a5_06): `11 77 76 59 35 56 17` — "la le [76] est [35-noun] [56] fois" — clean
  at battery grade (35=noun battery-promote, prof-35).
- @1291 (a7_03): `11 17 84 59 35 94 52` — "la fois on est [35-noun] ne [52]" — clean
  at battery grade.
- @1804 (a8_10): `64 77 84 59 35 94 52` — "qui le on est [35-noun] ne [52]" — clean
  at battery grade.

**Negated copular — 2 windows:**
- @559 (a3_02): `17 86 94 59 30 67 11` — "fois [86] ne est pas et la" — clean
  negated copula at battery grade (30="pas" conditional promote; 94='ne' STRONG LEAD).
- @1715 (a8_06): `65 94 44 59 30 64 47` — "[65-noun] ne [44] est pas qui ce" — clean
  negated copular frame at battery grade; subject slot conditional on open 44
  (pronoun-44-1714 queued; noun-44 killed).

**Copular-passive / predicative participle — 2 windows:**
- @825 (a5_06): `13 24 87 59 38 82 01` — "ce est [38-pp] m' [01]" — "c'est [pp]"-shaped;
  clean at battery grade (noun26-38-profile C1 PASS, conditional on provisional 59='est').
- @1777 (a8_09): `24 87 64 59 19 48 74` — "qui est [19]e [74]" — copular-passive candidate;
  clean at battery grade (19=verb lexeme battery-promote; 48='e' R17 letter-tier).

**Copular + PP complement — 2 windows:**
- @763 (a5_03): `20 62 94 59 39 88 66` — "il ne est a/à [88] [66]" — "est à [88-verb]"-shaped
  ("être à + infinitive"); clean at battery grade (39="a/à" battery LEAD).
- @1511 (a7_11): `41 12 61 59 39 81 88` — "[61] est à [81-noun] [88]" — "est à [noun]"
  ("c'est à vous"-shaped); clean at battery grade.

### Fenced — 3 windows

- @103 (a1_03): `62 94 93 59 45 28 00` — "il ne [93] est ce [28] pour" — "est ce [28]"
  is copular iff 28 is predicative/nominal; 28's value is open (28='donc' killed by
  donc-28-triangulate; ce28-contact PROMOTE adopted). Fenced, not contradicted.
- @463 (a2_10): `79 87 11 59 42 96 00` — "tout ce la est [42] par pour" — copular iff
  42 is predicative/nominal; 42's value open (val-42-nominal / stem-42-verb / subj-42
  batteries variously null/promote at battery grade). Fenced.
- @1186 (a6_10): `82 06 06 59 42 06 84` — fenced as a **subjectless-'est' residual**
  per battery-subject-1186-est42 PROMOTE (finding grade, adopted as premise, not
  re-litigated). The subject hunt at @1186 is closed at battery level; 59 IS 'est'
  here but has no clean copular parse.

### Kill-grade residuals — 4 windows

- @216 (a2_00): `77 78 06 59 46 29 42` — "est que er [42]": "est que" + infinitive
  is ungrammatical in 1841 French (46=que pencil GT, 29='er' pencil GT). No copular
  parse under standing values.
- @554 (a3_01): `81 00 86 59 34 17 86` — the known genuine residual "59 34 17":
  "est-il fois" cannot parse (34='i' pencil GT letter). Kill-grade, adopted.
- @1190 (a6_10): `42 06 84 59 46 07 24` — 59 is word-internal here: REPORT.md's A15
  correction (crowd10 conditioner59) voids the "on est" family at @1189–1190; the
  live lane reading is the 3-syllable -este verb unit (06-84-59, set-valued).
  59 is not standalone 'est' at this window. Kill-grade for the copular parse.
- @1496 (a7_10): `00 66 15 59 24 89 41` — "est [24-finite-modal]": a copula followed
  by a finite modal is ungrammatical under standing values (24=finite-modal
  promoted). Would re-open only via red-team `24-en-verb-conflict` (red-team venue).

## Per-clause pass/fail

1. **C1 FAIL.** Copular coverage = 20/27 = **74.07%**, below the pre-registered
   80% threshold. Standing-grant copular: 11/27 (6 x 59-37 + 3 x 59-32 + 2 x 59-36);
   battery-grade copular: 9/27 (3 x 59-35, 1 x 59-38, 2 x 59-30, 1 x 59-19, 2 x 59-39).
   The 6-point gap to the bar is structural: 4 kill-grade residuals cannot recover
   to copular under current grants.
2. **C2 PASS.** All 7 non-copular windows are fenced with stated cause (3 fenced,
   4 kill-grade residuals); no open unexplained contradiction of the copular reading.

## Adverses

None listed in the queue entry.

## Verdict: KILL (of the harden claim)

The copular control **cannot be hardened to the 80% standard**: 20/27 = 74.1%
of 59's windows parse as copular, with 4 kill-grade residuals and 3 fenced
windows. The harden antecedent (≥80%) fails on the complete census.

**Scope fence (what did NOT die):** 59='est' itself is NOT killed. It remains
provisional standing with 74% copular support across 27 windows. This kill
targets only the harden claim (the 80% distributional threshold), not the value.
No standing or red-team verdict contradicted or downgraded; §7 intact.

**Re-open conditions (red-team venue):** any kill-grade residual re-parsing —
e.g. `24-en-verb-conflict` resolving 24='en' (moots @1496's modal obstruction),
the -este verb unit at @1190 re-scoped by the red team, or a licensed "est que"
parse at @216. Battery-grade premises already counted in the 20; ratifying them
does not change the count.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-est-59-frame-census.md
- Queue: `est-59-frame-census` → status `verdict`, result `kill`, date 2026-10-09
  (pre-write assert passed — was `queued`/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone). `canonical.py`
  never used; R5005, sealed gates, red-team queue untouched.
- Kill verdict — no follow-ups required per protocol (re-open conditions recorded above).
