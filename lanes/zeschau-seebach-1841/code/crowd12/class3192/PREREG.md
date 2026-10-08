# PRE-REGISTRATION — CLASS-31-92 executor, round 12 (WO3 + WO4)
**Executor:** CLASS-31-92
**Timestamp:** 2026-10-07 (written before any round-12 decision computation;
only standing/recorded numbers consulted: repaired parse facts, round-11
`results_r11.json` 31/92 entries, NOTES.md F77/F82/N52, STATE.md round-12 WOs)

**Task:** STATE.md round-12 WO3 (31-class battery) + WO4 (92-class battery).

## Standing record (not re-derived)
- Repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json`); positions
  per `code/crowd4/REINDEX.md`. Byte-verify gate: N=1847; @1519 window =
  [11,91,67,8,31]; @902 window = [16,92,67,16,88].
- Board: GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
  provisional 87=ce, 64=qui, 96=par, 59=est (ISLET-10 conditioned),
  77="le" (provisional-conditioned); leads {93,8}="l'", 00="pour" (strong),
  06="ent"-iff-82 (ISLET 3), 94="ne" (provisional-strong).
- Round-11 recorded (results_r11.json, F82): 31 contested leaning verbal —
  nominal: 11→31 ×1 (GT); verbal: 64→31 ×2 (qui-prov), 31→29 ×1 (stem+er),
  31→11 ×1; n(08→31)=3; **prereg flaw caught**: 08="l'" article/pronoun-ambiguous,
  cannot license nominals unconditionally. 92 contested infinitive/noun —
  verbal: 00→92 ×6 (pour+inf), 46→92 ×1 (que-GT); nominal: 11→92 ×3 (GT).
- No re-litigation of settled kills (STATE.md round-12 WO9 list). The @1519 /
  @902 nulls recorded the flaw; this battery REPAIRS the named flaw (WO3/WO4
  explicitly order it) — not re-litigation.
- No manual-tiling bearing counts (F59 ban). All counts programmatic.
- No status changes applied by this executor — recommendations only; red team
  adjudicates.

## Era instrument (upgraded per work-order standing flags)
- **Rate/attestation bars use the clean French pool, NOT Nesselrode-v8-alone.**
  Pool = 14 French files of `code/side-period/corpus/`:
  nesselrode-v7/v8/v9/v10, pozzo-di-borgo-correspondance-v1,
  guizot-memoires-t1/t2/t3-gutenberg, guizot-memoires-t5-t6,
  talleyrand-memoires-v1, revue-deux-mondes-1841-q1/q2/q3/q4.
  German/English files (allgemeine-zeitung ×15, metternich-papiere v4/v6,
  adb-zeschau, levant-correspondence) EXCLUDED for French rates.
  Pool size: **3,212,595 tokens** (lane tokenizer; counted at instrument setup).
- Tokenizer (lane verbatim): lowercase; `[’‘`]` → `'`; elision pre-split
  `\b([a-zàâäéèêëîïôöùûüç]+)'([a-zàâäéèêëîïôöùûüç]+)` → `\1' \2`;
  findall `[a-zàâäéèêëîïôöùûüç]+'?`.
- **v8-VOID rule (F77):** Nesselrode-v8 OCR word-splits are VOID as French.
  No attestation or zero may rest on v8-only OCR text; pool-wide zeros required;
  every counted hit constituency-read (small-n: all; large-n: sampled).
- Legs below are ATTESTATION-kind (≥1 genuine hit) or ZERO-kind (pool-wide 0
  with constituency-read of near-misses), never v8-alone rate bars.

## Battery B31 — 31's class (WO3, route (a): 08-disambiguation)
Route (b) pre-check (parse facts): second GT-anchored nominal contact would need
another 11→31 (n=1, @1516 only) or 46→31 (n=0). **Route (b) unmeetable on the
repaired parse — recorded, not attempted.** This battery runs route (a).

### The disambiguator (pre-registered)
08="l'"-lead is article/pronoun-ambiguous. Disambiguation rules use ONLY the
predecessor of 08 — never 31's class, 31's successor, or any 31-derived value
(no leak: inference flows pre(08) → 08's role → 31's class, strictly one-way).

- **D-ce:** pre(08)=87 ("ce"-provisional, C1). French grammar: demonstrative/
  subject "ce" never precedes article+noun (*"ce l'homme" ungrammatical — "ce"
  is itself a determiner); "ce l' X" ⇒ 08=PRONOUN (object clitic), X=verb
  ("ce l'empêche" — grammatical, diplomatic-register clean pending frenchman).
- **D-que:** pre(08)=46 ("que"-GT). "que" (conjunction/relative) never precedes
  article+noun; "que l' X" ⇒ 08=PRONOUN, X=verb.
- **D-ne:** pre(08)=94 ("ne"-provisional-strong, C1). "ne" precedes the verb
  complex; "ne l' X" ⇒ 08=PRONOUN, X=verb (diplomatic register never drops "ne").
- **D-qui:** pre(08)=64 ("qui"-provisional, C1). Subject-relative "qui" must be
  followed by a verb; "qui l' X" ⇒ 08=PRONOUN, X=verb.
- **One-sidedness (disclosed):** no pre-registered rule forces 08=article
  ("de/à/pour/et/veut l'" are all ambiguous; no clause-initial 08 in parse).
  The disambiguator can only prove PRONOUN. A NOMINAL verdict via this route is
  impossible by construction — recorded, not a null against nominals generally.
- **qui-relative leg (standing, re-verified):** 64="qui"-provisional (C1);
  "qui 31" ⇒ 31=finite verb (relative "qui" is clause subject). Independent of
  the D-rules (different anchor, different windows).

### Census plan (programmatic, repaired parse)
1. Byte-verify gate (N, @1519, @902 windows).
2. All 18 08-positions: apply D-ce/D-que/D-ne/D-qui; report hits per rule.
3. All 8 31-positions ±2: classify each window's 31-licensor contact:
   disambiguated-verbal (D-rule pronoun ⇒ 31=verb; qui-relative ⇒ 31=verb),
   disambiguated-nominal (none expected — no article-forcing rule),
   ambiguous (pre ∈ {08-undisambiguated, 11, 61, 48}).
4. Era leg E31-1 (attestation): n(("ce","l'")) in French pool ≥ 1; report n +
   3 constituency-read examples (all must be pronoun+verb by grammar).

### Verdict rule B31 (mechanical)
- 31=VERBAL iff ≥2 disambiguated verbal contacts from DISTINCT 31-windows
  (one window = one contact; shared provisional conditionals marked C1).
- 31=NOMINAL iff ≥2 disambiguated nominal contacts.
- Else NULL (contested; leaning recorded, not a verdict).
- Recommendation only. Expected shape (NOT a decision): verbal candidates
  @1489 (D-ce), @338/@1647 (qui ×2); nominal candidates 0.

## Battery B92 — conditioned polyvalence (WO4)
### Conditioning variable (pre-registered): pre(92)
Three arms; all other pre (40, 98, 16, 84×2, 83, 30, 13, 31, 81) → UNCLASSIFIED
(recorded, never forced).
- **POUR-arm:** pre=00 ("pour"-strong-lead). "pour" governs infinitives AND nouns
  — the contest lives here.
- **LA-arm:** pre=11 (GT "la"). Article+noun (92=NOUN) vs pronoun+verb
  (92=verb) — standing ambiguity, recorded.
- **VERB-arm:** pre ∈ {94 ("ne"-prov-strong, C1), 46 ("que"-GT)} ⇒ 92=finite VERB
  (recorded third reading; not part of the INF/NOUN decision).

### Signatures (pre-registered; grammar facts, not fitted counts)
- **INF-lean:** suc(92)=29 — "pour [stem]-er" = pour+infinitive. LEAN only:
  noun-in-"-er" alternative named ("pour [boulanger]").
- **NOUN-strong:** suc(92)=64 ("qui"-provisional, C1) — *"pour [INF] qui" is
  ungrammatical in French, period; "pour [NOUN] qui [verb]" (relative) is live.
  A POUR-arm window with suc=64 forces 92=NOUN.

### Decision tree (pre-registered)
1. **H-pre** (predecessor-only): INF-arm = POUR (n=6), NOUN-arm = LA (n=3).
   GRANT H-pre iff: ≥2 POUR-arm windows show INF-lean AND ≥1 LA-arm window
   shows NOUN-strong AND **zero cross-signatures** (no suc=64 in POUR-arm;
   no suc=29 in LA-arm). **Falsifier:** any cross-signature ⇒ H-pre REFUTED
   as stated (F33 falsifiability: the conditioner, not polyvalence, fails).
2. **If H-pre refuted → H-presuc** (pre=00 ∧ suc; WO's "predecessor/successor
   class" licenses the two-level conditioner):
   - NOUN-islet: pre=00 ∧ suc=64 ("pour [N] qui"). INF-islet: pre=00 ∧ suc=29
     ("pour [stem]-er").
   - GRANT-with-islets iff: both islets non-empty on DISJOINT windows; no window
     shows both signatures; unclassified windows recorded not forced; each islet
     carries its era leg (E92-1/2/3); no double-counting (conditioner=pre,
     signatures=suc — disjoint positions).
   - **n_eff bar:** islets below ISLET-3's n=4/n_eff=3 precedent cap the
     recommendation at **FENCED** (hypothesis + named missing legs for round 13),
     never GRANT.
3. Else **NULL** (92's class stays contested).

### Era legs B92 (French pool, lane tokenizer)
- E92-1 (zero-kind): enumerate ALL ("pour", *, "qui") trigrams pool-wide;
  constituency-read every *; assert ZERO infinitives (supports *"pour INF qui").
- E92-2 (attestation-kind): n("pour", NOUN, "qui") ≥ 1 from the E92-1 read —
  the noun-islet frame is live French; report n + examples.
- E92-3 (attestation-kind): n(("pour", w) with w endswith "er") — "pour"+INF
  frame live; report n (frame grammaticality uncontroversial; light leg).

### VERB-arm mini-bar (recorded)
pre∈{94,46} → 92=finite verb: legs = 94="ne" prov-strong (C1) / 46="que" GT;
n=3 (@66, @1550, @1453). Recorded as third conditioned reading; does not
interact with the INF/NOUN decision.

## What counts / gates
- Census-fidelity gate first: N=1847; @1519=[11,91,67,8,31]; @902=[16,92,67,16,88];
  n31=8, n92=22, n08=18. HALT on drift.
- Leg supplied: pre-registered bar passes on repaired parse + French pool.
- Clean nulls name the exact missing leg. FENCED names the replication legs.
- All status changes are RECOMMENDATIONS for red-team adjudication.
