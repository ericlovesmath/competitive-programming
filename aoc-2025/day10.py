with open("day10.in") as f:
    inp = f.read().strip().splitlines()

# Part 1: Brute force

def combos(xs):
    if len(xs) == 0:
        yield []
    else:
        for rem in combos(xs[1:]):
            yield [xs[0]] + rem
            yield rem

def check(state, switches):
    if len(switches) == 0:
        return not any(state)
    else:
        for i in switches[0]:
            state[i] = not state[i]
        return check(state, switches[1:])

total = 0
for row in inp:
    lights, *switches, _ = [s[1:-1] for s in row.split()]
    lights = [c == "#" for c in lights]
    switches = [list(map(int,s.split(","))) for s in switches]

    ans = float("inf")
    for case in combos(switches):
        if check(lights.copy(), case):
            ans = min(len(case), ans)
    total += ans

print(total)


# Part 2: Linear constraint optimization

from z3 import *

total = 0
for row in inp:
    _, *switches, joltages = [s[1:-1] for s in row.split()]
    switches = [list(map(int, s.split(","))) for s in switches]
    joltages = list(map(int, joltages.split(",")))

    opt = Optimize()

    switch_vars = [Int(f"s{i}") for i in range(len(switches))]

    for s in switch_vars:
        opt.add(s >= 0)

    for j, jolt in enumerate(joltages):
        can_jolt = [i for (i, switch) in enumerate(switches) if j in switch]
        can_jolt_vars = [switch_vars[i] for i in can_jolt]
        opt.add(sum(can_jolt_vars) == jolt)

    opt.minimize(sum(switch_vars))
    if opt.check() == sat:
        model = opt.model()
        res = model.evaluate(sum(switch_vars))
        assert isinstance(res, IntNumRef)
        total += res.as_long()
    else:
        print("Error: No solution")

print(total)
