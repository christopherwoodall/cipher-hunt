# Battery verdict: ce88-leftedge-402 — resolve the @400-401 '11 45' ('la ce') contact

- Target: `ce88-leftedge-402` (priority 2; queue listed 3, stored 2 — dispatched as filed)
- Claim: resolve the @400-401 '11 45' ('la ce') contact at @402
- Worker: battery worker (subagent session 02071fa7-7d4e-4a42-9e0d-c9a2fea687d5)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, repair_parse.py tokenization). 1,847 pairs / 96 types re-verified. canonical.py never used. R5005 untouched. Sealed gates untouched. Red-team queue untouched. No invented numbers.
- Lock: code/crowd17/next-token/locks/ce88-leftedge-402.lock created 2026-10-09T07:22:42Z (no pre-existing lock; nothing stale); deleted on completion.
- Verdict: **PROMOTE** (decided: 45 is non-determiner at @401 — 'ce' demonstrative pronoun; the "ce [88-noun]" determiner frame FALLS at @402)

## 1. Bar (verbatim from battery-queue.json)

"decide whether 11 belongs leftward (clause boundary / prior word), 11 is non-'la' here, or 45 is non-determiner; the 'ce [88]' frame stands or falls on the answer"

Numbered clauses (pre-registered BEFORE any window analysis; bar not modified after seeing data):

- **B1.** 11 belongs leftward: (B1a) a clause boundary falls between @400 and @401 with 'la' licensed as the prior clause's tail, or (B1b) @399-400 "06 11" form one word with 11 word-final in the prior word.
- **B2.** 11 is non-'la' at @400.
- **B3.** 45 is non-determiner at @401 (45='ce' value intact, demonstrative-pronoun role instead of determiner role).
- **B4.** The 'ce [88]' determiner-noun frame stands or falls on the answer.

## 2. Method

Re-derived the stream independently. Census facts below are byte-exact from the repaired parse. Standing values used: banked pencil (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout A5, 00=pour A9, 84=on A15, 47=ce A4, 45=ce A11 hold); provisional (59=est, 77=le). Battery-grade items cited with status labels: 06='ent' (ent-06 PROMOTE, never ratified — cited as battery-grade), 48='e' letter (battery-grade), 88=verb-class governor (battery-governor-88-value PROMOTE; battery-finiteness-88-86 PROMOTE). No battery-grade item treated as ratified.

## 3. Window-level evidence

**The locus.** @388-402, all row a2_07 except the last three on a2_08:
`36 62 91 84 73 34 67 64 79 82 48 06 | 11 45 88`
i.e. @399=06 (a2_07), @400=11 (a2_08), @401=45 (a2_08), @402=88 (a2_08).
Under standing values: `... 84=on [73] 34=i 67=et 64=qui 79=tout 82=m [48] [06] 11=la 45=ce [88] ...`
Note: an upstream row boundary falls between @399 and @400 (a2_07 -> a2_08). Recorded as a datum only; manuscript line breaks are not clause evidence (canonicality caveat stands).

**Exhaustiveness.** "11 45" occurs exactly 1x stream-wide (@400). "45 88" occurs exactly 1x stream-wide (@401). The contact is a hapax bigram; this window is the entire population for both the 'la ce' contact and the 'ce [88]' frame. The decision is window-local but covers 100% of the evidence type.

**B1b test — "06 11" as one prior word.** "06 11" occurs 4x: @319, @399, @1122, @1720. The parent battery ent-06 (PROMOTE, battery-grade) FENCED the two relevant instances with stated cause: @318-320 "94-06-11" = "neent la" (no parse, non-stem in stem slot) and @398-400 "48-06-11" = "eent la" (no parse; 48='e' letter, battery-grade). The exact window's leftward word-attachment was fenced by the owning battery. Additionally, no French word ends in "-entla"/"-mentla" (the only battery values on the table for 06), and "ment la" as adverb+article returns to the ungrammatical "la ce". **B1b: REJECT at kill grade for this window** — fenced by the parent battery with a cause that directly covers @398-400.

**B1a test — clause boundary between @400 and @401 with 'la' as prior-clause tail.** 'la' as article needs a following noun: follower is 45='ce' (dead). 'la' as object pronoun needs a governing verb in a licensed position: the leftward sequence (@390-399: 91, 84=on, 73, 34=i, 67=et, 64=qui, 79=tout, 82=m, 48, 06) offers no imperative or infinitive host; post-verbal "-ent-la" after a 3pl indicative is ungrammatical in 1841 French (enclitics attach only to imperatives/infinitives), and 48+06 carry no licensed verb+enclitic frame at battery grade. 'la' as tail of the prior clause is therefore unlicensed under every standing value. **B1a: REJECT** — no licensed 'la' reading at the clause tail (fenced residual, see §6).

