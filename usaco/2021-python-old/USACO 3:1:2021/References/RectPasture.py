"""
ID: dazzlethelightwing
LANG: PYTHON3
TASK: Rectangular Pasture
"""
import math

n = int(input())

adj = [[] for i in range(n)]

for i in range(n-1):
    line = map(int, input().split(" "))
    adj[line[0]-1].append(line[1]-1)
    adj[line[1]-1].append(line[0]-1)

def process(curr, parent, adj):
    children = 0
    cost = 0
    for i in adj[curr]:
        if i == parent:
            continue
    children += 1
    cost += process(i, curr, adj)
    cost += children + children.bit_length()
    return cost

print(process(0, -1, adj))

# Notes
#somelist.sort(key=lambda x: x[2]) # sorts list by second item in sub lists