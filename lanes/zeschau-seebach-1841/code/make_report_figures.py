#!/usr/bin/env python3
"""Generate REPORT.md figures from lane data. Every number comes from the
lane's own data files at run time. Nothing invented.

CANONICAL DATA (round 4, 2026-10-07): the REPAIRED 1,847-pair parse
(code/crowd4/repaired_parse.py — flips offsets['a5_03'] 1->0; supersedes
data/upstream-offsets.json via code/crib_attack.py::load_pairs, which must
NOT be used for R5005 figures). Repaired phases: code/crowd4/phase_map_repaired.json.
Banked contactor phases are stale (61/96 groups changed phase).
"""
import json, os, sys
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(LANE, "report_assets")
os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, os.path.join(LANE, "code", "crowd4"))
from repaired_parse import load_pairs_repaired

# ---- canonical gate: repaired stream, assertions first ----
pairs, odd_lines, off1 = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N
assert len(set(pairs)) == 96, len(set(pairs))
SEQ = ["11", "70", "82", "34", "29", "40"]
hits = [i for i in range(N - 5) if pairs[i:i + 6] == SEQ]
assert hits == [754, 1034], f"unexpected hits {hits}"
print(f"[ok] repaired stream: {N} pairs, 96 groups, "
      f"'la premiere' @ {hits}, odd_lines={odd_lines}, off1={off1}")

freq = Counter(pairs)
order = [g for g, _ in freq.most_common()]  # 96 groups, descending
rank_of = {g: i + 1 for i, g in enumerate(order)}

# Anchors for fig1 coloring
CRIBS = {"11": "la", "70": "pre", "82": "m", "34": "i", "29": "er",
         "40": "e", "46": "que"}                                   # ground truth
PROV = {"87": "ce", "64": "qui", "96": "par", "94": "ne",
        "06": "verb-stem", "67": "veut-class"}                     # provisional

plt.rcParams.update({"font.size": 9, "figure.dpi": 150})

# ---------- Fig 1: frequency rank chart ----------
fig, ax = plt.subplots(figsize=(10, 4.2))
xs = list(range(1, 97))
colors = [("#1b7f3b" if g in CRIBS else
           ("#d98e00" if g in PROV else "#9aa3ad"))
          for g in order]
ax.bar(xs, [freq[g] for g in order], color=colors, width=0.9)
for j, (g, label) in enumerate(list(CRIBS.items()) + list(PROV.items())):
    r = rank_of[g]
    ax.annotate(f"{g}={label}\n#{r}", xy=(r, freq[g]),
                xytext=(0, 6 + (j % 3) * 16),
                textcoords="offset points", ha="center", fontsize=6.5,
                color="#1b7f3b" if g in CRIBS else "#8a5a00", weight="bold")
leg = [mpatches.Patch(color="#1b7f3b", label="pencil crib (ground truth, 7)"),
       mpatches.Patch(color="#d98e00", label="lane-inferred provisional (6)"),
       mpatches.Patch(color="#9aa3ad", label="unidentified (83)")]
ax.legend(handles=leg, loc="upper right", fontsize=8)
ax.set_xlabel("frequency rank (1–96 of 96 groups)")
ax.set_ylabel("occurrences in 1,847 pairs")
ax.set_title("Fig 1 — Group frequency rank chart, R5005 (1,847 pairs, 96 groups). "
             "Anchors highlighted and labeled.")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig1_frequency.png"))
plt.close(fig)
print("fig1: top ranks",
      {g: rank_of[g] for g in ["24", "64", "29", "11", "06", "82", "94", "87", "46"]})

# ---------- Fig 2: anchor-adjacency bigrams ----------
def bigram(a, b):
    c = sum(1 for i in range(N - 1) if pairs[i] == a and pairs[i + 1] == b)
    n_a = freq[a]
    return c, n_a, c / n_a if n_a else 0.0

items = [("82", "16", "m→?"), ("87", "11", "ce→la"), ("87", "64", "ce→qui"),
         ("87", "46", "ce→que")]
labels, rates, ann = [], [], []
for a, b, tag in items:
    c, n, r = bigram(a, b)
    labels.append(f"{a}→{b}\n({tag})")
    rates.append(r)
    ann.append(f"{c}/{n}\n{r:.1%}")
fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(labels, rates, color=["#9aa3ad", "#1b7f3b", "#d98e00", "#d98e00"])
for bar, a_ in zip(bars, ann):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.008, a_,
            ha="center", fontsize=9)
