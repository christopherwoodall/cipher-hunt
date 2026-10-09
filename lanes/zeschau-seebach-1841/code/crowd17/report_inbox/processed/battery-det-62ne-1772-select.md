# Battery verdict: det-62ne-1772-select

**Verdict: NULL** — the bar is untestable as written: its load-bearing premise
(78="le" at @1771) contradicts the standing red-team R16-005 LEAD (78="ver",
confirmed R17-006). Per §5 the contradiction is recorded as the headline and
escalated to the red team; no standing verdict is downgraded or overwritten.
C1 passes on red-team-granted grounds. C2's frame cannot be tested without the
contradicted premise; its conditional (arguendo) analysis is fenced below.

**Target:** `det-62ne-1772-select` (P3)
**Date:** 2026-10-09
**Stream:** repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py`; asserts 1,847 pairs / 96 types held
in-session). `canonical.py` never used. R5005, sealed gates, red-team
adjudication queue untouched.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"name 24's value/role at @1775 with zero new assumptions, then test whether
the 'le [62]ne [24] ce qui est' frame selects 'regne' or 'trone'"

Numbered clauses (restated before testing; not modified after):

- **C1**: Name 24's value/role at the @1772-window 24 locus using zero new
  assumptions (standing grants/promotes/provisionals only).
- **C2**: Test whether the "le [62]ne [24] ce qui est" frame selects "règne"
  or "trône" at battery grade.

## Byte-exact window (re-derived in-session, 0-based)

Row a8_09: `37@1770 78@1771 62@1772 94@1773 24@1774 87@1775 64@1776 59@1777
19@1778 48@1779 74@1780 65@1781`.

Offset corrections to the bar/parent listing: the bar says "24's value/role
at @1775" — 24 is at **@1774** (0-based); 87=ce is at @1775. The parent's
8-token listing "@1772 '37 78 [62] 94 24 87 64 59'" starts at @1770 (37@1770,
78@1771, [62]@1772, 94@1773, 24@1774, 87@1775, 64@1776, 59@1777). Census
in-session: "62 94" exactly 9 windows (@100, @508, @761, @840, @1329, @1362,
@1686, @1704, @1772); "78 62 94" exactly 1 (@1771); "77 62 94" exactly 1
(@507). Matches the parent census.

## Standing premises adopted (not re-litigated)

- R17-009: **24 = finite verb, modal-shaped — GRANT PROMOTE (class level)**;
  value ("peut"/"sait"/"doit"-class) unnamed.
- R16-005: **78="ver" LEAD**; confirmed R17-006 (ver-78-rebar NULL ratified as
  correct discipline); rival 78="er" KILLED R17-014. §7: 67 et/veut is the sole
  true polyvalence — 78 cannot simultaneously be "le".
- 94="ne" (R19-167/168); 87=ce granted; 64=qui granted; 59=est provisional;
  77="le" provisional.
- 62-subject-shape-evidence (NULL, fence executed, 2026-10-09): W9 @1772
  **FITS** the subject+'ne' shape — "[62] ne [24]" parses cleanly on granted
  values only (24 finite/modal per R24, follower 87 ≠ 85); W2 @508 is
  **hostile** to subject+'ne' ("ne qui" ungrammatical), forcing the "[62]ne"
  word reading there (w508-noun-ne "trône" battery promote stands).
- ne-24-profile (PROMOTE, class level): @1774 parses "[62-subj] ne [24].
  Ce qui est [19]…" with clause boundary before 87.

## C1: 24's value/role — PASS

24's role at @1774 is named with zero new assumptions: **finite verb,
modal-shaped** (R17-009 red-team GRANT PROMOTE, class level). Verified
in-session: 24@1774, follower 87=ce (≠ 85, so not the R24 "en" fork);
predecessor 94="ne" gives the lone-"ne" modal frame "[62] ne [24]"
("ne [modal]"-shaped), the author's norm per ne-24-profile's 34/37 baseline.
24's VALUE is open (not named, not promoted) — naming it would exceed the
zero-assumption budget. Role named; value honestly fenced.

## C2: frame selection test — UNTESTABLE AS WRITTEN (premise contradicted)

The frame "le [62]ne [24] ce qui est" requires 78="le" at @1771. Standing
red-team grading says 78="ver" (R16-005 LEAD, R17-006 confirmed). These are
incompatible (§7 sole-polyvalence rule), and a battery worker does not
overturn red-team grading. The frame therefore cannot be tested as written;
per §2 this is recorded as a finding (null), not silently rewritten.

Conditional analysis (arguendo, fenced — not acted on): even granting the
frame's segmentation, it does not select. Under "[62]ne [24]", both "le
règne [V]" and "le trône [V]" are grammatical — finite/modal verbs impose no
règne-vs-trône selectional distinction, and 24's value is open. "Ce qui est
[19]…" is a separate free-relative clause (clause-anaphoric "ce qui" is
selectionally inert — it comments on any preceding clause). Under the
standing segmentation ("[62] ne [24-modal]"), the "[62]ne" word is not even
present at this window, so the règne/trône question does not arise here.

## Claim check

"@1772 … the only other 'le [62]ne' window in the stream": true as a byte
pattern only under the contradicted 78="le" premise. Under standing values
@1771 is 78="ver" (R16-005 LEAD), so this window is **not** a "le [62]ne"
window at all — @508 ("77 62 94", 77="le" provisional) stands as the sole
surviving "le [62]ne" candidate. The claim's distributional half (only one
other 62-94 window with a "le"-shaped predecessor) is verified; its value
half is contradicted by red-team grading.

## Adverses

- **"zero-assumption budget per parent" — ANSWERED.** Zero new assumptions
  introduced. The single premise the bar needs beyond standing values
  (78="le") is contradicted by standing red-team grading (R16-005 LEAD,
  78="ver"); rather than smuggling it in, the contradiction is the headline
  and is escalated. C1 answered on R17-009 grant; C2 fenced per §2.

## Verdict: NULL

C1 passes; C2's frame is untestable as written because its "le" premise
contradicts the standing red-team R16-005 LEAD (78="ver"). Per §5 this
contradiction is escalated, not acted on. The règne/trône tie is unbroken by
this window — under standing values the window does not contain "[62]ne" at
all. No standing or red-team verdict contradicted or downgraded. §7 intact.
Canonical-stream caveat stands (row a8_09's upstream offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json; for supervisor queuing)

1. `redteam-78-1771-adjudication` (P2) — **Red-team venue / escalation.**
   Adjudicate @1770–1777 under R16-005 (78="ver"): does "37 ver [62] ne
   [24-modal]. Ce qui est…" parse cleanly on granted values, and does it
   definitively exclude the "le [62]ne" word-reading at @1772? Decides whether
   @1772 can ever serve as a règne/trône witness. (This battery's §5 escalation.)
2. `seg-1772-wordbound` (P3) — Under standing values only (78="ver" LEAD, 24
   finite-modal R17-009, 94="ne", 87=ce, 64=qui, 59=est provisional), test
   whether ANY grammatical parse of @1771–1774 makes "[62]ne" a single word
   (the règne/trône candidacy condition). Bar: produce one zero-new-assumption
   parse with "[62]ne" as a word, or fence the word-reading at this window
   permanently.
3. `le-62ne-recensus` (P4) — Re-census determiner+62+94 windows under standing
   values (78="ver" LEAD): is @508 ("77 62 94", 77="le" provisional) the SOLE
   surviving "le [62]ne" window? Bar: confirm sole-survivor status, or name
   another determiner-led 62-94 window on granted values.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-det-62ne-1772-select.md` (this file)
- Queue: `det-62ne-1772-select` → `status: verdict`, `verdict: {"result": "null", "report": "code/crowd17/report_inbox/battery-det-62ne-1772-select.md", "date": "2026-10-09"}` (pre-write assert: was queued/verdictless; temp-file `battery-queue.json.det-62ne-1772-select.tmp` + rename; JSON re-validated post-write; own entry only; no downgrade)
- Lock: `locks/det-62ne-1772-select.lock` created on start (agent worker-47678, 2026-10-09T19:47:44Z), deleted on completion
- R5005, sealed gates, red-team adjudication queue untouched.
