# Battery report: inf-83-fork — 83 as infinitive value

- Target: `inf-83-fork` (priority 3 per queue)
- Date: 2026-10-09
- Worker: 66bfccb1-24d2-4241-b0f8-383e972d203f
- Verdict: **KILL** (of the infinitive fork; 83's value stays open)

## Bar (verbatim, pre-registered — queue text)

"resolve iff the three formula windows parse with a re-read 98 or the fork dies at those windows"

## Bar restated as numbered pass/fail clauses

1. (C1) The three formula windows `98 83 82 96 21 [60/62/68]` parse with 83 as
   an infinitive under a battery-grade re-read of 98 → resolve (promote).
2. (C2, else-branch) The fork dies at those windows: no grammatical parse of
   the formula frame with 83-as-infinitive under standing values.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/inf-83-fork.lock` on start
(2026-10-09T05:57:08Z, no prior lock). Re-derived the repaired stream
in-session: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(1,847 pairs / 96 types verified). `canonical.py` never touched. R5005,
sealed gates, red-team adjudication queue untouched. All @-offsets 0-based
(queue convention).

Standing values used as premises only (§7): 82='m', 34='i', 46='que',
64='qui', 96='par', 00='pour' (A9 class-level), 87='ce', 47='ce' (A4),
11='la', 17='fois', 77='le' (provisional), 86 INF-class (A9 grant).
Adopted without re-litigation: prof-98 PROMOTE (98 = finite-verb class,
2026-10-09), vient-98-name battery promote (98='vient'), frame-vient-parvenir
KILL ("vient de me parvenir" thirds dead), fence-83-1217 NULL ('36 77 83'
@1215-1217 fenced with 83 as designated blocker), le83-window NULL
(5/5 '98-83' windows parse as 'vient de X' under the 83='de' lead).

## Window-level evidence

83 census re-derived: n=15, byte-identical to le83-window's census.
The three formula windows (byte-identical 5-gram `98 83 82 96 21`
verified in-session; thirds vary):

- **W1** 0b@228 (row a2_01, mid-row): `87 46 98 83 82 96 21 60 71`
  = "ce que [98] [83] m par [21-noun] [60] …" (46='que' GT, 87='ce').
- **W2** 0b@1061 (row a6_04, mid-row): `09 98 83 82 96 21 62 18`
  = "[09] [98] [83] m par [21-noun] [62] …".
- **W3** 0b@1784 (row a8_09, mid-row): `23 98 83 82 96 21 68 47`
  = "[23] [98] [83] m par [21-noun] [68] …".

Phase note: W3's row a8_09 sits in the phase-uncertainty list
(phase-likelihood-row-sweep: −4.21 nats, rival phase favored). W1 (a2_01)
and W2 (a6_04) are phase-solid. The kill below stands on W1+W2 alone;
W3 is corroborating under the standing canonical parse (canonicality
caveat recorded, not litigated).

### C1 test: parse the formula with 83-as-infinitive

**"vient dire"-shaped (98 as governor):** Under standing 98='vient'
(battery-promoted, vient-98-name), "98 [83-inf]" = "vient dire".
"Venir" does not govern a bare infinitive in French of any period —
"venir de" + infinitive is the construction (it is exactly the 'de' lead's
frame). "Vient dire" is ungrammatical. FAIL.

**"le dire"-shaped (nominalized infinitive):** needs "le" immediately before
83. The token before 83 is 98 at all three windows (98≠le), and 98's own
left neighbors are 46='que' (W1), 09 (W2), 23 (W3) — no "le" anywhere in
reach. FAIL.

**Re-read 98 as a bare-infinitive-governing finite verb** ("veut/peut/doit"):
would make "98 [83-inf]" grammatical, but it contradicts the standing
battery promote vient-98-name (98='vient') — protocol forbids downgrading
an existing verdict, and a value re-read is a red-team act. Closed at
battery grade. FAIL.

**Re-read 98 as non-finite** (noun/infinitive + infinitive): contradicts
prof-98's PROMOTE (98 = finite-verb class, decided by follower census,
§5-standing). A battery cannot overwrite it; per protocol §5 this would be
a null-with-contradiction at most, and the bar's resolve arm needs a parse,
not a contradiction. Closed at battery grade. FAIL.

**Independent 82-strand (kills the fork regardless of 98):** even granting a
hypothetical "veut", the frame is "98 [83-inf] 82" = "veut dire m par …".
82='m' is banked ground truth and cannot be placed: it cannot compose
leftward ("[83]m" — no French infinitive ends in 'm'), cannot compose
rightward ("m"+"par"), cannot stand alone, and has no elision context
(96='par' is consonant-initial; proclitic "m'" belongs before the verb,
not after the infinitive). The letter strands under every fork parse. FAIL.

C1 **FAILS at kill grade**: the three formula windows force 83≠infinitive.
Every rescue either invents ungrammatical French or contradicts a standing
promote.

### C2: the fork dies at the formula windows — FIRES

Corroboration at the fork's remaining windows (outside the bar's scope,
for completeness):

- 0b@898 (a5_08): "98 83 86" — "vient dire [86-INF]": "venir"+bare-inf
  ungrammatical, and "dire"+infinitive complement ungrammatical. Dead under
  the fork; clean under the 'de' lead ("vient de [86-inf]", prof-98).
- 0b@931 (a5_10): "98 83 56" — "vient dire [56]": "venir"+bare-inf
  ungrammatical. Dead under the fork; clean under the 'de' lead.
- 0b@1217 (a7_00): "36 77 83" ('le [83]') — already fenced with 83 as the
  designated blocker (fence-83-1217, NULL).

The fork is dead at every window where it could apply. The 'de' lead
parses all five 98-83 windows (le83-window C2 5/5; prof-98 Clause 1 5/5
"vient de X") — the fork explains nothing the 'de' lead does not, and the
'le [83]' window that motivated the fork is itself fenced.

## Per-clause verdict

- C1: FAIL at kill grade (three formula windows force 83≠infinitive).
- C2: FIRES — the infinitive fork dies at the formula windows.

**Verdict: KILL** — 83-as-infinitive ('le dire'-shaped / 'vient dire'-shaped)
is refuted. Scope: kills the fork only. 83's value stays open; the
conditioned 83='de' lead is untouched (its promotion path is owned by the
queued de-83-sweep, NULL-standing).

## Adverses answered

- "coordinate with frame-vient-parvenir (98's French unconfirmed)":
  answered — frame-vient-parvenir is verdict KILL (the "vient de me
  parvenir" thirds reading is dead; not revived here), and 98's French is
  now class-confirmed by prof-98 (finite verb, PROMOTE), which supersedes
  the "unconfirmed" premise. Both adopted, neither re-litigated.
- "fights the 'de' lead at formula windows": answered — no fight remains.
  The 'de' lead parses all five 98-83 windows including the three formula
  windows (le83-window, prof-98); the fork's death is consistent with the
  'de' lead surviving. Nothing downgraded.

## Standing state

No standing verdict contradicted or downgraded; §7 intact (no polyvalence
declared — the fork's death removes a candidate, creates none). No
follow-ups proposed: the surviving 'de' lead's promotion path is already
owned by queued de-83-sweep. Canonicality caveat stands (68 of 70 upstream
row offsets unvalidated; W3's row carries the noted phase uncertainty).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-inf-83-fork.md` (this file).
- `battery-queue.json`: `inf-83-fork` → status `verdict`, result `kill`,
  date 2026-10-09 (temp-file + rename; pre-write assert confirmed
  `queued`/verdictless; JSON re-validated post-write).
- Lock `locks/inf-83-fork.lock` created on start, deleted on completion.
