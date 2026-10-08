# Registry Rewrite — downstream reference changes (2026-10-07)

Round-14 registry-restructuring per red-team R-IA1–R-IA7 (GRANTED),
`code/crowd13/adjudicator/RULINGS-ROUND13.md`. New working registry:
`code/crowd14/registry/REGISTRY.md`.

## Changed

1. **`code/council/solver-architecture.md`** — PINS section: "10-islet
   registry → per-group candidate masks" → restructured registry
   (word-rule + class-tier constraints; 67 fork the only
   conditioned-polyvalence mask) + the ×4 non-merge constraints
   (33+86 / 48+94 / 76+78 / 52+59). §6 board-consistency criterion:
   "every islet-registry rule (10 islets)" → "every restructured-registry
   word/frame/class rule … (no 33+86 / 48+94 / 76+78 / 52+59 merges)".
2. **`code/council/systematic-drag.md`** — Source list #3: the "10
   conditioned islets" block (with its four example cell rules) replaced
   by the restructured registry summary + banked falsifiers/fences + ×4
   splits. H4: "islet-only matches don't anchor" → "registry-only matches
   don't anchor". Standing caveat 2: "Conditioned islets are consulted
   with predecessor context only" → "The registry's
   predecessor-conditioned rules are consulted with predecessor context
   only".
3. **`code/crowd13/liaison/smith-constraints.md`** (banked constraint memo
   — its own text said the 10-islet registry was binding UNTIL a red-team
   ruling changes it; R-IA1–R-IA7 did). §3b: prepended a dated amendment
   block giving the new tiering (word rules / sole polyvalence / class
   tier / singleton / kill + ×4 SPLIT constraints); the original 10-islet
   list kept as record, marked superseded where dissolved. §3c
   discriminating windows: item 1 "ISLET-8 frames + ISLET-10 este-arm" →
   "F-qui-le frame + W-este1/W-este2"; item 4 "frozen 06-islet core" →
   "frozen W-ment core".
4. **`code/crowd9/conditioner/islet_registry.md`** (round-9 record):
   supersession pointer added at the top pointing to the new registry;
   the file's content is otherwise untouched as the round-9 historical
   record.

## Deliberately left (historical records — the old framing is the record
of what was believed then)

- `code/council/break-the-frame.md`, `code/council/table-reconstruction.md`
  — the pre-round-13 attack plans that commissioned the compositional
  audit; their mission (Step 1: islet battery) is complete and ruled.
- `code/council/drag/DRAG-REPORT.md` — completed round-13 drag report.
- `REPORT.md`, `NOTES.md`, `STATE.md` — lane history logs; NOT the
  rewriter's to edit (curator owns NOTES/STATE).
- All `report_inbox/processed/*`, `code/crowd3–13` working docs,
  PREREGs, and past `RULINGS-ROUND*.md` — audit-trail records.
- `code/side-homophonic/`, `code/side-wordpattern/`,
  `code/side-rotation/`, `code/side-keyhunt/`, `code/sidepath/`,
  `code/crossfleet/`, `code/crowd10/liaison/`, `code/crowd11/
  smith_liaison/`, `code/crowd12/smithliaison/` — side experiments and
  older liaison memos using the pre-round-13 generic "islet" vocabulary;
  not live registry references.
- `code/crowd9/report_inbox/conditioner-islets.md`,
  `code/crowd9/redteam/RULINGS-ROUND9.md`, `code/crowd9/conditioner/
  PREREG9.md` — round-9 records.

## Verification (against the repaired stream)

Loader `code/crowd13/islet-audit/stream.py` (upstream-ct_R5005.txt +
repaired_offsets.json; NEVER canonical.py). 3 entries re-derived,
2026-10-07:

1. **W-ment** — 06 at [580, 738, 1184, 1355] all «06» with pre=82; full
   82-06 census [579, 737, 1183, 1354] (82-positions). MATCH.
2. **F-qui-le** — @1444: 37-64-77-84-59-36-67; @1800:
   87-64-77-84-59-35-94 (corrected frame-start indices per the docket's
   citation correction). MATCH.
3. **W-par-le** — @47/@465/@960 all read 96-00 (96-positions).
   MATCH.

3/3 byte-exact.

## Ambiguities found in the ruling text (recorded, NOT resolved)

- R-IA1's word-rule bank: the task brief (from the rulings, lines ~284–
  360) names the re-banking as "W-est1 (93-59=«l'est») / W-est2
  (94-59=«n'est») / W-este2 ([stem]-59, stems 84/06/61/44/86, fenced 15)
  / F-qui-est (64-59=«qui est»)". The docket's R-IA1 text uses the same
  names; the names were adopted verbatim. (No conflict found — recorded
  for the curator's traceability.)
- The curator's NOTES.md N60 says the "conditioned polyvalence" tier
  "shrinks to the 67 fork + ISLET 1's frame arms"; R-IA3 re-banks the
  66/89 arms as FRAME rules ("[noun] en [V]"), not as polyvalence. The
  new registry follows the adjudicator's ruling (FRAME tier), not the
  curator's gloss; the curator should reconcile N60's wording.
- R-IA5 moves ISLETS 6/7 "to a class-constraint tier (out of
  polyvalence)" while F-en's frame arms depend on them. If either class
  falls, the corresponding arm reverts to conditional-unanchored per the
  carried dependency note — the ruling does not say whether that
  reversion is a registry edit needing a new ruling; flagged for the
  red team.
- `code/crowd14/registry/REGISTRY.md` itself is the new working
  registry; the crowd14 dir also hosts unrelated round-14 work
  (poly62, prin81, fork78, value52, value59third, report_inbox) — no
  conflict, but the curator may want a crowd14 INDEX.
