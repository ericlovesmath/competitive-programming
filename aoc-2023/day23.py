from collections import defaultdict

with open("day23.in") as f:
    inp = f.read().strip().splitlines()
    N = len(inp)


# Basic DFS
def max_path(adj):
    stack: list[tuple[int, int, int]] = [(0, 1, 0)]  # (x, y, dist)
    visited = set()
    max_dist = 0
    while stack:
        x, y, dist = stack.pop()
        if dist == -1:
            visited.remove((x, y))
            continue
        if (x, y) == (N - 1, N - 2):
            max_dist = max(max_dist, dist)
            continue
        if (x, y) in visited:
            continue
        visited.add((x, y))
        stack.append((x, y, -1))  # Block looping path until clear
        for xx, yy, ddist in adj[(x, y)]:
            stack.append((xx, yy, dist + ddist))

    return max_dist


adj = defaultdict(lambda: set())
for x in range(N):
    for y in range(N):
        match inp[x][y]:
            case ".":
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    xx, yy = x + dx, y + dy
                    if not (0 <= xx < N and 0 <= yy < N):
                        continue
                    if inp[xx][yy] == ".":
                        adj[(x, y)].add((xx, yy, 1))
                        adj[(xx, yy)].add((x, y, 1))
            case ">":
                adj[(x, y)].add((x, y + 1, 1))
                adj[(x, y - 1)].add((x, y, 1))
            case "v":
                adj[(x, y)].add((x + 1, y, 1))
                adj[(x - 1, y)].add((x, y, 1))

print("Part 1:", max_path(adj))

adj = defaultdict(lambda: set())
for x in range(N):
    for y in range(N):
        if inp[x][y] in ".>v":
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx, yy = x + dx, y + dy
                if not (0 <= xx < N and 0 <= yy < N):
                    continue
                if inp[xx][yy] in ".>v":
                    adj[(x, y)].add((xx, yy, 1))
                    adj[(xx, yy)].add((x, y, 1))

# Compress paths with no intersection (deg == 2)
# There are probably better ways to do this.
while True:
    for (x, y), adjs in adj.items():
        if len(adjs) == 2:
            (xl, yl, dl), (xr, yr, dr) = adjs
            adj[(xl, yl)].remove((x, y, dl))
            adj[(xr, yr)].remove((x, y, dr))
            adj[(xl, yl)].add((xr, yr, dl + dr))
            adj[(xr, yr)].add((xl, yl, dl + dr))
            del adj[(x, y)]
            break
    else:
        break

print("Part 2:", max_path(adj))
