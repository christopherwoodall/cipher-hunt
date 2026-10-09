# Battery verdict: subj-62-06-1537

**Verdict: PROMOTE (finding grade).** 41 is determiner-shaped (non-nominal) at window B's "62 06" site, so the finite "[62]ent" reading loses its only candidate subject there.

## Bar (verbatim, pre-registered)

> CLAIM: test 41's class at @1536: can 41 (or the 66-73-41 phrase) serve as a 3pl subject?
> BARS: if 41 is non-nominal, the finite reading loses its only candidate subject at window B
> ADVERSES: None

Numbered clauses (pre-registered before testing):
- **C1:** Determine 41's class at 0-based @1535 (1-based @1536) — the "41" immediately preceding the "62 06" pair at window B (0-based @1536–1537, 1-based @1537–1538, row a8_00).
- **C2:** If 41 is non-nominal, enumerate all other subject candidates for the finite "[62]ent" reading at window B (66, 73, the "66-73-41" phrase, any pre-"pour" position) and confirm none is available.

Offset note: the queue uses 0-based pair indices (per stem-62-ent-665-1536's offset note). The parent brief's "@1537" is the 1-based index of the "62 06" pair. 41 sits at 0-based @1535.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/subj-62-06-1537.lock` on start, deleting on completion. Re-derived the full 1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`; 1,847 pairs / 96 types verified). `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched. Standing values used as premises only (00="pour" A9, 21 noun-class, 94="ne" STRONG LEAD); nothing re-litigated.

## Window (re-derived, byte-exact)

Window B, 0-based @1528–1544, row a8_00 (mid-row, no boundary):

`46 21 65 63 | 00 66 73 41 | 62 06 | 21 62 93 88 …`
`…            | pour …   | [62][06] | …`

i.e. 0b@1532=00("pour"), 0b@1533=66, 0b@1534=73, **0b@1535=41**, 0b@1536=62, 0b@1537=06, 0b@1538=21(noun-class).

## Per-clause results

**C1 — PASS: 41 is determiner-shaped (non-nominal) at 0-based @1535.**

1. **Frame parallel (positive evidence).** The 4-gram "00 66 73 41" occurs exactly **2x** stream-wide (0-based @1108 and @1532). At the other instantiation (0b@1108–1112): "00 66 73 41 65" = "pour [66] [73] [41] [65-noun]" — 41 sits in determiner position immediately before a nominal (65, noun class per R18). The byte-identical frame at window B puts 41 in the same determiner slot.
2. **Standing battery support.** battery-val-41-det-windows (PROMOTE, 2026-10-09) packaged 0b@1535 as a conditional determiner leg: "pour [66] [73] [41-det] [62-ne]", conditional on 62's nominal arm.
3. **Noun-41 has zero legs stream-wide.** n(41)=19, all censused byte-exact. 41's attested roles: verb after "qui" (1b@40, class-41-contact), determiner before "fois" (1b@238, class-41-contact), word-internal letter after "12" (1b@60–61, donn-41-44). No nominal-41 window exists anywhere.
4. **Bare-noun subject ungrammatical.** Even setting (3) aside, a bare "41" as subject of a finite verb is ungrammatical in 1841 French (subject NPs require a determiner or proper-noun status). The only conceivable licensor, 73, is class-open (n=6, all windows open, zero determiner-shaped legs) — an unevidenced rescue, not a reading.

Determiner is therefore the unique positively-supported reading for 41 at @1535. A determiner is non-nominal as a standalone: it cannot serve as the finite reading's subject (it needs a nominal head to its right — which is exactly the syllabic "[41-det] [62]ne" parse, not the finite one).

**C2 — PASS: no other subject candidate exists at window B.**

- **41 alone:** determiner → excluded (C1).
- **The "66-73-41" phrase:** determiner-final; French determiners precede their head. The phrase has no nominal head (66: n=19, open, zero nominal legs; 73: n=6, open, zero nominal legs). A headless determiner phrase cannot be a subject NP.
- **66 or 73 alone:** both class-open with no nominal evidence; neither can head a subject phrase.
- **Pre-"pour" position:** "pour" (00, A9-promoted) opens a prepositional phrase; a finite verb inside it cannot take a subject from outside the phrase. No candidate there by construction.
- **Number:** for completeness, 41 carries no plural marking anywhere; a 3pl subject needs plural agreement, adding a second strain to any nominal-subject rescue.

The finite "[62]ent" reading therefore has **zero** available subjects at window B. The bar's consequent fires.

## Standing-state check

- Consistent with class-41-contact (NULL): 41 is a §7 split candidate (verb @40 / determiner @238 / letter @61); this battery names 41's class **at @1535 only** (determiner), declares no polyvalence, §7 intact.
- Consistent with battery-val-41-det-windows (PROMOTE): adopts its conditional determiner leg as premise, does not re-litigate it.
- Consistent with battery-ent-06-host-census: 06's function follows 62's class; untouched.
- Consistent with battery-stem-62-ent-665-1536 (NULL): adopts window B's byte description and the "pour + finite verb ungrammatical" standing note as premises, not re-litigated. Note the finite reading was already dead on that count; this battery removes its subject independently, per the pre-registered bar.
- No standing verdict contradicted or downgraded. No value named for 41, 62, 66, or 73.

## Caveat (stated, not hidden)

The determiner reading needs a nominal head to 41's right — i.e. 62 nominal. 62's class is open (red-team venue; "règne"/"trône" live per battery-val-62-ne-noun NULL). If 62 resolves as a verb stem, 41's role at @1535 needs re-examination — but noun-41 still has zero legs stream-wide, and the finite reading remains independently dead on "pour" + finite. In no live branch does 41 serve as a nominal subject here.

## Bookkeeping

- Lock `locks/subj-62-06-1537.lock` created on start (agent id + UTC 2026-10-09T05:48:19Z); deleted on completion.
- `battery-queue.json`: target `subj-62-06-1537` queued → verdict/promote (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated post-write).
- R5005, sealed gates, red-team adjudication queue untouched. `canonical.py` never used.
- No follow-ups required (promote, not null). Residual for the red team: 62's class adjudication will reframe 41's @1535 role only in the verb-stem-62 branch.
