# battery-personal-tonic-pour-only-drama-recall — report

Follow-up #1 from NULL battery-personal-tonic-pour-inf-drama-corpus (2026-10-09):
the pour-only tonic-pronoun net with the sibling's recall widening
(400-char windows + '?' termination) on the 14-play drama corpus. Mirrors
battery-personal-tonic-governed-excl-recall (356 candidates, 0 genuine),
restricted to the pour-only governor.

## Bar (verbatim, pre-registered)

">=1 genuine under the widened net re-opens the pour-governor question; a
confirmed zero closes the recall gap for the pour governor at drama level."

## Numbered clauses

1. **C1 (re-open arm):** ≥1 genuine personal tonic pronoun topic +
   pour-governed exclamatory/interrogative infinitive under the widened net
   ('!' or '?' termination, 400-char windows) re-opens the pour-governor
   question.
2. **C2 (closure arm):** a confirmed zero (every candidate classified with
   cause) closes the recall gap for the pour governor at drama level.

## Method

- Parent: battery-personal-tonic-pour-inf-drama-corpus (null, 2026-10-09):
  5 candidates (2 strict, 3 loose-only), 0 genuine, 180-char windows,
  '!' locality only.
- Re-runnable script:
  `code/crowd17/next-token/personal_tonic_pour_only_drama_recall_census.py`
  (parent taxonomy, pour-only, recall window). Raw census JSON alongside:
  `personal-tonic-pour-only-drama-recall_census.json`.
- P1 (dislocation): `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]`
  (case-insensitive). Identical to parent and sibling.
- Window: text from the pronoun through the next `[!?]` (inclusive), capped
  at 400 chars (parent: 180 chars, `[!?.]`). Exclamatory filter: window must
  contain `!` or `?` (automatic — the window always terminates on one; kept
  as an explicit gate, per the sibling recall design).
- P3 (pour-governed-infinitive candidate): strict —
  `\bpour\s+[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b`; loose
  (clitic-tolerant, tagged separately) —
  `\bpour\s+(?:[a-zàâäçéèêëîïôöùûü']{1,4}\s+){1,2}[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b`.
  Identical to parent.
- Manual classification of all candidates (regex cannot judge exclamatory
  illocutionary force, topic status, or government).

## Corpus gate (verified on disk before testing)

- 14 unique plays, 2,969,582 chars total, 1,986 pronoun-comma hits — matches
  the parent and sibling censuses exactly. `hugo-hernani.txt` present-but-
  excluded as expected (duplicate Hernani edition). Gate: PASS.

## Yield

- **75 recall candidates** (37 strict, 38 loose-only) over 2,969,582 chars.
- **All 5 parent candidates re-appear** (offset-set overlap 5/5, verified).
  Their classifications stand (0 genuine): [00]/[01] purpose adjuncts of
  finite clauses, [02]/[03] regex noun-phrase false positives, [04]
  finite-matrix-governed.
- **70 new candidates**, all hand-classified in full window context
  (six close calls re-checked against ±400/600-char context on disk).

## Classification (70 new candidates)

**1 GENUINE.**

- **[26] dumas-henri-iii.txt @86308 — GENUINE.** "Moi, monsieur, et pour
  écrire à qui ?" Full turn: LE DUC DE GUISE: "Voulez-vous bien me servir
  de secrétaire ?" / LA DUCHESSE DE GUISE: "Moi, monsieur, et pour écrire
  à qui ?" — "Moi" is the left-dislocated tonic topic (understood subject
  of "écrire"); "monsieur" is a vocative aside; "pour écrire à qui" is a
  self-contained interrogative infinitive phrase governed by "pour"; the
  "?" terminates the infinitive phrase directly, so the illocutionary force
  falls on the infinitive; no finite verb occurs anywhere in the turn, so
  no finite-matrix government. The "et" is a discourse connective to the
  prior turn, not a governor. All four gates pass: tonic topic ✓,
  pour-government ✓, force on the infinitive ✓, self-contained ✓.
