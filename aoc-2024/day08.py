with open("day08.in") as f:
    inp = f.read().strip().splitlines()
    N = len(inp)

towers = {}
for i, row in enumerate(inp):
    for j, c in enumerate(row):
        if c == ".":
            continue
        if c not in towers:
            towers[c] = []
        towers[c].append(i + j * 1j)

nodes = set()
for c in towers:
    cands = towers[c]
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            d = cands[j] - cands[i]
            for m in range(0, N):
                nodes.add((cands[i] - d * m))
                nodes.add((cands[j] + d * m))

nodes = [n for n in nodes if 0 <= n.real < N and 0 <= n.imag < N]
print(len(nodes))
