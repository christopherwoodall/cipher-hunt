# Battery report: verb-60-ent (name the ent-60 verb across V5–V6)

Worker: subagent session 79f85a3f-78e5-4828-90f8-9faf7a7be143.
Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py.
canonical.py never used. R5005 never touched. @i = 0-based pair index.
Lock: locks/verb-60-ent.lock created at start, no prior lock (no stale lock to note).
No red-team verdict on 60 exists — no contradiction, no escalation.

## Bar (verbatim, pre-registered before testing)

"name one ent-prefixed verb (ent[60]...) parsing both windows with stated boundaries; 60='on' ('entonne') excluded (84='on' granted; fails V2)"

Numbered clauses (fixed before data examination):

1. (C1) One ent-prefixed verb (ent[60]...) is NAMED such that it parses V5
   (@1563 '06 60 71') with stated syllable boundaries, using only
   banked/granted/promoted values.
2. (C2) The SAME verb parses V6 (@1735 '06 60 12 48') with stated syllable
   boundaries, including a decided boundary for the 'ent[60]ne' span
   (one word vs 'ne' word).
3. (C3) 60='on' ("entonne") is not the named verb (excluded: 84='on'
   granted A15; fails V2).
4. (C4) Adverses answered: 71 fenced or resolved (71 open); the V6 boundary
   decided with stated cause; the @232 '60 71' twin coordinated with queued
   frame-vient-parvenir, not duplicated.

## Method

Fresh parse per protocol. No prior counts trusted. Standing values used:
banked 11=la, 29=er, 40=e, 70=pre, 82=m, 34=i, 46=que; granted 64=qui,
96=par, 87=ce, 47=ce (A4), 84=on (A15); promoted 94=ne, 12=n (letter),
48=e (letter), 06=ent, 30=pas; provisional 59=est, 77=le. 1841 diplomatic
French for all grammaticality judgments. The 'entonne' candidate was not
re-tested (excluded by bar).

## Window-level evidence (re-derived on the repaired stream)

V5 — @1563 (row a8_01):
@1559 11 @1560 26 @1561 30 @1562 06 @1563 60 @1564 71 @1565 50 @1566 29 @1567 24
Reads: "...e[40] fois[17] la[11] [26] pas[30] ent[06] [60] [71] [50] er[29] [24]..."
- 26=noun forced by banked 11=la (noun26-1560-pas: "la [26]" exactly 2x
  stream-wide; clause boundary between @1560 and @1561 forced). So V5 opens
  mid-clause: "...la [26-noun]. pas[30] ent[06] [60] [71]..."
