# Battery verdict: det-86-dlife-partition — partition of 86's 26 D-windows + per-subset value hypotheses

Date: 2026-10-09. Worker: subagent 94b15c37-1af3-bdb2-709a-5f1d5e7923ca (battery worker).
Lock: code/crowd17/next-token/locks/det-86-dlife-partition.lock (created
2026-10-09T08:25:00Z; no prior lock existed — the earlier dispatch's worker
never started; deleted on completion).
Target id: det-86-dlife-partition. Queue status at take: queued, priority 2.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
n=1847 asserted). canonical.py never used. R5005, sealed gate instances,
red-team adjudication queue untouched. No data invented; every number
re-derived below. @-offsets are 0-based stream indices.

## Bar (pre-registered verbatim from battery-queue.json, BEFORE testing)

"a subset-value promotes iff it parses all its windows with zero hard
contradictions; kill any subset-value a pencil/granted window forces false.
Does not declare any split (red-team act)."

### Numbered clauses (operative, pre-registered)

1. A subset-value PROMOTES iff it parses all its subset windows with zero
   hard contradictions.
2. KILL any subset-value that a pencil/granted window forces false.
3. This battery does NOT declare any split — split declaration is a
   red-team act. Subset-values are tested independently; sharing a value
   across subsets is recorded, never declared.

Adverses (pre-registered): none listed.

## Method

1. Re-parsed the repaired stream per repair_parse.py; extracted all 32
   windows of 86 independently (n=32 confirmed; D-life = follower not in
   {29,59,06}, n=26 — matches battery-split-86-amended-rule 26/26).
2. Re-derived the four-way partition on bytes alone: le-life (L1 in
   {00,96,67} AND R1 in {50,01,52,56,66}), det-left (L1 in {87,11,47}),
   77-adjacent (L1 = 77), residual (rest). Verified exceptionless: zero
   non-le D-windows match the le frame; all 9 le windows match it.
3. Values usable at kill grade: pencil (11=la, 70=pre, 82=m, 34=i, 29=er,
   40=e, 46=que) + red-team granted (87=ce, 64=qui, 96=par, 17=fois,
   79=tout, 00=pour, 84=on, 47=ce). Provisional 77=le and battery-promoted
   values (94=ne, 30=pas, 12=n, 48=e, 24=finite-verb class, 06=ent,
   39=a) cited as caveated, never as kill-grade forcing.
4. Each subset got a named value hypothesis; every window tested under it
   on standing values. Coordinated with (not duplicating):
   battery-det-86-dlife-value (uniform-value KILL adopted), battery-voir-86-sweep
   (V/D frame adopted), battery-le-86-determiner-subset (9-window fence
   adopted), battery-split-86-amended-rule (26/6 partition adopted),
   battery-reseg-86-problem-windows (word-internal rival KILL adopted).

## The partition (re-derived, byte-level)

- **le-life, n=9:** @661 (16 00 [86] 50), @948 (98 96 [86] 01),
  @962 (96 00 [86] 56), @1002 (33 00 [86] 56), @1099 (29 67 [86] 52),
  @1128 (43 00 [86] 52), @1458 (21 67 [86] 66), @1506 (33 00 [86] 56),
  @1792 (03 00 [86] 56). Left-frame split exceptionless on bytes.
- **det-left, n=3:** @175 (09 87 [86] 21), @671 (67 11 [86] 24),
  @1345 (38 47 [86] 66). Left = ce/la/ce (87 granted, 11 pencil, 47 granted).
- **77-adjacent, n=4:** @799 (44 77 [86] 44), @878 (16 77 [86] 78),
  @951 (01 77 [86] 96), @1134 (24 77 [86] 20).
- **residual, n=10:** @300 (40 97 [86] 91), @557 (34 17 [86] 94),
  @716 (63 00 66 [86] 01), @728 (64 11 00 [86] 48), @867 (47 46 00 [86] 70),
  @899 (14 98 83 [86] 16), @1131 (86 52 37 [86] 24), @1147 (42 98 98 [86] 67),
  @1335 (52 39 83 [86] 71), @1739 (12 48 52 [86] 12).

## Subset 1 — le-life 9: hypothesis 86='le'

Window-level (L2 L1 [86] R1 R2 R3; standing values only):

- @661: "pour(00) le [50]" — 50 nominal-strong ("la 50" x2). PASS.
- @948: "par(96) le [01]" — 01 nominal-strong ("ce 01" x2). PASS.
- @962: core "pour le [56]" parses (56 nominal-weak-positive @131), BUT the
  full window reads "et par pour le [56]": "96 00" = "par pour" is
  ungrammatical under GRANTED 96=par / 00=pour, under EVERY 86 value. The
  defect is orthogonal to 86 (discriminates nothing about its value).
  FAIL as full-window parse; owned by queued par-pour-962-adjudicate.
