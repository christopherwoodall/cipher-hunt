"""Shared loader for battery48 (round 14). Repaired stream only."""
import sys
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
sys.path.insert(0, str(LANE / 'code/crowd7/keystruct'))
from aliasing import load_stream

PAIRS = load_stream()
N = len(PAIRS)
assert N == 1847, N

# banked values: GT plain, provisional '?', fenced/strong '~'
VALS = {11: 'la', 70: 'pre', 82: 'm', 34: 'i', 29: 'er', 40: 'e', 46: 'que',
        87: 'ce?', 64: 'qui?', 96: 'par?', 59: 'est/-este?', 77: 'le?',
        62: 'on~fenced', 52: 'pas~', 94: 'ne?'}

def gloss(p):
    return [str(x) if x not in VALS else "%d=%s" % (x, VALS[x]) for x in p]

CORP = LANE / 'code/side-period/corpus'
FILES = ['guizot-memoires-t1-gutenberg.txt', 'guizot-memoires-t2-gutenberg.txt',
         'guizot-memoires-t3-gutenberg.txt', 'guizot-memoires-t5-t6.txt',
         'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
         'pozzo-di-borgo-correspondance-v1.txt', 'levant-correspondence-1841-p3.txt',
         'talleyrand-memoires-v1.txt', 'revue-deux-mondes-1841-q1.txt',
         'revue-deux-mondes-1841-q2.txt', 'revue-deux-mondes-1841-q3.txt',
         'revue-deux-mondes-1841-q4.txt']
