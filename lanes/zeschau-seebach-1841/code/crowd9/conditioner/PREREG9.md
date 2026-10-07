# CONDITIONER round-9 — PRE-REGISTRATION (written BEFORE any new computation, 2026-10-07)

Owner: conditioner (islet-registry owner). Guardrails: no re-derivation of
banked windows (F61/F62/F63 adjudicated); no manual-tiling bearing counts
(T7 rule); era rates from Nesselrode v8 (`code/side-period/corpus/`:
despatches_primary = nesselrode-v8.txt + levant-correspondence-1841-p3.txt,
N≈369,589 wc; diplomatic_all = all corpus *.txt); elision-split tokenizer
per F53; positions 0-based repaired 1,847-pair starts.

## (1) 84 — classify the 9 still-unclassified windows

Round-8 left 9 residual: @391 (91-84-73), @788 (65-84-06), @412 (53-84-51),
@1021 (53-84-92), @857 (48-84-02), @1501 (74-84-33), @1189 (06-84-59),
@1290 (17-84-59), @1418 (32-84-79). The 4 EN-EXTENSION windows
(@154/@1151 66-84 ×2, @276/@1378 89-84 ×2) are F62-GRANTED — no re-derivation.

Apply round-8's rules as re-stated here:
- C-EN-EXT: joins "en" islet iff (i) pre grammatical with "en", (ii) suc
  doesn't break it, (iii) recurrence n≥2 same pre or n≥2 same pre-class or
  independent era-rate leg. Singleton grammatical reads → "consistent-with-en,
  n=1" (residual-with-lean, NOT classified).
- C-NOUN-EXT: fires only for pre with independent article reading ≥2 legs
  (expected: does not fire).
- C-WORD: full trigram matches a banked formula/word reading (explicit legs).
- C-RESID: stays UNCLASSIFIED.

New predecessor classes need recurrence — singletons do not extend islets
(round-8 prereg, still binding).

Banked falsifiers: F62's re-scope is final — @310/@473 OUT (qu'en en
era-0); @1665 stays fenced-adverse; 84=noun islet RESCOPED (not one
era-rate masculine noun; identity NULL) — the registry records it as
RESCOPED/WITHDRAWN, not as an active conditioned reading.

## (2) Test qui-96-43 ×2 as formula with 96=verb-stem

Windows: 64 96 43 87 01 ×2. F18 cites @341/@1024 (pre-repair indexing;
re-derive exact positions on the repaired stream FIRST — @341 < 748
unchanged, @1024 ≥ 773 → +1 = @1025; verify by search, do not trust the
shift blindly). 96=verb-stem conditioned LEAD (pre==64 & suc==47, n_eff=1,
F55/F63); 87=ce provisional; 43="me" WEAK (round-6 downgrade); 01="est"
CONFIRM MEDIUM.

