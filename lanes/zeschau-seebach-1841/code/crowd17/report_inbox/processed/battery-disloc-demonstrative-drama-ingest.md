# Battery report: disloc-demonstrative-drama-ingest

- Target id: `disloc-demonstrative-drama-ingest`
- Claim: "commission: ingest public-domain 19th-century French drama into the lane corpus."
- Date: 2026-10-09
- Worker: battery worker (subagent c7a52bab-f066-4861-be8a-569ccee05de5)
- Stream: not applicable — corpus-ingest commission for the drama-register
  census batteries (`disloc-demonstrative-drama` NULL, 2026-10-09). The
  1,847-pair repaired parse was not used. R5005, sealed gate instances, and
  the red-team adjudication queue were not touched.

## Bar (verbatim, pre-registered before testing)

"corpus lands with provenance notes (source URL, retrieval time, sha256) in
the lane corpus dir; the drama battery's exact bars become testable."

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) One or more public-domain 19th-century French DRAMA texts land in the
   lane corpus dir (`code/side-period/corpus/`), unmodified from source.
2. (C2) Each file carries a provenance note: source URL, retrieval time and
   method, and sha256.
3. (C3) The drama battery's exact bars are testable on the new corpus — i.e.
   a census per `disloc-demonstrative-drama`'s bar (">=1 genuine
   'cela/ceci/ca, [bare inf] !' in drama promotes arm (a); confirmed zero
   fences it at drama-register level") runs to completion over the new
   texts.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/disloc-demonstrative-drama-ingest.lock`
   on start (no prior lock); deleted on completion.
2. Queried the Internet Archive advanced-search API for French
   (language:fre) texts by Victor Hugo, Alfred de Musset, Alexandre Dumas
   père, and Alfred de Vigny; filtered to pre-1923 drama editions with
   OCR full text (`_djvu.txt`).
3. Downloaded via `curl -sSL` (plain `curl` returns zero bytes: archive.org
   redirects `archive.org/download/...` to a `dn*.archive.org` host; `-L`
   is required — logged here so future harvests don't re-learn this).
   Files saved byte-unmodified into `code/side-period/corpus/`.
4. Computed sha256 per file; appended Family 9 to
   `code/side-period/corpus/PROVENANCE.md` (new section, existing entries
   untouched).
5. Ran the `disloc-demonstrative-drama` census bars over the new corpus:
   strict pattern `(cela|ceci|ça) [,;:…] (≤1 short word) [infinitive-er/ir/re] !`
   within 50 chars, plus a loose fallback `(cela|ceci|ça) …[infinitive] …!`
   within 35 chars; every loose hit inspected with ±90 chars of context.

## Ingest (all four files, byte-unmodified)

| File | Work | Edition | Bytes | sha256 |
|---|---|---|---|---|
| `hugo-hernani-1870.txt` | Hugo, *Hernani* | New York: W. R. Jenkins, 1870 (Masson notes) | 207,880 | 05a6b8f7…e0bac6 |
| `dumas-mariage-louis-xv-1841.txt` | Dumas père, *Un mariage sous Louis XV* | Paris, 1841 ed. — contemporary with the R5005 letter | 207,347 | f51b724d…205e63b |
| `vigny-chatterton-1835.txt` | Vigny, *Chatterton* | Bruxelles: L. Hauman, 1835 | 192,684 | 277dd951…6a608ac |
| `musset-comedies-proverbes-1850.txt` | Musset, *Comédies et proverbes* (10 plays incl. Lorenzaccio, Le Chandelier, On ne badine pas avec l'amour) | Poitiers: A. Dupré, 1850 | 990,193 | fb6074c3…1aa3427 |

Total: 1,598,104 bytes / 1,569,886 characters of 19th-century French drama.
All authors long deceased (Hugo 1885, Musset 1857, Dumas 1870, Vigny 1863);
editions all pre-1923. Public domain.

Provenance: source URLs, retrieval time (2026-10-09 ~08:30 UTC), method
(`curl -sSL`), and full sha256 values recorded in
`code/side-period/corpus/PROVENANCE.md`, "Family 9 — 19th-century French
DRAMA".

## Census result (bars testable — and run)

- Strict shape `cela/ceci/ça, [bare infinitive] !`: **0 candidates** in all
  1,569,886 characters.
- Loose fallback: 10 candidates; **all classified as false friends with
  cause** — e.g. Dumas "cela à son couvent !" (couvent = noun),
  "à propos … cela ? … Pardieu !" (demonstrative, no infinitive), Musset
  "Cela serait drôle à penser ! penser n'est rien" (penser follows a
  different clause; "penser n'est rien" is its own sentence), "Cela est
  singulier !" (est = finite), "cela m'ennuie" (ennuie = finite 3sg),
  "cela est sérieux" (est = finite).
- Notable positive control: Hernani uses bare exclamatory infinitives —
  "Gouverner tout cela ! — Monter, si l'on vous nomme !" — but with the
  demonstrative as OBJECT after the infinitive, never as a fronted topic.
  The register has the infinitive construction; it does not show the
  dislocated-demonstrative topic shape.
- **Outcome under the drama battery's bar: confirmed zero in the
  drama register** (strict 0/1.57M chars; loose 10/10 false friends
  excluded with cause). Arm (a) of `ce87-1028-role` stays fenced at the
  drama-register level. No attestation promotes it; zero is an absence,
  not a kill, per the bar's clause 2.

## Per-clause pass/fail

1. (C1) PASS — four drama texts (14 plays across Hugo/Dumas/Vigny/Musset)
   landed in `code/side-period/corpus/`, unmodified.
2. (C2) PASS — PROVENANCE.md Family 9 records source URL, retrieval
   time/method, byte counts, and full sha256 for each file.
3. (C3) PASS — the census ran to completion over all four files (strict +
   loose + per-candidate classification), yielding the confirmed-zero
   result the bar needs.

Adverses: none listed.

## Verdict: PROMOTE

The corpus commission is complete and its downstream bars are now testable —
and the first test (the `disloc-demonstrative-drama` bar) runs to a
confirmed-zero verdict in the drama register.

## Follow-ups proposed (for supervisor queuing)

1. **disloc-demonstrative-drama-reissue** (already queued, P3): re-run the
   `disloc-demonstrative-drama` NULL battery over the four new drama files
   to formally retire its null — do not duplicate the census above
   (adopt it; its classification list is recorded here).
2. **disloc-demonstrative-drama-dialogue** (already queued, P3): dialogue-
   register extension, if the red team wants it.

Note for the supervisor: `disloc-demonstrative-drama-reissue` already
exists in the queue — do not create a duplicate follow-up from this report.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-disloc-demonstrative-drama-ingest.md`
- Lock `locks/disloc-demonstrative-drama-ingest.lock`: created on start,
  deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched.
- No standing or red-team verdict contradicted or downgraded; §7 intact.
