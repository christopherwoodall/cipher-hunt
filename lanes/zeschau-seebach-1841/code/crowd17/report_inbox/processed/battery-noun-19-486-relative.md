# Battery verdict: noun-19-486-relative

## Bar (verbatim from queue)
"resolve iff @486 parses with 19's class named; deciding it kills or fences the relative-clause rival, sharpening the predicative account"

Restated as numbered clauses:
- C1: @486 parses with 19's class named (adjective or noun decided on the bytes).
- C2: that decision kills or fences the relative-clause rival (the listed adverse).
- C3: no standing verdict contradicted or downgraded; the predicative account is sharpened, not damaged.

## Method
Read BATTERY-PROTOCOL.md first. Created `locks/noun-19-486-relative.lock` on start
(agent id + UTC timestamp). Re-derived the repaired 1,847-pair / 96-type stream
in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`; 1,847
pairs, 96 groups verified). `canonical.py` never used. R5005, sealed gates,
red-team queue untouched. All @-offsets 1-based. 1841 diplomatic French only.

## The @486 window (byte-exact)
Row a2_11, @482-495:
`@482=13 @483=52 @484=30 @485=01 @486=19 @487=64 @488=76 @489=42 @490=41 @491=20 @492=67 @493=78 @494=42 @495=94`
i.e. `… 30 01 19 64 76 42 41 20 67 78 42 94 …`.
The "01 19" bigram occurs exactly twice stream-wide (@328, @485); "19 64"
occurs exactly once (@486-487).

## Evidence

**E1 — 76 is a standing battery-promoted noun.** `battery-noun-76.md`
promotes 76 = noun, masculine; never downgraded. `battery-frame-qui-47.md`
(kill-grade) confirms 76 verb-hood dead against that promote, and explicitly
lists "64 76" @487 as a verb-ish contact residual that does not overturn the
promote ("a noun/verb polyvalence declaration is red-team's act (§7), not
available here"). Independent legs re-verified this session: "47 76" @1273
and "87 76" @1275 ("ce 76" x2; 47="ce" A4 granted, 87="ce" promoted),
"77 76" x3 (@833, @892, @969; 77="le" provisional), "76 59" @834 ("76 est";
59="est" provisional), "93 76" @735 (93=verb promoted, verb+object),
"98 76" @13 (98=finite verb promoted, verb+object). The only verbal-looking
contact, "94 76" x2 (@653, @1578), is fenced: both are "82 94 76" with 82='m'
(banked pencil letter-tier), i.e. syllabic-94 word-internal, consistent with
the standing §7 94 particle-vs-syllable duality — not particle-'ne' + verb.

**E2 — "qui 76" cannot be a subject relative.** 64="qui" is banked GT. In
1841 diplomatic French (standard French), subject-"qui" must be followed by
its verbal predicate (clitics/negation aside); a determiner-taking nominal
subject directly after "qui" is ungrammatical (*"l'homme qui Jean voit").
@487-488 = "qui 76" with 76 a promoted noun. No rescue is battery-available:
76-as-verb is kill-grade dead (E1); 76-as-adverb/clitic is excluded by
"ce 76" x2 and verb+76 objects; parenthetical or elision rescues would invent
unmarked structure. The ungrammaticality is antecedent-independent: whatever
"01 19" is, "qui 76[noun]…" cannot open a subject relative.

**E3 — control: the encoder writes clean "qui + verb" relatives.**
"64 98" @511-512 ("94 64 98 65" = "…qui [98-finite-verb] 65") and @19-20
("17 64 98 82" = "fois qui [98-verb] …") are well-formed subject relatives
under standing values. "qui 76[noun]" @487 is the anomaly, not the norm.

**E4 — 19's class is not named anywhere in the window.** "01" has no
established class (n=28, 21 distinct predecessors, 20 distinct successors;
"01 11" @296 and "01 77" @950 put 01 before banked "la"/provisional "le", so
unitary-01 is not a determiner; a §7 split is red-team territory). "01 19"
x2 (@328 pre=10, @485 pre=30) therefore confers no class. "30 01" @484 is a
singleton (30='pas' conditional promote) — fenced, no inference drawn.

## Per-clause results
- **C1 — FAIL at kill grade.** The @486-488 window forces the claim's
  presupposition false: there is no relative clause at @486 ("qui 76[noun]"
  is ungrammatical, E1-E3), so 19 cannot be "adjective or noun as head of the
  relative clause", and no other element of the window names 19's class (E4).
- **C2 — PASS (strong form).** The relative-clause rival reading — the listed
  adverse — is KILLED, not merely fenced: shown to be a misread of the bytes.
  This is the bar's preferred outcome ("deciding it kills… the
  relative-clause rival").
- **C3 — PASS.** No standing verdict touched: 64="qui" (banked), 76=noun
  (battery promote), 47/87="ce", 98=finite verb, 93=verb all relied upon,
  none re-litigated. The protocol hold "19 (1 leg)" — the predicative
  "est 19[e]" @1778-1780 — is untouched and sharpened by elimination: @486 no
  longer offers a rival class frame for 19.

## Verdict: KILL
@486 contains no relative clause. "19 qui 76…" with 76 a battery-promoted
noun cannot parse as antecedent + subject-relative in 1841 diplomatic
French, against clean "qui + verb" controls at @19 and @511. The
relative-clause rival to the predicative account of 19 dies at kill grade;
19's class remains unnamed by @486, and the single predicative leg
("est 19[e]") stands alone, unchallenged.

## Fenced residuals (not follow-ups; kill ends this line)
- "01 19" x2 with 01 classless: 19's class is still unnamed stream-wide
  outside the one predicative leg. Naming 01 is a separate target, not this
  target's bar.
- "qui ce 76" @1269-1273 and "qui ce 68" @1715-1719 ("qui"-syntax puzzles,
  cf. frame-qui-47): out of scope here; neither establishes "qui + bare
  nominal" as grammatical, so neither rescues @486.
- Canonicality caveat: row a2_11's offset is not pencil-gloss validated
  (68/70 upstream row offsets unvalidated per protocol §7); finding is on the
  repaired stream as mandated.

## Bookkeeping
- `battery-queue.json` `noun-19-486-relative` → status `verdict`, result
  `kill`, date 2026-10-09 (temp-file + rename, own entry only; pre-write
  assert confirmed status `queued` with no verdict; JSON re-validated
  post-write).
- Lock created on start with agent id + UTC timestamp, deleted on completion.
- No standing verdict contradicted, downgraded, or re-litigated. R5005,
  sealed gates, red-team queue untouched; `canonical.py` never used.
- 1841 diplomatic French only; every number re-derived on the repaired stream.
