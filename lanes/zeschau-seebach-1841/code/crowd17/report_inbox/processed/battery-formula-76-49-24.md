# Battery `formula-76-49-24` — verdict: PROMOTE (frame licensed as formula)

- Target: `formula-76-49-24`
- Claim: "test the byte-identical '76 49 24 26 30 03' x2 frame (@652/@989) as a licensed 1841 French formula"
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue
  untouched.
- Lock: `code/crowd17/next-token/locks/formula-76-49-24.lock` (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

">=1 genuine 1841 formula attestation licenses the frame ('N [49] [V] …'); confirmed zero fences it as an unparsed repeat"

## Numbered pass/fail clauses (restated before testing, not modified after)

1. **C1 (license arm)** — >=1 genuine 1841 attestation of the frame's head
   geometry ('N [49] [V] …') as a licensed formula licenses the frame.
2. **C2 (fence arm)** — confirmed zero genuine attestations fences the frame
   as an unparsed repeat. (Fires only if C1 fails.)

## Adopted premises (not re-litigated)

- `formula-49-value` NULL (2026-10-09): 49 fenced class-open; verb,
  determiner, relative/interrogative pronoun killed globally for 49; leading
  surviving leg = adjective (post-nominal position at the x2 frame is its
  positive evidence; hostile windows @366, @420 recorded there).
- Standing values: 76 = masculine noun (promoted R19); R24 — 24 is
  finite/modal verb unless follower is 85 ("en"); 00=pour (A9); 11=la (GT).
- 26, 30, 03 unvalued at this window (03's verb-stem class is scoped to the
  three `03 29` windows per R19; here 03's followers are 62 @657 / 60 @994).

## Window-level evidence (byte-exact, 0-based)

The 6-gram "76 49 24 26 30 03" occurs exactly 2x stream-wide:

| pos | row | window (±3) |
|-----|-----|-------------|
| @652 | a4_02 | `52 82 94 [76 49 24 26 30 03] 62 16 00` |
| @989 | a6_01 | `89 48 01 [76 49 24 26 30 03] 60 67 11` |

Both 24s (@654, @991) have follower 26 (not 85): R24 declares them
finite/modal verbs. Both 76s carry the promoted masculine-noun class.
Under 49's leading adjective leg the head reads "[N-masc] [49-adj]
[V-finite] …" — the canonical post-nominal-adjective position, repeated
byte-identically. Left contexts differ (`52 82 94` = "…m ne" vs
`89 48 01` = "…e [01]"), so the frame starts at 76 in both windows.

## Method (corpus test)

Census over `code/side-period/corpus` (75 text files, 34,525,238 chars —
the period prose corpus family; whitespace-normalized regex). Searched the
frame's head geometry directly: NOUN + single ADJECTIVE + FINITE VERB, with
stock diplomatic noun heads
(gouvernement/conseil/ministère/cour/Majesté/Altesse/Roi/Empereur/ministre/
ambassadeur/sultan/pacha/prince…), 1841 adjective forms, and finite verb
forms (a/est/sont/ont/avait/fut/sera/veut/décide/ordonne/approuve/s'est/
vient/peut/doit/nomme/accorde/refuse/exige…). Every unique phrase was
hand-checked in context against the genuine criterion: a real 1841 French
sentence with the N-ADJ-Vfinite geometry. Census saved to
`code/crowd17/next-token/formula-76-49-24_census.json`.

## Findings

**C1: PASS.** 98 raw hits, **66 unique genuine phrases** with the
'N [adj] [V-finite]' geometry in 1841 French. Hand-verified examples:

1. `revue-deux-mondes-1841-q1.txt@350025` — "Le gouvernement français **a**
   eu le tort réel, et nous l'avons déjà reconnu…" (N ADJ V-finite, 3sg)
2. `revue-deux-mondes-1841-q1.txt@1164735` — "le conseil municipal **accorde**
   à l'instituteur public un traitement supplémentaire…" (N ADJ V-finite, 3sg)
3. `revue-deux-mondes-1841-q1.txt@1918569` — "Le gouvernement anglais **n'a**
   pas désavoué ses agens." (N ADJ V-finite negated)
4. `talleyrand-memoires-v1.txt@508067` — "Le gouvernement américain **s'est**
   trop laissé entrainer par sa position géographique…" (N ADJ V-finite)
5. `revue-deux-mondes-1841-q2.txt@2071958` — "Le ministère anglais **s'est**
   montré à l'intérieur, dans son intérêt personnel…" (N ADJ V-finite)
6. `revue-deux-mondes-1841-q2.txt@2319137` — "Le gouvernement espagnol **a**
   toujours redouté pour ses états d'outre-mer…" (N ADJ V-finite)
7. `revue-deux-mondes-1841-q3.txt@478477` — "Le gouvernement prussien **a**
   intérêt à satisfaire les vœux légitimens du pays…" (N ADJ V-finite)

The frame's head geometry — masculine noun + single modifier + finite verb —
is a genuinely licensed formulaic construction in 1841 diplomatic French,
attested dozens of times across Revue des Deux Mondes (1841 quarters),
Talleyrand's Mémoires, and Nesselrode. This is exactly the geometry the
x2 cipher frame requires under 49's leading adjective leg
(`formula-49-value`: verb/determiner/relative-pronoun all killed for 49;
adjective survives).

**C2: does not fire** (C1 passed; no confirmed zero).

## Scope (explicit)

The license covers the frame's **head geometry** ('N [49] [V] …') as the bar
scopes it. It does NOT attest the full 6-cell string — cells 26, 30, 03 are
unvalued at these windows, so no literal French string can be matched to
the tail; 26/30/03 stay open. The license is consistent with adjective-49
but does not name 49's value (red-team/queue venue: `adj-49-420-366`,
`noun-49-909-875`). No standing or red-team verdict contradicted or
downgraded; §7 intact (67 sole polyvalence); canonical-stream caveat stands
(rows a4_02/a6_01 unvalidated).

## Verdict: PROMOTE

C1 passes with 66 unique genuine attestations; no adverses listed. The
byte-identical '76 49 24 26 30 03' x2 frame is licensed as a formulaic
'N [49] [V] …' construction in 1841 French. Per §4, promote proposes no
mandatory follow-ups; the frame's tail (26/30/03) and 49's value remain
open work for the queued targets above.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-formula-76-49-24.md` (this file).
- Census: `code/crowd17/next-token/formula-76-49-24_census.json` (66 unique
  phrases with file@offset, match, context).
- Queue: `formula-76-49-24` status `queued` -> `verdict`, result `promote`,
  date 2026-10-09 (pre-write assert confirmed queued/verdictless; temp-file
  + rename; JSON re-validated post-write; only this entry's keys touched;
  no downgrade).
- Lock created at start, deleted at end (verified gone).
