# Battery verdict: det-77-86-substantivized

- Target: `det-77-86-substantivized` (battery-queue.json, priority 3, status queued)
- Claim: determiner-77's last stand via substantivized-infinitive 86 at '77 86' windows; fail -> determiner-77 closes at battery grade
- Worker: a6210833-2ead-450e-b32e-4c63da393627. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held in-session: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team adjudication queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/det-77-86-substantivized.lock` created on start (no lock present, no stale lock); deleted on completion.
- Lineage: follow-up #2 of the NULL verdict on `val-77-722-det` (follower census: 0/44 nominal followers, determiner-77 unlicensed; clitic-77 unforced). This battery tests the proposed last stand: 86's stems substantivizing under determiner-77.

## Bar (pre-registered verbatim, frozen BEFORE testing)

"revive determiner-77 iff the five '77 86' windows parse cleanly as determiner-77 + substantivized-infinitive 86 with zero new assumptions; fail at kill grade -> determiner-77 closes at battery grade"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (revive):** each of the 5 '77 86' windows (@430, @798, @877, @950, @1133) parses as provisional-77='le' governing a substantivized infinitive headed by 86 under the A9 stem-life (86 = verb stem), using only pencil/granted/provisional values, with zero new assumptions (no new value claims, no unratified classes, no elision rescues). PASS iff >=3 of 5 parse cleanly.
2. **C2 (kill):** if C1 fails AND at least one window forces the substantivization false at kill grade (ungrammatical under banked values with no stem-life-consistent rescue), determiner-77 is closed at battery grade -> verdict KILL. If C1 fails with no kill-grade window (windows merely unresolvable under current banked values), verdict NULL with 1-3 follow-ups.

Standing values used (protocol §7): pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77="le"); A9 INF-class for 86 (stem-life evidenced at 86-29 x4 per `battery-stem-86.md`); kills hold (incl. 20="fois").

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session (asserts held). Enumerated all 5 indices i with seq[i]=='77' and seq[i+1]=='86': @430, @798, @877, @950, @1133 (matches the `val-77-722-det` census exactly).
3. Pre-registered the bar above BEFORE inspecting window contents. Judged each window against banked values only.

## Window-level evidence (banked-value glosses; 77 shown as le*)

- **@430** (row a2_09): `@424-438: 14 62 e 76 42 63 le* 86 er m 16 78 63 45 que`. 86@431 followed by 29='er' (pencil). Parse: "le [stem]er" = substantivized infinitive, "le pouvoir"-shaped, under the A9 stem-life. Zero new assumptions. **PARSSES CLEANLY.**
- **@798** (row a5_04): `@792-806: que 07 qui 56 37 44 le* 86 44 74 62 98 53 69 24`. 86@799 followed by 44 (class unknown). No infinitive ending present. Substantivization would need 44 to be a verb ending (new assumption) or a bare-stem nominalization (ungrammatical in 1841 French). **FAILS — assumption gap, not forced.**
- **@877** (row a5_08): `@871-885: 89 e 20 74 49 16 le* 86 78 fois 08 31 tout 68 37`. 86@878 followed by 78 ('ver' unsettled LEAD per R16-005, verbal not nominal). No ending. **FAILS — assumption gap, not forced.**
- **@950** (row a6_00): `@944-958: 08 62 98 par 86 01 le* 86 par ce que 24 85 04 20`. 86@951 followed by 96='par' (granted), then 87='ce', 46='que' (pencil). Claimed parse gives "le [substantivized infinitive] par ce que": (a) 86 lacks any infinitive ending and the banked follower 'par' cannot be one — no stem-life-consistent rescue exists; (b) even granting the substantivization, a nominalized infinitive cannot take "par ce que" as complement in 1841 French. The verbal rescue (86 verbal so "par ce que" attaches) concedes the claimed parse and makes "77 86" = "le [verb]", ungrammatical — killing determiner-77 at this window anyway. No elision/resegmentation rescue is available under banked values. **FAILS AT KILL GRADE — the window forces the claimed parse false.**
- **@1133** (row a6_08): `@1127-1141: pour 86 52 37 86 24 le* 86 20 62 98 pour 98 78 62`. 86@1134 followed by 20 (value killed, class open). No ending. (Note: 86@1129 sits in the determiner-shaped "pour 86 52" frame — stem-86 #19 — so the two adjacent 86s are already in different lives.) **FAILS — assumption gap, not forced.**

## Clause results

- **C1: FAIL.** 1/5 windows parse cleanly (@430); 3/5 fail on assumption gaps (@798, @877, @1133); 1/5 fails at kill grade (@950). The uniform claim "the '77 86' windows parse cleanly as determiner-77 + substantivized-infinitive 86" does not hold.
- **C2: FIRES.** @950 forces the claimed parse false with banked values only (96='par', 87='ce', 46='que' + 1841 French grammar; no rescue consistent with the A9 stem-life, and the verbal rescue kills determiner-77 at the window instead). The only evidenced infinitive shape for 86 is stem+29 (A9; 86-29 x4); @950's banked follower 'par' proves the ending absent rather than merely unknown — that is what makes this kill grade rather than an assumption gap.

## Adverses

- 77='le' provisional: stands, untouched. This kill is class-level (determiner), not value-level; 'le'-as-value survives via the still-open clitic arm (`objpron-77-89`, queued as follow-up #1 of `val-77-722-det`).
- @430 determiner-compatible leg: fenced with stated cause. @430 genuinely parses as "le [stem]er", but one compatible window does not license the class against (i) 0/44 nominal followers stream-wide (`val-77-722-det`), (ii) the kill-grade forced failure at @950, (iii) 3/5 windows unresolvable without new assumptions. Recorded as the surviving determiner-compatible leg for any future re-opening (e.g. if 44/78/20 classes settle in a way that relicenses), not as a live counter.
- `battery-stem-86.md` windows #9/#11/#15/#21 (the same 77-86 windows) already fail 86='le' via "le le": consistent — 86 has no viable nominal life in 4/5 of these windows under any banked reading, leaving determiner-77 with nothing to govern. No contradiction with any standing or red-team verdict; nothing downgraded. Protocol §7 intact (A15 'l'on', A8 'ce le [verb]' frames untouched — both are non-determiner geometries for 77).

## Verdict: KILL — determiner-77 closed at battery grade

The last stand failed at kill grade. Determiner-77 is closed at battery grade per the claim's own fail clause and the pre-registered C2. The clitic-77 arm is NOT closed by this verdict (unforced per `val-77-722-det`; `objpron-77-89` remains the venue).

## Bookkeeping

- `battery-queue.json`: `det-77-86-substantivized` queued -> verdict/kill (temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated from disk; no downgrade; no other entries touched).
- Lock `locks/det-77-86-substantivized.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched. No invented data; every number traces to the repaired stream.
