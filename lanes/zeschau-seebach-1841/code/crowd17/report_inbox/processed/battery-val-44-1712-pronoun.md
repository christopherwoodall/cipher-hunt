# Battery report: val-44-1712-pronoun — "44 = pronominal at the @1712 window; frame semantically empty for 65"

- Worker: battery worker val-44-1712-pronoun, agent 55df0b0c-9f1c-467e-a72f-3418c28b90d2
- Date: 2026-10-09 (lock created 2026-10-09T07:53:42Z)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per repair_parse.py). canonical.py NOT used. R5005 untouched.

## Offset alignment (verified in-work, before testing)

- The evidence string "@1710–1716 '06 29 40 65 94 44 59 30 64'" holds 9 tokens; on the repaired stream it spans @1709–@1717: 06@1709 29@1710 40@1711 65@1712 94@1713 44@1714 59@1715 30@1716 64@1717 (row a8_06).
- The target id's "@1712" is the window anchor (65's index); the 44 token itself is at @1714.
- The frame '65 ne 44 est pas' = @1712–@1716 = 65·94·44·59·30.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"Name 44's class at @1712 iff '65 ne 44 est pas' parses with <=1 ungranted assumption; if pronominal, record 'n'est pas 44' as semantically empty for 65's value; if content noun/adjective, its value constrains 65."

Numbered clauses (frozen before testing):

1. **Gate (parse):** the window @1712–1716 reads as '65 ne 44 est pas' using ≤1 ungranted assumption — an "ungranted assumption" = any parse step relying on a value or frame not banked/promoted/provisional in protocol §7 or the evidence field (94=ne battery-level, 30=pas battery-promoted, 59=est provisional all count as granted). PASS/FAIL.
2. **Pronominal branch:** if clause 1 passes AND 44 is pronominal → verdict records 'n'est pas 44' as semantically empty for 65's value (no constraint on 65).
3. **Content branch:** if clause 1 passes AND 44 is a content noun/adjective → the report states the specific constraint its value imposes on 65.
4. **Naming rule:** 44's class at the @1712 window may be named only if clause 1 passes; if clause 1 fails → null.

## Method

- Re-parsed the repaired stream in-work (replication of repair_parse.py: same offsets file, same row file, same tokenization): 1,847 pairs confirmed; n(44)=15; the '94 44' adjacency occurs exactly once stream-wide (@1713→@1714); window tokens @1712–1716 = 65 94 44 59 30 verified byte-exact.
- Standing verdicts coordinated (cited, not re-litigated):
  - battery-noun-44.md (KILL, 2026-10-08): @1714 forces 44 into a clitic slot — a lexical noun cannot intervene between 'ne' and the finite verb; conditional on 94='ne' + 59='est'.
  - battery-pronoun-44-1714.md (NULL, 2026-10-08): the clitic forcing at @1714 is the standing residual; value ∈ {'en','l''} unresolved there.
  - battery-clitic-44-65-discriminator.md (PROMOTE, 2026-10-08): @1714 discriminates to "ne l'est pas" — 44='l'' (elided le/la), window-local; 'en' fenced.
  - battery-clitic-44-census.md (PROMOTE, 2026-10-09): @1714 is the sole clitic-slot window of 44's 15 (12 whole-word nominal + 2 word-internal stem elsewhere).
- No standing verdict re-argued; 94='ne', 30='pas', 59='est' used as granted, not overturned.

## Window-level evidence

- @1712–1716 (row a8_06): 65 · 94='ne' (battery-promoted) · 44 · 59='est' (provisional) · 30='pas' (battery-promoted).
- With 44='l'' (window-local, discriminator promote): "65 ne l'est pas" — grammatical. Elision of le/la before vowel-initial 'est' is standard French phonology, not an ungranted assumption.
- Right context @1717=64='qui' (granted), @1718=47='ce' (granted A4): accepts the clitic parse; no contact discriminator against it.
- '94 44' x1 stream-wide (this window only) — the clitic frame is unique to this window, consistent with the census promote.

## Per-clause verdicts

1. **Gate: PASS** — "65 ne l'est pas" parses under standing values with 0 ungranted assumptions (94, 59, 30 all standing; 44='l'' window-local promoted; elision is standard phonology).
2. **Pronominal branch: FIRES** — 44 at @1714 is pronominal (object clitic 'l''). RECORDED: 'n'est pas 44' ("65 ne l'est pas" = "65 is not it") is **semantically empty for 65's value**. The frame contributes no lexical or type constraint on 65. **Input to noun-65-value: do not mine the @1712–1716 window for a constraint on 65's value; the 'ne 44 est pas' frame is anaphoric, not predicative.**
3. **Content branch: MOOT** — antecedent false (44 is not content noun/adjective at this window; the global noun claim was killed by battery-noun-44).
4. **Naming rule: satisfied** (clause 1 passed) — 44's class at the @1712 window: **pronominal (object clitic; window-local value 'l'' per the discriminator promote)**.

## Adverses (answered, none ignored)

- "44's value open lane-wide": ANSWERED — class named; value not forced beyond the standing window-local assignment (44='l'' at @1714 per discriminator promote; lane-wide value remains open; 'en' fenced there).
- "94='ne' is battery-level": ANSWERED — used as granted standing value; not re-litigated.
- "Coordinate with queued pronoun-44-1714 — scoped to the @1712 window as input to noun-65-value, not a duplicate": ANSWERED — pronoun-44-1714 returned NULL (processed 2026-10-08); its residual was refined by the discriminator promote. This battery answers the downstream question neither adjudicated: the consequence for 65 (semantic emptiness). No duplication.

## Verdict: PROMOTE

Epistemic status (marked up front): conditional on 94='ne' (battery-promoted, pending red-team ratification) and 59='est' (provisional) standing, and on the discriminator's window-local 44='l'' (battery-level promote, pending red-team ratification). Consistent with all standing verdicts (noun-44 kill, pronoun-44-1714 null, discriminator promote, clitic-44-census promote); none contradicted or downgraded. If the red team ratifies escalate-1714-ne44 (queued), this promote and the noun-44 kill must be revisited.

## Follow-ups

None required (promote). Pointer for the supervisor: the discriminator's live-end follow-up antecedent-44-l-prime (locate l''s predicative antecedent) is the open end of this window; noun-65-value (null, 2026-10-09) should treat @1712–1716 as constraint-empty for 65 per clause 2 above.

## Provenance

Every number re-derived from the repaired 1,847-pair stream in-work: window tokens @1709–@1717 byte-exact; n(44)=15; '94 44' x1. No invented data. canonical.py not used. R5005, sealed gates, and the red-team adjudication queue untouched. Lock deleted on completion.
