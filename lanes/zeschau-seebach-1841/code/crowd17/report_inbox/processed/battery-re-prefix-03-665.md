# Battery verdict: re-prefix-03-665

**Verdict: KILL** — the one-stem 're-[62]ent' reading dies at window A.

## Bar (verbatim from battery-queue.json, pre-registered)

> "if 03 cannot be prefixal, the one-stem 're-[62]ent' reading dies at window A"

**Restated as numbered pass/fail clauses:**
- **C1:** Enumerate all 20 of 03's windows; test the 're-' prefix parse at each (a bound prefix must attach to a following stem; it never stands as an independent word).
- **C2:** KILL iff any window forces a non-prefixal (independent-word/stem) parse at kill grade → 03 cannot be prefixal → the one-stem 're-[62]ent' reading dies at window A.
- **C3:** PROMOTE iff the prefix parse survives all 20 windows with stated cause.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/re-prefix-03-665.lock` on start (UTC 2026-10-09T09:05:27Z), deleted on completion. Re-derived the repaired 1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`; asserts 1847 pairs / 96 groups hold). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. Window A = 1-based @666 (0-based @665), row a4_02: `… 80 03 | 62 06 | 00 20 …` (the parent battery's Window A, byte-exact).

Coordinate with stem-03 (adverse): stem-03 already returned verdict/promote (03 = verb stem, class-level) — used as a premise, not re-litigated, not duplicated.

## Census (n(03) = 20, 1-based @, center = 03)

| @ | left | right | row | prefix-parse outcome |
|---|------|-------|-----|----------------------|
| 32 | 30 | 64 | a1_00 | FAILS (E2+E3) |
| 337 | 40 | 64 | a2_05 | FAILS (E3) |
| 600 | 40 | 39 | a4_00 | untested (word-internal-e context) |
| 658 | 30 | 62 | a4_02 | FAILS (E2) |
| 665 | 80 | 62 | a4_02 | window A (the reading under test) |
| 675 | 80 | 64 | a5_00 | FAILS (E3) |
| 692 | 60 | 39 | a5_00 | untested |
| 723 | 77 | 91 | a5_02 | untested |
| 887 | 37 | 02 | a5_08 | untested |
| 995 | 30 | 60 | a6_01 | FAILS (E2) |
| 1015 | 47 | 24 | a6_02 | untested |
| 1031 | 01 | 29 | a6_03 | FAILS (E1) |
| 1238 | 10 | 40 | a7_01 | untested |
| 1321 | 24 | 29 | a7_04 | FAILS (E1) |
| 1368 | 60 | 30 | a7_06 | FAILS (E2-mirror: "re pas" ungrammatical) |
| 1595 | 81 | 29 | a8_02 | FAILS (E1) |
| 1646 | 60 | 64 | a8_04 | FAILS (E3) |
| 1650 | 10 | 38 | a8_04 | untested |
| 1676 | 60 | 39 | a8_05 | untested |
| 1791 | 47 | 00 | a8_09 | FAILS (E4: "ce re pour" ungrammatical) |

## Kill-grade evidence (three independent families)

**E1 — "03 29" x3 (@1031, @1321, @1595): forces verb-stem status.**
29="er" is banked ground truth. "03 29" = [stem]+"er" infinitive — three independent frames per battery-promoted stem-03 (F1: "faire [03]er" @1321 with 24='faire' battery-promoted; F2: exclamatory "[03]er!" @1031; F3: 80-frame infinitive @1595). If 03 = "re-", then "03 29" = "re"+"er" = "reer". No French infinitive "reer" exists: corpus census over `code/side-period/corpus/` finds zero genuine attestations (the single `\breer\b` hit is OCR noise, "reer'd", in a garbled passage of vigny-chatterton-1835.txt; all other "reer" substrings are medial in é-stem verbs like "créer"/"agréer", which confirm the morphology point — "-er" attaches to a stem with content, never to a bare prefix). A bound prefix cannot serve as the entire stem of an infinitive; the stem slot would be empty. Kill-grade: 29="er" is pencil GT; the causative "faire [03]er" frame is grammatical only with a real verb.

**E2 — "30 03" x3 (@31, @657, @994): forces verbal (independent-word) status.**
30="pas" is red-team promoted (R17; table-registry cells ["pas","prom"]). In French, "pas" directly precedes a verb (infinitive or finite) — "pas re" with a bare bound prefix is ungrammatical. At @31 the frame is "pas [03] qui [32]" — 03 is simultaneously the verb of the negation and the head of the relative clause. A prefix cannot occupy either slot. Kill-grade: 30="pas" is a red-team value grant. Mirror: @1368 "60 03 30" = "[03] pas" — "re pas" is equally ungrammatical (supporting).

**E3 — "03 64" x4 (@32, @337, @675, @1646): forces word (relative-clause head) status.**
64="qui" is promoted/granted (protocol §7). A relative pronoun requires a head; a bound prefix followed by "qui" with no intervening stem is morphologically impossible ("re-qui" is not a French word; corpus: no such form). Each window forces 03 to be a nominal or verbal head of the "qui" clause. Kill-grade: 64="qui" is a standing grant, and the morphological impossibility is value-independent.

**E4 — @1791 "47 03 00 86":** 47="ce" granted (A4), 00="pour" promoted (A9). "ce [03] pour [86]" — "ce re pour" is not French; 03 must be a word (noun or verb). Supporting (one window, not the primary kill).

## Per-clause pass/fail

- **C1: PASS** — all 20 windows enumerated; the prefix parse fails at 11 of them (7 kill-grade across E1–E3, 1 mirror, 1 E4; 9 windows untested but irrelevant — C2 needs only one kill-grade failure).
- **C2: FIRES** — three independent families force non-prefixal parses at kill grade. 03 cannot be prefixal as a uniform value.
- **C3: does not fire.**

## Verdict rationale

Under §7 (67 is the sole true polyvalence), 03 cannot be simultaneously a bound "re-" prefix (required for the "re-[62]ent" one-stem reading at window A) and an independent verb stem elsewhere (forced by E1–E3) without a red-team polyvalence declaration. The bar's conditional fired: **03 cannot be prefixal, so the one-stem 're-[62]ent' reading dies at window A** (1b@666, row a4_02).

Scope: kills only the "re-" prefix avenue for the one-stem reading at window A. Other word-internal compositions of "03 62 06" (with different prefix values) were not tested. Converges with — does not duplicate or downgrade — stem-03's battery PROMOTE (03 = verb stem, class-level). 80's subject role (imp-80-set's venue) and 62's stem value were not re-litigated.

Adverses: "coordinate with queued stem-03" — satisfied: stem-03's promote adopted as premise; its bar not duplicated.

No standing or red-team verdict contradicted; §7 intact. No follow-ups mandated (kill, not null); the parent's sibling follow-ups (`subj-62-06-1537`, `ent-06-host-census`) remain queued for the supervisor.

Caveat: row a4_02's offset is one of the 68 unvalidated upstream offsets (canonical-stream verdict per protocol).

## Bookkeeping

- Lock `locks/re-prefix-03-665.lock` created on start (UTC 2026-10-09T09:05:27Z); deleted on completion.
- `battery-queue.json`: target `re-prefix-03-665` queued → verdict/kill (own entry only, temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated post-write).
- R5005, sealed gates, red-team adjudication queue untouched. No invented numbers; every count re-derived from the repaired stream.
