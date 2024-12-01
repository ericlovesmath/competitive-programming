from collections import defaultdict

with open("day01.in") as f:
    inp = f.read().strip().split("\n")

ls = [int(row.split()[0]) for row in inp]
rs = [int(row.split()[1]) for row in inp]

ls.sort()
rs.sort()

print(sum(abs(ls[i] - rs[i]) for i in range(len(ls))))

freq = defaultdict(int)
for r in rs:
    freq[r] += 1

print(sum(l * freq[l] for l in ls))
