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
    portal[(x, right, 0)] = (x, left, 0)
    portal[(x, left, 2)] = (x, right, 2)

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
    portal[(down, y, 1)] = (up, y, 1)
    portal[(up, y, 3)] = (down, y, 3)

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
            next = (pos[0], pos[1], dir)
            if next in portal:
                x, y, new_dir = portal[next]
                x, y = x + dirs[new_dir][0], y + dirs[new_dir][1]
            else:
                x, y = next[0] + dirs[dir][0], next[1] + dirs[dir][1]
            x, y = x % HEIGHT, y % HEIGHT

            if board[x][y] == ".":
                pos = (x, y)
            else:
                break

print(pos, dir)
print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + dir)
