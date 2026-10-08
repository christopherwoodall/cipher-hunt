#!/usr/bin/env python3
"""Next-syllable predictor for the Seebach R5005 lane.

CLI:
  predict.py --context "syll1 syll2 ..." --k 10 [--byear] [--words]
             [--beam 60] [--maxlen 3] [--db PATH]

  --context  space-separated syllable cells in the model's segmentation.
             The last up-to-5 cells are used as the n-gram context
             (model order is 6).
  --k        number of candidate continuations returned (default 10).
  --byear    use the by-ear fine-cut model (default: standard syllabifier).
  --words    treat --context as plain French words and segment them with
             the mode's segmenter instead of taking cells literally.
  --beam     beam width for multi-syllable expansion (default 60).
  --maxlen   max syllables per returned candidate, 1..3 (default 3).
  --db       path to models/seebach_nexttoken.db (default: alongside script).

Output: JSON array on stdout:
  [{"syllables": ["que"], "prob": 0.42}, ...]
sorted by prob descending. "prob" is the model's JOINT probability
P(s1..sm | context) under stupid backoff -- a ranking score, NOT
renormalized over the returned set (the beam truncates the tail).

Scoring: stupid backoff (Brants et al. 2007), backoff weight 0.4:
  S(w | c1..cn) = cnt(c,w)/cnt(c)            if seen
                = 0.4 * S(w | c2..cn)        otherwise
  unigram floor: cnt(w)/N, unseen w -> 0.4^5 / V.
Multi-syllable candidates come from beam search: at each depth the top
--beam next-cells extend every beam; all prefixes of length 1..maxlen
are candidates with joint probability = product of conditionals.

Reproduction: the DB is built by build.py from the era corpus
(see CALIBRATION.md for the file inventory and segmentation rules).
"""
import argparse
import json
import math
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tokenize import segment_stream  # noqa: E402

DEFAULT_DB = os.path.join(HERE, "models", "seebach_nexttoken.db")
SEP = "\x1f"
BACKOFF = 0.4
MAX_ORDER = 6


