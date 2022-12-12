from typing import Any

with open("day12.in") as f:
    start = (0, 0)
    end = (0, 0)
    inp: Any = [list(row) for row in f.read().strip().splitlines()]
    for x in range(len(inp)):
        for y in range(len(inp[0])):
            if inp[x][y] == "S":
                inp[x][y] = 0
                start = (x, y)
            elif inp[x][y] == "E":
                end = (x, y)
                inp[x][y] = 27
            else:
                inp[x][y] = int(ord(inp[x][y]) - ord("a") + 1)

ROWS, COLS = len(inp), len(inp[0])

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
# queue = [start]
queue = [end]
depth = 0

# while len(queue) > 0 and end not in queue:
while len(queue) > 0 and all(inp[x][y] != 1 for x, y in queue):
    for _ in range(len(queue)):

        x, y = queue.pop(0)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x == ROWS or new_y < 0 or new_y == COLS:
                continue
            if visited[new_x][new_y]:
                continue
            # if inp[new_x][new_y] - inp[x][y] <= 1:
            if inp[x][y] - inp[new_x][new_y] <= 1:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))

    depth += 1

print(depth)
