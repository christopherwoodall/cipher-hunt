#!/usr/bin/env python3
"""Held-out calibration for the Seebach next-token predictor.

Held-out = 3 WHOLE documents, never seen in training (no leakage):
  guizot-memoires-t2-gutenberg.txt, revue-deux-mondes-1841-q4.txt,
  talleyrand-memoires-v1.txt

Measures, separately for --standard and --byear modes:
  A. global next-cell accuracy: sample N positions, rank the true next
     cell under stupid backoff (optimistic ties:
     rank = 1 + #{w: P(w) > P(true)}). Reports top-1/3/5, MRR, and
     accuracy by available context length.
  B. targeted solved contexts: every occurrence of each solved context in
     held-out; rank of the true next cell (all occurrences) AND of the true
     next word (1-3 cells via the beam; first <=40 occurrences per phrase,
     2026-10-08 cap so the run finishes under contention; cell ranks are
     unaffected). Contexts: "la première", "par ce que",
     "par le", "qui", "que", "ce qui", "en ce", "m'en", "ne" (verb slot),
     "ne X" -> "pas" for the 25 most frequent "ne X" bigrams.
  C. verb stems + inflections: top-30 stems mined from TRAINING word
     counts; in held-out, rank of the true cell following each stem.
  D. by-ear mismatch quantification: segmentation disagreement rate,
     cells/word, vocab overlap (Jaccard), banked-cell rank shifts,
     solved-context counts in train under both modes.

Writes JSON to stdout; the human-readable numbers go to CALIBRATION.md.
"""
import json
import math
import os
import random
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from predict import Model  # noqa: E402
from tokenize import segment_stream, iter_words  # noqa: E402
from build import CORPUS, HELDOUT, TRAIN  # noqa: E402

SEP_CTX = 5  # model context width
SAMPLE_N = 20000


def load_streams(files, mode):
    streams = {}
    for fn in files:
        with open(os.path.join(CORPUS, fn), encoding="utf-8", errors="replace") as f:
            streams[fn] = segment_stream(f.read(), mode)
    return streams


def rank_of(dist, true):
    """Optimistic rank of true under dist {cell: prob}."""
    pt = dist.get(true)
    if pt is None:
        return float("inf")
    return 1 + sum(1 for w, p in dist.items() if p > pt)


