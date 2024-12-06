with open("day06.in") as f:
    inp = [list(s) for s in f.read().strip().splitlines()]
    N, M = len(inp), len(inp[0])
    M = len(inp[0])
    start = (0, 0)
    for i in range(N):
        for j in range(M):
            if inp[i][j] == "^":
                start = (i, j)

turn = {
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
}

curr = start
dir = (-1, 0)
visited = set()
while True:
    visited.add(curr)
    next = (curr[0] + dir[0], curr[1] + dir[1])
    if not (0 <= next[0] < N and 0 <= next[1] < M):
        break
    if inp[next[0]][next[1]] == "#":
        dir = turn[dir]
    else:
        curr = next

print(len(visited))

COPY = inp.copy()

stuck = 0
for i in range(N):
    for j in range(M):
        if (i, j) == start:
            continue

        inp = [[s for s in row] for row in COPY]
        inp[i][j] = "#"
        curr = start
        dir = (-1, 0)
        visited = set()

        while True:
            if (curr, dir) in visited:
                stuck += 1
                break

            visited.add((curr, dir))
            next = (curr[0] + dir[0], curr[1] + dir[1])

            if not (0 <= next[0] < N and 0 <= next[1] < M):
                break
            if inp[next[0]][next[1]] == "#":
                dir = turn[dir]
            else:
                curr = next
print(stuck)