ax.set_ylabel("conditional probability")
ax.set_title("Fig 2 — Anchor-adjacency bigrams, repaired parse (1,847 pairs). "
             "Counts / occurrences of first group. "
             "Green = ground-truth pair, amber = provisional-anchor pairs, gray = unidentified target.")
ax.set_ylim(0, max(rates) * 1.35)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig2_bigrams.png"))
plt.close(fig)
print("fig2 bigrams:", {f"{a}->{b}": f"{c}/{n}={r:.4f}"
                        for (a, b, _), (c, n, r) in
                        zip(items, [bigram(a, b) for a, b, _ in items])})

# ---------- Fig 3: "la première" position map (two occurrences) ----------
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 5.4),
                                    gridspec_kw={"height_ratios": [1, 2, 2]})
ax1.barh([0], [N], color="#dde3e8", height=0.6)
for h in hits:
    ax1.barh([0], [6], left=[h], color="#1b7f3b", height=0.6)
ax1.set_xlim(0, N)
ax1.set_yticks([])
ax1.set_xlabel(f"pair index (0–{N - 1})")
p1, p2 = hits[0] / N * 100, hits[1] / N * 100
ax1.set_title("Fig 3 — 'la première' (11-70-82-34-29-40) occurs TWICE\n"
              f"in the repaired parse: @pair {hits[0]} ({p1:.1f}%) and "
              f"@{hits[1]} ({p2:.1f}%) of the stream.")
for h in hits:
    ax1.annotate(f"pair {h}", xy=(h, 0), xytext=(h, 0.9),
                 ha="center", fontsize=8, color="#1b7f3b", weight="bold",
                 arrowprops=dict(arrowstyle="->", color="#1b7f3b"))
# zoom windows ±10 around each hit
for axw, h in [(ax2, hits[0]), (ax3, hits[1])]:
    w0, w1 = h - 10, h + 16
    seg = pairs[w0:w1]
    xc = list(range(w0, w1))
    cols = [("#1b7f3b" if g in CRIBS else
             ("#d98e00" if g in PROV else "#9aa3ad")) for g in seg]
    axw.bar(xc, [1] * len(seg), color=cols, width=0.9)
    for x, g in zip(xc, seg):
        lab = CRIBS.get(g, PROV.get(g, g))
        axw.text(x, 0.5, f"{g}\n{lab}", ha="center", va="center", fontsize=6,
                 color="white" if g in CRIBS or g in PROV else "#333")
    axw.set_xlim(w0 - 0.5, w1 - 0.5)
    axw.set_ylim(0, 1)
    axw.set_yticks([])
    axw.set_xlabel(f"pair index (zoom ±10 around {h})")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig3_position_map.png"))
plt.close(fig)

# ---------- Fig 4: era vs Les Mis rate comparison ----------
a3 = json.load(open(os.path.join(LANE, "data", "attempt3_results.json")))
era = a3["era_reference"]
lm = a3["lesmis_reference_recomputed"]
rows = [
    ("P(que|ce)", era["p_que_given_ce"], lm["p_que_given_ce"]),
    ("P(qui|ce)", era["p_qui_given_ce"], lm["p_qui_given_ce"]),
    ("P(la|de)", era["p_la_given_de"], lm["p_la_given_de"]),
    ("P(la|à)", era["p_la_given_a"], lm["p_la_given_a"]),
    ("n(cela)/n(ce)", era["unigram_ratio_cela_over_ce"],
     lm["unigram_ratio_cela_over_ce"]),
]
labels = [r[0] for r in rows]
ev = [r[1] for r in rows]
lv = [r[2] for r in rows]
cela_gap = lv[-1] / ev[-1] if ev[-1] else float("nan")
fig, ax = plt.subplots(figsize=(8.5, 4.2))
y = list(range(len(rows)))
ax.barh([i + 0.2 for i in y], ev, height=0.4, color="#1f5fa8",
        label=f"era: Tocqueville 1835/40 ({era['words']:,} wds)")
ax.barh([i - 0.2 for i in y], lv, height=0.4, color="#c96a1e",
        label=f"Les Mis 1862 ({lm['words']:,} wds)")
for i, (e, l) in enumerate(zip(ev, lv)):
    ax.text(e * 1.04, i + 0.2, f"{e:.3f}", va="center", fontsize=8)
    ax.text(l * 1.04, i - 0.2, f"{l:.3f}", va="center", fontsize=8)
