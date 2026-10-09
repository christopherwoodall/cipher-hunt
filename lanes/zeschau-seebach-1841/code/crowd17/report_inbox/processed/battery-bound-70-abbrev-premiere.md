# Battery `bound-70-abbrev-premiere` — verdict: NULL (abbreviation arm fenced)

Target: test 70 as manuscript abbreviation of "premiere" (the pencil gloss "la pre m i er e" writes "pre" as the head). Date: 2026-10-09. Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-work). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. Lock `code/crowd17/next-token/locks/bound-70-abbrev-premiere.lock` created on start (agent-session e1573c9c-029a-41b9-8cca-3ba0fd572904, 2026-10-09T10:51:15Z); deleted on completion.

## Bar (verbatim, pre-registered)

"resolve iff attested at battery grade; else fence the abbreviation arm"

Numbered clauses (fixed BEFORE the stream census, not modified after):

- **C1:** 70 reads as a manuscript abbreviation of "première" at ≥1 window with a licensed parse under standing values (attestation at battery grade).
- **C2 (else-arm):** the abbreviation arm is fenced with stated cause if no such window exists.

## Method

1. Full census of 70 (n=15, byte-exact on the repaired stream): every window's follower and left context enumerated.
2. Each window tested for a slot that could admit "premier/première" under standing values (banked pencil: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; grants: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; provisional 59=est, 77=le).
3. The only candidate window (@368, the only "70 17" stream-wide) deep-read with full ±6 context.

## Window-level evidence

"70 X" follower census (all 15, byte-exact): 98, 12, **17(@368, unique)**, 91, 88, 82(×2, gloss loci @755/@1035), 87, 39(×2), 12(×3 total), 37, 52, 64.

- **@755 / @1035 (rows a5_03, a6_03):** the pencil-gloss-anchored flagships "11 70 82 34 29 (40) 17" = "la pre m i er e (fois)". The gloss spells "pre" as a **syllable** of a fully spelled-out word — it attests 70="pre" as a syllable, not as an abbreviation of "première". The abbreviation arm gets no support from the gloss; if anything, the gloss's spelling-out works against abbreviation.
- **@368 (row a2_06):** the ONLY "70 17" ("pre" + "fois", promoted) window stream-wide. Full context (0-based): `362=76 363=47 364=78 365=48 366=49 367=61 368=70 369=17(fois) 370=06 371=21 372=65 373=63 374=29 375=85 376=82`. The abbreviation parse reads "…[48] [49] [61=la] [70=première] fois…" = "[48] [49] la première fois". It requires **≥3 unstated assumptions**: 61="la" (61's global value is kill-grade dead per val-61-contact; locus-level "la" is the unproven venue of queued frame-367-la-pre), 49's value (fully open), and 48's value (open; {48,94} homophony killed, 48="est"/"ne"/"de" killed). The parse is not licensed under standing values.
- **All other 13 windows:** no slot admits "premier/première" under standing values (@235 "pre"+"vient"(98); @347 "06 pre 12"; @519 "09 pre 91"; @615 "83 pre 88-verb"; @868 "86 pre ce(87)"; @1067 "18 pre 39"; @1118 "88-verb pre 12"; @1300 "02 pre 37-predicative"; @1331 "94 pre 52"; @1547 "46-que pre 12"; @1586 "36 pre qui(64)" — the stranded "pre", fenced by stem48-qui-65-hapax; @1604 "44 pre 39").

## Per-clause results

- **C1: FAIL.** No window gives 70 a licensed "première" reading under standing values. The two gloss windows license 70="pre" as a syllable (attested), not as an abbreviation (unattested). The only abbreviation candidate (@368) needs ≥3 unstated assumptions.
- **C2: FIRES.** The abbreviation arm is fenced at battery grade with stated cause: (a) attestation is absent — the gloss spells the word out; (b) the single candidate window (@368) is a quadruple hapax ("49 61", "61 70", "70 17" each 1/1,847) whose abbreviation parse needs ≥3 unstated assumptions (61="la", 49's value, 48's value).

## Scope

Fence, not kill: no window forces "70=première-abbreviation" false, so kill grade is not met. The fence closes the arm as a **battery-grade claim** only. The queued `frame-367-la-pre` target's venue ("test 61='la' with 70 as abbreviation of 'première'; needs 49's value") is preserved — it is gated on exactly the assumptions this battery found missing, so there is no contradiction: when 49's value and 61's locus value resolve, that target fires on its own bar. No standing or red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands (row a2_06 offset unvalidated).

## Follow-ups proposed (for supervisor queuing)

1. `abbrev-70-367-rerun-gated` (P4) — gated re-run of this bar once 49's value and 61's locus value resolve; fires iff the abbreviation parse then licenses with ≤1 assumption. Red-team-adjacent venue (feeds frame-367-la-pre).
2. `prem-abbrev-corpus` (P3) — corpus check of 1841 manuscript/diplomatic abbreviation practice: does "pre." stand for "premier/première" as a whole word in the lane's period texts? If unattested in practice, the fence hardens toward kill; if attested, the arm re-opens as licensed.
3. `locus-368-fullparse` (P3) — full-clause parse of @362–376 under newly-resolved 48/49/61 values; the "48 49 61" left trigram is the real load-bearer of the @368 residual.

## Bookkeeping

- Queue: `bound-70-abbrev-premiere` queued → verdict/null via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated post-write.
- Lock `bound-70-abbrev-premiere.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
