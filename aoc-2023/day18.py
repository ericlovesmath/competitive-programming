with open("day18.in") as f:
    inp = f.read().strip().splitlines()

# Shoelace
def get_area(inp):
    x, y = (0, 0)
    area = 0
    border = 0
    for ((dx, dy), dist) in inp:
        xx, yy = x + dx * dist, y + dy * dist
        area += x * yy - xx * y
        x, y = xx, yy
        border += dist
    return abs(area // 2) + (border // 2) + 1

def parse_1(inp):
    DIRS = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    for row in inp:
        dir, dist, _ = row.split(" ")
        yield DIRS[dir], int(dist)

def parse_2(inp):
    DIRS = {"3": (0, 1), "1": (0, -1), "0": (1, 0), "2": (-1, 0)}
    for row in inp:
        _, _, color = row.split(" ")
        yield DIRS[color[-2]], int(color[2:-2], 16)

print(get_area(parse_1(inp)))
print(get_area(parse_2(inp)))