- @1002: "pour le [56] ce(47) [91]". PASS.
- @1099: "er(29) et(67 positional: 52 not infinitive-shaped) le [52]" —
  52 nominal-strong ("la 52" x3). PASS.
- @1128: "pour le [52]". PASS.
- @1458: "et(67) le [66] tout(79) fois(17)" — 66 nominal ("pour 66" x7). PASS.
- @1506: "pour le [56]". PASS.
- @1792: "pour le [56]". PASS.

Grade: 8/9 windows parse fully; the 9th fails on a granted-neighbor defect
independent of 86. Clause 1 (promote) FAILS strictly — not all windows
parse. Clause 2 (kill) FAILS — no pencil/granted window forces 86≠'le'
(the @962 defect does not discriminate values). **Subset-value verdict:
NULL.** The 'le'-life lead survives; its promote is gated on
par-pour-962-adjudicate (already queued by the le-subset battery — no
duplicate).

## Subset 2 — det-left 3: hypothesis 86 = NOUN (class-level)

- @175: "[09] ce(87=ce granted) [86-N] [21]..." — "ce [N]" is a clean
  determiner-noun frame. R1=21 is noun-class at battery level only
  (caveated); "ce [N] [21]" adjacency is tension under that caveat, not a
  standing-value contradiction. PASS.
- @671: "[67=et positional] la(11=la pencil) [86-N] [24]..." — "la [N]"
  clean; 24 is unvalued at grant grade (finite-verb class is
  battery-promoted/caveated — under it the window reads as a full clause
  "la [N] [V]"). Zero hard contradictions on standing values. PASS.
- @1345: "[38] ce(47=ce granted) [86-N] [66]..." — "ce [N]" clean; 66
  unvalued at grant grade. PASS.

No pencil/granted window forces the noun reading false. The reseg battery
killed only the word-internal (syllable) rival at @175/@671 — the
standalone-noun reading is consistent with that kill. Clause 1 met on
standing values; clause 2 not triggered. **Subset-value verdict: PROMOTE
(battery level, subset-scoped, class-level — the noun value itself is
unnamed).** Caveats: 21's noun class and 24's verb class are battery-level,
pending ratification; they were not needed for the promote.

## Subset 3 — 77-adjacent 4: two hypotheses tested

### 3a. 86 = object clitic (le/la/les)

- @951: "[01] 77 [86] 96=par(GRANTED) 87=ce 46=que" — an object clitic must
  be followed by its finite verb; "le par" is ungrammatical in French, and
  96=par is granted. **Kill grade: a granted window forces the clitic
  value false. Subset-value verdict: KILL.**
- (@799/@878/@1134 do not rescue it; one kill-grade window suffices.)

### 3b. 86 = NOUN (class-level)

- @799: "44 77 [86] 44 74 62" — "[77] [N] [44]"; no standing-value force.
  Under provisional 77='le': "le [N]" clean. PASS.
- @878: "16 77 [86] 78 17 08" — "le [N] [78]..." (78 unvalued at grant).
  PASS.
- @951: "01 77 [86] 96=par 87=ce 46=que" — "le [N] par ce que" parses
  cleanly — the same window that kills the clitic reading supports the
  noun reading. PASS.
- @1134: "24 77 [86] 20 62 98" — "[77] [N] [20]"; under caveated 24-class:
  "[V] le [N] [20]" parses as verb + object NP. PASS.

Zero hard contradictions on standing values. **Subset-value verdict:
PROMOTE (battery level, subset-scoped, class-level, value unnamed).**
Recorded, not declared: det-left and 77-adjacent both promote 86=noun —
whether they are one value is a red-team adjudication, not a battery
declaration (clause 3).

## Subset 4 — residual 10: hypotheses 86='le' and 86=noun

### 4a. 86='le'

- @300: "[97] le [91]" — 97/91 unvalued; no contradiction. PASS-open.
- @557: "i(34) fois(17) le [94]..." — "fois le" needs a clause boundary;
  the absolute construction ("une fois le [N]...") keeps it grammatical;
  94/59/30 open-or-caveated at grant grade. Fenced tension, not kill.
- @716: "pour(00) [66] le [01]" — asyndetic double NP, odd but not a hard
  contradiction on standing values (66 unvalued). Fenced tension.
