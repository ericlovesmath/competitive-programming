from collections import deque

with open("day18.in") as f:
    inp = f.read().strip().splitlines()
    inp = [row.split(",") for row in inp]
    inp = [(int(row[0]), int(row[1])) for row in inp]
    N = 70


def bfs(grid):
    queue = deque([(0, 0, 0)])
    visited = set([(0, 0)])

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == (N, N):
            return steps

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            i, j = x + dx, y + dy
            if 0 <= i <= N and 0 <= j <= N and (i, j) not in visited and grid[i][j]:
                visited.add((i, j))
                queue.append((i, j, steps + 1))

    return None


grid = [[True for _ in range(N + 1)] for _ in range(N + 1)]

for i, (x, y) in enumerate(inp):
    grid[x][y] = False
    min_steps = bfs(grid)
    if i == 1024:
        print(min_steps)
    if min_steps is None:
        print((x, y))
        break
