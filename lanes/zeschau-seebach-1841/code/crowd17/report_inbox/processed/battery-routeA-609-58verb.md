# Battery `routeA-609-58verb` — verdict: KILL (Route A fenced at kill grade)

## Bar (verbatim, pre-registered from battery-queue.json)

"promote the Route-A parse iff 58-verb is forced at @610 with 02 nominal; else fence Route A at kill grade"

Numbered clauses:
- **C1 (promote arm):** 58-verb is FORCED at @610 with 02 nominal → promote the Route-A parse ("qui [02-S] [58-V] ce[=cela]").
- **C2 (fence arm):** otherwise → fence Route A at kill grade.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session (`repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `repair_parse.py`). Asserts held: 1,847 pairs, 96 types. `canonical.py` never used (obsolete 1,846-pair parse).

## Window evidence

- Locus byte-exact, row a4_00 (span 0b@590–617, n=28): 0b@606–612 = `64 39 64 02 58 47 77` (1-based @607–613).
- The target's "@610" is 1-based pair indexing: 0b@609 = `02`, 0b@610 = `58`. The relative clause opens at 0b@608 = `64` = "qui" (granted).
- So the frame is: `qui(@608) [02](@609) [58](@610) [ce](@611)` — with 47="ce" promoted (A4, allophone tier).
- 58's seven windows stream-wide (0b): @55, @122, @157, @610, @1202, @1695, @1756.

## Per-clause results

- **C1 FAIL (kill grade):** 58-verb is not merely unforced at @610 — it is barred by standing red-team verdict **R19-185 (GRANT: 58=nominal, noun-class)**. R19-185's own language: "@1202 anchor (24-independent): '45 58 47' forces nominal at kill grade (ant-58-ending forced 58 non-verbal)." The @610 window carries the same `58 47` frame (0b@610–611 = `58 47`), so the nominal anchor applies directly. The battery-level `ant-58-ending` (verdict: kill) independently forced 58 non-verbal. A finite-verb reading of 58 would need a second 58 value — polyvalence is §7 red-team venue only; no battery promotion act can touch it.
- 02's class is open (`02-class-609` NULL), so "02 nominal" is not contradicted — but the bar requires BOTH arms, and the 58-verb arm is dead by standing verdict. Nothing at @610 forces the verb reading.
- **C2 FIRES:** Route A ("qui [02-S] [58-V] ce[=cela]") is fenced at kill grade with stated cause: R19-185's nominal grant + the kill-grade `58 47` nominal anchor + ant-58-ending.

## Scope

Fences only the Route-A parse (58 as finite verb at @610). Untouched: 58's standing nominal class (R19-185, unchanged), 02's open class, 47="ce" promoted, 64="qui" granted, and the sibling `58-noun-adjudicate` / `58-value-name` targets. No standing or red-team verdict contradicted or downgraded (this finding aligns with R19-185); §7 intact. Canonical-stream caveat stands (a4_00 offset unvalidated). Per §4, kills regenerate no follow-ups. Re-open is red-team venue (naming a second 58 value or overturning R19-185).