class Calibrator:
    def __init__(self, db):
        self.model = Model(db)

    def dist(self, mode, ctx):
        # NOTE (2026-10-07): this used to cache the full cond_dist dict per
        # context, but 5-cell contexts are ~all distinct, so the cache grew
        # to tens of GB (16.7k-entry dict per context) and OOM-killed the
        # run. Recompute per call: ~13ms each, flat memory.
        key = tuple(ctx[-SEP_CTX:])
        return self.model.cond_dist(mode, key)[0]

    def global_accuracy(self, streams, mode, n=SAMPLE_N, seed=7):
        rng = random.Random(seed)
        # sample positions with >=1 context cell, spread across docs
        per_doc = []
        for fn, s in streams.items():
            idx = [i for i in range(1, len(s) - 1)]
            k = max(1, int(n * len(s) / sum(len(v) for v in streams.values())))
            per_doc.extend((fn, i) for i in rng.sample(idx, min(k, len(idx))))
        rng.shuffle(per_doc)
        per_doc = per_doc[:n]
        hits = {1: 0, 3: 0, 5: 0}
        mrr = 0.0
        by_len = {}
        total = 0
        for fn, i in per_doc:
            s = streams[fn]
            ctx = s[max(0, i - SEP_CTX):i]
            true = s[i]
            d = self.dist(mode, ctx)
            r = rank_of(d, true)
            total += 1
            mrr += 1.0 / r if r != float("inf") else 0.0
            for kk in hits:
                if r <= kk:
                    hits[kk] += 1
            L = len(ctx)
            b = by_len.setdefault(L, [0, 0, 0, 0])
            b[0] += 1
            if r == 1:
                b[1] += 1
            if r <= 3:
                b[2] += 1
            if r <= 5:
                b[3] += 1
        return {
            "n": total,
            "top1": hits[1] / total, "top3": hits[3] / total,
            "top5": hits[5] / total, "mrr": mrr / total,
            "by_context_len": {str(L): {"n": b[0], "top1": b[1] / b[0],
                                        "top3": b[2] / b[0], "top5": b[3] / b[0]}
                               for L, b in sorted(by_len.items())},
        }

    def targeted_contexts(self, streams, mode, resume=None, on_phrase=None):
        """Solved contexts (as word phrases) -> next-cell / next-word ranks.

        resume: dict {phrase: result} of already-computed phrases (skipped).
        on_phrase(ph, result): called after each newly computed phrase, so
        the caller can checkpoint (2026-10-08: a VM reboot killed a run
        135 min in; the JSON is only written at the end, so everything was
        lost -- checkpoint per phrase now).
        """
        phrases = ["la première", "par ce que", "par le", "qui", "que",
                   "ce qui", "en ce", "m'en", "ne"]
        res = dict(resume) if resume else {}
        for ph in phrases:
            if ph in res:
                continue
        for ph in phrases:
            cells = segment_stream(ph, mode)
            n_cell = len(cells)
            occ = 0
            cell_hits = {1: 0, 3: 0, 5: 0}
            word_ranks = []  # rank of true next WORD (1-3 cells) in beam
            examples = []
            for fn, s in streams.items():
                for i in range(len(s) - n_cell - 3):
                    if s[i:i + n_cell] == cells:
                        occ += 1
                        ctx = s[max(0, i + n_cell - SEP_CTX):i + n_cell]
                        true = s[i + n_cell]
                        d = self.dist(mode, ctx)
                        r = rank_of(d, true)
                        for kk in cell_hits:
                            if r <= kk:
                                cell_hits[kk] += 1
                        # next-word rank: beam candidates vs true word cells.
                        # true word = cells until... we approximate with the
                        # next 1-3 cells vs beam's top-20 sequences.
                        # (2026-10-07: beam work capped at 120 occurrences per
                        # phrase so the calibration finishes; 2026-10-08:
                        # cut to 40 -- under machine contention each beam
                        # predict costs ~8s, and 120/phrase made the section
                        # take hours. Cell-level ranks above still use EVERY
                        # occurrence; word ranks use the first <=40.)
                        if occ <= 40:  # cap beam work
                            beam = self.model.predict(
                                mode, list(ctx), k=20, beam=40, maxlen=3)
                            true1 = [true]
                            true2 = s[i + n_cell:i + n_cell + 2]
                            true3 = s[i + n_cell:i + n_cell + 3]
                            wr = None
                            for j, c in enumerate(beam):
                                if (c["syllables"] == true1 or
                                        c["syllables"] == true2 or
                                        c["syllables"] == true3):
                                    wr = j + 1
                                    break
                            word_ranks.append(wr)
                            if len(examples) < 3:
                                examples.append({
                                    "true_next3": s[i + n_cell:i + n_cell + 3],
                                    "top5": [c["syllables"] for c in beam[:5]],
                                })
            wr_hits = {1: 0, 3: 0, 5: 0}
            for wr in word_ranks:
                if wr is not None:
                    for kk in wr_hits:
                        if wr <= kk:
                            wr_hits[kk] += 1
            res[ph] = {
                "cells": cells, "occurrences": occ,
                "next_cell_top1": cell_hits[1] / occ if occ else None,
                "next_cell_top3": cell_hits[3] / occ if occ else None,
                "next_cell_top5": cell_hits[5] / occ if occ else None,
                "next_word_n": len(word_ranks),
                "next_word_top1": wr_hits[1] / len(word_ranks) if word_ranks else None,
                "next_word_top3": wr_hits[3] / len(word_ranks) if word_ranks else None,
                "next_word_top5": wr_hits[5] / len(word_ranks) if word_ranks else None,
                "examples": examples,
            }
            if on_phrase is not None:
                on_phrase(ph, res[ph])
        return res

    def ne_pas_frames(self, streams, mode):
        """'ne X' bigrams in held-out -> rank of 'pas' given ('ne', X)."""
        big = Counter()
        for s in streams.values():
            for i in range(len(s) - 2):
                if s[i] == "ne":
                    big[(s[i], s[i + 1])] += 1
        top = big.most_common(25)
        rows = []
        for (ne, x), c in top:
            d = self.dist(mode, ("ne", x))
            r = rank_of(d, "pas")
            rows.append({"bigram": [ne, x], "count": c, "pas_rank": r})
        return rows

    def verb_stems(self, streams, mode):
        """Top stems from TRAIN word counts -> rank of true next cell in held-out."""
        wc = Counter()
        for fn in TRAIN:
            with open(os.path.join(CORPUS, fn), encoding="utf-8", errors="replace") as f:
                for w in iter_words(f.read()):
                    wc[w] += 1
        suffixes = ["aient", "ait", "ant", "ent", "ez", "ons", "er", "ir",
                    "re", "is", "it", "as", "ai", "a", "e", "es", "ee"]
        stems = Counter()
        word_stem = {}
        for w, c in wc.items():
            if len(w) < 5:
                continue
            for suf in suffixes:
                if w.endswith(suf) and len(w) - len(suf) >= 3:
                    st = w[:len(w) - len(suf)]
                    stems[st] += c
                    word_stem[w] = st
                    break
        top_stems = [s for s, _ in stems.most_common(30)]
        res = {}
        for st in top_stems:
            cells = segment_stream(st, mode)
            occ = 0
            hits = {1: 0, 3: 0, 5: 0}
            mrr = 0.0
            for fn, s in streams.items():
                L = len(cells)
                for i in range(len(s) - L - 1):
                    if s[i:i + L] == cells:
                        occ += 1
                        if occ > 600:
                            break
                        ctx = s[max(0, i + L - SEP_CTX):i + L]
                        true = s[i + L]
                        r = rank_of(self.dist(mode, ctx), true)
                        mrr += 1.0 / r if r != float("inf") else 0.0
                        for kk in hits:
                            if r <= kk:
                                hits[kk] += 1
            if occ:
                res[st] = {"cells": cells, "occurrences": occ,
                           "top1": hits[1] / occ, "top3": hits[3] / occ,
                           "top5": hits[5] / occ, "mrr": mrr / occ}
        return res


