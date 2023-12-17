from heapq import heappop, heappush

with open("day17.in") as f:
    inp = [[int(n) for n in row] for row in f.read().strip().splitlines()]
    N = len(inp)


def get_loss(min, max):
    heap = [(0, 0, 0, (None, None))]  # loss, x, y, prev_dir

    visited = set()
    losses = {}
    while heap:
        loss, x, y, prev_dir = heappop(heap)

        if x == N - 1 and y == N - 1:
            return loss
        if (x, y, prev_dir) in visited:
            continue
        visited.add((x, y, prev_dir))

        for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dir[0] == prev_dir[0] or dir[1] == prev_dir[1]:
                continue

            dloss = 0
            for dist in range(1, max + 1):
                i, j = x + dir[0] * dist, y + dir[1] * dist
                if not (0 <= i < N and 0 <= j < N):
                    continue
                dloss += inp[i][j]
                if dist >= min and loss + dloss < losses.get((i, j, dir), float("inf")):
                    losses[(i, j, dir)] = loss + dloss
                    heappush(heap, (loss + dloss, i, j, dir))


print(get_loss(1, 3))
print(get_loss(4, 10))
