#!/usr/bin/env python3
"""Simulated-annealing monoalphabetic substitution solver (from scratch).

Target: Catherine de Medicis -> Philibert du Croc, 27 Apr 1567 cipher
(lane catherine-medici-1567). The cipher uses ~40 distinct glyph tokens for a
French plaintext, so the key maps each cipher symbol to one of 26 letters
(many-to-one allowed: homophones/nulls possible). Scoring is French quadgram
log-likelihood built from a Project Gutenberg French corpus.

Usage:
  python3 code/anneal.py --stats            # cipher stats only
  python3 code/anneal.py --build-model      # build + cache quadgram model
  python3 code/anneal.py                    # full anneal run (uses cache)
"""
import argparse, json, math, os, random, re, sys, unicodedata

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(LANE, "data")
CIPHER_FILE = os.path.join(DATA, "medici-1567-cipher.txt")
CORPUS_FILE = os.path.join(DATA, "gutenberg-17489-miserables1.txt")
MODEL_CACHE = os.path.join(DATA, "french-quadgrams.json")
PLAINTEXT_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ---------------------------------------------------------------- corpus ---
def normalize_french(text):
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return re.sub(r"[^A-Z]", "", text.upper())

def build_quadgrams(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        raw = f.read()
    # strip Gutenberg header/footer
    m1 = raw.find("*** START OF")
    m2 = raw.find("*** END OF")
    if m1 != -1 and m2 != -1:
        raw = raw[m1:m2]
    t = normalize_french(raw)
    counts = {}
    total = 0
    for i in range(len(t) - 3):
        q = t[i:i+4]
        counts[q] = counts.get(q, 0) + 1
        total += 1
    floor = 0.01
    logp = {}
    denom = total + floor * (26 ** 4)
    for q, c in counts.items():
        logp[q] = math.log10((c + floor) / denom)
    logp_floor = math.log10(floor / denom)
    meta = {"corpus_chars": len(t), "quadgrams_total": total,
            "distinct_quadgrams": len(counts)}
    return logp, logp_floor, meta

def load_model():
    if os.path.exists(MODEL_CACHE):
        with open(MODEL_CACHE) as f:
            d = json.load(f)
        return d["logp"], d["floor"], d["meta"]
    logp, floor, meta = build_quadgrams(CORPUS_FILE)
    with open(MODEL_CACHE, "w") as f:
        json.dump({"logp": logp, "floor": floor, "meta": meta}, f)
    return logp, floor, meta

# ---------------------------------------------------------------- cipher ---
def load_cipher():
    """Parse NORMALIZED section of the transcription file -> list of tokens."""
    toks, in_norm, in_inline = [], False, False
    with open(CIPHER_FILE, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s.startswith("## NORMALIZED"):
                in_norm = True
                continue
            if s.startswith("## STATS"):
                break
            if not in_norm or not s or s.startswith("#"):
                continue
            if s.startswith("INLINE:"):
                in_inline = True
                toks.append(s.split(":", 1)[1].strip())
                continue
            if s[:2] in ("L1", "L2", "L3", "L4", "L5", "L6"):
                body = s.split(":", 1)[1].strip()
                toks.extend(body.split())
    # sanity: every token must be a single char
    bad = [t for t in toks if len(t) != 1]
    assert not bad, f"multi-char tokens: {bad}"
    return toks

# ---------------------------------------------------------------- anneal ---
def score_text(text, logp, floor):
    s = 0.0
    for i in range(len(text) - 3):
        s += logp.get(text[i:i+4], floor)
    return s

def decode(toks, key):
    return "".join(key[t] for t in toks)

def anneal(toks, logp, floor, seed, iters=40000, t0=20.0, t1=0.1):
    rng = random.Random(seed)
    symbols = sorted(set(toks))
    key = {s: rng.choice(PLAINTEXT_ALPHA) for s in symbols}
    cur_txt = decode(toks, key)
    cur = score_text(cur_txt, logp, floor)
    best_key, best = dict(key), cur
    for it in range(iters):
        T = t0 * (t1 / t0) ** (it / iters)
        s = rng.choice(symbols)
        old = key[s]
        if rng.random() < 0.5:
            new = rng.choice(PLAINTEXT_ALPHA)
        else:  # swap two symbols' images
            s2 = rng.choice(symbols)
            new = key[s2]
            key[s], key[s2] = new, old
            cand_txt = decode(toks, key)
            cand = score_text(cand_txt, logp, floor)
            if cand >= cur or rng.random() < math.exp((cand - cur) / T):
                cur = cand
                if cand > best:
                    best, best_key = cand, dict(key)
            else:
                key[s], key[s2] = old, new
            continue
        key[s] = new
        cand_txt = decode(toks, key)
        cand = score_text(cand_txt, logp, floor)
        if cand >= cur or rng.random() < math.exp((cand - cur) / T):
            cur = cand
            if cand > best:
                best, best_key = cand, dict(key)
        else:
            key[s] = old
    return best, best_key, decode(toks, best_key)

# ------------------------------------------------------------------ main ---
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--build-model", action="store_true")
    ap.add_argument("--restarts", type=int, default=25)
    ap.add_argument("--iters", type=int, default=40000)
    ap.add_argument("--seed", type=int, default=15670427)
    args = ap.parse_args()

    toks = load_cipher()
    from collections import Counter
    freq = Counter(toks)
    n = len(toks)
    print(f"cipher tokens: {n}  distinct symbols: {len(freq)}")
    print("top symbols:", " ".join(f"{s}:{c}" for s, c in freq.most_common(12)))

    if args.stats:
        return

    logp, floor, meta = load_model()
    print(f"quadgram model: {meta['distinct_quadgrams']} distinct quads from "
          f"{meta['corpus_chars']} corpus chars "
          f"({os.path.basename(CORPUS_FILE)})")

    if args.build_model:
        print("model cached at", MODEL_CACHE)
        return

    # unicity math (work-order rule of thumb: ~28 * alphabet-size chars needed)
    need = 28 * len(freq)
    print(f"unicity check: have {n} tokens, rule-of-thumb needs ~{need} "
          f"(28 x {len(freq)} symbols) -> {'ENOUGH' if n >= need else 'TOO SHORT'}")

    best_overall, best_key, best_txt = -1e18, None, None
    for r in range(args.restarts):
        b, k, t = anneal(toks, logp, floor, args.seed + r, iters=args.iters)
        print(f"restart {r+1:2d}/{args.restarts}  score={b:10.2f}  "
              f"plain={t[:60]}", flush=True)
        if b > best_overall:
            best_overall, best_key, best_txt = b, k, t
    print("=" * 70)
    print(f"BEST score: {best_overall:.2f} over {args.restarts} restarts x "
          f"{args.iters} iters")
    print("BEST key:", " ".join(f"{s}->{best_key[s]}" for s in sorted(best_key)))
    print("BEST plaintext guess:")
    print(best_txt)

if __name__ == "__main__":
    main()
