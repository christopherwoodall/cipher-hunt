# PRE-REGISTRATION — INFINITIVE-33, round 14 (Fork S/W discriminator + 79="tout" F-C unlock)
**Executor:** INFINITIVE-33 · **Date:** 2026-10-07 (written BEFORE any round-14
computation; only standing/recorded numbers consulted: NOTES.md F77/F79/F103/F109,
STATE.md round-14 WO2, `code/crowd12/identifier33/`, `code/crowd13/carry-classes/`,
`code/crowd12/redteam/RULINGS-ROUND12.md`, `code/crowd13/adjudicator/RULINGS-ROUND13.md`)
**Work dir:** `code/crowd14/infinitive33/`
**Report note:** `code/crowd14/report_inbox/infinitive33-fork14.md`
**Value paradox:** DO NOT FORCE. Report candidate (≥2 legs) or sharpened paradox.

## 1. Fork definitions (standing, GRANTED — not re-derived)

- **Fork S (stem):** 33 = infinitive STEM; the infinitive word = "33"+"suc"
  (the successor group completes it). Standing support: F79-I4 (33→29 ×5 =
  stem+"er", pencil-GT 29=er). Cost rule: a frame whose suc-gloss is a complete
  word (not an infinitive-ending chunk) is ungrammatical under Fork S.
- **Fork W (whole-word):** 33 = complete monosyllabic infinitive; suc = next
  word. Standing support: F79-I1 ("pour 33" ×8) + I2 (pre==67 ×1,
  "veut"-prov ⇒ "veut INF" licensed). Cost rule: I4's "33 29" = "INF er" is
  ungrammatical under Fork W (the fork's open cost — unexplained, recorded).
  Value scope: ONLY monosyllabic infinitives (F22 granularity: 1 group = 1 chunk).

## 2. Discriminator design (pre-registered)

For each of the 8 "pour 33" frames, under each fork, the reading imposes a
constraint on the successor group (suc) and/or pre-context. Per-frame verdicts:

- **SUPPORT:** the fork's reading is consistent with ALL standing gloss values
  at that frame (GT > provisional > banked > lead priority — no overrides) AND
  era-licensed where testable, AND adds a NEW testable leg (not mere
  non-contradiction).
- **NEUTRAL:** the fork's reading is compatible but untestable (suc unglossed,
  no era query definable).
- **COUNTER (conditional):** the fork's reading contradicts a standing value
  or an era-zero; the condition (which value/query) is named explicitly.

**Era instrument:** pool∖v8 only (3,867,332 tokens; lane `tok()` verbatim;
F77 rule — v8 phrase queries VOID). Gate: pool∖v8 token count == 3867332.

**Per-frame pre-registered predictions:**

| frame | Fork S prediction | Fork W prediction |
|---|---|---|
| F-A @186/@1245 "00 33 16 00 67" | 33+16 must be an infinitive ending. If 16="i" (lead) ⇒ stem+/i/ — no French infinitive ends in bare /i/ [FR-JUDGMENT] ⇒ S COUNTERS 16="i" at F-A; 16 must be an ending-chunk (unidentified) ⇒ else NEUTRAL | "pour [mono INF] 16 pour 67" — F81 double-pour stack has NO era license (~16.5MB) ⇒ F-A FENCED under W (frame-level) |
| F-B @408 "00 33 01 02" | 33+01 must be an infinitive ending; 01 unidentified (01="ci" killed N23) ⇒ NEUTRAL | "pour [mono INF] 01 02", tails unglossed ⇒ NEUTRAL |
| F-C @467/@1088 "00 33 79 80 06" ×2 | 33+79 = infinitive. **If 79="tout" ⇒ stem+"tout" — no French infinitive ends /tu/ [FR-JUDGMENT] ⇒ S REFUTED at F-C (CONDITIONAL on 79="tout" promotion; both frames, replication-consistent)** | "pour [mono INF] tout W" — testable battery T_fc (below). W predicts era license with monosyllabic X |
| F-D @846 "00 33 96 40" | 33+96; 96="par"-prov ⇒ stem+/paʁ/ — no infinitive ends /paʁ/ [FR-JUDGMENT] ⇒ S REFUTES 96="par" at F-D (CONDITIONAL; expensive — recorded as tension, NOT re-litigation of F19) | "pour [mono INF] par [e-word]" = 0/pool∖v8 (re-verify) ⇒ F-D FENCED under W (CONDITIONAL on 96="par") |
| F-E @936/@1630 "00 33 21 64" | 33+21; 21="ce"-banked ⇒ stem+/s(ə)/ — no infinitive ends /s(ə)/ [FR-JUDGMENT] ⇒ S REFUTES 21="ce" at F-E (CONDITIONAL; breaks banked lead — expensive) | "pour [mono INF] ce qui" — T2's winner "savoir"×2 is NOT monosyllabic ⇒ fork-forbidden; enumerate monosyllabic X with n≥1 |

