import re

with open("day03.in") as f:
    inp = f.read().strip()

pat = r"mul\((\d+),(\d+)\)"

res = re.findall(pat, inp)
print(sum(int(i) * int(j) for (i, j) in res))

cut = ""
save = True
for i in range(len(inp)):
    if inp[i:i+4] ==  "do()":
        save = True
    if inp[i:i+7] ==  "don't()":
        save = False
    if save:
        cut += inp[i]

res = re.findall(pat, cut)
print(sum(int(i) * int(j) for (i, j) in res))