def mismatch_quant(train_files):
    """By-ear mismatch quantification on TRAIN files (streamed per file,
    so the raw cell streams are never all in memory at once).

    2026-10-07 fix: the original divided total TRAIN cells by the 200k-word
    *sample* word count, inflating cells/word ~17x. n_w now counts every
    training word.
    """
    import itertools
    from tokenize import iter_words
    from byear import byear_cut, strip_acc
    sys.path.insert(0, "/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period")
    from syllabify import syllabify as _syllabify
    c_std, c_by = Counter(), Counter()
    n_std = n_by = n_w = 0
    sample_n = 0
    diff = 0
    for fi, fn in enumerate(train_files):
        with open(os.path.join(CORPUS, fn), encoding="utf-8", errors="replace") as f:
            wlist = list(iter_words(f.read()))
        n_w += len(wlist)
        for w in wlist:
            s_std = [strip_acc(c) for c in _syllabify(w)]
            s_by = byear_cut(w)
            n_std += len(s_std)
            n_by += len(s_by)
            for c in s_std:
                c_std[c] += 1
            for c in s_by:
                c_by[c] += 1
            # word-level disagreement on the first 200k words of TRAIN[:4]
            if fi < 4 and sample_n < 200000:
                sample_n += 1
                if s_std != s_by:
                    diff += 1
    set_std = set(c_std)
    set_by = set(c_by)
    inter = len(set_std & set_by)
    banked = ["la", "pre", "m", "i", "er", "e", "que", "ce", "qui", "par",
              "est", "le"]
    # approximate frequency rank (ties share the first index of their count)
    def rank(c, w):
        return (sorted(c.values(), reverse=True).index(c[w]) + 1) if w in c else None
    return {
        "word_sample_n": sample_n,
        "word_disagreement_rate": diff / sample_n,
        "cells_per_word_standard": n_std / n_w,
        "cells_per_word_byear": n_by / n_w,
        "vocab_standard": len(set_std), "vocab_byear": len(set_by),
        "vocab_jaccard": inter / len(set_std | set_by),
        "byear_only_cells": len(set_by - set_std),
        "standard_only_cells": len(set_std - set_by),
        "banked_ranks": {w: {"standard": rank(c_std, w), "byear": rank(c_by, w),
                             "std_count": c_std.get(w, 0), "by_count": c_by.get(w, 0)}
                         for w in banked},
    }