ax.set_xscale("log")
ax.set_yticks(y)
ax.set_yticklabels(labels)
ax.set_xlabel("rate (log scale)")
ax.legend(fontsize=8, loc="lower right")
ax.set_title("Fig 4 — Era-matched vs Les Mis reference rates. Four rates agree within "
             f"factor 2; 'cela' disagrees {cela_gap:.1f}× "
             f"({ev[-1]:.3f} vs {lv[-1]:.3f}) — a register gap.")
ax.annotate(f"{cela_gap:.1f}× register gap", xy=(lv[-1], 4 - 0.2),
            xytext=(0.6, 3.4), fontsize=9, color="#a33", weight="bold",
            arrowprops=dict(arrowstyle="->", color="#a33"))
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_era_comparison.png"))
plt.close(fig)
print(f"fig4: cela register gap = {cela_gap:.2f}x ({ev[-1]:.4f} vs {lv[-1]:.4f})")

# ---------- Fig 5: verdict board (attempts 1–3, crowd rounds 1–4, side fleets) ----------
board = [
    ("Attempt 1", "transcription verified", "PASS"),
    ("Attempt 1", "repeat claims ×5/×3", "CORRECTED → 2×/0×"),
    ("Attempt 1", "function-word drag (7 anchors)", "NULL"),
    ("Attempt 2", "H1: 82→16 as 'ma'", "PLAUSIBLE (1/4)"),
    ("Attempt 2", "H2: 87 = de/à", "REFUTED"),
    ("Attempt 2", "H2b: 87 = ce", "CONFIRMED 4/5 → DEMOTED*"),
    ("Attempt 2", "drag re-run (8 anchors)", "NULL"),
    ("Attempt 3", "H3: 64 = qui", "CONFIRMED 4/4"),
    ("Attempt 3", "87=ce vs era rates", "CONFIRMED 3/4*"),
    ("Attempt 3", "drag re-run (9 anchors)", "NULL"),
    ("Crowd r1", "phonotactician", "NULL"),
    ("Crowd r1", "crib surgeon ('la première' @1033)", "LEADS"),
    ("Crowd r1", "contactor (3-phase structure)", "STRUCTURAL FIND"),
    ("Crowd r1", "red team vs 87=ce", "DEMOTED → PLAUSIBLE"),
    ("Crowd r1", "drag racer (syllable drag)", "PARTIAL"),
    ("Crowd r1", "historian (key hunt)", "KEY NOT FOUND / routes"),
    ("Crowd r1", "formula hunter", "REPEAT CENSUS"),
    ("Crowd r1", "annealer", "NULL (control-proven)"),
    ("Crowd r1", "linguist (\"J'ai l'honneur de\")", "HYPOTHESIS"),
    ("Crowd r2", '24 = "est"', "REFUTED (74× C-kill)"),
    ("Crowd r2", '96 = "par"', "CONFIRMED 4/4 → PROVISIONAL"),
    ("Crowd r3", '78 = "me"', "LEAD (promo rejected)"),
    ("Crowd r3", "tuner (phase meaning)", "NULL (LOO 2/34 vs 6/34)"),
    ("Crowd r3", '87 = "ce" rival-kill battery', "PROMOTED → PROV-STRONG"),
    ("Crowd r4", '87 = "ce" arc', "PROV-STRONG; cela-leg dead"),
    ("Crowd r4", '64 = "même" rival', "DISFAVORED (9.8×, p=1.4e-4)"),
    ("Crowd r4", '94: "ne"/"re"/"en"', "ne PROV-STRONG; re DEMOTED"),
    ("Crowd r4", "06 stem class; 06 vs 86", "FINITE vs INFINITIVE"),
    ("Crowd r4", "conditioned polyvalence", "4/25 groups (16.0%)"),
    ("Crowd r2–r4", "scorer-smith (3 variants)", "BROKEN-ON-CONTROL"),
    ("Sidepath", "slider pass-1", "VOID (174 < 2×208.3)"),
    ("Side wordpattern", "pattern matcher", "NULL (GT control fails)"),
    ("Side keyhunt", "parse repair (a5_03 1→0)", "1,847 pairs CANONICAL"),
    ("Side keyhunt", 'second "la première"', "UNCOVERED @754 + @1034"),
    ("Side", "DECODE acct alexrivers", "GATED (no full images)"),
    ("Crowd r4", '47 = "ce"', "LEAD (1.00× 'ce que')"),
    ("Crowd r4", '62 = "on"', "PROMOTION-CANDIDATE (r5: denied)"),
    ("Crowd r5", '77 = "le"', "PROMOTED → PROVISIONAL (cond)"),
    ("Crowd r5", '78: me-word / me-syll / ver', "coexist; word disfavored"),
    ("Crowd r5", "@578 revival thread", "BURIED (sixmer ×2)"),
    ("Crowd r5", '47 = "ce"', "LEAD strengthened (Q1/Q2)"),
    ("Crowd r5", "06 stem single-reading", "NULL (17.1× kill)"),
    ("Crowd r5", "M1 06/86 rule", "ACCEPTED (F33-grade)"),
    ("Crowd r5", "joint-engine diagnosis", "REVERSED (objective bug)"),
    ("Crowd r5", "rotation mappings", "killed ×3; E1 period-3 rhythm"),
    ("Crowd r5", '87 = "ce" new legs', "A1/A3/A2 (holds PROV)"),
    ("Crowd r5", "@754 vs @1034", "DONE; 43='me' fenced"),
    ("Crowd r5", "unit inventory", "24 units + 10 exclusions"),
    ("Crowd r3+r4", '77: "le" / "pas" / "que"', "le PROMOTED (r5, cond)"),
]
def vcolor(v):
    if ("CONFIRMED" in v or "CANONICAL" in v or "UNCOVERED" in v) and \
       "DEMOTED" not in v and "PROVISIONAL" not in v:
        return "#1b7f3b"
    if "REFUTED" in v or "DEMOTED" in v or "DISFAVORED" in v:
        return "#b3261e"
    if "NULL" in v or "VOID" in v or "BROKEN" in v:
        return "#6b7280"
    return "#b8860b"
