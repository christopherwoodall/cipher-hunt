# Battery verdict: stem-85-then-1700

- Target: `stem-85-then-1700` (battery-queue.json, priority 2, status queued)
- Claim: re-test @1699-1702 once stem-85 names 85's value (the true discriminator)
- Worker: aad6071c-1e33-4b50-9cb9-252aeddbdc6c. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- All @-offsets are pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/stem-85-then-1700.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"resolve @1700 iff the named 85 yields a grammatical clause under exactly one of the two 30 values"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C0 (trigger):** stem-85 has named 85's value at battery grade — i.e. a battery-grade value exists to re-test @1699-1702 against.
2. **C1:** @1700 resolves iff the named 85 yields a grammatical clause under exactly one of the two 30 values (bar's discriminator).
3. **C2:** every listed adverse is answered (none listed).

Standing values used (per protocol §7): pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); frames granted (A3 85 verb-stem class, value open).

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Checked the trigger condition FIRST: read `stem-85`'s queue entry and its verdict report (`code/crowd17/report_inbox/processed/battery-stem-85.md`, verdict dated 2026-10-08).
3. Did not test C1: the discriminator cannot fire without a named value.

## Clause results

- **C0: FAIL — trigger unresolved.** `stem-85` (bar: "promote iff value named with >=2 independent verb-stem frames") returned **verdict null** on 2026-10-08: no value for 85 was named. Its findings: the "que [85]er" frame leg does not re-derive (the second leg belongs to 42, not 85; no 46-85 bigram stream-wide); of five "en [85]" legs, 3 are clean gerunds and @733 is genuinely ambiguous between a gerund adjunct and a finite-85 pronoun-cluster parse. 85's value remains open at battery grade. No subsequent report (through this run, 2026-10-09 ~10:26 UTC) names 85's value.
- **C1: not testable** — the bar's discriminator ("the named 85") has no input. Testing C1 without a named value would require inventing a value, which protocol §3 forbids.
- **C2: PASS** — no adverses listed.

## Verdict: NULL (fence)

The bar is self-gating and its gate is closed: the trigger "once stem-85 names 85's value" has not fired. This is a fence, not a refutation — no window forced the claim false, because the claim's condition was never met. Running C1 now would be a guess, not a test.

No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Queue companions with the same gate (`croire-33-compound85`, `laisser-gate-85`) remain queued and untouched.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `stem-85-value-rerun` (P3) — the true gate itself: re-run stem-85's bar ("promote iff value named with >=2 independent verb-stem frames") under current standing values. The 2026-10-08 run predates several standing-value shifts (e.g. stem-03 verb-stem promoted 2026-10-09; 01-verbclass @1256 leg). A value named here unlocks this target plus `croire-33-compound85` and `laisser-gate-85`.
2. `val-85-1700-compound` (P3) — narrow alternative: name 85's value from the @1699-1702 "85 33 94 30" compound locus itself (byte-verified `91 85 33 94 30` at row a8_06; cf. stem-85's W-at-1699). If 85 compounds with "33 94 30" as dire/croire, the value is licensed directly at the locus this target was meant to re-test.
3. `stem-85-then-1700-rerun-gated` (P4) — gated re-run of this exact bar once follow-up 1 or 2 lands a named value; resolves @1700 under exactly one of the two 30 values as the bar's discriminator requires.

## Bookkeeping

- `battery-queue.json`: `stem-85-then-1700` queued → verdict/null (temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated; no downgrade).
- Lock `locks/stem-85-then-1700.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
