import sys
from collections import deque
from math import lcm

with open("day20.in") as f:
    inp = f.read().strip().splitlines()

# Part 1: 363,  Part 2: 155
# Not a fan of this problem

broadcaster = deque()
flips, conjs = {}, {}
for row in inp:
    l, r = row.split(" -> ")
    r = r.split(", ")
    if l[0] == "%":
        flips[l[1:]] = (False, r)  # State, Module
    elif l[0] == "&":
        conjs[l[1:]] = ({}, r)  # History, Module
    else:
        for module in r:
            broadcaster.append(("broadcast", False, module))

cycles = {}
for row in inp:
    l, r = row.split(" -> ")
    mod = l if l == "broadcast" else l[1:]
    for out in r.split(", "):
        if out in conjs:
            conjs[out][0][mod] = False
        if out == "vf":
            cycles[mod] = 0

pulses = [0, 0]
for i in range(1, sys.maxsize):
    pulses[False] += 1
    queue = broadcaster.copy()
    while len(queue) > 0:
        prev, freq, mod = queue.popleft()

        # If `hit` is triggered twice, it saves the cycle length
        # Manually, we see only &vf -> rx
        # We take the LCM of the cycles it takes for each of &vf's predecessors
        # to send &vf a HIGH then LOW signal
        # Turns out that they all cycle starting at 0 though
        # I don't like this type of problem where I need to guess the input type
        if freq == False and mod in cycles:
            if cycles[mod] == 0:
                cycles[mod] = i
        if all(cycle > 0 for cycle in cycles.values()):
            print("Part 2:", lcm(*cycles.values()))
            sys.exit()

        # Directly simulate button presses for Part 1
        pulses[freq] += 1
        if mod in conjs:
            hist, nexts = conjs[mod]
            hist[prev] = freq
            for next in nexts:
                queue.append((mod, not all(hist.values()), next))
        elif mod in flips and freq == False:
            state, nexts = flips[mod]
            flips[mod] = (not state, nexts)
            for next in nexts:
                queue.append((mod, not state, next))

    if i == 1000:
        print("Part 1:", pulses[0] * pulses[1])
