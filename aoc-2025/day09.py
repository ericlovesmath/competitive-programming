from shapely.geometry import Polygon

with open("day09.in") as f:
    inp = [tuple(map(int, row.split(","))) for row in f.read().strip().splitlines()]

ans = 0
for x, y in inp:
    for i, j in inp:
        area = (abs(x - i) + 1) * (abs(y - j) + 1)
        ans = max(ans, area)

print(ans)

shape = Polygon(inp)

ans = 0
for x, y in inp:
    for i, j in inp:
        rect = Polygon([(x, y), (x, j), (i, j), (i, y)])

        if shape.contains(rect):
            ans = max(ans, int(rect.area))

print(ans)
