# Battery report: reinforced-head-topology-drama

- Target id: `reinforced-head-topology-drama`
- Claim: "classify how the 41 drama dem-comma topic windows actually resolve (governed, finite, adjectival, quoted...)"
- Date: 2026-10-09
- Worker: battery worker (subagent ca665889-63ed-42f3-ab2f-b312b03929e0)
- Stream: not applicable — corpus census against period French drama, per target charter. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, ceux-là, celle-là, celles-là, celui-ci, ceux-ci, celle-ci, celles-ci), per the parent battery's DEM_REINF inventory. "Dem-comma window" = a reinforced head followed by `[,;:]` in the 14-play drama corpus (2,939,372 chars). "Governed infinitive" = an infinitive governed by a preposition (pour / à / de), per the parent's glossary — bare modal-complement infinitives ("il faut partir") are NOT counted as governed.

## Parentage

Follow-up #3 of the NULL `reinforced-pour-inf-drama` (2026-10-09), which found 0 genuine reinforced-head + governed-exclamatory-infinitive attestations in the drama corpus, with 41 dem-comma topic windows "all excluded with cause, but their actual resolutions uncatalogued." This battery catalogues them.

## Bar (verbatim, pre-registered before testing)

"a full-resolution map of the 41 windows sharpens the fence: 'reinforced heads govern infinitives, but never exclamatory'"

Numbered pass/fail clauses (restated before testing, not modified after):

