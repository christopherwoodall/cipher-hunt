# Provenance — corpus-grammars19c

19th-century French school grammars searched by battery `gov-excl-inf-grammars`
(2026-10-09) for cited governed exclamatory infinitives. Verdict: KILL (confirmed
zero; the grammatical category itself is absent from 19th-c school grammar).

All texts are the Internet Archive OCR `_djvu.txt` of Google-scanned public-domain
editions, retrieved 2026-10-09 via `http://archive.org/download/<id>/<id>_djvu.txt`
(port 80; archive.org :443 is blocked from this VM). SHA-256 in `SHA256SUMS`.

| file | work | edition | archive.org id |
|---|---|---|---|
| `girault-duvivier_1843.txt` | Girault-Duvivier, *Grammaire des grammaires* | 1843 | `grammairedesgra00unkngoog` |
| `bescherelle_1847.txt` | Bescherelle, *Grammaire nationale* | 1847 | `grammairenation00nicogoog` |
| `noel-chapsal_1849.txt` | Noël/Chapsal, *Nouvelle grammaire française* | 1849 | `nouvellegrammair00noel` |

Method note: full-text grep for `exclamat*`, all `infinitif` lines, `!`-terminated
`de/pour/à + infinitive` shapes, and the INFINITIF doctrine sections. See the
battery report `code/crowd17/report_inbox/battery-gov-excl-inf-grammars.md`.
