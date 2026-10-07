# Report note — smith-liaison (round-10 WO7): rebuild2 health + constraints update

Context: bank-constraints work order for the Smith (side-homophonic-rebuild2).
The round-10 constraints memo is banked at
`code/crowd10/liaison/smith-constraints.md` — it supersedes the round-9 memo
(`code/crowd9/liaison/smith-constraints.md`, which stands unrepealed and is
fully carried forward). No Smith work was duplicated; nothing on the Smith's
side was changed.

## Decision

- Wrote the round-10 constraints update. Carry-forward: all round-9 F33
  conditioned-polyvalence rules (§1a–1e), the anchor set (7 GT + 5
  provisional), the must-NOT-break list, the scope-zero/C1 gate, T7.
- Incorporated the round-9 adjudication deltas (RULINGS-ROUND9.md, which
  post-dates the round-9 memo): 86=que-family REFUTED (kill-grade), H_verb
  for 48 KILLED (K2 fired; 48 UNIDENTIFIED), 59="est"-as-word dead at
  @1447/@1803 (fenced n=2), 66/89 classes CONFIRMED (84's en-islet
  extensions now condition on CONFIRMED classes), 84 residual census banked
  (n84=25), 06-islet GT core citation corrected to @1182–1185 (0-based),
  06-islet fragility banked (n_eff=3; coincidence probe p=0.0138 between
  bars), @1248 NEITHER-fence UPHELD + Gate-4 non-finite era-bounding,
  @199 NEITHER-conditional on 08="l'", @630 et-CONDITIONAL (C1∧C2),
  H3a banked WEAK for 78 fork-tine (c) (fork unresolved), M3 struck scoped
  (German phonetics window-specific only), germanist/frenchman V1–V5 vetoes
  banked as constraints on future proposals, 43="me" clitic-order adverse
  banked in the qui-96-43 frame, B3 3.19× STANDS (dissolution premise dead).
- Added three new discriminating windows for the future joint scorer:
  §3.6 @199 (NEITHER-conditional on 08="l'"); §3.7 @1351–1356
  (FENCED-PENDING round-10 resolution — fence, don't revisit banked
  neighbors); §3.8 the 59-conditioned windows (pending the battery).
  Window 1 refined: 59-as-word era-absent at @1447/@1803; viable parse is
  the bisyllabic-verb unit.
- Added §7: the six round-10 live questions the Smith's future scorer must
  respect when decided (@1351 resolution, 59 conditioned-polyvalence
  battery, 48 syllable-cell battery, @1248 ≥2-leg arm, 67 residuals,
  06 islet frame test). Round-10 executors haven't landed yet — no new
  rulings to bank; the liaison will relay them.

## Why

The round-9 memo predates the independent round-9 adjudication, so the
Smith's spec was missing nine rulings that change conditioned rules and the
must-not-break list. Round 10's live questions (notably the 59 battery and
the @1351 resolution) can revalue or condition the provisional anchor set —
the memo now tracks them as pending hazards with explicit interim rules
(§3.7, §7).

## Enlightenment

- The biggest cross-fleet hazard this round is the **59 conditioner
  battery**: 59=est is the only provisional anchor whose conditioning is
  actively being built, and Frenchman Gate 2's @1184 fenced adverse plus the
  §3.1 frame both depend on the outcome. Until the red team rules: 59=est
  provisional everywhere except @1447/@1803 (no standalone "est" there).
- No current control corruption found: verified by grep that the Smith's
  preregs plant neither 59=est nor any 48/@1351-dependent readings — the
  hazards are prospective (future joint scorer), not live. Scope-zero until
  C1 is unaffected; all three tracks are executing per PREREG with nothing
  stalled or killed.

## Verification

- Rebuild2 mtimes checked: newest files are Track B's PREREG (20:25 UTC)
  and redteam/RULINGS.md (19:30 UTC); no `results/` dirs exist on any track.
- Round-9 rulings re-read from `code/crowd9/redteam/RULINGS-ROUND9.md`
  (the 8 rulings R1–R9, all numbers curator-re-derived there).
- The constraints memo was written fresh to
  `code/crowd10/liaison/smith-constraints.md` (19,180 bytes) and cites
  the authoritative ruling files per section.
