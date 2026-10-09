# Battery verdict: quant-71-925-value

**Bar (verbatim from battery-queue.json):** `null` (no bars field; brief: "name 71's value at battery grade or fence the value route").

**Bar restated as numbered clauses:**
- C1: Name 71's quantifier/determiner value at 1b@925 at battery grade (positive, discriminating evidence for one value; rival values excluded or answered).
- C2: Else fence the value route with stated cause.

**Adverses:** none stated.

## Method
Read BATTERY-PROTOCOL.md first. Created `locks/quant-71-925-value.lock` on start (agent id + UTC timestamp). Re-derived the repaired stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`: 1,847 pairs / 96 types verified. `canonical.py` never touched; R5005, sealed gates, red-team adjudication queue untouched. Offsets below are 1-based on the repaired stream.

Standing values used: 11=la (gt), 17=fois (prom), 40=e (gt), 48=e (prom), 64=qui (prom), 65=noun (cls, battery), 79=tout (prom, A5), 96=par (prom).

## Locus
1b@925 (row a5_10, in-row 0): `49 74 74 40 08 65 [71] 17 61 96 48 82 98` (1b@919–930). 71 is row-initial; left neighbor 65 ends row a5_09.

## Adopted premises (not re-litigated)
- `val-71-quant-nominal` (PROMOTE): nominal@1337 vs non-nominal@925 is a §7 split candidacy; "71 fois" forces non-nominal at @925.
- `class-71-adjective` (KILL): adjective-uniform route dead at both anchor windows.
- `frame-367-la-pre` (KILL): 61="la" excluded (homophone collision with banked GT 11="la"); 71="la" excluded on the same ground.
- 67 et/veut remains the sole declared polyvalence; this battery declares no split (§7).

## C1: value naming — TESTED, FAILS (underdetermination)

**Corpus census** (lane 1841 corpus, 75 files, 34,437,202 chars, NFKD-normalized):
- "[Q] fois": une 762, deux 149, plusieurs 103, trois 90, cent 87, mille 68, chaque 66, quatre 19, maintes 8, quelques 1.
- "[Q] fois par": une 17, deux 13, trois 6, plusieurs 4, quatre 1, chaque 1, maintes 1, quelques/mille/cent 0.
- "fois X par" (X = any word): X is a past participle in the genuine hits (reçue, révélée, interrompue/interrompu, établie, vérifiée...) — i.e. the frame "[Q] fois [part] par [agent]" is the licensed geometry, which makes 61 participle-shaped (feminine, agreeing with "fois") at @927.

**Candidate elimination:**
- "la": EXCLUDED (standing kill, homophone collision with 11).
- "chaque": WEAKLY DISFAVORED — "chaque fois" strongly selects "que" (46="que" banked GT, absent here); "chaque fois par" ×1 in 34.4M chars. Not kill-grade.
- "une": frequency leader (762 "une fois"), no cell holds "un"/"une" yet — survives.
- "deux": 149 "deux fois", 13 "deux fois par" — survives; monosyllabic like most promoted values.
- "plusieurs" (103), "trois" (90): survive; no exclusion.
- "quelques": 1 "quelques fois" — survives but marginal.

**Result:** at least four values (une, deux, plusieurs, trois) parse @925 cleanly with zero unstated assumptions, and no letter-tier, cross-window, or orthographic evidence discriminates among them. Corpus frequency ranks but does not name — ranking is not battery-grade evidence for a value. C1 FAILS: no single value can be named at battery grade.

## C2: fence the value route — FIRES

The value route is fenced with stated cause: **underdetermination among ≥4 surviving candidates** (une/deux/plusieurs/trois; chaque weakly disfavored, la excluded). The class (quantifier/determiner) stands forced; the value stays open. No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands.

## Verdict: NULL (value route fenced)

**Follow-ups proposed (all verified ABSENT from battery-queue.json):**
1. `val-61-participle` (P3) — name 61's class at @927 ("71 fois [61] par [48]"). If 61 = feminine past participle, the "[Q] fois [part-fém] par [agent]" frame locks and "chaque" is further disfavored (no "que" complement); if 61 is not a participle, the frame must be re-derived and the quantifier inventory re-ranked.
2. `un-71-det-census` (P3) — census the cipher's determiner inventory for "un"/"une" across all cells: if another cell holds "une", 71="une" is excluded by homophony (cf. the 61="la" kill); else "une" remains the frequency leader and needs a positive leg.
3. `deux-71-numeral-test` (P4) — test numeral-71 ("deux"/"trois") against the left edge "65 [71] fois" under 65's noun class: does any 1841 frame license "[noun] deux fois [part] par" without a recovered verb, or does the verbless geometry force a non-numeral (determiner-like) value?

## Bookkeeping
- Queue update: `quant-71-925-value` → status `verdict`, result `null`, report `code/crowd17/report_inbox/battery-quant-71-925-value.md`, date 2026-10-09 (pre-write assert: was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock created on start, deleted on completion.
