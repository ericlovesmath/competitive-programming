import numpy as np

with open("day13.in") as f:
    raw = f.read().strip().split("\n\n")
    inps = [np.array([list(s) for s in inp.splitlines()]) for inp in raw]

def score(inp, change):
    N = len(inp)
    for i in range(1, N):
        widths = range(0, min(i, N - i))
        diffs = np.sum([inp[i - j - 1] != inp[i + j] for j in widths]) 
        if diffs == change:
            return i
    return 0

# Rank 290 + 227

print(sum(100 * score(inp, 0) + score(inp.transpose(), 0) for inp in inps))
print(sum(100 * score(inp, 1) + score(inp.transpose(), 1) for inp in inps))
