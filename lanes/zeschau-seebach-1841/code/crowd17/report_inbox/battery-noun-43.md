# Battery verdict: noun-43 — name 43's noun value with the 'pour que' discriminator

- Target: `noun-43`
- Claim: 43 feminine noun (means/purpose)
- Worker: battery worker noun-43 (acf1d1e0-cd10-4409-abee-0c623170257f)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py. 1,847 pairs / 96 types verified in-session. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. No data invented. @-offsets are 0-based stream indices with row labels (this battery family's convention).
- Lock: created `code/crowd17/next-token/locks/noun-43.lock` on start, deleted on completion.

## 1. Bar (verbatim from battery-queue.json)

"promote iff value named with 'pour que' discriminator"

Numbered clauses:
1. A value for 43 is named that passes the 'pour que' discriminator (government reading: "X pour que [subjunctive]" grammatical in 1841 diplomatic French).
2. The named value survives the byte evidence at all other 43 windows (no kill-grade failure under standing values); the listed adverse ("exact value unnamed") is thereby closed.

## 2. Method

- Re-derived the repaired stream in-session; 43 census n=16 at 0-based @21/@43/@244/@258/@343/@386/@439/@563/@1027/@1092/@1126/@1204/@1303/@1305/@1544/@1724 — byte-identical to the ce-frame battery's independent census.
- Standing values used (protocol §7 + red-team rounds): 11=la, 82=m, 34=i, 29=er, 40=e, 46=que, 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce, 59=est (prov), 77=le (prov), 06=ent, 30=pas, 86 INF-class, 80/89 verb-frames, 12=n, 48=e, 94=ne, 98='vient' (battery-grade).
- Adopted, not re-litigated (protocol §5 — never downgrade an existing verdict):
  - battery-noun-43-discriminator (verdict KILL, 2026-10-08): killed 43='suite' and 43='manière'; defined the 'pour que' discriminator — under the government reading "condition pour que" ✓, "mesure pour que" ✓, "suite pour que" ✗, "manière pour que" ✗; @21 forces V(43)!="suite".
  - battery-cond-mesure-43full (verdict NULL, survivor set EMPTY, 2026-10-09): 'condition' and 'mesure' both fail par-43 x2 (0-based @343, @1027) and @21 at kill grade. Full-distribution survivor set: {}.
  - battery-43-29-segment (verdict PROMOTE, segmentation only, 2026-10-09): @21 "43 29" is word-internal "[43]er", an infinitive in the "vient me + INF" frame ("…qui vient me [43]er ce"); 43 keeps noun standing in 15/16 windows; the verb-stem shape is escalated to the red team; the bar explicitly states "do not re-name 43 at battery level".
- The boundary-vs-government adjudication at @1544 belongs to queued frame-43-pour-que-1544 (not pre-empted); the 43-21-43 doublet to queued frame-43-21-43-doublet; the 37/32-43 frames to queued frame-43-pred-37-32.

## 3. Window-level evidence (the three discriminator windows, re-derived)

**@1544 (a8_00) — the 'pour que' discriminator window:**
`62 06 21 62 93 88 77 78 [43] 00=pour 46=que 70=pre 12=n 94=ne 92 45 23`
Byte-identical to the discriminator battery's reading. 00='pour' (A9) + 46='que' (banked) = "pour que"; 70+12+94 = "prenne" (subjunctive, compositional on 12='n'/94='ne', battery-promoted). "43→00" occurs exactly once stream-wide; "00 46" occurs 4x stream-wide. Under the government reading ("[43] pour que [subj]"), the positive set is exactly {condition, mesure} — see §4. Under the boundary alternative ("…78 43. Pour que prenne 92…") the frame is non-discriminating; that adjudication belongs to queued frame-43-pour-que-1544.

**@343 (a2_05) / @1027 (a6_03) — par-43 x2:**
`40 03 64 31 14 45 64 96 [43] 87 01 06 70 12 94 74 67` / `91 53 84 92 64 45 64 96 [43] 87 01 03 29 80 77 11 70`
"96-43-87-01" = "par [43] ce [01]" (the 6-gram heads 0-based @340/@1024). Adopted kill-grade finding: bare "par condition" and bare "par mesure" are not idiomatic 1841 French (no "à condition que"/"sous condition" government here; "par mesure de X" needs its "de", absent). Any new candidate must license bare "par X".

**@21 (a1_00) — the class window:**
`76 45 91 53 17 64=qui 98 82=m [43] 29=er 47=ce 33 55 81 00 34 24`
Promoted word-internal segmentation: "…qui [98] m[43]er ce [33]". For a monovalent noun X, "mXer" must be a French infinitive AND X a French noun. The only French X with "mXer" an infinitive is X="en" ("mener") — and "en" is not a noun. No monovalent noun value parses @21. Protocol §7 bars polyvalence at battery level (67 et/veut is the sole true polyvalence); 43-29-segment's bar explicitly reserves the @21 shape for the red team.

## 4. The 'pour que' discriminator's positive set is exhausted

Testing extended feminine-noun candidates against the government reading "N pour que [subj]" in 1841 diplomatic French:
- condition ✓ — dead (par-43 x2 + @21 kill-grade, cond-mesure-43full).
- mesure ✓ — dead (par-43 x2 + @21 kill-grade, cond-mesure-43full).
- façon ✗ — the idiom is "de façon que / de façon à ce que", never bare "façon pour que".
- manière ✗ — idiom "de manière à ce que"; already killed (noun-43-discriminator).
- raison ✗ — "la raison pour laquelle", not "raison pour que".
- fin ✗ — "à cette fin que / afin que".
- cause ✗ — "à cause de" + noun, never "cause pour que".
- intention ✗ — "dans l'intention de" + infinitive.
- précaution ✗ — no "précaution pour que" government.
- disposition — "prendre des dispositions pour que" is idiomatic, but it dies on bare "par disposition" (not French) and at @21 (class kill-grade, same as every noun).

The discriminator's positive set within French feminine nouns is {condition, mesure} — both killed at kill grade on independent windows. No new candidate can pass the discriminator while surviving par-43 and @21.

## 5. Per-clause pass/fail

1. **Clause 1 (value named with 'pour que' discriminator): FAIL.** The candidate set {suite, manière, condition, mesure} is fully exhausted (all killed at battery grade); the discriminator's positive set is exhausted at the lexical level (§4); and @21 independently kills every monovalent noun at kill grade via the promoted word-internal segmentation. No value can be named.
2. **Clause 2 (no kill-grade failure; adverse closed): FAIL.** The adverse "exact value unnamed" cannot be closed at battery grade — the exhaustion is complete, and the only escapes (period-corpus attestation of bare "par mesure"/"par condition"; the @21 polyvalence adjudication) are red-team acts, not battery acts.

No standing verdict is contradicted or downgraded (suite/manière kills, cond-mesure-43full's empty survivor set, and 43-29-segment's segmentation promote all stand; no red-team ruling covers 43's value). R5005, sealed gates, and the red-team adjudication queue untouched.

## 6. Verdict: NULL

The bar's promote condition is unsatisfiable at battery grade: no feminine-noun value passes the 'pour que' discriminator while surviving the byte evidence. The noun-43 line is closed at battery level pending red-team act — either (a) a period-corpus defense of bare "par mesure"/"par condition" as 1841 adverbials, or (b) the red team's ruling on the @21 verb-stem shape (polyvalence question, escalated by battery-43-29-segment).

## 7. Follow-up targets (null regenerates work)

1. `pour-que-lexicon-close` (P3) — formalize the 'pour que' discriminator's positive set: census which French feminine nouns license bare "N pour que [subj]" in 1841 diplomatic/administrative French with period-dictionary evidence (Littré / Dictionnaire de l'Académie), and certify the set = {condition, mesure} (both dead). This closes the discriminator itself as exhausted, so no future battery re-runs it.
2. `par43-adverbial-attestation` (P2) — 1841 corpus attestation check for bare "par mesure" / "par condition" as adverbials; coordinate with queued venir-a-1841-corpus (do not duplicate — merge if it covers this). If attested, re-open the noun premise with the attestation; if not, the par-43 kill is terminal and the noun-43 line is closed pending only the @21 polyvalence ruling.
