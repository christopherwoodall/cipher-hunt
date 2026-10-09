# Battery `subj-62-1329-agree` — verdict: NULL

Target: `subj-62-1329-agree` (battery-queue.json, priority 3, status queued).
Follow-up proposed by `battery-syll-52-locus-1334.md` (verdict null, 2026-10-09).
Worker: 67ed023f-398d-4a1b-90d4-9d0566146417.

## Bar (verbatim, pre-registered)

"Bar: name 62 at @1329 (the \"ne pre[52]a\" subject slot). Bar: if 62 names plural, all three 3sg candidates die by agreement (fence, not kill, pending 62's own standing); if 62='il' (battery-promoted) holds, the 3sg agreement leg is banked for the surviving subset."

Numbered clauses:

- **C1.** Name 62's value at @1329 with battery-grade evidence.
- **C2.** If 62 names plural at @1329, fence (not kill) the three 3sg candidates {prescrira, préserva, prévoira} by agreement, pending 62's own standing.
- **C3 (dead arm, per supervisor brief — NOT tested).** "If 62='il' holds, bank the 3sg agreement leg." 62='il' was KILLED at kill grade (R19-106), confirmed R20-125; the kill is permanent. The conditional's antecedent is false forever; this arm is dead, not merely unfired.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/subj-62-1329-agree.lock` on start (agent 67ed023f-398d-4a1b-90d4-9d0566146417, 2026-10-09T20:40:00Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` parsed per `repair_parse.py`: 1,847 pairs, 96 types. `canonical.py` never used.
3. Byte-confirmed the locus (0-based): @1328=06, @1329=62, @1330=94, @1331=70, @1332=52, @1333=39, @1334=83, @1335=86 (rows a7_04/a7_05).
4. Adopted (not re-litigated): 94='ne' STRONG LEAD (R17-001); 70='pre' pencil GT; 39=/a/ (a-39 PROMOTE); 83='de' lead; 86 INF class; `syll-52-locus-1334` NULL (three-way tie {prescrira, préserva, prévoira}, all 3sg finite, tie unbreakable stream-wide); `unif-52a-1334-orphan` PROMOTE (uniformity extension of 52="a" to @1332 fenced; locus keeps the syllable reading); `class-62-fullcensus` NULL (no single class parses all 35 windows of 62; 'il' dead at kill grade globally; conditioned split is §7 red-team venue); R19-106/R20-125 ('il' kill stands permanent).

## Findings

### C1 — name 62's value at @1329: FAIL

The window: `…[06] [62] ne pre [52] a de [86-INF] …` — 62 sits in the subject slot of a "ne [finite-verb]" clause whose verb is the parent's 3sg trio.

No value is selectable at battery grade:

- The subject slot admits noun, pronoun, and proper-noun values **identically**: no determiner, no agreement controller beyond 3sg (all three verb candidates are 3sg), no object, no complement, no selectional restriction anywhere in the window distinguishes one subject value from another.
- 'il' — the former demonstrated rival — is **dead at kill grade globally** (R19-106, R20-125) and cannot be named.
- Remaining pronoun candidates {elle, on, ils, elles, nous, vous, ce} parse the frame identically; naming any one would be arbitrary (precedent: val-03-value-census, parsing ≠ naming).
- Noun/proper-noun values: zero positive legs at this locus (no determiner; the bare-proper-noun fork from bare-subj-corpus needs a NAMED value, which is exactly what is missing).
- Number is value-dependent: 62's number cannot be named without a value.

### C2 — plural-fence arm: MOOT (fires nothing)

C2's antecedent ("62 names plural") cannot be established — see C1. Neither the plural-fence nor the 3sg-bank fires. The three 3sg candidates stand exactly as the parent left them.

### C3 — dead arm: RECORDED

Per the supervisor brief, the "if 62='il' holds" conditional is not tested; its antecedent is permanently false. No agreement leg is banked.

### Adverses honored

- The 'il' kill: honored, not re-litigated; its blast radius is why C1 cannot fall back on the former rival.
- `class-62-fullcensus` NULL: untouched; no uniform class declared; the §7 conditioned-split question stays with the red team.
- `syll-52-locus-1334` NULL and the three-way tie: adopted; this battery adds no naming pressure to 52.

## Verdict: NULL

C1 fails (no value selectable), C2 moot, C3 dead. The @1329 subject slot names nothing at battery grade; the agreement question for {prescrira, préserva, prévoira} stays open in both directions.

## Scope

- Locus-level only (@1328–1335). 62's global value/class stay open (registry cell absent); the 62-94 family residuals (@1362/@1686 twins) untouched; §7 intact.
- No standing or red-team verdict contradicted, downgraded, or re-litigated.
- Canonical-stream caveat stands (a7_04/a7_05 boundary offsets unvalidated).

## Follow-ups (for supervisor queuing; all verified ABSENT from the queue)

1. `subj-62-1329-reseg` (P4) — test whether @1329=62 is word-medial rather than the subject slot: "06 62" composition with @1328=06='ent' (62-06 ×5 @665/@1536/@1539; class-62-fullcensus fenced these as segmentation, not grammar). If 62 composes leftward, the subject slot dissolves and the agreement bar is moot. Bar: licensed "…ent[62]…" composition with stated values, or fence.
2. `agree-62-1324-twin` (P4) — test the twin @1324=62 ("[62] vient [56] pas"): if the two 62s share one value, the 3sg "vient" constrains @1324's 62 to 3sg and @1329 inherits it → banks the 3sg agreement leg for the trio. Bar: twin-value constraint demonstrated with stated values, or fence.
3. Note: `ne-1330-bare-corpus` (the parent's follow-up 2) is **already queued** — not duplicated here.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-subj-62-1329-agree.md`
- Queue: `subj-62-1329-agree` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.subj-62-1329-agree.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/subj-62-1329-agree.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
