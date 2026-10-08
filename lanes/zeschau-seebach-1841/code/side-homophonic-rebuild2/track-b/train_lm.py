#!/usr/bin/env python3
"""Track B: train a from-scratch numpy char-LSTM on era/register-matched French.

Implements PREREG.md (+ Amendments A1/A2) after red-team GO (R5, 2026-10-07).

Pipeline:
  1. Build training stream (14-file manifest; R5b guizot word-offset exclusion;
     WORD_RE tokenization; phonetics.project; spaceless projected stream;
     line-shuffle seed 20261007; 2% held-out by (file,line) hash).
  2. Gradient-check gate (finite differences on a toy model; halt if failed).
  3. Train with Adam, BPTT-64, batch-96, 2h HARD wall-clock stop.
  4. Write model.npz (best by held-out), loss_curve.json, manifest.json.

Deterministic: seeds 20261007; numpy 1.26.4; python 3.12.3; CPU only.
NO R5005 contact. Control/diagnostic only.
"""
import hashlib
import json
import math
import os
import re
import sys
import time
import unicodedata

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
REBUILD = os.path.join(LANE, 'code', 'side-homophonic-rebuild')
TRACK = HERE

sys.path.insert(0, os.path.join(REBUILD, 'solver'))
from phonetics import project  # noqa: E402  (library project(); verifier cross-checked)

SEED = 20261007
WORD_RE = re.compile(r"[a-zàâäéèêëîïôöùûüÿçœæ]+")  # byte-identical to build_lm.py:54
BUDGET_S = 6 * 3600  # A3 (2026-10-07): 2h -> 6h wall per round-2 work order
EVAL_EVERY = 300

# ---------------- R5b exclusion (Track A truth-plaintext slices, guizot word offsets)
GUIZOT_EXCLUDE = [(100000, 104000), (200000, 204000)]  # [start, end), 8000 words

FILES = [  # (relative path, is_gutenberg)
    ('code/side-period/corpus/guizot-memoires-t5-t6.txt', False),
    ('code/side-period/corpus/nesselrode-v7.txt', False),
    ('code/side-period/corpus/nesselrode-v8.txt', False),
    ('code/side-period/corpus/nesselrode-v9.txt', False),
    ('code/side-period/corpus/nesselrode-v10.txt', False),
    ('code/side-period/corpus/revue-deux-mondes-1841-q1.txt', False),
    ('code/side-period/corpus/revue-deux-mondes-1841-q2.txt', False),
    ('code/side-period/corpus/revue-deux-mondes-1841-q3.txt', False),
    ('code/side-period/corpus/revue-deux-mondes-1841-q4.txt', False),
    ('code/side-period/corpus/metternich-papiere-v4.txt', False),
    ('code/side-period/corpus/metternich-papiere-v6.txt', False),
    ('code/side-period/corpus/talleyrand-memoires-v1.txt', False),
    ('data/gutenberg-30513-tocqueville-t1.txt', True),
    ('data/gutenberg-30514-tocqueville-t2.txt', True),
]


def body_of(path, is_gutenberg):
    t = open(path, encoding='utf-8', errors='replace').read()
    if is_gutenberg:
        m1 = re.search(r'\*\*\* START OF.*?\*\*\*', t, re.S)
        m2 = re.search(r'\*\*\* END OF.*?\*\*\*', t, re.S)
        assert m1 and m2, f'no Gutenberg markers in {path}'
        return t[m1.end():m2.start()]
    return t


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def heldout_member(file_index, line_index):
    d = hashlib.sha256(f'{file_index}:{line_index}'.encode()).digest()
    return int.from_bytes(d[:8], 'big') % 50 == 0


