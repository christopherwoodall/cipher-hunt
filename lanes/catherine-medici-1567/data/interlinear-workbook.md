# Interlinear transcription workbook — Charles IX -> du Croc (Lasry 2022)
# Source: data/lasry-charlesIX-decipher-recto.png / -verso.png
# Method: black cipher glyphs segmented per row (connected components), viewed
#   enlarged in strips (/tmp/vN_strip.png, /tmp/rN_strip.png); red plaintext read
#   from 3x row crops; paired by vertical column alignment.
# Pairing direction: red ABOVE <-> black BELOW (proven by "≠1"->"QUE" anchor,
#   verso row 0: small red "Que" sits directly above black "≠1").
# Glyph naming: visual ASCII approximation. "~" prefix = uncertain glyph ID.
# Letter in CAPS = red plaintext letter. "(null)" = glyph under red word-space.
# "QUE" nomenclator: black "≠"+"1" (two glyphs) -> Q,u,e.

## VERSO ROW 0
# red: D E D O N N E R O R D R E _ Que L E S _ A N G L O I S N E N P I E T E N T A V C V
# ("DE DONNER ORDRE Que LES ANGLOIS NEN PIETENT AV CV")
# Evidence: /tmp/v0_start.png (6x, x0-200: letters 1-13), /tmp/v0_que_anchor.png (8x: "E_QueLES_AN")
1. 9c -> D        [v0_start: 9c directly under D]
2. 1 -> E         [v0_start: under E]
3. 5 -> D         [v0_start: under D]
4. + -> O         [v0_start: under O]
5. inf -> N       [v0_start: under N]
6. x -> N         [v0_start: under 2nd N]  NOTE conflicts with #13 x->E below
7. dash -> E      [v0_start: under E; glyph is short horizontal stroke]
8. SIGMA -> R     [v0_start: under R]
9. alpha -> O     [v0_start: under O]
10. 7 -> R        [v0_start: under R]
11. alpha -> D    [v0_start: under D]
12. 7 -> R        [v0_start: under R]
13. x -> E        [v0_que_anchor: x directly under E]  CONFLICT with #6
14. 9 -> (null)   [v0_que_anchor: 9 under red word-space]  NOTE shape ~ #1 9c; treated as distinct-or-null, UNCERTAIN
15. neq -> Q }    [v0_que_anchor: "≠1" under small red "Que"]
16. 1 -> u,e }    [two glyphs -> Q,u,e; split unknown, record as digraph]
17. DELTA -> L    [v0_que_anchor: under L]
18. h -> E        [v0_que_anchor: under E]
19. xi -> S       [v0_que_anchor: under S]
# --- remainder of row 0 (glyphs 20-40) paired by strip order vs red order;
# --- column alignment NOT individually verified: mark ~uncertain
20. ~s_curl -> A
21. ~zeta -> N
22. ~+ -> G
23. ~+ -> L
24. ~s -> O
25. ~OMEGA -> I
26. ~f -> S
27. ~9c -> N
28. ~xi -> E
29. ~f -> N
30. ~8 -> P
31. ~x -> I
32. ~theta -> E
33. ~9c -> T
34. ~f -> E
35. ~qmark -> N
36. ~3 -> T
37. ~6 -> A
38. ~r -> V
39. ~LAMBDA -> C
40. ~R -> V
