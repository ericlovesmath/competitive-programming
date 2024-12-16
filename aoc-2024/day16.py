import networkx as nx

with open("day16.in") as f:
    inp = [list(s) for s in f.read().strip().splitlines()]
    N = len(inp)

    S = (N - 2) + 1j
    E = 1 + (N - 2) * 1j
    free = set()
    for i in range(N):
        for j in range(N):
            if inp[i][j] != "#":
                free.add(i + 1j * j)

# Shortest path, where moving straight is not penalized
G = nx.DiGraph()
for c in free:
    for dir in [1, -1, 1j, -1j]:
        d = 0
        while c + d * dir in free:
            weight = 1000 + d
            if c == S and dir == 1j:
                weight = d
            G.add_edge(c, c + d * dir, weight=weight)
            d += 1

distance, _ = nx.single_source_dijkstra(G, S, E, weight="weight")
print(distance)

paths = nx.all_shortest_paths(G, S, target=E, weight="weight")
res = set()
for path in paths:
    # Add all points in between straight lines
    for (a, b) in zip(path, path[1:]):
        d = b - a
        n = abs(d)
        d = d / n
        for i in range(int(n + 1)):
            res.add(a + i * d)
print(len(res))
