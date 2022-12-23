import re
from functools import cache

with open("day23.in") as f:
    inp = f.read().strip().splitlines()
    elves = set()
    for x in range(len(inp)):
        for y in range(len(inp[0])):
            if inp[x][y] == "#":
                elves.add((x, y))

N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
NE, SE, SW, NW = (-1, 1), (1, 1), (1, -1), (-1, -1)
MOORE = (N, E, S, W, NE, SE, SW, NW)


def move(elf, dir):
    return (elf[0] + dir[0], elf[1] + dir[1])


proposal_checks = [
    [(N, NE, NW), N],
    [(S, SE, SW), S],
    [(W, NW, SW), W],
    [(E, NE, SE), E],
]

# for i in range(100000):
for i in range(10):

    proposals = {}
    count = {}

    for elf in elves:
        if any(move(elf, dir) in elves for dir in MOORE):
            for shift in range(4):
                dirs, proposal = proposal_checks[(i + shift) % 4]
                if all(move(elf, dir) not in elves for dir in dirs):
                    proposal = move(elf, proposal)
                    proposals[elf] = proposal
                    if proposal in count:
                        count[proposal] += 1
                    else:
                        count[proposal] = 1
                    break

    for elf, proposal in proposals.items():
        if count[proposal] == 1:
            elves.remove(elf)
            elves.add(proposal)

    # if len(proposals) == 0:
    #     print(i + 1)
    #     break

hori = [elf[0] for elf in elves]
vert = [elf[1] for elf in elves]
print((max(hori) - min(hori) + 1) * (max(vert) - min(vert) + 1) - len(elves))