**B2 test — 11 non-'la'.** 11='la' is pencil ground truth, anchored by the a5_03 manuscript crib ("la premiere", repair_parse.py gloss (i)). Zero byte-level support exists anywhere in the stream for an 11-split; §7 sole polyvalence (67 et/veut) bars a second 11 value without a red-team ruling. Adopting B2 would contradict pencil ground truth. **B2: REJECT** (rejected by elimination, not adopted — no escalation triggered since the standing verdict is preserved, not contradicted).

**B3 test — 45 non-determiner.** Positive stream precedent: "45 64" occurs 3x (@314 "78 45 64", @340 "14 45 64", @1024 "64 45 64") = "ce qui" — the textbook demonstrative-PRONOUN + relative construction, grammatical in all three windows. 45='ce' therefore already functions as demonstrative pronoun on the stream; determiner-vs-pronoun is one French word (same doctrine as the det-14-census resolution: one French word, no polyvalence), so B3 preserves the A4/A11 holds intact. At @401-402: "ce [88]" with 88 in its battery-grade verb-class governor role (battery-governor-88-value; battery-finiteness-88-86: "finite transitive verb-governor") reads "ce + finite verb" — standard French ("ce fut", "ce serait", "ce doit"). 53 as post-verbal complement is open at class level. **B3: PASS** — the only bar option with positive stream precedent and zero standing-value conflict.

**B4 — the 'ce [88]' frame.** The determiner-noun reading ("ce [88-noun]") required by noun-88-det clause 1 is KILLED at @402: "la ce [noun]" is ungrammatical, and every re-segmentation that would license it (B1a, B1b) is fenced above. The 'ce [88]' contact survives only as pronoun + verb-governor. noun-88-det's null already noted the "la ce" contact as "unresolved, non-breaking"; this verdict makes it breaking for the determiner frame: **the "ce [88-noun]" frame FALLS at @402** (window-scoped kill of the determiner reading, not of 45='ce' or of 88's class).

## 4. Per-clause pass/fail

- B1 (11 leftward): FAIL — B1b fenced by ent-06 at the exact window; B1a leaves 'la' unlicensed.
- B2 (11 non-'la'): FAIL — zero support; contradicts pencil.
- B3 (45 non-determiner): PASS — "ce qui" x3 pronoun precedent; one-word 'ce', no polyvalence; "ce [88-verb]" grammatical under battery-grade 88=verb-class.
- B4 (frame consequence): decided — "ce [88-noun]" determiner frame KILLED at @402; pronoun+verb-governor reading stands.

## 5. Adverses answered

- **45='ce' granted A4 (hold A11): ANSWERED, preserved.** B3 refines the role (demonstrative pronoun, stream-attested x3 as "ce qui"), not the value. No value change, no polyvalence declared.
- **11='la' pencil: ANSWERED, preserved.** B2 rejected; the pencil value is untouched. (The residual licensing problem at @400 is a window anomaly, fenced in §6 — it does not contradict the value.)

No standing red-team verdict is contradicted; no battery verdict is downgraded (ent-06's fence of @398-400 is used, not re-litigated).

## 6. Fenced residual (not a bar failure)

Under the B3 parse ("...[48] [06] la. Ce [88] [53]..."), @400 'la' has no grammatical license under standing values (no following noun, no governing verb, no host word, both leftward attachments fenced). This is a genuine window-level anomaly — candidate explanations: an unrecognized 1841 construction at the clause edge, or a canonical-offset object (it joins the growing list: 43-21-43 frame, 81-30 @44-45, 78-40 bigrams, 77-62 singleton, @345, @1596, 86 problem windows, 78-45 loci). The upstream row boundary between @399 and @400 is recorded as a datum, not evidence. Not decided here.

## 7. Recommended follow-ups (for supervisor queueing; verdict is promote, these are optional)

- F1. id: `la-400-residual` | priority: 3 — license or fence the dangling 'la' at @400 under the B3 parse. Bars: produce one grammatical 1841-French parse licensing @400 'la' as clause tail, or fence it as a canonical-offset object with the offset hypothesis stated. Evidence: this report §6. Adverses: 11='la' pencil (do not revalue 11); do not touch R5005.
- F2. id: `ce88-pronoun-frame` | priority: 3 — test the "ce [88-verb]" pronoun+governor frame at @401-402. Bars: 53 must parse as 88's complement/object under the verb-governor role with zero standing-value contradiction, cross-checked against 88's other governor windows (@86, @646, @1541); else fence with stated cause. Evidence: this report §3 B3. Adverses: 88=verb-class battery-grade (do not re-litigate the class; red-team venue owns ratification).

## 8. Bookkeeping

- Report: code/crowd17/report_inbox/battery-ce88-leftedge-402.md (this file).
- Queue: battery-queue.json `ce88-leftedge-402` queued -> verdict/promote, date 2026-10-09 (pre-write assert: no prior verdict; own entry only; temp-file + rename; JSON re-validated).
- Lock: created 2026-10-09T07:22:42Z (no pre-existing lock); deleted on completion.
- canonical.py never used; R5005, sealed gates, red-team queue untouched.
