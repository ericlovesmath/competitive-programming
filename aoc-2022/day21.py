from sympy import solve, symbols

monkeys = {}
unknown = {}
SIZE = 0

with open("day21.in") as f:
    for row in f.read().strip().splitlines():
        SIZE += 1
        monkey, rule = row.split(": ")
        if rule.isdecimal():
            monkeys[monkey] = int(rule)
        else:
            left, op, right = rule.split()
            unknown[monkey] = (left, op, right)

# Part 1 must be commented before Part 2 works

while len(unknown.keys()) > 0:
    for monkey in unknown.copy().keys():
        left, op, right = unknown[monkey]
        if left in monkeys and right in monkeys:
            monkeys[monkey] = int(
                eval(f"monkeys['{left}'] {op} monkeys['{right}']")
            )
            del unknown[monkey]

print(monkeys["root"])


def get_exp(expression):
    # Is this cheating? Using Sympy? Yes.

    ans = []
    for exp in expression:
        if exp == "humn":
            ans.append("x")
        elif exp.isdecimal() or exp in "()*/-+":
            ans.append(exp)
        elif exp in monkeys:
            ans.append(str(monkeys[exp]))
        elif exp in unknown:
            ans.append("(")
            ans.extend(get_exp(unknown[exp]))
            ans.append(")")

    return ans


left = "".join(get_exp([unknown["root"][0]]))
right = "".join(get_exp([unknown["root"][2]]))

x = symbols("x")
print(round(eval(f"solve({left}-{right})")[0]))
