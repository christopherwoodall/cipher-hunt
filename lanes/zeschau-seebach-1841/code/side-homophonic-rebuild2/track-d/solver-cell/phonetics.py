#!/usr/bin/env python3
"""Phonetic projection pi for the Seebach homophonic solver (side fleet).

WHY THIS EXISTS
---------------
The encipherer spells BY EAR and cuts inconsistently (code/sidepath/
phonetic_rules.md R1-R9). A strict orthographic language model mis-scores the
true decipherment:
  - "prend" written "pre" (silent -d- dropped, R3 SOLID)
  - "personne" as per|so|nne AND pers|on|ne in one cipher (R2 SOLID)
  - mute final -e written as its own group 40 (R1 SOLID)
  - "erre" written 29+40 = er|e, single-r sound (R8 PROVISIONAL)
The projection maps the era corpus, the lexicon, AND the solver's decoded
stream into one shared phonetic-class alphabet. The language model is then
indifferent to the spelling variants the encipherer treats as identical.

DESIGN PRINCIPLES
-----------------
1. Deterministic; applied IDENTICALLY to corpus (LM training), lexicon, and
   every decoded value. Self-consistent by construction: any systematic
   choice affects both sides equally, so the true key still maximizes the
   objective.
2. Merge only same-sound spelling variants (au/eau->o, ou->u, ph->f ...).
   Never merge sounds the ear distinguishes.
3. DELETE only licensed silent finals (R3 SOLID for -d; the -s/-t/-x/-p/-b/-g
   generalization is R11 SPECULATIVE -- default ON, toggleable, graded
   PROVISIONAL below).
4. NEVER delete final -e (R1 SOLID: 40="e" is written) and never delete
   single-letter values (they are the letter tier: 82=m, 34=i, 40=e).
5. By-ear LOSSES (dropped nasals as in "prend"->"pre", vowel confusions like
   'e' for 'e-grave' inside "premiere") are NOT modelled -- they are noise
   the character n-gram absorbs, not signal. Modelling the encipherer's exact
   ear is a rabbit hole; tolerance beats imitation.

Each rule carries an evidence grade from the phonetic_rules.md legend:
SOLID / PROVISIONAL / SPECULATIVE.
"""

import re
import unicodedata

# ---------------------------------------------------------------------------
# Rule table: (name, grade, description). The implementation is project().
# ---------------------------------------------------------------------------
RULES = [
    ("lower+oe/ae", "SOLID",
     "lowercase; ligature oe->oe, ae->ae (orthographic variants)."),
    ("accents", "SOLID",
     "a-grave/circumflex->a; e-acute/grave/circumflex/diaeresis->e (MERGED: the "
     "ground-truth crib writes plain 'e' for e-grave inside 'premiere', so the "
     "encipherer's ear does not reliably distinguish e-open/e-closed); "
     "i-circumflex/diaeresis->i; o-circumflex->o; u-accents->u; c-cedilla->S "
     "(c-cedilla is always /s/)."),
    ("h-delete", "SOLID",
     "h is always silent in French; by-ear spelling never writes it."),
    ("digraphs", "SOLID",
     "eau,au->o; ai,ei->e; ou->u; ph->f; th->t; qu->k; ch->C (/sh/); "
     "gn->N (/ny/). Same-sound spelling variants merged; the encipherer "
     "hears one sound. h-digraphs precede h-deletion."),
    ("nasals", "PROVISIONAL",
     "ain,ein,ien,yen,oin->I; an,en,am,em->A; on,om->O; in->I; un,um->U -- "
     "but ONLY when not followed by a vowel or n/m (context-sensitive). "
     "'enfant'->AnfA and 'vent'->vA, but 'ennemi'->enemi, 'premier'->premier, "
     "'bonne'->bone. The guard is load-bearing: without it the ground-truth "
     "crib 'premiere' mis-projects to 'prAiere'. The vowel-class choice "
     "(A vs I) follows standard French; ambiguous spellings ('science' vs "
     "'chien') are normalized one way and the residue is n-gram noise."),
    ("y/w", "PROVISIONAL",
     "y->i; w->v. Overwhelmingly true in French loanwords."),
    ("x", "PROVISIONAL",
     "word-final x after a vowel deletes (deux->deu, six->si: the x is silent); "
     "else x->ks (axe->akse)."),
    ("geminates", "SOLID",
     "orthographic doubles collapse to one pronounced consonant (R8: 'erre' "
     "written er|e with a single r). EXCEPTION: ss->S, kept distinct from "
     "single s, because /s/ vs /z/ is a real sound distinction the ear keeps "
     "('poisson' vs 'poison')."),
    ("silent-finals", "PROVISIONAL",
     "word-final d,t,s,x,p,b,g,z delete AFTER A VOWEL/NASAL (R3 SOLID for -d "
     "in 'prend'->'pre'; the rest is the R11 generalization, SPECULATIVE as a "
     "discriminator but safe here: it is applied to BOTH sides, so it only "
     "removes a spelling choice the by-ear encipherer makes inconsistently). "
     "The vowel guard is load-bearing: without it, the consonant cluster 'st' "
     "(a real inventory value) deletes to '' -- an empty projection scores 0 "
     "and becomes a degenerate attractor (found 2026-10-07). NEVER touches "
     "final -e (R1), -r (29=er), -l, -m, -n, -f, -c, or single-letter values."),
]

