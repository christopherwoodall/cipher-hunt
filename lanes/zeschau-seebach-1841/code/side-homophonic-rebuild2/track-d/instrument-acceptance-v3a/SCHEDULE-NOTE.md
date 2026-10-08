# Rung A schedule provenance note (2026-10-07)

- pkg-1 / agent1: judged in the prior (interrupted) session; log verified mechanically (18 records, 6 labels x 3 passes, no dupes, sha pins OK, parse audit PASS).
- pkg-3 / agent3: the coordinator's task message carried a fresh-random per-pass schedule that differed from the /tmp scratch schedule file generated earlier (transcription delta, not a protocol event). The judge followed the message schedule exactly. The message schedule was: pass1 = 3bdb24a3, f3d099d8, 56343aae, aa397659, 8a8932d1, c3a5ae84; pass2 = 56343aae, f3d099d8, c3a5ae84, 3bdb24a3, aa397659, 8a8932d1; pass3 = 8a8932d1, c3a5ae84, aa397659, 56343aae, 3bdb24a3, f3d099d8. /tmp/rungA-sched-agent3.json was overwritten to match the schedule actually used. All three per-pass orders are fresh randomizations; protocol requirement (fresh random order per pass) is satisfied.
- pkg-2 / agent2: in flight; the message schedule (seed-order) will be reconciled against the returned log on completion.

## agent2 (pkg-2) schedule note
Same transcription delta: the judge followed the message schedule (pass1 = 51569b66, 701e7e02, 30429b0e, a223a3ab, d5f5e4f6, ab83f1d5; pass2 = 701e7e02, 30429b0e, ab83f1d5, d5f5e4f6, 51569b66, a223a3ab; pass3 = a223a3ab, ab83f1d5, 30429b0e, d5f5e4f6, 51569b66, 701e7e02). The /tmp scratch file was not reconciled (no longer needed); the used order is recorded here.
