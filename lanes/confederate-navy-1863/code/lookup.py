#!/usr/bin/env python3
"""lookup.py — parse (page)-(column)-(word) dictionary-code groups from the
Barney -> Mallory letter of 19 March 1863 and substitute plaintext words
from a page->column->word index.

Usage: python3 lookup.py [letter.txt] [index.json]

The index is optional. If data/dictionary-index.json exists (page -> column ->
word dict of strings), each group is replaced inline by [word]. Otherwise
groups are printed unchanged, so the output still proves parsing worked.

Group grammar handled:
  (177)-2-16-      standard, trailing dash
  (23)-3-29.       trailing punctuation instead of dash
  (215)-2-26       no trailing dash
  (149)-1-30-a     trailing variant letter after a dash (kept; lookup uses the
                   base triple page-col-word)
  (10)-1-12-.      trailing dash + punctuation
"""

import json
import re
import sys

# token = (page)-col-word with optional "-<letter>" variant and optional
# trailing dash; following punctuation/whitespace is left untouched
GROUP_RE = re.compile(
    r"\((?P<page>\d+)\)-(?P<col>\d+)-(?P<word>\d+)"
    r"(?P<var>(?:-[a-z])?)"
    r"(?P<dash>-?)"
)


def parse_groups(text):
    """Return list of dicts: token, page, col, word, var for each group."""
    out = []
    for m in GROUP_RE.finditer(text):
        out.append({
            "token": m.group(0),
            "page": int(m.group("page")),
            "col": int(m.group("col")),
            "word": int(m.group("word")),
            "var": m.group("var"),
            "start": m.start(),
            "end": m.end(),
        })
    return out


def load_index(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def substitute(text, index=None):
    def repl(m):
        page, col, word, var = m.group("page"), m.group("col"), m.group("word"), m.group("var")
        if index is not None:
            try:
                w = index[page][col][word]
            except (KeyError, TypeError):
                w = None
            if w:
                tag = f"{page}-{col}-{word}{var}"
                return f"[{w}]({tag})"
        return m.group(0)
    return GROUP_RE.sub(repl, text)


def main():
    letter_path = sys.argv[1] if len(sys.argv) > 1 else "data/letter.txt"
    index_path = sys.argv[2] if len(sys.argv) > 2 else "data/dictionary-index.json"
    with open(letter_path, "r", encoding="utf-8") as f:
        text = f.read()
    try:
        index = load_index(index_path)
        mode = f"decoding with {index_path}"
    except (FileNotFoundError, json.JSONDecodeError):
        index = None
        mode = "no index found — groups printed undecoded"
    groups = parse_groups(text)
    sys.stdout.write(substitute(text, index))
    sys.stderr.write(f"\n[lookup.py] {mode}; parsed {len(groups)} groups\n")


if __name__ == "__main__":
    main()
