# Formulae Inventory — 1840–42 French Diplomatic Despatches
**Miner:** FORMULAE MINER (direct French-work agent, no coordinator)
**Date:** 2026-10-07
**Corpus:** `code/side-period/corpus/` — Guizot Mémoires t5–t6 (his printed 1840–42 despatches), Nesselrode *Lettres* v8 (full 1841), Levant Correspondence 1841 P3 (Jan–Feb 1841 French originals + translations). Whitespace-normalized (OCR double-spaces collapsed), NFC.

Every formula below carries source + frequency. By-ear cuts follow the lane's finer-than-standard convention (cf. "première" = pre|m|i|er).

---

## 1. Openings (salutations)

| French form | Freq | Sources |
|---|---|---|
| Monsieur le baron, | 4 | Guizot t5–t6 (all in quoted instructions) |
| Monsieur le comte, | 3 | Guizot t5–t6 (2), Nesselrode v8 (1) |
| Monsieur l'ambassadeur, | 4 | Guizot t5–t6 |
| Monsieur le ministre, | 1 | Guizot t5–t6 |
| Monsieur, (standalone vocative) | 29 | Guizot t5–t6 (24), Levant (5) |

**Grade note:** Seebach was a baron → "Monsieur le baron," is the expected R5005 salutation. By-ear: **mon|sieur|le|ba|ron** (5 units).

### Head verification (@pair 0, cipher `09 00 97 51 47 41`)
**NULL — independently confirmed.** Pair 1 is `00` = "pour" (strong lead, no conditioned exception for pre=09). "Monsieur le Baron" needs 00="sieur" → direct conflict. "Mon cher Baron" (00="cher") and bare "Monsieur," (00="sieur") die the same way. This agrees with the T1 drag's NULL. **The despatch does NOT open with a standard salutation under the standing board** — either 00≠pour at pair 1 (against a strong lead) or the opening is non-standard. Standing tension, not resolved here.

---

## 2. Early-despatch frames

| French form | Freq | Sources |
|---|---|---|
| J'ai reçu (votre dépêche / la dépêche) | 23 | Nesselrode v8 (16), Guizot t5–t6 (7) |
| En réponse à (votre dépêche) | 22 | Guizot t5–t6 (17), Nesselrode v8 (5) |
| Votre dépêche | 6 | Nesselrode v8 (4), Guizot t5–t6 (2) |
| Votre dépêche du [date] | 2 | Nesselrode v8 (2) |
| par le dernier courrier | 5 | Nesselrode v8 (5) — "dernier courrier" all Nesselrode |

By-ear: **zhay|re|çu** · **an|ray|pon|se|a** · **vo|tre|day|pe|che** · **par|le|der|nyay|koo|ryay**.

(T2/T5 drags already nulled "Votre dépêche du" and "par le dernier courrier" in 0–150 — not re-dragged.)

---

## 3. Transitions

| French form | Freq | Sources |
|---|---|---|
| J'ai l'honneur de | 7 | Guizot t5–t6 (6), Nesselrode v8 (1) |
| J'ai l'honneur de vous (informer/annoncer) | 3 | Guizot t5–t6 (3) |
| Je vous prie | 32 | Guizot t5–t6 (21), Nesselrode v8 (9), Levant (2) |
| faire connaître | 28 | Guizot t5–t6 (13), Levant (12), Nesselrode v8 (3) |
| porter à (votre/sa/la) connaissance | 6 | Guizot t5–t6 (2), Levant (3), Nesselrode v8 (1) |
| donner connaissance | 4 | Nesselrode v8 (2), Guizot t5–t6 (1), Levant (1) |
| Je m'empresse de | 2 | Levant (2) |
| Je me hâte de | 3 | Guizot t5–t6 (2), Nesselrode v8 (1) |
| veuillez | 6 | Nesselrode v8 (4), Guizot t5–t6 (1), Levant (1) |

By-ear: **zhay|lo|neur|de** · **zhe|voo|pree** · **fay|re|ko|nay|tre** · **por|tay|a|vo|tre|ko|nay|sance**.

---

## 4. Closings