def build_lines():
    """Return (train_word_lists, heldout_word_lists, per_file_stats, guizot_info).

    Each 'line' is a list of raw words. guizot (file 0) contributes 50-word
    pseudo-lines built AFTER the R5b word-offset exclusion.
    """
    train_lines, heldout_lines = [], []
    stats, guizot_info = [], {}
    for fi, (rel, is_gut) in enumerate(FILES):
        path = os.path.join(LANE, rel)
        body = body_of(path, is_gut)
        n_train_l = n_ho_l = n_train_w = n_ho_w = 0
        if fi == 0:
            # R5b: tokenize whole body, drop Track-A slices, re-chunk.
            words_all = WORD_RE.findall(body.lower())
            n_all = len(words_all)
            excl = set()
            for a, b in GUIZOT_EXCLUDE:
                assert 0 <= a < b <= n_all, 'exclusion range out of bounds'
                excl.update(range(a, b))
            assert len(excl) == sum(b - a for a, b in GUIZOT_EXCLUDE)
            # positive control: excluded ranges are non-empty real text
            heads = [' '.join(words_all[a:a + 8]) for a, _ in GUIZOT_EXCLUDE]
            used = [w for i, w in enumerate(words_all) if i not in excl]
            assert len(used) == n_all - len(excl)
            assert set(range(n_all)).difference(excl).isdisjoint(excl)
            guizot_info = {
                'n_words_total': n_all, 'n_words_excluded': len(excl),
                'n_words_used': len(used), 'excluded_heads': heads,
                'ranges': GUIZOT_EXCLUDE,
            }
            pseudo = [used[i:i + 50] for i in range(0, len(used), 50)]
            for li, wl in enumerate(pseudo):
                if heldout_member(fi, li):
                    heldout_lines.append(wl)
                    n_ho_l += 1
                    n_ho_w += len(wl)
                else:
                    train_lines.append(wl)
                    n_train_l += 1
                    n_train_w += len(wl)
        else:
            for li, raw in enumerate(body.split('\n')):
                wl = WORD_RE.findall(raw.lower())
                if not wl:
                    continue
                if heldout_member(fi, li):
                    heldout_lines.append(wl)
                    n_ho_l += 1
                    n_ho_w += len(wl)
                else:
                    train_lines.append(wl)
                    n_train_l += 1
                    n_train_w += len(wl)
        stats.append({'file': rel, 'sha256': sha256_file(path),
                      'train_lines': n_train_l, 'heldout_lines': n_ho_l,
                      'train_words': n_train_w, 'heldout_words': n_ho_w})
    return train_lines, heldout_lines, stats, guizot_info


def words_to_ids(word_lists, c2i):
    """Project word lists -> flat int array of alphabet ids (spaceless)."""
    out = []
    alpha = set(c2i)
    for wl in word_lists:
        for w in wl:
            p = project(w)
            for ch in p:
                assert ch in alpha, f'alphabet violation: {ch!r} from {w!r}'
                out.append(c2i[ch])
    return np.array(out, dtype=np.int32)


# ------------------------------------------------------------------ model
class CharLSTM:
    """Single-layer char LSTM, numpy float32. x: (T,B) int ids."""

    def __init__(self, V, H, seed, dt=np.float32):
        self.V, self.H = V, H
        self.dt = dt
        rng = np.random.default_rng(seed)

        def xav(fin, fout):
            lim = math.sqrt(6.0 / (fin + fout))
            return rng.uniform(-lim, lim, size=(fin, fout)).astype(self.dt)

        self.Wx = xav(V, 4 * H)
        self.Wh = xav(H, 4 * H)
        self.b = np.zeros(4 * H, dtype=self.dt)
        self.b[H:2 * H] = 1.0  # forget-gate bias
        self.Wy = xav(H, V)
        self.by = np.zeros(V, dtype=self.dt)
        self.pnames = ['Wx', 'Wh', 'b', 'Wy', 'by']

    def zero_state(self, B):
        return (np.zeros((B, self.H), self.dt),
                np.zeros((B, self.H), self.dt))

    @staticmethod
    def _sig(z):
        return 1.0 / (1.0 + np.exp(-z))

    def forward(self, x, h0, c0):
        T, B = x.shape
        H = self.H
        xe = self.Wx[x]                      # (T,B,4H) embedding lookup
        h = np.empty((T + 1, B, H), self.dt)
        c = np.empty((T + 1, B, H), self.dt)
        h[0] = h0
        c[0] = c0
        igo = np.empty((T, B, 4 * H), self.dt)
        tanhc = np.empty((T, B, H), self.dt)
        for t in range(T):
            z = xe[t] + h[t] @ self.Wh + self.b
            i, f, g, o = np.split(z, 4, axis=1)
            i = self._sig(i)
            f = self._sig(f)
            g = np.tanh(g)
            o = self._sig(o)
            c[t + 1] = f * c[t] + i * g
            tc = np.tanh(c[t + 1])
            h[t + 1] = o * tc
            igo[t] = np.concatenate([i, f, g, o], axis=1)
            tanhc[t] = tc
        logits = h[1:] @ self.Wy + self.by   # (T,B,V)
        m = logits.max(axis=2, keepdims=True)
        e = np.exp(logits - m)
        logp = logits - m - np.log(e.sum(axis=2, keepdims=True))
        return logp, (x, xe, h, c, igo, tanhc, logp), (h[T], c[T])

    def loss_and_grad(self, x, y, h0, c0):
        T, B = x.shape
        H, V = self.H, self.V
        logp, cache, _ = self.forward(x, h0, c0)
        x, xe, h, c, igo, tanhc, _ = cache
        flat = logp.reshape(-1, V)
        tgt = y.reshape(-1)
        nll = -float(flat[np.arange(T * B), tgt].mean())
        # --- backward ---
        dlog = np.exp(logp)                  # softmax probs (recompute; cheap)
        dlog = dlog.reshape(-1, V)
        dlog[np.arange(T * B), tgt] -= 1.0
        dlog /= (T * B)
        dlog = dlog.reshape(T, B, V)
        dWy = np.tensordot(h[1:].reshape(-1, H), dlog.reshape(-1, V),
                           axes=([0], [0]))
        dby = dlog.sum(axis=(0, 1))
        dh = dlog.reshape(T, B, V) @ self.Wy.T      # (T,B,H)
        dWx = np.zeros_like(self.Wx)
        dWh = np.zeros_like(self.Wh)
        db = np.zeros_like(self.b)
        dh_next = np.zeros((B, H), self.dt)
        dc_next = np.zeros((B, H), self.dt)
        for t in range(T - 1, -1, -1):
            dh_t = dh[t] + dh_next
            i, f, g, o = np.split(igo[t], 4, axis=1)
            tc = tanhc[t]
            do = dh_t * tc * o * (1 - o)
            dc = dh_t * o * (1 - tc * tc) + dc_next
            df = dc * c[t] * f * (1 - f)
            di = dc * g * i * (1 - i)
            dg = dc * i * (1 - g * g)
            dz = np.concatenate([di, df, dg, do], axis=1)
            np.add.at(dWx, x[t], dz)
            dWh += h[t].T @ dz
            db += dz.sum(axis=0)
            dh_next = dz @ self.Wh.T
            dc_next = dc * f
        grads = {'Wx': dWx, 'Wh': dWh, 'b': db, 'Wy': dWy, 'by': dby}
        return nll, grads, (h[T], c[T])

    def get_params(self):
        return {k: getattr(self, k) for k in self.pnames}

    def set_params(self, d):
        for k in self.pnames:
            getattr(self, k)[:] = d[k]


