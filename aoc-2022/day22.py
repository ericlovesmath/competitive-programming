import re

with open("day22.in") as f:
    board, path = f.read().split("\n\n")

    # Parse Input
    board = board.splitlines()

    HEIGHT = len(board)
    WIDTH = max(len(row) for row in board)

    board = [row.ljust(WIDTH) for row in board]

    path = [
        val if val in "LR" else int(val)
        for val in re.split(r"(R|L)", path.strip())
    ]

# Generate horizontal and vertical "portals" for edges
portal = {}
for x in range(HEIGHT):
    in_walls = False
    left, right = 0, WIDTH - 1
    for y in range(WIDTH):
        if not in_walls:
            if board[x][y] != " ":
                left = y
                in_walls = True
        else:
            if board[x][y] == " ":
                right = y - 1
                break
    portal[(x, right + 1)] = (x, left)
    portal[(x, left - 1)] = (x, right)

for y in range(WIDTH):
    in_walls = False
    up, down = 0, HEIGHT - 1
    for x in range(HEIGHT):
        if not in_walls:
            if board[x][y] != " ":
                up = x
                in_walls = True
        else:
            if board[x][y] == " ":
                down = x - 1
                break
    portal[(down + 1, y)] = (up, y)
    portal[(up - 1, y)] = (down, y)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

pos = (0, board[0].index("."))
dir = 0

# print(portal.keys())

for move in path:
    if move == "L":
        dir = (dir - 1) % 4
    elif move == "R":
        dir = (dir + 1) % 4
    else:
        for _ in range(move):
            next = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
            if next in portal:
                next = portal[next]
            if board[next[0] % HEIGHT][next[1] % WIDTH] == ".":
                pos = next
            else:
                break

print(pos, dir)
print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + dir)
