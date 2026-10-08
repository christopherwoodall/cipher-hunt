import streamkit as s
def dump(name, lines):
    open(f"context/{name}.txt", "w").write("\n".join([f"### {name}"] + lines) + "\n")
for g in (37, 32, 42, 19):
    L = s.starts(59, g)
    lines = [f"59->{g}: n={len(L)} @ {L}"]
    for i in L:
        lines.append(f"  @{i}: pre={s.P[i-1]} | {s.ctx_gloss(i,3,3)} | suc={s.P[i+1] if i+1 < len(s.P) else '?'}")
    lines.append(f"  59 suc profile: {sorted(s.suc_c(59).items())}")
    dump(f"est-{g}", lines)
dump("ce47-en-window", [
  f"24->47: {[i for i in s.starts(47) if s.P[i-1]==24]}",
  f"24->87: {[i for i in s.starts(87) if s.P[i-1]==24]}",
  f"47 pre: {sorted(s.pre_c(47).items())} suc: {sorted(s.suc_c(47).items())}",
  f"87 pre: {sorted(s.pre_c(87).items())} suc: {sorted(s.suc_c(87).items())}",
  f"47->33 starts: {[i for i in s.starts(47,33)]}",
  f"87->33 starts: {[i for i in s.starts(87,33)]}",
])
dump("ce47-windows", [f"  @{i}: {s.ctx_gloss(i,2,2)}" for i in s.starts(47)])
dump("tout-windows", [f"  @{i}: {s.ctx_gloss(i,2,3)}" for i in s.starts(79)] + [f"79 pre: {sorted(s.pre_c(79).items())} suc: {sorted(s.suc_c(79).items())}"])
dump("pour-windows", [f"00 n={s.G[0]}"] + [f"  @{i}: {s.ctx_gloss(i,2,3)}" for i in s.starts(0)] + [f"00 pre: {sorted(s.pre_c(0).items())}"])
dump("fois-windows", [f"17 n={s.G[17]}"] + [f"  @{i}: {s.ctx_gloss(i,3,3)}" for i in s.starts(17)] + [f"17 pre: {sorted(s.pre_c(17).items())} suc: {sorted(s.suc_c(17).items())}"])
dump("le-windows", [f"77 n={s.G[77]} pre: {sorted(s.pre_c(77).items())} suc: {sorted(s.suc_c(77).items())}"] + [f"  @{i}: {s.ctx_gloss(i,2,2)}" for i in s.starts(77)])
for g in (31, 33):
    dump(f"class-{g}", [f"{g} n={s.G[g]} pre: {sorted(s.pre_c(g).items())} suc: {sorted(s.suc_c(g).items())}"] + [f"  @{i}: {s.ctx_gloss(i,2,2)}" for i in s.starts(g)])
for g in (67, 78, 48, 94):
    dump(f"fork-{g}", [f"{g} n={s.G[g]} pre: {sorted(s.pre_c(g).items())} suc: {sorted(s.suc_c(g).items())}"])
dump("collision-62-84", [f"  62@{i}: {s.ctx_gloss(i,2,3)}" for i in s.starts(62)] + [f"  84@{i}: {s.ctx_gloss(i,2,3)}" for i in s.starts(84)])
lines = []
for g in (11,70,82,34,29,40):
    lines.append(f"{g} n={s.G[g]} pre: {sorted(s.pre_c(g).items())} suc: {sorted(s.suc_c(g).items())}")
dump("crib-words", lines)
dump("par-windows", [f"  @{i}: {s.ctx_gloss(i,3,3)}" for i in s.starts(96)])
print("context dumps written")
