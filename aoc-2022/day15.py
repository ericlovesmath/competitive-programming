import re

with open("day15.in") as f:
    inp = [
        list(map(int, re.findall(r"-?\d+", row)))
        for row in f.read().strip().splitlines()
    ]


def dist(row) -> int:
    return abs(row[0] - row[2]) + abs(row[1] - row[3])


ROWS, TARGET = 5000000, 2000000
# ROWS, TARGET = 50, 10

count = 0
for x in range(-ROWS, ROWS):
    if any(dist(row) >= dist([row[0], row[1], x, TARGET]) for row in inp):
        if all([row[2], row[3]] != [x, TARGET] for row in inp):
            count += 1
    if x % 100000 == 0:
        print(x)
print(count)

for x in range(0, 4000001):
    for y in range(0, 4000001):
        if all(dist(row) < dist([row[0], row[1], x, y]) for row in inp):
            print(x, y)
            break
        if x % 100000 == 0 and y % 100000 == 0:
            print(x, y)
