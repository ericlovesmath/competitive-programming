with open("day16.in") as f:
    inp = f.read().strip().splitlines()
    N = len(inp)

def count_energized(start):
    currs: list[tuple[int, int, int, int]] = [start]
    visited = set()
    energized = set()

    while len(currs) > 0:
        curr = currs.pop()
        x, y, dx, dy = curr
        if not (0 <= x < N and 0 <= y < N):
            continue
        if curr in visited:
            continue
        visited.add(curr)
        energized.add((x, y))

        match inp[x][y]:
            case ".":
                currs.append((x + dx, y + dy, dx, dy))
            case "/":
                currs.append((x - dy, y - dx, -dy, -dx))
            case "\\":
                currs.append((x + dy, y + dx, dy, dx))
            case "|":
                if dy == 0:
                    currs.append((x + dx, y + dy, dx, 0))
                else:
                    currs.append((x - 1, y, -1, 0))
                    currs.append((x + 1, y, 1, 0))
            case "-":
                if dx == 0:
                    currs.append((x + dx, y + dy, 0, dy))
                else:
                    currs.append((x, y - 1, 0, -1))
                    currs.append((x, y + 1, 0, 1))

    return len(energized)

print(count_energized((0, 0, 0, 1)))

ans = 0
for i in range(N):
    ans = max(
        ans,
        count_energized((i, 0, 0, 1)),
        count_energized((i, N - 1, 0, -1)),
        count_energized((0, i, 1, 0)),
        count_energized((N - 1, i, -1, 0)),
    )

print(ans)
