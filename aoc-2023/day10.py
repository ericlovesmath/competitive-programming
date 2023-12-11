from sys import setrecursionlimit

with open("day10.in") as f:
    inp = f.read().strip().splitlines()
    N, M = len(inp), len(inp[0])

adj = {(i, j): [] for i in range(N) for j in range(M)}
start = None

for i in range(N):
    for j in range(M):
        if inp[i][j] == "S":
            start = (i, j)
        if inp[i][j] in "-LFS" and (j + 1 != M and inp[i][j + 1] in "-J7S"):
            adj[(i, j)].append((i, j + 1))
            adj[(i, j + 1)].append((i, j))
        if inp[i][j] in "|7FS" and (i + 1 != N and inp[i + 1][j] in "|LJS"):
            adj[(i, j)].append((i + 1, j))
            adj[(i + 1, j)].append((i, j))

setrecursionlimit(20000)

# Shoelace Formula, note that (*1/2) is done at end
visited = set()
def dfs(curr, prev, area, depth):
    area += prev[0] * curr[1] - curr[0] * prev[1]
    if curr == start and depth > 2:
        return (depth // 2, (abs(area) - depth) // 2 + 1)
    if curr in visited:
        return None
    visited.add(curr)
    for next in adj[curr]:
        ans = dfs(next, curr, area, depth + 1)
        if ans is not None:
            return ans

print(dfs(start, start, 0, 0))
