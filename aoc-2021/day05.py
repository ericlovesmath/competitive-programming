import re

with open("day05.in") as f:
    inp = f.read().strip().splitlines()
    inp = [[int(i) for i in re.findall(r"\d+", row)] for row in inp]

board = [[0 for _ in range(1000)] for _ in range(1000)]

for row in inp:
    x1, y1, x2, y2 = row

    d = max(abs(x2 - x1), abs(y2 - y1)) + 1
    dx = 0 if x1 == x2 else 1 if x1 < x2 else -1
    dy = 0 if y1 == y2 else 1 if y1 < y2 else -1

    # For Part 1
    # if dx != 0 and dy != 0:
    #     continue

    for i in range(d):
        board[x1 + dx * i][y1 + dy * i] += 1

print(sum(c > 1 for row in board for c in row))
