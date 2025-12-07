from collections import defaultdict
with open("day07.in") as f:
    inp = f.read().strip().splitlines()
    N, M = len(inp), len(inp[0])
    beam = inp[0].index("S")

count = 0
beams = defaultdict(int)
beams[beam] = 1
for i in range(1, N):
    splitters = [j for j in range(M) if inp[i][j] == "^"]
    next = defaultdict(int)
    for b in beams:
        if b in splitters:
            next[b-1] += beams[b]
            next[b+1] += beams[b]
            count += 1
        else:
            next[b] += beams[b]
    beams = next

print(count)
print(sum(beams[b] for b in beams))