1. A full-resolution map of all 41 dem-comma windows is produced — every window classified into a stated resolution class with window-level evidence.
2. ≥2 windows show a reinforced head with a governed infinitive in complement position (the bar's stated positive boundary for the sharpened fence).
3. Adverses: none pre-registered.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock `code/crowd17/next-token/locks/reinforced-head-topology-drama.lock` on start (agent id + UTC timestamp; no lock, stale or fresh, existed for this id).
2. Re-ran the parent's DEM_REINF pattern verbatim over the same 14 drama files (`code/side-period/corpus`, 2,939,372 chars). Reproduced exactly 41 dem-comma hits with identical per-file counts (musset 11, ruy-blas 6, tour-de-nesle 6, kean 4, verre-d-eau 3, burgraves 2, mariage-louis-xv 2, chatterton 2, bertrand-et-raton 2, antony 1, henri-iii 1, chapeau-de-paille 1, hernani 0, poudre-aux-yeux 0). Extraction windows widened to 500 chars for classification.
3. Every window hand-classified with ±500-char context. A governed-infinitive regex sweep over all 41 windows was run as a check; every hit was hand-audited for head-relatedness (most are unrelated downstream infinitives or noun/adjective false positives like "livre", "figure", "sombre").

## Window-level evidence: the full-resolution map

41/41 windows classified. Classes:

**A. Copular/cleft "c'est" identification — 13 windows.** The head is identified by "c'est / ce sera / n'est... que": #1 "celle-ci, ce sera, je vous le jure, une leçon pour toute ma vie" (mariage-louis-xv @172768); #8 "Celui-là, c'est Nicolini" (musset @104030); #9 "celui-là, c'est le provéditeur" (musset @104064); #12 "celle-là, Spark? C'est une romance portugaise" (musset @430933, addressee interposed); #14 "celle-là, ce sera donc l'autre que je brûlerai" (musset @928715, cleft); #18 "ceux-là, c'est un jaloux" (ruy-blas @14744); #19 "ceux-ci, c'est la jalousie" (ruy-blas @14776); #20 "Celui-là, — fût-il grand de Castille... N'est pour moi qu'un maraud sinistre" (ruy-blas @34184, subjunctive concessive + ne...que); #21 "Celle-là, c'est un ange" (burgraves @30427); #23 "celle-ci : c'est, je crois, la plus grande" (antony @59732); #25 "celui-là, c'est celui qui a voulu que tu ôtasses ton masque" (tour-de-nesle @51454); #26 "celui-là, c'est celui qui t'a fait à la figure la cicatrice" (tour-de-nesle @51517); #31 "Ceux-là, c'est la gloire de la presse" (kean @43821).

**B. Clitic resumption in a finite clause — 6 windows.** #0 "celui-là, je vous le donne" (mariage-louis-xv @115561); #2 "celle-ci, je la choisirais" (chatterton @25120); #5 "Celui-là, Cordiani, tu l'as tué" (musset @40999); #22 "ceux-ci, je les ai laissés dire" (burgraves @117981); #36 "celle-là, mais nous l'obtiendrons" (bertrand-et-raton @123054); #39 "celui-là, j'en suis sûre" (verre-d-eau @124330).

**C. Clitic resumption + governed/bare infinitive complement (head = the infinitive's object) — 3 windows.** #24 "celui-là, il faut le sauver" (tour-de-nesle @20203 — bare infinitive under modal "faut", head resumed by "le"); #35 "ceux-là, et, s'il fallait les perdre ou les voir compromis... j'aimerais mieux mourir !" (bertrand-et-raton @110103 — bare infinitives under "fallait", head resumed by "les"); #38 "ceux-là, je ne suis pas libre de les accueillir" (verre-d-eau @36952 — de-governed infinitive under "libre", head resumed by "les"; the parent's classified near-miss).

**D. Finite clause, anaphoric, no clitic resumption — 8 windows.** #3 "celle-ci, et le mérite en est grand" (chatterton @151996); #7 "celle-là ; et cependant Dieu sait si leur damnée de musique me donne envie de danser" (musset @93942, head = "leur damnée de musique", resumed by possessive "leur"); #13 "celui-là, et il a un maître à danser ?" (musset @731479); #17 "ceux-là ; et enfin, du choc de ces caractères..." (ruy-blas @3153); #29 "celui-ci ; moi qui vous demandais du repos, je suis le premier à vous dire : Il le faut" (tour-de-nesle @121981); #30 "ceux-là, morbleu ! j'ai fait une croix blanche sur leur porte" (henri-iii @33211, possessive "leur" resumption; downstream "de décrocher" governed by "l'occasion", head-unrelated); #33 "celui-là ; l'autre le trouvait trop fort" (kean @66336); #34 "celui-là, je ne ferais plus de perruques" (kean @109567, elliptic topic, no resumption).

**E. Verbless appositive / NP enumeration — 4 windows.** #15 "ceux-ci, le plaisir des yeux ; celles-là, le plaisir du cœur ; les derniers, le plaisir de l'esprit" (ruy-blas @1185, preface rhetoric); #16 "celles-là, le plaisir du cœur ; les derniers, le plaisir de l'esprit" (ruy-blas @1216); #27 "celui-ci, des murs aussi sourds et aussi épais que ceux-ci, des murs qui étouffent les cris..." (tour-de-nesle @79885); #28 "ceux-ci, des murs qui étouffent les cris..." (tour-de-nesle @79936).

**F. Colon-introduced direct speech / vocative — 2 windows.** #6 "celui-ci : Cordiani ! Cordiani !..." (musset @54850); #10 "celui-là : Je peux si je veux !" (musset @248302).

**G. Relative-clause continuation — 2 windows.** #32 "celui-là ; ce qui n'est pas difficile, en vous y prenant comme vous faites" (kean @55087); #37 "celle-ci, qui me va bien, à ce qu'on dit" (verre-d-eau @15786).

**H. Adjectival apposition + exclamation — 1 window.** #4 "celle-ci, pleine de jeunes gens, de valets !" (musset @2635). Note: this is the corpus's closest approach to an exclamatory shape with a reinforced head — but the exclaimed phrase is an adjectival apposition, not an infinitive.

**I. Verbless deictic fragment — 2 windows.** #11 "celui-là, quand j'avais douze ans, sur la couverture de mes livres de classe" (musset @421386, pointing at an object); #40 "celle-là, imbécile" (chapeau-de-paille @38030, deictic + vocative).

Class totals: 13 + 6 + 3 + 8 + 4 + 2 + 2 + 1 + 2 = 41. All 41 accounted for.

### Key quantitative findings

- **0/41**: a reinforced head directly governing an exclamatory infinitive ("celui-là, pour rire !" shape). The fenced zero holds.
- **0/41**: a reinforced head governing ANY infinitive as its subject/controller. In every infinitive window the head is the infinitive's OBJECT (via clitic resumption), never its governor.
- **1/41 strict**: a reinforced head with a preposition-governed infinitive in complement position — #38 ("je ne suis pas libre de les accueillir").
- **3/41 loose**: a reinforced head as the (resumed) object of an infinitive in a complement clause — #24, #35 (bare modal complements), #38 (de-governed).
- **22/41**: resumption-dominant resolutions (classes A+B+C) — the reinforced head in topic position is normally resumed by "c'est", a clitic, or a possessive.
- Downstream governed infinitives unrelated to the head occur in 15 windows (e.g. #1 "oubliais de vous dire", #29 "le premier à vous dire", #36 "pour renverser Struensée", #37 "peine à me décider") — all audited and excluded: their subjects/controllers are other clause participants, never the reinforced head.

## Per-clause pass/fail

1. Full-resolution map of all 41 windows: **PASS.** 41/41 classified into 9 stated classes with file + char-offset evidence above.
2. ≥2 windows with a reinforced head + governed infinitive in complement position: **FAIL (strict reading).** Only 1/41 (#38) meets the parent glossary's "governed" definition (preposition-governed). On the loose reading (any infinitive complement with the head as resumed object), 3/41 (#24, #35, #38) — but two are bare modal complements, and in all three the head is the infinitive's OBJECT, never its governor. The bar's sharpened fence as worded ("reinforced heads govern infinitives") is not earned: no window shows a reinforced head governing an infinitive.
3. Adverses: none pre-registered. Self-check: no standing or red-team verdict contradicted; §7 intact.

## Verdict: NULL (map complete; sharpening not earned)

The full-resolution map is delivered — the 41 windows' actual resolutions are now catalogued, which was this battery's commissioned work. But the bar's sharpening leg fails: the positive boundary has only one strict leg (#38), and the direction of government runs the wrong way for the bar's wording (head as infinitive object, never governor). Per §4, this is a null, not a kill: the map stands as a positive deliverable and work regenerates via the follow-ups below.

The precise positive boundary the map DOES support: reinforced heads in topic position resolve by resumption (22/41: c'est-identification, clitic, or possessive); they co-occur with governed infinitives only as the infinitive's (resumed) object inside finite complement clauses; the "head + exclamatory infinitive" shape stays at 0/41.

## Follow-ups (nulls regenerate work)

1. **reinforced-head-modal-inf-drama** (P4): test whether the 2 bare-modal windows (#24 "il faut le sauver", #35 "fallait les perdre") plus a widened bare-infinitive census form a systematic "reinforced head as infinitive object" pattern in drama. Bar: ≥3 head-as-object infinitive windows with stated government direction sharpens the fence to "heads never govern infinitives; they occur as infinitive objects."
2. **gov-inf-complement-prose-recall** (P4): run the head-related governed-infinitive search (head = resumed object of a de/pour/à-governed infinitive in a complement clause) against the 27.66M-char prose corpus. Bar: ≥1 prose replication of #38's shape earns the cross-register positive boundary; confirmed zero keeps the positive boundary drama-only.
3. **head-government-direction-redteam** (P2, red-team input, gather-only): package the direction-of-government finding (0/41 head-as-governor, 1/41 strict head-as-object of governed infinitive, 22/41 resumption-dominant) as red-team input for the personal-tonic / reinforced-head family's stream-side closure. No battery decision requested.

## Bookkeeping

- Extraction/classification script: `code/crowd17/next-token/reinforced_head_topology_drama.py` (re-runnable; reproduces the 41 windows with 500-char context; outputs `reinforced-head-topology-drama_windows.json`).
- Raw windows: `/tmp/topology_windows.json` (ephemeral; the re-runnable script regenerates it).
- Report: `code/crowd17/report_inbox/battery-reinforced-head-topology-drama.md` (this file).
- battery-queue.json: `reinforced-head-topology-drama` queued -> verdict/null via temp-file + rename (pre-write assert confirmed queued/verdictless; JSON re-validated post-write; own entry only; claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on completion. No stale lock for this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces to the named corpus files or the scripts; no invented data.