class Model:
    def __init__(self, db_path=DEFAULT_DB):
        self.con = sqlite3.connect("file:%s?mode=ro" % db_path, uri=True)
        self.con.execute("PRAGMA query_only=ON")
        meta = dict(self.con.execute("SELECT k,v FROM meta").fetchall())
        self.max_order = int(meta.get("max_order", MAX_ORDER))
        self.vocab = {}
        for mode in ("standard", "byear"):
            rows = self.con.execute(
                "SELECT syl, cnt FROM unigram WHERE mode=?", (mode,)).fetchall()
            self.vocab[mode] = {s: c for s, c in rows}
        self.total = {m: sum(self.vocab[m].values()) for m in self.vocab}
        # small caches: candidate nexts per (mode, ord, ctx)
        self._cand_cache = {}

    def candidates(self, mode, ctx):
        """{nxt: cnt} for each backoff level: list of dicts, longest first."""
        key = (mode, ctx)
        if key in self._cand_cache:
            return self._cand_cache[key]
        out = []
        for o in range(min(len(ctx) + 1, self.max_order), 1, -1):
            c = SEP.join(ctx[-(o - 1):])
            rows = self.con.execute(
                "SELECT nxt, cnt FROM ngram WHERE mode=? AND ord=? AND ctx=?",
                (mode, o, c)).fetchall()
            d = {n: cnt for n, cnt in rows}
            tot = self.con.execute(
                "SELECT total FROM ctx_total WHERE mode=? AND ord=? AND ctx=?",
                (mode, o, c)).fetchone()
            out.append((d, tot[0] if tot else 0))
        self._cand_cache[key] = out
        return out

    def cond_dist(self, mode, ctx):
        """Full next-cell distribution {cell: prob} under stupid backoff.

        Only cells observed after some backoff suffix of ctx get mass;
        unseen cells share the floor (returned separately via floor_prob).
        Longest-match: each cell takes its probability from the longest
        context level where it was observed, times 0.4 per backed-off level.
        """
        levels = self.candidates(mode, tuple(ctx))
        V = len(self.vocab[mode])
        N = self.total[mode]
        uni = self.vocab[mode]
        dist = {}
        for lvl, (d, tot) in enumerate(levels):
            for w, c in d.items():
                if w not in dist:
                    dist[w] = (BACKOFF ** lvl) * (c / tot)
        for w, c in uni.items():
            if w not in dist:
                dist[w] = (BACKOFF ** 5) * (c / N)
        floor = (BACKOFF ** 5) / max(V, 1)
        return dist, floor

    def logprob_next(self, mode, ctx, w):
        """log P(w | ctx) under stupid backoff (exact, no full distribution)."""
        ctx = tuple(ctx)
        V = len(self.vocab[mode])
        N = self.total[mode]
        for o in range(min(len(ctx) + 1, self.max_order), 1, -1):
            c = SEP.join(ctx[-(o - 1):])
            row = self.con.execute(
                "SELECT cnt FROM ngram WHERE mode=? AND ord=? AND ctx=? AND nxt=?",
                (mode, o, c, w)).fetchone()
            if row:
                tot = self.con.execute(
                    "SELECT total FROM ctx_total WHERE mode=? AND ord=? AND ctx=?",
                    (mode, o, c)).fetchone()[0]
                return math.log(row[0] / tot) + (self.max_order - o) * math.log(BACKOFF)
        c = self.vocab[mode].get(w)
        if c:
            return math.log(c / N) + 5 * math.log(BACKOFF)
        return math.log(1.0 / max(V, 1)) + 5 * math.log(BACKOFF)

    def top_next(self, mode, ctx, beam):
        """Top-`beam` (cell, logprob) continuations for ctx."""
        dist, _ = self.cond_dist(mode, tuple(ctx))
        items = sorted(dist.items(), key=lambda kv: -kv[1])[:beam]
        tot = sum(dist.values())
        return [(w, math.log(p)) for w, p in items]

    def predict(self, mode, context_cells, k=10, beam=60, maxlen=3):
        ctx = tuple(context_cells[-5:])
        # beams: list of (seq_tuple, logprob)
        beams = [((), 0.0)]
        cands = {}  # seq -> logprob (all prefixes length 1..maxlen)
        for depth in range(1, maxlen + 1):
            new_beams = []
            for seq, lp in beams:
                ext = self.top_next(mode, ctx + seq, beam)
                for w, wlp in ext:
                    nseq = seq + (w,)
                    nlp = lp + wlp
                    if nseq not in cands or nlp > cands[nseq]:
                        cands[nseq] = nlp
                    new_beams.append((nseq, nlp))
            # keep global top-`beam` beams for next expansion
            new_beams.sort(key=lambda t: -t[1])
            beams = new_beams[:beam]
            if not beams:
                break
        ranked = sorted(cands.items(), key=lambda kv: -kv[1])[:k]
        return [{"syllables": list(seq), "prob": math.exp(lp)}
                for seq, lp in ranked]


def main():
    ap = argparse.ArgumentParser(description="Seebach R5005 next-syllable predictor")
    ap.add_argument("--context", required=True,
                    help="space-separated syllable cells (or words with --words)")
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--byear", action="store_true",
                    help="use the by-ear fine-cut model (default: standard)")
    ap.add_argument("--words", action="store_true",
                    help="segment --context as French words instead of cells")
    ap.add_argument("--beam", type=int, default=60)
    ap.add_argument("--maxlen", type=int, default=3)
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    mode = "byear" if a.byear else "standard"
    if a.words:
        cells = segment_stream(a.context, mode)
    else:
        cells = a.context.strip().split()
    model = Model(a.db)
    out = model.predict(mode, cells, k=a.k, beam=a.beam,
                        maxlen=max(1, min(3, a.maxlen)))
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
