# Battery report: quoted-dialogue-goldset — verdict: PROMOTE

## Bar (verbatim from battery-queue.json)
"goldset of >=200 hand-verified dialogue spans; re-run the quoted-drama census method against it to bound OCR-noise impact"

Numbered clauses:
- C1: build a hand-verified dialogue control corpus of >=200 spans — PASS (248 spans, each reviewed head+tail).
- C2: re-run the quoted-drama census method against the goldset and bound the OCR-noise impact — PASS (method re-run verbatim; monster-span impact bounded, see findings).

Adverses listed: none.

## Method
- Extracted dialogue spans from `revue-deux-mondes-1841-q1..q4` with the parent battery's `dialogue_spans()` verbatim (guillemet / dquote / em-dash paragraph): 3,590 spans total (1,409 em-dash, 1,280 guillemet, 901 dquote).
- Stratified random sample of 340 spans (120+120 em-dash, 60 guillemet<=4000ch, 40 dquote<=4000ch, seeds 42/7) plus 25 monster spans (>4000ch); each reviewed head+tail (280-char snippets) by hand, verdict GENUINE vs NOISE with cause.
- Goldset kept: 248 GENUINE spans. Saved: `code/crowd17/next-token/quoted_dialogue_goldset.json` (with provenance, per-span verdict causes).
- Re-ran the parent's DEM/INF patterns verbatim on the goldset (window = dem through next [!?.], cap 180, must contain "!"). Saved: `code/crowd17/next-token/quoted_dialogue_goldset_census.json`.

## Findings
- Review yield: 248 genuine / 340 reviewed (73%). Noise taxonomy: runaway-dquote narrative 27, quoted non-dialogue documents (dispatches, essays, orders) 24, quoted fragments 10, quoted letters 5, mixed narrative-dominated 4, empty/single-dash artifacts 4, em-dash news/essay paragraphs 3, misc 7.
- Monster inventory (25 reviewed, all >4000ch, max 76,250ch): 100% are runaway-quote spans — an opening « or " whose closing mark was dropped/mangled by OCR, swallowing whole articles (5k–72k chars each). 441 such monsters = 12.3% of spans but **83.3% of all "dialogue" chars** (8,589,618 / 10,315,830).
- Census on goldset: 248 spans, 60,338 chars, **4 dem-comma hits, 0 exclamatory candidates**.
- De-monstered re-run (spans <=4000ch): 3,149 spans, 1,726,212 chars, 47 dem hits, **3 exclamatory candidates — the same 3 unique windows as the parent's 6** (the parent's other 3 were duplicates: runaway dquote monsters had swallowed the same em-dash dialogue text, double-counting identical windows).
- The 3 unique candidates manually classified (parent taxonomy): "cela, un vagabondage eternel, sans but !" (exclamatory NP, no infinitive), "cela, papa !" (vocative, no infinitive), "cela, vous!" (fragment, no infinitive) — **0 genuine** dislocated-demonstrative + bare exclamatory infinitive anywhere: not in the goldset, not in the de-monstered corpus, not in the monsters.
- **OCR-noise bound**: monsters contribute 83% of dialogue chars and 72% (122/169) of dem-comma hits yet yield **zero unique candidates**; de-monstering changes the candidate set not at all (3 unique windows before and after). The parent battery's null result is robust to the monster-span noise — the noise dilutes rates but does not hide or fabricate candidates.

## Scope
- Bounds OCR noise for the quoted-drama census only (rdm-q1..q4, D1/D2/D3 spans, DEM/INF patterns verbatim). Does not re-litigate the parent's candidate taxonomy beyond the 3 unique windows. The goldset is a control corpus for dialogue-window methods, reusable by sibling batteries.
- No standing/red-team verdict contradicted; §7 intact; `canonical.py` never used (this battery touches only the period corpus, not R5005).

## Bookkeeping
- Lock: created on start (2026-10-09T15:24:09Z), deleted on completion.
- Scripts/data: review sheets and verdict log in worker notes; goldset + census JSON saved under `code/crowd17/next-token/` as above.
- Queue: `quoted-dialogue-goldset` → status verdict, result promote, 2026-10-09 (own entry only; temp-file + rename; pre-write assert passed: was queued/verdictless; no downgrade).
- Per §4 (promote): no follow-ups required.
