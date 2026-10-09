# Battery report: valency-maugreer-56

- Target id: `valency-maugreer-56`
- Date: 2026-10-09
- Worker: battery worker (subagent 6bfe4fe7-8a10-4cab-9aec-12675920260e)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
- Parent: null-mandated follow-up of `xeent-register-tiebreak` NULL (2026-10-09). Sibling `valency-56-wide` NULL (2026-10-09) owns the wide valency sweep; this battery does not duplicate its bar (coordination in §C4).

## Bar (verbatim, pre-registered)

"kill maugreer iff 'qui maugree [37-predicative]' is ungrammatical at valency grade; coordinate with valency-56-wide; do not duplicate its bar"

Numbered clauses (frozen before testing, not modified after):

1. C1 — Establish maugreer's valency arms from the lexicon (Littre v.n. per the parent fetch; TLFi checked in-session): does any arm license a predicative complement after the finite verb?
2. C2 — Test the @795 construction 'qui maugree [37-predicative]' (37 pinned predicative per A1, standing §7 grant): grammatical or ungrammatical at valency grade? Corroborating instance @1654 ('01 56 37') carries the same frame.
3. C3 — Test @1745's frame 'ne m que maugreent [65]' (objectless 3pl + postverbal subject 65): compatible or incompatible with maugreer's valency?
4. C4 — Coordination: state the relation to valency-56-wide's bar without duplicating it. Kill maugreer iff C2 finds the predicative construction ungrammatical at valency grade.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/valency-maugreer-56.lock` on start (agent id + UTC timestamp); deleted on completion.
2. Byte re-derivation of the "56 37" bigram census and the three named windows from the repaired stream (0-based pair indices).
3. Lexicon check: Littre premise inherited from the parent's 2026-10-09 fetch (littre.org re-fetch attempted in-session, HTTP 403 — premise flagged, not re-verified; see caveats). TLFi entry for MAUGREER verified in-session via cnrtl.fr (independent source, fetched 2026-10-09).
4. Standing premises adopted, not re-litigated: 64='qui' (banked), 37/32/42 predicative frames (A1 grant, §7), 56 whole-word verb-shaped (stem-56-whole PROMOTE per the sibling battery).

## Window-level evidence (byte-confirmed, 0-based)

