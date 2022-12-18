import re
import sys

with open("day18.in") as f:
    inp = set(
        tuple(map(int, re.findall(r"\d+", row)))
        for row in f.read().strip().splitlines()
    )

# We want to count adjacents
# Each adjacent removes 2 from the total surface area


def adj(L, R):
    if L[0] - R[0] == 0 and L[1] - R[1] == 0 and abs(L[2] - R[2]) == 1:
        return True
    if L[1] - R[1] == 0 and L[2] - R[2] == 0 and abs(L[0] - R[0]) == 1:
        return True
    if L[2] - R[2] == 0 and L[0] - R[0] == 0 and abs(L[1] - R[1]) == 1:
        return True
    return False


total = len(inp) * 6
for left in inp:
    for right in inp:
        if adj(left, right):
            total -= 1  # left, right and right, left contribute 1 each

print(total)

# Part 2
# We want to perform BFS from (0, 0, 0), an "open source"
# Even if visited already (wall), we will track it multiple times
# If we visit it twice, it has 2 external faces, ex.

X_MAX, X_MIN = max(row[0] for row in inp), min(row[0] for row in inp)
Y_MAX, Y_MIN = max(row[1] for row in inp), min(row[1] for row in inp)
Z_MAX, Z_MIN = max(row[2] for row in inp), min(row[2] for row in inp)

MAX = max(X_MAX, Y_MAX, Z_MAX) + 5  # 5 is arbitrary

# We only care about ~20x20x20 box for my test case
# We shift by +1 on each axis to account for (0, _, _) types

visited = [[[0 for _ in range(MAX)] for _ in range(MAX)] for _ in range(MAX)]

sys.setrecursionlimit(100000000)  # Ignore me please


def dfs(x: int, y: int, z: int):
    if x < 0 or x >= MAX or y < 0 or y >= MAX or z < 0 or z >= MAX:
        return

    if (x - 1, y - 1, z - 1) in inp:
        visited[x][y][z] += 1
        return

    if visited[x][y][z] > 0:
        return

    visited[x][y][z] = 1

    dfs(x - 1, y, z)
    dfs(x + 1, y, z)
    dfs(x, y - 1, z)
    dfs(x, y + 1, z)
    dfs(x, y, z - 1)
    dfs(x, y, z + 1)


dfs(0, 0, 0)

print(sum(visited[val[0] + 1][val[1] + 1][val[2] + 1] for val in inp))
