# Battery verdict: x29-80-collocation

- Target id: `x29-80-collocation` (priority 2)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py`).
  All @-offsets are 0-based repaired-stream indices. `canonical.py` NOT used.
  R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/x29-80-collocation.lock` (created on
  start with agent id + UTC timestamp; deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"resolve the '[X]er [80]' collocation x4 (03 x3 @1030/@1320/@1594, 92 x1 @1154);
name 80's role in this frame. Naming 80 here constrains 03's stem through the
shared '80-le' imperative link."

Numbered pass/fail clauses (restated before testing, not modified after):

1. The "[X]er [80]" collocation is enumerated byte-exactly on the repaired
   stream (all X-29-80 trigrams, with ±8 windows).
2. 80's role is NAMED (single, uniform role) across all four windows,
   with every listed adverse answered (re-parsed, fenced with stated cause,
   or shown misread — not ignored).
3. The naming constrains 03's stem via the shared "80-le" imperative link.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types confirmed).
2. Byte-exact census of all X-29-80 trigrams (n=4 found, matching the target);
   full ±8 windows re-glossed with standing values only (pencil: 11=la,
   70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted: 87=ce, 64=qui, 96=par,
   17=fois, 79=tout (A5), 00=pour (A9), 84=on (A15), 47=ce (A4), 24=faire
   (battery-promoted), 06=ent (battery-promoted); provisional: 59=est, 77=le).
3. Tested each window for every plausible role of 80 (imperative verb,
   determiner/quantifier, nominal object, adverb, pronoun) against 1841
   diplomatic French grammar; tested uniform-role hypotheses across all four.
4. Coordinated with (did not re-litigate or duplicate) standing batteries:
   imp-80-set (NULL), det-adj-80-adjudicate (NULL, HARD @1156), det-80-1156-corrob
   (NULL), stem-03-value (NULL). No standing verdict contradicted or downgraded.

## Findings — the four windows (byte-exact, re-derived)

X ∈ {03 x3 (@1030, @1320, @1594), 92 x1 (@1154)}. 29=er (pencil), so every
window is "[V]er [80]" (03 = verb stem at its three windows per imp-80-set;
92's value open, verb class only, per det-80-1156-corrob).

| @ | row | window | 80's role |
|---|---|---|---|
| 1030 | a6_03 | `87 01 03 29 80 77 11 70 82 34 29 40 17` | IMPERATIVE VERB + enclitic 'le' |
| 1154 | a6_09 | `84 02 00 92 29 80 17 77 82 44 83 21` | DETERMINER/QUANTIFIER before "fois" |
| 1320 | a7_04 | `00 36 74 62 48 98 15 24 03 29 80 08 62 98 56 30 06` | determiner-leaning (class level) |
| 1594 | a8_02 | `65 48 29 47 08 81 03 29 80 67 77 81 82 98 00` | NOMINAL OBJECT |

Window notes:

- **@1030–1033** = "ce [01] [03]er [80]-le la première [fois]".
  The nominal alternative ("[03]er [80] le, la première") is ungrammatical:
  "le la première" is an impossible article+article sequence, so "80 77"
  cannot be noun + article. Standing imp-80-set enclitic diagnostic holds:
  "80-77" = imperative full-form + enclitic 'le' (n=2: @720/@1032; the only
  grammatical verb+enclitic order among 80's followers). **80 = imperative verb.**
- **@1154–1157** = "pour [92]er [80] fois [le]".
  Standing HARD determiner per det-adj-80-adjudicate: the pre-"fois" slot is
  determiner-only; escapes (a) 92-29-80 one-word, (b) 80-17 one-word,
  (c) clause boundary after 29, (d) adverb — all dead byte-exactly
  (corroborated by det-80-1156-corrob C2). **80 = determiner/quantifier.**
- **@1320–1323** = "[15] faire [03]er [80] [08] [62]...".
  Readings: determiner+noun ("faire [V]er [det] [N]" — causative + quantified
  object phrase, e.g. "faire bâtir deux maisons"; grammatical, NO boundary
  assumption); imperative (needs an ungranted clause boundary after 80, then
  "[08]..." opens a new clause — possible, not battery-grade); two nouns
  ("[80] [08]" with no preposition) ungrammatical. 08's value is open
  lane-wide (n=18, no standing class), so this is class-level only:
  **80 determiner-leaning; imperative fenced.**
- **@1594–1597** = "ce [08] [81] [03]er [80] et le [81] m [98] pour".
  67="et" by the positional rule (follower 77='le' provisional is not
  infinitive-shaped). Imperative reading fails twice: it needs an ungranted
  boundary after 80 AND "et le [81]" (et + article-headed NP) is an
  ungrammatical imperative continuation (a conjoined imperative continuation
  needs a verb, not "et + le + N"). Determiner reading fails: the follower
  is "et", not a noun — no determiner+noun pair. Nominal reading fits:
  "[V]er [N] et le [N]" — parallel conjoined object NPs
  ("[03]er [80] et le [81]"). **80 = nominal object** (modulo 81's open class).

## Clause 1: PASS — collocation enumerated byte-exactly (4/4 as briefed)

## Clause 2: FAIL — no uniform role; the frame is role-split

Uniform-role hypotheses, all tested and rejected on the bytes:

- Uniform imperative: dies at @1156 (HARD — verb/adverb in the pre-"fois"
  slot ungrammatical; escapes dead).
- Uniform determiner: dies at @1032 ("[det] le" ungrammatical;
  imperative+enclitic is the standing parse).
- Uniform nominal: dies at @1156 (HARD) and at @1032 ("le la" ungrammatical).
- Adverb / pronoun (en/y): adverb dead at @1156 per standing escape (d);
  pronoun dead at @1032 ("en le"/"y le" impossible).

The SAME surface collocation "[X]er [80]" forces at least two mutually
exclusive roles at battery grade: imperative verb (@1032, enclitic
diagnostic) vs determiner/quantifier (@1156, HARD). A third role
(nominal object, @1596) and a determiner-leaning fourth (@1322) complete
the split. 80's role in "this frame" cannot be named once — the bar's
presupposition fails on the windows.

## Clause 3: FAIL — 03's stem unconstrained

As stem-03-value already found (its clause 1, FAIL): the open neighbors
(01/80/08/81/15) admit dozens of grammatical -er stems; nothing forces one.
This battery adds that the "shared '80-le' imperative link" covers only the
@1030 window — @1320/@1594 do not share it, and 80's within-frame split
dissolves the link as a naming constraint.

## Adverses: HONORED (gathered, not declared)

80's roles remain morphologically incompatible with ONE French lexeme at
group granularity (imperative full-form "80-le" x2, finite 3pl "80-ent" x2,
post-'vient'/'faire' infinitive slot x5 — per imp-80-set's inventory). This
report ADDS new §7 material: the incompatibility now lives INSIDE a single
4-window collocation ("[X]er [80]"), not just across disparate frames —
the @1032 imperative-verb vs @1156 determiner/quantifier pair is
byte-grounded on both sides and survives every re-segmentation in the
standing escapes. No polyvalence declared at battery level (§7; 67 et/veut
stays the sole true polyvalence). Escrowed for the queued P1
`poly-80-docket`; the docket's evidence set grows by this report.

## Verdict: NULL — escalate to poly-80-docket

The bar's uniformity presupposition is falsified within the frame (two
standing-grade, mutually exclusive roles), but ruling the contradiction
would implicate the §7 67-sole-polyvalence law, which batteries do not rule
on — per lane precedent (det-adj-80-adjudicate), the battery marks NULL
with the contradiction as the headline and escalates. The new content for
the red team: the poly-80 question is no longer cross-frame only; the SAME
"[X]er [80]" surface splits imperative-verb (@1032) vs determiner (@1156)
vs nominal (@1596), with @1322 determiner-leaning. No standing verdict
contradicted or downgraded. R5005, sealed gates, red-team queue untouched.

## Follow-ups proposed (for supervisor queuing)

1. `poly-80-x29-frame` (P2) — re-segmentation audit of the @1032/@1156 pair
   inside the "[X]er [80]" frame: test every byte-grounded re-segmentation
   ("80|77" vs word-internal, "29 80 17" boundary variants) for one that
   dissolves the imperative-vs-determiner split; if none survives, the frame
   alone forces the polyvalence question. Docket feeder for `poly-80-docket`.
2. `x29-80-1596-nominal` (P2) — close @1596's 80 as nominal object: census
   81's windows (n=?; "ce [08] [81]" @1592, "et le [81]" @1596-1598) for
   noun-compatibility of "[03]er [80] et le [81]". Discriminates nominal-80
   from any surviving imperative/verb reading at @1596.
3. `x29-80-1322-det` (P3) — test @1322's 80 as determiner of 08: census 08's
   post-"ce" windows (@1488 "87 08 31", @1592 "47 08 81") for nominal
   compatibility; if 08 is nominal, @1322 becomes a second determiner leg
   beside @1156, narrowing 80's determiner paradigm.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-x29-80-collocation.md (this file).
- battery-queue.json: `x29-80-collocation` queued → verdict/null (temp-file +
  rename, own entry only, pre-write assert confirmed no prior verdict;
  JSON re-validated after write).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- No standing verdict contradicted or downgraded. No second polyvalence
  declared. R5005, sealed gates, red-team queue untouched. canonical.py
  never used; every number re-derived on the repaired 1,847-pair stream.
