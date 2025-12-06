with open("day06.in") as f:
    *nums, ops = f.read().splitlines()
    nums = [[int(i) for i in row.split()] for row in nums]
    ops = ops.split()
    N = len(ops)

def run(op, curr):
    if op == "*":
        c = 1
        for n in curr:
            c *= n
        return c
    if op == "+":
        c = 0
        for n in curr:
            c += n
        return c
    return 0

print(sum(run(ops[i], [row[i] for row in nums]) for i in range(N)))

with open("day06.in") as f:
    *nums, ops = f.read().splitlines()
    nums = [row + " " for row in nums]
    ops = ops + " "
    N = len(ops)

op = ""
res = 0
curr = []
for i in range(len(ops)):
    if ops[i] != " ":
        op = ops[i]
    col = "".join([row[i] for row in nums])
    if len(col.strip()) == 0:
        res += run(op, curr)
        curr = []
    else:
        curr.append(int(col))
print(res)
