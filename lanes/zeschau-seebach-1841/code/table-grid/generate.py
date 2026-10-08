#!/usr/bin/env python3
"""Regenerate the R5005 key-table grid: HTML fragment + PNG, from the live lane state.

Reads:
  code/table-grid/table-registry.json   (cell -> [value, status])
  data/upstream-ct_R5005.txt + code/side-keyhunt/repaired_offsets.json (frequencies)

Writes (only if content changed):
  code/table-grid/table-grid.html
  code/table-grid/table-grid.png

Usage: python3 generate.py [--check]   # --check exits 0/1 on changed/unchanged
"""
import hashlib
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))
OUT_HTML = os.path.join(HERE, "table-grid.html")
OUT_PNG = os.path.join(HERE, "table-grid.png")

STATUS_COLORS = {
    "gt":   "#2e9e5b",
    "prom": "#3b82f6",
    "prov": "#d97706",
    "cls":  "#8b5cf6",
    "lead": "#888888",
}
STATUS_LABELS = {
    "gt": "pencil ground truth",
    "prom": "promoted",
    "prov": "provisional",
    "cls": "class",
    "lead": "lead (pending)",
}
UNOBSERVED = {"05", "25", "72", "75"}  # of 00-99 never seen; recomputed below anyway


def load_frequencies():
    rows = []
    with open(os.path.join(LANE, "data", "upstream-ct_R5005.txt")) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lid, digits = line.split()
            rows.append((lid, re.sub(r"\D", "", digits)))
    off = json.load(open(os.path.join(LANE, "code", "side-keyhunt",
                                      "repaired_offsets.json")))
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [digits[i:i + 2] for i in range(o, len(digits) - 1, 2)]
    assert len(pairs) == 1847, len(pairs)
    return Counter(pairs)


def build_html(freq, registry):
    maxn = max(freq.values())
    cells = registry["cells"]

    def cls(g):
        if g not in freq:
            return "miss"
        return cells.get(g, [None, None])[1] or "unk"

    def val(g):
        return cells.get(g, [None, None])[0] or ""

    css = """<style>
.cg-wrap{box-sizing:border-box;max-width:100%;font-family:system-ui,sans-serif;padding:8px}
.cg-grid{display:grid;grid-template-columns:repeat(10,1fr);gap:3px;max-width:560px;margin:0 auto}
.cg-cell{aspect-ratio:1/1;border-radius:6px;border:1px solid var(--hatch-widget-border);
 background:var(--hatch-widget-surface-muted);position:relative;display:flex;flex-direction:column;
 align-items:center;justify-content:center;overflow:hidden;min-width:0}
.cg-num{font-size:9px;color:var(--hatch-widget-muted);line-height:1}
.cg-val{font-size:12px;font-weight:700;color:var(--hatch-widget-text);line-height:1.2;white-space:nowrap}
.cg-freq{font-size:8px;color:var(--hatch-widget-muted);line-height:1}
.cg-bar{position:absolute;bottom:0;left:0;height:3px;background:var(--hatch-widget-accent);opacity:.55}
.cg-cell.gt{border-color:#2e9e5b;border-width:2px}.cg-cell.gt .cg-val{color:#34a05e}
.cg-cell.prom{border-color:#3b82f6;border-width:2px}.cg-cell.prom .cg-val{color:#3f8cff}
.cg-cell.prov{border-color:#d97706;border-width:2px}.cg-cell.prov .cg-val{color:#d98a06}
.cg-cell.cls{border-color:#8b5cf6;border-width:2px}.cg-cell.cls .cg-val{color:#8f6ff2;font-size:9px}
.cg-cell.lead{border-style:dashed;border-color:var(--hatch-widget-muted);border-width:2px}
.cg-cell.lead .cg-val{color:var(--hatch-widget-muted);font-size:10px}
.cg-cell.miss{background:repeating-linear-gradient(45deg,transparent,transparent 4px,rgba(128,128,128,.18) 4px,rgba(128,128,128,.18) 8px)}
.cg-legend{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:10px;font-size:11px;color:var(--hatch-widget-muted)}
.cg-key{display:inline-flex;align-items:center;gap:4px}
.cg-dot{width:10px;height:10px;border-radius:3px;border:2px solid;display:inline-block}
html[data-theme="dark"] .cg-cell.gt .cg-val{color:#4ade80}
html[data-theme="dark"] .cg-cell.prom .cg-val{color:#60a5fa}
html[data-theme="dark"] .cg-cell.prov .cg-val{color:#fbbf24}
html[data-theme="dark"] .cg-cell.cls .cg-val{color:#a78bfa}
</style>"""
    parts = ['<div class="cg-wrap">', css, '<div class="cg-grid">']
    for r in range(10):
        for c_ in range(10):
            g = f"{r}{c_}"
            n = freq.get(g, 0)
            w = (n / maxn * 100) if n else 0
            v, k = val(g), cls(g)
            inner = f'<span class="cg-num">{g}</span>'
            if v:
                inner += f"<span class='cg-val'>{v}</span>".replace("'", '"')
            inner += f"<span class=\"cg-freq\">{n if n else '&#8212;'}</span>"
            if n:
                inner += f"<span class=\"cg-bar\" style=\"width:{w:.0f}%\"></span>"
            parts.append(
                f"<div class=\"cg-cell {k}\" title=\"group {g} — {n} occurrences\">{inner}</div>")
    parts.append("</div>")
    from collections import Counter as _C
    _counts = _C(v[1] for v in cells.values())
    legend = "".join(
        f"<span class=\"cg-key\"><span class=\"cg-dot\" style=\"border-color:{STATUS_COLORS[s]}\"></span>{STATUS_LABELS[s]} ({_counts.get(s, 0)})</span>"
        for s in ("gt", "prom", "prov", "cls", "lead"))
    legend += ("<span class=\"cg-key\"><span class=\"cg-dot\" style=\"border-color:#888\"></span>"
               "hatched = unobserved</span>")
    parts.append(f"<div class=\"cg-legend\">{legend}</div>")
    parts.append("<div class=\"cg-legend\"><span>bar = frequency in the 1,847-pair stream"
                 " &middot; hover a cell for its count</span></div>")
    parts.append("</div>")
    return "".join(parts)


