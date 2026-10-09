# Battery verdict: agr-89-872-adj — **NULL** (fence on agreement grounds; anchor unavailable)

## Target
- id: `agr-89-872-adj` (priority 3)
- claim: Twin of agr-89-642-adj: agreement check for "le [89]e" at @871 against 20's adjective candidacy once 89's value resolves.
- Parent: `subj-20-872` NULL (2026-10-09) — follow-up 2 of 3. 20's post-nominal-adjective class did NOT replicate at @873 (NP cannot open; no finite verb).
- adverses: "coordinate with agr-89-642-adj - do not duplicate its method."

## Bar (verbatim from battery-queue.json)
"confirm or fence the adjective arm on agreement grounds at battery grade"

Numbered pass/fail clauses (restated before testing — bar not modified after data):
1. **C1 (confirm):** the gender/number anchor — the determiner→noun relation fixing
   89's gender/number at @871 — is nameable with zero ungranted assumptions under
   standing values, AND no forced gender/number mismatch excludes an adjectival
   20 at @873 → adjective arm confirmed as agreement-admissible at this window.
2. **C2 (fence):** otherwise → fence the adjective arm on agreement grounds with
   stated cause.

Verdict rule: promote iff C1 passes; kill iff a window forces a gender/number
mismatch at kill grade; else null with fence + 1–3 follow-ups.

