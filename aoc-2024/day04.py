with open("day04.in") as f:
    inp = [list(row) for row in f.read().strip().splitlines()]
    N, M = len(inp), len(inp[0])

def rays(x, y):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1),
         (1, 1), (-1, 1), (-1, -1), (1, -1)]
    for (dx, dy) in d:
        if 0 <= x + 3 * dx < N and 0 <= y + 3 * dy < M:
            yield [inp[x + i * dx][y + i * dy] for i in range(4)]

count = 0
for x in range(N):
    for y in range(M):
        for ray in rays(x, y):
            if "".join(ray) == "XMAS":
                count += 1
print(count)

count = 0
for x in range(1, N - 1):
    for y in range(1, M - 1):
        if inp[x][y] != "A":
            continue
        if set([inp[x-1][y-1], inp[x+1][y+1]]) == \
           set([inp[x-1][y+1], inp[x+1][y-1]]) == \
           set("SM"):
            count += 1

print(count)