def build_png(freq, registry):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch

    cells = registry["cells"]
    maxn = max(freq.values())

    BG, FG, MUT = "#14161c", "#e8eaf0", "#8a8f9e"
    fig, ax = plt.subplots(figsize=(11, 13.4), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.5, 10.9)
    ax.axis("off")

    ax.text(5, 10.55, "R5005 key table — current state", ha="center", va="center",
            fontsize=17, color=FG, weight="bold")
    ax.text(5, 10.22, "96 of 100 cells observed · 1,847 pairs · bar = frequency",
            ha="center", va="center", fontsize=10, color=MUT)

    for r in range(10):
        for c_ in range(10):
            g = f"{r}{c_}"
            x, y = c_, 9 - r
            n = freq.get(g, 0)
            entry = cells.get(g)
            if g not in freq:
                face, edge, lw, ls = "#1b1e26", "#3a3f4d", 1, (0, (3, 2))
                hatch = "///"
            elif entry:
                col = STATUS_COLORS[entry[1]]
                face, edge, lw, ls, hatch = "#1e222c", col, 2.2, "-", None
            else:
                face, edge, lw, ls, hatch = "#1e222c", "#3a3f4d", 1, "-", None
            box = FancyBboxPatch((x + 0.04, y + 0.04), 0.92, 0.92,
                                 boxstyle="round,pad=0.01,rounding_size=0.08",
                                 facecolor=face, edgecolor=edge, linewidth=lw,
                                 linestyle=ls, hatch=hatch)
            ax.add_patch(box)
            ax.text(x + 0.5, y + 0.72, g, ha="center", va="center",
                    fontsize=8, color=MUT)
            if entry:
                ax.text(x + 0.5, y + 0.45, entry[0], ha="center", va="center",
                        fontsize=11 if len(entry[0]) <= 4 else 9,
                        color=STATUS_COLORS[entry[1]], weight="bold")
            ax.text(x + 0.5, y + 0.20, str(n) if n else "—", ha="center",
                    va="center", fontsize=7.5, color=MUT)
            if n:
                ax.add_patch(plt.Rectangle((x + 0.08, y + 0.07),
                                           0.84 * n / maxn, 0.045,
                                           facecolor="#7aa2f7", alpha=0.8,
                                           edgecolor="none"))

    ly = -0.55
    items = [("pencil ground truth", STATUS_COLORS["gt"], "-"),
             ("promoted", STATUS_COLORS["prom"], "-"),
             ("provisional", STATUS_COLORS["prov"], "-"),
             ("class", STATUS_COLORS["cls"], "-"),
             ("lead (pending)", STATUS_COLORS["lead"], (0, (3, 2))),
             ("unobserved", "#3a3f4d", (0, (3, 2)))]
    xs = [0.75, 3.0, 4.45, 6.0, 7.05, 8.85]
    for (label, col, ls), x0 in zip(items, xs):
        ax.add_patch(plt.Rectangle((x0 - 0.45, ly - 0.13), 0.34, 0.22,
                                   facecolor="none", edgecolor=col,
                                   linewidth=2, linestyle=ls))
        ax.text(x0 + 0.02, ly, label, ha="left", va="center",
                fontsize=9, color=MUT)
    ax.text(5, -1.1,
            f"gt {sum(1 for v in cells.values() if v[1] == 'gt')} · "
            f"prom {sum(1 for v in cells.values() if v[1] == 'prom')} · "
            f"prov {sum(1 for v in cells.values() if v[1] == 'prov')} · "
            f"cls {sum(1 for v in cells.values() if v[1] == 'cls')} · "
            f"lead {sum(1 for v in cells.values() if v[1] == 'lead')} — "
            f"{len(cells)}/96 observed cells · generated "
            f"{__import__('datetime').date.today().isoformat()}",
            ha="center", va="center", fontsize=9, color=MUT)
    fig.savefig(OUT_PNG, facecolor=BG, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)


def main():
    check_only = "--check" in sys.argv
    freq = load_frequencies()
    registry = json.load(open(os.path.join(HERE, "table-registry.json")))
    html = build_html(freq, registry)

    def sha(p):
        return hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None

    changed = False
    if sha(OUT_HTML) != hashlib.sha256(html.encode()).hexdigest():
        if not check_only:
            open(OUT_HTML, "w").write(html)
        changed = True
    # PNG: regenerate to temp and compare
    import tempfile
    global OUT_PNG
    real_png = OUT_PNG
    with tempfile.TemporaryDirectory() as td:
        OUT_PNG = os.path.join(td, "t.png")
        build_png(freq, registry)
        new_sha = sha(OUT_PNG)
        OUT_PNG = real_png
        if sha(real_png) != new_sha:
            changed = True
            if not check_only:
                build_png(freq, registry)
    print("CHANGED" if changed else "UNCHANGED")
    return 0 if (changed or not check_only) else 1


if __name__ == "__main__":
    sys.exit(main())
