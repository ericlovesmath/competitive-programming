with open("day10.in") as f:
    inp = f.read().strip().splitlines()
    inp = [[int(i) for i in row] for row in inp]
    N = len(inp)

def neighbors(x, y):
    for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        i, j = x + dx, y + dy
        if 0 <= i < N and 0 <= j < N:
            yield (i, j)

def search(x, y, n):
    if n == 10:
        return [(x, y)]

    count = []
    for (i, j) in neighbors(x, y):
        if inp[i][j] == n:
            count.extend(search(i, j, n + 1))
    return count

part1 = 0
part2 = 0
for i in range(N):
    for j in range(N):
        if inp[i][j] == 0:
            dsts = search(i, j, 1)
            part1 += len(set(dsts))
            part2 += len(dsts)

print(part1)
print(part2)