Bar (pre-registered):
- CONFIRM as "«qui [96=verb-stem] [43] … ce» formula": (a) both windows
  share a parallel wider context (≥5 groups identical or
  cipher-homophone-variant) BEYOND the 5-mer itself; (b) era corpus attests
  «qui [verb] X» with X = 43-candidate ("me" and ≥1 rival, e.g. 43="que"?
  no — 43's banked rivals) at nonzero rate; (c) 43's reading is the SAME
  in both windows. All three → recommend CONFIRM as formula (values of
  96-stem/43 still unidentified — formula status ≠ value status).
- STRENGTHEN: (a) holds + (b) holds for one 43-candidate only → lead.
- HOLD/REFUTE: if (a) fails (no parallel wider context) → formula stays
  FORMULA-UNCONFIRMED (recurrence alone, n=2, n_eff=?); if era «qui [V] me»
  is era-0 in the diplomatic corpus → 43="me" suffers an adverse datum
  (bank it, do not re-litigate 43's WEAK status elsewhere).

Note: 96=verb-stem's banking window (@149: 64-96-47) has suc==47="ce" —
here suc(96)=43. The verb-stem reading of 96 does NOT require suc==47;
the conditioning rule (pre==64 & suc==47) is the banking context only.
Do NOT re-litigate F55's rule.

## (3) Test «qui le [verb=84-59]» ×2

Windows @1447, @1803 (64-77-84-59; F62-referred). 77="le"
provisional-conditioned (pronoun reading under test); 59="est"
provisional (as WORD — banked). The new hypothesis needs 59-as-VERB-SYLLABLE,
which is UNBANKED and in tension with 59="est"-as-word: this is itself a
conditioned-polyvalence candidate (59 word vs 59 syllable).

Bar (pre-registered):
- STRENGTHEN (max achievable this round — the verb's identity is
  unidentified, so CONFIRM of the full reading is out of reach): (a) both
  windows' wider contexts (≥±5) are grammatical under «qui le [84-59=verb]»
  with no break; (b) era corpus: «qui le X» trigram scan — count cases
  where XY after «qui le» is a single bisyllabic verb (X=first syllable,
  Y=second) vs noun+"est" vs other; the verb-frame must be the DOMINANT
  parse (≥50% of «qui le X Y» tokens where X is a plausible 84-shape,
  i.e. short frequent first syllable); (c) falsifier BANKED up front:
  if era «qui le [bisyllabic verb]» requires verbs whose second syllable
  = /ɛst/ ("-este" family: contester/détester/manifester/rester…), check
  those verbs' diplomatic-era rates — if the only candidates are
  era-rare/absent, the reading FAILS (adverse datum banked); (d) 59-word
  vs 59-syllable: enumerate ALL 59 windows (n59=?) and test whether a
  clean conditioning split exists (word-"est" vs verb-final-syllable
  contexts) — if no split is statable, the reading stays
  HYPOTHESIS-INTERNAL (needs 59 conditioned polyvalence, unbanked).
- REFUTE: if (b) shows noun+"est" or other frames dominate AND no
  verb candidate clears (c) → bank the adverse datum; the 5-gram
  64-77-84-59 ×2 returns to OPEN (unresolved residual).

Do NOT claim "59 is a verb syllable" — only whether the frame test passes.

## (4) 86's identity — fresh battery (B3 dissolves iff 86 is que-family)

F40 M1 (F33-grade, red-team ACCEPT): 00→86 ×12 vs 00→06 ×0; 86 never in
06's finite frames (0/14); working hypothesis 86=verb-stem-class allomorph
of 06 (unestablished). Ratelane caveat: B3's numerator (00→46 ×4) assumes
86∉que-family; if 86 were que-family, B3 dissolves (16/55≈0.29 vs era 0.31
per ratemodel note — verify the era number from the French-only pool).

Pre-registered test battery (each leg independent; need ≥2 to NAME):
- L1 UNIGRAM: P(86)=n86/1847 vs era P("qu'")/P("que") and vs era
  verb-stem-class rate (informative only).
- L2 QUE-FRAME: 00→86 ×12 — test «pour qu'» under both readings: era
  P("qu'"|"pour") (elision-split) vs 12/55=0.218; grammaticality of the
  SUCCESSORS (86→?: all 12 successor values — under "qu'" they must start
  vowel-initial words; 29="er"-GT successors like @1378 00-86-29 are
  decisive: «pour qu'er…» = vowel-initial "er…" stem? vs 86=verb-stem +
  29="er" infinitive ending «pour [V]er» — the two readings make OPPOSITE
  predictions at 86-29 windows; count how many of the 12 have suc=29).
- L3 FINITE-FRAME ABSENCE: 86 never in 06's finite frames (→11 ×4, →77 ×6,
  →00 ×4) — under "qu'" this is EXPECTED (qu' never precedes those),
  under verb-stem it needs the mood story; score both.
- L4 que-FAMILY PARITY: 46=que GT — compare 86's full
  predecessor/successor profile to 46's (Jaccard or exact-test on the
  top-k contexts); 86≈46 supports que-family.
- L5 ELISION TEST: if 86="qu'", its successors must be vowel-initial
  stems in ≥10/12 windows (era "qu'" rate ≈ 1.0 by definition); find the
  successor values' banked/provisional identities and check.

Verdict ladder: ≥2 legs for que-family → 86=que-family LEAD (recommend;
B3 DISSOLVED — red team rules); ≥2 legs for verb-stem → F40 working
hypothesis strengthened (B3 stands); split → HONEST NULL (both recorded).

## (5) Confirm 66/89 class readings (84-extension dependencies)

The 84 islet's pre∈{66,89} arm (F62-GRANTED, conditional) depends on 66/89
being classes after which "en" is grammatical.

- 66: «pour 66» ×7 (verify count on repaired stream); "pour" never takes
  subject pronouns → 66 ∈ {noun, infinitive}-class. Battery: (a) 66's full
  predecessor profile — is «pour» the dominant pre (≥5/7)?; (b) 66's
  successors — noun-class vs infinitive-class signature (era P(N|pour),
  P(V-inf|pour) from despatches_primary); (c) 66-84 ×2 windows' wider
  contexts under «[pour] [66] en [V]» (cf. round-8 «ce que le roi en dit»).
  Confirm as NOUN/INFINITIVE-CLASS iff (a)+(b) or (a)+(c) hold.
- 89: round-8's three positional legs (77-89 ×2 «le [89]», 29-89 ×5
  infinitive-object, 89-48 ×3 «[89] ne» subject) + 29-89-84 ×2. Re-verify
  counts on the repaired stream (no re-derivation of the argument);
  confirm NOUN-CLASS iff all three legs re-verify AND no adverse
  (e.g. a 89-window breaking noun-class) is found in a full 89-window
  census.

Any window breaking the class → bank as adverse datum, do not force.

## (6) 67 fork bookkeeping

67 agent owns classification; I own the registry entry. Current banked
state (from lane notes, NOT re-derived): 29/38 classified (et=18,
veut=11, open=9), F33-grade rules R_et4/5/6, fork SUPPORTED, @1248
NEITHER-class fenced counterdatum (F63). Registry records this verbatim;
any new 67 windows touched by my tests (none planned) get flagged to the
67 agent's file.

## Verdict ladder for this round

- Registry entries carry: conditioning rule (exact), status, n/n_eff,
  supporting windows (positions), banked falsifier + status, leftover
  unclassified windows.
- Recommendations are PACKAGES for red-team ruling; I promote nothing.
- Honest NULLs are first-class results.
