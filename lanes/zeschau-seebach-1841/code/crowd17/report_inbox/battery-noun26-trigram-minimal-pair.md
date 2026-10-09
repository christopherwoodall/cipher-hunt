# Battery verdict: noun26-trigram-minimal-pair

## Bar (verbatim from battery-queue.json)

"under the stated positional rule, state the constructional difference between @1250 (verb, no 'ne' in 15) and @1560 (noun, forced boundary) for the '26 30 06' trigram, or fence it with stated cause."

## Bar as numbered pass/fail clauses

- Clause 1: under the positional rule, state the constructional difference between
  the @1250 (verb-branch) and @1560 (noun-branch) realizations of the '26 30 06'
  trigram. If no difference can be stated, fence with stated cause.

## Method

Read BATTERY-PROTOCOL.md first; created/deleted
locks/noun26-trigram-minimal-pair.lock per §6. Re-derived the repaired 1,847-pair
/ 96-type stream from data/upstream-ct_R5005.txt +
code/side-keyhunt/repaired_offsets.json (parsed per repair_parse.py);
canonical.py never touched; R5005, sealed gates, red-team queue untouched.

Offset convention: this battery family (noun-26) uses 0-based stream indices,
matching the brief. 1-based equivalents noted once: trigram A at 0-based
1250-1252 = 1-based @1251-1253; trigram B at 0-based 1560-1562 = 1-based
@1561-1563.

## Standing state taken as decided (not re-litigated)

- Positional rule (R17-020, HELD under §7): 26 = feminine noun in the article
  slot '11 (02)? 26' (@129/@240/@1560, 0-based 26-token index); 26 = verb-class
  elsewhere.
- R17-011 "'26 30' = [verb] pas": re-scoped by R18-004 from x4 to x3
  (@655/@992/@1250, 0-based); @1560 excluded.
- R18-004 (constructional GRANT): @1560 = noun under banked 11="la"; forced
  26|30 boundary; "30 06 60" is a fragment (proven by the @1733 parallel
  "30 06 60 12 48", left-independent); 'pas' heads RIGHT of the boundary as
  head of the second pas-limb.
- R17-007: 06="ent" granted (conditional on 94="ne" STRONG LEAD).
- 67 et/veut positional rule: 67="veut" iff follower infinitive-shaped.

## Byte-verified census

- Trigram '26 30 06' occurs exactly **2x** stream-wide: 0-based 1250, 1560
  (26-token index). True minimal pair.
- Bigram '26 30' exactly 4x: 0-based 655, 992, 1250, 1560.
- Bigram '30 06' exactly 4x: 0-based 1251, 1327, 1561, 1733.
- 94 census within +/-15 tokens of trigram A (0-based 1235-1267): **none**.
  The "no 'ne' in 15" premise is byte-confirmed: trigram A is a bare-'pas'
  negation with no 94 nearby.

## Window A — 0-based @1250 (verb branch)

Context (0-based): `1248:67 1249:46 | 1250:26 1251:30 1252:06 | 1253:65 1254:46 1255:01`

- 67: follower 46="que" (banked GT) is not infinitive-shaped, so 67="et"
  under the standing 67 positional rule.
- 26 = verb-class (positional rule, elsewhere branch).
- Parse: "et que [26-verb] pas ent [65-noun] que [01]..."
- The trigram is a **single verbal constituent**: [V] + pas + ent.
  '26 30' = the R17-011 "[verb] pas" bare-negation constituent (leg @1250 of
  the rescoped x3; no 94 within +/-15, byte-confirmed above); 06="ent"
  (granted R17-007) attaches as the verbal ending. No constituent boundary
  falls inside the trigram.

## Window B — 0-based @1560 (noun branch)

Context (0-based): `1557:40 1558:17 | 1559:11 1560:26 | 1561:30 1562:06 1563:60 1564:71`

- 17="fois" (granted), 11="la" (banked GT); 26 = noun (positional rule,
  article-slot branch; R18-004: "26@1560 = noun under banked 11=la").
- Forced boundary 26|30 (R18-004).
- '30 06 60' = fragment (R18-004; the @1733 parallel proves fragment status);
  'pas' heads RIGHT of the boundary as head of the second pas-limb.
- Parse: "fois, la [26-noun] | pas ent [60] [71]..."
- The surface trigram **straddles a constituent boundary**: the '26 30'
  bigram is not a constituent here — it is a boundary artifact of a nominal
  phrase followed by a pas-limb fragment. This is why R17-011 rescoped x4->x3
  with @1560 excluded.

## Clause result

- Clause 1: PASS — difference stated.

## Constructional difference (the verdict)

Under the positional rule, the identical surface trigram is licensed by two
different constructions:

- **@1250 (verb branch):** the trigram is verb-internal — "[verb] pas ent",
  the R17-011 negative-verb frame with granted 06="ent". No boundary inside.
- **@1560 (noun branch):** the trigram is a boundary artifact — "la [26-noun]
  | pas ent [60]", a nominal phrase followed by a forced boundary and a
  right-headed pas-limb fragment (byte-parallel @1733).

The minimal pair therefore CONFIRMS the positional rule's two branches at
constructional grade: the same surface string is verb-phrase-internal where
the rule says verb, and noun-boundary-crossing where the rule says noun.
No new red-team adjudication is needed; this packages R18-004 + the rescoped
R17-011 as the stated difference the bar asked for.

## Adverses answered

- "do not re-litigate noun-26's positional rule — test its two branches only":
  honored. The rule is taken as the frame; only the two trigram branches were
  tested against bytes. Nothing was re-litigated; no standing verdict
  contradicted or downgraded (R17-011 rescoped x3, R17-020 held, R18-004
  grant, R17-007 grant all respected as stated).

## Verdict: PROMOTE

The constructional difference is stated with byte-level evidence on the
repaired stream, under standing red-team adjudications. The trigram minimal
pair confirms both branches of the positional rule.
