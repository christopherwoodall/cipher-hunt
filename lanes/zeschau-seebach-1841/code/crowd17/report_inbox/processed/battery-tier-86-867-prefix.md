# Battery verdict: tier-86-867-prefix

- Target: `tier-86-867-prefix` (battery-queue.json, priority 3, status queued)
- Claim: "Name 86's tier at @867: prefix of a -prendre compound (comprendre/apprendre/surprendre/reprendre/entreprendre — test which prefix parses 'pour [prefix]pre ce le [89]') vs stem tier. If prefix-tier is confirmed against the stem-tier at the four '86 29' windows, package the tier-split for red-team section-7 adjudication."
- Adverses: "package as red-team input if split - no battery-level split declaration"

## Bar (verbatim, pre-registered)

"name the tier at battery grade; package tier-split as red-team input iff prefix-tier is confirmed against stem-tier"

Numbered clauses:
- C1: Name 86's tier at @867 at battery grade. 
- C2: Iff prefix-tier is confirmed against stem-tier, deliver the tier-split as red-team input (gather-only; no §7 declaration at battery level).
- C3 (adverse): No battery-level split declaration.

## Method

Repaired 1,847-pair / 96-type stream re-derived in-session via
`code/side-keyhunt/repair_parse.py` + `code/side-keyhunt/repaired_offsets.json`;
asserts held (1,847 pairs, 96 types). `canonical.py` never used.

Standing values adopted, not re-litigated: 70='pre' pencil GT; 87='ce' granted
(A4); 00='pour' granted (A9, leg-1 class-level); 29='er' pencil GT; 77='le'
provisional; 86=['INF','cls'] registry. Adopted: `stem-86-29-value` NULL
(2026-10-09) — "pour S+pre ce le [89]" ungrammatical for every -er stem S;
tier tension is §7 red-team venue. Adopted: `celle-7780-fusion-515-869` KILL —
'87 77'='celle' fusion killed at kill grade at @869 (this exact locus).
Adopted: `ce-le-verb-frame` NULL — "ce le" two-word reading fenced as a
77-value residual at @869.

## Window-level evidence

@867 byte-confirmed (row a5_07):
`@865=46('que') @866=00('pour') @867=86 @868=70('pre') @869=87('ce')
@870=77('le') @871=89 @872=48('e')` — "que pour [86]pre ce le [89] e".

- "86 70" is a stream hapax (1/1,847). n(86)=32.
- The four "86 29" windows (@431, @1375, @1391, @1825): "[86]er" — 86 as verb
  stem + 29='er'. Stem-tier at battery grade (adopted premise).
- 29='er' occurs 0× after 86 outside those four windows (follower census
  re-derived in-session: 29×4, 56×4, 18 singletons incl. 70×1).

## C1: 86's tier at @867

**Stem-tier FAILS at @867:**
(a) No -er stem S makes "pour S+pre" grammatical — S+"pre" is not a French
word (adopted from `stem-86-29-value` NULL, which tested this exact frame).
(b) 86 has no completion neighbor at @867: under the lane's stem+completion
model (A10: 33+29; 03+29 conditioned; 06='ent' pure completion), a stem needs
a completion neighbor to surface as a complete word; 29='er' is 0× after 86
here (follower is 70='pre').
(c) 70='pre' is a pencil-GT syllable, not a standalone French word, so
"pour [86-word] pre" fails; 86-as-complete-infinitive leaves "pre" dangling.

**The "86 70" contact must be word-internal** (both elements sub-lexical:
86 unvalued cell, 70='pre' syllable). French word-internal "Xpre":
the sole licensed word-family is the -prendre compounds — comprendre,
apprendre, surprendre, reprendre, entreprendre (méprendre needs a reflexive
and is ungrammatical on the left edge; "re-pré-" as in représenter is the
same prefix-tier shape). In every -prendre compound, X occupies the PREFIX
slot and "pre" belongs to "prendre". Alternatives ruled out: pré- compounds
place "pre" as the prefix itself, leaving 86 pre-prefixal with no licensed
account; "âpre"/"empre" shapes fail on class (86 is INF, not adjective) and
grammar.

**Per-prefix test** ("which prefix parses 'pour [prefix]pre ce le [89]'"):
comprendre / apprendre / surprendre / reprendre / entreprendre — left edge
"pour + infinitive" grammatical for all five, but NO prefix is selected:
all five fail identically on (i) the missing "-ndre" completion (@869=87='ce'
is a granted whole word and cannot be "-ndre"), and (ii) the fenced right
edge "ce le [89]" ('celle' KILLed at @869; "ce le" fenced NULL). The prefix
VALUE is unnameable at battery grade (no selector; lane precedent:
`masc-noun-86-name`, `stem-86-29-value`).

**Positive structural assignment:** 86 operates sub-lexically in prefix
position at @867. The tier is determined by the structural slot, not by the
complete word — the word-level blockers (missing "-ndre", fenced "ce le")
make the WINDOW a residual, but they do not move 86 out of the prefix slot,
just as 03's verb-stem tier is named from the "[03]+29" slot.

→ C1 PASS: 86 is **prefix-tier** at @867 at battery grade. Value open.

## C2: tier-split package (red-team input, gather-only)

- Stem-tier: battery-grade at the four "86 29" windows ("[86]er" = stem + 'er').
- Prefix-tier: battery grade at @867 ("[86]pre" = prefix + "pre" of -prendre).
- Conditioned shape: 86's tier is conditioned on follower (29='er' → stem;
  70='pre' → prefix).
- This is a **§7 tier-split candidacy**. NO SPLIT DECLARED at battery level
  (C3/adverse honored).
- Package for red-team adjudication: this report + `stem-86-29-value` NULL +
  the @867 byte evidence + the -prendre prefix candidate set (value
  unnameable) + the word-level blockers ("-ndre" absent; "ce le" fenced).

→ C2 FIRES: package delivered; no declaration.

## Verdict: PROMOTE

Promotes the tier finding (86 is prefix-tier at @867 at battery grade) and
delivers the conditioned tier-split package for red-team §7 adjudication.
No value named. No split declared.

## Scope

Names 86's tier at @867 only. Untouched: 86's INF class, the four "86 29"
stem-tier windows, `ce86-le86-parity` merge, `noun-86-dlife` KILL,
`split-86-amended-rule` (§7 venue), 77='le' provisional, 89's value,
98='vient' LEAD, 67 sole polyvalence. No standing/red-team verdict
contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream
caveat stands (row a5_07 offset unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-tier-86-867-prefix.md`
- Queue: `tier-86-867-prefix` → `status: verdict`, `result: promote`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique tmp
  `battery-queue.json.tier-86-867-prefix.tmp` + atomic rename; JSON re-validated
  from disk; own entry only; no downgrade)
- Lock `locks/tier-86-867-prefix.lock`: created on start
  (3c9919a5-8376-4374-bb5c-5b27bd692b24, 2026-10-09T19:50:00Z, no stale lock),
  deleted on completion (verified gone). R5005, sealed gates, red-team
  adjudication queue untouched.
