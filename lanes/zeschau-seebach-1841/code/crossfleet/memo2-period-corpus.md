# CROSSFLEET MEMO 2 — period corpus cribs for the main fleet (RED-TEAM ADJUDICATED)
**From:** PERIOD-SOURCES red team · **Date:** 2026-10-07 · **Status:** final gate passed.
Full adjudication: `code/side-period/cribs-adjudicated.md`.
**Bottom line:** 117 of 121 cards survive (31 P0 unique / 54 P1 / 32 P2). 3 killed:
"mon cher comte" (Seebach was a baron — misaddress), and two envoy→minister formulae
("Daignez, je vous prie, m'indiquer…", "Votre Excellence vient de m'adresser…") whose
direction is reversed for a minister→envoy despatch. Kossuth stays off (0 hits in all 1841
sources; only 1849+ in Nesselrode v9/v10). Hong Kong/Chuenpi were never proposed and are
absent corpus-wide — the news-lag rule holds: nothing in the list needs post-18-Jan knowledge.

## 1. Corpus inventory (what the cribs are mined from)
`code/side-period/corpus/` — 24 text files, ~27.7 MB total. All pre-1923 public domain.
| file | size | content |
|---|---|---|
| revue-deux-mondes-1841-q1..q4.txt | 3.0 / 2.9 / 3.0 / 3.1 MB | RdM Parisian quarterly, all of 1841 — exact-year vocabulary ("Méhémet-Ali" 293×, "15 juillet" 156×) |
| guizot-memoires-t5-t6.txt | 2.0 MB | Guizot prints his 1840–41 despatches **verbatim** — the official-register formulae source |
| levant-correspondence-1841-p3.txt | 1.7 MB | British parliamentary paper, Jan–Feb 1841 Levant despatches (EN + French originals) |
| metternich-papiere-v6.txt / -v4.txt | 1.7 / 1.5 MB | Metternich papers; v6 has the 1840–41 French despatches ("clôture des détroits", "Pachalik d'Egypte") |
| nesselrode-v7/v8/v9/v10.txt | 524 / 616 / 504 / 560 KB | Nesselrode *Lettres et papiers*; **v8 (1840–46) is the dated anchor** — confidential minister→ambassador French, the closest surviving analogue of a Zeschau→Seebach despatch |
| pozzo-di-borgo-correspondance-v1.txt | 1008 KB | Russian-embassy French, 1814–18 — register continuity only |
| talleyrand-memoires-v1.txt | 932 KB | on disk; not yet mined for cards |
| guizot-memoires-t1/t2/t3-gutenberg.txt | 788 / 852 / 872 KB | on disk; v2 cards use t5–t6 only |
| allgemeine-zeitung-augsburg-1841-01-11..16.txt | ~124 KB each | the Saxon minister's own daily, **11–16 Jan 1841** — the exact news Zeschau had when writing (Ibrahim at Damascus 13 Dec, Porte's firman terms) |
| adb-zeschau-heinrich-anton-von.txt | 12 KB | Zeschau ADB biography (Zollverein man; Prince Johann his close friend) |
| PROVENANCE.md | 12 KB | retrieval provenance per file |

Durable mining output: `code/side-period/work/mine-nesselrode/mine.json`,
`code/side-period/work/mine-rdm/mine.json`. Miner: `code/side-period/miner.py` (idempotent).

