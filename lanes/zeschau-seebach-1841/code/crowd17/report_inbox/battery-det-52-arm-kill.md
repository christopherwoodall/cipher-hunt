# Battery verdict: det-52-arm-kill

- Target: `det-52-arm-kill` (battery-queue.json, priority 3, status queued)
- Claim: "Formal kill-grade test of 52's determiner arm at @383 (currently only 'unattested')"
- Date: 2026-10-09
- Worker: battery worker (subagent fbfdeaa0-a95a-485f-aae2-d0dec6863f02). Lock `locks/det-52-arm-kill.lock` created on start (2026-10-09T19:19:00Z), deleted on completion.
- `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

> "Kill iff a window forces the determiner reading false or a distributional kill at the lane standard; else fence as unattested"

**Numbered clauses (restated before testing):**
- C1: Some window forces the determiner reading of 52 false → KILL.
- C2: A distributional kill at the lane standard (cf. the 91 determiner-kill precedent) → KILL.
- C3 (else): Neither → NULL; fence the determiner arm as unattested.

## Method

1. Read BATTERY-PROTOCOL.md first.
2. Re-derived the stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: 1,847 pairs / 96 types, asserts hold. All @-offsets 0-based queue convention.
3. Byte-confirmed the @383 locus: @383=52, @384=38, @385=37, @386=43 (row a2_07). Full window @375–391: `85 82 48 00 11 50 82 16 52 38 37 43 91 36 62 91 84`.
4. Adopted as premises (not re-litigated): battery-det-385-leftedge NULL (determiner arm "unattested"; 52 split-shaped across verb/adverb/sub-lexical tiers per val-52-630-frame; 16 verb-shaped 'a'/'est' at this window; "52-38" unit KILLed); battery-val-52-38-unit KILL (via @1343); registry 38=['verb','lead']; S5 rival (37="le" as internal determiner) stays live in red-team venue.
5. Ran the full 52 follower census (n=27) against standing classes.

## Window-level evidence

**C1 — @383 forces the determiner reading false (kill-grade):**

A French determiner requires a strictly adjacent nominal complement (modulo stacked adjectives). At @383 (`16 52 38 37 43`):

1. The immediate follower @384=38 is verb-class: registry `['verb','lead']`, and all 7 of its stream windows are verb-shaped — @826 "59(est) 38", @1113 "65(noun) 38 30(pas)", @1343 "64(qui) 52 38", @1469 "02 62 38 26(noun)", @1650 "03(verb-stem) 38", @1828 "82(m) 38", @384 "52 38 37 43". Zero nominal legs stream-wide; no nominal-38 battery exists anywhere. A determiner cannot take a finite-verb-shaped cell as its complement.
2. The only nominal in the fragment, @386=43 (noun cls), stands two cells away with the verb-shaped 38 intervening. A determiner cannot span a verb to reach its noun.
3. 52-determines-37 requires 37 to be nominal — unestablished (37 has no registry entry; the live S5 rival claims 37="le" IS the determiner, which excludes 52 anyway).
4. All rescues dead: the "52-38" compositional unit is KILLed at kill grade (val-52-38-unit, via @1343's "ce"-follower); 38-as-substantivized-infinitive is impossible (38 is finite-shaped across all 7 windows; the INF-class cells are 86/33, not 38); no re-segmentation is available on fixed bytes.
5. Robustness to the S5 fork: if 37="le" determines the fragment internally, 52 is not the determiner; if 37 is adjectival, 52 has no licensable nominal complement. Under both forks, 52-as-determiner dies at @383.

**C2 — distributional kill (corroborating):**

Full 52 follower inventory (n=27; 26 with followers), tested against standing classes:

| Follower | Class | n | Determiner-compatible? |
|---|---|---|---|
| 82 | 'm' letter (pencil) | 5 | NO — determiner cannot compose word-internally with a bare letter |
| 37 | open | 4 | claimed by adjective-slot frames, no determiner leg |
| 89 | noun (lead) | 2 | compatible but no positive leg (@284 has letter-48 left; @1081 verb-ending-06 left) |
| 38 | verb (lead) | 2 | NO — determiner + finite verb ungrammatical |
| 30 | 'pas' (prom) | 2 | NO — determiner + "pas" ungrammatical |
| 80 | open | 2 | claimed by "94 52 80 04" adverb tier |
| 94 | 'ne' (lead) | 1 | NO — determiner + clitic ungrammatical |
| 33 | INF (cls) | 1 | compatible in principle ("le manger"-shape), no positive leg |
| 87 | 'ce' (prom) | 1 | NO — stacked determiners ungrammatical |
| 67 | et/veut (polyvalence) | 1 | NO — ungrammatical under both values |
| 35/42/68 | noun (cls) | 3 | compatible but no positive leg (@1007 "la 52 35" is Tier-3 "la plus"; @1409/@1441 merely compatible) |
| 39 | 'a/à' (lead) | 1 | NO — determiner + preposition ungrammatical |
| 32 | verb (cls) | 1 | NO — determiner + verb ungrammatical |
| 86 | INF (cls) | 1 | compatible in principle, no positive leg |

14 of 26 follower-windows force the determiner reading false. The remaining windows offer zero positive determiner legs — no battery has ever named a determiner value for 52 at any of its 27 windows, and the French determiner inventory's plausible candidates are already taken (11=la, 77=le provisional, 47/87=ce, 79=tout). A determiner arm with no determiner-headed NP in 27 windows and active exclusion at 14 meets the lane's distributional-kill standard (91 determiner-kill precedent: ungrammatical geometry + hostile successor set).

## Per-clause pass/fail

- **C1 — PASS (kill-grade).** @383 forces the determiner reading false: no licensable nominal complement exists under either fork of the S5/37-adjectival split.
- **C2 — PASS (corroborating).** Distributional kill: 14/26 windows force false, zero positive legs stream-wide.
- **C3 — moot.**

## Adverse answered

- **"A kill closes the last open-class candidate at @383":** confirmed as the intended consequence — this was the bar's purpose. The kill is scoped to the determiner arm only; 52's verb tier ("qui 52" x2), adverb tiers ("ne 52 [INF]" x2, "la plus" x3), and sub-lexical tier ("t52", "pre52") are untouched, as are the parent's listed live arms at @383 (adjective/nominal/clitic — owned by other batteries, not re-litigated here).
- **"38's verb class is LEAD, not ratified":** answered — the kill does not depend on ratification. All 7 of 38's windows are verb-shaped with zero nominal legs and no nominal-38 battery anywhere; the determiner reading needs a nominal complement, and none is licensable at battery grade regardless of 38's ratification status.

## Scope

Kills only 52's determiner arm (locus @383 by forced-false geometry; arm-wide by distributional kill). Untouched: 52's verb/adverb/sub-lexical tiers, 38's verb LEAD, the S5 37="le" fork (red-team venue), the bare-NP fence from det-385-leftedge. No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact — no polyvalence declared, no value named. Canonical-stream caveat stands (row a2_07 offset unvalidated).

No follow-ups required (kill, not null).

## Verdict: KILL

## Bookkeeping

- Report filed: `code/crowd17/report_inbox/battery-det-52-arm-kill.md`.
- Queue: `det-52-arm-kill` → status `verdict`, verdict `{"result": "kill", "report": "code/crowd17/report_inbox/battery-det-52-arm-kill.md", "date": "2026-10-09"}` via target-id-unique temp file `battery-queue.json.det-52-arm-kill.tmp` + atomic rename (pre-write assert: was `queued`/verdictless; post-write JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/det-52-arm-kill.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
