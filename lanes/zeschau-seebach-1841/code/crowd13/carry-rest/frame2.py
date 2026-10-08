#!/usr/bin/env python3
"""C: second "48-47-46" hunt (round 13 carry-rest). Implements PREREG.md section C.

Byte-exact census of 48-47-46 trigrams on the repaired stream (+ near-miss
48-47-X and 48-X-46). Verifies @1658 = 48-47-98, not 48-47-46.
"""
import json, sys
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
sys.path.insert(0, str(LANE / 'code/crowd7/keystruct'))
from aliasing import load_stream

PAIRS = load_stream()
N = len(PAIRS)
assert N == 1847, N

VALS = {11: 'la', 70: 'pre', 82: 'm', 34: 'i', 29: 'er', 40: 'e', 46: 'que',
        87: 'ce?', 64: 'qui?', 96: 'par?', 59: 'est/-este?', 77: 'le?',
        62: 'on~fenced', 52: 'pas~', 94: 'ne?'}
def gloss(p):
    return [str(x) if x not in VALS else f"{x}={VALS[x]}" for x in p]

strict = [i for i in range(N - 2)
          if PAIRS[i] == 48 and PAIRS[i+1] == 47 and PAIRS[i+2] == 46]
near_48_47_X = [(i, PAIRS[i+2]) for i in range(N - 2)
                if PAIRS[i] == 48 and PAIRS[i+1] == 47 and PAIRS[i+2] != 46]
near_48_X_46 = [(i, PAIRS[i+1]) for i in range(N - 2)
                if PAIRS[i] == 48 and PAIRS[i+1] != 47 and PAIRS[i+2] == 46]

def win(i):
    return {"ctx": PAIRS[max(0, i-3):i+6], "gloss": gloss(PAIRS[max(0, i-3):i+6])}

res = {"n": N,
       "strict_48_47_46": {str(i): win(i) for i in strict},
       "near_48_47_X": {str(i): {"x": x, **win(i)} for i, x in near_48_47_X},
       "near_48_X_46": {str(i): {"x": x, **win(i)} for i, x in near_48_X_46}}
out = LANE / 'code/crowd13/carry-rest/frame2_raw.json'
out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
print("strict 48-47-46:", strict)
print("48-47-X:", [(i, x) for i, x in near_48_47_X])
print("48-X-46:", [(i, x) for i, x in near_48_X_46])
