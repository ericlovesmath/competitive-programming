with open("day11.in") as f:
    inp = f.read().strip().splitlines()
    N, M = len(inp), len(inp[0])

# Rank 57 + 58!

row_gap = set(i for i in range(M) if all(inp[i][j] == "." for j in range(M)))
col_gap = set(j for j in range(M) if all(inp[i][j] == "." for i in range(N)))

def get_distances(offset):
    stars = set()
    offset_i = 0
    for i in range(N):
        if i in row_gap:
            offset_i += offset
        offset_j = 0
        for j in range(M):
            if j in col_gap:
                offset_j += offset
            if inp[i][j] == "#":
                stars.add((i + offset_i, j + offset_j))

    dists = 0
    for a in stars:
        for b in stars:
            dists += abs(a[0] - b[0]) + abs(a[1] - b[1])
    return dists // 2

print(get_distances(1))
print(get_distances(1_000_000 - 1))
