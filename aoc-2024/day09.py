with open("day09.in") as f:
    inp = f.read().strip()
    inp = [int(i) for i in inp] + [1]
    inp = [inp[i:i+2] for i in range(0, len(inp), 2)]

# Part 1

state = []
for i, (n, gap) in enumerate(inp):
    state.extend([i for _ in range(n)])
    state.extend([None for _ in range(gap)])

l = 0
r = len(state) - 1
while True:

    while state[l] != None:
        l += 1

    while state[r] == None:
        r -= 1

    if l > r:
        break

    state[l], state[r] = state[r], state[l]

print(sum(i * n for i, n in enumerate(state) if n is not None))


# Part 2

state = []
for i, (n, gap) in enumerate(inp):
    state.extend([i for _ in range(n)])
    state.extend([None for _ in range(gap)])

r = len(state) - 1

for x in range(len(inp) - 1, -1, -1):
    # Only have to search for start of new block 2 * 10 back
    r = max(r - 20, 0)
    while state[r] != x:
        r += 1

    d = 0
    while state[r] == state[r + d]:
        d += 1

    # Searching for gap has to have a better solution, but splitting seems
    # complicated to implement and pypy makes this fast enough (~3s)
    l = state.index(None)
    while any(i != None for i in state[l:l + d]):
        l += 1

    if l <= r:
        state[l:l + d], state[r:r + d] = state[r:r + d], state[l: l + d]

print(sum(i * n for i, n in enumerate(state) if n is not None))
