with open("day07.in") as f:
    inp = [int(i) for i in f.read().strip().split(",")]

def tri(i):
    return (i * i + i) // 2

# Remove tri() for Part 1
print(min(sum(tri(abs(i - d)) for i in inp) for d in range(2000)))
