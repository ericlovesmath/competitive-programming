with open("day02.in") as f:
    inp = f.read().strip().split("\n")
    inp = [[int(i) for i in row.split()] for row in inp]

def ans(row):
    if row != sorted(row) and row != sorted(row, reverse=True):
        return False

    for i in range(len(row) - 1):
        d = abs(row[i] - row[i+1])
        if d < 1 or d > 3:
            return False

    return True

print(sum(ans(row) for row in inp))

res = 0
for row in inp:
    flag = False
    for i in range(len(row)):
        if ans(row[:i] + row[i+1:]):
            flag = True
    if ans(row):
        flag = True
    if flag:
        res += 1
print(res)
