# 84-CONDITIONER round 8 — PRE-REGISTRATION (written BEFORE any new computation, 2026-10-07)

Work order 4, STATE.md round-8. F53 banked: 84="en" iff pre∈{46,94,82} (LEAD,
n=4, n_eff=3, @1665 adverse fenced); 84=noun iff pre∈{77,11} (LEAD, n=8,
n_eff=6, zero adverses, identity NULL); 13 windows FREE (pre∉{46,94,82,77,11}).
This is partial F33-grade polyvalence, NOT a partition — no forced partition.

## (a) Classification rules for the 13 free windows

FREE windows (0-based repaired starts): @154 (66-84-26), @276 (89-84-91),
@391 (91-84-73), @412 (53-84-51), @788 (65-84-06), @857 (48-84-02),
@1021 (53-84-92), @1151 (66-84-02), @1189 (06-84-59), @1290 (17-84-59),
@1378 (89-84-92), @1418 (32-84-79), @1501 (74-84-33).

- **C-EN-EXT**: a free window joins the "en" islet iff (i) pre is a word after
  which "en" (pronoun or preposition) is grammatical in diplomatic French, AND
  (ii) the successor does not break the "en" reading, AND (iii) the pattern
  recurs (n≥2 same pre, or n≥2 same pre-class) or an independent era-rate leg
  supports it. Singleton grammatical reads → "consistent-with-en, n=1"
  (residual-with-lean, NOT classified).
- **C-NOUN-EXT**: a free window joins the noun islet iff pre carries an
  independent article reading (le/la/les/un/des) with ≥2 legs of its own.
  No free pre currently has one → expected to NOT fire; any fire is a new
  claim needing its own battery.
- **C-WORD**: classify by a banked formula/word reading when the full trigram
  matches one (e.g. 06=verb-stem … 59="est"), with explicit legs cited.
- **C-RESID**: no rule fires cleanly → window stays UNCLASSIFIED (honest
  residual). Partial polyvalence is an acceptable terminal outcome.
- Guardrail: no re-derivation of F53's banked windows; the 13 free windows are
  the only classification targets. New predecessor classes need recurrence —
  singletons do not extend islets.

## (b) Noun-identity bar — name ONLY on ≥2 INDEPENDENT legs

Noun-class windows: @146 (77-84-29), @260 (77-84-74), @1058/@1764 (77-84-09 ×2,
n_eff=1), @1447/@1803 (77-84-59 ×2, n_eff=1; extends to 64-77-84-59 ×2 per F42),
@1485 (77-84-24), @1620 (11-84-78). 59="est" provisional, 24="en" STRONG,
29="er" pencil GT, 74="te" lead, 78="me"-syllable LEAD / "vrai" lead.

Candidate legs (independent = no double-counted windows or corpus cells):
- L1 UNIGRAM: era unigram rate of candidate noun ≈ P84 = 25/1847 (in-band ≤2×,
  diplomatic corpus, elision-split tokenizer per F53).
- L2 "le N est": "qui le N est" / "le N est" attested in diplomatic corpus
  (covers @1447/@1803 ×2).
- L3 "le N en": "le N en" attested with matching syntax (covers @1485).
- L4 SEGMENT: 84 = the noun's sole syllable (pre=77="le"/11="la" directly
  adjacent; successors 59/24 are words, so the noun ends at 84).
- L5 CORROB: "la N 78" (@1620) or "le N 09" (×2) corroboration in corpus.
Name the noun iff ≥2 of L1–L5 hold; otherwise BOUND it (candidate set with
per-candidate surviving legs) or leave NULL honestly.

## (c) «que 84 24» adjudication (@310, @473 — both 46-84-24, n_eff=1)

- Q1: 24's identity at these windows. 24="en" STRONG (F31) globally; check
  local consistency (no adverse at @311/@474).
- Q2: era "en en" bigram rate (elision-split tokenizer; "qu'en"→"qu en") on
  the diplomatic corpus (despatches_primary = nesselrode-v8 + levant-1841-p3;
  diplomatic_all as secondary).
- Q3: if "en en" is ABSENT (or rate ≈ 0) in diplomatic French → "qu'en en"
  is an adverse datum for the en-reading at @310/@473 → en-islet support
  reverts to @167 (+fenced @1665) → recommend DEMOTION of the en-islet
  (or fencing of the two windows), per B2's adverse-datum rule.
- Q4: test rival readings at @310/@473 ("que [noun] en", 84=other) — only to
  bound, not to force a reclassification.

No status change merges without red-team ruling (standing).
