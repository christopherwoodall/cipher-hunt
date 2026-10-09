# Battery verdict: left-88-02-88-307

## Bar (verbatim from battery-queue.json, pre-registered)

"A prepositional or clausal construction at @304-306 selects between \"chaque fois que\" and \"une fois que\" independently of the continuation; else no decision."

**Restated as numbered pass/fail clauses:**
- **C1:** @304-306 ("88 02 88") parses as a licensed prepositional or clausal construction under standing values, with byte evidence.
- **C2:** that construction selects one @307 reading ("chaque fois que" = habitual vs "une fois que" = completed-tense) independently of the continuation.
- **Else-arm:** no discrimination → NULL, fenced with stated cause.

## Method
- Read BATTERY-PROTOCOL.md first; lock `locks/left-88-02-88-307.lock` created on start (agent 499619c1, 2026-10-09T10:41:10Z), deleted on completion.
- Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py` (pair up from row offset, drop trailing odd digit). Verified: **1,847 pairs, 96 types**.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- @-offsets are 0-based pair indices.

## Window-level evidence (byte-exact)

Locus, row a2_04 (byte-verified):

| @ | 298 | 299 | 300 | 301 | 302 | 303 | 304 | 305 | 306 | 307 | 308 | 309 | 310 | 311 | 312 | 313 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| g | 40 | 97 | 86 | 91 | 18 | 89 | **88** | **02** | **88** | **20** | **17** | **46** | **84** | **24** | **37** | **78** |

- @304-306 = "88 02 88". @307-311 = "[20] fois(17, promoted) que(46, pencil GT) on(84, A15) [24]" — the @307 discriminator window.
- **"88 02 88" is a stream hapax** (1/1,845 trigram positions). Both component bigrams are hapax: "88 02" = 1x (@304), "02 88" = 1x (@305). Zero repetition leverage.
- **"17 46" ("fois que") is 1x stream-wide** (@308). No temporal-frame family exists; the selection question lives or dies at this single window.

Distributional profiles (re-derived):
- 88: n=23. Successors: 77×3, 11×2, 24×2, then 17 singletons (incl. 02×1, 20×1). Verb class (battery PROMOTE); **value open**.
- 02: n=17. Predecessors: 01×3, 64(qui)×2, 84(on)×2, 11×1, 88×1, ... Successors: 79(tout)×2, 24×2, 00(pour)×2, 26/88/53/58/50/21/97/55/70/62/09 ×1. **Class and value open.**
- 20: n=15. "20 17" occurs only at @307. **Value open** ("fois" killed; det-20-value returned null 2026-10-09).

Standing values used: 17=fois (promoted), 46=que (pencil GT), 84=on (A15), 88=VERB class (battery PROMOTE, value open), 79=tout (A5), 00=pour (A9), 67=et/veut sole polyvalence.

## C1: no licensed construction — FAIL

**Prepositional arm:** requires 02 as a preposition. 02's successor profile is hostile: 00="pour"×2 ("[prep] pour" ungrammatical), 24×2 (verb-shaped), 79="tout"×2. No independent 02-preposition frame exists stream-wide. No licensed preposition value for 02 at any grade. DEAD.

**Clausal arm:** "[88] [02] [88]" with 88 verb-class. Candidate readings:
- "[88-V-finite] [02] [88-V-finite]": two adjacent finite verbs — ungrammatical.
- 02 as verb-object between two verbs: 02's object-hood unnamed; "V [obj] V" with no conjunction/relativizer — ungrammatical.
- Relative/interrogative: no wh-word present (02 ≠ 64=qui, 46=que).
- 02 as conjunction ("et"): 67=et is the standing grant; 02's conjunctionhood is unnamed and unlicensed. Even arguendo, "[88-V] et [88-V]" = VP coordination, which carries no temporal-frame selection (see C2).
DEAD on all arms. Both 88 and 02 are valueless at standing grade, so no construction can be licensed with byte evidence without inventing values.

## C2: selection is impossible independently of the continuation — FAIL

Even under a hypothetically licensed @304-306 construction, selection would require deciding 20's value ("une" vs "chaque") — 20 is valueless at standing grade (det-20-value null), and no French mechanism makes a @304-306 construction determine the determiner of a following "fois que" clause. The discriminator's own premise ("une fois que" needs completed-tense verb; "chaque fois que" habitual) makes the reading depend on 24's tense/form — i.e. on the continuation — directly contradicting the bar's "independently of the continuation" requirement. 24's tense/form is unresolved at standing grade (R18-008: 24="faire" rejected, demoted to conditional lead; R17-009 finite-verb class stands).

## Per-clause results
- **C1: FAIL** — no licensed prepositional or clausal construction (hapax; 02-prep hostile; clause arms ungrammatical; both heads valueless).
- **C2: FAIL** — selection would need 20's value (open, det-20-value null) and 24's tense (open, R18-008); cannot be independent of the continuation.
- **Else-arm: TAKEN** — no decision; the window is fenced with stated cause.

## Verdict: NULL

Not kill-grade: no window forces the claim false — the claim is conditional and the locus is a hapax; a kill would require named values to exclude every construction. §7 intact. No standing/red-team verdict contradicted or downgraded. Canonical-stream caveat stands (row a2_04 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-02-prep-sweep` (P3) — test 02 for preposition class across its 17 windows; a licensed 02-prep re-opens the prepositional arm of this claim.
2. `frame-307-rightedge-gated` (P4) — gated re-test of the @307 discriminator once 24's tense/form resolves (red-team venue); the reading selection inherently depends on the continuation.
3. `hapax-88-02-88-lettertier` (P4) — letter-tier composition test of the "88 02 88" hapax once letter values name for 88/02; re-opens the boundary question.

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-left-88-02-88-307.md` (this file).
- Queue: `left-88-02-88-307` queued → verdict/null via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated post-write.
- Lock `left-88-02-88-307.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
