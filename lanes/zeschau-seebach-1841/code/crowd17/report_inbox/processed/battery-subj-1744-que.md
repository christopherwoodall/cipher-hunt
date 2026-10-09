# Battery report: subj-1744-que (PROMOTE — finding grade)

**Target:** subj-1744-que — locate the subject of 'que [56]ent' (@1744-1747)
**Worker:** cd75ac35-cd06-4bf9-bb22-c173f9a97b59 | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py; 1,847 pairs / 96 types re-verified in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim from battery-queue.json)

"one grammatical subject placement (postverbal 65 'que [56]ent [65]' vs subject-from-fenced-left-edge) with <=1 non-granted assumption, or confirm the subject gap as a stated cause inside the @1742-1744 red-team fence"

## Bar as numbered clauses (pre-registered before testing)

1. C1 — one grammatical subject placement located: either postverbal 65 ("que [56]ent [65]") or subject-from-fenced-left-edge, with ≤1 non-granted assumption.
2. C2 (disjunct) — OR the subject gap confirmed as a stated cause inside the @1742-1744 red-team fence.

## Method

1. Re-derived the repaired stream byte-exactly per repair_parse.py; asserts hold (1,847 pairs, 96 types).
2. Re-derived the window (0-based, queue convention): @1742=94, @1743=82, @1744=46, @1745=56, @1746=40, @1747=06, @1748=65, @1749=34, @1750=07 (row a8_07/a8_08 boundary; no row break inside @1744-1748).
3. Adopted as premises (not re-litigated): rightedge-56-1745 C2/C3 (46 56 40 06 = "que" + 3pl verb "[56]e ent", zero contradiction; right edge fixed, failure isolated left of @1744); leftedge-52-86-1736 C2 (clause boundary between @1739 and @1740; @1740-1741 fenced debris); ni-1740-1742 KILL (both readings of @1739-1744 dead).
4. Tested the postverbal-65 placement against the lane's 19th-c French corpus texts (data/gutenberg-17489-miserables1.txt, gutenberg-30513/30514-tocqueville-t1/t2) for que-clause postverbal-subject licensing.
5. Censused 65 (n=25) for number/shape signals.

## Window-level evidence (@-offsets)

**Target window (byte-confirmed):**
- @1744-1747 = `46 56 40 06` = "que" (banked GT) + 56-verb-stem + "e" (banked GT) + "ent" (promoted 3pl ending, in-grant use) = subordinate clause with 3pl finite verb.
- @1748 = 65 (R18-001 granted: noun class). @1749 = 34 ('i', banked GT), @1750 = 07 — the clause after 65.

**Left-edge route (subject-from-fenced-left-edge): DEAD.**
- @1742-1744 = `94 82 46` = "ne" + "m" + "que" — verbless strain. ni-1740-1742 killed both readings of @1739-1744 (2026-10-08); leftedge-52-86-1736 fenced @1740-1741 (12-34 hapax debris) and stated the clause boundary before @1740. No nominal occupies @1742-1744; no preverbal subject is available left of the verb. The fence stands; breaching it is red-team territory.

**Postverbal-65 route: GRAMMATICAL under standing values.**
- "que [56]ent [65]": 46="que" (banked GT), 56 verb-stem class (rightedge-56-1745 C2 PASS, battery-grade), 40="e" (banked GT), 06="ent" 3pl (promoted, in-grant use), 65 noun class (R18-001 granted).
- Postverbal subjects in que-clauses are **corpus-attested in the lane's 19th-c French texts**, not an assumption:
  - Tocqueville t1: "Quelque grands et soudains **que soient les événements** qui viennent de s'accomplir en un moment sous nos yeux" — 3pl subjunctive "soient" + postverbal plural subject "les événements". Exact parallel to "que [56]ent [65]".
  - Misérables: "Quel **que soit ce rêve**, l'histoire de cette nuit serait incomplète" — postverbal subject "ce rêve".
- 65's profile (n=25) confirms nominal subject-shape: "64 65" @724 ("[65] qui la" — 65 as relative antecedent), "21 65 64 59" @1208 (R18-001 leg: "21 65 qui est 32", verb-65 kill-grade dead), "65 64 52" @1340 ("[65] qui [52]"). No window forces 65 singular; number is open.

**Rival considered:** 65 as object/complement of "[56]ent" — live as an ambiguity but does not kill the subject placement; the bar requires ONE grammatical placement, which is met. If 65 is object, the gap disjunct (C2) remains available; it is not needed.

## Per-clause pass/fail

- **C1 — PASS.** One grammatical subject placement located: postverbal 65 — "que [56]ent [65-noun]". Non-granted assumptions used: exactly **1** — 65 is plural (required for 3pl agreement; number open across all 25 windows). Postverbal-subject licensing in que-clauses is evidence-backed (two corpus attestations above), not counted as an assumption. All other premises are granted standing values/tiers.
- **C2 — not needed** (disjunct; C1 passed).

## Adverses answered

- **"fenced left edge @1742-1744"**: answered — the left-edge route is closed under standing fences (ni kill + leftedge boundary + debris fence), adopted as premises, not re-litigated. The fence is narrowed, not breached: the subject is found right of it.
- **"coordinate with leftedge-52-86-1736, do not duplicate its bar"**: honored — leftedge's bar (52's value, its boundary, A9 compatibility) untouched; only its clause-2 boundary statement reused as standing context.

## Standing-state check

No value named (56's verb identity stays open; 65's noun value stays open). No lead re-graded. No polyvalence declared (§7 intact). No red-team verdict contradicted or downgraded. R18-001 (65=noun class) used in-grant. rightedge-56-1745's NULL (56 unnameable) and leftedge-52-86-1736's NULL (52 unnameable) both affirmed and built on, not re-opened.

## Verdict

**PROMOTE (finding grade).** The subject of "que [56]ent" @1744-1747 is **65 in postverbal position** — "que [56]ent [65]" parses as a que-subordinate clause with 3pl verb and postverbal plural subject, under the single stated assumption that 65 is plural. The subject gap is closed; the @1742-1744 red-team fence keeps only its left-edge debris (the "ne m que" verbless strain), not the subject slot.

---
Lock: locks/subj-1744-que.lock created 2026-10-09T05:30:00Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No promotions made beyond this battery finding (red-team ratification required for any registry change).
