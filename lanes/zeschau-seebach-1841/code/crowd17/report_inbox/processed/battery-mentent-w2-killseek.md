# Battery report: mentent-w2-killseek — KILL

**Target:** `mentent-w2-killseek` — kill-seek the "ne mentent" one-word rival at W2: "ne mentent est [42]" (@1182–1187) under f1-confirmed 59="est". Distinct from `mentent-580-rival` (W1-scoped, now verdict/kill).

## Bar (verbatim, pre-registered)

> Bar: kill-seek the "ne mentent" one-word rival at W2: "ne mentent est [42]" (@1182–1187) under f1-confirmed 59="est". Bar: kill iff no grammatical rescue parses W2; distinct from queued `mentent-580-rival` (W1-scoped).

Restated as numbered clauses (before testing):

- **C1 (rescue):** a grammatical rescue parses @1182–1187 under standing values (byte-exact, zero invented values) → no kill.
- **C2 (kill):** no grammatical rescue parses → KILL the "ne mentent" one-word rival at W2.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts: 1,847 pairs, 96 types — held). `canonical.py` never used.

Adopted as premises (not re-litigated):
- R19-167: 94's value is the single syllabic spelling "ne"; no split; 67 sole polyvalence.
- R19-168: the dual94 package is fenced red-team-tracked.
- R17-007: 06="ent" GRANT PROMOTE (conditional on 94="ne" STRONG LEAD — stands).
- R24: 24 finite/modal (follower ≠ 85 here).
- f1 = seg-94-82-06-f1: 59@1186='est'-as-word (0 ungranted assumptions); the "mentent est" contact ungrammatical; verb-unit alternatives dead.
- subject-1186-est42: @1186 fenced as subjectless-'est' residual ('est-il' inversion arm is red-team-reserved).
- mentent-580-rival (W1): the "ne mentent" 3pl rival killed at W1; kill targets the clause parse, not the 06 value.
- nementent-W2-subject: W1/W2 share one subject account (subjectless); the R17-007 conditional grant rests on subjectless clauses — consistent with this kill, no new red-team act requested.
- Registry: 87='ce' (prom), 82='m' (gt), 48='e' (gt), 46='que' (gt), 77='le' (prov), 59='est' (prov), 84='on' (prom), 94=['ne','lead'], 78=['ver','lead'], 76=['noun','prom'], 21/32/42=['noun'/'verb'/'noun','cls'].

## Findings

**Locus byte-confirmed:** 0-based @1182=94 @1183=82 @1184=06 @1185=06 @1186=59 @1187=42, row a6_10.

Left: @1170–1181 = `87 83 21 | 85 36 74 | 32 48 59 37 77 78`
("ce" "de" [21-noun] [85-verb-stem] [36] [74] | [32-verb] "e" "est" [37-pred] "le" [78-ver]).

Right: @1188–1193 = `06 84 59 46 07 24` ("[06] on est que [07] [24-fin/modal]…").

**Rescue audit (each tested under standing values only):**

1. **Finite-3pl clause "ne mentent" (mentir):** needs a 3pl subject. Full audit of every candidate in @1170–1187:
   - 87='ce' (prom): strictly singular. Dead.
   - 21 (noun-class, value open): "de"-complement, not a preverbal subject; naming it plural invents a value (§3), and even granting plural arguendo, it cannot govern "mentent" across the closed copular clause. Dead.
   - 76 (noun, promoted masculine): singular. Dead.
   - "le ver" (77-78): 77='le' provisional singular; plural "les vers" would be a determiner-number mismatch (kill-grade ungrammatical). Dead.
   - 32 (verb-class): not a noun. Dead.
   - 42 (noun-class, @1187, after 3sg "est"): predicative frame A1; no 3pl licensing; "est" agreement broken. Dead.
   - 84='on' (@1189, postposed): "on" takes 3sg agreement ("on ment"); "*mentent-on" ungrammatical. Dead.
   - No other NP anywhere in @1170–1187. → **No 3pl subject licensed. Dead at kill grade** (the failure is positive — slots occupied by singular-licensed items — not epistemic; French is non-pro-drop).

2. **"mentent" as noun:** no French noun "mentent". Dead.

3. **One-word "nementent":** not a French word. Dead.

4. **"ne m'ent-ent" ("entent"):** "entent" is not a French word. Dead.

5. **Mentir imperative:** imperative 2pl is "mentez" ≠ "mentent". Dead.

6. **"mentent est" double-finite:** ungrammatical (f1 decided; adopted). Dead.

7. **94 as word-final "-ne" (R19-167 segmentation distinction):** e.g. "[78]ne" + "mentent" — "verne" would invent 78's value (§3; R16-005 venue), and "mentent" still needs the absent 3pl subject. Dead.

8. **Interrogative "ne mentent(-ils)?":** no "ils" present. Dead.

9. **Pro-drop / subjunctive without matrix:** unlicensed in French declarative. Dead.

10. **Downstream 24@1193 (R24 finite/modal) as rescuer:** licenses its own clause ("est que [07] [24]…"); provides no 3pl subject for "mentent". Dead.

11. **Alternative 06 value (≠ "ent"):** R17-007 grants 06="ent"; challenging it is red-team venue. Unavailable at battery grade.

12. **"nement" + "ent" re-segmentation:** "nement" is not a standalone French word. Dead.

**C1 FAIL / C2 FIRES.** No grammatical rescue parses W2 under standing values.

## Verdict: KILL

Kills only the "ne mentent" one-word rival parse at W2 (@1182–1187). Untouched: 06="ent" (R17-007 conditional grant stands — the kill targets the clause parse, not the value), 94="ne" (R19-167/168), 82='m', f1's "est"-as-word decision, subject-1186-est42's fence, and the nementent-W2-subject evidence package (this kill is its parse-level consequence and is consistent with it). No standing/red-team verdict contradicted or downgraded; §7 intact (no polyvalence declared). Per §4, kills regenerate no follow-ups. Re-open is red-team venue only (a naming act licensing a 3pl subject, or a re-opening of R17-007).

Canonical-stream caveat stands (row a6_10 offsets unvalidated).

## Bookkeeping

- Queue: `mentent-w2-killseek` → `status: verdict`, `result: kill`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/mentent-w2-killseek.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched. `canonical.py` never used.
