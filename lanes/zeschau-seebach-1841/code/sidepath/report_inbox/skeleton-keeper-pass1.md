## skeleton-keeper: pass-1 skeleton built + verified
- Context: Standing up the side-path's canonical applied-value ledger. The Slider
  needs one file that says, for each of the 1,846 pair positions (0-indexed),
  which value (if any) the lane currently endorses, with an honest status tag.
  Pass 1 applies only the inventory the coordinator approved today — nothing
  was promoted or killed on my authority.
- Decision: Built `code/sidepath/skeleton.json` via `code/sidepath/build_skeleton.py`
  (re-runnable; bumps the pass counter on later promotions). Applied the full
  17-group inventory: 7 ground-truth pencil cribs; 6 provisional (87=ce
  provisional-strengthened, 64=qui provisional with re-promotion BLOCKED,
  96=par, 94=ne provisional-strong, 06=verb-stem-class, 67=veut); 4 leads
  (62=on, 78=me, 52=pas, 24=en). The banned readings (77=pas, 77=que, 06=ent
  general, 06=/mɑ̃/) are asserted-absent in the builder and recorded in the
  file's `not_applied` list. 06 carries the class value "verb-stem-class", not a
  phonetic value — per F25 neither side holds CONFIRMED on 06.
- Why: Pair alignment is THE silent killer here. The naive read of the
  transcription (concatenate all digits, chunk by 2) gives 3,764/2 = 1,882
  pairs — NOT the lane's 1,846. The builder replicates the lane-canonical parse
  (`code/crib_attack.py::load_pairs`): `data/upstream-ct_R5005.txt` +
  `data/upstream-offsets.json` (32 offset-1 lines, 28 odd-digit lines, one
  dropped digit each), verified byte-for-byte to reproduce exactly 1,846 pairs
  / 96 distinct groups. Any Slider or later executor MUST use this alignment or
  their positions will be shifted by up to ±1 vs mine.
- Enlightenment: The cross-check landed perfectly — my 7 ground-truth hit
  counts (11:44, 70:15, 82:38, 34:10, 29:47, 40:21, 46:29) are byte-identical
  to `data/attempt1_results.json`'s `crib_freq`. That's the independent proof
  the canonical alignment is what the lane has been using all along. Also
  worth noticing: the 4 LEAD groups alone contribute 144 positions (7.8%),
  nearly as much as all 6 provisional groups (218 positions, 11.8%) — the
  side-path's next coverage gains live in adjudicating leads, not in the
  pencil cribs.
- For the report: Side-path / skeleton section. Numbers that matter:
  sha256 of `data/upstream-ct_R5005.digits.txt` =
  18d48ccdca83fe5133b840cd427d5b89046839c866441d1c7c06fc264493e73f
  (3,764 digits, 70 lines). Coverage **566/1,846 positions = 30.66%** carrying
  ≥1 value: ground-truth 204 (11.05%), lead 144 (7.80%), provisional 150
  (8.13%), provisional-strengthened 32 (1.73%), provisional-strong 36 (1.95%).
  Per-group hits: 06:46, 11:44, 24:52, 29:47, 34:10, 40:21, 46:29, 52:27,
  62:34, 64:46, 67:37, 70:15, 78:31, 82:38, 87:32, 94:36, 96:21.
- Caveats: (1) Coverage is single-value-per-group; known polyvalence
  (06 /ɑ̃/ vs /mɑ̃/, 94 ne/en islets — F31) is NOT modeled in pass 1. (2)
  62="on" is one independent check from promotion but filed as LEAD per
  current orders — a promotion will shift 34 positions between statuses, not
  change total coverage. (3) The `pass` field is 1; the coordinator's later
  promotions should come with explicit value+status instructions and I will
  bump the counter and recompute. (4) The builder refuses to run if the
  transcription's sha256, digit count, pair count, or group count changes —
  a changed upstream file fails loud rather than silently shifting the ledger.
