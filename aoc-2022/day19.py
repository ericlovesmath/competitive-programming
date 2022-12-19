import re
import sys
from functools import cache

with open("day19.in") as f:
    blueprints = []
    for blueprint in f.read().strip().splitlines():
        costs = list(map(int, re.findall(r"\d+", blueprint)))
        # cost = [[C1, 0, 0, 0], [C2, 0, 0, 0], [C3, C4, 0, 0], [C5, 0, C6, 0]]
        blueprints.append(tuple(costs[1:]))


# This is the most toxic bad code I've written
# But it got me rank 85 so *yeay*
# This ran for a solid 30 minutes
# If this didn't give me the right answer I was going to give up

sys.setrecursionlimit(100000000)  # Ignore me please


@cache
def simulate(robots, resources, time, blueprint, building) -> int:
    resources = list(resources)  # List-Tuple for Caching

    time -= 1
    if time == 0:
        return resources[3]
    resources = [resources[i] + robots[i] for i in range(4)]

    if building != -1:
        robots = list(robots)
        robots[building] += 1
        robots = tuple(robots)
        building = -1

    T = simulate(robots, tuple(resources), time, blueprint, -1)

    # Ore Bot
    if resources[0] >= blueprint[0]:
        new_resources = resources.copy()
        new_resources[0] -= blueprint[0]
        T = max(simulate(robots, tuple(new_resources), time, blueprint, 0), T)

    # Clay Bot
    if resources[0] >= blueprint[1]:
        new_resources = resources.copy()
        new_resources[0] -= blueprint[1]
        T = max(simulate(robots, tuple(new_resources), time, blueprint, 1), T)

    # Obsidian Bot
    if resources[0] >= blueprint[2] and resources[1] >= blueprint[3]:
        new_resources = resources.copy()
        new_resources[0] -= blueprint[2]
        new_resources[1] -= blueprint[3]
        T = max(simulate(robots, tuple(new_resources), time, blueprint, 2), T)

    # Geode Bot
    if resources[0] >= blueprint[4] and resources[2] >= blueprint[5]:
        new_resources = resources.copy()
        new_resources[0] -= blueprint[4]
        new_resources[2] -= blueprint[5]
        T = max(simulate(robots, tuple(new_resources), time, blueprint, 3), T)

    return T


P1 = 0
P2 = 1
for i, blueprint in enumerate(blueprints):
    P1 += (i + 1) * simulate((1, 0, 0, 0), (0, 0, 0, 0), 24, blueprint, -1)
    if i < 3:
        P2 *= simulate((1, 0, 0, 0), (0, 0, 0, 0), 32, blueprint, -1)

print(P1, P2)
