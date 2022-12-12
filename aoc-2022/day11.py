import re
import math

with open("day11.in") as f:
    inp = [rules.split("\n") for rules in f.read().strip().split("\n\n")]

monkeys = [
    {
        "items": list(map(int, re.findall(r"\d+", monkey[1]))),
        "rule": monkey[2][19:],
        "test": int(monkey[3][21:]),
        "pass": int(monkey[4][29:]),
        "fail": int(monkey[5][30:]),
        "inspections": 0
    }
    for monkey in inp
]

worry_cap = math.lcm(*[monkey["test"] for monkey in monkeys])

for _ in range(10000):
    for monkey in monkeys:
        while monkey["items"]:
            monkey["inspections"] += 1
            item = monkey["items"].pop(0)
            # item = eval(monkey["rule"].replace("old", str(item))) // 3
            item = eval(monkey["rule"].replace("old", str(item))) % worry_cap
            if item % monkey["test"] == 0:
                monkeys[monkey["pass"]]["items"].append(item)
            else:
                monkeys[monkey["fail"]]["items"].append(item)

inspections = sorted([monkey["inspections"] for monkey in monkeys])
print(inspections[-1] * inspections[-2])

