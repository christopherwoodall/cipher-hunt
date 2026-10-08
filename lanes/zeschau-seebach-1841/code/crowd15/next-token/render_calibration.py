#!/usr/bin/env python3
"""Render calibrate.json numbers as markdown tables for CALIBRATION.md.

Usage: python3 render_calibration.py > tables.md   (stdout only)
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "calibrate.json"), encoding="utf-8"))

out = []


def pct(x):
    return "n/a" if x is None else f"{100*x:.1f}%"


def avg(x):
    return "n/a" if x is None else f"{x:.3f}"


out.append("## A. Global next-cell accuracy (held-out, n=20,000)")
out.append("")
out.append("| mode | top-1 | top-3 | top-5 | MRR |")
out.append("|---|---|---|---|---|")
for mode in ("standard", "byear"):
    g = d["modes"][mode]["global"]
    out.append(f"| {mode} | {pct(g['top1'])} | {pct(g['top3'])} | {pct(g['top5'])} | {avg(g['mrr'])} |")
out.append("")
out.append("By available context length (cells):")
out.append("")
out.append("| mode | ctx len | n | top-1 | top-3 | top-5 |")
out.append("|---|---|---|---|---|---|")
for mode in ("standard", "byear"):
    for L, b in d["modes"][mode]["global"]["by_context_len"].items():
        out.append(f"| {mode} | {L} | {b['n']} | {pct(b['top1'])} | {pct(b['top3'])} | {pct(b['top5'])} |")
out.append("")

out.append("## B. Targeted solved contexts (held-out)")
out.append("")
out.append("| phrase | mode | cells | occ | next-cell top-1/3/5 | next-word top-1/3/5 (beam, n) |")
out.append("|---|---|---|---|---|---|")
for ph in ["la première", "par ce que", "par le", "qui", "que", "ce qui", "en ce", "m'en", "ne"]:
    for mode in ("standard", "byear"):
        t = d["modes"][mode]["targeted"][ph]
        cells = "|".join(t["cells"])
        c = f"{pct(t['next_cell_top1'])}/{pct(t['next_cell_top3'])}/{pct(t['next_cell_top5'])}"
        w = (f"{pct(t['next_word_top1'])}/{pct(t['next_word_top3'])}/{pct(t['next_word_top5'])} "
             f"(n={t['next_word_n']})")
        out.append(f"| {ph} | {mode} | {cells} | {t['occurrences']} | {c} | {w} |")
out.append("")
for ph in ["la première", "par ce que"]:
    for mode in ("standard", "byear"):
        t = d["modes"][mode]["targeted"][ph]
        out.append(f"### {ph} [{mode}] — examples (true next 3 cells vs model top-5 beam)")
        out.append("")
        for ex in t["examples"]:
            out.append(f"- true: `{'|'.join(ex['true_next3'])}`")
            for i, b in enumerate(ex["top5"][:5], 1):
                out.append(f"  beam#{i}: `{'|'.join(b)}`")
        out.append("")

out.append('### "ne X" → "pas" frames (25 most frequent held-out bigrams)')
out.append("")
out.append("| mode | ne X | count | rank of \"pas\" |")
out.append("|---|---|---|---|")
for mode in ("standard", "byear"):
    for r in d["modes"][mode]["ne_pas"]:
        out.append(f"| {mode} | `{'|'.join(r['bigram'])}` | {r['count']} | {r['pas_rank']} |")
out.append("")

out.append("## C. Verb-stem inflection prediction (held-out)")
out.append("")
out.append("| stem | mode | cells | occ | top-1 | top-3 | top-5 | MRR |")
out.append("|---|---|---|---|---|---|---|---|")
for mode in ("standard", "byear"):
    vs = d["modes"][mode]["verb_stems"]
    for st, v in sorted(vs.items(), key=lambda kv: -kv[1]["top1"]):
        out.append(f"| {st} | {mode} | {'|'.join(v['cells'])} | {v['occurrences']} | "
                   f"{pct(v['top1'])} | {pct(v['top3'])} | {pct(v['top5'])} | {avg(v['mrr'])} |")
out.append("")

m = d["mismatch"]
out.append("## D. By-ear mismatch quantification (TRAIN)")
out.append("")
out.append(f"- word disagreement rate (200k-word sample): {100*m['word_disagreement_rate']:.1f}%")
out.append(f"- cells/word: standard {m['cells_per_word_standard']:.3f}, byear {m['cells_per_word_byear']:.3f}")
out.append(f"- vocab: standard {m['vocab_standard']}, byear {m['vocab_byear']}, "
           f"Jaccard {m['vocab_jaccard']:.3f}")
out.append(f"- by-ear-only cells: {m['byear_only_cells']}; standard-only cells: {m['standard_only_cells']}")
out.append("")
out.append("| banked cell | std rank (count) | byear rank (count) |")
out.append("|---|---|---|")
for w, r in m["banked_ranks"].items():
    out.append(f"| {w} | {r['standard']} ({r['std_count']}) | {r['byear']} ({r['by_count']}) |")
out.append("")

sys.stdout.write("\n".join(out) + "\n")
