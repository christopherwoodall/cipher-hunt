"""Canonical R5005 pair sequence (Seebach key-hunt test harness).

Replicates the lane-canonical parse exactly: upstream-ct_R5005.txt
(one row per written line, tagged a<block>_<line>) grouped with the
per-line offsets from upstream-offsets.json (offsets chosen by EM on
pair frequency). Self-validates on load:

  - 3,764 digits total, 1,846 pairs, 96 distinct groups
  - the ground-truth pencil sequence 11-70-82-34-29-40 ("la première")
    occurs exactly once, at pair index 1033 (0-based)

Do NOT hand-roll a parse; import load_canonical_pairs() from here.
"""
import json
import os
import re

_LANE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..")
_LANE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
_DATA = os.path.join(_LANE, "data")

EXPECTED = {
    "digits": 3764,
    "pairs": 1846,
    "distinct_groups": 96,
    "anchor_seq": ["11", "70", "82", "34", "29", "40"],
    "anchor_index": 1033,
}

# Ground-truth anchors from the erased pencil decipherment
# (upstream-NOTES.md; see also closer-87ce-resolution.md in report_inbox).
GROUND_TRUTH = {
    "11": "la",
    "70": "pre",
    "82": "m",
    "34": "i",
    "29": "er",
    "40": "e",
    "46": "que",
}

# Lane-inferred, provisional: usable only as secondary checks, never as gates.
PROVISIONAL = {
    "87": "ce",
    "64": "qui",
    "96": "par",
}


def load_canonical_pairs():
    """Return the canonical 1,846-pair sequence as a list of 2-char strings.

    Raises AssertionError if the parse does not match every canonical landmark.
    """
    offsets = json.load(open(os.path.join(_DATA, "upstream-offsets.json")))
    pairs = []
    for line in open(os.path.join(_DATA, "upstream-ct_R5005.txt")):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        digits = re.sub(r"\D", "", digits)
        d = digits[offsets.get(lid, 0):]
        for i in range(0, len(d) - 1, 2):
            pairs.append(d[i:i + 2])

    total_digits = sum(len(re.sub(r"\D", "", l.split()[1]))
                       for l in open(os.path.join(_DATA, "upstream-ct_R5005.txt"))
                       if l.strip())
    assert total_digits == EXPECTED["digits"], f"digit count {total_digits}"
    assert len(pairs) == EXPECTED["pairs"], f"pair count {len(pairs)}"
    assert len(set(pairs)) == EXPECTED["distinct_groups"], f"distinct {len(set(pairs))}"
    hits = [i for i in range(len(pairs) - 5)
            if pairs[i:i + 6] == EXPECTED["anchor_seq"]]
    assert hits == [EXPECTED["anchor_index"]], f"anchor seq hits at {hits}"
    return pairs
