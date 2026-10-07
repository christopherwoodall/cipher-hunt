"""unit_inventory.py — INVENTORIST executor (Seebach cipher, crowd round 5).

Learns the cipher's syllable-unit inventory bottom-up from ground truth:
pencil cribs + ear-cutting exemplars + polyvalence islets + cutting rules.
F30: rigid French syllabification is DEAD as the unit set; do not import it.
All evidence is recomputed here from the canonical parse
(code/side-keyhunt/repaired_offsets.json, 1,847 pairs).

Usage: python3 unit_inventory.py
Emits: unit_inventory.json (same directory).
"""
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))  # lane root


def load_pairs():
    """Canonical repaired parse: 1,847 pairs, 96 groups (F32)."""
    off = json.load(open(os.path.join(LANE, 'code', 'side-keyhunt',
                                      'repaired_offsets.json')))
    toks = []
    for l in open(os.path.join(LANE, 'data', 'upstream-ct_R5005.txt')):
        k, s = l.split()
        o = off[k]
        toks += [s[i:i + 2] for i in range(o, len(s) - 1, 2)]
    assert len(toks) == 1847, len(toks)
    return toks


pairs = load_pairs()
N = len(pairs)
freq = Counter(pairs)


def bigram(a, b):
    return sum(1 for i in range(N - 1) if pairs[i] == a and pairs[i + 1] == b)


def find(seq):
    L = len(seq)
    return [i for i in range(N - L + 1) if pairs[i:i + L] == list(seq)]


def followers(g):
    return Counter(pairs[i + 1] for i in range(N - 1) if pairs[i] == g)


def predecessors(g):
    return Counter(pairs[i - 1] for i in range(1, N) if pairs[i] == g)


# ---------------------------------------------------------------- checks
# (assertions = the evidence the inventory rests on; each must hold)
# Tier 0: the seven pencil cribs (GT)
assert find(['11', '70', '82', '34', '29', '40']) == [754, 1034], \
    'la premiere crib windows'
# Tier 1: ear-cutting exemplars (R2 inconsistent cuts; R3 mute-e written)
assert find(['93', '52', '94'])[0] == 159, 'personne cut 1 (per|so|nne)'
assert find(['77', '62', '94'])[0] == 507, 'personne cut 2 (pers|on|ne)'
assert len(find(['29', '40'])) == 9, 'erre = er|e x9'
assert find(['62', '94', '70', '52']) == [1329], 'on ne prend pas (prend->pre)'
# note: the frenchman's prose cited @1331 (loose); old parse had 62-94-70-52
# @1328, REINDEX.md's n+1 rule gives 1329 on the canonical parse.
assert bigram('46', '62') == 0, 'qu/on one spoken syllable -> one group'
# Tier 2: polyvalence islets (F33 conditioned polyvalence)
assert find(['77', '78', '94', '82', '06']) == [1180, 1351], '94-82-06 trigram'
assert find(['94', '82', '06']) == [578, 1182, 1353], '94-82-06 x3'
assert bigram('94', '52') == 3 and bigram('94', '59') == 3, 'ne se frames'
assert find(['82', '94', '76']) and find(['94', '87', '83']), '94=en islets'
assert find(['06']) and bigram('06', '40') == 0, '06 crib-contradiction N17'

