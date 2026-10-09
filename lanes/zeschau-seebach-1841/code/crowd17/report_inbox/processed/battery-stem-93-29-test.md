# Battery report: stem-93-29-test

- Target id: `stem-93-29-test` (battery-queue.json, priority 3, status queued)
- Claim: "Test 93 as a verb stem via independent stem-shaped 93 windows; if \"[93]er\" becomes an attested infinitive, re-test W1's (@113) frame under Frame F"
- Date: 2026-10-09
- Worker: battery worker (subagent 87c069f9-3017-4ce8-b29d-0801106f67b6)
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 types asserted). All @-offsets below are 0-based repaired-stream
  indices. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Evidence cited: battery-x-er-89-frame.md (null-mandated follow-up; GATED on
  "[93]er" becoming an attested infinitive); de-frame-21-class (precedent: "93-29
  mirrors the X-er shape but 93-29 is not an attested infinitive. Fenced as ambiguous.");
  x-er-89-frame W1 (@113) finding.

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"[93]er" attested as an infinitive via independent windows

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) "[93]er" is attested as an infinitive via at least one window INDEPENDENT of
   W1 (@111-112, the locus under test) — i.e. a "93 29" bigram (or equivalent
   licensed composition) at a non-@111 locus parses as an infinitive under standing
   values.
2. (C2) Else: the gate condition for re-testing W1's (@113) frame under Frame F is
   not met; fence the re-test route with stated cause (verdict NULL, fence executed).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/stem-93-29-test.lock` on start
   (agent 87c069f9-3017-4ce8-b29d-0801106f67b6, 2026-10-09T21:36:00Z); will delete on completion.
2. Re-derived the repaired stream in-session; asserted 1,847 pairs / 96 types. Never used canonical.py.
3. Census of all 93 windows (14 total) and all stem-relevant bigrams involving 93:
   "93 29", "67 93", "00 93", "24 93", "93 06", "93 00", "93 40", "93 89".
4. Adopted as premises (not re-litigated):
   - er89-wordinternal-govern KILL: "29 89" is a word boundary at all five windows;
     89 standalone; the word-internal "[G]er89" fork is dead.
   - 93's standing class is VERB (R19-166); 93's value is open.
   - 29 = 'er' pencil ground truth; 06 = 'ent' conditional (06-attachment rule);
     00 = 'pour' (A9); 67 et/veut positional rule (sole polyvalence: 67="veut" iff
     follower infinitive-shaped).
   - x-er-89-frame W1 (@113) verdict: Frame F fails at battery grade because
     "[93]er" as an infinitive is an ungranted assumption.

## Window-level evidence

### Bigram censuses (re-derived, stream-wide)

| bigram | count | loci (0-based) |
|---|---|---|
| "93 29" | 1x | @111 (row a1_03) |
| "67 93" | 1x | @110 (row a1_03) |
| "00 93" | 0x | — |
| "24 93" | 0x | — |
| "93 06" | 1x | @1761 (row a8_08) |
| "93 00" | 1x | @479 (row a2_11) |
| "93 40" | 0x | — |
| "93 89" | 0x | — |

### Finding 1 — the sole "93 29" window is W1 itself, not independent

"93 29" occurs exactly once stream-wide: @111-112 on row a1_03, inside the W1
context `00 46 11 21 67 93 29 89 68 21 67` ("pour(00) que(46) la(11) [21] [67]
[93]er(29) [89] [68]..."). This IS the locus under test (the parent battery's
W1 @113 = the 89 position = 0-based 29-position + 1). No independent "93 29"
window exists anywhere in the 1,847-pair stream.

### Finding 2 — no independent stem-shaped 93 window licenses a "[93]er" attestation

- **Infinitive governors before 93: none.** 93 never follows 00='pour' ("00 93": 0x)
  and never follows the modal 24 ("24 93": 0x). The only 67-pre-93 window is
  @110, the W1 locus itself, where 67's follower is 93 (verb-class, not
  infinitive-shaped) → 67="et" by the positional rule; the 67="veut" rescue is
  circular (needs "[93]er" infinitive-shaped first) — adopted from x-er-89-frame,
  not re-litigated.
- **"93 06" @1761** (`15 93 06 77 84 09 24`): stem+'ent' = 3pl finite, consistent
  with 93's standing VERB class (R19-166) — supports verb-hood, not a
  stem+infinitive composition, and is not a "[93]er" attestation.
- **"93 00" @479** (`45 93 00 13 52 30 01`): finite-93 + purpose-"pour" is the
  standing-shaped reading; not infinitive evidence.
- **No "[93]e" route either** ("93 40": 0x) — no letter-tier composition rescues
  an infinitive reading at any independent window.

### Finding 3 — consequence for the W1 re-test

Because no independent window attests "[93]er" as an infinitive, the claim's
conditional ("if '[93]er' becomes an attested infinitive, re-test W1's (@113)
frame under Frame F") does not fire. W1's Frame-F re-test stays unlicensed at
battery grade — consistent with x-er-89-frame's NULL verdict and the standing
de-frame-21-class fence ("93-29 mirrors the X-er shape but 93-29 is not an
attested infinitive. Fenced as ambiguous.").

## Per-clause pass/fail

1. **C1 FAIL** — "[93]er" is not attested as an infinitive via any independent
   window. "93 29" is a stream-wide hapax at @111 (the locus under test itself);
   no infinitive-governor precedes 93 anywhere; the only stem-shaped contacts
   ("93 06" @1761, "93 00" @479) support the standing verb class, not a
   stem+infinitive composition.
2. **C2 FIRES** — the re-test gate stays closed. Fence executed on the W1
   Frame-F re-test route (evidentiary, re-openable iff a "93 29"-shaped infinitive
   is attested via a licensed resegmentation or a new window).

## Verdict: NULL (fence executed)

## Scope

Fences only the "[93]er"-as-infinitive attestation route and the W1 Frame-F
re-test it gates. Untouched: 93's standing VERB class (R19-166), 93's open value,
x-er-89-frame's NULL, er89-wordinternal-govern's KILL, the Frame-F 3/5 result,
67's positional rule, all standing/red-team verdicts, §7. No standing or
red-team verdict contradicted or downgraded. Canonical-stream caveat stands
(68 of 70 upstream row offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json, left for supervisor)

1. `stem-93-1761-ent` (P4) — test @1761's "93 06" as stem+'ent' (3pl finite) under
   the 06-attachment rule; a licensed 93-stem+'ent' composition names 93's stem
   shape for finite forms — the narrower stem test independent of the infinitive route.
2. `w1-113-framef-rerun` (P4, gated) — re-arm W1's (@113) Frame-F re-test iff
   "[93]er" is ever attested as an infinitive via a licensed resegmentation or a
   new window; do not dispatch until the gate condition is met.
3. `stem-93-inventory-14` (P4, gather-only) — package 93's 14 windows with
   standing-class context as red-team input on 93's stem/value candidacy
   (93's value open; class verb R19-166).

## Bookkeeping

- Lock created on start: `code/crowd17/next-token/locks/stem-93-29-test.lock`
  (agent 87c069f9-3017-4ce8-b29d-0801106f67b6, 2026-10-09T21:36:00Z); no stale lock.
- Report: `code/crowd17/report_inbox/battery-stem-93-29-test.md`.
- Queue: `stem-93-29-test` → `status: verdict`, `verdict: {"result": "null",
  "report": "code/crowd17/report_inbox/battery-stem-93-29-test.md", "date": "2026-10-09"}`.
- R5005, sealed gates, red-team adjudication queue untouched.
