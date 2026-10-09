# Battery verdict: stem-62-ent-665-1536

**Verdict: NULL** — 62 as verb-stem-final cannot be confirmed or killed at battery grade; no stem can be stated at either window under granted values.

## Bar (verbatim, pre-registered)

> CLAIM: test 62 as verb-stem-final in the two "62-ent" windows
> BARS: test 62 as verb-stem-final at @665/@1536
> ADVERSES: None

Numbered clauses (from class-62-nof94's elaboration of this bar): (1) parse both windows as "[stem]-62-ent" 3pl verbs with stated stems, or kill the stem hypothesis.

Offset note: the queue's @665/@1536 are 0-based pair indices. On the repaired stream they are 1-based @666 (row a4_02) and @1537 (row a8_00). Same windows.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/stem-62-ent-665-1536.lock` on start, deleted on completion. Re-derived the full 1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`). `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.

## Windows (re-derived, byte-exact)

- **Window A** — 1-based @666 (0-based @665), row a4_02:
  `… 86 50 80 03 | 62 06 | 00 20 67 11 86 24 …`
- **Window B** — 1-based @1537 (0-based @1536), row a8_00:
  `… 00 66 73 41 | 62 06 | 21 62 93 88 …`

These are the only two "62 06" windows stream-wide (62 n=35; 06 follows 62 exactly x2).

## Per-clause results

**Clause 1 — FAIL (epistemic, not kill-grade).** No stem can be stated at either window under granted values:

- **Window A.** Two-word reading "…[03] [62]ent…" is ungrammatical: 03 is a verb-stem-family group ("03 29" = "[03]er" infinitive x3, imp-80-set), and a bare infinitive stem directly followed by a finite 3pl verb has no French parse. One-word reading "03-62-ent" (stem "03-62" + "ent") needs 03 = "re-" prefix (e.g. "re-[62]ent" = "reviennent"): ungranted, and 03 as "re" conflicts with 03's independent-word windows ("pas [03]" x3, "[03] qui" x4 — "pas re" is not French). It also needs 80 as a 3pl subject, and 80's battery roles (imperative "80-le" x2, finite "80-ent" x2, infinitive slots x5 — imp-80-set) include no pronominal role. Right context is fine ("[62]ent pour [20]" = finite verb + "pour X", grammatical), so the failure localizes left.
- **Window B.** "…pour [66] [73] [41] [62]ent…" — 'pour' (00, promoted A9) directly governing a finite verb is ungrammatical; no byte evidence (row break, punctuation proxy, clause marker) supports a clause boundary mid-row a8_00. No subject is identifiable: 41's class is open, and 66/73 are open. Even with a subject, the stem would need stating (62 = "vienn"? "donn"? "parl"?) — 62's value is open, so every candidate is invented. Note "21" follows 06: a transitive "[62]ent [21-noun]" is grammatical *only* under a stated transitive stem — again unavailable.

**Not kill-grade.** Neither window forces the claim false. A conditioned word-internal reading (62 stem-final inside a longer word, e.g. "re-vienn-ent" at A) remains logically possible under ungranted values — that is a §7 red-team question, not a battery kill. The failure is epistemic: the bar demands stated stems, and none can be stated.

## Distributional context (supporting, not decisive)

- 06's preceder census: 28 distinct groups precede 06 (42 x5, 82 x4, 30 x4, 14/80/06/62/64/12 x2, 20 others x1). Per wordbound-30-06-importent, 06's left-attachment is bimodal — it is not always a suffix. So "62 06" = stem + "ent" is one attachment hypothesis, not a given.
- 62's other followers invite word-internal readings rather than killing them: 62→94 x9 (e.g. "21 62 94 93 59" — a bare stem before particle 'ne' is ungrammatical, so 94 reads syllabic there), 62→48 x6, 62→98 x5 (the "62 vient" compound-verb lead, e.g. parvenir/devenir family). These are consistent with stem-final 62 as a *conditioned* behavior — recorded, not declared (§7 honored).
- Consistent with class-62-25's NULL: no single independent-word class parses 62's windows; the verb-stem-final reading survives only as a conditioned-split lead.

## Adverses

None listed. Standing-state check: no contradiction — class-62-25 (NULL) and class-62-nof94 (NULL) both leave the stem-final lead open; imp-80-set's 80 findings are used, not re-litigated; nothing downgraded.

## Follow-ups (proposed for supervisor queuing)

1. `subj-62-06-1537` (P3) — test 41's class at @1536: can 41 (or the 66-73-41 phrase) serve as a 3pl subject? If 41 is non-nominal, the finite reading loses its only candidate subject at window B.
2. `re-prefix-03-665` (P3) — test 03 as "re-" prefix at @665 against 03's full profile ("pas [03]" x3, "[03] qui" x4); if 03 cannot be prefixal, the one-stem "re-[62]ent" reading dies at window A.
3. `ent-06-host-census` (P3) — resolve 06's left-attachment bimodality across its 28 preceder groups: at which windows is 06 a finite ending vs a syllable? No "X-06" stem claim can be stated until this is settled.

## Bookkeeping

- Lock `locks/stem-62-ent-665-1536.lock` created on start (agent id + UTC 2026-10-09T03:51:18Z); deleted on completion.
- `battery-queue.json`: target `stem-62-ent-665-1536` queued → verdict/null (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated post-write).
- R5005, sealed gates, red-team adjudication queue untouched. No standing verdict contradicted or downgraded.