# ---------------------------------------------------------------- units
UNITS = [
    # ---- TIER 0: pencil-crib ground truth (status: PROOF) ----
    {'group': '11', 'value': 'la', 'status': 'PROOF (pencil crib)',
     'shape': 'CV open syllable; whole function word',
     'evidence': 'la premiere 11-70-82-34-29-40 @754 (gloss line a5_03) and @1034; '
                 'n=45 (2.44%, rank 4/96)',
     'fixes': "proves whole-word CV units exist; anchors R2's other cuts"},
    {'group': '70', 'value': 'pre', 'status': 'PROOF (pencil crib)',
     'shape': 'CCV onset-cluster syllable',
     'evidence': 'la premiere @754/@1034; n=15 (0.81%). Also writes '
                 '"prend" (silent d dropped) @1332: 62-94-70-52 "on ne pre nd pas" '
                 '-- phonetic spelling, not orthographic',
     'fixes': 'proves onset clusters are single units AND that units follow '
              'pronunciation, not spelling (mute-d unwritten while mute-e IS written)'},
    {'group': '82', 'value': 'm', 'status': 'PROOF (pencil crib)',
     'shape': 'BARE CONSONANT single letter (no vowel)',
     'evidence': 'la premiere @754/@1034 ("pre|m|i|er|e": the encipherer splits '
                 'mi->m|i); n=39 (2.11%, rank 9/96)',
     'fixes': 'THE kill of rigid syllabification: standalone m is phonotactically '
              'impossible in French but REAL here (lexicon: "m" as syllable in '
              'exactly 1 of 11,870 era words). R1 (1-letter cells) is mandatory.'},
    {'group': '34', 'value': 'i', 'status': 'PROOF (pencil crib)',
     'shape': 'BARE VOWEL single letter',
     'evidence': 'la premiere @754/@1034; n=11 (0.60%, rank 70/96)',
     'fixes': 'proves single-letter vowel cells; with 82=m proves cuts go below '
              'the phonological syllable'},
    {'group': '29', 'value': 'er', 'status': 'PROOF (pencil crib)',
     'shape': 'morphological ending (infinitive marker), word-final-ish',
     'evidence': 'la premiere @754/@1034; n=45 (2.44%, rank 4/96). Phase-C anchor '
                 '(prev-A 0.77, next-B 0.89; contactor F11). Era bare-"er" as a '
                 'standalone unit: 0.038% (lane-banked N15) -- 64x cipher overage; '
                 'bigram-closer: 182x over era (N22).',
     'fixes': 'proves morphological endings are units; the cipher segments '
              '"premiere" ending as er|e (er for the pronounced part, e for mute); '
              'rate gap proves era-syllable-conditioned rate legs VOID (F30)'},
    {'group': '40', 'value': 'e', 'status': 'PROOF (pencil crib)',
     'shape': 'MUTE -e written as its own unit',
     'evidence': 'la premiere @754/@1034 writes mute final -e as 40; '
                 '"erre"=29-40 x9 @62/291/500/597/685/758/1038/1050/1710; n=21 '
                 '(1.14%). N20: era tokenizers almost never emit word-final bare '
                 '"e" (syllabifier artifact), so 40-conditionals are uncalibrated.',
     'fixes': 'R3: mute -e is WRITTEN by default (kills phonetic models needing '
              'mute-e unwritten, N17: 06->40 = 0x).'},
    {'group': '46', 'value': 'que', 'status': 'PROOF (pencil crib)',
     'shape': 'whole function word (consonant + schwa)',
     'evidence': 'pencil crib 46=que; n=29 (1.57%). 46->62 = 0x: "qu/on" = /ko~/ '
                 '= ONE spoken syllable -> one group (frenchman N28: the by-ear '
                 'model PREDICTED this zero).',
     'fixes': 'proves whole-word function units; proves elided compounds are '
              'ONE unit by ear (units are spoken-syllable chunks, not orthographic)'},
    # ---- TIER 1: lane-inferred values (status: provisional/confirmed) ----
    {'group': '87', 'value': 'ce', 'status': 'PROVISIONAL-strengthened (F27)',
     'shape': 'whole function word (proclitic)',
     'evidence': '87->11 "cela" x7 @P(11|87)=0.219; 87->46 "ce que" x3; '
                 '87->64 x5; 14 distinct predecessors (rank 15/96, n=32, 1.73%). '
                 'cela-leg register-dependent (N27); ci/te scan NULL.',
     'fixes': 'compound function-word frames; every downstream value inherits '
              'this provisional status (64="qui", 96="par")'},
    {'group': '64', 'value': 'qui', 'status': 'PROVISIONAL, re-promotion BLOCKED',
     'shape': 'whole function word',
     'evidence': 'n=47 (2.54%, rank 3/96). 87->64 x5; 24-87-64 x3 formula '
                 '(value withheld); rival 64="meme" demoted->disfavored (N27); '
                 '64-77-84 x3 is ONE byte-identical trigram (n_eff=1).',
     'fixes': 'check (b) conditioned on provisional 87=ce; factor-2 band admits '
              'qui/qu/n (F20)'},
    {'group': '96', 'value': 'par', 'status': 'CONFIRMED 4/4 on repaired C1 leg; '
     'inherits 87=ce provisional status (F28)',
     'shape': 'whole function word',
     'evidence': 'n=21 (1.14%). P(87|96)=0.1429 vs syllabary-aware predicted '
                 '0.1130 (1.26x); "parce que" frame 96-87-46 x3 @224/952/1526. '
                 '96="de" REFUTED (N14).',
     'fixes': 'whole-word compound frames (parce, parce que) are multi-group '
              'compounds from word-units'},
    {'group': '94', 'value': 'ne', 'status': 'PROVISIONAL-strong (F24, N24)',
     'shape': 'whole function word (negation particle)',
     'evidence': 'n=37 (2.00%). Era syllable rate 1.025x; trigram 94-82-06 x3 '
                 '@578/1182/1353 with GT 82=m centered; 94->82 x4 total; '
                 '"on ne prend pas" lock @1332; rival 94="re" demoted->disfavored '
                 '(N24: word-space host odds 2.27:1 for ne; 0/36 composing).',
     'fixes': 'negation frames are multi-group compounds (94-52 "ne pas" x3, '
              '94-59 x3); trigram-internal "ent" is the CONDITIONED co-reading'},
    {'group': '06', 'value': 'verb-stem-class', 'status': 'PROVISIONAL (F25, N29)',
     'shape': 'verb stem (class-level reading; specific stem unidentified)',
     'evidence': 'n=44 (2.38%). 06->77 x6, 06->29 x4 (infinitive frames), '
                 '06->11 x4, 06->00 x4; 30 distinct predecessors. 06/86 '
                 'complementary distribution: 06=finite/imperative stem '
                 '(00->06 x0), 86=infinitive-complement stem (00->86 x12). '
                 '06=/mA~/ "demand-" KILLED by crib contradiction (N17: '
                 '06->40 = 0x). 06="ent" general REFUTED (N19), restricted to '
                 'the 3 trigrams = PLAUSIBLE.',
     'fixes': 'lexical stems (not just syllables) are inventory units; '
              'complementary distribution is the first inventory-level '
              'conditioning rule discovered from contact data'},
    {'group': '67', 'value': 'veut', 'status': 'PROVISIONAL (demoted CONFIRMED, N18)',
     'shape': 'whole word / modal governor',
     'evidence': 'n=38 (2.06%). Modal-governor + 06 lexical-stem is the live '
              'verb-system picture.',
     'fixes': 'verb-system units may be whole-word, not syllabic'},
    {'group': '62', 'value': 'on', 'status': 'STRONG LEAD (N28; promotion held '
     'for an instrument-independent third leg)',
     'shape': 'nasal monosyllable / whole function word',
     'evidence': 'n=35 (1.89%). 62->94 "on ne" x9 @0.2571 (2.18x era, repaired); '
                 'pers|on|ne @507 (77-62-94); fresh-window subject triangulation '
                 '@845-853 "...par ecrit, on me [dit]...", zero counterexamples '
                 'in 26 windows; /o~/ rivals killed. Note: 62->94 is x9 not x8 '
                 'on the repaired parse (a5_03 region contributes a 9th @761).',
     'fixes': 'nasal vowel + consonant is one unit; the personne double-cut '
              'shares group 94 for the unchanged /n/ sound (allophony direction)'},
    {'group': '78', 'value': 'me', 'status': 'LEAD (promotion REJECTED, N20; '
     'B-78b fix verified N25)',
     'shape': 'whole function word (proclitic) OR word-internal "ver"',
     'evidence': 'n=31 (1.68%). 78->40 x3; 11->78 x2; 47->78 x5; 37->78 x4. '
                 'Rival "l\'" killed (58x); rival "e" LIVE (the "e"-kill was a '
                 'syllabifier artifact). 77->78 x7 frames fenced: 2/7 sit inside '
                 'the "gouvernement" trigram -> 78="ver" word-internal there.',
     'fixes': 'the "ver"/"me" tension is a conditioned-polyvalence candidate '
              '(word-internal vs proclitic positions)'},
    {'group': '77', 'value': 'le', 'status': 'LEAD (promoted LEAD-weak->LEAD, '
     'N25; ACCEPT fenced)',
     'shape': 'article/pronoun unit; verb-adjacent',
     'evidence': 'n=44 (2.38%). 77->86 x5 (object-pronoun frame); 77="pas" '
                 'DISFAVORED-strong (N21,N25); 77="que" disfavored. '
                 'Verb-adjacent: 64-77-84 x3 reads "qui [verbe] 84"; '
                 'verb-stem predecessors 06x6, 67x6.',
     'fixes': 'direction for 77 is verb-adjacent, not a standalone fragment'},
    {'group': '47', 'value': 'ce', 'status': 'LEAD (N29; polyvalent with 87)',
     'shape': 'whole function word, polyvalent with 87',
     'evidence': 'n=28 (1.52%). 47="me" as uniform word KILLED (3 independent: '
                 '"par me" era n=0; "me que" P=0; "me la" P=0). 47->46 "ce que" '
                 'x3 @3/28=0.1071 vs era 0.1076 -> 1.00x exact (curator-verified); '
                 '"par ce" 2.85x; 47->11 x3 "cela".',
     'fixes': 'first verified 1-sound->2-groups allophony at the FUNCTION-WORD '
              'level: "ce" = {87, 47}'},
    # ---- TIER 2: polyvalence islets (F33 — CONDITIONED, not free) ----
    {'group': '06+86', 'value': 'complementarity', 'status': 'PROOF-level pattern '
     '(N29), reading provisional',
     'shape': 'paired groups: 06 finite/imperative stem, 86 infinitive-complement',
     'evidence': '00->86 x12 vs 00->06 x0 (repaired parse). 06->29 x4 '
                 '(infinitive frames, repaired count; old 5th was off-phase '
                 'artifact); 06->77 x6; 06->11 x4; 06->00 x4.',
     'fixes': 'the same stem can sit in two inventory slots by MOOD; the '
              'encipherer distinguishes finite vs infinitive encodings'},
    {'group': '52', 'value': 'pas | so/se (conditioned)',
     'status': 'PROOF (K5 scoped kill forces polyvalence) + STRONG-bounded "pas" (F31)',
     'shape': 'one group, two readings by position',
     'evidence': '52="pas" iff negation-frame: 94->52 x3 ("ne pas"); 70->52 x1 '
                 '("prend pas" @1332); "on ne prend pas" lock; ne-pas-inf x2. '
                 '52="so" word-internal @159 (93-52-94 "per|so|nne" vs 77-62-94 '
                 '"pers|on|ne" @507); 52="se" LEAD (94->52 x3 also reads "ne se"; '
                 '94->59 x3 splits the other "ne se"). 52="pas"-as-single-reading '
                 'killed @159 (N23).',
     'conditioning_rule': '52 = "pas" iff immediate predecessor in {94, 70} '
                          '(negation frame); else "so"/"se" (word-internal)',
     'fixes': 'first VERIFIED conditioned-polyvalence rule: the SAME group '
              'writes a grammatical particle AND a word-internal syllable, '
              'selected by local context'},
    {'group': '94', 'value': 'ne | en (conditioned)',
     'status': 'PROOF-level (N31: co-value promotion DENIED only on independence, '
     'legs stand)',
     'shape': 'one group, two readings by position',
     'evidence': '94="ne" provisional-strong (see Tier 1). 94="en" islets: '
                 '82-94-76 "m\'en" @1576 and 94-87-83 "en ce" @1169 (repaired), '
                 '4/4 conditioned (pre=82 or suc=87). Rival 94="re" disfavored '
                 '(N24). @1742 (old @1741) unresolved under both readings.',
     'conditioning_rule': '94 = "en" iff pre=82 ("m\'en") or suc=87 ("en ce"); '
                          'else "ne"',
     'fixes': 'conditioning can be lexical (m\'en / en ce are idiom frames), '
              'not just positional'},
    # ---- TIER 3: cutting rules (banked in code/crowd4/syllabary4.py) ----
    {'group': 'R1', 'value': 'cells are 1-4 letters; 1-letter cells exist',
     'status': 'PROOF (crib)',
     'shape': 'inventory alphabet constraint',
     'evidence': 'pre|m|i|er|e: 3-letter, 1-letter, 1-letter, 2-letter, 1-letter '
                 'in one word. Any fragment leg must allow 1-letter cells.',
     'fixes': 'no unit inventory may exclude single letters'},
    {'group': 'R2', 'value': 'cuts are by ear and INCONSISTENT',
     'status': 'PROOF (frenchman ear-read, positions verified)',
     'shape': 'segmentation freedom',
     'evidence': '"personne" = 93|52|94 (per|so|nne @159) vs 77|62|94 '
                 '(pers|on|ne @507); same word, two cuts, one cipher. '
                 '"prend" -> "pre" (silent d dropped) @1332.',
     'fixes': 'no fragment leg may require a unique segmentation; test the '
              'SET of plausible cuts'},
    {'group': 'R3', 'value': 'mute -e is WRITTEN',
     'status': 'PROOF (crib)',
     'shape': 'default orthographic treatment',
     'evidence': 'premiere -> ...|er|e with 40 for mute final -e; "erre"=29|40 '
                 'x9. Phonetic models needing mute-e unwritten contradict the '
                 'crib (N17).',
     'fixes': 'unwritten-mute-e readings need their own positive evidence'},
    {'group': 'R4', 'value': 'morphological endings are cells; table mixes '
     'letters, syllables, endings, whole function words',
     'status': 'PROOF (crib + phase analysis F11)',
     'shape': 'inventory type mixture',
     'evidence': '29=er word-final-ish (phase C: prev-A 0.77, next-B 0.89). '
                 '11=la and 46=que are whole words.',
     'fixes': 'the inventory is a mixed table, not a pure syllabary'},
]

