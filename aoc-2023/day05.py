with open("day05.in") as f:
    start, *inp = f.read().strip().split("\n\n")

# Problem 1 (RANK 31)

curr = [int(num) for num in start.split()[1:]]

for mapping in inp:
    visited = [False for _ in range(len(curr))]
    for m in mapping.splitlines()[1:]:
        dst, src, rng = [int(num) for num in m.split()]
        for i in range(len(curr)):
            if not visited[i] and src <= curr[i] < src + rng:
                curr[i] += dst - src
                visited[i] = True

print(min(curr))

# Problem 2 (RANK 130, if only I didn't screw up hard...)

curr = [int(num) for num in start.split()[1:]]
curr = set((curr[i], curr[i] + curr[i + 1] - 1) for i in range(0, len(curr), 2))
    
for mapping in inp:
    found = set()
    for m in mapping.splitlines()[1:]:
        dst, src, rng = [int(num) for num in m.split()]
        jmp, src = dst - src, (src, src + rng - 1)
        for (curr_lo, curr_hi) in list(curr):
            lo, hi = max(src[0], curr_lo), min(src[1], curr_hi)
            if lo <= hi:
                curr.remove((curr_lo, curr_hi))
                found.add((lo + jmp, hi + jmp))
                if curr_lo < lo:
                    curr.add((curr_lo, lo - 1))
                if hi < curr_hi:
                    curr.add((hi + 1, curr_hi))
    curr = curr.union(found)

print(min(curr)[0])
