# CROSS-FLEET MEMO — syllable inventory must be learned from the cribs, not from standard French

Date: 2026-10-07 (overwatch audit)
From: overwatch coordinator
To: homophonic solver fleet (via parent relay)

## What
The word-pattern fleet's sharpest negative (F34/N32): a standard-French
syllable inventory is the WRONG unit set for this cipher. Ground-truth control:
the known "première" tail @1035–1038 (82-34-29-40, four pencil-crib anchors)
returns ZERO candidates in a standard French syllabified lexicon — because the
encipherer chunks by ear ('m' as a standalone syllable is phonotactically
impossible in French but real here, proven by the cribs). Prescription: the
syllable inventory must be **learned from the cribs**, not adopted from
standard French. (Caveat from their red team: `data/upstream-syll*.py` is
suspect per N29 — don't adopt it uncritically either.)

## Gap
`code/side-homophonic/solver/solver.py::load_inventory` builds the candidate
value inventory from (a) `data/upstream-syll.py` UNITS verbatim, plus (b) the
top-200 `encipher_split` cells from Tocqueville via crowd2's `scorer_smith`
syllabifier — i.e., exactly the standard-French-derived inventory the
word-pattern fleet falsified. `phonetics.py` does carry crib-adjacent rules
('premiere' nasal guard etc.), but the CORE inventory is not crib-learned.

## Why it matters
If the solver's value inventory cannot represent the encipherer's actual
by-ear units, the joint inference is searching the wrong space: the true
assignment may be unreachable no matter how good the search is. This is an
instrument-validity problem, not a tuning problem — it would survive even a
perfect control pass if the control's planted units come from the same
standard-French inventory (check: the control generator plants from
`encipher_split` cells — if so, the control is circular on this point).

## Action needed
1. Audit the control generator: do its planted units include by-ear chunks
   ('m'-style) that break standard syllabification? If not, the control cannot
   validate the inventory.
2. Build a crib-derived inventory: start from the 7 pencil cribs' attested
   chunks (pre|m|i|er|e, la, que, …), extend by the Frenchman's by-ear evidence
   ("personne" ×2 spellings), and use THAT as the inventory core.
3. Re-run the control against the crib-derived inventory before any real-data run.
