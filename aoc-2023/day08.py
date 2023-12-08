from math import lcm

with open("day08.in") as f:
    dirs, rows = f.read().strip().split("\n\n")
    N = len(dirs)
    paths = {}
    for row in rows.splitlines():
        paths[row[0:3]] = (row[7:10], row[12:15])

# PROBLEM 1: RANK 231
curr = "AAA"
i = 0
while curr != "ZZZ":
    curr = paths[curr][dirs[i % N] == "R"]
    i += 1
print(i)

# PROBLEM 2: RANK 72

steps = []
for curr in filter(lambda path: path[2] == "A", paths):
    i = 0
    while curr[2] != "Z":
        curr = paths[curr][dirs[i % N] == "R"]
        i += 1
    steps.append(i)

print(lcm(*steps))
