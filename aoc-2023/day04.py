import re

with open("day04.in") as f:
    inp = f.read().strip().split("\n")

ans = 0
count = [1 for _ in range(len(inp))]
for i, row in enumerate(inp):
    nums, vals = row.split(":")[1].split("|")
    nums = set(re.findall(r"\d+", nums))
    vals = set(re.findall(r"\d+", vals))
    n = len(vals.intersection(nums))
    if n > 0:
        ans += 2 ** (n-1)
    for j in range(n):
        count[i + j + 1] += count[i]

print(ans)
print(sum(count))
