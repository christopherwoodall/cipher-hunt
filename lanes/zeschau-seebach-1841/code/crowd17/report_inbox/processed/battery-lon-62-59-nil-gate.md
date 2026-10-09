# Battery report: lon-62-59-nil-gate

**Target:** `lon-62-59-nil-gate` — conditional re-test of the 62→59 nil.
**Date:** 2026-10-09. **Worker:** 4fad9496-2571-4c2e-b3e9-26a5dc516a08.

## Pre-registered bar (verbatim)

"re-census 62->59; the standing nil (x0) holds unless a 62->59 frame appears or 59='est' provisional changes status; a future 62->59 hit re-opens the 'on est'-analog leg for conditioned 62='on'"

Numbered clauses:
- **C1:** 62→59 re-census performed on the repaired stream.
- **C2:** The standing nil (x0) holds, unless a 62→59 frame appears (→ re-opens the 'on est'-analog leg for conditioned 62='on').
- **C3:** 59='est' provisional status change acts as an independent trigger.

## Method

Stream re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed exactly like `code/side-keyhunt/repair_parse.py` (upstream tokenization: `s[i:i+2]` at row offsets; one continuous 0-based stream, row joins included — matching the lane's byte-boundary convention). `canonical.py` never used.

Asserts held: **1,847 pairs, 96 types**. n(62)=35, n(59)=27.

## Evidence

- **62→59 adjacency: exactly x0** across the full 1,847-pair stream (0-based global scan; includes row-boundary adjacencies). No 62→59 frame exists.
- 62 follower distribution (for context): 94×9, 48×6, 98×5, 16×4, 61×2, 06×2, 96/91×1.
- 62 predecessor distribution: 21×5, 20×4, 74×3, 93/03/08/78/92×2, 30/51/36/14/10/77/40/04/06/34/02/98/41×1. Reproduces the parent's finding: **46/47/11/94 never precede 62**.
- 59 follower distribution: 37×6, 32×3, 35×3, 46/42/30/39/36×2, 45/34/38/24/19×1.
- 59='est' status: still **provisional** (BATTERY-PROTOCOL §7; Round 20 has not ratified it). No status change.

## Clause results

- **C1 PASS** — re-census complete, byte-exact, x0.
- **C2 PASS** — standing nil holds; no 62→59 frame appeared, so the 'on est'-analog re-open for conditioned 62='on' does not fire.
- **C3 PASS** — no 59='est' status change; trigger unfired.

## Adverse answered

Adverse: "conditional gate - do not run until a 62->59 frame appears or 59='est' provisional changes status". The parent dispatched this target explicitly; the gate question is answered rather than bypassed: neither trigger has fired (no frame, 59 still provisional). No new information forces a re-open.

## Verdict: PROMOTE

The 62→59 nil is re-verified at battery grade. No standing or red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands. No follow-ups per §4 (promote). Re-open condition restated: any future 62→59 hit, or a 59='est' status change at Round 20, re-opens this gate.