class Adam:
    def __init__(self, params, lr=2e-3, b1=0.9, b2=0.999, eps=1e-8):
        self.lr = lr
        self.b1, self.b2, self.eps = b1, b2, eps
        self.m = {k: np.zeros_like(v) for k, v in params.items()}
        self.v = {k: np.zeros_like(v) for k, v in params.items()}
        self.t = 0

    def step(self, params, grads, clip=5.0):
        # global-norm clip
        tot = math.sqrt(sum(float((g * g).sum()) for g in grads.values()))
        scale = min(1.0, clip / max(tot, 1e-12))
        self.t += 1
        for k in params:
            g = grads[k] * scale
            self.m[k] = self.b1 * self.m[k] + (1 - self.b1) * g
            self.v[k] = self.b2 * self.v[k] + (1 - self.b2) * g * g
            mh = self.m[k] / (1 - self.b1 ** self.t)
            vh = self.v[k] / (1 - self.b2 ** self.t)
            params[k] -= self.lr * mh / (np.sqrt(vh) + self.eps)


def gradient_check():
    """Finite-difference gate on a toy model. Returns True iff passed."""
    V, H, T, B = 30, 8, 5, 2
    rng = np.random.default_rng(999)
    net = CharLSTM(V, H, seed=12345, dt=np.float64)
    x = rng.integers(0, V, size=(T, B))
    y = rng.integers(0, V, size=(T, B))
    h0 = rng.standard_normal((B, H)).astype(np.float64) * 0.1
    c0 = rng.standard_normal((B, H)).astype(np.float64) * 0.1

    def loss_fn():
        nll, _, _ = net.loss_and_grad(x, y, h0, c0)
        return nll

    _, grads, _ = net.loss_and_grad(x, y, h0, c0)
    worst = 0.0
    worst_key = None
    eps = 1e-6
    for k in net.pnames:
        p = getattr(net, k)
        g = grads[k]
        it = np.nditer(p, flags=['multi_index'])
        while not it.finished:
            ix = it.multi_index
            old = float(p[ix])
            p[ix] = old + eps
            lp = loss_fn()
            p[ix] = old - eps
            lm = loss_fn()
            p[ix] = old
            num = (lp - lm) / (2 * eps)
            ana = float(g[ix])
            rel = abs(num - ana) / max(1e-8, abs(num) + abs(ana))
            if rel > worst:
                worst, worst_key = rel, (k, ix)
            it.iternext()
    print(f'[gradcheck] worst rel err = {worst:.2e} at {worst_key}', flush=True)
    return worst < 1e-4


