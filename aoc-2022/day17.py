rocks = [
    [0b0011110],
    [
        0b0001000,
        0b0011100,
        0b0001000,
    ],
    [
        0b0011100,
        0b0010000,
        0b0010000,
    ],
    [
        0b0000100,
        0b0000100,
        0b0000100,
        0b0000100,
    ],
    [
        0b0001100,
        0b0001100,
    ],
]

with open("day17.in") as f:
    inp = f.read().strip()


def overlap(rock, height, tower) -> bool:
    if height <= 0:
        return False
    for i in range(len(rock)):
        if height <= i:
            return False
        if rock[i] & tower[len(tower) - 1 - height + i] != 0:
            return True
    return False


# 1234
# 1234567
# 0000000x
# 000x000


# Tower will be upside down
tower = [
    0b1111111,
    0b1111111,
    0b1111111,
    0b1111111,
]
new = True
height = -3
count = 0
rock = []
rock_id = 0
i = 0

while count <= 2022:
    if new:
        count += 1
        height = -3
        rock = rocks[rock_id]
        rock_id = (rock_id + 1) % 5
        new = False
    match inp[i % len(inp)]:
        case ">":
            if all(row & 0b1000000 == 0 for row in rock):
                rock = [row << 1 for row in rock]
            if overlap(rock, height, tower):
                rock = [row >> 1 for row in rock]
        case "<":
            if all(row & 0b0000001 == 0 for row in rock):
                rock = [row >> 1 for row in rock]
            if overlap(rock, height, tower):
                rock = [row << 1 for row in rock]
    height += 1
    if overlap(rock, height, tower):
        height -= 1
        # Place rock
        for i in range(len(rock)):
            if height <= i:
                tower.append(rock[i])
            else:
                tower[len(tower) - 1 - height + i] |= rock[i]
        new = True
    i += 1

print(len(tower))
