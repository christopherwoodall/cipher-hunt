# Battery report: lever-lement-rival

Target: `lever-lement-rival`
Claim: "the '…levement' rival at @1180/@1351 stays undemonstrated"
Date: 2026-10-09
Worker: fdd05089-3e41-469f-95ae-743ced6585e3
Lock: `code/crowd17/next-token/locks/lever-lement-rival.lock` created on start, deleted on completion. No stale lock existed.
Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`; pair counts re-derived in-session: 1,847 pairs, 96 types — matches). `code/side-keyhunt/canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"(1) test whether 59@1178 / 62@1349 can host the missing pre-syllable of '…levement' (sou-/en-/re-) under any granted, provisional, or battery-promoted value; (2) if no host, record the 77-78-94-82-06 'nement'-host as a count-level observation (morph94), not a parse — it does not kill the lever composition; (3) state which 06 value (trigram-internal-'ent' vs verb-stem) the clause-2 boundary parse requires at 06@1184/@1355"

Numbered pass/fail clauses (fixed before testing, not modified after):

1. 59@1178 or 62@1349 hosts the pre-syllable (sou-/en-/re-) under a standing (granted, provisional, or battery-promoted) value. FAIL = no host under any standing value.
2. If no host: the 77-78-94-82-06 'nement'-host is recorded as a count-level observation only, and does not kill the 77-78 'lever' composition.
3. The clause-2 boundary parse's required 06 value at 06@1184/@1355 is stated (trigram-internal-'ent' vs verb-stem).

## Standing values used (granted, provisional, battery-promoted — §7 plus queue verdicts)

- 59: provisional **"est"** (§7); battery-promoted frames **est-59-frames** (2026-10-08, PROMOTE). No other standing value. Red-team registry: null.
- 62: battery-promoted **"il"** (il-62, 2026-10-08, PROMOTE). 62="man" killed (mannequin-62-98-test); 62="on" killed lane-wide (collision-62-84); conditioned "on" only at @508 (lon-62-on-conditioned, NULL). règne/trône hypotheses unnamed (val-62-ne-noun, NULL). Red-team registry: null.
- 94 = "ne" (ne-94, PROMOTE); 82 = 'm' (banked GT, letter); 06 = "ent/ment" (ent-06, PROMOTE 2026-10-08); 48 = 'e' (letter, promoted); 37 predicative frames granted, value open (A1).

## Method

1. Re-derived the repaired stream in-session; asserted 1,847 pairs / 96 types.
2. Verified the @ positions byte-exactly: pairs[1178]='59', pairs[1349]='62', pairs[1180:1185]=['77','78','94','82','06'], pairs[1351:1356]=['77','78','94','82','06'].
3. Enumerated all standing values for 59 and 62 (queue verdicts + §7 + red-team registry) and tested each against the pre-syllable set {sou-, en-, re-} of attested French "-lèvement" words (soulèvement, enlèvement, relèvement).
4. Census: 5-gram "77 78 94 82 06" and trigram "94 82 06" stream-wide; parsed each trigram site under standing values.
5. Stated the 06 requirement of the lever-77-78 clause-2 boundary route ("…lever | Ne me [06-verb]…") against ent-06's promoted frames.

## Window-level evidence (0-based @)

### W1 @1178 (row a6_10): `…32 48 [59] 37 [77 78 94 82 06] 06 59 42 06…`
- 59@1178 = "est" (provisional + battery-promoted frames). "est" does not spell sou-/en-/re-. NO HOST.
- Structural observation (stated, not a bar criterion): 37@1179 intervenes between 59@1178 and 77@1180 — even a hypothetical host value at 59 would need to absorb 37 (predicative frames granted, value open) into the word; no composition exists.
- The only other standing 59 value is none. Rival-required 59="sou" would contradict the battery-promoted est-59-frames — a new value claim, not a standing value; out of scope per the bar.

### W2 @1349 (row a7_05→a7_06): `…34 [62] 48 [77 78 94 82 06] 52 37 64 35…`
- 62@1349 = "il" (battery-promoted). "il" does not spell sou-/en-/re-. NO HOST.
- Structural observation: 48@1350 ('e', promoted letter) intervenes between 62@1349 and 77@1351 — "il"+"e"+"…lement" composes no French word.
- Rival-required 62="en" would contradict the battery-promoted il-62 — a new value claim, not a standing value; out of scope per the bar.