**Pre-registered discriminator bar:** the discriminator DECIDES (kills a fork)
only if a fork is refuted UNCONDITIONALLY (no standing value broken in the
refutation). Expected outcome: NEITHER fork dies unconditionally (all
refutations are conditional on provisional/banked/lead values) ⇒ the paradox
stands, sharpened per-frame. One CONDITIONAL refutation per fork is recorded
as that fork's cost.

## 3. F-C battery — 79="tout" unlock (pre-registered, named)

F-C = @467/@1088: "00 33 79 80 06" ×2 (one unknown infinitive ×2, R1).
79="tout" @1799 clean (F109: "79 87 64" = "tout ce qui"; the ×3 via-24 hits are
dead-if-24="en"-STRONG per F31 — re-verify the trigram census).

Battery T_fc on pool∖v8, Fork-W scope (33 = whole monosyllabic infinitive):
- (a) n("pour X tout W") for X ∈ monosyllabic infinitives (mechanical
  vowel-group pre-filter, HAND-VERIFIED syllable count on the firing set) AND
  for X ∈ all infinitives (scope check — is the construction mono-only?).
- (b) W-slot distribution: what follows "pour INF tout" in era French
  (hand-read 3 examples, constituency-checked).
- (c) License verdict: if n=0 ⇒ F-C UNLICENSED under Fork W ⇒ Fork W costs
  F-C too (frame joins F-A/F-D as fenced).
- (d) 79 census: ALL 79 positions in the stream, ±4 windows. Unlock test: any
  "00 33" frame with 79 in +1..+4 beyond the F-C pair? Any 33-frame with 79
  in the tail? Report the full census regardless.

**Pre-registered unlock bar:** 79="tout" UNLOCKS iff (i) @1799 is the sole
clean "tout"-frame AND (ii) the F-C pair is the only "pour 33 … tout"
occurrence (replication stands) AND (iii) T_fc licenses "pour [mono INF] tout W"
with a W-slot distribution compatible with unknowns 80/06 (report; no forcing).

## 4. Value candidacy (honest fork constraint, pre-registered)

- **Fork-W battery:** monosyllabic X with n≥2 INDEPENDENT legs across
  {T2 "pour X ce qui" (F-E), T_fc "pour X tout W" (F-C)} + no contradiction at
  F-A/F-B/F-D. ID needs ≥2 legs; report the intersection honestly.
- **Fork-S battery:** the joint constraint — ONE stem 33 such that
  {33+16, 33+01, 33+79, 33+96, 33+21} are ALL real infinitive endings. With
  standing glosses (79="tout"-lead, 96="par"-prov, 21="ce"-banked), count the
  standing values Fork S must break. Report the exact blocking constraint.
- **Paradox check (F109):** verify "savoir is fork-forbidden under BOTH forks":
  under W by syllable count (disyllabic vs 1 group); under S by the banked suc
  (33="savo"+21="ce"-banked ⇒ "savoce" ≠ "savoir" — S needs 21="ir"-chunk,
  breaking the banked lead). If no value clears both forks ⇒ PARADOX STANDS,
  sharpened with the exact blocking constraint. DO NOT PROMOTE, DO NOT FORCE.

## 5. What would break the paradox (pre-registered)
1. A pencil-GT-anchored multi-group word containing 33 (WO2 named path (a)).
2. 79="tout" promotion ⇒ Fork S dies at F-C CONDITIONALLY (fork resolution
   toward W, not a value ID).
3. A monosyllabic X with ≥2 independent legs (T2 + T_fc) under Fork W.
4. A stem 33 with all five suc-compositions real infinitive endings without
   breaking standing values (Fork S) — currently blocked by 79/96/21.
5. The suc-homophone hypothesis (round-12 path (a)) — side-homophonic-rebuild's
   lane; dissolves conditional refutations, not run here.

## 6. Verification (pre-registered)
- Re-derive the 8 "pour 33" positions from the repaired stream INDEPENDENTLY:
  all i with pairs[i]=='33' and pairs[i-1]=='00'; assert == {186,408,467,846,
  936,1088,1245,1630} or report drift honestly.
- Re-derive n33, F79-I4 (33→29) positions, F79-I2 (pre==67) position.
- Re-derive the 79-87-64 trigram census (@1799 + the via-24 ×3).
- Frame windows byte-checked against r13_33_results.json ctx strings.

## 7. Frenchman perspective (required)
Era infinitive syntax note: "pour tout + INF" is the standard order
("pour tout dire"); "pour INF tout" needs "tout" as object/degree adverb —
hand-read the T_fc examples for constituency. "pour savoir ce qui" = "find out"
sense, standard in diplomatic correspondence. Monosyllabic infinitives in
1841 diplomatic register: être, faire, voir, dire, lire, prendre, mettre,
rendre, suivre, vivre, fuir, rire, naître, paraître (by-ear cuts may merge).

## Outputs
`fork_disc.py`, `fork_disc_results.json` (per-frame fork verdicts, F-C battery,
79 census, value candidacy, paradox statement), this PREREG.md,
`code/crowd14/report_inbox/infinitive33-fork14.md`.
