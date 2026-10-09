# Battery report: `nom-97-526-class`

Date: 2026-10-09. Worker: battery worker (subagent 42f932e0).

## Bar (verbatim, pre-registered)

> "promote noun-97 from the @525 window alone."

Restated as numbered pass/fail clauses (before testing):

- **C1:** The @525 window (0-based, row a3_00) parses under noun-97 with zero ungranted assumptions besides noun-97 itself, at battery grade — i.e. the parse is unblocked (no 13-class dependency as at @566).
- **C2:** This warrants promoting noun-97 (the class).

Index note: 0-based @525 = 1-based @526 (the brief's "@525" follows the inf97-526-vs-567 convention where the brief's 1-based @526 = 0-based @525). All @-offsets below are 0-based unless marked 1b.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`); asserts held (1,847 pairs, 96 types, crib "la premiere" pair-aligned). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Standing premises adopted (not re-litigated):

- 81 = nominal at @524, window-level (battery PROMOTE, `nom-97-526-adverb`, 2026-10-09); adverbial-81 dead at this window; R19-123's global noun-81 fence untouched.
- 47 = 'ce' (promoted, A4); 59 = 'est' (provisional); 37/32/42 predicative (A1).
- 00 = 'pour' (granted, A9); 86 INF-class (A9); 46 = 'que' (banked).
- 97 infinitive-class (battery PROMOTE, class-level, `frame-97-profile`, 2026-10-08); 97 finite-verb KILL (battery `val-97-verb-test`, 2026-10-09); INF/NOM tie preserved (battery NULL, `val-97-verb-test`).
- §7: 67 sole true polyvalence; R24 adopted.
- Canonical-stream caveat stands (row a3_00 offsets unvalidated).

## Window-level evidence (byte-exact on the repaired stream)

**W1** (row a3_00), 0b@520–532:
`91 @520 | 77 @521 | 06 @522 | 55 @523 | 81 @524 | 97 @525 | 47 @526 | 44 @527 | 59 @528 | 37 @529 | 64 @530 | 26 @531 | 32 @532`

**C1 test — the noun-97 parse at @525:**

Under noun-97, W1 reads "[81-nominal] [97-noun] ce(47) [44] est(59) [37]":
- "[81] [97-noun]" — appositive NP (81-nominal at @524 is battery-grade, window-level; the "55 81" ×6 collocation re-verified in-session, n(81)=14, predecessors 55×6/77×4/43/98/39/08×1).
- "ce(47) [44] est(59) [37]" — the A1 copula shape ("ce [44] est [predicative-37]"), adopted from `nom-97-526-adverb`.
- The INF rival at this window is strained/closed: the infinitive-topic reading ("Partir, c'est…"-shaped) was conditional on adverbial-81, which is dead at @524 (adopted, `nom-97-526-adverb`).

Ungranted-assumption audit: 81-nominal (granted at battery grade, window-level), 47/59 (promoted/provisional), 37 (A1 frame), 44 (unvalued but in a licensed copula-frame position — adopted from the sibling's clean parse). The sole ungranted assumption is noun-97 itself. No 13-class dependency (unlike @566). **C1 PASSES.**

**C2 test — can @525 carry a class promote?**

A class-level noun-97 promote must survive the 10-window census. Re-derived n(97)=10 at 0b [2, 94, 288, 299, 525, 566, 588, 751, 1412, 1823] (matches `frame-97-profile`).

The tally is symmetric (adopted from `val-97-verb-test`, re-verified in-session):

- INF clean: the four "pour [97]" windows (@2/@288/@588/@1823) + the @1823 "pour 97 pour 86er" parallel (86 in explicit infinitive form). 6 legs.
- NOM clean: @525 (appositive NP + copula, this battery), @94 ("[81] [97-N] que [relative]"), @566 ("[80-V] [97-N]" object), @1412 ("[16-INF] [97-N]" object). 4 legs.
- Unforced: @299 ("40 97 86" hapax, fenced), @751 ("02 97 40").

Three blockers for a class promote from @525 alone:

1. **Standing class-level verdict.** `frame-97-profile` holds PROMOTE (class-level): 97 is infinitive-class, on the pour-windows + the @1823 parallel. Promoting noun-97 as a class would directly contradict it. Never downgrade an existing verdict.
2. **The article discriminator (re-verified in-session).** 00's successor census: bare takes are exclusively verb-frame cells (86×12, 33×8, 92×6, 66×7, 97×4); 00's nominal takes are article-mediated (00→11×4, "pour la…"). Zero 00→bare-noun windows stream-wide. This distributional pattern (4/4 vs 4/4) disfavors NOM at the four pour-windows. A one-window class promote does not address it.
3. **One window cannot resolve a 10-window tie.** The INF/NOM tie is genuine at battery grade (`val-97-verb-test` NULL, preserved). The class question is red-team venue.

**C2 FAILS.** The @525 evidence is real and strengthens the NOM arm, but it does not warrant a class promote.

## Per-clause verdict

1. C1 (@525 parses cleanly under noun-97, unblocked): **PASS.**
2. C2 (class promote warranted): **FAIL** — blocked by the standing class-level infinitive verdict, the 4v4 symmetric tie, and the pour-window discriminator.

## Verdict: NULL

Noun-97 cannot be promoted as a class from the @525 window alone. The window's NOM parse is clean, unblocked, and battery-grade (C1), and it strengthens the tie's NOM arm — but the class question stays with the red team. The INF/NOM tie survives exactly as before. No standing or red-team verdict is contradicted or downgraded (`frame-97-profile`, `val-97-verb-test`, `nom-97-526-adverb`, `inf97-526-vs-567`, `noun-97-568` all adopted as premises); §7 intact; no polyvalence declared; canonical-stream caveat stands.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `pour-97-noun-discriminator` (P3) — Formal battery test of the article discriminator: census 00's government for bare-noun takes at battery grade. Bar: if 00's bare takes are exclusively verb-frame cells (86/33/92/66/97) with nominal takes article-mediated (00→11×4), the pour-windows stay INF-favoring; a single verified 00→bare-noun take collapses the discriminator and gives NOM-97 four windows. The sharpest class-level discriminator for the tie.
2. `redteam-97-tie-adjudication` (P2) — Red-team input package for the INF/NOM tie: the leg tally (INF 6 legs: pour-windows ×4 + @1823 parallel + que-valency; NOM 4 clean windows: @525/@94/@566/@1413), the @525 clean NOM parse (this battery), the pour-window discriminator, the @566 13-blocker status. Battery gathers only (§7); the class decision is red-team venue.
3. `nom97-525-inf-rival-kill` (P3) — Kill-seek the INF rival at @525 specifically: with adverbial-81 dead at @524, test whether any grammatical INF parse survives at @525 under standing values. Bar: kill iff no grammatical INF parse exists; else fence. A kill makes @525 a NOM-only window, strengthening the tie's NOM arm for adjudication.

## Bookkeeping

- Report: this file.
- Queue: `nom-97-526-class` → `status: verdict`, `result: null`, 2026-10-09 (update follows; pre-write assert: was queued/verdictless; temp-file + rename; own entry only; no downgrade).
- Lock `locks/nom-97-526-class.lock` created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched.
