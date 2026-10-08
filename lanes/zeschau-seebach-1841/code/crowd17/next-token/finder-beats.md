# Finder beats registry — crowd17 next-token pipeline

## Wave 1 (complete, 2026-10-07)

16 beats, one finder each. Finder reports live in
`code/crowd16/report_inbox/next-token-findings-<beat>.md`;
coordinator-ingested battery briefs in
`code/crowd16/report_inbox/next-token-<beat>.md`.

| beat | status | finder report |
|---|---|---|
| la (11 followers) | complete | next-token-findings-la.md |
| pre (70 followers) | complete | next-token-findings-pre.md |
| m (82 followers) | complete | next-token-findings-m.md |
| i (34 followers) | complete | next-token-findings-i.md |
| er (29 followers) | complete | next-token-findings-er.md |
| e (40 followers) | complete | next-token-findings-e.md |
| par-rest (96, solved windows excluded) | complete | next-token-findings-par-rest.md |
| est (59 followers — adjective battleground) | complete | next-token-findings-est.md |
| le (77 followers) | complete | next-token-findings-le.md |
| fois (17 followers — virgin territory) | complete | next-token-findings-fois.md |
| ce47 (47 frames — allophone verification) | complete | next-token-findings-ce47.md |
| tout (79 followers — compositional test) | complete | next-token-findings-tout.md |
| classes (31/33 followers) | complete | next-token-findings-classes.md |
| forks (67/78/48/94) | complete | next-token-findings-forks.md |
| pour (00 followers — all 55 windows) | complete | next-token-findings-pour.md |
| formula-tails (tails of closed formulae) | complete | next-token-findings-formula-tails.md |

Earlier wave (crowd15, also ingested): qui-followers, que/ce-followers,
par-le-and-rest — reports in `code/crowd15/report_inbox/next-token-findings-*.md`.

## Wave 2 (proposed, status: queued)

Spawned by the supervisor when wave-1 batteries resolve or new values promote.
Each beat: extract windows from the repaired 1,847-pair stream, cluster by
follower pattern first, predict from 1840s diplomatic French, rank by
confidence × testability, write to
`code/crowd17/report_inbox/next-token-findings-<beat>.md`. Nulls are results.

| beat | why now | status |
|---|---|---|
| ne-frames (94 followers) | 94="ne" is the top promotion-track target; verify its frames independently of the pre-finder | complete — next-token-findings-ne-frames.md |
| n-e-frames (12/48 followers) | 12="n"/48="e" letter battery needs GT-anchored frame verification | complete — next-token-findings-n-e-frames.md |
| ce45-frames (45 followers) | 45="ce" HOLD (A11) needs the second mirror frame-type | complete — next-token-findings-ce45-frames.md (2026-10-08) |
| bigram-contexts ("le fait" vs "l'[84]", "ne m'", "n'est") | elision behavior decides 84="on" conditions and 94="ne" frames | complete — next-token-findings-bigram-contexts.md |
| post-promotion sweep | re-scan follower contexts after each newly promoted value (94, 12, 48, 77, 33, 78, 30, 39) for second-order predictions | complete — next-token-findings-post-promotion-sweep.md (2026-10-08) |
| 84-adjudication inputs | 62/84 "on" collision: profile 62 ("il" rival) vs 84 (elision-discriminated) | complete — next-token-findings-84-adjudication.md (2026-10-08) |
| noun26-frames | 26 noun-vs-verb war: "…fois, la [26]" ×2 vs "en ce qui 26-37" | complete — next-token-findings-noun26-frames.md (2026-10-08) |
| parvenir-thirds | "vient de me parvenir" thirds (60/62/68) homophone-set test + 83="de" cross-check | complete — next-token-findings-parvenir-thirds.md (2026-10-08) |
| f-qui-par full read | 43/01 profiles + formula French; the 6-gram is resolving from the edges | complete — next-token-findings-f-qui-par.md (2026-10-08) |
| est-reexam | crowd16 est-finder's fenced-leftover challenge vs A1 grant: re-derive fencing window by window for red-team adjudication | complete — next-token-findings-est-reexam.md (2026-10-08) |

## Beat method (all waves)

1. Extract every target occurrence ±3 groups from the repaired stream.
2. Cluster by follower pattern FIRST — same-group clusters are top targets.
3. Predict plaintext from 1840s French diplomatic register.
4. State cipher-testable consequences; rank by confidence × testability.
5. Respect standing constraints (see BATTERY-PROTOCOL.md §7). Never re-litigate
   settled kills. De-duplicate formula windows before counting productive frames.
