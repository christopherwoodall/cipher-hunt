# Battery report: val-91-pp-adj (PROMOTE — finding grade, locus-level)

**Target:** val-91-pp-adj (priority 2). Worker session 5b6708d9-ae13-475f-afe4-ac245ab1a037 (supervisor-dispatched). Date: 2026-10-09.
**Stream:** repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`; 1,847 pairs, 96 groups, asserts hold). `canonical.py` never used. R5005 untouched. Sealed gates untouched. Red-team adjudication queue untouched. No data invented. @-offsets 0-indexed on the repaired stream.

## Bar (verbatim from battery-queue.json — pre-registered BEFORE testing)

"class name decides the discriminator"

## Bar as numbered pass/fail clauses (frozen before testing; not modified after seeing data)

1. **C1 (class-naming arm):** name 91's class at the 16-91 x2 windows (0b@537–538, 0b@1370–1371; the claim's "@538/@1371" is the 91 position, 0-indexed). Per the claim, past participle selects 16='a', adjective selects 16='est'.

## Method

1. Read BATTERY-PROTOCOL.md in full. Created `locks/val-91-pp-adj.lock` on start (no stale lock existed).
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types verified). 91 census n=21, byte-identical to battery-adj-91-723-second-leg's census. "16 91" bigram occurs exactly 2x stream-wide (0b@537 a3_01, 0b@1370 a7_06). "82 16" bigram occurs 11x; only these two are followed by 91.
3. Tested every word-class candidate for 91 in the "82 16 91" frame against standing values (protocol §7). Banked: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que. Granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce. Provisional: 59=est, 77=le. Battery: 94=ne (STRONG LEAD), 12=n, 48=e, 06=ent, 30=pas, 36=noun-class (R18), 67=et/veut (sole polyvalence).

## Window-level evidence

**W1 — 0b@537–538 (row a3_01):** `26 32 16 08 24 82 16 91 12 44 29 48 42 06 00 46 24 47 46 55 …` → "…[08] [24] m a [91] n [44]er e …".
- 82='m' banked letter. Frame under test: "82 16 91" = "m [16] [91]".
- 16='a' + 91=past participle: "m'a [91-pp]" — passé composé with 'me' as preceding direct object. Grammatical shape.
- 16='est' + 91=adjective: "m'est [91]" — CLOSED. Adjective-91 is fenced lane-wide (battery-adj-91-723-second-leg, verdict null/fence, 2026-10-09): among 91's 21 windows exactly one adjective-shaped window (@723, itself conditional on 03's class) exists; @538 was explicitly examined there and found not adjective-shaped.
- 91=noun: "m'a/m'est [91-noun]" — bare noun after 'a'/'est' is ungrammatical in 1841 French. Dead.
- 91=adverb/infinitive: 'a'/'est' cannot take a bare adverb or infinitive complement here. Dead.
- Past participle is the unique surviving class in this frame.

**W2 — 0b@1370–1371 (row a7_06):** `…03 30 82 16 91 67 98 00 86 29 89 84 92 69 13 24 65 68 52` → "…[03] pas m a [91] et [98] pour …".
- Same class elimination: pp ("m'a [pp]") survives; adjective fenced; noun/adverb/infinitive ungrammatical.
- 67='et' via the positional rule (follower 98 is finite-verb class, not infinitive-shaped → not 'veut').

**Cross-window check:** no other "16 91" bigram exists stream-wide, so the class naming is uniform across the only two windows. 91's value stays open (no value named); the naming is locus-level, per the lane's locus-level precedents (61="premier" @1556, 69-11="cela" @1115–1116).

## Per-clause pass/fail

- **C1: PASS.** 91 = past participle at both 16-91 windows (locus-level class naming). Per the claim's discriminator, past participle selects **16='a'** at 0b@537 and 0b@1370.

## Adverses (none listed; strains recorded as fenced residuals)

- **No overt subject for "m'a" at W1:** fenced with stated cause — subjectless clauses are battery-confirmed in this lane (battery-subj-w1-573-reroute, PROMOTE finding grade, 2026-10-09: W1's "ne mentent" confirmed subjectless). A missing subject is a residual, not kill-grade against the class naming.
- **"pas m'a" order at W2:** 30='pas' as negator normally follows the finite verb in this lane (battery-w2-pas-nelicense: ne-drop precedent, "pas" post-verbal). The pre-verbal "30 82 16" is fenced via a clause boundary ("…[03] pas | m'a [91]…", with 30 negating leftward under ne-drop) — the noun-"pas" ("step") rival is noted as unevaluated, not claimed. The strain does not overturn the class naming: the adjective arm is fenced independently of it.
- **"91 12 44 29" tail at W1** ("[pp] n [44]er e"): open segmentation residual; does not threaten the pp reading.

## Standing-state check (no contradiction, no downgrade)

- No red-team verdict on 91 exists; 91's value stays open. The adjective fence (battery-adj-91-723-second-leg) is adopted as premise, not re-litigated.
- 16's global uniformity is NOT decided here: battery-val-16-a-vs-est (verdict null/fence, 2026-10-09) forced-false the finite-verb class at @1480 (0b) and fenced the global 'a'/'est' discrimination — that fence stands. This report selects 16='a' locus-level at the two 16-91 windows only; 16's class uniformity remains red-team territory (§7: no polyvalence declared at battery level).
- §7 intact: no polyvalence declared; 67 sole-polyvalence untouched.

## Verdict: PROMOTE (finding grade, locus-level)

91 = past participle at the 16-91 x2 windows (0b@537–538, 0b@1370–1371) → selects **16='a'** at both windows. Promotes no value, re-grades no lead, declares no polyvalence. Evidence package for the red-team 16 adjudication.