- **@795** (row a5_04): `64 46 07 64 56 37 44 77 86` — "...[07] qui [56] [37]...". The brief's 'qui [56] [37]' predicative frame. 64='qui' granted: relative subject + finite 3sg verb + 37 in postverbal complement position.
- **@1654** (row a8_04): `38 82 16 01 56 37 11 24 48` — "[16] [01] [56] [37]...". Second instance of the same "56 37" frame.
- **"56 37" bigram census:** exactly 2 occurrences in the whole stream (@795, @1654). No other 56 window places 37 postverbally.
- **@1745** (row a8_08): `34 94 82 46 56 40 06 65 34` — "ne m que [56]e ent [65]". Xeent-class 3pl (40='e' + 06='ent'), no object, postverbal subject 65.
- **@1626** (row a8_03): `66 67 33 46 56 69 26 00 33` — 56 followed by 69, not 37; outside this bar's scope (noted, not graded).
- **A1 spot-check re-derived in-session:** 59->37 x6 (37's top predecessor is 59, 6/28) — the predicative grant stands as adopted.

## Lexicon findings

- **Littre (parent fetch 2026-10-09, adopted as the bar's premise):** maugreer = v.n. (verb neutre = intransitive), "Temoigner son mauvais gre, son mecontentement en pestant, jurant". No transitive arm. Premise correction stands: NOT marked 'fam.'.
- **TLFi (verified in-session, cnrtl.fr):** A. Emploi intrans. — "Montrer sa mauvaise humeur, son mecontentement... en prononcant des paroles a mi-voix"; complements only via "apres/contre + subst." and "de + inf.". B. Emploi trans. — 1. "Vx, litter. Maudire quelqu'un, blasphemer" (object = a PERSON); 2. "Dire quelque chose a mi-voix" (attested 1875 — postdates the 1841 dispatch); 3. pronominal reciprocal.
- French grammar (valency grade): predicative complements attach to copulas and the closed attributive-verb set (etre, devenir, sembler, rendre, trouver, croire, juger...). "Maudire" is not an attributive verb; intransitive "maugreer" has no complement slot at all.

## Per-clause results

- **C1: PASS (established).** Under the bar's Littre premise, maugreer is purely intransitive: zero postverbal complement slot. The TLFi transitive arm exists but is (a) marked "Vx, litter.", (b) outside the bar's Littre authority, (c) person-object-only ("maudire quelqu'un") — it cannot license a predicative adjective complement either.
- **C2: FAILS at kill grade — the construction is ungrammatical.** 'qui maugree [37-predicative]': with 37 in predicative complement position after the finite verb, intransitive maugreer has no slot for it — ungrammatical at valency grade, regardless of 37's value. The TLFi transitive arm does not rescue the PREDICATIVE reading (its object selects a person NP, not a predicative adjective; and "maudire" is not an attributive verb). Both "56 37" windows (@795, @1654) instantiate this frame. **Kill condition FIRES.**
- **C3: COMPATIBLE — no kill from @1745.** 'ne m que maugreent [65]' (objectless 3pl + postverbal subject) parses cleanly under the intransitive arm ("que ... ne maugreent" restrictive + subject 65). @1745 does not contradict maugreer; the kill rests on C2 alone, as the bar specifies.
- **C4: COORDINATED, not duplicated.** valency-56-wide's bar tested all nine candidates against the frame read as "object/predicative" (ambiguous) and returned FITS for maugreer via the TLFi transitive arm. This battery pins 37 predicative per A1 (the standing §7 grant the wide bar left unpinned) and tests the predicative construction specifically: the wide bar's FITS depended on the unpinned reading plus a non-Littre arm. This kill narrows the wide battery's NULL fence; it does not overturn any verdict (the fence had no result) and contradicts no red-team adjudication.

## Discrimination note (why this kill is maugreer-specific, not a frame kill)

The other seven surviving candidates are v.a. in Littre (creer, agreer, suppleer, recreer, greer, degreer, procreer): while 37's VALUE stays open, they retain the direct-object parse of "qui [56] [37]" (a nominal 37 parses as object). Maugreer uniquely lacks the object escape hatch under the bar's Littre premise — intransitive, no slot — so the A1 predicative pin leaves it with no grammatical parse where the transitives keep one open. (reer was already killed on register.)

## Adverses

None listed on the target. Answered anyway: the wide battery's "FITS (all 9)" at W795 is addressed in C4 — it used the unpinned frame and the TLFi arm, both superseded by this bar's pin and premise.

## Caveats (fenced, not hidden)

1. **littre.org not re-fetched in-session (HTTP 403).** The "Littre = v.n." premise is inherited from the parent's 2026-10-09 fetch, recorded in the target's evidence field. If that fetch is ever corrected, this kill re-opens.
2. **TLFi B. transitive arm ("maudire quelqu'un", vx/litter.) is real.** Fenced because it is outside the bar's Littre authority and marked old-fashioned/literary. Narrow escape hatch, stated precisely: even admitting the arm, the kill stands unless 37's VALUE is a person-denoting nominal (value open) — follow-up `sel-37-pressure` (already queued) decides it.
3. **Depictive-adjunct and clause-boundary re-reads** ("qui maugree, [37]") are DIFFERENT frames requiring comma intonation or a boundary absent from the bytes. Not graded here; a depictive battery could test them.
4. @1626 ('33 46 56 69...') not graded — outside the bar's scope.

## Verdict: KILL

'qui maugree [37-predicative]' is ungrammatical at valency grade under the bar's Littre v.n. premise (no complement slot; the predicative-complement position cannot attach to an intransitive verb, and the fenced transitive arm licenses person objects only, not predicative adjectives). Both "56 37" windows (@795, @1654) instantiate the killing frame. @1745 is compatible and does not block the kill. No standing or red-team verdict contradicted; §7 intact.

## Bookkeeping

- Queue: `valency-maugreer-56` → `verdict`/`kill`, 2026-10-09 (temp-file + rename; pre-write assert passed — was queued/verdictless; JSON re-validated; own entry only).
- Report: `code/crowd17/report_inbox/battery-valency-maugreer-56.md` (this file).
- Lock created on start, deleted on completion (verified gone). `canonical.py` never used; R5005, sealed gates, red-team queue untouched.
- Conditional follow-up (not null-mandated; for the supervisor's discretion): if the red team ever admits the TLFi B. transitive arm as period-valid for this dispatch, re-test maugreer against the named value of 37 from `sel-37-pressure` — a person-denoting nominal 37 would reopen the kill.
