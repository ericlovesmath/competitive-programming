with open("day04.in") as f:
    inp = [[c == "@" for c in row] for row in f.read().strip().splitlines()]
    N = len(inp)
    assert(len(inp) == len(inp[0]))

def neighbors(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            i, j = x + dx, y + dy
            if 0 <= i < N and 0 <= j < N:
                yield (i, j)

def movable(inp):
    moved = []
    for x in range(N):
        for y in range(N):
            if not inp[x][y]:
                continue
            count = 0
            for (i, j) in neighbors(x, y):
                if inp[i][j]:
                    count += 1
            if count < 4:
                moved.append((x, y))
    return moved

print(len(movable(inp)))

c = 0
while len(movable(inp)) > 0:
    for (i, j) in movable(inp):
        c += 1
        inp[i][j] = False
print(c)
    
