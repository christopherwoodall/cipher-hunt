# Battery `det-87-644-function` — verdict: PROMOTE (function-level)

## Bar (verbatim, pre-registered before testing)

"name 87's function at @644 with zero ungranted assumptions; fence if undecidable"

Restated as numbered clauses:
- **C1:** name 87's function (determiner vs pronominal) at @644 using only
  standing granted/banked/adopted premises — zero new assumptions.
- **C2:** if C1 cannot be met, fence with stated cause.

## Method

Per BATTERY-PROTOCOL.md: protocol read first, lock created on start,
bar pre-registered above before any testing, stream re-derived in-session
from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed per `repair_parse.py`; 1,847 pairs asserted; `canonical.py` never used).
R5005, sealed gates, red-team queue untouched.

## Locus (byte-exact)

0-based @641–648, row a4_02:

```
641:48 642:20 643:24 | 644:87 645:61 646:88 647:77 648:78
```

"…[48] [20] [24] ce [61] [88] le [78]…"

Distributional anchors: "87 61" is 1x stream-wide (no repetition leverage);
"24 87" is 10x (positions 73, 162, 179, 190, 643, 823, 829, 1486, 1766, 1774).

Standing premises used (all granted, none new):
- 87 = "ce" (battery-promoted).
- 24 = finite/modal-shaped verb class (R17-009, standing; reaffirmed in the
  24 correction; value open). 24 = "en" is kill-grade dead (en24-311).

## The pronominal arm is dead at grammar level (C1, elimination leg 1)

"ce" as a pronoun has exactly three licensed frames in French, and a fourth
candidate that fails:

1. **Postverbal direct object** ("[24-fin] ce"): bare "ce" is never a COD
   pronoun — the COD series is me/te/le/la/nous/vous/les/se ("*il veut ce"
   is ungrammatical in every period). Corpus check on the lane's 1841 side-
   period corpus (31,664,431 chars): **0 instances** of finite-verb + bare
   "ce" + clause punctuation (every V+"ce" hit resolves to determiner+"ce"+
   noun, "ce qui/que", or "est-ce" inversion). DEAD.
2. **Relative antecedent** ("ce qui" / "ce que"): 61 follows 87, not 64/46.
   DEAD.
3. **"c'est"** (ce + etre): 59 does not follow 87. DEAD.
4. **Prepositional "ce"** ("sur ce", "a ce"): needs 24 to be a preposition;
   R17-009's verb-class support stands and no preposition value for 24 has
   any support. DEAD at standing grade.

Dislocated-topic "ce" ("…24, ce [61]…") would need a licensed resumptive;
none exists at zero assumptions — fenced as sub-route.

## The determiner arm is the sole survivor (C1, elimination leg 2)

With the pronominal arm grammatically impossible, 87 = "ce" at @644
functions as a **determiner**: "…[24] [ce 61]…" = finite/modal verb + NP
object "ce [61]" ("V ce [N/Adj]" — e.g. "veut ce [livre]").

This naming uses zero ungranted assumptions: 87=ce (granted), 24's class
(R17-009, standing), French grammar (period corpus confirms the "*V ce"
gap). It does NOT assume 61's class — it predicts it: 61 must head the
NP as nominal or adjectival ("premier"-shaped), which is exactly the arm
the parent follow-up (`val-61-646-locus`) was built to test. The premier-
61-flank-census's flank-supported @645 ("ce premier [88]", needs 88
finite) is consistent with this naming; the determination of 61's head
class stays open and is not claimed here.

One-word "87 61" rival: 61 has no letter value at battery grade (locus-level
"premier" @1556 only) — fenced as untestable sub-route, not a function rival.

## Verdict rationale

C1 PASS: 87's function at @644 is named **determiner** by grammatical
elimination, with every premise standing and zero new assumptions.
C2 moot. No adverses were listed on the target.

**Verdict: PROMOTE (function-level).** Scope: 87's function at @644 only.
This licenses the 61 adjectival/nominal arm at @645 (the "premier" route)
and closes the pronominal-87 route at this window.

## Flags for red team (not decided here)

- **S7 tension:** 87 shows pronominal-shaped uses elsewhere ("ce qui" x5,
  "ce que" x3, "c'est" x1 @823) alongside determiner-shaped "ce [78-N]"
  x2 (@572/@628, 78 nominal independent of 87). Polyvalence is barred
  (67 sole), so the global 87 function is red-team venue. This battery
  decides @644 only.
- The "24 87 11" x3 windows ("ce la") remain residual under any 87
  function; untouched.
- Canonical-stream caveat stands (row a4_02 offset unvalidated).

## Bookkeeping

- Queue: `det-87-644-function` -> `status: verdict`,
  `verdict: {result: promote, report:
  code/crowd17/report_inbox/battery-det-87-644-function.md, date:
  2026-10-09}` (pre-write assert passed — was queued/verdictless;
  temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
- No standing/red-team verdict contradicted or downgraded; S7 intact.
