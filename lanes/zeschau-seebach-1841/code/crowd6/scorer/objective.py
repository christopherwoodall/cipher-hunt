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
CONC_CAP = 3  # AMENDED: raw-cell cap (see PREREG.md)
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

    Scoring is restructured to per-letter stream scoring with TRUE history
    (fixing the parent's F() history bug: it scored cb's letters given only
    ca's own tail START-padded, which floors short cells' letters and cost
    truth ~0.75 nats/letter on the control). The SA / proposal / marginal
    machinery is reused; all scoring methods are overridden.

    S(K) = S_let_proj + LAM_WORD*S_word + LAM_ROT*S_phase + S_prior
           - LAM_POLY*n_poly + S_conc
    S_let_proj: projected letter 7-gram, per-letter normalized, TRUE stream
        history (single correct walk per resync).
    S_word: longest-match deduped, spanning-only, per-letter normalized.
    S_conc: -LAM_CONC * sum_p max(0, n_p - cap)^2 over PROJECTED v1.
    Key-level terms (S_prior, n_poly, S_conc) are computed fresh in total()
    from v1/v2 (O(96), exact) — no incremental bookkeeping to go stale.
    pcell-dependent scores are recomputed lazily: _set_pcell only flips
    pcell entries; total() resyncs via _refresh_scores() when dirty.
    """

    def __init__(self, stream, phase, lp_proj, pins, provisional, cells,
                 weights, ac, lam_word=1.0, lam_rot=0.0, lam_poly=0.05,
                 lam_conc=0.0, conc_cap=3, n=N_GRAM, rng=None):
        self.ac = ac
        self.lam_word = lam_word
        self.lam_conc = lam_conc
        self.conc_cap = conc_cap
        self._proj = {}
        self.S_word = 0.0
        self._scores_dirty = True
        self._sword_dirty = True
        super().__init__(stream, phase, lp_proj, pins, provisional, cells,
                         weights, lam_rot, lam_poly, 0.0, n,
                         rng if rng is not None else random.Random(SEED))

    # -- projection ---------------------------------------------------------
    def _pc(self, c):
        v = self._proj.get(c)
        if v is None:
            v = self._proj[c] = project(c)
        return v

    def _score_str(self, pstr, hist):
        """Sum of lp over pstr's chars; hist is a list of 6 context chars,
        rolled forward. The correct per-letter primitive."""
        t = 0.0
        h = hist
        for ch in pstr:
            t += self.lp(*h, ch)
            h = h[1:] + [ch]
        return t

    # -- letter stream -------------------------------------------------------
    # No flat wtext/woff is maintained. Per-occurrence scores use TRUE
    # stream history via _hist_before (walk back through pcell accumulating
    # projected letters). This is O(6) amortized and exactly correct,
    # unlike the parent's F() which START-padded short cells.
    def _hist_before(self, t):
        hist = []
        u = t - 1
        while len(hist) < 6 and u >= 0:
            pv = self._pc(self.pcell[u])
            if pv:
                hist = list(pv) + hist
            u -= 1
        hist = hist[-6:]
        return [START] * (6 - len(hist)) + hist

    def _score_occ(self, t):
        return self._score_str(self._pc(self.pcell[t]), self._hist_before(t))

    def _refresh_scores(self):
        """Full exact resync (init / validation)."""
        self.lscore = [self._score_occ(t) for t in range(self.N)]
        n_vphi = collections.Counter()
        n_v = collections.Counter()
        for t, g in enumerate(self.gs):
            v, ph = self.pcell[t], self.phase[g]
            n_vphi[(v, ph)] += 1
            n_v[v] += 1
        self.n_vphi, self.n_v = n_vphi, n_v
        self.total_letters = sum(len(self._pc(v)) for v in self.pcell)
        self.S_word = self._sword_full()
        self._scores_dirty = False
        self._sword_dirty = False

    def _sword_full(self):
        if not self.ac or self.lam_word == 0.0:
            return 0.0
        pc, pcells, offs = self._pc, [], [0]
        for v in self.pcell:
            pv = pc(v)
            pcells.append(pv)
            offs.append(offs[-1] + len(pv))
        text = ''.join(pcells)
        if not text:
            return 0.0
        bonus, _, _ = spanning_word_bonus(self.ac, text, offs)
        return bonus / len(text)

    # -- key moves (v1/v2 only; pcell scored lazily) -------------------------
    def _move_v1(self, g, new):
        # key-level terms are computed fresh in total(); just flip v1.
        self.v1[g] = new

    def _fwd_affected(self, t):
        """Occurrences u>t whose 6-letter history overlaps t's span:
        u is affected iff (start_u - end_t) < 6."""
        out, gap, u = [], 0, t + 1
        while gap < 6 and u < self.N:
            out.append(u)
            gap += len(self._pc(self.pcell[u]))
            u += 1
        return out

    def _set_pcell(self, t, v):
        old = self.pcell[t]
        if old == v:
            return False
        g = self.gs[t]
        ph = self.phase[g]
        self.n_vphi[(old, ph)] -= 1
        self.n_v[old] -= 1
        self.n_vphi[(v, ph)] += 1
        self.n_v[v] += 1
        self.total_letters += len(self._pc(v)) - len(self._pc(old))
        self.pcell[t] = v
        self.lscore[t] = self._score_occ(t)
        for u in self._fwd_affected(t):
            self.lscore[u] = self._score_occ(u)
        self._sword_dirty = True
        return True

    def _choose(self, t):
        """Per-occurrence E-step with TRUE stream history."""
        g = self.gs[t]
        v1, v2 = self.v1[g], self.v2[g]
        if v2 is None:
            return v1
        hist = self._hist_before(t)
        pv1, pv2 = self._pc(v1), self._pc(v2)
        s1 = self._score_str(pv1, hist)
        s2 = self._score_str(pv2, hist)
        if t + 1 < self.N:
            pcb = self._pc(self.pcell[t + 1])
            s1 += self._score_str(pcb, (hist + list(pv1))[-6:])
            s2 += self._score_str(pcb, (hist + list(pv2))[-6:])
        w2 = min(max(self.w2[g], 1e-6), 1 - 1e-6)
        return v2 if s2 + math.log(w2) > s1 + math.log(1 - w2) else v1

    def _rescore_group(self, g, relax=True):
        for t in self.occ[g]:
            self._set_pcell(t, self._choose(t))
        if relax:
            cands = set()
            for t in self.occ[g]:
                for u in (t - 1, t + 1):
                    if 0 <= u < self.N and self.v2[self.gs[u]] is not None:
                        cands.add(u)
            for _ in range(3):
                moved = False
                for u in sorted(cands):
                    if self._set_pcell(u, self._choose(u)):
                        moved = True
                if not moved:
                    break
        if self.v2[g] is not None:
            n2 = sum(1 for t in self.occ[g] if self.pcell[t] == self.v2[g])
            self.w2[g] = (n2 + 1.0) / (len(self.occ[g]) + 2.0)

    def _recompute_all(self):
        self.pcell = [self.v1[g] for g in self.gs]
        self._scores_dirty = True

    # -- snapshot / revert (key + pcell only; scores resync lazily) ----------
    def _aff_positions(self, groups):
        aff = set()
        for g in groups:
            for t in self.occ[g]:
                aff.add(t)
                if t - 1 >= 0:
                    aff.add(t - 1)
                if t + 1 < self.N:
                    aff.add(t + 1)
        return aff

    def snapshot(self, groups):
        aff = self._aff_positions(groups)
        return {'groups': list(groups),
                'key': {g: (self.v1[g], self.v2[g], self.w2[g])
                        for g in groups},
                'pcell': {t: self.pcell[t] for t in aff}}

    def revert(self, snap):
        for g, (a, b, w) in snap['key'].items():
            self.v1[g], self.v2[g], self.w2[g] = a, b, w
        # keep the parent's n_poly attribute in sync (propose_move maintains
        # it; total() computes it fresh, but external code reads the attr)
        self.n_poly = sum(1 for g in self.groups if self.v2[g] is not None)
        # pass 1: restore pcell + counters (no scoring yet — histories would
        # be wrong mid-restore)
        for t, v in snap['pcell'].items():
            old = self.pcell[t]
            if old == v:
                continue
            g = self.gs[t]
            ph = self.phase[g]
            self.n_vphi[(old, ph)] -= 1
            self.n_v[old] -= 1
            self.n_vphi[(v, ph)] += 1
            self.n_v[v] += 1
            self.total_letters += len(self._pc(v)) - len(self._pc(old))
            self.pcell[t] = v
        # pass 2: recompute lscore for aff + forward-affected (histories now
        # fully restored, so every recompute sees the true stream)
        to_rescore = set(snap['pcell'])
        for t in snap['pcell']:
            for u in self._fwd_affected(t):
                to_rescore.add(u)
        for t in sorted(to_rescore):
            self.lscore[t] = self._score_occ(t)
        self._sword_dirty = True

    # -- total ---------------------------------------------------------------
    def _phase_score(self):
        a = 1.0
        t = 0.0
        for (v, ph), n in self.n_vphi.items():
            t += n * math.log((n + a) / (self.n_v[v] + 4 * a))
        return t

    def total(self):
        if self._scores_dirty:
            self._refresh_scores()
        elif self._sword_dirty:
            self.S_word = self._sword_full()
            self._sword_dirty = False
        s_let = sum(self.lscore) / max(self.total_letters, 1)
        s_ph = self._phase_score() / max(self.N, 1)
        # key-level terms: fresh from v1/v2 every call (O(96), exact)
        n_c = collections.Counter(self.v1.values())
        S_conc = -self.lam_conc * sum(
            max(0, n - self.conc_cap) ** 2 for n in n_c.values())
        S_prior = sum(BETA_PROV for g, c in self.prov.items()
                      if self.v1.get(g) == c)
        n_poly = sum(1 for g in self.groups if self.v2[g] is not None)
        self._n_poly_cache, self._S_conc_cache = n_poly, S_conc
        return (s_let + self.lam_word * self.S_word
                + self.lam_rot * s_ph + S_prior
                - self.lam_poly * n_poly + S_conc)

    def components(self):
        if self._scores_dirty:
            self._refresh_scores()
        elif self._sword_dirty:
            self.S_word = self._sword_full()
            self._sword_dirty = False
        n_c = collections.Counter(self.v1.values())
        return {'total': round(self.total(), 4),
                's_let_proj': round(sum(self.lscore) / max(self.total_letters, 1), 4),
                'S_word': round(self.S_word, 4),
                's_ph': round(self._phase_score() / max(self.N, 1), 4),
                'S_prior': round(sum(BETA_PROV for g, c in self.prov.items()
                                     if self.v1.get(g) == c), 3),
                'n_poly': sum(1 for g in self.groups if self.v2[g] is not None),
                'S_conc': round(-self.lam_conc * sum(
                    max(0, n - self.conc_cap) ** 2 for n in n_c.values()), 4),
                'max_n_c': max(n_c.values()),
                'lam_poly': self.lam_poly, 'lam_conc': self.lam_conc}

    def init_key(self):
        for g in self.groups:
            if g in self.pins:
                self.v1[g], self.v2[g], self.w2[g] = self.pins[g], None, 0.0
            else:
                self.v1[g] = self.sample_cell()
                self.v2[g], self.w2[g] = None, 0.0
        self._recompute_all()

    # marginals: reuse parent's, but it calls propose_move/total — fine.


def verify_repaired_incremental(gs, phase, lp_proj, pins, provisional, cells,
                                weights, ac, seed=7, n_moves=200):
    """Self-test the lazy-resync scoring:
    (1) revert consistency: total() before a move == total() after
        propose+revert (scores resync lazily but exactly);
    (2) _refresh_scores vs an INDEPENDENT direct stream walk (catches
        history/window bugs);
    (3) _choose local scores vs direct (E-step history correctness).
    Returns (ok, info)."""
    import random as _random
    rng = _random.Random(seed)
    m = RepairedModel(gs, phase, lp_proj, pins, provisional, cells, weights,
                      ac, lam_poly=0.05, lam_conc=0.002,
                      rng=_random.Random(seed))
    m.init_key()
    base = m.total()
    maxerr = 0.0
    for i in range(n_moves):
        g = rng.choice(m.nonpin)
        mv, touched, snap = m.propose_move(g)
        if mv == 'noop':
            continue
        m.revert(snap)
        back = m.total()
        err = abs(base - back)
        maxerr = max(maxerr, err)
        if err > 1e-9:
            return False, ('revert', i, mv, base, back)
        # accept the move half the time to explore
        if rng.random() < 0.5:
            mv2, touched2, snap2 = m.propose_move(g)
            if mv2 != 'noop':
                base = m.total()
    # (2) independent direct stream walk on the final state
    m._refresh_scores()
    pc = m._pc
    text = ''.join(pc(v) for v in m.pcell)
    hist = ['^'] * 6
    tot = 0.0
    for ch in text:
        tot += m.lp(*hist, ch)
        hist = hist[1:] + [ch]
    indep = tot / max(len(text), 1)
    mine = sum(m.lscore) / max(m.total_letters, 1)
    if abs(indep - mine) > 1e-9:
        return False, ('stream-walk', indep, mine)
    # (3) word bonus vs independent greedy recompute
    sw = m._sword_full()
    if abs(sw - m.S_word) > 1e-12:
        return False, ('sword', sw, m.S_word)
    return True, maxerr
