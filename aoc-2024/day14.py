import zlib
import re

with open("day14.in") as f:
    inp = f.read().strip().splitlines()
    inp = [[int(i) for i in re.findall(r"-?\d+", row)] for row in inp]

N, M = 101 // 2, 103 // 2
a, b, c, d = 0, 0, 0, 0
for [px, py, vx, vy] in inp:
    x = (px + 100 * vx) % 101
    y = (py + 100 * vy) % 103
    if x < N and y < M:
        a += 1
    if x > N and y < M:
        b += 1
    if x < N and y > M:
        c += 1
    if x > N and y > M:
        d += 1

print(a * b * c * d)

best = ""
res = None
min_entropy = 1000000

for steps in range(10000):
    seen = set()
    for [px, py, vx, vy] in inp:
        x = (px + steps * vx) % 101
        y = (py + steps * vy) % 103
        seen.add((x, y))

    s = ""
    for i in range(103):
        for j in range(101):
            if (i, j) in seen:
                s += "O"
            else:
                s += "."
        s += "\n"

    entropy = len(zlib.compress(s.encode()))

    if entropy < min_entropy:
        best = s
        res = steps
        min_entropy = entropy

print(best)
print(res)
