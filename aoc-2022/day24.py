import sys
from functools import cache

with open("day24.in") as f:
    board = f.read().strip().splitlines()
    HEIGHT = len(board) - 2
    WIDTH = len(board[0]) - 2

    R, L, U, D = set(), set(), set(), set()

    for x in range(HEIGHT):
        for y in range(WIDTH):
            match board[x + 1][y + 1]:
                case ">": R.add((x, y))
                case "<": L.add((x, y))
                case "^": U.add((x, y))
                case "v": D.add((x, y))


@cache
def state(time):
    return (
        set(((x + time) % HEIGHT, y) for x, y in D) |
        set(((x - time) % HEIGHT, y) for x, y in U) |
        set((x, (y - time) % WIDTH) for x, y in L) |
        set((x, (y + time) % WIDTH) for x, y in R)
    )

LIM = 500 # Increase until this is no longer the answer

@cache
def travel(x: int, y: int, time: int):
    if time == LIM:
        return sys.maxsize
    if (x, y) == (HEIGHT - 1, WIDTH - 1):
        # return time
        return travel_back(x, y, time)
    SPEED = sys.maxsize
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)):
        to = (x + dx, y + dy)
        if 0 <= to[0] < HEIGHT and 0 <= to[1] < WIDTH \
                and to not in state((time + 1) % (HEIGHT * WIDTH)):
            SPEED = min(travel(to[0], to[1], time + 1), SPEED)

    return SPEED

@cache
def travel_back(x: int, y: int, time: int):
    if time == LIM:
        return sys.maxsize
    if (x, y) == (0, 0):
        return time
    SPEED = sys.maxsize
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)):
        to = (x + dx, y + dy)
        if 0 <= to[0] < HEIGHT and 0 <= to[1] < WIDTH \
                and to not in state((time + 1) % (HEIGHT * WIDTH)):
            SPEED = min(travel(to[0], to[1], time + 1), SPEED)

    return SPEED

print(travel(0, 0, 2) + 1)