| French form | Freq | Sources |
|---|---|---|
| Agréez, … | 14 | Guizot t5–t6 (6), Nesselrode v8 (5), Levant (3) |
| Je saisis, &c. (= "Je saisis cette occasion…") | 4 | Levant (4) |
| l'assurance de ma haute considération | 4+ | Guizot t5–t6, Levant |
| l'assurance de sa haute considération | 2 | Guizot t5–t6 |
| l'assurance de ma considération distinguée | 1 | Levant (Nesselrode's signed hand, late-1840 circular) |
| haute considération (any) | 8 | Guizot t5–t6 (4), Levant (4) |
| considération distinguée | 1 | Levant (1) |
| Agréez, en même tems, l'assurance de ma haute considération. | 1 | Levant (full form, French original) |
| Recevez, monsieur l'ambassadeur, l'assurance de ma haute considération. | 1 | Guizot t5–t6 |

**Grade note (from cribs-adjudicated):** "haute considération" is ambassador-grade; to a baron-envoy **"considération distinguée" outranks it**. R5005's closing is likelier the distinguée form.

By-ear: **a|gray|ay** · **la|su|rance|de|ma** · **kon|si|day|ra|syon** · **dis|tin|gay**.

### Tail search (pairs 1747–1846): HONEST NULL
No closing formula places conflict-free with ≥2 board anchors in the last 120 pairs (sliding-window search, script at `/tmp/formula_search.py`). The tail is densely unidentified; closings are mostly unidentified words (assurance, considération, agréez), so board-anchored search cannot reach them. **Not evidence against a closing — evidence of insufficient board.** LEAD-grade at best when proposed; no promotion without a battery.

---

## 5. Cipher-side formula confirmations (96 = par neighborhoods)

**"par ce que" ×3 — CONFIRMED formula, GT-anchored:**
- @224: `96=par 87=ce 46=que` (que is GT)
- @952: `96=par 87=ce 46=que`
- @1526: `96=par 87=ce 46=que`
By-ear: **par|ce|que**. Corpus: "par ce que" 1× Nesselrode v8 (rare but grammatical; the cipher's 3× is its own datum). Simultaneously validates 96="par" and 87="ce".

**"par le" ×3 — the 00="le" islet (already banked, confirmed):**
- @47, @465, @960: `96=par 00=le` (00="le" iff pre=96, conditioned islet)
Note: without the islet these read "par pour" (impossible) — the islet is load-bearing here.

**"parmi" @1196–1198** `[96,82,16]` — already a lead (F48), not re-derived.

**"par m|33" @998:** `96=par 82=m 33=? 00=pour` — "par m[33]pour"; 33 is infinitive-class → possibly "par me [INF] pour". Unresolved; flagged for the conditioner.

**Corpus par-frames NOT in cipher:** par+la (240×) and par+les (207×) have zero 96→11 instances — datum: "par la"/"par les" do not occur in R5005 (or 96≠par there).

---

## 6. Ranked crib candidates (all LEAD-grade max)

| # | Crib | Position | Alignment | Basis |
|---|---|---|---|---|
| 1 | **"par ce que"** | @224, @952, @1526 | par=96, ce=87, que=46(GT) — syllable-by-syllable exact, ×3 | GT-anchored ×3, grammatical |
| 2 | **"par le"** | @47, @465, @960 | par=96, le=00 (islet, pre=96) — ×3 | Banked islet, "par pour" impossible otherwise |
| 3 | "Monsieur le baron," | @0 (head) | **NULL** — 00="pour" blocks | Honest null; standing tension |
| 4 | "considération distinguée" (closing) | tail, unplaced | unattested in cipher | Grade-correct form, no board reach |
| 5 | "par m[33]pour" | @998 | par=96, m=82(GT), 33=INF-class | Unresolved; conditioner item |

---

## 7. Most formulaic region

**The 96=par neighborhoods.** 6 of 21 par-positions carry confirmed formulae ("par ce que" ×3, "par le" ×3), all multiply-anchored. The head (0–100) is the *least* formulaic-looking region — the expected salutation is absent under the standing board, which is itself a datum (either 00="pour" is wrong at pair 1, or the opening is non-standard). The tail is unidentified-dense; closings are currently unreachable.

## 8. Notes for the main fleet
- The "par ce que" ×3 frame is new as a *formula* (the groups were known, the frame wasn't named). It costs nothing and confirms two provisionals.
- The missing "par la"/"par les" (0/21 vs 447 corpus instances) constrains 96's distribution — worth a conditioner check.
- Head opening remains the single most anomalous unidentified region; consider a dedicated "what precedes pour at pair 1" battery.
- Tail closings need more board before they're reachable; deprioritize until then.
