import math

def component_sizes(edges):
    parent = list(range(N))
    size = [1] * N

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)

        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i

            parent[root_j] = root_i
            size[root_i] += size[root_j]
            return True
        return False

    for u, v in edges:
        union(u, v)

    sizes = {}
    for i in range(N):
        root = find(i)
        sizes[root] = size[root]

    return list(sizes.values())

with open("day08.in") as f:
    inp = [tuple(map(int, row.split(","))) for row in f.read().strip().splitlines()]
    N = len(inp)

gaps = []
for i in range(len(inp)):
    for j in range(i + 1, len(inp)):
        (x, y, z) = inp[i]
        (x2, y2, z2) = inp[j]
        d = math.sqrt(abs(x - x2) ** 2 + abs(y - y2) ** 2 + abs(z - z2) ** 2)
        gaps.append((d, i, j))

edges = [(i, j) for (_, i, j) in sorted(gaps)]

sizes = component_sizes(edges[:1000])
sizes = sorted(sizes, reverse=True)[:3]
print(sizes[0] * sizes[1] * sizes[2])

for i in range(1000, len(edges)):
    c = component_sizes(edges[:i])
    if len(c) == 1:
        x, y = edges[i - 1]
        print(inp[x][0] * inp[y][0])
        break
