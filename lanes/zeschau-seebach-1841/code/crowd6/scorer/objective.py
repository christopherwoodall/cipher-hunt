#!/usr/bin/env python3
"""REPAIRED JOINT OBJECTIVE — round 6, scorer-smith (N36 ordered import list).

Lane: zeschau-seebach-1841. Repairs the round-4 joint engine's objective
(code/crowd4/joint_engine.py) per the ordered import list in
code/crowd5/scorer_identifiability.md §5 / homophonic_synergy.md:

  (1) lam_poly scale fix — penalty commensurate with the per-letter letter
      term (was ~100x over scale: configured 10, crossover at < 0.09);
  (2) phonetic projection — side-homophonic's phonetics.py, imported
      verbatim (absorbs ~0.33 nats/letter of by-ear noise);
  (3) spanning word bonus — with the D2 repair (longest-match dedupe;
      the side fleet's frozen overlapping-hit S_word is control-broken and
      is NOT imported verbatim);
  (4) concentration penalty — over PROJECTED values (accent variants
      collude), calibrated on the observed collapse, no truth labels.

S(K) = S_let_proj + LAM_WORD*S_word + LAM_ROT*S_phase + S_prior
       - LAM_POLY*n_poly + S_conc

All likelihood terms are per-letter (or per-position) normalized, so the
key-level penalties are on a commensurate scale. Subclasses JointModel to
reuse the tested annealing / marginal / snapshot machinery; only the
scoring terms change.
"""
import bisect
import collections
import json
import math
import os
import random
import sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd2'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'scorer'))
from joint_engine import JointModel, PINS  # noqa: E402 (tested SA machinery)
from phonetics import project  # noqa: E402 (imported, self-test passes)

SEED = 1841
N_GRAM = 7
ALPHA_NG = 0.1
BETA_PROV = 0.2
CONC_CAP = 6
START = '^'


# ---------------------------------------------------------------- projected LM
def build_letter_ngram_proj(toks, n=N_GRAM, exclude=None):
    """Era letter n-gram log-probs over PHONETICALLY PROJECTED text.

    toks: lane token list (M['toks']); exclude=(a,b) word-span to skip
    (control independence — same span the raw build excludes).
    Projection is applied per WORD (silent-final rules are word-final),
    then concatenated spacelessly — mirroring the raw-letter build.
    """
    words = toks[:exclude[0]] + toks[exclude[1]:] if exclude else list(toks)
    letters = ''.join(project(w) for w in words)
    ngram = collections.Counter()
    n1 = collections.Counter()
    V = len(set(letters)) + 1
    p0 = START * (n - 1) + letters
    for i in range(len(p0) - n + 1):
        ng = tuple(p0[i:i + n])
        ngram[ng] += 1
        n1[ng[:-1]] += 1

    def lp(*args):
        ctx, ch = args[:-1], args[-1]
        ng = ctx + (ch,)
        return math.log((ngram.get(ng, 0) + ALPHA_NG) /
                        (n1.get(ctx, 0) + ALPHA_NG * V))
    return lp, len(letters)


def build_lexicon_proj(toks, exclude=None, minlen=4, minfreq=3, top=40000):
    """Projected word lexicon mirroring side-homophonic build_lm.py's recipe:
    word freqs (span-excluded) -> f>=minfreq -> project -> len>=minlen ->
    dedup summing freq -> top by freq -> weight log(1+freq).

    Uses the LANE tokenizer (M['toks']) so the control-span exclusion is
    exact; the recipe (thresholds, weighting) is the imported one.
    Returns [(projected_word, weight)].
    """
    words = toks[:exclude[0]] + toks[exclude[1]:] if exclude else list(toks)
    wfreq = collections.Counter(words)
    lex = collections.Counter()
    for w, f in wfreq.items():
        if f < minfreq:
            continue
        pw = project(w)
        if len(pw) >= minlen:
            lex[pw] += f
    return [(pw, math.log1p(f)) for pw, f in lex.most_common(top)]


