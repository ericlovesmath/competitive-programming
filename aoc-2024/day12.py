from collections import deque

with open("day12.in") as f:
    inp = [list(row) for row in f.read().strip().splitlines()]
    N = len(inp)

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def neighbors(x, y):
    for (dx, dy) in DIRS:
        i, j = x + dx, y + dy
        if 0 <= i < N and 0 <= j < N:
            yield (i, j)

part1 = 0
part2 = 0

visited = set()
for i in range(N):
    for j in range(N):

        if (i, j) in visited:
            continue

        area = 0
        border = { dir: set() for dir in DIRS }
        q = deque([(i, j)])
        while q:
            cx, cy = q.popleft()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            area += 1
            for dx, dy in DIRS:
                nx = cx + dx
                ny = cy + dy
                if 0 <= nx < N and 0 <= ny < N and inp[nx][ny] == inp[cx][cy]:
                    q.append((nx, ny))
                else:
                    border[(dx, dy)].add((cx, cy))

        # We're basically just counting connected components
        sides = 0
        for squares in border.values():
            seen = set()
            for x, y in squares:
                if (x, y) in seen:
                    continue
                sides += 1
                q = deque([(x, y)])
                while q:
                    cx, cy = q.popleft()
                    if (cx, cy) in seen:
                        continue
                    seen.add((cx, cy))
                    for (nx, ny) in neighbors(cx, cy):
                        if (nx, ny) in squares:
                            q.append((nx, ny))

        perim = sum(len(n) for n in border.values())
        part1 += area * perim
        part2 += area * sides

print(part1)
print(part2)
