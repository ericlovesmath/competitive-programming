with open("day04.in") as f:
    inp = f.read().strip().split("\n")

ans = 0
count = [1 for _ in range(len(inp))]
for i, row in enumerate(inp):
    nums, vals = row.split(":")[1].split("|")
    nums, vals = set(nums.split()), set(vals.split())
    n = len(nums.intersection(vals))
    if n > 0:
        ans += 2 ** (n - 1)
    for j in range(n):
        count[i + j + 1] += count[i]

print(ans)
print(sum(count))
