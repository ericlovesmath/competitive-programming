with open("day09.in") as f:
    inp = [[int(i) for i in s] for s in f.read().strip().splitlines()]
    N, M = len(inp), len(inp[0])

def neighbors(x, y):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for (dx, dy) in d:
        i, j = x + dx, y + dy
        if 0 <= i < N and 0 <= j < M:
            yield (i, j)

lows = []
for i in range(N):
    for j in range(M):
        if all(inp[i][j] < inp[x][y] for (x, y) in neighbors(i, j)):
            lows.append((i, j))

print(sum(inp[i][j] + 1 for (i, j) in lows))

def search(i, j, visited):
    if (i, j) in visited:
        return
    visited.add((i, j))
    for (x, y) in neighbors(i, j):
        if inp[i][j] < inp[x][y] < 9:
            search(x, y, visited)

sizes = []
for (i, j) in lows:
    visited = set()
    search(i, j, visited)
    sizes.append(len(visited))

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