### 'nement'-host count-level observation (clause 2)
- 5-gram "77 78 94 82 06": exactly **2x** stream-wide — @1180 and @1351 (the two lever sites). Recorded as a count-level observation.
- Trigram "94 82 06": exactly **3x** — @578, @1182, @1353.
  - @578: under standing values = "94-82-06-06" = **"ne mentent"** (ent-06 F1, CLEAN).
  - @1182: "94-82-06-06" = **"ne mentent"** (ent-06 F2, CLEAN).
  - @1353: "94-82-06" + 52 — no second 06, so "ne mentent" does not complete here; "ne"+"m"+"ent" partial, fenced (52 open).
- Under the standing battery verdicts, the trigram's demonstrated parses are "ne mentent" (x2 clean), not "…ment". The 'nement'-host is therefore a distributional observation (morph94), NOT a parse; it does not kill the 77-78 'lever' composition and it does not demonstrate the rival.

### Clause-2 boundary parse's 06 requirement (clause 3)
- The lever-77-78 boundary route at both sites is "…lever | **Ne me [06-verb]**…" — "ne"(94) + "me"(82='m' banked) + finite verb in correct French order.
- This requires **06@1184/@1355 as verb-stem**: the finite 3pl "-ent" ending on the "ment-" stem (82='m' as stem-final letter) = "mentent". It does NOT require trigram-internal-'ent'.
- This is exactly ent-06's promoted F2 frame (@1182-1185 "94-82-06-06" = "ne mentent", CLEAN). The boundary parse is therefore **consistent with the standing ent-06 promote**.
- The trigram-internal-'ent' reading (crowd4 conditioning: 06@[580,1183,1354] inside 94-82-06) belongs to the rival "…lement" word-composition, which must additionally override ent-06's demonstrated "ne mentent" frame — a further burden the rival does not meet.

## Per-clause pass/fail

1. Host at 59@1178 or 62@1349: **FAIL (no host)** — 59="est", 62="il" under all standing values; neither spells sou-/en-/re-. The bar's (2) branch fires.
2. 'nement'-host recorded as count-level observation: **PASS** — 5-gram x2 (@1180, @1351), trigram x3 with "ne mentent" standing parses; not a parse; lever composition untouched.
3. 06 value required by the clause-2 boundary parse: **STATED** — verb-stem (finite "-ent", "mentent"), consistent with ent-06's promoted F2 frame; trigram-internal-'ent' is the rival's requirement, not the boundary parse's.

## Adverses answered

- "bare 'levement' is not standard French": ANSWERED — the rival itself requires the pre-syllable; the adverse supports the claim (the composition under test is "…levement", never bare "levement").
- "the rival needs the unattested pre-syllable": ANSWERED — tested at both named loci under every standing value (granted, provisional, battery-promoted); unattested. Reinforced by the intervening-token structure (37@1179, 48@1350).
- "red-team denied 94='en' co-value (LEAD-held)": ANSWERED — consistent with the 94="ne" promote used throughout; the trigram sites parse as "ne mentent" under standing values, so the syllabic-'en' route to "…lement" via 94 is closed at battery grade. (Sub-lexical 94='e' remains open in principle — "prenne" proves syllabic use — but is undemonstrated here and needs the missing pre-syllable anyway.)

## Verdict: PROMOTE (finding grade)

All three bar clauses are satisfied (clause 1's no-host outcome is the claim's expected result per the bar's own (2) branch); all three adverses are answered. The "…levement" rival at @1180/@1351 **stays undemonstrated at battery grade**: no standing value of 59@1178 ("est") or 62@1349 ("il") can host the missing pre-syllable, and the rival would additionally need to override ent-06's demonstrated "ne mentent" frames.

Scope: this promotes the negative finding only — no value or class is promoted or killed. The lever-77-78 NULL (composition underdetermined) is untouched; the "…lement" word-composition is closed at battery grade unless red team re-opens it.

Caveats: canonicality (§7 — 68 of 70 row offsets unvalidated; all @ positions on the canonical stream). No red-team verdict contradicted or downgraded; §7 intact.

## Follow-ups

None required (promote, not null). Optional P4 note for the supervisor: `lement-37-48-intervene` — test 37@1179/48@1350 as part of any future revived "…lement" composition (they intervene between the candidate hosts and 77); only re-open if red team re-values 59 or 62.