# ---- what the inventory rules out ---------------------------------------
RULED_OUT = [
    {'claim': 'The 180-unit upstream inventory (data/upstream-syll*.py: 24 '
              'single letters + 156 French syllable/function-word units)',
     'status': 'DEAD as the encipherer\'s table',
     'evidence': 'All three off-the-shelf annealers "still no French" '
                 '(upstream-NOTES.md "What failed"); syllabary4.py documents it '
                 'as a hypothesis, not a recovery; N29: upstream 180-unit '
                 'inventory is NOT the encipherer\'s table (all three annealers '
                 'failed on it). Treat as one hypothesis among others, never '
                 'the default.'},
    {'claim': 'Standard French syllabification as the unit set',
     'status': 'DEAD (ground-truth control)',
     'evidence': 'The 4-GT-anchor "premiere" tail (82-34-29-40) returns ZERO '
                 'lexicon candidates at every tier (matcher README: HONEST '
                 'NULL). Lexicon "m" as a syllable: 1 of 11,870 entries; '
                 'lexicon "premiere" = pre|mi|e|re (4) vs cipher pre|m|i|er|e '
                 '(5). Standalone m is phonotactically impossible in French '
                 'but GT-proven here.'},
    {'claim': 'Era-syllable-conditional rate legs on morphological fragments',
     'status': 'VOID (F30)',
     'evidence': '29=er 2.44% vs era bare-"er" 0.038% (lane-banked N15; 182x '
                 'bigram-closer N22); 82=m 2.11% vs era bare-"m" (61x); '
                 '34=i 0.60% vs era bare-"i" (3.3x). The cipher\'s segmentation '
                 'does not match ANY rule tried (tuner N15). 40-conditionals '
                 'also excluded: era tokenizer almost never emits word-final '
                 'bare "e" (N20 syllabifier artifact).'},
    {'claim': 'Rigid syllabification as an instrument',
     'status': 'DEAD (F30) — three independent lines: tuner NULL (N15), '
               'calibration mismatch (N22), frenchman\'s by-ear enlightenment',
     'evidence': 'Tuner LOO: phase-constrained 2/34 vs unconstrained 6/34 '
                 'top-10 slots; phases are NOT word-position classes (rotation '
                 'itself real, chi2=366.3 on repaired parse, N30).'},
    {'claim': 'Phonetic models needing mute-e UNWRITTEN',
     'status': 'KILLED (N17)',
     'evidence': 'Crib writes 40="e" for mute final -e; 06=/mA~/ "demand-" '
                 'died on 06->40 = 0x (this script re-verifies: 0).'},
    {'claim': 'Unique segmentation of a word',
     'status': 'KILLED (R2)',
     'evidence': '"personne" cut two ways in one cipher (@159 vs @507).'},
    {'claim': '"J\'ai l\'honneur de" = 77 78 94 82 06 (H5)',
     'status': 'KILLED (N11)',
     'evidence': 'Kill-grade structural contradiction: position 4 is 82=\'m\' '
                 '(ground truth) but the phrase needs "neur"; plus 67x/184x/47x '
                 'rate failures.'},
    {'claim': 'Free (unconditioned) polyvalence',
     'status': 'ZERO verified cases (F33)',
     'evidence': '3/25 identified groups (12.0%) carry >=2 live readings, '
                 'each with a verified conditioning rule (06, 52, 94). All '
                 'encipherer noise runs the allophony direction (1 sound -> N '
                 'groups; "personne" keeps 94 for unchanged /n/), never '
                 'unconditioned 1 group -> 2 sounds. Falsifiable: one verified '
                 'unconditioned case breaks it.'},
    {'claim': '"ment"-family instruments needing 82 as "neur"-position',
     'status': 'DEAD with H5',
     'evidence': '82=\'m\' is ground truth; the 94-82-06 trigram is '
                 '"ne|m|ent" (conditional 06) or "gouvernement"-family, not '
                 '"ment" as a fused unit.'},
    {'claim': 'The "parce" rate as computed by the sweeper (132/1036)',
     'status': 'MISCOMPUTED, repaired (F28)',
     'evidence': 'True word-space P(ce|par)=13/1036=0.0125 (11.4x fail); '
                 'syllabary-aware repair P(87|96)=0.1429 vs predicted 0.1130 '
                 '(1.26x). 96="par" CONFIRMED stands on the repaired leg only.'},
]