- **Sibling-disagreement note (headlined):** the sibling recall battery
  (battery-personal-tonic-governed-excl-recall) held this exact window
  (@86308) in its 356-candidate net and reported 0 genuine overall. This
  battery disagrees on this window: under the widened-net taxonomy the
  sibling itself adopted ('!' or '?' termination counting toward the
  exclamatory filter), the window satisfies every stated gate. The sibling's
  report does not give a per-candidate classification for @86308, so the
  precise ground of its rejection is unrecoverable; the most likely
  readings are (a) a stricter exclamatory-only (non-interrogative) gate,
  or (b) treating the cross-turn "et" as non-self-contained. This battery
  records the disagreement explicitly and classifies on the stated gates:
  the bar's widened net admits '?' termination, and the turn is
  self-contained (no finite verb in the speaker's utterance).

**74 non-genuine**, by confound class:

Regex false positives — noun/non-infinitive "pour X" (12): [00] "pour un
autre" (hernani @28068, "autre" noun); [21] "pour un autre" (antony
@32039); [28] "pour la première" (kean @9180, "première" noun — "la
première fois"); [29]/[30] "pour votre" (kean @53594/@66960, possessive,
not infinitive); [33] "pour la gloire", "pour un soupir" (kean @103664,
nouns); [40] "pour mon gendre" (bertrand-et-raton @104088, noun phrase);
[41] "pour ce pauvre" (@132619, noun phrase); [52] "pour la dernière"
(musset @36746, "la dernière fois"); [56] "pour rire" (@201323, "le mot
pour rire" noun phrase); [58] "pour ton père" (@463984, noun phrase);
[62] "pour rien dans l'affaire" (@780988, "rien" pronoun).

Finite-matrix-governed infinitive (dominant, 50): the "pour"-infinitive is
the purpose complement/adjunct of a finite verb in the window — [02]
("il vaudrait mieux"), [03] ("prenez-vous… Pour faire, vous, barons"),
[04] ("veux"), [06] ("verses/risques"), [07] ("écrirez"), [08]/[09]
("veux"/"sais"), [10] ("attendrai"), [11] ("connais"), [12] ("compte"),
[13] ("avez"), [14] (finite matrix in wider context), [15]
("promettant"/"écrire"), [17] ("ferais"), [18] ("étais venu"), [19]/[20]
("risquerais"/"aurais"), [22] ("auriez oublié"), [24] ("attend"), [25]
("avais besoin"), [31]/[32] ("fait"), [35] ("a besoin"), [37] ("faut"),
[38] ("ce serait"), [43]/[44] ("éloignez"/"congédiez"), [45]
("demander"), [47] ("soyons"), [48] ("viens d'écarter"), [49] ("faut"),
[50] ("laisse"), [51] ("a donné"), [53] ("ai dissipé", cleft), [54]
("bouchais"/"fallu"), [55] ("cache-t-on"), [59] ("sais"), [60] ("faut"),
[61] ("faut"), [63] ("est fait"/"ferai"), [64] ("c'est"), [65]
("descendais"), [66] ("suis cassé"), [67] ("cours"), [68] ("c'était").

Non-topic pronoun matches (6): [23] "lui, ils causent" (stage-direction
dative, "pour cacher" governed by "s'adresse"); [27] "appartient-elle,"
(henri-iii @111451 — "elle" is the inverted subject of the finite verb,
not a dislocated tonic); [36] "de moi," (tour-de-nesle @102455 — "moi"
is the object of "de", "pour promettre" governed by "raillez-vous");
[57] "devant moi," (musset @275406 — "moi" object of "devant", "pour
savoir" governed by "Attendez-vous"); [69] "dites-moi," (musset @969693
— "moi" is the imperative clitic, "pour mériter" governed by "suis-je").

Ellipsis-interrupted, force not on the infinitive (3): [34] "elle, pour te
disculper…" (kean @105373 — sibling near-miss [110], "!" terminates the
later "plus que ma vie !"); [39] "moi, Raton de Burkenstaff… et pour
escorter mademoiselle…" (bertrand-et-raton @77029 — sibling near-miss
[159], "!" terminates "À la bonne heure !"); [42] "moi, pour acheter…
or, en achetant des diamants… on cause" (verre-d-eau @14189 — the
infinitive is cut off by "…" and the turn continues with finite "on
cause"; the window's "!" belongs to a later "Ah !").

