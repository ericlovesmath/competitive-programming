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

for i in range(1000000):
    seen = set()
    for [px, py, vx, vy] in inp:
        x = (px + i * vx) % 101
        y = (py + i * vy) % 103
        seen.add((x, y))
    if len(seen) == len(inp):
        print(i)
        break