## Method (non-duplicative vs the twin — adverses answered)
Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/agr-89-872-adj.lock`
on start (agent a87c68a3-e4cd-4aad-9034-c57e80a26de1, 2026-10-09T19:50:06Z); no prior/stale
lock. Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(byte-exact tokenization per `code/side-keyhunt/repair_parse.py`; asserts held:
1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances,
and the red-team adjudication queue untouched.

The twin (`agr-89-642-adj`, PROMOTE) ran an **abstract forced-mismatch scan** on a
*granted* "le [89]e" premise at @639: nothing forced a gender/number contradiction,
so it confirmed agreement-admissibility and derived a masculine-singular constraint
on 89. This battery runs the test the twin never ran: an **anchor-availability
differential test** — agreement (adjective↔noun gender/number compatibility) needs
the determiner→noun relation that carries the gender/number. At each of the two
"77 89 48" loci, test whether that anchor relation is nameable with zero ungranted
assumptions, then run candidate-conditional agreement cells.

Adopted standing premises (used, not re-litigated):
- 77="le" provisional (masculine singular determiner); 87="ce" promoted (A4);
  48="e" promoted inflectional letter tier; 67 et/veut sole polyvalence.
- `subj-20-642` PROMOTE (20 = post-nominal adjective at @642, window-level).
- `subj-20-872` NULL (adjective arm fenced at @873 on frame grounds).
- `celle-7780-fusion-515-869` KILL (2026-10-09): "87 77" ≠ "celle" at @869.
- `ce-le-verb-frame` NULL: preverbal "87 77" has no grammatical account — the
  two-word "ce le" reading is fenced as a 77-value residual.
- `ce-le-869-residual-input` (queued P4): the @869 residual packaged as red-team
  input for the 77-value venue.
- 89's value open; 89's global noun-vs-infinitive class red-team venue;
  20's value/class unvalued globally (`poly-20-docket` red-team venue).
- Kills hold: 20="fois"; 48="est"/"ne"/"de".

## Locus (byte-exact, re-derived)
- 0-based @865–878, rows a5_07/a5_08:
  `47(ce)@864 46(que)@865 00(pour)@866 86@867 70(pre)@868 |87(ce)@869 77(le)@870
  89@871 48(e)@872 |20@873| 74@874 49@875 16@876 77(le)@877 86@878`
- 89 census: n=14 — @113 @222 @275 @285 @303 @640 @781 @871 @986 @1082 @1377
  @1393 @1498 @1752 (matches twin report exactly).
- "89 48 20" occurs exactly 2x stream-wide: @640 (20@642) and @871 (20@873).
- "77 89 48" occurs exactly 2x stream-wide: @639 and @870.
- "87 77" occurs exactly 2x stream-wide: @515 and @869.
- Index note: the claim's "@871" is 89's 0-based position; 20 sits at @873.
  The conj convention named this trigram "@872" (48's position). All offsets
  below are 0-based.
- Observation (recorded, not hidden): the parent report placed the "87 77"
  residual at @515/@611/@869. The stream shows `47@611 77@612 87@613`
  ("ce le ce" order), not "87 77". The "87 77" bigram is only at @515 and
  @869. The @869 residual stands regardless.

## Anchor-availability differential test

**Locus A (@639, twin's window):** `67(et)@638 77(le)@639 89@640 48(e)@641
|20@642| 24-fin@643`. The token left of 77 is the coordinator 67, cleanly
outside any NP; nothing abuts 77's left. "le" attaches to 89 with zero
ungranted assumptions. **Anchor available** (this is the premise the twin's
confirm rested on — not re-litigated).

**Locus B (@870, this window):** `87(ce)@869 77(le)@870 89@871 48(e)@872
|20@873| 74@874`. The token left of 77 is 87 ("ce", promoted A4), directly
abutting. The "87 77" contact has no licensed parse at this locus:
fusion "celle" is KILLED at @869, and the two-word "ce le" reading is fenced
as a 77-value residual with no grammatical account; both "87 77" exemplars
stream-wide (@515, @869) are residuals. 77="le" is provisional. Naming 77@870
as the masculine-singular determiner of 89@871 — the relation that carries
gender/number into any agreement test — therefore requires granting either
the fenced two-word parse or an unnamed third parse: **≥1 ungranted
assumption. Anchor unavailable.**

**Kill-grade scan:** no forced gender/number mismatch anywhere at this window.
20 is unvalued globally (no forced feminine/plural shape); 89's value is open;
48="e" is promoted inflectional, not a feminine marker; no plural licensor
adjacency at 89@871 or 20@873 (20's 15 followers stream-wide: 62×4, 67×3,
61/17/24/12/30/74/57/64×1 — no plural "s"-class adjacent). No kill.

**Candidate-conditional agreement cells** (supporting, not decisive):
- 89 = masculine singular noun AND anchor granted → agreement admissible (the
  twin's logic transfers, conditional only).
- 89 = feminine noun → collides with 77="le", but 77 is provisional and sits
  inside the @869 residual: the contradiction would re-open 77's value (the
  red-team 77-value venue, already fed by `ce-le-869-residual-input`), not the
  adjective arm per se.
- 89 = infinitive (red-team venue, "-re" family, infinitive-shaped under 24 at
  @222) → no determiner-noun relation at all; agreement moot.

**C1 FAILS** on the anchor clause: the gender/number anchor at @871 is not
nameable with zero ungranted assumptions. **C2 applies: fence.**

## Verdict: NULL (fence on agreement grounds)

**The adjective arm at @873 is fenced on agreement grounds with stated cause:**
the gender/number compatibility of an adjectival 20 cannot be evaluated at
battery grade at this locus because the anchor relation (77@870 as 89@871's
determiner, the carrier of masculine-singular) is unavailable — "87 77" is a
standing residual with no licensed parse (fusion killed at @869, two-word
reading fenced). This is not a kill: no forced mismatch exists, and the
twin's compatibility logic transfers unchanged *if* the anchor ever becomes
nameable. The fence lifts exactly when (i) 77's value at @869 resolves in a
way that licenses 77 as 89's determiner, AND (ii) 89's value resolves to a
masculine singular noun. Until then, agreement testing at @871 is deferred —
which is why the twin's PROMOTE does not transfer to this window despite the
identical surface trigram.

## Scope and caveats
- Window-level only (@869–873). 89 and 20 stay unvalued; no registry change.
- Does not touch the @639–642 twin PROMOTE (`agr-89-642-adj` stands); does not
  re-litigate the @873 frame fence (`subj-20-872` stands). No standing or
  red-team verdict contradicted or downgraded.
- §7 intact: no polyvalence declared; 67 remains the sole true polyvalence.
- 89's global noun-vs-infinitive class stays red-team venue; if ruled
  non-noun globally, the agreement question is moot at both windows — their
  act, not battery's.
- Canonical-stream caveat stands (rows a5_07/a5_08 upstream row offsets
  unvalidated).

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json)

1. `agr-89-872-anchor-lift` (P3) — re-run the agreement check at @871 once the
   @869 "87 77" residual resolves (77-value red-team venue): bar = name 77@870's
   grammatical role with zero ungranted assumptions, then apply the abstract
   compatibility test; else re-fence.
2. `agr-89-candidate-matrix` (P4) — once 89's value resolves, test the
   candidate-conditional agreement cells at both "77 89 48" loci (@639, @870):
   a feminine-89 candidate must first survive 77="le" at @639 before it can
   license any @871 reading.
3. `shape-20-agr` (P4) — agreement-shape census of 20's 15 stream positions:
   test whether 20 ever sits in a forced-plural or forced-feminine frame; an
   independent leg fencing (or freeing) the "20 must agree masculine singular"
   assumption at @873 without touching 89's value.

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-agr-89-872-adj.md` (this file).
- Queue: `agr-89-872-adj` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/agr-89-872-adj.lock` created on start, deleted on completion
  (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