INVENTORY = {
    'meta': {
        'role': 'INVENTORIST (crowd round 5)',
        'canonical_parse': 'code/side-keyhunt/repaired_offsets.json '
                           '(1,847 pairs, 96 groups, F32)',
        'n_pairs': N, 'n_groups': len(freq),
        'method': 'bottom-up from ground truth: pencil cribs + ear-cutting '
                  'exemplars + polyvalence islets (F33) + cutting rules (R1-R4)',
        'lane_rule': 'F30: rigid French syllabification DEAD; era word-space '
                     'legs survive; fragment hypotheses test against THIS '
                     'inventory',
    },
    'units': UNITS,
    'ruled_out': RULED_OUT,
    'shape_regularities': {
        'unit_lengths': '1-4 letters (R1); proven: 1-letter (m bare consonant, '
                        'i bare vowel, e mute vowel), 2-letter (la, er), '
                        '3-letter (pre, que)',
        'inventory_mix': 'letters + syllables + morphological endings + whole '
                         'function words (R4)',
        'whole_word_units': ['la (11, GT)', 'que (46, GT)', 'ce (87, PROVs)',
                             'qui (64, PROV)', 'par (96, CONF-inherits)',
                             'ne (94, PROVs)', 'on (62, SLEAD)', 'me (78, LEAD)',
                             'le (77, LEAD)'],
        'ending_units': ['er (29, GT; word-final-ish, phase-C)'],
        'polyvalence_rate': '3/25 identified groups = 12.0% (F33); all '
                            'conditioned; code information-lossless in principle',
        'rotation': 'A->C->B->A contact rotation real (chi2=366.3, repaired, '
                    'N30) but phases are NOT word-position classes (tuner N15); '
                    'cluster assignments fragile (61/96 change phase, N30)',
        'token_coverage': '35.2% (lane-banked STATE.md; 10 values + leads)',
        'unidentified_head': '00 (n=55, rank 1), 24 (n=52, rank 2), 98 '
                             '(n=40), 48 (n=38), 74 (n=34) — the inventory\'s '
                             'empty slots',
    },
    'status_legend': {
        'PROOF': 'pencil crib or lane-verified structural kill; not overturned '
                 'by corpus choice',
        'PROVISIONAL(-strengthened)': '>=2 independent checks, no surviving '
                                      'rival; register/corpus caveats fenced',
        'LEAD/STRONG LEAD': 'live working hypothesis, one check from promotion',
        'PLAUSIBLE': 'survives a kill, needs more evidence',
    },
}

with open(os.path.join(HERE, 'unit_inventory.json'), 'w') as f:
    json.dump(INVENTORY, f, indent=2, ensure_ascii=False)

print('wrote unit_inventory.json')
print(f'verified: {N} pairs, {len(freq)} groups, '
      f'{len(UNITS)} units, {len(RULED_OUT)} ruled-out claims')
print('la-premiere @', find(['11', '70', '82', '34', '29', '40']))
print('personne cuts:', find(['93', '52', '94'])[0], find(['77', '62', '94'])[0])
print('erre n =', len(find(['29', '40'])), '| 46->62 =', bigram('46', '62'))
print('94-82-06 @', find(['94', '82', '06']), '| 06->40 =', bigram('06', '40'))