ACCENT_MAP = {
    'à': 'a', 'â': 'a',
    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'î': 'i', 'ï': 'i', 'ÿ': 'i',
    'ô': 'o',
    'û': 'u', 'ü': 'u', 'ù': 'u',
    'ç': 'S',
}

# Phase A: context-free digraphs, longest-first. Nasal digraphs
# (ain/ein/ien/yen/oin) come before ai/ei so 'pain' -> pIn, not 'pen'.
# (ch/ph/th) MUST precede h-deletion.
DIGRAPHS_A = [
    ('eau', 'o'),
    ('ain', 'I'), ('ein', 'I'), ('ien', 'I'), ('yen', 'I'), ('oin', 'I'),
    ('au', 'o'), ('ai', 'e'), ('ei', 'e'), ('ou', 'u'),
    ('ch', 'C'), ('ph', 'f'), ('th', 't'), ('qu', 'k'), ('gn', 'N'),
]

# Phase B: context-sensitive nasals. Vowel+n/m is nasal ONLY when not
# followed by a vowel or n/m ("enfant"->AnfA, but "ennemi"->enemi,
# "premier"->premier, "bonne"->bone). Without the guard, the ground-truth
# crib 'premiere' mis-projects to 'prAiere'.
_NASAL_MAP = {'an': 'A', 'en': 'A', 'am': 'A', 'em': 'A',
              'on': 'O', 'om': 'O', 'in': 'I', 'un': 'U', 'um': 'U'}
_NASAL_RE = re.compile(r'(an|en|am|em|on|om|in|un|um)(?![aeiouynm])')


def _nasal_rep(m):
    return _NASAL_MAP[m.group(1)]


SILENT_FINALS = set('dtsxbpgz')  # word-final; see RULES (never -e/-r/singletons)


def project(word, silent_finals=True):
    """Map a French word (or cipher value string) to phonetic classes."""
    w = word.lower().replace('œ', 'oe').replace('æ', 'ae')
    w = ''.join(ACCENT_MAP.get(ch, ch) for ch in w)
    w = ''.join(c for c in unicodedata.normalize('NFD', w)
                if unicodedata.category(c) != 'Mn')
    w = re.sub(r'[^a-z]', '', w)
    if not w:
        return w
    for pat, rep in DIGRAPHS_A:
        w = w.replace(pat, rep)
    w = w.replace('h', '')
    w = _NASAL_RE.sub(_nasal_rep, w)
    w = w.replace('y', 'i').replace('w', 'v')
    w = re.sub(r'(?<=[aeiouAEIOU])x$', '', w)
    w = w.replace('x', 'ks')
    w = w.replace('ss', 'S')
    w = re.sub(r'(.)\1', r'\1', w)
    if silent_finals and len(w) > 1:
        # vowel guard: only delete after a vowel/nasal-class char, so
        # consonant clusters ('st','tr','pr') survive intact
        w = re.sub(r'(?<=[aeiouAEIOU])[dtsxbpgz]+$', '', w)
    # belt-and-braces: a projection must never be empty (empty scores 0 and
    # is a degenerate attractor for the optimizer)
    if not w:
        w = re.sub(r'[^a-z]', '', word.lower())
    return w


def alphabet():
    """The projected alphabet (computed from the rules; informational)."""
    return sorted(set('aeiou' + 'ACNOIUS' + 'bcdfgjklmnpqrstvzx'))


