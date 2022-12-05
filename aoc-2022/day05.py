import os
import re

script_dir = os.path.dirname(__file__)

with open(os.path.join(script_dir, "day05.in")) as f:
    inp = f.read().strip().split("\n")
    inp.pop(0)

# Parsing Data

TOTAL_ROWS = 8
TOTAL_COLS = 9

towers = [[] for _ in range(TOTAL_COLS)]
for row in range(TOTAL_ROWS - 1, -1, -1):
    for i in range(0, len(inp[row]), 4):
        if inp[row][i] != " ":
            towers[i//4].append(inp[row][i + 1])

moves = [list(map(int, re.findall(r'\d+', row))) for row in inp[TOTAL_ROWS + 2:]]

# for move in moves:
#     amount, source, target = move
#     for _ in range(amount):
#         towers[target-1].append(towers[source-1].pop())

for move in moves:
    amount, source, target = move
    towers[target-1].extend(towers[source-1][-amount:])
    del towers[source-1][-amount:]

print("".join(row[-1] for row in towers))
