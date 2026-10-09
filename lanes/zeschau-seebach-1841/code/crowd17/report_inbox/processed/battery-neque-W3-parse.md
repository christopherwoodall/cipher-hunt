# Battery neque-W3-parse — report

**Verdict: KILL** — W03 fenced as restrictive-'ne...que'-incapable (bar else-branch executed).

## Bar (verbatim, pre-registered)

> "complete clause parse with <=1 new assumption, else fence W03."

## Bar restated (numbered, before testing)

- C1: A complete clause parse of @161–217 is demonstrated — every cell
  integrated into one grammatical clause structure hosting the restrictive
  'ne [24] ... que' frame.
- C2: The parse uses ≤1 new assumption (any value/class/grammar assignment
  beyond standing law: §7 banked/promoted/provisional values, R24, R19-167,
  class and frame grants).
- C3 (else-branch): If C1 or C2 fails, W03 is fenced as 'ne...que'-incapable.

Adverses: none stated.

## Method

Stream re-derived in-session: 1,847 pairs / 96 types from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs,
96 distinct groups). `canonical.py` never used. Adopted as premises (not
re-litigated): R24 (R19-191, 24='en' iff follower=85 else finite/modal verb,
kill-grade byte evidence); R19-167 (94 = single syllabic "ne"); §7 standing
values (11=la, 82=m, 46=que, 87=ce, 64=qui, 00=pour, 84=on, 47=ce, 59=est
provisional, 77=le provisional, 67 et/veut positional rule); class grants
(60/92/98/63 verb-class, 86 INF-class, 88 gov-class, 37/42 predicative
frames, 69/76 noun).

## Window-level evidence (0-based, byte-exact, rows a1_05→a2_01)

```
@161 94  ne        @180 87  ce
@162 24  V-fin     @181 64  qui
@163 87  ce        @182 23  (open)
@164 11  la        @183 37  pred-fr
@165 24  V-fin     @184 06  (open)
@166 82  m         @185 00  pour
@167 84  on        @186 33  (open)
@168 53  (open)    @187 16  (open)
@169 12  (open)    @188 00  pour
@170 48  (open)    @189 66  (open)
@171 21  (open)    @190 24  V-fin
@172 60  V-cls     @191 87  ce
@173 09  (open)    @192 98  V-cls
@174 87  ce        @193 56  (open)
@175 86  INF-cls   @194 47  ce
@176 21  (open)    @195 01  (open)
@177 69  N         @196 21  (open)
@178 14  (open)    @197 60  V-cls
@179 24  V-fin     @198 08  (open)
                   @199 67  et (§7: follower 76=N, not infinitive-shaped)
                   @200 76  N
                   @201 87  ce
                   @202 11  la
                   @203 92  V-cls
                   @204 63  V-cls
                   @205 42  pred-fr
                   @206 06  (open)
                   @207 77  le (prov)
                   @208 44  (open)
                   @209 50  (open)
                   @210 88  gov-cls
                   @211 19  (open)
                   @212 74  (open)
                   @213 77  le (prov)
                   @214 78  ver (LEAD R16-005)
                   @215 06  (open)
                   @216 59  est (prov)
                   @217 46  que
```

R24 arms (byte-exact): 24@162 follower 87≠85 → verb; 24@165 follower 82≠85
→ verb; 24@179 follower 87≠85 → verb; 24@190 follower 87≠85 → verb.
Four finite/modal verbs in the ne–que span, plus provisional 59='est'@216.

Subordinator census in @161–216 (byte-exact): 46: none (only @217);
94: none (only @161); 64='qui': @181 only — post-verbal, introduces the
nominal free relative "ce qui"@180–181 inside 24@179's clause, does not
subordinate 24@179; 00='pour': @185/@188 — preposition, cannot subordinate a
finite clause; 67='et'@199 — coordinator at best, still multi-clausal.

Open cells (no standing value; kills/holds/splits name no values): 22 —
@168(53), @169(12), @170(48), @171(21), @173(09), @176(21), @178(14),
@182(23), @184(06), @186(33), @187(16), @189(66), @193(56), @195(01),
@196(21), @198(08), @206(06), @208(44), @209(50), @211(19), @212(74),
@215(06).

## Per-clause results

- **C1 FAIL at kill grade.** The restrictive 'ne...que' frame is monoclausal
  by definition: "ne" scopes to its clause's finite verb and "que" is that
  same clause's restrictive particle — ne@161 and que@217 must be
  clause-mates. The span contains three further R24 finite verbs (@165, @179,
  @190), each heading a clause, and the byte-exact subordinator census finds
  no licensed subordinator for any of them (no complementizer 46 in span;
  "qui"@181 post-verbal; "pour"@185/@188 cannot take finite; "et"@199
  coordinates at best). The span is therefore ≥4 clauses; ne@161 and que@217
  are not clause-mates; the restrictive 'ne [24@162] ... que@217' frame is
  structurally impossible. This is a proof from standing law, not a
  non-discovery. Auxiliary count: 22 open cells → any complete parse needs
  ≥22 new assignments.
- **C2 FAIL (consequence).** Assumption budget is 1; the floor is ≥22 for a
  complete parse and the structural bar (C1) is independently unpassable.
- **C3 EXECUTES.** W03 (@161–217, rows a1_05→a2_01) is fenced as incapable of
  hosting a genuine restrictive 'ne [24] ... que' frame.

## Adverses answered (self-raised; none pre-registered)

- "24's value is unnamed (sait/veut open; sait-veut-24-discriminator in
  flight)": the kill needs only 24's finiteness (R24, standing), never its
  value. Untouched.
- "The extra finite verbs could be subordinated": exhausted byte-exact —
  no complementizer, no pre-verbal relative, "pour" finite-incompatible,
  "ce qui" nominal and post-verbal. Answered.
- "Uniformity / 24 mutual-kill escalation": not touched; R24 adopted as
  premise per protocol.
- "Restrictive monoclausality premise": definitional French grammar —
  *"il ne dit [que Marie] que vient" is not a restrictive pairing; "ne"
  and restrictive "que" are clause-mates. Not a new assumption.

## Verdict rationale

C1 fails at kill grade: the window's own structure forces the claim false —
no ≤1-assumption complete parse can exist, and the restrictive pairing
ne@161/que@217 is structurally severed by intervening clause boundaries.
Per the bar's else-branch, W03 is fenced. Combined with
`neque-15slot-fence`'s promote, all 16 nearest-46 '94...46' windows are now
fenced as restrictive-'ne...que'-incapable: the restrictive
'ne...que'-bracket family is closed at battery grade.

Scope: frame-shape fence only. No cell value killed or named (24's value,
que@217's actual governor — e.g. complementizer of a following clause —
and all 22 open cells untouched). No standing/red-team verdict contradicted
or downgraded (R24, R19-167, R19-191, §7, R16-005 LEAD all adopted).
Canonical-stream caveat stands (row offsets unvalidated beyond a5_03).

No follow-ups required per §4 (kill, not null). Loose ends for the lane's
record (not queued): que@217's true governor; 24's value
(sait-veut-24-discriminator in flight, lock live at run time).

## Bookkeeping

- Target: `neque-W3-parse`, status queued → verdict at start of run.
- Lock: created 2026-10-09T21:21:34Z (no prior lock), deleted on completion.
- Queue write: target-id-unique tmp `battery-queue.json.neque-W3-parse.tmp`
  + atomic rename; JSON re-validated from disk; own entry only; no downgrade.
- R5005, sealed gate instances, red-team adjudication queue untouched.
