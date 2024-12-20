from collections import deque
from itertools import product

with open("day20.in") as f:
    inp = f.read().strip().splitlines()
    inp = [list(s) for s in inp]
    N = len(inp)

    start = end = None
    for r in range(N):
        for c in range(N):
            if inp[r][c] == "S":
                start = (r, c)
            if inp[r][c] == "E":
                end = (r, c)


def bfs(start, end):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        (x, y), dist = queue.popleft()

        if inp[x][y] == "#":
            continue

        if (x, y) == end:
            return dist

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), dist + 1))

    return -1


from_start = [[bfs((x, y), start) for y in range(N)] for x in range(N)]
from_end = [[bfs((x, y), end) for y in range(N)] for x in range(N)]

path = bfs(start, end)

def solve(cheat):
    count = 0
    for (sx, sy) in product(range(N), range(N)):
        for (ex, ey) in product(range(N), range(N)):
            gap = abs(sx - ex) + abs(sy - ey)
            if (gap <= cheat and
                inp[sx][sy] != "#" and
                inp[ex][ey] != "#" and
                from_start[sx][sy] != -1 and
                from_end[ex][ey] != -1 and
                path - (from_start[sx][sy] + from_end[ex][ey] + gap) >= 100):
                    count += 1
    return count

print(solve(2))
print(solve(20))
