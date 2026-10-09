# Battery verdict: adj-frame-995-solo

**Verdict: PROMOTE (frame-level)** — '03 60 67' @995 parses as '[03-N] [60-adj] et[67] la[11]' postnominal with independently supported 03-nominal anchors and zero contradictions. Frame promoted; 60's VALUE is not named here (poly-60-redteam owns the global adjudication).

## Bar (verbatim from battery-queue.json)

promote-frame iff '03 60 67' @995 parses as '[03-N] [60-adj] et[67] la[11]' postnominal with 03 nominal independently supported ('ce [03]' x2 @1014/@1790 via granted 47='ce'; 'le [03]' @722; '03 64' x4; 'pas [03] qui' @30) + zero contradictions

Numbered clauses:
1. '03 60 67' @995 parses as '[03-N] [60-adj] et[67] la[11]' postnominal.
2. 03 nominal independently supported: 'ce [03]' x2 via granted 47='ce'; 'le [03]'; '03 64' x4; 'pas [03] qui' @30.
3. Zero contradictions.

Adverses: none beyond the 67 positional rule (follower 11='la' banked).

## Method

Read BATTERY-PROTOCOL.md first. Tested ONLY against the repaired 1,847-pair stream (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt parsed per repair_parse.py; canonical.py never touched). All @-offsets below are 0-based on that stream; the brief's @-numbers are +1 (brief @995 = stream @994 for the trigram start; 60 sits at stream @995, 67 at @996).

## Window-level evidence

- '03 60 67' occurs x1 on the repaired stream, at @994 (stream): `30 03 60 67 11 96 82 33` = "pas[30, banked] [03] [60] et[67] la[11, banked] par[96] m[82] [33]". Frame unique — confirmed.
- Clause 1: PASS. The 4-gram parses as [03-N] [60-adj] et[67] la[11]: nominal 03, postnominal adjective 60 (French N-adj order), 67='et' (follower 11='la' is banked ground truth, non-infinitive-shaped → 'et' per the sole-polyvalence positional rule), 'la' article. The wider left edge "pas 03" (@993='pas' banked) is itself nominal-compatible ("pas [N] [adj] et la..."). No parse failure.
- Clause 2: PASS. Independent nominal support for 03, all re-derived:
  - 47-03 x2 @1013, @1789 (brief @1014/@1790): 47='ce' granted (A4) → "ce 03" demonstrative+nominal.
  - 77-03 @721 (brief @722): 77='le' provisional → "le 03".
  - 03-64 x4 @31, @336, @674, @1645: 64='qui' promoted → "03 qui" relative-clause head — nominal.
  - 30-03-64 @30 (brief @30): "pas 03 qui" — nominal.
  - 30-03 x3 @30, @656, @993 (the @993 instance is the immediate left edge of the @995 window).
- Clause 3: PASS. Zero contradictions. 60's noun reading was killed (standing); no window forces a non-adjective parse at @995. The adj-frames-995-637 null report's C2 block concerned @637's coordinated-adjective parse (needs red-team ruling on 89's class) — explicitly out of this narrow re-bar's scope. @995 sitting inside verb-60's V3 window list is a queued coordination note, not a contradiction; this battery does not re-litigate verb-60's bar.
- Adverse (67 positional rule): answered — follower 11='la' banked ground truth, not infinitive-shaped; '67 11' x4 on stream corroborates the et-reading.

## Verdict

**PROMOTE (frame-level).** All three bar clauses pass and the sole adverse is answered. Promoted: the @995 postnominal-adjective frame '[03-N] [60-adj] et[67] la[11]'. NOT promoted: any value for 60 (unnamed), any global class claim for 60 — those belong to poly-60-redteam. No standing verdict contradicted or downgraded. R5005, sealed gates, and the red-team adjudication queue untouched.
