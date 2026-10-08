#!/usr/bin/env python3
"""Build the syllable n-gram model DB for the Seebach next-token predictor.

Training inventory (French-only; see corpus language audit in
CALIBRATION.md -- the 15 Allgemeine-Zeitung issues, the ADB entry, the 2
Metternich volumes (Fraktur OCR + German editorial) and the mixed
English/French Levant volume are EXCLUDED):

  TRAIN (11 docs):
    guizot-memoires-t1-gutenberg.txt, guizot-memoires-t3-gutenberg.txt,
    guizot-memoires-t5-t6.txt,
    nesselrode-v7.txt, nesselrode-v8.txt, nesselrode-v9.txt, nesselrode-v10.txt,
    pozzo-di-borgo-correspondance-v1.txt,
    revue-deux-mondes-1841-q1.txt, revue-deux-mondes-1841-q2.txt,
    revue-deux-mondes-1841-q3.txt
  HELDOUT (3 whole documents -- never counted here):
    guizot-memoires-t2-gutenberg.txt, revue-deux-mondes-1841-q4.txt,
    talleyrand-memoires-v1.txt

Model: orders 1..6 over syllable cells (context up to 5). Pruning: every
1-gram and 2-gram kept; orders >= 3 kept iff count >= 2. Scoring uses
stupid backoff (see predict.py); pruning at >=2 for higher orders is the
standard companion choice.

Durability (2026-10-07 fix): the 2026-10-07 builder died in a daemon
restart mid-build leaving an EMPTY db (tables created, zero rows, stale
-journal) because the first commit only happened after a full mode
finished — and a SECOND build died the same way in a VM reboot an hour
later, this time mid-staging. The build is now RESUMABLE: per-file counts
stage into a separate staging DB (plain append tables, no indexes — fast)
with the filename recorded and a commit per file, so a kill/reboot loses
at most one file's work; reruns skip already-staged files, verify every
TRAIN file is staged before aggregating, and wipe staging if the TRAIN
list changed. Each mode's staged counts are then aggregated (GROUP BY)
into the indexed final tables in one pass. Pruning stays GLOBAL
(delete-after-load on the summed counts), so the model is identical to the
original accumulate-then-insert design. meta rows are written last, so a
missing 'built_utc' key marks a partial build. (An earlier
per-file-ON-CONFLICT-upsert variant was abandoned: upserts against the
growing PK degraded steeply on the big files — file 3's ~2.8M-row upsert
was still running after 15 minutes; staging + one GROUP BY per mode is an
order of magnitude faster. The redundant idx_ngram_lookup was also
dropped: (mode,ord,ctx) is a leftmost prefix of the ngram PK, which serves
those lookups directly.)

Output: models/seebach_nexttoken.db (SQLite):
  ngram(mode, ord, ctx, nxt, cnt)   -- ord>=2, ctx = \x1f-joined cells
  ctx_total(mode, ord, ctx, total)
  unigram(mode, syl, cnt)
  meta(k, v)                        -- build manifest, counts, git-free version
"""
import hashlib
import json
import os
import sqlite3
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tokenize import segment_stream  # noqa: E402

CORPUS = "/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus"
DB = os.path.join(HERE, "models", "seebach_nexttoken.db")
MAX_ORDER = 6
SEP = "\x1f"

TRAIN = [
    "guizot-memoires-t1-gutenberg.txt",
    "guizot-memoires-t3-gutenberg.txt",
    "guizot-memoires-t5-t6.txt",
    "nesselrode-v7.txt", "nesselrode-v8.txt", "nesselrode-v9.txt",
    "nesselrode-v10.txt",
    "pozzo-di-borgo-correspondance-v1.txt",
    "revue-deux-mondes-1841-q1.txt",
    "revue-deux-mondes-1841-q2.txt",
    "revue-deux-mondes-1841-q3.txt",
]
HELDOUT = [
    "guizot-memoires-t2-gutenberg.txt",
    "revue-deux-mondes-1841-q4.txt",
    "talleyrand-memoires-v1.txt",
]


