# Battery `adj-49-420-366` — verdict: KILL (adjective leg for 49)

- Target: `adj-49-420-366`
- Claim: "resolve the adjective leg's two hostile windows — @366 ('48(e) 49 61': find 49 a host or kill the adjective leg) and @420 ('46(que) 49 36-noun': test re-segmentation or a second class for 49 at this window)"
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue
  untouched.
- Lock: `code/crowd17/next-token/locks/adj-49-420-366.lock` (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"adjective-49 named iff both windows parse with <=1 total unstated assumption; else the adjective leg is killed and the '76 49 24' formula needs a new class"

## Numbered pass/fail clauses (restated before testing, not modified after)

1. **C1** — @366 (`48 49 61`, 49 at 0-based @366) parses under adjective-49.
2. **C2** — @420 (`46 49 36`, 49 at 0-based @420) parses under adjective-49.
3. **C3 (budget)** — total unstated assumptions across C1+C2 is <=1 → name
   adjective-49; else the bar's kill clause fires (adjective leg killed).

## Adopted premises (not re-litigated)

- `formula-49-value` NULL (2026-10-09): 49 fenced class-open; verb,
  determiner, relative/interrogative pronoun killed globally for 49;
  adjective was the leading surviving leg with hostile windows @366/@420.
- 48="e" letter-tier (battery-promoted F86): 48 is a letter, never a
  standalone word. Word-tier 48="est"/"de"/"ne" readings are killed.
- 47="ce" promoted (A4); 46="que" GT; 36=noun class (R18); 29="er" GT
  (syllable); 70="pre" GT; 76=masculine noun (promoted R19).
- `locus-368-fullparse` NULL (2026-10-09, same @362–375 locus): "vere" is not
  a French word (kill-grade dead); bare-'e' standalone is unlicensed
  (kill-grade dead); the full-clause parse of @362–375 is fenced.
- 61's values "pren" (N149) and "son"-possessive (N192) are killed; 61's
  CLASS is open (no standing class verdict).
- §7: 67 is the sole true polyvalence — battery declares no second class.
  §3: never invent values.

## Method

Byte-exact window extraction from the repaired stream (0-based pair
indices). For each hostile window, enumerated the grammatical routes for a
word-tier adjective-49 and counted the minimum unstated assumptions each
route needs. An "unstated assumption" is anything the parse needs that is
not a standing value/grant or the hypothesis under test (49=adjective).

## Window-level evidence (byte-exact, 0-based)

@366 window (row a2_06): `@361=48 @362=76 @363=47 @364=78 @365=48 [@366=49] @367=61 @368=70 @369=17 @370=06`
— i.e. `48 76 47 78 48 [49] 61 70 17 06`.

@420 window (row a2_08): `@416=49 @417=74 @418=74 @419=46 [@420=49] @421=36 @422=29 @423=47 @424=14`
— i.e. `49 74 74 46 [49] 36 29 47 14`. No 94 ("ne") anywhere in @380–419.

## C1 test — @366 ("48 49 61")

49 as a word-tier adjective needs a noun host (attributive) or a copula
(predicative; none present).

Host candidates:
- Left @365=48: letter 'e' (F86) — not a noun. Dead as host.
- @364=78 ('ver' lead), @363=47 ('ce', complete promoted word): neither is
  a noun host; 47 cannot be re-segmented without contradicting its
  promotion.
- @362=76 (promoted masculine noun): 4 cells distant with 47/78/48
  intervening — ungrammatical attachment. Dead.
- Right @367=61: unvalued. Naming 61=noun gives the host:
  "[49-adj] [61-noun]" (pre-nominal, a licensed class-level shape).
  **Assumption #1: 61 is a noun** (class-level; permitted currency, and
  consistent with standing verdicts — only 61's VALUES were killed).

The letter 48='e' @365 must still be accommodated (bare-'e' standalone is
kill-grade dead, adopted). 47='ce' is a complete promoted word, so no word
may span @363–365. Left-attachment "78+48" = "vere" is kill-grade dead
(adopted). Therefore 48 MUST be word-initial on the word to its right —
i.e. 49's word begins with 'e', i.e. **49's VALUE begins with 'e'**.
**Assumption #2: a value-level property of 49** (§3 bars inventing it;
counted here as unstated).

No single assumption covers both needs (host-naming is class-level about
61; 'e'-accommodation is value-level about 49 or 78). Cheapest alternative
(78's value + 'e' forming a word leftward) is likewise value-level plus the
61=noun host: still 2.

**C1 minimum: 2 unstated assumptions. C1: FAIL** (a 1-assumption parse does
not exist; a 0-assumption parse does not exist).

## C2 test — @420 ("46 49 36")

Standing: 46='que' (GT word), 36=noun class (R18), 29='er' syllable
attaches left ("[36]er", consistent with 36=noun, no assumption).

Routes for "que [49-adj] [36-noun]":
1. Relative-"que" + subject + verb: subject "49 36" is determinerless —
   ungrammatical in 1841 French for an ordinary Adj+N (only lexicalized
   determinerless NPs escape, which is value-level). Dead at 0 assumptions.
2. "ne...que" restrictive: no 94 in @380–419. Dead.
3. Comparative "que": needs a licensed comparative head left (74 unvalued;
   assuming one is value-level). Dead at 0 assumptions.
4. Numeral-adjective rescue ("que [49=num] [36] [V]", cf. "les livres que
   deux amis m'ont prêtés"): needs 49's value to be a numeral (value-level)
   AND a verb after "que Num N" ("29→36, 47=ce, 14…" supplies none
   licensed). ≥2 assumptions.
5. Re-segmentation ("que"+49 or 49+36 as one word): needs 49's value (§3).
   Dead at battery grade.
6. Second class for 49 at this window: polyvalence — §7 red-team venue
   only. Not declarable here.

**C2 minimum: ≥1 unstated assumption (realistically ≥2). C2: FAIL.**

## C3 — budget

Minimum total = C1 (2) + C2 (≥1) = **≥3 unstated assumptions**, against a
budget of ≤1. The overrun is already decided at @366 alone (2 > 1).

**C3: FAIL → the bar's kill clause fires.**

## Verdict: KILL — the adjective-49 leg is killed

Scope (explicit):
- Killed: adjective as 49's class. The "76 49 24 26 30 03" x2 frame can no
  longer be read as "N [49-adj] [V-fin]" on the adjective leg.
- Untouched: the strained noun-49 and adverb-49 legs (still open, still
  strained); 49 stays class-open overall; the global kills for 49 (verb,
  determiner, relative/interrogative pronoun) stand.
- No standing or red-team verdict contradicted or downgraded; §7 intact
  (no polyvalence declared); canonical-stream caveat stands.

Consequence (per the bar): **the "76 49 24" formula needs a new class for
49's slot.** Note for supervisor/red team: `formula-76-49-24` (2026-10-09,
promote) licensed the x2 FRAME as a genuine 1841 "N [X] [V-fin]" formula —
the frame license stands; what is now open is the slot-filler class X=49.
The queued `noun-49-909-875` (P4) tests the leading surviving alternative.

Per §4, kills regenerate no follow-ups: none proposed.

## Adverses answered

- None listed on the target.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-adj-49-420-366.md` (this file).
- Queue: `battery-queue.json` — `adj-49-420-366` status `queued` ->
  `verdict`, result `kill`, date 2026-10-09 (temp-file + rename; pre-write
  assert confirmed queued/verdictless; JSON re-validated post-write; only
  this entry's keys touched; no downgrade).
- Lock created at start, deleted at end (verified gone).
