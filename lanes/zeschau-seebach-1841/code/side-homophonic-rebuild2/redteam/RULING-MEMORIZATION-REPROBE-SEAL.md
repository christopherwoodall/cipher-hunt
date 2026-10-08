# RULING — Memorization re-probe seal paradox (2026-10-07)

**Adjudicator:** red team. **Status: BINDING.** **Ruling: (a) — AUTHORIZE the narrow trusted-party read.**

## The question

PREREG-D-v2 §6(1) requires the memorization re-probe on the 6 FRESH gate
truths (seeds 184201–184204, 184206, 184207) BEFORE unsealing
("non-negotiable"). §10(6) forbids reading fresh keys, pclasses, or
plaintexts until Runner scoring. The 6 fresh instances exist only as
`SYNTHETIC-ct-<seed>.pairs.txt` + `SYNTHETIC-key-<seed>.json` + crib/meta
under `code/side-homophonic-rebuild/control/instances/` (verified present,
all 6 seeds, 2026-10-07). No truth-decode plaintext files exist. A
dispatched key-holder stopped cleanly rather than decode. The filed
`track-d/memorization-reprobe-20261007.jsonl` records the probe BLOCKED with
`no_probe_inputs` as a terminal blocker.

## Finding: the paradox is apparent, not real

The protocol already prescribes option (a). No amendment is required.

- **R12e (binding, RULINGS.md):** "the gate-truth probe construction
  requires READING the fresh truths to write paraphrases, in tension with
  §10(6)... v2 specifies no containment mechanism. Before Stage-2
  clearance, the probe must name its trusted party: the key-holding
  Runner/coordinator constructs and freezes the paraphrases, exposing ONLY
  the paraphrase strings to the track pipeline (forensics-class carve-out,
  logged) — or a red-team-supervised alternative."
- **R14f (binding, RULINGS.md):** "the key-holder supplies ALL 12 candidate
  strings as opaque blind-labeled inputs (frozen, sha256 logged); the track
  must not derive truth decodes from keys."
- **PREREG-D-v2-branchB §5(1):** "the key-holding Runner/coordinator — NOT
  the track pipeline — constructs the paraphrases from the gate truths and
  freezes them (sha256 logged) BEFORE any track unsealing; the track sees
  ONLY the paraphrase strings (forensics-class carve-out, logged). This
  resolves the v2 §10(6) tension: the track never reads fresh keys,
  pclasses, or plaintexts."

§10(6)'s prohibition binds the **track pipeline**. The trusted party's read
is the explicitly prescribed containment mechanism, not a violation of it.
"Unsealing" in §6(1)/§10(6) means **track-side exposure** of truths; a
contained key-holder decode that never reaches the track is not unsealing.
R14f necessarily implies the key-holder derives the truth decodes — one
cannot supply 12 strings including 6 truth decodes without reading them.

The dispatched key-holder's stop was correct under its narrow brief (it was
told to locate pre-existing truth files and stop if absent). The brief
under-authorized relative to the protocol. The fix is a re-dispatch with
R12e/R14f authority, per the work order in the appendix.

## Why not (b) or (c)

- **(b) Defer until Runner scoring** would violate §6(1)'s explicit
  "non-negotiable, before unsealing" language and the filed jsonl's own
  rejection of workarounds. A post-hoc probe cannot detect memorization
  that would already have contaminated the gate — the control would be
  decorative.
- **(c) Waive on pilot-originals-clean** is rejected for the reason §6(1)
  itself gives: the pilot probed OLD slices; memorization is
  text-dependent; a clean result on 184101–184106 does not transfer to
  fresh slices. Waiving would remove the gate's only memorization control
  while the 2,700-call gate is exactly the stage where a memorizing
  solver does its damage.

## Ruling

1. The key-holding trusted party (a fresh, track-isolated agent — NOT a
   track worker, NOT the coordinator running the gate) is AUTHORIZED to
   decode the 6 fresh instances' ct with the sealed keys for the SOLE
   purpose of constructing the 12 probe candidate strings, per the
   appendix work order.
2. This read does not constitute unsealing. The §6(1) "before unsealing"
   requirement is satisfied because the track never sees the truths; the
   probe still runs before Runner scoring.
3. This ruling settles R14f's under-specification: "the track sees ONLY
   the paraphrase strings" is operationalized as "the track sees only the
   12 opaque blind-labeled strings"; the mapping stays sealed.
4. The `no_probe_inputs` blocker in
   `track-d/memorization-reprobe-20261007.jsonl` is cleared by delivery of
   the frozen 12-string package, not by any track-side derivation.

## Appendix — key-holder work order (exact)

**Agent:** fresh subagent, depth ≥ 1, track-isolated. It must have NO prior
or subsequent contact with the track pipeline, the solver, the judge
instrument, or the gate coordinator. Its transcript is the seal boundary.

**May touch (and nothing else):**
- `code/side-homophonic-rebuild/control/instances/SYNTHETIC-ct-<seed>.pairs.txt`
  and `SYNTHETIC-key-<seed>.json` for seeds 184201, 184202, 184203, 184204,
  184206, 184207 — for decoding only.
- It may NOT touch R5005, `upstream-ct_R5005.txt`, the solver, the judge
  instrument, any track working file, or any file outside the 6 instances.

**Procedure:**
1. Decode the 6 truth passages with the sealed keys (mechanical decode;
   verify byte counts against the meta files).
2. Write 6 fresh French paraphrases, one per truth: reword the meaning in
   fresh natural French prose, normal spacing/punctuation, comparable
   length to the truth. Genuinely reworded, not near-copies. Do NOT reuse
   the pilot paraphrases in `track-d/freeze_paraphrases.py`.
3. Assign 12 fresh random 8-hex blind labels (6 truth decodes + 6
   paraphrases), with zero overlap against any label in
   `track-d/candidates.json`, `track-d/label_map.json`, or the 84+16
   rung-C labels. Compute sha256 of each candidate string.
4. Write TWO files:
   - `track-d/memorization-reprobe-candidates.json` (TRACK-VISIBLE):
     `{label: {text, sha256}}` — strings only. No seed linkage, no
     truth/paraphrase class marking, no ordering signal. Shuffle entry
     order with a logged seed.
   - `track-d/memorization-reprobe-key.json` (SEALED): the full mapping
     `{label: {seed, class}}` where class ∈ {truth, paraphrase}.
5. Append a `seal_status` record to
   `track-d/memorization-reprobe-20261007.jsonl` noting: key-holder decode
   performed under this ruling, files written, sha256 manifest frozen, key
   sealed, zero track contact.
6. Report back ONLY: "12 candidates frozen, sha256 manifest written, key
   sealed, zero content leaked." The report must contain NO text from any
   truth passage, paraphrase, key, or the mapping.

**Re-sealing requirements:**
- After delivery the key-holder agent is DONE: no further messages, no
  follow-ups, no contact with any track agent. (Close, do not resume.)
- The sealed key file is never opened until Runner scoring.
- The 12 strings are frozen: no edits after the sha256 manifest is
  written. Any correction requires a new red-team ruling.
- The probe's 36 judge calls run against the 12 opaque strings exactly as
  frozen, under PREREG-D-v2 §6(1) (median-of-3, void rule mT−mP ≥ 15).

**Verification (red team, before the probe runs):**
- 12 labels unique and non-overlapping with all historical labels.
- sha256 manifest recomputes from the candidate file.
- Zero 18420x candidate-string text outside the two files (prose mentions
  excepted); the track-visible file contains no seed or class signal
  (byte-level check).
- Key-holder transcript contains no truth/paraphrase/key content beyond
  the file paths it was authorized to touch.
