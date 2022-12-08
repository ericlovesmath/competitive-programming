import os

script_dir = os.path.dirname(__file__)

with open(os.path.join(script_dir, "day08.in")) as f:
    inp = f.read().strip().split("\n")
    inp = [list(map(int, list(row))) for row in inp]

WIDTH = len(inp)
HEIGHT = len(inp[0])

count = 0
for x in range(1, WIDTH - 1):
    for y in range(1, HEIGHT - 1):
        if all(inp[i][y] < inp[x][y] for i in range(0, x)) or \
           all(inp[i][y] < inp[x][y] for i in range(x + 1, HEIGHT)) or \
           all(inp[x][i] < inp[x][y] for i in range(0, y)) or \
           all(inp[x][i] < inp[x][y] for i in range(y + 1, WIDTH)):
               count += 1

print(count + 2 * WIDTH + 2 * HEIGHT - 4)

max_score = 0
for x in range(1, WIDTH - 1):
    for y in range(1, HEIGHT - 1):
        L = R = D = U = 1

        i = x - 1
        while i > 0 and inp[i][y] < inp[x][y]:
            i -= 1
            L += 1

        i = x + 1
        while i < WIDTH - 1 and inp[i][y] < inp[x][y]:
            i += 1
            R += 1

        i = y - 1
        while i > 0 and inp[x][i] < inp[x][y]:
            i -= 1
            D += 1

        i = y + 1
        while i < HEIGHT - 1 and inp[x][i] < inp[x][y]:
            i += 1
            U += 1

        max_score = max(max_score, L * R * D * U)

print(max_score)
