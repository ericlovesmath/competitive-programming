import networkx as nx

with open("day23.in") as f:
    inp = [(row[:2], row[3:]) for row in f.read().strip().splitlines()]
    G = nx.Graph(inp)

cliques = list(nx.find_cliques(G))

res = set()
for clique in cliques:
    for i in range(len(clique)):
        for j in range(i + 1, len(clique)):
            for k in range(j + 1, len(clique)):
                a, b, c = clique[i], clique[j], clique[k]
                if "t" in (a[0], b[0], c[0]) and \
                    G.has_edge(a, b) and G.has_edge(b, c) and G.has_edge(c, a):
                    res.add((a, b, c))
print(len(res))

print(",".join(sorted(max(cliques, key=len))))