# ---------------------------------------------------------------------------
# Self-test: every case traces to a lane artifact (file named in the comment).
# ---------------------------------------------------------------------------
def self_test():
    cases = [
        # (input, expected, why)
        ('première', 'premiere', 'crib: cipher writes pre|m|i|er|e (STATE.md)'),
        ('la', 'la', 'anchor 11'),
        ('pre', 'pre', 'anchor 70'),
        ('que', 'ke', 'anchor 46: qu->k'),
        ('qui', 'ki', 'soft 64=qui'),
        ('ce', 'ce', 'soft 87=ce'),
        ('par', 'par', 'soft 96=par'),
        ('m', 'm', 'anchor 82: singleton kept'),
        ('i', 'i', 'anchor 34: singleton kept'),
        ('e', 'e', 'anchor 40: singleton kept, -e never deleted (R1)'),
        ('er', 'er', 'anchor 29: -r kept'),
        ('prend', 'prA', 'R3: silent -d- drops; nasal kept as class A'),
        ('premier', 'premier', 'nasal guard: em+i stays oral (crib-adjacent)'),
        ('ennemi', 'enemi', 'nasal guard: en+n stays oral'),
        ('bonne', 'bone', 'nasal guard: on+n stays oral; nn->n'),
        ('pain', 'pI', 'ain->I consumes the n (/pEhN/); before ai->e'),
        ('vent', 'vA', 'en+t nasal; silent -t drops'),
        ('moyen', 'moI', 'yen->I (/jEhN/)'),
        ('chien', 'CI', 'ien->I; ch->C'),
        ('les', 'le', 'silent -s drops (PROVISIONAL/R11)'),
        ('des', 'de', 'silent -s drops'),
        ('est', 'e', 'silent -st drop; by-ear /e/'),
        ('et', 'e', 'silent -t drops'),
        ('nous', 'nu', 'ou->u; silent -s drops'),
        ('pas', 'pa', 'silent -s drops'),
        ('dans', 'dA', 'an->A, silent -s drops'),
        ('en', 'A', 'soft 94=en islet reading'),
        ('ne', 'ne', '94=ne reading'),
        ('on', 'O', 'soft 62=on'),
        ('eau', 'o', 'digraph eau->o'),
        ('au', 'o', 'digraph au->o'),
        ('ou', 'u', 'digraph ou->u'),
        ('chat', 'Ca', 'ch->C'),
        ('photo', 'foto', 'ph->f'),
        ('qui', 'ki', 'qu->k'),
        ('passe', 'paSe', 'ss->S distinct from s'),
        ('poison', 'poisO', 'on nasal /pwazO~/; single s kept'),
        ('terre', 'tere', 'R8: rr->r'),
        ('deux', 'deu', 'final x after vowel deletes'),
        ('six', 'si', 'final x after vowel deletes'),
        ('axe', 'akse', 'else x->ks'),
        ('honnête', 'onete', 'h deletes; on+n stays oral'),
        ('ment', 'mA', 'en->A, silent -t drops'),
        ('ent', 'A', '-ent verb ending'),
        ('gouvernement', 'guvernemA', 'ou->u, em+e oral, en->A, silent -t'),
        ('st', 'st', 'vowel guard: consonant cluster survives intact'),
        ('tr', 'tr', 'vowel guard: consonant cluster survives intact'),
        ('ours', 'urs', 'ou->u; vowel guard: s after r kept (/uRs/)'),
    ]
    bad = []
    for src, exp, why in cases:
        got = project(src)
        if got != exp:
            bad.append((src, exp, got, why))
    # invariants over a fixed probe list
    probe = ['la', 'pre', 'm', 'i', 'er', 'e', 'que', 'ce', 'qui', 'par',
             'ne', 'pas', 'so', 'en', 'on', 'de', 'les', 'des', 'un', 'une']
    alpha = set(alphabet())
    for p in probe:
        q = project(p)
        assert q, f'empty projection of {p!r}'
        assert set(q) <= alpha, f'out-of-alphabet char in {p!r}->{q!r}'
    # NOTE: project() is not idempotent on its own output by design -- the
    # output alphabet contains uppercase class chars (A/C/N/O/I/U/S) which
    # project() lowercases on entry. The projection is applied exactly ONCE
    # to each input (corpus word, lexicon word, inventory value), never to
    # its own output, so idempotence is not required. Determinism is what
    # matters and holds trivially.
    for p in probe:
        assert project(p) == project(p), f'nondeterministic: {p!r}'
    return bad


if __name__ == '__main__':
    bad = self_test()
    print(f'alphabet: {"".join(alphabet())} (n={len(alphabet())})')
    if bad:
        print(f'SELF-TEST FAILURES ({len(bad)}):')
        for src, exp, got, why in bad:
            print(f'  {src!r}: expected {exp!r}, got {got!r} ({why})')
        raise SystemExit(1)
    print('phonetics self-test: all cases pass')
    print('rule grades:')
    for name, grade, desc in RULES:
        print(f'  [{grade:12s}] {name}: {desc}')
