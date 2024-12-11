from collections import defaultdict

with open("day11.in") as f:
    inp = [int(i) for i in f.read().strip().split()]

state = {i : 1 for i in inp}

for _ in range(75):
    next = defaultdict(int)
    for n in state:
        if n == 0:
            next[1] += state[n]
        elif len(str(n)) % 2 == 0:
            l = len(str(n)) // 2
            next[n // (10 ** l)] += state[n]
            next[n % (10 ** l)] += state[n]
        else:
            next[n * 2024] += state[n]
    state = next

print(sum(state.values()))
