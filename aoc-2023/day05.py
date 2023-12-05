with open("day05.in") as f:
    start, *inp = f.read().strip().split("\n\n")
    start = [int(num) for num in start.split()[1:]]
    N = len(start)

# Problem 1 (RANK 31)

curr = start.copy()

for mapping in inp:
    visited = [False for _ in range(N)]
    for m in mapping.splitlines()[1:]:
        dst, src, rng = [int(num) for num in m.split()]
        for i in range(N):
            if not visited[i] and src <= curr[i] < src + rng:
                curr[i] += dst - src
                visited[i] = True

print(min(curr))

# Problem 2 (RANK 130, if only I didn't screw up hard...)

curr = set((start[i], start[i] + start[i + 1] - 1) for i in range(0, N, 2))

for mapping in inp:
    found = set()
    for m in mapping.splitlines()[1:]:
        dst, src, rng = [int(num) for num in m.split()]
        for (lo, hi) in list(curr):
            map_lo, map_hi = max(src, lo), min(src + rng - 1, hi)
            if map_lo <= map_hi:
                curr.remove((lo, hi))
                found.add((map_lo + dst - src, map_hi + dst - src))
                if lo < map_lo:
                    curr.add((lo, map_lo - 1))
                if map_hi < hi:
                    curr.add((map_hi + 1, hi))
    curr = curr.union(found)

print(min(curr)[0])
