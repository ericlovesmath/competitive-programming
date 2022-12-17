import re
from functools import lru_cache

with open("day16.in") as f:
    tunnel = {}
    flow = {}
    for row in f.read().strip().splitlines():
        valve, rate, *to = re.findall(r"[A-Z]{2}|\d+", row)
        tunnel[valve] = set(to)
        flow[valve] = int(rate)


@lru_cache(maxsize=None)
def simulate(curr, time, open):
    if time <= 0:
        return 0

    P = 0

    if curr not in open:
        new_flow = flow[curr] * (time - 1)
        new_open = tuple(sorted(open + (curr,)))  # Tuple so that I can cache

        for target in tunnel[curr]:
            P = max(simulate(target, time - 1, open), P)
            if flow[curr] != 0:
                P = max(new_flow + simulate(target, time - 2, new_open), P)

    return P


pressure = simulate("AA", 30, ())
print(pressure)

# Construct directed graph between weights
# Distance represents time to take
# 0 chance this bad caching solution will work for part 2
# I give up for now

@lru_cache(maxsize=None)
def sim_2(human, elephant, time, open):
    if time <= 0:
        return 0

    P = 0

    if human not in open:
        new_flow = flow[human] * (time - 1)
        new_open = tuple(sorted(open + (human,)))

        for target in tunnel[human]:
            P = max(sim_2(target, elephant, time - 1, open), P)
            if flow[human] != 0:
                P = max(new_flow + sim_2(target, elephant, time - 2, new_open), P)
    if elephant not in open:
        new_flow = flow[elephant] * (time - 1)
        new_open = tuple(sorted(open + (elephant,)))

        for target in tunnel[elephant]:
            P = max(sim_2(human, target, time - 1, open), P)
            if flow[elephant] != 0:
                P = max(new_flow + sim_2(human, target, time - 2, new_open), P)

    return P

pressure = sim_2("AA", "AA", 26, ())
print(pressure)
