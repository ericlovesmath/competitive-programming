with open("day01.in") as f:
    inp = list(map(int, f.read().strip().split()))

print(sum(inp[i] < inp[i + 1] for i in range(len(inp) - 1)))
print(sum(inp[i] < inp[i + 3] for i in range(len(inp) - 3)))
