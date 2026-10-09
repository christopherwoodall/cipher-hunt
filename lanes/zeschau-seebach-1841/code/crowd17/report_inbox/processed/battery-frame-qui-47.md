# Battery report: frame-qui-47 — 76/68 verb-hood ("qui ce" vs "qui se")

## Bar (verbatim from queue)
"resolve iff 76/68 verb-hood decided by contact profiles"

## Bar restated as numbered clauses
1. 76's verb-hood is decided by its contact profile (n=21).
2. 68's verb-hood is decided by its contact profile (n=8).
3. If both are verbs, the "qui se [76/68]" reading (47='se') is live; otherwise it dies.

## Method
Read BATTERY-PROTOCOL.md first. Created `locks/frame-qui-47.lock` on start. Re-derived the full 1,847-pair stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (pair count verified: 1,847; 96 types). Never touched `canonical.py`, R5005, sealed gates, or the red-team queue. All @-offsets 0-based.

Standing constraints honored: 47="ce" GRANTED (A4, allophone tier); 76=noun LEAD (registry), battery-PROMOTE "76 = noun, masculine" (`battery-noun-76.md`, "le [76]" x3 determiner legs); 79="tout", 77="le" provisional, 59="est" provisional, 06="-ent" promoted, 21 noun-class ("suite" lead), 67 et/veut sole polyvalence (§7).

## Target windows
- @1271–1273: `64 47 76` — "qui ce [76]"
- @1717–1719: `64 47 68` — "qui ce [68]"

## Clause 1: 76 verb-hood — DECIDED, NEGATIVE (kill-grade)
76 = noun at battery grade (standing battery PROMOTE "76 = noun, masculine", never downgraded per protocol). Contact profile confirms:
- Determiner legs: "77 76" x3 (@833 "ce la le [76]", @892, @969) — "le [76]", exactly the promote legs.
- "94 76" x2 (@652, @1577) = "ne [76]" — ne + noun is ungrammatical as a verb frame; consistent with noun (94's syllabic/word-final face).
- Followers 42 x3, 49 x3, 47 x4, 87 x2 — nominal-adjacent, never clitic/verb-shaped.
- Verb-ish contacts ("64 76" @487, "98 76" @13, "67 76" x2 @200/@1046) exist but do not overturn the standing promote at battery level; they are residuals, not refutations. A noun/verb polyvalence declaration is red-team's act (§7), not available here.
Verdict on 76: NOT a verb. Verb-hood is kill-grade dead against the standing battery verdict.

## Clause 2: 68 verb-hood — DECIDED, NEGATIVE
n=8. Full windows:
- @114: `93 29 89 68 21 67 14` — "[89] [68] suite"
- @504: `40 56 39 68 21 67 77` — "[39] [68] suite"
- @884: `08 31 79 68 37 03 02` — "tout [68] [37]"
- @1286: `32 98 55 68 00 11 17` — "[55] [68] pour la fois"
- @1384: `13 24 65 68 52 82 16` — "[65] [68] [52] m [16]"
- @1442: `85 01 52 68 59 37 64` — "[52] [68] est [37] qui"
- @1719: `30 64 47 68 06 11 52` — "pas qui ce [68]ent la [52]"
- @1788: `82 96 21 68 47 03 00` — "m par suite [68] ce [03] pour"

Non-verb frames dominate:
- "79 68" @884: "tout [68]" — tout adverb + adjective/noun; "tout" + finite verb is ungrammatical.
- "68 21" x2 (@114, @504): "[68] suite" — bare "suite" as direct object of a verb is ungrammatical; noun/adjective + "suite" is the natural frame.
- "21 68" @1788: "suite [68]" — noun + adjective, the classic frame.
- "68 59" @1442: "[68] est" — subject + copula frame.
The single verb-shaped leg is "68 06" @1719 ("[68]ent", 3pl -ent). Per the wordbound-30-06-importent battery, 06's left-attachment is bimodal (attaches to stems and stands word-initial), so one 06-contact cannot carry verb-hood against four non-verb frames. 0/8 windows require a verb.
Verdict on 68: NOT a verb. Profile leans adjective/nominal; no verb support.

## Clause 3: the "qui se" reading — DEAD
The se-alternative requires BOTH 76 and 68 to be verbs ("qui se [verb]" is the only natural parse; "qui se [noun]" is ungrammatical). 76 is battery-promoted noun; 68 has no verb profile. Both windows' "qui se" parse is impossible. The 'qui-47' x2 evidence therefore does NOT support 47='se'. 47="ce" (A4 granted) stands undisturbed.

## Per-clause results
- C1: PASS (76 verb-hood decided: dead)
- C2: PASS (68 verb-hood decided: dead)
- C3: PASS (se-reading dead at both windows)

## Verdict: KILL
76/68 verb-hood is dead at battery grade. The "qui ce [76/68]" windows feed no 47='se'-after-infinitives hypothesis.

## Escalation note (not a finding)
76's verb-ish contacts ("qui [76]" @487, "vient [76]" @13, "et/veut [76]" x2) would be a noun/verb polyvalence question, but §7 reserves polyvalence declarations to the red team; not declared here.

## Bookkeeping
- `battery-queue.json`: `frame-qui-47` queued → verdict/kill via temp-file + rename (pre-write assert confirmed no prior verdict; JSON re-validated).
- Lock created on start, deleted on completion. No standing verdict contradicted or downgraded.