## 2. Top cribs (adjudicated) — syllabification + by-ear variants
Cut model: the encipherer cuts **finer than natural** ("première" = pre|m|i|er) and **spells by
ear** with inconsistent cuts. Retry every failed drag with fused/split variants.
1. **Nesselrode** — nes-sel-ro-de — by-ear: Neselrode, Nesselrod. (Russian chancellor; Seebach's father-in-law.)
2. **l'Empereur** — em-pe-reur — by-ear: anpereur. (Nicholas I; "l'empereur" 754× in corpus.)
3. **le traité de Londres** — trai-té-de-Lon-dres — by-ear: le traité de Londre. Alt surface: **le traité du 15 juillet** — trai-té-du-quin-ze-juil-let ("15" spelled "quinze"; RdM house name 156×). Drag both.
4. **Mehemet-Ali** — me-he-met-A-li — by-ear: Méhémet-Ali (RdM house form, 293×), Mehmet-Ali, Mehmed-Ali, Mehemed Ali (AZ German, 8×). Drag accentless, all surfaces.
5. **le firman** — fir-man — clean. (The *word*; the investiture firman itself was issued Feb 1841 — after the despatch date.)
6. **la Porte** — por-te — clean.
7. **les détroits** — dé-troits — by-ear: destroits. Alt Straits formula: **la clôture des détroits** (Metternich) — clô-tu-re-des-dé-troits.
8. **la convention orientale** — con-ven-tion-o-rien-tale — by-ear: convension. (The coming Straits Convention; "pleins-pouvoirs pour signer la convention orientale" is Nesselrode's own phrase.)
9. **la question orientale** — ques-tion-o-rien-tale. Alt frame: **l'affaire d'Orient** — af-fai-re-d'O-rient.
10. **Guizot** — gui-zot — by-ear: Guisot. (French foreign minister since Oct 1840.)
11. **Metternich** — met-ter-nich — by-ear: Meternich, Metternik.
12. **mon cher baron** — mon-cher-ba-ron — clean. [private register]
13. **Monsieur le Baron,** — mon-sieur-le-Ba-ron — clean. [official opening]
14. **Votre dépêche du …** — vo-tre-dé-pê-che-du — by-ear: depeche, dépèche. (Standard despatch-reference opener.)
15. **par le dernier courrier** — par-le-der-nier-cour-rier — **96=par is KNOWN: sharp anchor.**
16. **l'assurance de ma considération distinguée** — [official closing; Nesselrode's signed hand, Levant circular late 1840 — highest authority in corpus]. Grade note: drag "considération distinguée" BEFORE "haute considération" (the latter is ambassador-grade; Seebach is a baron-envoy).
17. **Constantinople** — cons-tan-ti-no-ple — alt cut con-stan-ti-no-ple.

Anti-collision (red-team enforced): **never drag "premier"/"première"** — pre|m|i|er is read at
both "la première" windows. The background adjective "premier" is struck from the vocab list.

## 3. Suggested drag targets (positions are raw 0-based pair offsets in `data/upstream-ct_R5005.digits.txt`;
the miner's "754/1034" labels for the "la première" windows = raw **766** and **1054** — verified)
- **T1 · Opening @ pair 0.** Raw open: `09 00 97 51 47 41 …`. Drag "Monsieur le Baron," (mon|sieur|le|ba|ron, 5u) vs "Mon cher Baron," (mon|cher|ba|ron, 4u) at offset 0. Why: every despatch opens with the address; these are the only two plausible shapes for a baron.
- **T2 · Early window, pairs 0–150.** Drag "Votre dépêche du …" (6u) and "J'ai reçu votre dépêche du …". Why: the despatch-reference opener sits in §1; "votre dépêche du 17 octobre / du 5 août" shapes are attested in v8.
- **T3 · The "la première" windows @766 and @1054.** Both read `11 70 82 34 29` (la|pre|m|i|er) and — critically — **both are followed by 40=e**. That shared successor kills "fois", "nouvelle", "lettre", and "époque+que" (46=que does not follow at either window). The noun is é-initial: drag **entrevue** (by-ear e|n|tre|vue), **expédition** (by-ear e|x|pé|di|tion — chancellery vocabulary), **épreuve**. Preceding context: @766 `… qui(64) 02 97 e(40) 67 la première`; @1054 `… par(96) 43 ce(87) 01 03 er(29) 80 le(77) la première`. Why: two anchored windows with a shared-successor constraint — the cheapest disambiguation on the board.
- **T4 · The long repeats — "le gouver(n)ment" hypothesis.** `77 78 94 82 06` @**884** and @**1204**; `06 77 78 18 71 10 01` @**1429**. With 77=le and 82=m known, R1 parses as le|?|?|m|? — the by-ear spelling **"le gouverment"** (dropped e, exactly the encipherer's profile) gives **78=gou, 94=ver, 06=ent**. Cross-check: R2 then opens `06|77|78` = "…ent le gou…" — consistent (tail of a preceding -ment word, then "le gou…"). Alternatives with the same 82/06 skeleton: "le renversement", "le consentement". Why it matters: **06 is the top-frequency unassigned group (39×)** — confirming 06=ent unlocks every -ment/-ent ending in the despatch. Context: R1a is followed by 77=le ("…le gouverment. Le…" — likely sentence break); R1b is followed by `06 59 42 06 84 59 47 46=que` ("…que"); R2 is preceded by `96=par … 64=qui 77=le 84 84`.
- **T5 · "par le dernier courrier" at every 96.** 96=par occurs at pairs **47, 132, 152, 228, 234, 372, 473, 494, 617, 701, 899, 930, 1046, 1221, 1238, 1285, 1419, 1558, 1700, 1717, 1870**. Drag 96|77|der|nier|cour|rier (expect 77=le second). Why: known-pair anchor + a 6-unit collocation attested in the firman context ("Par le dernier courrier que j'ai…").
- **T6 · Tail closings, last ~40 pairs.** Raw tail: `… 28 00 46=que 11=la 59 35 04 20 62 93 70=pre 10 20 91 90 09 70=pre 08 62 98 23 88 32 48 21 65 93 66 96=par 42 24 24 48 32 16 77=le 84 97 49 34`. Drag "Adieu, mon cher baron" (6u), "Tout à vous" (3u), and "l'assurance de ma considération distinguée" (halves) at the tail. Why: closings are positional; the official-vs-private register split tells you which despatch type this is.
- **T7 · Name drags, mid-despatch.** Nesselrode (4u), Guizot (2u), Metternich (3u), l'Empereur (3u), Mehemet-Ali (5u, all spelling surfaces). Why: Levant-substance paragraphs; 2–3u names are cheap tests.
- **T8 · Treaty double-surface.** Drag "le traité de Londres" (5u) AND "le traité du 15 juillet" (7u) in mid-despatch. Why: RdM's house name vs the chancellery name — the encipherer's surface is unknown.

## 4. Freshest dated fact in the corpus (for prioritisation)
AZ 11-Jan-1841: *"Ibrahim Pascha befand sich am 13 Dec. noch zu Damaskus"* — 5-week-old news,
in the Saxon minister's own paper, 7 days before R5005. If the despatch carries fresh news, it is
Damascus/Syria-evacuation news: prioritise **Damas** (da-mas), **Ibrahim** (i-bra-him / Ibraim),
**Gaza** (ga-za), **Jaffa** (jaf-fa), **l'évacuation (de la Syrie)**.