# ---------------------------------------------------------------- Aho-Corasick with match positions
class AhoCorasick:
    """Aho-Corasick emitting (start, end, weight) per match.

    Per-node output lists are propagated along fail links at build time,
    so scan() reports every pattern ending at each position (not just a
    summed weight — the D2 repair needs individual matches for
    longest-match dedupe).

    The transition function is densified over the projected alphabet
    (list-of-lists) so the per-character step is two list indexings —
    fast enough to run inside the anneal loop.
    """

    def __init__(self, patterns):
        self.max_len = 0
        nxt = [{}]
        fail = [0]
        out = [[]]  # node -> [(length, weight)]
        for s, w in patterns:
            if len(s) > self.max_len:
                self.max_len = len(s)
            node = 0
            for ch in s:
                d = nxt[node].get(ch)
                if d is None:
                    d = len(nxt)
                    nxt[node][ch] = d
                    nxt.append({})
                    fail.append(0)
                    out.append([])
                node = d
            out[node].append((len(s), w))
        q = collections.deque()
        for ch, d in nxt[0].items():
            fail[d] = 0
            q.append(d)
        while q:
            r = q.popleft()
            for ch, d in nxt[r].items():
                q.append(d)
                f = fail[r]
                while f and ch not in nxt[f]:
                    f = fail[f]
                fail[d] = nxt[f].get(ch, 0)
                out[d] += out[fail[d]]
        # densify over the alphabet actually used by the patterns
        alpha = sorted({ch for s, _ in patterns for ch in s})
        self._alpha = {ch: i for i, ch in enumerate(alpha)}
        A = len(alpha)
        self._trans = [[0] * A for _ in range(len(nxt))]
        self._out = out
        for s in range(len(nxt)):
            row = self._trans[s]
            for ch, i in self._alpha.items():
                ns = s
                while ns and ch not in nxt[ns]:
                    ns = fail[ns]
                row[i] = nxt[ns].get(ch, 0)
        self.n_states = len(nxt)

    def scan(self, s):
        """Yield (start, end, weight) for every pattern match in s."""
        trans, out, amap = self._trans, self._out, self._alpha
        node = 0
        for i, ch in enumerate(s):
            j = amap.get(ch)
            if j is None:
                node = 0
                continue
            node = trans[node][j]
            o = out[node]
            if o:
                for ln, w in o:
                    yield (i - ln + 1, i + 1, w)


def spanning_word_bonus(ac, text, boundaries):
    """Greedy longest-match word bonus, spanning-only (the D2 repair).

    ac: AhoCorasick over (projected_word, weight).
    text: projected letter stream (str).
    boundaries: sorted list of occurrence-boundary letter offsets
        (offsets[0]=0 ... offsets[N]=len(text)).
    Left-to-right: at each uncovered position take the LONGEST match
    starting there (kills the 'meme'/'eme'/'me' stacking — D2); a taken
    match counts iff it spans >=1 value boundary (spanning-only: a word
    inside one value is not decipherment evidence).
    Returns (bonus_weight_sum, n_taken, n_spanning).
    """
    by_start = collections.defaultdict(list)
    for st, en, w in ac.scan(text):
        by_start[st].append((en, w))
    # longest match per start
    longest = {st: max(v, key=lambda x: (x[0], x[1])) for st, v in by_start.items()}
    bonus, n_taken, n_span = 0.0, 0, 0
    covered_until = 0
    bi = 0
    nb = len(boundaries)
    for st in sorted(longest):
        if st < covered_until:
            continue
        en, w = longest[st]
        covered_until = en
        n_taken += 1
        # spanning check: any boundary strictly inside (st, en)
        while bi < nb and boundaries[bi] <= st:
            bi += 1
        if bi < nb and boundaries[bi] < en:
            bonus += w
            n_span += 1
    return bonus, n_taken, n_span


