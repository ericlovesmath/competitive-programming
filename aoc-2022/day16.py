import re
from functools import cache

with open("day16.in") as f:
    tunnel = {}
    flow = {}
    for row in f.read().strip().splitlines():
        valve, rate, *to = re.findall(r"[A-Z]{2}|\d+", row)
        tunnel[valve] = set(to)
        flow[valve] = int(rate)


@cache
def simulate(curr, time, open, again):
    if time <= 0:
        if again:
            return simulate("AA", 26, open, False)
        return 0

    P = 0

    if curr not in open:
        new_flow = flow[curr] * (time - 1)
        new_open = tuple(sorted(open + (curr,)))  # Tuple so that I can cache

        for target in tunnel[curr]:
            P = max(simulate(target, time - 1, open, again), P)
            if flow[curr] != 0:
                P = max(
                    new_flow + simulate(target, time - 2, new_open, again), P
                )

    return P


print(simulate("AA", 30, (), False))
print(simulate("AA", 26, (), True))
