# Battery report: leftedge-60-value (KILL — the 'de' arm at @1736–1739's left edge is dead)

**Target:** leftedge-60-value — "name 60 at @1735 to decide the 'de' arm of F2"
**Worker:** 6d5ccb46-491f-42c2-9c32-dfebc9db6267 | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py; asserts 1847/96 held in-session). Never canonical.py. No R5005 touched. No data invented. Every @-offset re-derived from the stream.
**Offset convention:** lane @ = 0-based stream index (matches leftedge-52-86-1736, split-60-verbs, adj-60-2160).
**Canonicality caveat:** row a8_07's offset is one of the 68 unvalidated upstream offsets — canonical-stream verdict per protocol.

## Bar (verbatim from battery-queue.json)

"name 60 under standing values; the named value decides whether @1736-1739's left edge hosts the 'de' arm"

## Bar as numbered clauses (pre-registered before testing)

1. (C1) A French value for 60 is named under standing values (≤1 ungranted assumption), parsing @1735.
2. (C2) The named value decides whether @1736-1739's left edge hosts the 'de' arm (F2's "[60]=de" arm: @1736-1739 = "[60=de] ne [52-86-INF]" on the corpus-attested "de ne [INF]" pattern).

## Method

1. Re-derived the repaired stream in-session; asserted 1,847 pairs / 96 types.
2. Byte-confirmed the locus: @1734-1739 = `06 60 12 48 52 86` (row a8_07); left edge @1728-1733 = `24 30 15 01 56 30`; so @1732 = 30, @1733 = 06, @1735 (target) = 60, @1736 = 12, @1737 = 48, @1738 = 52, @1739 = 86.
3. Ran 60's full census (n=18) and 06's full census (n=44) with ±4 context.
4. Adopted as premises (not re-litigated): split-60-verbs PROMOTE (finding grade — @1735 is V6 of the ent-60 verb arm: "ent[06] [60] …"), adj-60-2160 PROMOTE (adjective arm at the four '21 60' windows only), stem-03 battery PROMOTE (03 = verb stem, class-level), 30 = 'pas' (red-team promoted, complete word), 06 = 'ent' (promoted value; verb ending / syllabic).
5. Standing values used: 12='n' + 48='e' (R17 letter grants), 64='qui', 96='par', 47='ce', 29='er' (banked GT).

## Window-level evidence (@-offsets)

**The locus (byte-exact):** @1732-1739 = `30 06 60 12 48 52 86` = "pas[30] ent[06] [60] n[12]e[48] [52] [86]".

**60's full census (n=18, lane @):** @120, @173, @198, @233, @323, @455, @638, @691, @701, @996, @1339, @1367, @1475, @1564, @1645, @1675, @1691, @1736(0-based 1735).
Successor profile: 03 x4 (@691 '29 60 03', @1367 '14 60 03', @1645 '98 60 03', @1675 '92 60 03'), 08 x2, 71 x2, 67 x2, 12 x2 (@700, @1735), 90/09/15/65/06 x1.

**06's profile (n=44):** successors spread (77 x6, 00/11/29 x4, 67 x3…); predecessors include 30 x4. '30 06' bigram x4 stream-wide.

## Per-clause pass/fail

**Clause 1 (name 60) — FAIL at null grade.**
No value is nameable for 60 at @1735 under standing values:
- ent-60-verb-arm syllable: unnameable (verb-60-ent already null — adopted, not duplicated).
- Adjective: licensed only at the four '21 60' windows (adj-60-2160); @1735's frame ("ent [60] n…") does not admit it, and declaring it here would be polyvalence (red-team venue per §7; poly-60-redteam queued).
- Noun: killed globally (noun-60).
- "de": killed — see Clause 2 legs.

**Clause 2 (decide the 'de' arm) — the 'de' arm is KILLED at kill grade. Two independent legs.**

**Leg A (boundary — kill grade).** F2's arm needs the parse "… [06] | de[60] | ne[12-48] | [52-86 INF]", i.e. a word boundary 06|60 with 60 a free word. 06 = 'ent' cannot terminate left of 60:
- (i) Standalone "ent" is not a French word — kill-grade language fact (06's standing value is the verb ending / syllabic 'ent', never a free word).
- (ii) 06 cannot attach left: @1732 = 30 = 'pas' is a red-team-promoted complete word; "pasent" is not French and would contradict the promoted value.
- (iii) 06 therefore attaches right — the standing ent-60 arm (split-60-verbs PROMOTE, finding grade: @1735 = V6 "ent[06][60]…"), making 60 word-internal.
A word-internal syllable cannot simultaneously be the free preposition "de". No grammatical parse hosts "de" at @1735. The arm's antecedent ("60 takes 'de'/de-class value") is dead at this window.

**Leg B (value — supporting).** 60 = "de" as a uniform value is unsupported and contradicted: 60's successor 03 x4 (@691, @1367, @1645, @1675) is verb-stem-shaped (stem-03 battery PROMOTE, class-level; re-prefix-03-665 confirms 03 a free stem, "re-" killed); "de" + bare verb stem is ungrammatical 1841 French (a preposition governs a noun or infinitive, never a bare stem). A value is uniform per §7 — dead at four windows ⇒ dead at @1735. §7 additionally bars a third class for 60 at battery grade (adjective-vs-verb is already red-team venue; noun is killed).

**Decision:** @1736-1739's left edge does NOT host the 'de' arm. F2's antecedent is dead; the leftedge stays on F1's working arm ("[60] ne [52] [86]") — whose own 60-value problem is noted below, not decided here.

## Adverses

- "coordinate with open 60-value work (split-60-verbs, adj-60-2160 verdict), do not duplicate" — ANSWERED: split-60-verbs PROMOTE adopted as the premise that makes Leg A work (ent-60 arm at V6); adj-60-2160 PROMOTE untouched (different windows, no conflict). Neither bar re-run.
- F2's own 52-86-unit bar not duplicated — this battery decides only the 'de' arm via the 60/06 boundary.

## Red-team consistency check

- No red-team verdict on 60 exists (poly-60-redteam queued, pri 1) — nothing contradicted, nothing overwritten.
- split-60-verbs PROMOTE (finding grade): upheld and relied upon.
- Parent leftedge-52-86-1736 NULL (clauses 2–3: boundary before @1742 stated; A9 intact): untouched — this battery decides only the F2 'de' arm, not the "ne [52] [86-INF]" frame.
- §7 sole-polyvalence rule: honored — no polyvalence declared.

## Verdict

**KILL** — the 'de' arm of F2 at @1736-1739's left edge is dead at kill grade (Leg A: 06='ent' cannot stand or attach left, so 60 is word-internal under the standing ent-60 arm and cannot be free "de"; Leg B: 60="de" as a uniform value is contradicted by the 03 x4 verb-stem successors). Per protocol §4, kills regenerate no follow-ups.

**Observation for the supervisor (not a finding):** F1's subject-noun arm for 60 at @1735 also lacks a nameable value (noun-60 killed globally) — the leftedge's left edge is value-open on both arms. The parent's "ne [52] [86-INF]" frame (x3) stands on its own legs, unaffected by this kill.

---
Lock: locks/leftedge-60-value.lock created 2026-10-09T09:12:10Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No red-team verdicts modified.