# ---------------------------------------------------------------- repaired model
class RepairedModel(JointModel):
    """JointModel with the repaired objective.

    Differences from the parent (scoring only; SA/marginals/snapshot
    machinery reused):
      - letter n-gram scores PROJECTED letters (F via _letters override);
      - total_letters counts PROJECTED letters;
      - total() adds LAM_WORD * S_word (longest-match deduped,
        spanning-only, per-letter normalized; full exact recompute) and
        S_conc (projected-value concentration penalty, incremental);
      - lam_hom forced 0.0 (superseded by S_conc).
    """

    def __init__(self, stream, phase, lp_proj, pins, provisional, cells,
                 weights, ac, lam_word=1.0, lam_rot=0.0, lam_poly=0.05,
                 lam_conc=0.0, conc_cap=CONC_CAP, n=N_GRAM, rng=None):
        self.ac = ac
        self.lam_word = lam_word
        self.lam_conc = lam_conc
        self.conc_cap = conc_cap
        self._proj = {}
        self.n_cp = collections.Counter()
        self.S_conc = 0.0
        self.S_word = 0.0
        super().__init__(stream, phase, lp_proj, pins, provisional, cells,
                         weights, lam_rot, lam_poly, 0.0, n,
                         rng if rng is not None else random.Random(SEED))

    # -- projection helpers ------------------------------------------------
    def _pc(self, c):
        v = self._proj.get(c)
        if v is None:
            v = self._proj[c] = project(c)
        return v

    def _letters(self, c):
        # override: score projected letters (parent caches list(c))
        return list(self._pc(c))

    def _plen(self, c):
        return len(self._pc(c))

    # -- concentration penalty (incremental, over projected v1) ------------
    def _conc_pen(self, n):
        return self.lam_conc * max(0, n - self.conc_cap) ** 2

    def _move_v1(self, g, new):
        old = self.v1[g]
        if old == new:
            return
        # parent's raw-cell bookkeeping (S_hom=0, harmless)
        super()._move_v1(g, new)
        # projected concentration bookkeeping
        po, pn = self._pc(old), self._pc(new)
        if po != pn:
            self.S_conc += self._conc_pen(self.n_cp[po])
            self.n_cp[po] -= 1
            self.S_conc -= self._conc_pen(self.n_cp[po])
            self.S_conc += self._conc_pen(self.n_cp[pn])
            self.n_cp[pn] += 1
            self.S_conc -= self._conc_pen(self.n_cp[pn])

    def _refresh_scores(self):
        super()._refresh_scores()
        # projected lengths (parent used raw lengths)
        self.total_letters = sum(self._plen(v) for v in self.pcell)
        # projected concentration (full rebuild)
        self.n_cp = collections.Counter(self._pc(v) for v in self.v1.values())
        self.S_conc = -sum(self._conc_pen(n) for n in self.n_cp.values())
        # word bonus (full exact recompute)
        self.S_word = self._sword_full()

    def _set_pcell(self, t, v):
        # override: total_letters counts PROJECTED letters (parent used raw)
        old = self.pcell[t]
        if old == v:
            return False
        g = self.gs[t]
        ph = self.phase[g]
        self.n_vphi[(old, ph)] -= 1
        self.n_v[old] -= 1
        self.n_vphi[(v, ph)] += 1
        self.n_v[v] += 1
        self.total_letters += self._plen(v) - self._plen(old)
        self.pcell[t] = v
        ca = self.pcell[t - 1] if t > 0 else START
        self.lscore[t] = self.F(ca, v)
        if t + 1 < self.N:
            self.lscore[t + 1] = self.F(v, self.pcell[t + 1])
        return True

    def _sword_full(self):
        """Exact spanning word bonus from the current pcell decode."""
        if not self.ac or self.lam_word == 0.0:
            return 0.0
        pcells = [self._pc(v) for v in self.pcell]
        text = ''.join(pcells)
        if not text:
            return 0.0
        boundaries = [0]
        o = 0
        for p in pcells:
            o += len(p)
            boundaries.append(o)
        bonus, _, _ = spanning_word_bonus(self.ac, text, boundaries)
        return bonus / len(text)  # per-letter normalized

    def total(self):
        # S_word is recomputed fresh on every call: it is a pure function
        # of pcell, and caching it across moves was a staleness bug
        # (components() rounding hid a 1e-4 drift). The dense AC keeps
        # this at a few ms.
        s_let = sum(self.lscore) / max(self.total_letters, 1)
        s_ph = self._phase_score() / max(self.N, 1)
        self.S_word = self._sword_full()
        return (s_let + self.lam_word * self.S_word
                + self.lam_rot * s_ph + self.S_prior
                - self.lam_poly * self.n_poly + self.S_conc)

    # -- snapshot / revert: parent misses n_cp/S_conc/S_word ----------------
    def snapshot(self, groups):
        snap = super().snapshot(groups)
        snap['n_cp'] = dict(self.n_cp)
        snap['S_conc'] = self.S_conc
        # S_word is a pure function of pcell; the snapshot already stores
        # the affected pcell entries, so the cached value restores exactly.
        snap['S_word'] = self.S_word
        return snap

    def revert(self, snap):
        super().revert(snap)
        self.n_cp = collections.Counter(snap['n_cp'])
        self.S_conc = snap['S_conc']
        self.S_word = snap['S_word']

    def components(self):
        return {'total': round(self.total(), 4),
                's_let_proj': round(sum(self.lscore) / max(self.total_letters, 1), 4),
                'S_word': round(self.S_word, 4),
                's_ph': round(self._phase_score() / max(self.N, 1), 4),
                'S_prior': round(self.S_prior, 3),
                'n_poly': self.n_poly,
                'S_conc': round(self.S_conc, 4),
                'lam_poly': self.lam_poly, 'lam_conc': self.lam_conc}


def verify_repaired_incremental(gs, phase, lp_proj, pins, provisional, cells,
                                weights, ac, seed=7, n_moves=200):
    """Self-test: incremental total() == full recompute after every move,
    INCLUDING the word bonus and concentration terms. Returns (ok, info)."""
    rng = random.Random(seed)
    m = RepairedModel(gs, phase, lp_proj, pins, provisional, cells, weights,
                      ac, lam_poly=0.05, lam_conc=0.002,
                      rng=random.Random(seed))
    m.init_key()
    maxerr = 0.0
    for i in range(n_moves):
        g = rng.choice(m.nonpin)
        mv, touched, snap = m.propose_move(g)
        if mv == 'noop':
            continue
        inc = m.total()
        # full recompute from scratch
        m._refresh_scores()
        full = m.total()
        # _refresh_scores recomputes S_word from pcell — but pcell itself is
        # incremental; cross-check S_word against a from-scratch build
        sw_check = m._sword_full()
        err = abs(inc - full) + abs(m.S_word - sw_check)
        maxerr = max(maxerr, err)
        if err > 1e-9:
            return False, (i, mv, inc, full, m.S_word, sw_check)
    return True, maxerr
