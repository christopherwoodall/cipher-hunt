# Battery report: fois-corpus-article-audit

- Target id: `fois-corpus-article-audit`
- Claim: "audit the round-14 fois corpus X-inventory for article-completeness (standalone vs article-dependent predecessors)"
- Date: 2026-10-09
- Worker: battery worker (subagent 5ec210e4-fbb1-4b9c-a00e-07b407fcba39)
- Stream/corpus: lane period corpus `code/side-period/corpus/` (1840–42 diplomatic French, ~4.06M raw tokens incl. German files), re-audited in-session. `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/fois-corpus-article-audit.lock` (created on start, deleted on completion).

## Bar (verbatim, pre-registered before testing)

"re-audit the corpus \"fois que\" predecessor inventory for article-completeness"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) For each X in {cette, plusieurs, deux, dernière} (plus {chaque, une} as the det-20-value c1-survivor context), record from the corpus "X fois que" bigrams whether each attestation carries a preceding article ("[art] X fois que").
2. (C2) Classify each X as standalone determiner (admissible at @307's bare slot: "88 02 88 [20] 17 46") vs article-dependent (needs 88/02 to supply the article) vs unattested in the subordinator frame.

## Method

1. Read BATTERY-PROTOCOL.md first; created/deleted the lock per protocol.
2. Tokenized all 34 corpus txt files (lowercase, punctuation stripped); searched "X fois que" bigrams with the two preceding tokens recorded.
3. For every target X, read the full context of each hit to distinguish the genuine subordinator frame ("X fois que [clause]") from lookalikes (comparative "aussi X cette fois que", adverbial "plusieurs/deux fois" + que-clause).
4. Adopted det-20-value's frame: the round-14 fois corpus X-inventory is {chaque, cette, dernière, plusieurs, une, deux}; @307's slot ("88 02 88 [20] fois que") is bare.

## Corpus census (re-derived; cf. fois-battery's 91)

"fois que" bigram predecessor counts in my tokenization: les 25, première 24, chaque 15, une 10, dernière 4, la 3, deux 3, plusieurs 3, seconde 2, cette 2, bonne 1, millième 1, mainte 1 (+ OCR junk "215"). The fois-battery (2026-10-07, round-14) reported 91 with les 22, première 19, chaque 15, une 9, dernière 4, plusieurs 3, la 2, deux 2, cette 2 — same inventory, my slightly higher totals reflect no French-langvote paragraph filter; the article-status findings below are 100%-within-class and robust to the count delta.

## Window-level evidence (per-X article audit)

- **dernière (4 attestations): 4/4 carry the article "la".** Contexts: "la dernière fois que ce prince y a passé", "c'est la dernière fois que vous le voyez", "la dernière fois que je vous ai vu", "me dit-elle la dernière fois que j'eus". → **article-dependent**: at @307, "dernière" alone cannot fill the bare slot; 88/02 would have to supply the article (e.g. "88 02 88 [dernière] fois que" would need the unattested "la").
- **cette (2 attestations): corpus-unattested as a subordinator.** Both hits are the comparative, not the subordinator frame: "aussi net cette fois que la première" (RdM q1) and "aussi négligée cette fois que dans les Dernières Paroles" (RdM q3) — "as clean/neglected this time as…". Zero genuine "cette fois que [clause]" in the corpus. → **unattested**; no article status to record.
- **plusieurs (3 attestations): corpus-unattested as a subordinator.** All three are adverbial "plusieurs fois" (several times) followed by an independent que-clause: "on a imprimé plusieurs fois que les misères…" (printed several times that…), "il se faisait redemander plusieurs fois quelques bouteilles" (asked several times for…), "dit plusieurs fois que" (said several times that…). → **unattested** in the subordinator frame.
- **deux (3 attestations): corpus-unattested as a subordinator.** "m'a répéta deux fois que, sur toutes choses…" (repeated to me twice that…), "par deux fois que la cantatrice se mît" (twice, that the singer…). Adverbial "deux fois"/"par deux fois" + que-clause. → **unattested** in the subordinator frame.
- **chaque (15 attestations): 15/15 bare, no article.** E.g. "chaque fois que je voyais", "chaque fois que le poste sera devenu vacant", "et chaque fois que, par quelque événement nouveau". → **standalone determiner**, admissible at the bare slot.
- **une (10 attestations): 10/10 bare, no article.** E.g. "une fois que vos troupes n'y seront plus", "encore une fois que cela ne se peut pas", "une fois que les relations de bonne intelligence". → **standalone** (indefinite article itself), admissible at the bare slot.
- For the record: première 24/24 "la première fois que" (article-dependent); les 25/25 "toutes les fois que" (the article is the X itself); la 3/3 "à la fois que" (fixed locution).

## Per-clause pass/fail

1. C1 — PASS. Article status recorded for all four target X's (cette, plusieurs, deux, dernière) plus the {chaque, une} context, with full contexts read.
2. C2 — PASS. Standalone: {chaque 15/15, une 10/10}. Article-dependent: {dernière 4/4 "la", première 24/24 "la"}. Unattested-as-subordinator: {cette, plusieurs, deux} — all corpus hits are comparative/adverbial lookalikes.

## Verdict: PROMOTE

The audit is complete. The det-20-value follow-up #1 candidate set is sharpened as its bar requested:

- At @307's bare slot, only corpus-attested bare subordinators are admissible: **chaque** and **une** (15 and 10 attestations, 100% bare). This confirms det-20-value's c1 survivor pair on article-grounds.
- **dernière** needs a preceding article (4/4 "la dernière fois que") — it cannot fill the bare slot unless 88/02 supplies the article, which det-20-value's #1 follow-up (det-20-307-fenced) must treat as a stated cost.
- **cette, plusieurs, deux** have zero subordinator-frame attestations in the period corpus; all their "X fois que" hits are comparative or adverbial+que-clause constructions. They are not corpus-grounded candidates for @307 at all — this is a stronger finding than "article-dependent": the frame itself is unattested.

No standing or red-team verdict contradicted or downgraded. §7 intact. Canonicality caveat stands (audit is corpus-side, independent of the cipher stream).

## Follow-ups proposed (audit is complete; none required — nulls only need them)

None required: this is a completed audit, not a null. The sharpened candidate set feeds already-queued `det-20-307-fenced` (follow-up #1 of det-20-value) directly.

## Bookkeeping

- Queue: `battery-queue.json` → `fois-corpus-article-audit` status `verdict`, result `promote`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated post-write; only this entry touched; no downgrade).
- Lock created on start, deleted on completion.
