# Battery protocol — crowd17 next-token pipeline

Worker brief. Read this whole file before touching anything.

## 1. Take a target

1. Read `battery-queue.json`. Pick the highest-priority `status: "queued"` target
   with no lockfile in `locks/` (see §6). Priority 1 first.
2. Create `locks/<id>.lock` containing your agent id + UTC timestamp. One worker
   per target. If a lock is older than 90 minutes, it is stale: note it in your
   report and proceed (the previous worker died).

## 2. Pre-register the bar BEFORE testing

Copy the target's `bars` field into your report verbatim, then restate it as
numbered pass/fail clauses. Do not modify the bar after seeing data. If the
bar is genuinely untestable as written, record that as a finding (counts as a
null, §4) — do not silently rewrite it.

## 3. Test ONLY against the repaired stream

- Stream: the 1,847-pair parse from `code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`.
- **Never use `code/side-keyhunt/canonical.py`** — it reads the obsolete 1,846-pair parse.
- Never touch R5005. Never invent data. Every number traces to the stream.

## 4. Verdicts

- **promote** — all bar clauses pass AND every listed adverse is answered
  (answered = re-parsed cleanly, fenced with stated cause, or shown to be a
  misread — not ignored).
- **kill** — a bar clause fails at kill grade (a window forces the claim false,
  or a distributional test rejects at the lane's standard), or a cleaner rival
  value is demonstrated on the same frames.
- **null** — inconclusive. **A null MUST propose 1–3 follow-up targets**
  (narrower bars, discriminating frames, or a rival value to test). Nulls
  regenerate work; they never end it. Write the follow-ups into your report;
  the supervisor queues them.

## 5. Report and record

1. Write `code/crowd17/report_inbox/battery-<id>.md`:
   bar (verbatim + numbered clauses), method, window-level evidence with
   @-offsets, per-clause pass/fail, verdict, and (for nulls) the 1–3 follow-ups.
2. Update `battery-queue.json`: set the target's `status` to `"verdict"` and
   fill `verdict: {"result": "promote|kill|null", "report": "code/crowd17/report_inbox/battery-<id>.md", "date": "YYYY-MM-DD"}`.
   Never downgrade an existing verdict. If your result contradicts a standing
   red-team verdict, do NOT overwrite it — mark your result `"null"` with the
   contradiction as the headline and escalate to the red team.
3. Delete your lockfile.

## 6. Locks

`locks/<id>.lock` — created on start (agent id + UTC timestamp), deleted on
completion. Stale after 90 minutes: re-dispatchable, with a note.

## 7. Standing constraints (not negotiable)

- Banked ground truth (pencil): 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
- Promoted/granted: 87=ce, 64=qui, 96=par, 17=fois,
  79="tout" (A5), 00="pour" (A9, leg-1 class-level), 84="on" (A15, conditions C1–C3),
  47="ce" (A4, allophone tier).
- Provisional: 59=est, 77="le".
- Frames granted (value open): 37/32/42 predicative (A1), 80/89 verb-frames (A8),
  85 verb-stem (A3), 37-01 unit (A12), "tout me [48-verb]" (A7-L2).
- Kills hold: 20="fois", 81="prin", 48="est"/"ne"/"de", {48,94} homophone-set,
  09/92 "-ère" value, 84="fait" (superseded by 84="on").
- Splits hold: 20~17, 23~26. Holds hold: 19 (1 leg), 45="ce" (A11), 09~92 (A6), 33+29 (A10).
- 67 et/veut is the sole true polyvalence; positional resolution rule stands
  (67="veut" iff follower infinitive-shaped).
- 1690 frequency uniformity is necessary but insufficient for homophony.
- Canonicality caveat stands: pencil gloss on row a5_03; 68 of 70 upstream
  row offsets unvalidated.

## 8. What "done" looks like

Target verdict recorded in `battery-queue.json`, report filed, lock deleted,
no invented numbers, adverses answered or fenced — never ignored.