def count_stream(stream, counts):
    """counts[(ord, ctx_tuple, nxt)] += 1 for ord=2..MAX_ORDER."""
    n = len(stream)
    for i in range(1, n):
        nxt = stream[i]
        for o in range(2, min(MAX_ORDER, i + 1) + 1):
            ctx = tuple(stream[i - o + 1:i])
            counts[(o, ctx, nxt)] = counts.get((o, ctx, nxt), 0) + 1


def build():
    t0 = time.time()
    os.makedirs(os.path.join(HERE, "models"), exist_ok=True)
    # SQLite temp space for the per-mode GROUP BY sort: /tmp is a 512MB
    # tmpfs on this VM, so point it at the (roomy) home filesystem.
    tmpdir = os.path.join(HERE, "models", ".build-tmp")
    os.makedirs(tmpdir, exist_ok=True)
    os.environ["SQLITE_TMPDIR"] = tmpdir
    if os.path.exists(DB):
        os.remove(DB)
    if os.path.exists(DB + "-journal"):  # stale hot journal from a killed build
        os.remove(DB + "-journal")
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("CREATE TABLE ngram(mode TEXT, ord INTEGER, ctx TEXT, nxt TEXT, cnt INTEGER, PRIMARY KEY (mode, ord, ctx, nxt))")
    cur.execute("CREATE TABLE ctx_total(mode TEXT, ord INTEGER, ctx TEXT, total INTEGER, PRIMARY KEY (mode, ord, ctx))")
    cur.execute("CREATE TABLE unigram(mode TEXT, syl TEXT, cnt INTEGER, PRIMARY KEY (mode, syl))")
    cur.execute("CREATE TABLE meta(k TEXT PRIMARY KEY, v TEXT)")
    # NOTE: no idx_ngram_lookup — (mode,ord,ctx) is a leftmost prefix of the
    # ngram PK, which serves those lookups directly (verified post-build with
    # EXPLAIN QUERY PLAN). A separate index would only slow the load.
    cur.execute("PRAGMA cache_size=-262144")  # 256MB page cache for aggregation
    con.commit()

    # Staging DB: plain append tables, NO pk/indexes — per-file counts land
    # here with a commit per file (a kill/reboot loses at most one file's
    # work and never corrupts the final tables). The `file` column makes
    # the build RESUMABLE: files already staged are skipped on rerun, and
    # aggregation refuses to run unless every TRAIN file is staged.
    # (2026-10-07: a reboot killed a build mid-staging; the straggler
    # stage.db had no file markers, so its completeness was unverifiable
    # and it was discarded. Lesson: stage file-granular or don't bother.)
    stage_db = os.path.join(tmpdir, "stage.db")
    scon = sqlite3.connect(stage_db)
    scon.execute("CREATE TABLE IF NOT EXISTS s(mode TEXT, fn TEXT, ord INTEGER, ctx TEXT, nxt TEXT, cnt INTEGER)")
    scon.execute("CREATE TABLE IF NOT EXISTS su(mode TEXT, fn TEXT, syl TEXT, cnt INTEGER)")
    scon.execute("CREATE TABLE IF NOT EXISTS sig(k TEXT PRIMARY KEY, v TEXT)")
    # if the TRAIN list ever changes, previously staged rows are stale
    train_sig = hashlib.sha256(json.dumps(TRAIN).encode()).hexdigest()[:16]
    row = scon.execute("SELECT v FROM sig WHERE k='train'").fetchone()
    if row and row[0] != train_sig:
        scon.execute("DELETE FROM s")
        scon.execute("DELETE FROM su")
        print("staging wiped: TRAIN list changed since last stage", flush=True)
    scon.execute("INSERT OR REPLACE INTO sig VALUES ('train', ?)", (train_sig,))
    scon.commit()

    for mode in ("standard", "byear"):
        total_cells = 0
        staged = {r[0] for r in scon.execute(
            "SELECT DISTINCT fn FROM s WHERE mode=?", (mode,)).fetchall()}
        for fn in TRAIN:
            if fn in staged:
                # resume: count cells without re-segmenting (cheap wc-style
                # pass is unnecessary; totals recomputed from su below)
                print(f"[{mode}] {fn}: already staged, skipping", flush=True)
                continue
            with open(os.path.join(CORPUS, fn), encoding="utf-8", errors="replace") as f:
                stream = segment_stream(f.read(), mode)
            total_cells += len(stream)
            counts = {}
            count_stream(stream, counts)
            # keys are unique within one file: plain appends, no conflicts
            scon.executemany("INSERT INTO s VALUES (?,?,?,?,?,?)",
                             [(mode, fn, o, SEP.join(ctx), nxt, c)
                              for (o, ctx, nxt), c in counts.items()])
            uni = {}
            for s in stream:
                uni[s] = uni.get(s, 0) + 1
            scon.executemany("INSERT INTO su VALUES (?,?,?,?)",
                             [(mode, fn, s, c) for s, c in uni.items()])
            scon.commit()
            del counts, uni, stream
            print(f"[{mode}] {fn}: staged (committed)", flush=True)
        # verify completeness before aggregating: every TRAIN file staged
        staged = {r[0] for r in scon.execute(
            "SELECT DISTINCT fn FROM s WHERE mode=?", (mode,)).fetchall()}
        missing = [fn for fn in TRAIN if fn not in staged]
        if missing:
            raise RuntimeError(f"[{mode}] staging incomplete, missing: {missing}")
        total_cells = scon.execute(
            "SELECT SUM(cnt) FROM su WHERE mode=?", (mode,)).fetchone()[0]
        print(f"[{mode}] aggregating staged counts ({total_cells} cells)...", flush=True)
        cur.execute("ATTACH DATABASE ? AS st", (stage_db,))
        cur.execute("""INSERT INTO ngram
                       SELECT mode, ord, ctx, nxt, SUM(cnt) FROM st.s
                       WHERE mode=? GROUP BY mode, ord, ctx, nxt""", (mode,))
        cur.execute("""INSERT INTO unigram
                       SELECT mode, syl, SUM(cnt) FROM st.su
                       WHERE mode=? GROUP BY mode, syl""", (mode,))
        con.commit()
        cur.execute("DETACH DATABASE st")
        # GLOBAL pruning on summed counts (identical semantics to the old
        # accumulate-then-insert design): orders >= 3 kept iff cnt >= 2.
        cur.execute("DELETE FROM ngram WHERE mode=? AND ord >= 3 AND cnt < 2", (mode,))
        cur.execute("""INSERT INTO ctx_total
                       SELECT mode, ord, ctx, SUM(cnt) FROM ngram
                       WHERE mode=? GROUP BY mode, ord, ctx""", (mode,))
        con.commit()
        kept = cur.execute("SELECT COUNT(*) FROM ngram WHERE mode=?", (mode,)).fetchone()[0]
        v = cur.execute("SELECT COUNT(*) FROM unigram WHERE mode=?", (mode,)).fetchone()[0]
        print(f"[{mode}] kept ngrams={kept} unigrams={v} cells={total_cells}", flush=True)
        cur.execute("INSERT INTO meta VALUES (?,?)", (f"cells_{mode}", str(total_cells)))
        cur.execute("INSERT INTO meta VALUES (?,?)", (f"vocab_{mode}", str(v)))
        con.commit()

    cur.execute("INSERT INTO meta VALUES (?,?)", ("max_order", str(MAX_ORDER)))
    cur.execute("INSERT INTO meta VALUES (?,?)", ("train_files", json.dumps(TRAIN)))
    cur.execute("INSERT INTO meta VALUES (?,?)", ("heldout_files", json.dumps(HELDOUT)))
    cur.execute("INSERT INTO meta VALUES (?,?)", ("pruning", "ord>=3 kept iff cnt>=2"))
    cur.execute("INSERT INTO meta VALUES (?,?)", ("built_utc", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
    con.commit()
    scon.close()
    con.close()
    # stage.db is KEPT in models/.build-tmp: the final DB is standalone,
    # and a future rerun resumes from staged files instead of re-segmenting.
    size = os.path.getsize(DB)
    print(f"DB written: {DB} ({size/1e6:.1f} MB) in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    build()
