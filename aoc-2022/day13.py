with open("day13.in") as f:
    inp = f.read().strip().split("\n\n")


def compare(left, right):
    match (isinstance(left, int), isinstance(right, int)):
        case (True, True):
            return left - right
        case (True, False):
            return compare([left], right)
        case (False, True):
            return compare(left, [right])
        case (False, False):
            for x, y in zip(left, right):
                if val := compare(x, y):
                    return val
            return len(left) - len(right)


total = 0
for i in range(len(inp)):
    left, right = map(eval, inp[i].split())
    if compare(left, right) < 0:
        total += i + 1

print(total)

with open("day13.in") as f:
    inp = [eval(row) for row in f.read().strip().split("\n") if row != ""]

two_div = 1
six_div = 2

for row in inp:
    if compare(row, [[2]]) < 0:
        two_div += 1
        six_div += 1
    elif compare(row, [[6]]) < 0:
        six_div += 1

print(two_div * six_div)
