with open("day03.in") as f:
    inp = [list(row) for row in f.read().strip().split("\n")]

# Matrix, Stores (Num, [Hashable Data])
# This means that if we store all neighbors of special characters in a set,
# We will get unique numbers surrounding it even when numbers repeat or span
# over multiple neighboring squares

# Note: Code requires input to have an extra
# border of "." added to remove edge cases (I'm lazy)

def entries():
    for x in range(len(inp)):
        for y in range(len(inp[0])):
            yield (x, y)

nums = {}

curr_id = []
curr_num = 0
for (x, y) in entries():
    if inp[x][y].isdigit():
        curr_num = curr_num * 10 + int(inp[x][y])
        curr_id.append((x, y))
    elif curr_num != 0:
        for (xc, yc) in curr_id:
            nums[(xc, yc)] = (curr_num, x, y)
        curr_num = 0
        curr_id = []

def numeric_neighbors(x, y):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (x + dx, y + dy) in nums:
                yield nums[(x + dx, y + dy)]

# Problem 1

adj_nums = set()
for (x, y) in entries():
    if not inp[x][y].isdigit() and inp[x][y] != ".":
        for num in numeric_neighbors(x, y):
            adj_nums.add(num)
print(sum(num[0] for num in adj_nums))

# Problem 2

ans = 0
for (x, y) in entries():
    if inp[x][y] == "*":
        ratios = set()
        for num in numeric_neighbors(x, y):
            ratios.add(num)
        if len(ratios) == 2:
            a, b = list(ratios)
            ans += a[0] * b[0]
print(ans)