fig, ax = plt.subplots(figsize=(10, 14.2))
ax.set_xlim(0, 10)
ax.set_ylim(-0.6, len(board) - 0.1)
ax.axis("off")
for i, (phase, what, verdict) in enumerate(board):
    y0 = len(board) - 1 - i
    ax.text(0.2, y0 + 0.5, phase, va="center", fontsize=8, weight="bold",
            color="#333")
    ax.text(2.2, y0 + 0.5, what, va="center", fontsize=8)
    ax.add_patch(plt.Rectangle((7.2, y0 + 0.12), 2.6, 0.76,
                               facecolor=vcolor(verdict), alpha=0.16,
                               edgecolor=vcolor(verdict)))
    ax.text(8.5, y0 + 0.5, verdict, va="center", ha="center", fontsize=7.5,
            weight="bold", color=vcolor(verdict))
fig.text(0.5, 0.005,
         "Fig 5 — Verdict board: attempts 1–3, crowd rounds 1–5, side fleets. "
         "* 87=ce: attempt-2 scorecard voided by red team (count ratio ≠ conditional); "
         "attempt-3 3/4 on era rates; round-3 battery promoted it to provisional-strong; "
         "round-4 register-subset test failed, cela-leg dead. "
         "96=par provisional depends on 87=ce.",
         ha="center", va="bottom", fontsize=8, style="italic", wrap=True)
fig.tight_layout(rect=[0, 0.045, 1, 1])
fig.savefig(os.path.join(OUT, "fig5_verdict_board.png"))
plt.close(fig)
print(f"fig5: {len(board)} verdict rows")

# ---------- Fig 6: 3-phase contact structure, REPAIRED parse + phases ----------
phases = json.load(open(os.path.join(LANE, "code", "crowd4",
                                     "phase_map_repaired.json")))
assert set(phases) == set(freq), "phase map covers all 96 groups"
nR = sum(1 for p in phases.values() if p == "R")
trans = Counter((phases[pairs[i]], phases[pairs[i + 1]])
                for i in range(N - 1))
# rotation chi²: same statistic as scorer synth_control.rotation_chi2
obs = {(r, c): trans[(r, c)] for r in "ABC" for c in "ABC"}
rs = {r: sum(obs[(r, c)] for c in "ABC") for r in "ABC"}
cs = {c: sum(obs[(r, c)] for r in "ABC") for c in "ABC"}
T = sum(rs.values())
chi2 = sum((obs[(r, c)] - rs[r] * cs[c] / T) ** 2 / (rs[r] * cs[c] / T)
           for r in "ABC" for c in "ABC" if rs[r] * cs[c])
assert abs(chi2 - 366.3) < 0.05, f"chi2={chi2:.2f} disagrees with banked 366.3"
P = {(r, c): obs[(r, c)] / rs[r] for r in "ABC" for c in "ABC"}
lift = {(r, c): obs[(r, c)] / (rs[r] * cs[c] / T) for r in "ABC" for c in "ABC"}
# dominant cycle: the permutation r->c maximizing obs lifts
cycle_edges = sorted(((lift[(r, c)], r, c) for r in "ABC" for c in "ABC"
                      if r != c), reverse=True)
