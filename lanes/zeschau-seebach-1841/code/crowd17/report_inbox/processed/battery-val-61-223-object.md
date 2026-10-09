# Battery `val-61-223-object` — verdict: NULL (fence executed)

## Bar (verbatim, pre-registered)

> "name 61 iff one value parses @223 with <=1 ungranted assumption; else fence"

Restated as numbered clauses (before testing):

- **C1** — one (unique) value for 61 is named that parses @223 with ≤1 ungranted assumption → the naming claim promotes.
- **C2** — else fence value-naming of 61 at @223 (the fence arm).

Adverses: none listed.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/val-61-223-object.lock` on start (agent 775c49ca-4199-4a91-ac12-3e0c76a29cb0, 2026-10-09); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `code/side-keyhunt/repair_parse.py`: 1,847 pairs, 96 types. `canonical.py` never used.
3. Byte-confirmed the locus and rendered all 18 windows of 61.
4. Adopted (not re-litigated): R24 (24='en' iff follower=85; finite/modal verb elsewhere — at @222 the follower is 89, so 24 is finite/modal); A8 verb-frame grant for 89 (value open); 96='par' granted; 87='ce' granted; 98='vient' LEAD; 61='pren' killed globally (`seg-61-pren-polyvalence`); `val-61-contact` KILL (no single French value covers 61's four discriminating frames — global naming is kill-grade dead); `val-61-participle` NULL (participle the sole grammatical class at @926, but feminine/agent arms blocked — no value named anywhere for 61).

## Window-level evidence

**Target locus byte-confirmed** (0-based, row a2_01):
`@219=42 @220=16 @221=24 @222=89 @223=61 @224=96 @225=87 @226=46 @227=98 @228=83 @229=82 @230=96`
→ "[42-pred] [16-inf] [24-modal] [89-inf] **[61]** par ce que vient de m par …"

The object frame: modal 24 governs infinitive 89 (A8, granted); 61 is the direct object of 89's infinitive ("faire/dire/mettre [61]"), followed by the adjunct "par ce que vient de m[e]…" ("by what has just been [said] to me"). The frame itself parses with **zero** ungranted assumptions — but the frame parsing is not the bar; the bar is *naming 61's value*.

**61 census (n=18, byte-exact):** @223, @279, @281, @367, @447, @577, @645, @926, @1168, @1206, @1219, @1256, @1281, @1429, @1455, @1510, @1556, @1810. The windows are class-heterogeneous: nominal object (@223), "ce [61]" NP (@645), participle slot (@926), word-internal "prend" component (@577/@1168/@1206 — 61='nd'/'end' residual, no value), "61 31" contact (@1256), clitic/adverb-forced (@1510).

## Per-clause results

**C1 FAIL — no value is selectable at @223.** Every arm tested:

- **Object arm:** any French noun parses "89-inf [61-noun]" identically. No selectional pressure exists *from 89* (89's value is open — the whole point of the parent battery), and the right edge ("par ce que vient…") exerts none on 61's identity. Noun vs adverb vs pronominal parses identically. Per the val-03-value-census / masc-noun-86-name precedent, parsing ≠ naming. Naming any single noun would invent the value (§3 bars invention).
- **Word-internal arm ("89 61" one word):** unconstrained — 89's stem is unknown, 61's letter content at this window is unattested (61='pren' is killed globally, but nothing else is licensed). Inventing a composition partner is barred.
- **Letter-tier route:** 61 has no letter-tier neighbor at @223 (89 and 96 are word-tier). At the "55 61" windows 61 is word-internal but value-unresolved ('pre'+'nd' vs 'pr'+'end' residual).
- **Cross-window transfer:** `val-61-contact` KILL already deductively closes the global-naming route (nominal @645 vs clitic/adverb @1510 are disjoint classes). A locus-only naming at @223 would be a conditioned split — a §7 red-team act the battery cannot declare.

**C2 FIRES — value-naming of 61 at @223 is fenced** (evidentiary, re-openable — see below, not terminal).

## Headline finding for the parent (inf-89-222-value re-open strategy)

The selection direction in the parent's follow-up is reversed. The parent hoped for **object→verb** selection ("a named direct object selects among the -re candidates"). But 61's value has **no independent selective leg** at @223 or anywhere else (global naming is kill-grade dead; locus naming is unselectable). Nothing can flow from 61's side. The only viable direction is **verb→object**: once 89's value is named, 89's verb-object selectional restrictions become a real discriminator on 61's object value — which is exactly what the parent's *other* follow-ups (`inf89-letter-interior`, `inf89-222-rerun-gated`, both already queued) pursue. This follow-up's route as stated (name 61 first) is the wrong order; the fence stands until 89's value is named or the red team declares a §7 locus split.

## Scope

Fences only value-naming of 61 at @223. Untouched: the object frame itself (parses, granted premises), 89's open value, `val-61-contact` KILL, `val-61-participle` NULL, the "prend" 55-61 finding, A8, R24, §7 (no split declared), all standing/red-team verdicts. Canonical-stream caveat stands (row a2_01 offsets unvalidated).

## Follow-ups proposed (§4, all verified ABSENT from battery-queue.json)

1. `seg-89-61-word` (P4) — test the untested word-internal arm at @223: "89 61" as a single word under standing values with byte evidence; fence it or find the one licensed composition frame. If 61 is word-internal, the object theory dies and the parent's re-open calculus changes.
2. `frame-61-223-object` (P4) — census whether the direct-object frame is the *unique* parse at @223 (object vs adverb vs word-internal, per-window at battery grade); hardens the frame the eventual verb→object re-open depends on.

Not duplicated: `inf89-letter-interior` and `inf89-222-rerun-gated` are already queued (the verb-first re-open path).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-61-223-object.md`
- Queue: `val-61-223-object` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-61-223-object.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/val-61-223-object.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