- @728: "la(11 pencil) pour(00 granted) le [48]" — "la pour" is
  ungrammatical under pencil+granted values under EVERY 86 value: orthogonal
  granted-defect, discriminates nothing about 86. Fenced (defect family of
  @962's "par pour").
- @867: "que(46 granted) pour(00 granted) le pre(70)" — "que pour"
  ungrammatical under granted values under every 86 value: orthogonal
  granted-defect. Fenced.
- @899: "[83] le [16]" — open neighbors. PASS-open.
- @1131: "[37] le [24]..." — "[DET] [finite verb]" ungrammatical for a
  determiner reading, BUT 24's verb class is battery-promoted (caveated),
  not granted — not kill-grade on standing values. Fenced with caveat.
- @1147: "[98] le [67]..." — 67 positional-open (33's shape unresolved);
  no standing-value force. Fenced tension.
- @1335: "[83] le [71] qui(64)" — open neighbors. PASS-open.
- @1739: "[52] le [12] i(34)" — "le [12]" NP; no contradiction. PASS-open.

No pencil/granted window forces 86≠'le'; but @728/@867 do not parse at all
under granted values (orthogonally). **Subset-value verdict: NULL.**

### 4b. 86=noun

- @300: "[97] [N] [91]" — open; PASS.
- @557: "fois [N]" — bare noun after "fois" strained (proper-noun rescue
  unevidenced); fenced tension, not kill-grade on standing values.
- @716: "pour [66] [N] [01]" — double-NP strain; fenced tension.
- @728, @867: orthogonal granted-defects (as 4a). Fenced.
- @899, @1131, @1147, @1335, @1739: open neighbors; PASS each.

**Subset-value verdict: NULL.** Neither value is forced false; neither
parses all 10 cleanly. The residual is heterogeneous on current bytes and
needs a finer partition or per-window adjudication.

## Per-clause pass/fail (target level)

1. Subset-value promotes: noun promoted on det-left 3 and on 77-adjacent 4
   (zero hard contradictions on standing values each). 'le' not promoted on
   le-life 9 (8/9; @962 orthogonal defect) nor on residual 10; noun not
   promoted on residual 10. Clause applied consistently.
2. Subset-value kills: object-clitic killed on 77-adjacent 4 by @951
   (96=par granted → "le par" ungrammatical). No other kill-grade force.
3. No split declared: honored throughout. The noun promotes on two subsets
   are recorded as separate subset-scoped results; merging them is the
   red team's act.

## Adverses

- None listed pre-registration. §5.2 check: no standing red-team verdict
  names 86's D-life value; the amended-rule promote is positional and
  value-free — uncontradicted. The det-86-dlife-value kill covered the
  uniform determiner value only, not subset noun values. The 67
  sole-polyvalence law is untouched (no polyvalence declared at battery
  level). No standing verdict downgraded or overwritten.

## Verdict: PROMOTE (battery level, partition claim)

The commissioned product is delivered: the 26 D-windows partition
exceptionless into the four stated sub-lives on bytes, and every subset
carries a named, window-tested value hypothesis with a per-window evidence
trail — noun promotes (class-level) on det-left and 77-adjacent,
object-clitic killed on 77-adjacent, 'le' lead survives-but-ungated on
le-life, residual stays heterogeneous. No split declared; red-team owns
assembly.

## Follow-up targets (subset-nulls regenerate work)

1. `noun-86-dlife-name` (P3): name the noun value behind the 7 noun-parse
   windows (det-left 3 + 77-adjacent 4). Contact-profile the "ce [N]"
   (@175/@1345), "la [N] [V]" (@671), "le [N]" (@799/@878/@951/@1134)
   frames against lane noun batteries (81 = masculine abstract noun).
   Bar: promote a named noun value iff it parses all 7 windows with zero
   hard contradictions on standing values; kill iff a pencil/granted
   window forces it false.
2. `residual-86-finer` (P3): finer partition of the residual 10. Test the
   00-left pair (@728/@867) as the defective-left frame family of
   par-pour-962-adjudicate; test @1131/@1147 for clitic-vs-noun
   adjudication once 24's class / 67's positional value ratify; test
   @557/@716 for the noun reading's proper-noun/apposition rescue.
   Bar: a sub-subset value promotes iff it parses all its windows with
   zero hard contradictions; kill any a pencil/granted window forces false.
3. Coordinate note (not a new target): le-life 'le' promote stays gated on
   queued par-pour-962-adjudicate (+ conditional le-86-subset-rerun); the
   noun-on-two-subsets merge question is flagged for the red-team
   86-split docket, not re-proposed as a battery target.

## Constraints compliance

- Tested only on the repaired 1,847-pair stream; canonical.py never
  touched; R5005, sealed gates, red-team queue untouched.
- No standing verdict downgraded or overwritten; no red-team verdict
  contradicted (§5.2 headline: none).
- 86 polyvalence NOT declared; no new polyvalence implied at battery level.
- Sibling reports coordinated, not duplicated (see Method 4).