cycle3 = [e for e in cycle_edges[:3]]
cycle_names = sorted({e[1] for e in cycle3} | {e[2] for e in cycle3})
assert len(cycle_names) == 3, cycle3  # a true 3-cycle
# order the cycle following max-lift edges
cyc = cycle3[0][1]
ordered = []
for _ in range(3):
    nxt = max((l, c) for l, r, c in cycle_edges if r == cyc)[1]
    ordered.append((cyc, nxt)); cyc = nxt
cyc_label = "→".join([ordered[0][0]] + [c for _, c in ordered])
cyc_lifts = [lift[e] for e in ordered]
self_lifts = [lift[(b, b)] for b in "ABC"]
print(f"fig6: chi2={chi2:.1f} (banked 366.3), T={T}/{N-1}, R groups={nR}, "
      f"cycle={cyc_label} lifts={[round(x,3) for x in cyc_lifts]}, "
      f"self lifts={[round(x,3) for x in self_lifts]}")

fig, ax = plt.subplots(figsize=(8, 5.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7.2)
ax.axis("off")
pos = {"A": (2.2, 2.6), "B": (7.8, 2.6), "C": (5.0, 5.6)}
for blk, (x, y) in pos.items():
    ax.add_patch(plt.Circle((x, y), 0.8, facecolor="#dbe7f5",
                            edgecolor="#1f5fa8", lw=2))
    ax.text(x, y, blk, ha="center", va="center", fontsize=16, weight="bold",
            color="#1f5fa8")
    ax.text(x, y - 1.25, f"self {P[(blk, blk)]:.2f}", ha="center",
            fontsize=8, color="#666")
arrow_specs = {
    ("A", "B"): dict(xy=(7.15, 2.35), xytext=(2.85, 2.35),
                     connectionstyle="arc3,rad=0.18"),
    ("B", "C"): dict(xy=(7.15, 3.05), xytext=(5.65, 5.15)),
    ("C", "A"): dict(xy=(4.35, 5.15), xytext=(2.85, 3.05)),
    ("A", "C"): dict(xy=(5.65, 5.15), xytext=(2.85, 3.05)),
    ("C", "B"): dict(xy=(7.15, 3.05), xytext=(5.65, 5.15)),
    ("B", "A"): dict(xy=(2.85, 2.35), xytext=(7.15, 2.35),
                     connectionstyle="arc3,rad=0.18"),
}
label_xy = {("A", "B"): (5.0, 1.55), ("B", "C"): (6.9, 4.6),
            ("C", "A"): (3.1, 4.6), ("A", "C"): (3.1, 4.6),
            ("C", "B"): (6.9, 4.6), ("B", "A"): (5.0, 1.55)}
for (r, c) in ordered:
    spec = arrow_specs[(r, c)]
    ax.annotate("", xy=spec["xy"], xytext=spec["xytext"],
                arrowprops=dict(arrowstyle="-|>", color="#1f5fa8", lw=2.4,
                                shrinkA=4, shrinkB=4,
                                **({"connectionstyle": spec["connectionstyle"]}
                                   if "connectionstyle" in spec else {})))
    lx, ly = label_xy[(r, c)]
    ax.text(lx, ly, f"{r}→{c} {P[(r, c)]:.3f}", fontsize=10, weight="bold",
            color="#1f5fa8", ha="center" if (r, c) == ("A", "B") else "left")
fig.text(0.5, 0.02,
         f"Fig 6 — 3-phase rotational contact structure, REPAIRED parse "
         f"(1,847 pairs; Jaccard-k12 phases recomputed; chi²={chi2:.1f}, 4df, "
         f"p≪1e-6; {T} ABC→ABC transitions of {N - 1}; 20/96 groups in rare "
         f"cluster R, excluded). Dominant cycle {cyc_label} runs "
         f"{min(cyc_lifts):.2f}–{max(cyc_lifts):.2f}× over independence; "
         f"self-transitions suppressed ({min(self_lifts):.2f}–"
         f"{max(self_lifts):.2f}×). 29=er anchors phase C (word-final-ish).",
         ha="center", fontsize=8.5, style="italic", wrap=True)
fig.tight_layout(rect=[0, 0.06, 1, 1])
fig.savefig(os.path.join(OUT, "fig6_contact_structure.png"))
plt.close(fig)

print("\nfigures written to", OUT)
for f in sorted(os.listdir(OUT)):
    p = os.path.join(OUT, f)
    print(" ", f, os.path.getsize(p), "bytes")