Force-termination fails — "?" / "!" belongs to a later clause or turn
(3): [05] "Eux, ces spectres masqués, pour me rendre la force?"
(burgraves @147679 — "eux" is resumed by "ils" in the finite "Qu'ils
m'ont fait boire", so "pour me rendre" reads as the purpose adjunct of
that finite clause; the self-contained exclamatory reading is available
but the finite-matrix reading is grammatical, so not genuine under
strict standards); [16] "moi, pour me conduire à ce malheureux bal."
(mariage-louis-xv @147602 — the phrase ends with "."; the window's "?"
is Marton's later "Madame n'a personne ?"); [46] "vous, près de la
reine, pour épier mes desseins et servir les vôtres." (verre-d-eau
@109034 — accusatory infinitive shape, but the phrase ends with "." and
the window's "?" is Bolingbroke's next-turn "Comment vous rien
cacher ?"; near-miss on the force-termination gate).

## Per-clause pass/fail

1. **C1 (re-open arm): FIRES.** One genuine window — [26] dumas-henri-iii
   @86308, "Moi, monsieur, et pour écrire à qui ?" — satisfies all four
   gates (tonic topic, pour-government, force on the infinitive,
   self-contained). The pour-governor question is re-opened at drama
   level: "pour" does govern a self-contained tonic-topic infinitive in
   the drama register (interrogative force; the '!' exclamatory variant
   remains unattested in this net).
2. **C2 (closure arm): does not fire** — antecedent (confirmed zero)
   false.

## Adverse

"pour-only recall net overlaps the all-governor recall net in coverage —
acceptable as the bar is governor-specific" — ANSWERED. The overlap is by
design; the bar is governor-specific and the genuine hit is pour-specific
("pour écrire"); no finding is double-counted against the sibling's
all-governor verdict, which is corroborated, not re-litigated, on the
other 74 windows.

## Verdict

**PROMOTE** — C1 fires: the widened net yields one genuine
tonic-topic + pour-governed infinitive at drama level, re-opening the
pour-governor question. Scope is narrow and stated: the genuine is
interrogative ("pour écrire à qui ?"), not the '!' exclamatory shape;
the parent's fence against the exclamatory variant stands unrefuted, and
no stream tonic-dislocation route is revived by this battery alone. The
sibling disagreement on @86308 is headlined above for the red team.

Per §4 (promote), no follow-ups are required. Noted direction (not
queued): the re-opened question now points at the '!' exclamatory
variant hunt (still zero in this net) and at the already-queued
`tonic-pronoun-stream-locate` for the stream-side prerequisite. The
already-verdict `personal-tonic-pour-only-prose` (kill) keeps the prose
register closed; this finding is drama-register only.

## Standing items

- R5005: never touched. Sealed gate instances, red-team adjudication
  queue: untouched.
- Standing §7 values: untouched, none contradicted. No standing or
  red-team verdict contradicted or downgraded; the sibling battery's NULL
  is disagreed-with on one window (headlined), not overwritten.
- `canonical.py` never used; repaired 1,847-pair stream not needed here
  (corpus battery; the stream caveat stands).
- No numbers invented: every count traces to the census script output
  (`personal-tonic-pour-only-drama-recall_census.json`).
- Lock: created on start, deleted on completion (verified below).
