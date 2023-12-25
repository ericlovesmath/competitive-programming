import sys
import networkx as nx

with open("day25.in") as f:
    inp = f.read().strip().splitlines()
    N = len(inp)

# I downloaded networkx for this problem don't judge me
# Rank 77 + 68

nodes = [row[:3] for row in inp]

G = nx.Graph()
G.add_nodes_from(nodes)
for row in inp:
    for node in row.split(" ")[1:]:
        G.add_edge(row[:3], node, capacity=1)

for i in range(N):
    for j in range(i + 1, N):
        cut_size, (cut_l, cut_r) = nx.minimum_cut(G, nodes[i], nodes[j])
        if cut_size == 3:
            print(len(cut_l) * len(cut_r))
            sys.exit(0)