- 06 forward-attaches (pas-30's own @1561 parse: "la 26 pas 06 60"): "ent[60]"
  is word-initial, 60 the second syllable of an ent-prefixed verb.
- The "ne" for "pas"(@1561): only upstream 94 in @1500–1561 is @1549,
  consumed in "prenne" (70-12-94). Downstream 94 @1576 (d=15) is not a
  "ne...pas" partner. So V5's "pas" lacks "ne" — see finding F3 below.

V6 — @1735 (row a8_07):
@1732 56 @1733 30 @1734 06 @1735 60 @1736 12 @1737 48 @1738 52 @1739 86 @1740 12 @1741 34 @1742 94 @1743 82 @1744 46
Reads: "...[56] pas[30] ent[06] [60] n[12] e[48] [52] [86] n[12] i[34] ne[94] m[82] que[46]..."
- Same "pas 06 60" geometry as V5 (the '30 06 60' trigram is x2 stream-wide,
  @1561/@1733 — V5 and V6 only).
- @1740-1741 = 12-34 = "ni" (n+i, banked letters). @1742=94='ne' promoted.
- The "ne" for "pas"(@1733): upstream 94s @1687/@1701/@1705/@1713 are all
  consumed (@1701 pairs with its own 30; @1713 with @1716's frame).
  Downstream 94 @1742 (d=9). V6's "pas" also lacks "ne" — see F3.

71 census (n=7): prev {60 x2 (@232, @1563), 63, 48, 65, 86, 83};
next {51, 10, 12, 17, 64, 50 (@1565), 48}. No value; fenced as open.

## Key findings

F1. **V6 one-word "ent[60]ne" is lexically dead.** Exhaustive check of French
vocabulary for verbs matching "ent-?-ne": the ONLY such verb is
"entonner" (entonne/entonnent/entonn\u00e9...), which the bar excludes
(60='on' collides with granted 84='on' A15; fails V2). No other French verb
has the shape "ent"+syllable+"ne". The parent battery's stated preference
for the one-word parse ("'ne'-after-verb ungrammatical") is therefore
moot: one-word is not ungrammatical, it is non-existent. The two-word
boundary "ent[60] | ne[12-48]" is FORCED, and "ne" must be grammatical in
its own right — see F2.

F2. **"ne [52]" is a repeated frame x4.** @571 ("94 52": "...[45] ne[94]
[52] ce[87]..."), @1294/@1807 (byte-identical "59 35 94 52 80 04":
"...ne[94] [52] [80]..."), @1738 ("48 52": "...n[12] e[48] [52]...").
52's census (n=27): prev {94 x3, 11 x3, 93 x2, 48 x2, 06 x2, 86 x2, 64 x2};
next {82 x5, 37 x4, 89 x2, 38 x2, 30 x2, 80 x2}. Class open. If 52 proves
verbal, V6's "ne" is accounted (ne litt\u00e9raire, or "ne...que" with
@1744=46='que'); until then it is fenced, not kill-grade (the verb
"ent[60]" itself is complete before "ne").

F3. **"ne"-drop is stream-normative.** 8 of 19 "pas"(30) tokens have no 94
within \u00b115 (@30, @45, @742, @993, @1222, @1251, @1269, @1309). V5/V6's
"pas ent[60]" without "ne" is therefore not anomalous on this stream.
Register caveat stands for 1841 diplomatic French ("ne"-drop is informal),
but at battery grade the missing "ne" does not fail either window.

F4. **The candidate set does not reduce to one.** At least ten ent-prefixed
2-pair verbs parse both windows structurally: entendre (60='endre'),
entrer (60='trer'), entamer (60='amer'), enterrer/entourer/entacher
(60='errer'/'ourer'/'acher'), entra\u00eener (60='ra\u00eener'),
entretenir (60='retenir'), entrevoir (60='revoir'), entreprendre
(60='reprendre'), ent\u00e9riner... "entrer [71]" is mildly strained
(intransitive; needs 71='dans'), but 71 is open (n=7) and could be 'dans'.
No byte-level discriminator exists in either window: V5's "[71] [50]er"
and V6's "ne [52]" are class-open on every content pair.

## Per-clause pass/fail

- C1: FAIL at battery grade. No ONE verb is nameable: \u226510 ent-prefixed
  verbs parse V5 ("pas ent[60] [71]") with equal support (F4); 71 open, no
  transitivity discriminator. "entendre" is the frequency/register leader
  but naming it is arbitrary.
- C2: FAIL (consequence of C1). The same tie covers V6; additionally V6's
  "ne" depends on 52's open class (F2), fenced.
- C3: PASS. "entonne" not proposed; exclusion grounds confirmed
  (84='on' A15 granted; parent battery's V2 failure cited, not re-run).
- C4: PARTIAL. V6 boundary DECIDED (F1: one-word lexically dead \u2192
  two-word forced); 71 FENCED with stated cause (n=7 census above; no
  value); @232 '60 71' twin CITED to queued frame-vient-parvenir
  ("21 60 71 51 70 98" @227-233), not duplicated.

## Verdict

**NULL** — no single ent-prefixed verb is nameable at battery grade (C1/C2
fail: \u226510 candidates tie with no in-window discriminator). Not kill:
no window forces the claim false (F1/F2/F3 keep both windows parseable;
"entonne" stays excluded per C3). No standing verdict contradicted or
downgraded; R5005, sealed gates, and the red-team queue untouched. The
genuine advances are F1 (V6 boundary forced two-word — reverses the parent
battery's preference) and F2 (the "ne [52]" x4 frame).

## Follow-ups (work regenerates; none duplicates queued targets)

1. **dis-ent-60-verb** (priority 2): discriminate the ent-60 verb candidates
   (entendre/entrer/entamer/entretenir/...). Bar: "name 60's syllable value
   via 71's value (71='dans' \u2192 'entrer'; 71 a direct-object noun \u2192
   transitive shortlist) or via a new '06 60' window; else fence the
   candidate set with the tie recorded." Evidence: this battery (F4;
   71 n=7 census). Adverses: 71 open; @232 '60 71' twin owned by queued
   frame-vient-parvenir (coordinate, do not duplicate); 'entonne' excluded.
2. **ne-52-frame** (priority 2): resolve the "ne [52]" x4 frame (@571,
   @1294, @1807, @1738). Bar: "name 52's class with \u22652 frame-legs; if
   verbal, V6's 'ne' is accounted (ne litt\u00e9raire or ne...que with
   @1744=46='que'); if nominal, fence V6's 'ne' as residual." Evidence:
   this battery (F2; 52 n=27 census). Adverses: 52->82 x5 ('m'); 52<-94 x3.
3. **profile-71** (priority 3): full profile of 71 (n=7). Bar: "name 71's
   class/value with \u22652 frame-legs; transitivity verdict for the
   ent-60 verb (71='dans' vs direct-object noun)." Evidence: this battery
   (71 prev/next census). Adverses: n=7 thin; @232 token formula-bound
   (frame-vient-parvenir owns it).