CKPT = os.path.join(HERE, "calibrate_checkpoint.json")


def load_ckpt(db_built_utc):
    """Load checkpoint; invalidate if the DB was rebuilt since."""
    try:
        with open(CKPT, encoding="utf-8") as f:
            c = json.load(f)
    except (OSError, ValueError):
        return {}
    if c.get("db_built_utc") != db_built_utc:
        print("checkpoint stale (DB rebuilt), starting fresh", flush=True,
              file=sys.stderr)
        return {}
    n_done = sum(len(m.get("targeted", {})) for m in c.get("modes", {}).values())
    print(f"checkpoint: resuming with {n_done} targeted phrases done",
          flush=True, file=sys.stderr)
    return c


def save_ckpt(ckpt):
    tmp = CKPT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(ckpt, f)
    os.replace(tmp, CKPT)


def main():
    db = os.path.join(HERE, "models", "seebach_nexttoken.db")
    cal = Calibrator(db)
    built_utc = dict(cal.model.con.execute(
        "SELECT k,v FROM meta WHERE k='built_utc'")).get("built_utc")
    ckpt = load_ckpt(built_utc)
    ckpt["db_built_utc"] = built_utc
    ckpt.setdefault("modes", {})
    out = {"modes": {}}
    for mode in ("standard", "byear"):
        mc = ckpt["modes"].setdefault(mode, {})
        streams = None

        def need_streams():
            nonlocal streams
            if streams is None:
                print(f"loading held-out streams [{mode}]...", flush=True,
                      file=sys.stderr)
                streams = load_streams(HELDOUT, mode)
            return streams

        if "global" not in mc:
            print(f"  global accuracy [{mode}]...", flush=True, file=sys.stderr)
            mc["global"] = cal.global_accuracy(need_streams(), mode)
            save_ckpt(ckpt)
        if "targeted" not in mc:
            mc["targeted"] = {}

        def on_phrase(ph, res_ph, _mc=mc):
            _mc["targeted"][ph] = res_ph
            save_ckpt(ckpt)
            print(f"  targeted [{mode}] phrase done: {ph}", flush=True,
                  file=sys.stderr)

        if len(mc["targeted"]) < 9:
            print(f"  targeted contexts [{mode}]...", flush=True, file=sys.stderr)
            mc["targeted"] = cal.targeted_contexts(
                need_streams(), mode, resume=mc["targeted"], on_phrase=on_phrase)
            save_ckpt(ckpt)
        if "ne_pas" not in mc:
            print(f"  ne..pas frames [{mode}]...", flush=True, file=sys.stderr)
            mc["ne_pas"] = cal.ne_pas_frames(need_streams(), mode)
            save_ckpt(ckpt)
        if "verb_stems" not in mc:
            print(f"  verb stems [{mode}]...", flush=True, file=sys.stderr)
            mc["verb_stems"] = cal.verb_stems(need_streams(), mode)
            save_ckpt(ckpt)
        out["modes"][mode] = {"global": mc["global"], "targeted": mc["targeted"],
                              "ne_pas": mc["ne_pas"],
                              "verb_stems": mc["verb_stems"]}
    if "mismatch" not in ckpt:
        print("mismatch quantification (train)...", flush=True, file=sys.stderr)
        ckpt["mismatch"] = mismatch_quant(TRAIN)
        save_ckpt(ckpt)
    out["mismatch"] = ckpt["mismatch"]
    out["heldout_files"] = HELDOUT
    json.dump(out, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