# ------------------------------------------------------------------ training
def heldout_nll(net, Harr, block=2048):
    """Per-char NLL over held-out stream (B=1, carried state)."""
    B = 1
    h, c = net.zero_state(B)
    tot_lp, tot_n = 0.0, 0
    L = len(Harr)
    for s in range(0, L - 1, block):
        e = min(s + block, L - 1)
        x = Harr[s:e].reshape(-1, B)
        y = Harr[s + 1:e + 1].reshape(-1, B)
        logp, _, (h, c) = net.forward(x, h, c)
        flat = logp.reshape(-1, net.V)
        tot_lp += float(flat[np.arange(len(y.ravel())), y.ravel()].sum())
        tot_n += len(y.ravel())
    return -tot_lp / tot_n


def main():
    t_wall0 = time.time()
    # --- alphabet (fixed, from lm_ref) ---
    lm_meta = json.load(open(os.path.join(REBUILD, 'solver', 'lm_ref', 'lm.json')))['meta']
    alphabet = lm_meta['alphabet']
    assert len(alphabet) == 30
    c2i = {ch: i for i, ch in enumerate(alphabet)}
    V = len(alphabet)

    # --- data ---
    print('[data] building line pool...', flush=True)
    train_lines, heldout_lines, stats, guizot_info = build_lines()
    rng = np.random.default_rng(SEED)
    order = np.arange(len(train_lines))
    rng.shuffle(order)
    train_lines = [train_lines[i] for i in order]
    print(f'[data] train lines={len(train_lines)} heldout lines={len(heldout_lines)}',
          flush=True)
    S = words_to_ids(train_lines, c2i)
    Harr = words_to_ids(heldout_lines, c2i)
    print(f'[data] train chars={len(S)} heldout chars={len(Harr)}', flush=True)
    n_train_chars = int(len(S))
    n_ho_chars = int(len(Harr))
    per_file_chars = []
    # per-file projected char counts (recompute cheaply per file group is
    # expensive; record word counts from stats + totals here)
    for st in stats:
        per_file_chars.append({k: st[k] for k in
                               ('file', 'sha256', 'train_lines', 'heldout_lines',
                                'train_words', 'heldout_words')})

    # --- gradient gate ---
    print('[gate] running gradient check...', flush=True)
    if not gradient_check():
        print('[gate] GRADIENT CHECK FAILED — no training. See PREREG §2.',
              flush=True)
        sys.exit(42)

    # --- model & optimizer ---
    H, T, B = 96, 64, 96
    net = CharLSTM(V, H, seed=SEED)
    opt = Adam(net.get_params(), lr=2e-3)
    chunk = len(S) // B
    n_steps = (chunk - 1) // T
    print(f'[train] H={H} T={T} B={B} steps/epoch={n_steps}', flush=True)

    curve = []
    best = {'heldout': float('inf'), 'params': None, 'update': -1}
    h, c = net.zero_state(B)
    ema = None
    update = 0
    stop_reason = 'budget'
    t_start = time.time()
    prev_held = None
    max_updates = n_steps * 12  # A3: <=12 epochs (was 3); convergence-or-6h-wall
    # --- resume ---
    ckpt_npz = os.path.join(TRACK, 'ckpt.npz')
    ckpt_json = os.path.join(TRACK, 'ckpt.json')
    resume_update = 0
    if '--resume' in sys.argv and os.path.exists(ckpt_json):
        ck = json.load(open(ckpt_json))
        resume_update = int(ck['update'])
        z = np.load(ckpt_npz)
        net.set_params({k: z[k] for k in net.pnames})
        best = {'heldout': float(ck['best_heldout']),
                'params': {k: z['best_' + k] for k in net.pnames},
                'update': int(ck['best_update'])}
        curve = ck['curve']
        ema = float(ck['ema']) if ck['ema'] is not None else None
        prev_held = float(ck['prev_held']) if ck['prev_held'] is not None else None
        opt.lr = float(ck['lr'])
        print(f"[resume] loaded ckpt at update={resume_update} "
              f"best_held={best['heldout']:.4f}", flush=True)

    def save_ckpt():
        np.savez(ckpt_npz,
                 **{k: net.get_params()[k] for k in net.pnames},
                 **{'best_' + k: best['params'][k] for k in net.pnames})
        json.dump({'update': update, 'best_heldout': best['heldout'],
                   'best_update': best['update'], 'curve': curve,
                   'ema': ema, 'prev_held': prev_held, 'lr': opt.lr},
                  open(ckpt_json, 'w'))

    for epoch in range(12):  # A3: was range(3)
        for k in range(n_steps):
            update += 1
            if update <= resume_update:
                continue  # already done pre-resume; (h,c) reset, documented
            xs = np.empty((T, B), dtype=np.int32)
            ys = np.empty((T, B), dtype=np.int32)
            for b in range(B):
                s0 = b * chunk + k * T
                xs[:, b] = S[s0:s0 + T]
                ys[:, b] = S[s0 + 1:s0 + T + 1]
            nll, grads, (h, c) = net.loss_and_grad(xs, ys, h, c)
            opt.step(net.get_params(), grads)
            ema = nll if ema is None else 0.98 * ema + 0.02 * nll
            if update % 50 == 0:
                print(f'[hb] upd={update} ema={ema:.4f} '
                      f'wall={time.time()-t_start:.0f}s', flush=True)
            if update % EVAL_EVERY == 0 or update == max_updates:
                hnll = heldout_nll(net, Harr)
                wall = time.time() - t_start
                # LR schedule: halve on plateau (patience 1)
                if prev_held is not None and hnll >= prev_held and opt.lr > 2e-4:
                    opt.lr = max(2e-4, opt.lr / 2)
                    print(f'[train] plateau: lr -> {opt.lr:.1e}', flush=True)
                prev_held = hnll
                if hnll < best['heldout']:
                    best = {'heldout': hnll,
                            'params': {kk: vv.copy() for kk, vv in
                                       net.get_params().items()},
                            'update': update}
                rec = {'update': update, 'epoch': epoch,
                       'chars_seen': update * T * B,
                       'train_nll_ema': round(float(ema), 4),
                       'heldout_nll': round(float(hnll), 4),
                       'lr': opt.lr, 'wall_s': round(wall, 1)}
                curve.append(rec)
                print(f"[train] upd={update} ep={epoch} chars={update*T*B} "
                      f"train_ema={ema:.4f} held={hnll:.4f} lr={opt.lr:.0e} "
                      f"wall={wall:.0f}s", flush=True)
                save_ckpt()
            if time.time() - t_start > BUDGET_S:
                stop_reason = 'wallclock_2h'
                break
            if update >= max_updates:
                stop_reason = 'max_updates_12epochs'
                break
        # reset state at epoch boundary
        h, c = net.zero_state(B)
        if stop_reason != 'budget':
            break

    wall_total = time.time() - t_wall0
    print(f'[train] done: reason={stop_reason} updates={update} '
          f'wall_total={wall_total:.0f}s', flush=True)

    # --- save best ---
    assert best['params'] is not None
    net.set_params(best['params'])
    final_held = heldout_nll(net, Harr)
    np.savez(os.path.join(TRACK, 'model.npz'),
             **{k: v for k, v in net.get_params().items()},
             H=np.array(H), V=np.array(V))
    json.dump(curve, open(os.path.join(TRACK, 'loss_curve.json'), 'w'), indent=1)
    manifest = {
        'track': 'b', 'seed': SEED,
        'go_authorization': 'redteam/RULINGS.md R5 (2026-10-07)',
        'files': per_file_chars,
        'n_train_chars': n_train_chars, 'n_heldout_chars': n_ho_chars,
        'guizot_r5b_exclusion': guizot_info,
        'lesmis_scan': {'rule': 'word-8-grams on NFD-stripped trainable bodies',
                        'hits_total': 13,
                        'script': 'track-b/scan_lesmis_overlap.py'},
        'model': {'arch': 'char-LSTM 1 layer', 'H': H, 'T': T, 'B': B,
                  'params': sum(int(v.size) for v in net.get_params().values()),
                  'optimizer': 'Adam lr=2e-3 halve-on-plateau floor 2e-4, clip 5.0'},
        'training': {'updates': update, 'chars_seen': update * T * B,
                     'stop_reason': stop_reason,
                     'wall_s_total': round(wall_total, 1),
                     'best_update': best['update'],
                     'best_heldout_nll': round(float(best['heldout']), 4),
                     'final_heldout_nll': round(float(final_held), 4)},
        'pins': {'python': '3.12.3', 'numpy': '1.26.4', 'torch': None,
                 'cpu_threads': 2},
        'r5005_contact': False,
    }
    json.dump(manifest, open(os.path.join(TRACK, 'manifest.json'), 'w'), indent=1)
    print('[done] model.npz loss_curve.json manifest.json written', flush=True)


if __name__ == '__main__':
    main()
