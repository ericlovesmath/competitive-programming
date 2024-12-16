from collections import deque
from copy import deepcopy

with open("day15.in") as f:
    inp, instrs = f.read().strip().split("\n\n")
    inp = inp.splitlines()
    inp = [list(row) for row in inp]
    instrs = "".join(c for c in instrs if c != "\n")


def solve(inp):
    N = len(inp)
    M = len(inp[0])
    inp = deepcopy(inp)

    # Get start, remove robot
    cx, cy = (0, 0)
    for i in range(N):
        for j in range(M):
            if inp[i][j] == "@":
                inp[i][j] = "."
                cx, cy = i, j

    for instr in instrs:
        dr, dc = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}[instr]
        nx, ny = cx + dr, cy + dc

        # Essentially graph search to get moved pieces
        q = deque([(cx, cy)])
        visited = set()
        blocked = False
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            i, j = x + dr, y + dc
            match inp[i][j]:
                case "#":
                    blocked = True
                    break
                case "O":
                    q.append((i, j))
                case "[":
                    q.extend([(i, j), (i, j + 1)])
                case "]":
                    q.extend([(i, j), (i, j - 1)])
        if blocked:
            continue

        cx, cy = nx, ny

        # Move blocks that can be moved, loop until done
        while len(visited) > 0:
            for x, y in visited.copy():
                i, j = x + dr, y + dc
                if (i, j) not in visited:
                    inp[i][j] = inp[x][y]
                    inp[x][y] = "."
                    visited.remove((x, y))

    res = 0
    for i in range(N):
        for j in range(M):
            if inp[i][j] in "[O":
                res += 100 * i + j
    return res


print(solve(inp))

large_inp = []
for row in inp:
    new = []
    for c in row:
        match c:
            case "#":
                new.extend("##")
            case "O":
                new.extend("[]")
            case ".":
                new.extend("..")
            case "@":
                new.extend("@.")
    large_inp.append(new)

print(solve(large_inp))
