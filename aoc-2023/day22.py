from collections import defaultdict

with open("day22.in") as f:
    bricks = [
        [[int(num) for num in end.split(",")] for end in line.split("~")]
        for line in f.read().strip().splitlines()
    ]
    N = len(bricks)

bricks.sort(key=lambda x: x[0][2])

highest: defaultdict[tuple[int, int], tuple[int, int]] = defaultdict(
    lambda: (0, -1)
)
bad = set()
graph = [[] for _ in range(N)]  # Remembers chain reaction
for i, brick in enumerate(bricks):
    max_height = -1
    supports = set()
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if highest[(x, y)][0] + 1 > max_height:
                max_height = highest[(x, y)][0] + 1
                supports = {highest[(x, y)][1]}
            elif highest[(x, y)][0] + 1 == max_height:
                supports.add(highest[(x, y)][1])

    for x in supports:
        if x != -1:
            graph[x].append(i)

    if len(supports) == 1:
        bad.add(supports.pop())

    fall = brick[0][2] - max_height
    if fall > 0:
        brick[0][2] -= fall
        brick[1][2] -= fall

    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            highest[(x, y)] = (brick[1][2], i)

print(len(bricks) - len(bad) + 1)


def count(idx, graph):
    indeg = [0 for _ in range(N)]
    for j in range(N):
        for i in graph[j]:
            indeg[i] += 1
    q = [idx]
    count = -1
    while len(q) > 0:
        count += 1
        x = q.pop()
        for i in graph[x]:
            indeg[i] -= 1
            if indeg[i] == 0:
                q.append(i)

    return count


print(sum(count(x, graph) for x in range(N)))
